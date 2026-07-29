# Checklist 07. The Scoping Gate

**Run before the SOW is signed. Not after. Not during the build.**

Four of the checks below cannot be retrofitted once a build has started. Three
of them are legally irreversible. This gate is free to run and takes about half
a day of client time.

A gate is something you can **fail**. If a check comes back NO-GO, the correct
outcome is a paid process-mapping engagement, not a discounted build.

## How to use this

Work top to bottom. Each gate has a verdict box. Every verdict is recorded with
a date and a name, because these are the artifacts you will be asked for later
by a works council, a data protection officer, or a court.

Do not proceed past a RED verdict without a written, signed exception from the
client naming who accepted the risk.

## GATE 1. GDPR Article 22 classification

**Why this is first.** If Article 22 applies and you build without designing for
it, the workflow may not be lawfully operable at all. This is a legal
classification, not an engineering preference, and it decides whether the thing
may exist in the shape the client asked for.

Three questions. All three must be answered before anything else.

| # | Question | Yes / No |
|---|---|---|
| 1 | Does the process concern a **natural person**? | |
| 2 | Is a **decision produced or influenced** about that person? | |
| 3 | Is the effect **legal or similarly significant**? | |

Legal or similarly significant covers hiring and candidate screening, credit and
lending, insurance pricing, benefits and entitlement, access to services,
performance evaluation, disciplinary action, and shift or workload allocation.

**If all three are YES, Article 22 is in scope.**

Post-SCHUFA at the CJEU, a scoring tool that influences a selection decision is
in scope **even where a nominal human review exists**. Rubber-stamping does not
qualify. For the human review to count, that person must have the authority to
override, access to the underlying data, and an understanding of the logic.

Design consequences when Article 22 is in scope.

- [ ] The reviewing human is named, and their authority to override is written down
- [ ] The reviewer sees the input data, not only the output
- [ ] The reviewer is trained on how the system reaches its result
- [ ] The data subject's right to an explanation is wired into the interface
- [ ] The data subject's right to contest is wired into the interface
- [ ] A DPIA exists and covers prompts and retained conversation state as
      processing surfaces in their own right

That last point is easy to miss. A 2025-era DPIA template treats only the stored
record as processing. The EDPB support pool report on LLM risks names prompts,
retained conversation state and feedback as LLM-specific vectors that belong in
the assessment.

**Verdict.** GO / GO WITH DESIGN CONSTRAINTS / NO-GO
**Recorded by.** ______________ **Date.** ______________

## GATE 2. Works council trigger, BetrVG §87(1) Nr. 6

**Applies to German clients with a works council. This is the single most common
invisible reason a signed German project stalls for months or dies at rollout.**

An automation that is a *technische Einrichtung geeignet zur Überwachung*, a
technical device suitable for monitoring employee behaviour or performance,
triggers **mandatory co-determination**. Not consultation. Mandatory.

Note the word **geeignet**, suitable. The system does not have to be intended for
monitoring. It only has to be **capable** of it. That is a much lower bar than
most clients assume, and it is where projects get caught.

| # | Trigger question | Yes / No |
|---|---|---|
| 1 | Does the client have a Betriebsrat? | |
| 2 | Does the automation touch employee data in any form? | |
| 3 | Could its output be used to assess an individual's behaviour or performance? | |
| 4 | Does it log who did what, and when? | |
| 5 | Does it allocate work, shifts, or workload between named people? | |

**If 1 is YES and any of 2 to 5 is YES, assume co-determination applies.**

Introducing the system without a Betriebsvereinbarung is legally ineffective, and
the works council can force it to be switched off after you have delivered and
invoiced.

Actions when triggered.

- [ ] Flag it to the client sponsor in writing, in week one
- [ ] Confirm whether an existing IT-Rahmenbetriebsvereinbarung already covers it
- [ ] Offer the pre-drafted KI-Betriebsvereinbarung annex as a paid deliverable
- [ ] Add **"BV signed"** as a hard milestone in the project plan, before go-live
- [ ] Do not schedule go-live until that milestone closes

