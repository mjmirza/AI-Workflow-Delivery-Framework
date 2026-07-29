# Gap Analysis 2026

**Compiled 2026-07-28. This is the findings register behind the v3.0 rebuild.**

Five parallel research streams plus a two-model adversarial council produced this
list. Every item states its evidence grade. Nothing here is opinion dressed as
fact.

## How to read the evidence grades

| Grade | Meaning |
|---|---|
| **A** | Confirmed from a primary source, quoted and linked |
| **B** | Law firm, analyst or tier-one press, named and dated |
| **C** | Secondary reporting, single source, directionally useful |
| **U** | UNVERIFIED. Do not put in front of a client until confirmed |

## The measured starting position

A term-frequency scan across all 78,236 words of the v2.0 framework, run
2026-07-28.

**Zero occurrences anywhere.** MCP, Model Context Protocol, vector, embedding,
RAG as a standalone word, non-determinism, EU AI Act, sub-processor, ISO 27001,
OpenTelemetry, human-in-the-loop, queue mode, task runner, source control,
external secrets, and every competitor name.

**The headline number.** The word "agent" appeared **once** in 78,236 words, as a
single line in a pricing table reading `Custom AI agent  $8,000 - $25,000`.

Hardcoded `GPT-4` and `GPT-3.5`. No n8n version compatibility range stated
anywhere. Dates ran 2023 to 2025, with no 2026.

## The council verdict, and the correction it forced

Two differently-trained models were asked to refute the framing that the
framework was mis-scoped rather than stale. Both refuted it, and both were right.
The corrected verdict, which they reached independently.

- The **engineering content is stale**. Additive fix. The deterministic substrate
  already documented, credentials, triggers, retries, environments, promotion,
  handover, remains the billable core and becomes more important under agents,
  not less.
- The **commercial and acceptance layer is genuinely mis-scoped**. Fixed-bid
  bands and deterministic acceptance criteria do not age, they fail outright
  against probabilistic systems. That chapter needs re-architecture.

Both models converged on the same remedy. Keep n8n as the delivery spine, add an
AI governance and operations layer on top. Do not rename to a generic agentic
framework, because that discards the n8n Ambassador and Verified Expert Partner
trust anchor.

## TIER 1. Business risk. Fix these first

### 1.1 n8n licensing exposure on multi-tenant hosting. Grade A

n8n's own support article states that hosting a client's workflows and
credentials inside your own instance requires an **Enterprise license**, while
building on the client's own instance requires none. The common agency pattern of
one shared box across several clients is, by n8n's own answer, a license breach.

**Closed by.** `guides/12-n8n-platform-reality-2026.md` section 1.
**Still open.** A Platform Licence Register artifact, one row per platform, with
a hosting decision rule and a client-facing platform-dependency disclosure.

### 1.2 The CVE-to-upgrade-to-breakage vice has no named owner. Grade A

n8n shipped multiple CVSS 10.0 remote code execution flaws in 2026, one of them
unauthenticated, with a patch bypassed inside 24 hours. Compromise exposes
`N8N_ENCRYPTION_KEY` and every stored credential, so a shared instance means a
cross-client breach.

Security forces upgrades. n8n 2.0 upgrades break delivered workflows. **No
retainer template in the v2.0 framework says who pays for that remediation.**

**Closed by.** Guide 12 sections 2 and 3.
**Still open.** The retainer clause itself, and a patch SLA with a named owner.

### 1.3 Works council co-determination, the German deal-killer. Grade B

An automation touching employee data is a *technische Einrichtung geeignet zur
Überwachung* under **BetrVG §87(1) Nr. 6**, triggering mandatory co-determination,
not consultation. Introducing it without a Betriebsvereinbarung is legally
ineffective and the works council can force a shutdown.

This is the single most common invisible reason a signed German project stalls
four to six months or dies at rollout. Bitkom published a dedicated guide in
February 2026.

**Grade U.** A 2026 BAG ruling is cited by secondary German sources but no docket
number was confirmed. Do not cite the ruling to a client without the Aktenzeichen.

**Still open.** A Works Council Readiness Pack. Trigger checklist for the scoping
phase, a pre-drafted KI-Betriebsvereinbarung annex, a Betriebsrat briefing deck,
and a hard project-plan gate reading "BV signed" before go-live.

### 1.4 Your own insurance may not cover AI deliverables. Grade B

ISO added a generative AI exclusion to commercial general liability effective
January 2026. W.R. Berkley filed form PC 51380, an absolute AI exclusion for E&O
and professional indemnity. AIG filed AI exclusions in 2026.

