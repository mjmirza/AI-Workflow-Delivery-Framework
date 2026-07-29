# Template 12. Works Council Readiness Pack

**For German clients with a Betriebsrat. The single most common invisible reason
a signed German project stalls for months or dies at rollout.**

Most suppliers leave the client to handle this alone. The project then waits,
quietly, while nobody owns the problem. Turning up with a draft and a briefing
deck is a differentiator, and it is also billable work.

## The legal position, in one paragraph

An automation that is a *technische Einrichtung, die dazu geeignet ist, das
Verhalten oder die Leistung der Arbeitnehmer zu überwachen* triggers mandatory
co-determination under **BetrVG §87 Abs. 1 Nr. 6**. Mandatory, not consultation.
Introducing the system without a Betriebsvereinbarung is legally ineffective, and
the works council can force it to be switched off after delivery and invoicing.

**The word that catches people is *geeignet*, suitable.** The system does not
have to be intended for monitoring. It only has to be **capable** of it. Logging
who did what and when is usually enough. That is a far lower bar than clients
assume.

Bitkom published a guide on AI and co-determination in February 2026 which is the
usable reference for what an agreement should contain.

**Unverified.** A 2026 BAG ruling on AI co-determination is cited by secondary
German sources, but this research could not confirm an Aktenzeichen. **Do not
cite that ruling to a client without the docket number.** The statutory position
above stands on its own and does not need it.

## Part A. The trigger check

Run this at scoping, in week one. It takes ten minutes.

| # | Question | Yes / No |
|---|---|---|
| 1 | Does the client have a Betriebsrat? | |
| 2 | Does the automation process employee data in any form? | |
| 3 | Could its output be used to assess an individual's behaviour or performance? | |
| 4 | Does it log who did what, and when, at individual level? | |
| 5 | Does it allocate work, shifts or workload between named people? | |
| 6 | Does it record timing, duration or throughput per person? | |
| 7 | Could a manager derive a ranking or comparison from its output? | |

**If 1 is YES and any of 2 to 7 is YES, assume co-determination applies** and
proceed to Part B.

If 1 is NO, record that and move on. If the client is close to the threshold for
forming a works council, note it as a future risk in the project record rather
than ignoring it.

## Part B. The escalation path

- [ ] Flag in writing to the client sponsor, week one, before build starts
- [ ] Ask whether an existing **IT-Rahmenbetriebsvereinbarung** already covers
      this class of system. Often one does, and the project only needs an annex
- [ ] Ask who the Betriebsrat contact is, and whether they have seen AI
      proposals before
- [ ] Offer the briefing session and the draft annex as a **paid deliverable**
- [ ] Add **"BV signed"** as a hard milestone in the project plan
- [ ] Do not schedule go-live before that milestone closes
- [ ] Build the expected timeline into the commercial plan. Weeks, sometimes
      months, and it is not your delay

## Part C. What the agreement needs to cover

Drafting checklist for the annex. This is what a works council will ask about,
roughly in the order they ask.

**Purpose and scope**
- [ ] What the system does, in plain German, without vendor language
- [ ] Which processes and which employee groups are in scope
- [ ] What is explicitly **out** of scope

**Data**
- [ ] Exactly which employee data fields are processed
- [ ] Where the data goes, including any third party model provider
- [ ] Whether data leaves the EU, and on what legal basis
- [ ] Retention period per data category
- [ ] Who can access it, in which role

**The monitoring question, which is the whole point**
- [ ] An explicit statement that the system is **not** used for individual
      performance assessment, if that is true
- [ ] If it is used for that, say so plainly. A concealed purpose discovered
      later ends the agreement and the trust
- [ ] What aggregation level any reporting uses
- [ ] An explicit ban on deriving individual rankings, where agreed

**Human oversight**
- [ ] Which decisions require a human, tied to the Autonomy Matrix
- [ ] Who that human is, by role
- [ ] How an employee contests an outcome
- [ ] That the reviewing human can genuinely override, not merely confirm

**Transparency to employees**
- [ ] How employees are told the system exists
- [ ] What they are told about how it works
- [ ] Where they can read more

**Change and review**
- [ ] What counts as a change requiring renewed agreement
- [ ] How often the agreement is reviewed, and who attends
- [ ] What happens on a model swap, tied to the Model Register
- [ ] Termination and switch-off conditions

**Technical safeguards**
- [ ] Logging and audit, and who may read the logs
- [ ] Access control and least privilege
- [ ] What happens on a security incident

## Part D. The briefing session

A short session for the works council, run by the client with your support. Aim
for forty minutes, half of it questions.

**What works.**

- Show the system doing its actual job, live. Abstract descriptions create fear
- Lead with what it does **not** do, and be specific
- Bring the Autonomy Matrix. A signed matrix showing irreversible actions require
  a human is the most persuasive single artifact available
- Name the human in the loop, by role, out loud
- Answer the job-security question directly rather than deflecting it. If roles
  change, say so. If they do not, say why not
- Give them the draft in advance, not in the room

**What fails.**

- Vendor marketing language
- Claiming the AI is neutral or objective
- Treating the session as a formality to be survived
- Any hint that the decision has already been made
- Promising the system cannot be misused, rather than showing the controls that
  make misuse detectable

## Part E. The commercial framing

This is real work with a real deliverable. Price it as a line item.

| Deliverable | Typical shape |
|---|---|
| Trigger assessment | Half a day, at scoping |
| Draft BV annex | One to two days |
| Betriebsrat briefing deck | Half a day |
| Briefing session attendance | Half a day, plus follow-up |
| Revision round after council feedback | One day, usually needed |

Two things to say to the client sponsor early.

**This is not optional and it is not your delay.** The statute decides, not the
project plan. A sponsor who learns this in week one plans around it. One who
learns it in week ten blames you.

**A signed BV protects them, not only the employees.** It is the document that
makes the system lawfully operable and defensible. That reframes it from an
obstacle into an asset, which is the true position.

## What this pack does not do

It does not replace German employment counsel. The drafting checklist covers what
councils ask about, but the agreement itself is a legal instrument between the
employer and the works council, and neither you nor this template is a party to
it. Your role is to make the technical facts clear, accurate and complete enough
that the two parties can reach agreement quickly.

## Cross references

- `checklists/07-scoping-gate.md` GATE 2 for the trigger check in context
- `templates/11-model-register-autonomy-matrix.md` for the matrix to bring
- `guides/02-security-implementation.md` for the safeguards section
- `docs/GAP-ANALYSIS-2026.md` section 1.3 for the evidence and its limits
