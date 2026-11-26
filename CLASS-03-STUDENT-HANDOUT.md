# Meeting 3 — Student activity sheet

**Topic:** Docker image versus container; reproducible Flask build

**Time:** 180-minute meeting including a 10-minute break. Follow the facilitator's staged instructions; do not attempt later meetings early.

**Files to use now:** `lab/app.py`, `lab/Dockerfile`, `lab/requirements.txt`, `lab/.dockerignore`, `lab/tests/test_app.py`


## Your task

1. Predict what docker build creates.

2. Build epita-flask:v1 and run on host 8000.

3. Request /, /version and /health, inspect logs and UID. 

4. Edit greeting/version to produce v2; build a second image and run on separate host port.

5. Record both image IDs and responses. 6. Explain one cache hit/miss, then remove classroom containers.

## Submit this evidence

command log or screenshots: distinct greeting responses and image IDs; runtime UID; cache observation; cleanup. Label each item with the step it proves. A screenshot of a green check without the relevant artifact or behaviour is insufficient.

## Completion criteria (visible to students)

10 points: correct v1 build/run 2; genuinely different v2 response and ID 3; UID/port interpretation 2; cache explanation 2; safe cleanup 1. Passing ≥8/10 and distinct artifacts are mandatory.

## When stuck

Record the command or action, expected result, actual result, and your next discriminating check. Do not conceal failures; a well-diagnosed fault can demonstrate more understanding than an unexplained success.