The framework caps liability in its contract template while assuming cover exists
behind that cap.

**Still open.** An Insurance Verification Gate before signature. This is a
five-minute phone call to your broker and it is the highest-value single action
in this entire register.

### 1.5 Liability law shifted, quietly. Grade B

The AI Liability Directive was **withdrawn**, formalised in the Official Journal
2025-10-06. Product Liability Directive (EU) 2024/2853 fills the gap and is
harsher. Software, **including delivered as a service**, is now a product under
strict no-fault liability. Transposition deadline 2026-12-09.

From that date a defective AI deliverable can generate a strict-liability claim
from a third party who never signed your contract. A contract-law liability cap
does not reach that.

### 1.6 Scheinselbstständigkeit and AÜG. Grade B

Subcontracting a developer, or embedding in a client team taking direction on
hours and methods, can trigger reclassification. Deutsche Rentenversicherung can
claw back up to four years of combined social contributions plus penalties, and
§266a StGB makes wilful cases criminal. §7a SGB IV status determination is the
defensive instrument.

This is the risk most likely to end a small consultancy outright, and it is a
delivery-model risk, not a contract-template risk.

**Still open.** An Engagement Model Guard. A ten-point independence checklist at
SOW time, plus a trigger rule that any engagement beyond six months on-site or
above 70% revenue from one client goes through §7a.

### 1.7 DORA locks you out of every bank and insurer. Grade B

DORA applies from 2025-01-17. Delivering into a financial entity makes you an ICT
third-party provider, and the client's contract with you must satisfy **Art. 30**.
Single written document, SLAs, subcontractor disclosure, data locations, audit
and access rights, and for critical functions, participation in threat-led
penetration testing plus mandatory exit clauses guaranteeing data return on your
insolvency.

Without a DORA-ready annex you cannot be onboarded, and discovering this during
redlining costs a quarter.

### 1.8 The enterprise procurement barrier. Grade B

TISAX for automotive, usually Assessment Level 3, reportedly six to twelve months
and 30,000 to 80,000 EUR for a mid-market company. VDA ISA 6.0 mandatory since
April 2024. Separately NIS2 forces roughly 29,500 German entities to
contractually impose cybersecurity requirements on suppliers, which means those
obligations flow down to you.

**Still open.** A Procurement Readiness Kit. Pre-answered master questionnaire,
one-page security fact sheet, Lieferantenselbstauskunft, a stated NIS2
supplier-clause acceptance position, and a decision rule on when TISAX is worth
the cost versus declining automotive work.

## TIER 2. The commercial layer that is mis-scoped

### 2.1 Acceptance criteria for probabilistic systems. Grade A on the mechanism

You cannot write "the system shall correctly classify tickets" for a
probabilistic system without signing an unbounded warranty.

n8n now ships the vocabulary to fix this. Six evaluation metrics, Correctness,
Helpfulness, String Similarity, Categorization, Tools Used, and Custom, with
trend deltas against the previous run. **That delta is a defensible regression
gate.**

**Still open.** A Probabilistic Acceptance Annex. Per named workflow, defining
the frozen golden set under joint change control, the accuracy and latency
thresholds, the measurement window, the evidence format, what counts as
successful completion, the human-handoff rate, and the remedy as remediation
rather than refund.

### 2.2 Fixed-bid pricing does not survive agentic work. Grade A by council

Both council models independently reached this. Fixed-bid survives for bounded
build artifacts, scoping, architecture, migration, environment setup, credential
hardening, eval suite setup, documentation and handover. It does not survive as
an all-in operating price for open-ended agent usage.

The shape that works is **fixed-fee build plus pass-through or marked-up usage
plus retainer, with eval gates as acceptance**. The current bands survive only if
they explicitly exclude variable model, API, storage and execution costs.

### 2.3 Cost governance is a deliverable, not an optimisation. Grade B

FinOps Foundation now runs a Token Economics working group, and AI tokenomics was
the FinOps X 2026 Day 1 keynote theme.

Two structural problems. Model providers do not support tagging for cost
allocation, so an invoice shows spend by API key or project rather than by cost
centre. And runaway spend is a live failure mode, with one widely-cited incident
of four agents in a loop burning 47,000 USD over 11 days, **Grade U at source**.

n8n-specific and concrete. Cap `maxIterations` on the AI Agent node at 5 to 10.

