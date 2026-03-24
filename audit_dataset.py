import json, glob, re
from pathlib import Path

def classify(q):
    text=(q['questionText']+' '+q['explanation']).lower()
    types=set()
    if any(x in text for x in ['patient','pregnant','child','infant','postoperative','woman','man with','neonate']):
        types.add('clinical_vignette')
    if 'except' in q['questionText'].lower() or 'all except' in q['questionText'].lower():
        types.add('exception_based')
    if any(x in text for x in ['mechanism','acts by','rate-limiting','cofactor','mediated by']):
        types.add('mechanism_based')
    if any(x in text for x in ['which of the following','most likely','characteristic of','hallmark']):
        types.add('direct_recall')
    if any(x in text for x in ['lab','osmolality','d-dimer','abg','culture','indole','x-ray','ecg','pressure curve']):
        types.add('lab_or_image_interpretation')
    if any(x in text for x in ['contraindication','adverse effect','interaction','toxic']):
        types.add('drug_response_or_interaction')
    if not types:
        types.add('direct_recall')
    return sorted(types)

syllabus=json.load(open('dataset/syllabus_map.json'))
subject_chapters={}
question_count=0
subject_count=0
chapter_count=0
questions=[]
for path in glob.glob('dataset/**/*.json', recursive=True):
    if path.endswith('manifest.json') or path.endswith('syllabus_map.json'): continue
    d=json.load(open(path))
    subject=d['subject']
    chapter=d['chapter']
    subject_chapters.setdefault(subject,[]).append(chapter)
    chapter_count += 1
    for q in d['questions']:
        qtypes=classify(q)
        questions.append((subject,chapter,qtypes,q['difficulty']))
        question_count += 1
subject_count=len(subject_chapters)

expected_subjects=set(syllabus)
subject_coverage=subject_count/len(expected_subjects)
expected_chapters=sum(len(v) for v in syllabus.values())
chapter_coverage=chapter_count/expected_chapters
avg_q_per_chapter=question_count/chapter_count

type_counts={}
difficulty_counts={}
for _,_,qtypes,diff in questions:
    for t in qtypes:
        type_counts[t]=type_counts.get(t,0)+1
    difficulty_counts[diff]=difficulty_counts.get(diff,0)+1

def pct(n,d): return round(100*n/d,1) if d else 0

subject_gap={s: sorted(set(chs)-set(subject_chapters.get(s,[]))) for s,chs in syllabus.items()}
priority_subjects=['General Medicine','General Surgery','Obstetrics and Gynecology','Pediatrics','Pathology','Pharmacology','Microbiology','Anatomy','Physiology','Community Medicine']
priority_missing={s: subject_gap[s] for s in priority_subjects if subject_gap.get(s)}

score = round(subject_coverage*35 + chapter_coverage*35 + min(avg_q_per_chapter/15,1)*15 + min(len(type_counts)/6,1)*15,1)
report={
    'subjects_present': subject_count,
    'subjects_expected': len(expected_subjects),
    'subject_coverage_pct': pct(subject_count,len(expected_subjects)),
    'chapters_present': chapter_count,
    'chapters_expected': expected_chapters,
    'chapter_coverage_pct': pct(chapter_count, expected_chapters),
    'questions_present': question_count,
    'average_questions_per_chapter': round(avg_q_per_chapter,2),
    'difficulty_distribution_pct': {k: pct(v, question_count) for k,v in sorted(difficulty_counts.items())},
    'question_type_signals_pct': {k: pct(v, question_count) for k,v in sorted(type_counts.items())},
    'neet_pg_alignment_score_out_of_100': score,
    'rating': ('poor' if score < 40 else 'basic' if score < 60 else 'developing' if score < 75 else 'strong'),
    'priority_missing_chapters': priority_missing,
}
Path('research').mkdir(exist_ok=True)
json.dump(report, open('research/coverage_audit.json','w'), indent=2)
print(json.dumps(report, indent=2))
