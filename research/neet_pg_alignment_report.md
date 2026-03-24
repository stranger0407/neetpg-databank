# NEET PG / INI-CET dataset alignment review

## Research basis
This review compares the repository dataset against:

1. The standard MBBS/NEET PG subject spread reflected in the NMC undergraduate curriculum framework.
2. The broad subject-comprehensive, integrated, single-best-answer pattern used in NEET PG and INI-CET style preparation.
3. High-yield exam features repeatedly emphasized in mainstream preparation patterns: clinical vignettes, lab interpretation, mechanism-based traps, image/radiology-pathology correlation, and integrated pharmacology/pathology/microbiology questions.

Reference links used for the research pass:
- National Medical Commission curriculum portal / MBBS curriculum resources: https://www.nmc.org.in
- AIIMS examination information / prospectus portal for INI-CET pattern context: https://www.aiimsexams.ac.in/info/Prospectus.html
- National Board/NBEMS NEET PG exam portal (challenge-protected at time of review, so used only as a corroborative source target): https://natboard.edu.in/viewnbeexam?exam=neetpg

## What was audited in the repository
- `dataset/syllabus_map.json` as the target chapter map.
- All generated chapter JSON files under `dataset/`.
- The generator in `generate_dataset.py`.
- Automated scoring output in `research/coverage_audit.json`.

## Current measured status
From the automated audit:
- Subjects represented: 20 / 20.
- Chapter files present: 37 / 170 mapped chapters.
- Questions present: 111.
- Average questions per chapter: 3.0.
- Difficulty mix: EASY 31.5%, MEDIUM 53.2%, HARD 15.3%.
- Type signals: direct recall dominant at 67.6%, clinical vignette 23.4%, lab/image 9.9%, mechanism 4.5%, exception-based 1.8%, drug interaction 9.9%.
- Overall alignment score: 60.6 / 100.
- Overall rating: Developing.

## How close is this to a true NEET PG-complete dataset?
### Strengths
- All major NEET PG subject buckets are now represented.
- The JSON schema is consistent and parseable.
- Questions are mostly one-best-answer style and use plausible distractors.
- Several chapters already include clinically framed stems and high-yield traps.
- Textbook source attribution exists for each item.

### Gaps keeping it far from a true exam-complete bank
1. Chapter coverage is still low.
   - Only 21.8% of the mapped chapter inventory currently has a chapter file.
   - Big exam-weight subjects still have major uncovered sections, especially Medicine, Surgery, OBG, Pediatrics, Pathology, Pharmacology, Anatomy, Physiology, and Community Medicine.

2. Question density per chapter is too thin.
   - Three questions per chapter is not enough for revision-level coverage.
   - A realistic revision-grade chapter bank usually needs at least 12-25 questions for small chapters and substantially more for large, high-weight chapters.

3. Question-type diversity is still underpowered.
   - The bank remains heavily recall-weighted.
   - NEET PG/INI-CET style preparation needs more clinical vignettes, image/radiology/pathology prompts, interpretation-based items, and multi-step mechanism questions.

4. Hard-question proportion is below target.
   - The requested target was about 30% hard; current hard share is 15.3%.
   - This means the bank is not yet stress-testing differentiating concepts well enough.

5. Integrated chapter design remains incomplete.
   - Many chapters do not yet include anatomy-radiology, pathology-pharmacology, microbiology-treatment, or lab-clinical correlation layers within the same file.

## Rating interpretation
### Practical rating
- Syllabus breadth representation: 8/10 for subjects, 2/10 for chapter completion.
- Question-type realism: 5/10.
- Exam readiness for final revision: 4/10.
- Data structure quality: 8/10.
- Overall current usefulness: 6/10.

### Final verdict
The dataset is **developing but not yet close to true NEET PG completeness**.
A fair evidence-based rating is **60.6/100** right now.

## Improvements started in this revision
This iteration begins closing the gap by adding new chapter files in high-value areas:
- Anatomy: Head and Neck
- Physiology: Renal Physiology
- Biochemistry: Lipid Metabolism
- Pathology: Hematology
- Pharmacology: CNS Pharmacology
- Microbiology: Immunology
- Community Medicine: Immunization
- General Medicine: Respiratory Medicine
- General Surgery: Shock and Trauma
- Obstetrics and Gynecology: Labor
- Pediatrics: Immunization

This improves the dataset from 26 to 37 chapter files and from 78 to 111 questions.

## Recommended next improvement order
1. Finish large-core chapters in Medicine, Surgery, OBG, Pediatrics, Pathology, Pharmacology, and PSM.
2. Raise question density in already-started chapters from 3 to 12+ each.
3. Add explicit image-based and lab-interpretation blocks for radiology, pathology, anatomy, microbiology, and ophthalmology.
4. Increase hard, trap-heavy questions to reach about 25-30% of the bank.
5. Add more exam-style integrated questions linking diagnosis, investigation, and next-step management.

## Immediate priority missing chapters
The automated audit identified the highest-priority remaining gaps in major subjects inside `research/coverage_audit.json`.