**Still open.** A Cost Model and Budget Guard deliverable. Per-use-case API key
structure, hard spend limit, anomaly alert, and a documented cost-per-outcome
baseline the retainer is measured against.

### 2.4 Baseline capture has one window and it closes immediately. Grade C

Every retainer renewal turns on a number you cannot produce retroactively. If
nobody records the before-state, the value is unprovable forever.

The often-quoted "95% of GenAI pilots fail" figure is **MIT Project NANDA,
self-described preliminary findings from 52 interviews**. The real claim is "no
measurable P&L impact", not "failed". Quote it with the methodology or not at
all.

**Still open.** A Value Baseline Protocol. Volume, cycle time, error and rework
rate, FTE-minutes per instance, cost per transaction, signed off by the process
owner **before any build**, plus a quarterly Value Realisation Report.

### 2.5 DACH rates declined for the first time since 2016. Grade B

freelancermap Freelancer-Kompass 2026. 103 EUR per hour average across
freelancers, 95 EUR per hour median in IT, Bavaria 90 to 95 EUR. 43% of
freelancers without secured utilisation.

US agency pricing content puts a two to four week audit at 5,000 to 15,000 USD,
which sits **below the DACH cost base**. Price audits on outcome, never hours.

## TIER 3. Engineering gaps the platform can now close

### 3.1 Silent failure is the number one practitioner complaint. Grade A

Best-evidenced complaint in the whole sweep. Direct quote from the n8n community,
May 2026.

> your HubSpot node failed, your CRM row was never created, your client never got
> the email, and n8n's execution log shows success

Confirmed in production by three separate practitioners through July 2026. The
framing that belongs in the framework, from the same source, is that **silence is
not health. A healthy system reports that it is alive. Only broken systems are
quiet.**

Nine documented silent-death modes. No error workflow attached, workflow toggle
off, manual tests passing where scheduled runs fail, multiple cron expressions in
one Schedule Trigger, no timezone set, alternate entry points skipping
validation, the instance itself dead, credentials expired, and data shape changed
upstream.

**Still open.** A silent-failure checklist, a global error-workflow template with
a backup error workflow whose only job is to email when primary alerting fails,
and an **error-workflow conformance monitor**, a meta-workflow that lists every
workflow with no error workflow assigned and alerts weekly. That last one has no
published competitor anywhere.

### 3.2 Heartbeat monitoring, the check that catches silent death. Grade A

Prometheus answers "is the instance healthy". It does not answer "did the 6am
invoice sync actually run". That needs a dead man's switch where silence is
treated as failure. Healthchecks.io or Uptime Kuma push monitors.

**Still open.** A Heartbeat Register. Every schedule-triggered workflow gets a
push URL and an expected window.

### 3.3 Autonomy is a per-action decision, not a permissions setting. Grade B

Prompt injection is now OWASP's number one LLM risk, in a Top 10 rewritten for
the agentic era with tool-call hijacking as a new entry. First confirmed
malicious MCP package in the wild, September 2025.

The structural point. LLMs process a single token stream with no hardware
boundary between instruction and data, so injection is not fixable by prompt
engineering. Defence is architectural.

**Still open.** An Autonomy Matrix per delivered agent. For each tool, is the
action reversible, what is the blast radius, does it require approval.

### 3.4 Model deprecation is a maintenance obligation. Grade A

Anthropic commits to 60 days notice for public models. OpenAI gives six months
for GA models, three for specialised variants, and as little as **two weeks for
previews**. The April 2026 announcement ending the GPT-4 era was the largest
single deprecation notice any provider has issued.

A delivered system pinned to a model has a hard expiry date.

**Still open.** A Model Register per client, model, provider, retirement date,
fallback. Plus a model-swap regression suite, which is what the golden set is
for. **This is the strongest retainer argument available in 2026.**

### 3.5 Data contracts and upstream schema drift. Grade B

Every automation consumes somebody else's schema. When the client upgrades their
CRM, your workflow breaks and you get blamed and repair it unpaid. The Linux
Foundation Open Data Contract Standard under Bitol is the published instrument.

**Still open.** An Integration Contract Register plus a schema-drift canary that
fails loudly, plus a change-order trigger clause making upstream schema changes
billable rather than warranty.

### 3.6 GDPR Art. 22 is a classification gate, not an engineering pattern. Grade B

Distinct from human-in-the-loop as an engineering concern. Post-SCHUFA at the
CJEU, a scoring tool that influences a selection decision is in scope even where
nominal human review exists, and rubber-stamping does not qualify.

