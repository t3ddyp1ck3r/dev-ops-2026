# CLASS 01 — Student lab handout

## Exercise A — Investigate a failed release (25 minutes)

### Concepts first 

A service can return **HTTP 200** from one endpoint while another returns **HTTP 503**. An HTTP health check proves only the checks that endpoint actually performs. A *hypothesis* is a possible explanation; an *observation* is the evidence used to support or reject it.

### Incident card (synthetic; given facts)

- Unit tests passed before deployment.
- After deployment, `GET /health` returns **200**.
- After deployment, `GET /db-time` returns **503**.
- The incident report says a database-hostname lookup failed. This report is a **scenario clue**, not an actual log you must generate.
- Read `lab/app.py` and find the implementations of `/health` and `/db-time`.

### Your task

Work in pairs. **Do not run or deliberately break the service.** Submit one page with:

1. Which user-visible behaviour is unavailable? Why does the 200 result **not** prove the database works?
2. Three **different** possible causes consistent with the facts (do not declare one confirmed).
3. For each cause, an exact command **or observation** that would help distinguish it. Commands are plans; you are **not required to execute** them today.
4. Which check would you perform first, and why?
5. A safe temporary restoration approach and how you would verify recovery.
6. One change to tests or release checks that could catch this problem earlier.

**Expected submission:** one-page incident note, with a small table of **hypothesis | check | what result would mean**. **Success checklist:** correctly explain both endpoints (2 points), give three distinct plausible hypotheses (3), link each to a useful evidence check (3), propose safe recovery verification (1), and recommend prevention (1). A complete submission earns at least 7/10 and must include accurate endpoint interpretation and evidence-based reasoning. Do not include any passwords.

### Starter example (not one of your three answers)

Possible cause: a firewall blocks the database port. Check: a connection attempt from the running app environment to the configured database host/port; a timeout would support a network-path issue, while a DNS lookup failure suggests investigating name resolution first.

## Exercise B — Understand and calculate lead time (20 minutes)

**Lead time for changes** usually means the time from code committed to successful production deployment. In this simplified classroom scenario, calculate *total elapsed time across the supplied workflow*, including the clarification wait before coding; it is not necessarily identical to the formal commit-to-production metric.

**Worked example:** 10 minutes coding + 20 minutes waiting + 5 minutes deploying = **35 minutes elapsed**, **15 minutes active**, **20 minutes waiting**.

**Case data:** clarification wait 90 min; review queue 180 min; release-window wait 120 min; coding 30 min; active review 20 min; deployment 10 min.

1. Add all waiting periods (minutes).
2. Add all active work periods (minutes).
3. Calculate total elapsed time, also in hours/minutes.
4. Identify the largest single delay.
5. Recommend one specific change and one before/after measure to judge it.

**Passing:** correct totals, bottleneck, improvement and measurable check (at least 4 of these 5 requirements). Clearly distinguish elapsed time from active time.