Bitkom published a guide on AI and co-determination in February 2026 which is the
usable reference for what the agreement should contain.

**The commercial angle.** Turning up with a draft annex and a Betriebsrat
briefing deck is a differentiator. Most suppliers leave the client to work it out
alone, and the project dies quietly while everyone waits.

**Verdict.** NOT APPLICABLE / TRIGGERED, BV REQUIRED / TRIGGERED, EXISTING BV COVERS IT
**Recorded by.** ______________ **Date.** ______________

## GATE 3. Value baseline capture

**This window opens once and closes the moment you touch anything.**

Every retainer renewal conversation you will ever have turns on a number you
cannot produce retroactively. If nobody records the before-state, the value of
the work is unprovable forever, no matter how good the build is.

Capture these for each process in scope, before any change is made.

| Metric | Current value | Source of the number | Owner |
|---|---|---|---|
| Volume per period | | | |
| Cycle time, start to finish | | | |
| Error or rework rate | | | |
| Person-minutes per instance | | | |
| Fully loaded cost per transaction | | | |
| Current failure or exception rate | | | |

Rules for this table.

- [ ] Every number has a **named source**, a report, a query, an export, not an estimate
- [ ] Where a number is genuinely an estimate, it is labelled as one
- [ ] The **process owner signs it off** before the build starts
- [ ] A copy goes into the SOW as an annex

Then commit to the follow-up.

- [ ] A quarterly Value Realisation Report re-measures the same six metrics
- [ ] Attribution is stated honestly, separating what the automation caused from
      what other changes caused
- [ ] The report is a named deliverable in the retainer, not a favour

**Honesty note for the report.** If a client also changed team size, tooling or
process during the period, say so. A claimed saving that a CFO can pick apart
costs more credibility than a smaller number stated cleanly.

**Verdict.** BASELINE CAPTURED AND SIGNED / BASELINE INCOMPLETE, RISK ACCEPTED
**Recorded by.** ______________ **Date.** ______________

## GATE 4. Deterministic versus probabilistic verdict

**The question is not "can AI do this". It is "should this be AI at all".**

A deterministic solution costs less to run, never hallucinates, is trivially
testable, and can be given a real SLA. A probabilistic one needs an evaluation
set, a cost limit, guardrails, and a statistical acceptance clause. Choosing the
second when the first would do is how margin dies.

Work down. Stop at the first YES.

| # | Question | If YES |
|---|---|---|
| 1 | Can the rule be written down as a rule? | Build it deterministic. No LLM. |
| 2 | Is the input structured and predictable? | Build it deterministic. |
| 3 | Is a database constraint or a validation rule enough? | Build that instead. |
| 4 | Does the client need the answer to be identical every time? | Deterministic only. |
| 5 | Is a wrong answer intolerable and unrecoverable? | Deterministic, or human. |

Only if all five are NO does a probabilistic approach earn its place.

Then check the process is even automatable.

| # | Process readiness | Verdict |
|---|---|---|
| 6 | Is the process stable, or does it change monthly? | |
| 7 | How many variants exist? Count them. | |
| 8 | What is the current exception rate? | |
| 9 | Is the process documented, or does it live in someone's head? | |
| 10 | Does the data exist, is it accessible, and is it clean? | |
| 11 | Who owns the upstream system, and will they warn you before changing it? | |

**Never automate a broken process.** Automating an undocumented process with a
40% exception rate produces an automation with a 40% exception rate and a new
maintenance bill on top.

If gates 6 to 11 come back badly, the honest sale is a **paid process-mapping
engagement first**. That is a real deliverable, it is billable, and it protects
the build that follows.

**Verdict.** DETERMINISTIC BUILD / PROBABILISTIC BUILD / NO-GO, PROCESS WORK FIRST
**Recorded by.** ______________ **Date.** ______________