**Still open.** A three-question Art. 22 test at the scoping stage. Does it
concern a natural person, is a decision produced or influenced, is the effect
legal or similarly significant.

### 3.7 Credential custody across the client boundary. Grade B

Whose credentials does the automation run under, who holds them after the
engagement, and what happens at consultant offboarding. Buyer-side vetting
content names **vendor credential retention after delivery as a hard stop**.

A second problem. When an agent acts under a shared service account, the audit
trail attributes the action to the account rather than the actor, which breaks
accountability exactly where GDPR and works councils demand it.

**Still open.** A Credential Custody Schedule. Automations run under a named
service identity created by the client, never a personal account, never a
consultant-owned key.

## TIER 4. Compliance calendar

### 4.1 EU AI Act, with the corrected dates. Grade A

My first research pass had this wrong and a second pass corrected it. The
**Digital Omnibus** amended Regulation (EU) 2024/1689. Parliament endorsed
2026-06-16, Council gave final green light 2026-06-29.

| Obligation | Date |
|---|---|
| Prohibited practices, Art. 5, and AI literacy, Art. 4 | In force since 2025-02-02 |
| GPAI model obligations | In force since 2025-08-02 |
| **Art. 50 transparency** | **2026-08-02, unchanged** |
| Art. 50(2) watermarking, systems already on market | Grace to 2026-12-02 |
| **Annex III stand-alone high-risk** | **Deferred to 2027-12-02** |
| Annex I embedded high-risk | Deferred to 2028-08-02 |

**Do not sell the deferral as a reprieve.** A client's HR screening or credit
scoring automation is still Annex III and still needs the conformity package,
16 months later. The Commission retained power to pull dates forward, so
contracts should reference the date applicable under Art. 113 as amended rather
than hardcoding one.

**Grade U.** The 7% of global turnover penalty cap appears in secondary sources.
A direct fetch of the Gibson Dunn analysis returned no penalty figures. Confirm
against Art. 99 before quoting.

### 4.2 Art. 4 AI literacy is in force and usually skipped. Grade B

Obliges both consultancy and client to ensure sufficient AI literacy among those
operating the systems. Costs a day, bundles into handover, and is a differentiator
in DACH procurement.

### 4.3 Provider versus deployer role allocation. Grade B

When a consultancy builds a system shipping under the client's name, the client
is usually the provider. But placing it on the market under your own name, or
substantially modifying a high-risk system, makes you the provider, which pulls
in conformity assessment, technical documentation, post-market monitoring and
Art. 99 penalty exposure.

**Still open.** A Role Allocation Memo signed at scoping, before any build.

### 4.4 EU model contract clauses exist and are free. Grade A

The Commission's Model Contractual Clauses for AI procurement were updated
2025-03-05, in a full high-risk version, a light non-high-risk version, and a
commentary. Drafted for public buyers, explicitly usable by private ones.

**Still open.** Map the MSA against MCC-AI-Light and be able to say so in a
tender. In DACH public and semi-public procurement this approaches a qualifying
criterion.

### 4.5 German e-invoicing. Grade B

Since 2025-01-01 every German business must be able to receive structured
e-invoices under EN 16931. Issuing becomes mandatory 2027-01-01 above 800,000 EUR
prior-year turnover and 2028-01-01 for everyone. PDF permitted with recipient
consent only through 2026-12-31.

**Still open.** The invoice template must emit XRechnung or ZUGFeRD.

### 4.6 ISO/IEC 42001 approaching table stakes. Grade C

Reported on RFPs by mid-2026. Cost estimates vary wildly across sources and are
mutually inconsistent, all from consultancy marketing. **Grade U on every
figure.** Use to frame a range, never as a quoted price.

## TIER 5. Adoption and delivery practice

### 5.1 It works and nobody uses it. Grade B

Prosci research across 2,000+ change projects found structured change management
delivers six times better outcomes, and identifies the failure precisely as the
gap between Knowledge and Ability. Training completion proves information was
received, not that anyone can apply it.

For a consultancy this is worse than a technical failure, because you are
contractually done and the client is unhappy anyway.

**Still open.** An Adoption Plan as a standard SOW line item, with an **adoption
KPI in the acceptance criteria**, for example 70% of eligible transactions
flowing through the automation for four consecutive weeks, rather than a purely
technical acceptance test.

### 5.2 Should this even be AI. Grade B

Gartner predicted 50% of RPA implementations would fail to deliver sustainable
ROI, with 39% of decision-makers citing not fully understanding the process. The
doctrine of never automating a broken process is old, and almost no delivery
framework encodes it as a gate you can fail.