## GATE 5. Role allocation under the EU AI Act

Decide this before the build, because it determines who carries the conformity
obligations and the penalty exposure.

| # | Question | Answer |
|---|---|---|
| 1 | Does the system ship under the **client's** name? | |
| 2 | Does it ship under **your** name, or as your product? | |
| 3 | Are you substantially modifying an existing high-risk system? | |

If 1, the client is normally the provider and you are a supplier. If 2 or 3, you
may be the provider yourself, which pulls in conformity assessment, technical
documentation, post-market monitoring and Article 99 exposure.

- [ ] The answer is written into a Role Allocation Memo
- [ ] Both parties sign it before build starts
- [ ] The memo is referenced from the SOW

**Article 50 transparency applies from 2026-08-02** to any system a person
interacts with. Systems already on the market get a watermarking grace period to
2026-12-02. Annex III high-risk obligations were deferred to **2027-12-02** by
the Digital Omnibus, and Annex I embedded to 2028-08-02.

Do not sell the deferral as a reprieve. An Annex III system still needs the
conformity package, only later. Reference the date applicable under Article 113
as amended rather than hardcoding a date into a contract, because the Commission
retained power to pull the dates forward.

**Verdict.** CLIENT IS PROVIDER / WE ARE PROVIDER / SHARED, MEMO ATTACHED
**Recorded by.** ______________ **Date.** ______________

## GATE 6. The commercial and platform checks

Fast, but each one has ended a project when skipped.

**Insurance.**
- [ ] Confirmed with the broker that professional indemnity responds to AI deliverables
- [ ] Confirmed no absolute AI exclusion has been added at renewal
- [ ] The liability cap in the contract is one the policy can actually stand behind

**Platform licence.**
- [ ] Where will this run, the client's instance or ours? Decided and written down.
- [ ] If ours, the Enterprise licence question is resolved in writing with the vendor
- [ ] Platform dependency is disclosed to the client in the SOW

**Plan tier fit.**
- [ ] The client's plan supports what the SOW promises. Evaluations need Pro.
      Source control and SSO need Business. External secrets, log streaming,
      scoped API keys and full version history need Enterprise.
- [ ] The plan cost is in the client's budget, not a surprise at delivery

**Sector rules.**
- [ ] Is the client a financial entity? If yes, DORA Article 30 annex required.
- [ ] Is the client an automotive supplier? If yes, check TISAX expectations early.
- [ ] Will a consumer touch any interface? If yes, accessibility applies and is priced.

**Engagement model.**
- [ ] The engagement is deliverable-based, not time-and-direction based
- [ ] No dedicated desk, badge or client-issued equipment as of right
- [ ] If beyond six months on-site, or above 70% of revenue from one client, a
      §7a SGB IV status determination is started

**Verdict.** ALL CLEAR / EXCEPTIONS NOTED BELOW
**Recorded by.** ______________ **Date.** ______________

## Gate summary sheet

Attach this to the SOW.

| Gate | Verdict | Date | Recorded by |
|---|---|---|---|
| 1. GDPR Article 22 | | | |
| 2. Works council §87 | | | |
| 3. Value baseline | | | |
| 4. Deterministic vs probabilistic | | | |
| 5. AI Act role allocation | | | |
| 6. Commercial and platform | | | |

**Signed off to proceed to SOW.**

Client ______________ Date ______________

Supplier ______________ Date ______________

## Cross references

- `docs/GAP-ANALYSIS-2026.md` for the evidence behind each gate
- `guides/12-n8n-platform-reality-2026.md` for the tier-fit matrix
- `checklists/02-pre-project-checklist.md` for the operational setup that follows

## A note on legal content

The regulatory summaries here are a practitioner's starting point, not legal
advice. Article numbers, dates and thresholds change. Verify against the primary
source before relying on any of it in a real engagement, and have counsel review
anything that reaches a contract.