Separately, Gartner predicts **over 40% of agentic AI projects will be cancelled
by end 2027**, from a January 2025 poll of 3,412 webinar attendees, and notes
that only about 130 of thousands of agentic vendors are real.

**Still open.** A Feasibility and Fit Gate with an explicit NO-GO verdict and a
paid process-mapping offer as the alternative sale. The ability to say "this
should be a database constraint, not an LLM" is both a differentiator and a
margin protector.

### 5.3 The artifact layer barely exists, which is the opening. Grade A

A GitHub search for `n8n handover client documentation` returns **zero results**.
The n8n GitHub presence is roughly 10,000 workflow-JSON template dumps and no
delivery kits, no SOPs, no client-facing documentation systems.

The one purpose-built handover tool found was **one day old** at time of research
and closed-source. The canonical community thread on delivering workflows to
clients is effectively an unanswered survey, where the single reply declined to
share their approach.

Two patterns with no published competitor anywhere.

1. **Per-workflow running cost notes at handover.** Nobody documents opex.
2. **The error-workflow conformance monitor.** A meta-workflow alerting on any
   workflow that conforms to neither the global nor local error pattern.

Nobody has assembled engineering, cost, security, contracts and identity into one
delivery lifecycle. Anthropic and OpenAI publish engineering guides. FinOps owns
cost. OWASP owns threat model. EU MCC-AI owns contracts. NIST and Okta own agent
identity. Bitkom owns DACH co-determination. **That gap is the reason this
framework should exist.**

### 5.4 Business continuity and key-person risk. Grade C

Enterprise procurement increasingly asks small suppliers for a BCP, and DORA
makes exit provisions contractual for financial clients. Consultant incapacity is
the unspoken objection in every enterprise deal with a solo firm.

**Still open.** A two-page BCP, an escrow option in the price list, and a
documented architecture principle that everything runs in the client's tenant
under the client's credentials, which makes the consultant genuinely replaceable.

## Deliberately downgraded. Do not build for these yet

**CSRD and ESG.** Directive (EU) 2026/470 raised thresholds to roughly 1,000
employees and 450M EUR turnover, taking about 90% of previously-preparing
companies out of scope. The Value Chain Cap means CSRD filers cannot demand more
from suppliers under 1,000 employees than the VSME standard covers. Keep a
VSME-shaped one-pager on file. Nothing more. Grade B.

**Accessibility and the EAA.** In force since 2025-06-28, but scope is
consumer-facing. Purely B2B internal tooling is not covered, and a service
provider microenterprise exemption exists. Add one scoping question, will any
consumer touch this interface. If yes, EN 301 549 and WCAG 2.2 AA apply and get
priced in. Do not build a general accessibility programme. Grade B.

## What was actually written in this pass

| Artifact | Status |
|---|---|
| `LICENSE` swapped to CC BY 4.0 for docs, MIT retained for `pdf-generator/` | Done |
| `guides/12-n8n-platform-reality-2026.md` | Done |
| `docs/GAP-ANALYSIS-2026.md`, this file | Done |
| `research/` raw research reports | Done |
| Everything under "Still open" above | Specified, not written |

This is stated plainly rather than implied. The research is complete and the
highest-risk guide is written. The remaining artifacts are specified in enough
detail to build, but they do not exist yet.

## Known weaknesses in this research

- **Reddit was not fetchable.** The practitioner-voice vein is secondary
  throughout. Scoping and pricing complaints are the weakest-evidenced bucket.
- **The 2026 BAG works-council ruling** has no confirmed docket number.
- **Vendor indemnity terms** for OpenAI Copyright Shield and Microsoft's
  Customer Copyright Commitment were not retrievable. Most such indemnities are
  conditioned on unmodified services with safety filters enabled, which agentic
  deployments routinely break.
- **All agency pricing bands** are US SEO content with no methodology.
- **No authoritative probabilistic-SLA clause library** was found. Anyone
  claiming one exists should be asked for the URL.
- **One method only.** Web search and fetch. The regulatory section is the most
  solid, the pricing section the least.

## The single highest-value next move

Build the **Scoping Gate** first, and put four things in it that currently exist
nowhere in this framework.

1. The GDPR Art. 22 classification test
2. The Betriebsrat §87 trigger check
3. The value baseline capture
4. The deterministic-versus-probabilistic verdict

All four are free to run. All four are irreversible if skipped. Three of the four
cannot be retrofitted after the build starts.
