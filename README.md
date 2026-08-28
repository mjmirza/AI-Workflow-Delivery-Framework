# AI Workflow Delivery Framework

[![OpenRoots ORA 2.3](https://openroots.org/badge/ora.svg)](https://openroots.org/licenses/ora/2.3)

[![License CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Code MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/mjmirza/AI-Workflow-Delivery-Framework.svg)](https://github.com/mjmirza/AI-Workflow-Delivery-Framework/commits/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mjmirza/AI-Workflow-Delivery-Framework/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/mjmirza/AI-Workflow-Delivery-Framework/pulls)
[![n8n](https://img.shields.io/badge/n8n-2.x-orange?logo=n8n&logoColor=white)](https://n8n.io)
[![Sources](https://img.shields.io/badge/Sources-Primary%20and%20Dated-blue.svg)](docs/GAP-ANALYSIS-2026.md)

**Professional delivery standards for n8n automation and AI consultants.**
Version 3.0. Last research pass 2026-07-28.

## What you get

Not a tutorial. A set of artifacts you hand to a client, a lawyer, or a works
council, plus a set of gates you can fail before you have spent the client's
money.

- **Fail a project before you sell it.** The Scoping Gate runs in half a day and
  catches the four things that cannot be retrofitted once a build starts. Two are
  legal, and one has killed German projects at rollout after the invoice was
  already paid.
- **Say who pays when a security patch breaks the build.** Vendors ship severe
  vulnerabilities. Patching forces an upgrade. The upgrade breaks delivered
  workflows. Most retainers are silent on this. Template 10 is not.
- **Sign an acceptance clause you can survive.** Deterministic acceptance
  language on a probabilistic component is an unbounded warranty. There is
  drafting language here that splits the two.
- **Quote a platform without a licence surprise.** The tier-fit matrix tells you
  at scoping time which plan the SOW actually requires, rather than at delivery.
- **Cite dates that are real.** Every regulatory claim carries a source and an
  evidence grade. Anything unconfirmed is marked and must not reach a client.

## The five-minute version

If you read nothing else, read these three.

1. **[checklists/07-scoping-gate.md](checklists/07-scoping-gate.md)** before you sign anything.
2. **[guides/12-n8n-platform-reality-2026.md](guides/12-n8n-platform-reality-2026.md)** section 1, on platform licensing. Many agencies are in breach without knowing.
3. **[templates/10-ai-maintenance-addendum.md](templates/10-ai-maintenance-addendum.md)** clause 1, the security patch obligation.

## What changed in 2026

Version 2.0 was written for deterministic integration delivery. That is still the
billable core, and it gets more important under AI agents rather than less. But
four things moved underneath it, and version 3.0 exists because of them.

| What moved | Why it matters to a delivery contract |
|---|---|
| **Platform licensing** | Hosting a client's workflows and credentials on your own instance is an Enterprise-licence scenario by the vendor's own answer. Building on the client's instance is not. |
| **Security posture** | Multiple CVSS 10.0 remote code execution flaws shipped in 2026, one unauthenticated. A shared instance turns one compromise into a cross-client breach. |
| **Acceptance criteria** | Probabilistic components cannot be accepted on binary functional test. They need a frozen evaluation set and a statistical threshold. |
| **Regulatory calendar** | EU AI Act Article 50 transparency applies from 2026-08-02. Annex III high-risk was deferred to 2027-12-02 by the Digital Omnibus. Product liability for software delivered as a service turns strict on 2026-12-09. |

The full findings register, with evidence grades and named weaknesses, is in
**[docs/GAP-ANALYSIS-2026.md](docs/GAP-ANALYSIS-2026.md)**.

## Who this is for

| Role | What to read first |
|---|---|
| Automation consultant | Scoping Gate, then guides 01 to 07 |
| Agency owner | Gap analysis, then guide 12 section 1 |
| Freelance developer | Guide 10 workflow standards, guide 04 testing |
| Technical project manager | Checklists 01 to 06 |
| Sales | Templates 01, 06, 09, plus guide 08 pricing |
| Legal review | Templates 02, 03, 10, plus the Scoping Gate |

## Quick access templates (Google Docs)

| # | Template | Link |
|---|---|---|
| 01 | Master Checklist | [Open](https://docs.google.com/document/d/1ELsx36O76iHUsE-AgqRCQZsANT5HBTCu/edit?usp=sharing&ouid=113709258208959967521&rtpof=true&sd=true) |
| 02 | Standard Operating Procedure | [Open](https://docs.google.com/document/d/1l4ZiUPUJh_Mab6PhTL7EMyVMH-MqJpCr/edit?usp=sharing&ouid=113709258208959967521&rtpof=true&sd=true) |
| 03 | Client Onboarding Template | [Open](https://docs.google.com/document/d/1sLmUd-LtZA4KJ5dUI1wLhfW9MS6XMDA_/edit?usp=sharing&ouid=113709258208959967521&rtpof=true&sd=true) |
| 04 | Security Audit Checklist | [Open](https://docs.google.com/document/d/1vVUjvPYesw7gZDqAgsRLDYXpYkcaFaIY/edit?usp=sharing&ouid=113709258208959967521&rtpof=true&sd=true) |
| 05 | API Key Setup Guide | [Open](https://docs.google.com/document/d/13sajDpMGBo96LfKIGgyOvxqhEpDjZ21-/edit?usp=sharing&ouid=113709258208959967521&rtpof=true&sd=true) |
| 06 | Maintenance Retainer Template | [Open](https://docs.google.com/document/d/1z2ajbo7I6_M-Gdsd8-JjITTp666aHlxQ/edit?usp=sharing&ouid=113709258208959967521&rtpof=true&sd=true) |

> **PDF diagram viewing.** The generated PDFs may not render Mermaid diagrams
> correctly. For flowcharts, browse the `.md` files directly in this repository
> where diagrams render properly.

## Repository structure

```
checklists/     8 phase checklists, including the Scoping Gate
diagrams/       6 Mermaid architecture and lifecycle diagrams
guides/         12 delivery guides, onboarding through platform reality
processes/      7 role SOPs, lead gen through client
templates/      12 commercial, legal and operational templates
templates-html/ 5 print-ready HTML versions
docs/           Gap analysis and research output
pdf-generator/  Python tooling that builds the PDF set
generated-pdfs/ Pre-built PDFs of everything above
```

## Document index

**Checklists**

| # | Document | Use |
|---|---|---|
| 01 | Master checklist | The whole lifecycle in one page |
| 02 | Pre-project | Setup before build |
| 03 | Security | Credential and access posture |
| 04 | QA and testing | Before the client sees it |
| 05 | Handover | The day-one operator test |
| 06 | Offboarding | Clean exit |
| **07** | **Scoping Gate** | **Before the SOW. New in 3.0.** |
| **08** | **Silent Failure** | **The nine ways a workflow dies quietly. New in 3.0.** |

**Guides**

| # | Document |
|---|---|
| 01 | Client onboarding |
| 02 | Security implementation |
| 03 | API key management |
| 04 | Testing and QA |
| 05 | Handover and delivery |
| 06 | Maintenance and retainer |
| 07 | Offboarding |
| 08 | Pricing and estimation |
| 09 | Risk management |
| 10 | Workflow standards |
| 11 | Troubleshooting |
| **12** | **n8n platform reality 2026. New in 3.0.** |

**Templates**

| # | Document |
|---|---|
| 01 | Scope of work |
| 02 | Contract |
| 03 | Retainer agreement |
| 04 | Invoice |
| 05 | Email templates |
| 06 | Proposal |
| 07 | Project brief |
| 08 | Handover document |
| 09 | Change order |
| **10** | **AI and maintenance addendum. New in 3.0.** |
| **11** | **Model Register and Autonomy Matrix. New in 3.0.** |
| **12** | **Works Council Readiness Pack, DACH. New in 3.0.** |

**Processes.** Seven role SOPs covering lead generation, sales, closing, project
management, technical lead, developer and client.

## Find it by task

```
"I need to..."                          "Use this..."
----------------------------------------+--------------------------------------
Decide whether to take the project      | checklists/07-scoping-gate
Check if a works council must agree     | checklists/07-scoping-gate GATE 2
Decide if it should even be AI          | checklists/07-scoping-gate GATE 4
Qualify a new lead                      | checklists/02-pre-project-checklist
Write a proposal                        | templates/06-proposal-template
Create a contract                       | templates/02-contract-template
Add AI and patch clauses to a retainer  | templates/10-ai-maintenance-addendum
Estimate project pricing                | guides/08-pricing-estimation-guide
Assess project risks                    | guides/09-risk-management-guide
Onboard a new client                    | guides/01-client-onboarding-guide
Set up credentials securely             | guides/03-api-key-management
Follow workflow standards               | guides/10-workflow-standards-guide
Test my workflow                        | guides/04-testing-qa-framework
Check the platform tier a SOW needs     | guides/12-n8n-platform-reality-2026
Plan an n8n 2.x migration               | guides/12-n8n-platform-reality-2026
Stop a workflow failing silently        | checklists/08-silent-failure
Track model retirement dates            | templates/11-model-register-autonomy-matrix
Decide what an agent may do alone       | templates/11-model-register-autonomy-matrix
Handle a German works council           | templates/12-works-council-readiness
Do a security audit                     | checklists/03-security-checklist
Troubleshoot an issue                   | guides/11-troubleshooting-guide
Handle scope change                     | templates/09-change-order-template
Deliver to client                       | guides/05-handover-delivery
Set up ongoing support                  | guides/06-maintenance-retainer
End a client relationship               | guides/07-offboarding-guide
```

## Getting started

**First-time setup**

```
STEP 1: Read the core documents
        +-> README.md, this file
        +-> checklists/07-scoping-gate.md
        +-> diagrams/01-master-architecture.md
        +-> processes/00-sop-master-index.md

STEP 2: Customize the templates
        +-> templates/00-template-index.md
        +-> Replace every [PLACEHOLDER] with your own detail
        +-> Add your branding
        +-> Have counsel review templates 02, 03 and 10 before use

STEP 3: Train the team
        +-> Assign the role-specific SOPs
        +-> Walk the Scoping Gate on a past project as a dry run
        +-> Practise on a sample project
```

**Starting a new project**

```
1. checklists/07-scoping-gate.md            [Run this first. It can say no]
2. guides/01-client-onboarding-guide.md     [Onboarding]
3. diagrams/02-hosting-decision-tree.md     [Hosting decision]
4. templates/01-scope-of-work-template.md   [SOW]
5. templates/02-contract-template.md        [Contract]
6. templates/10-ai-maintenance-addendum.md  [If any AI component exists]
7. checklists/02-pre-project-checklist.md   [Pre-flight]
```

**Building and testing**

```
1. guides/02-security-implementation.md     [Security setup]
2. guides/12-n8n-platform-reality-2026.md   [Platform constraints and tier fit]
3. guides/04-testing-qa-framework.md        [QA]
4. checklists/03-security-checklist.md      [Security audit]
5. checklists/04-qa-testing-checklist.md    [QA verification]
```

**Delivering to the client**

```
1. guides/05-handover-delivery.md              [Delivery]
2. checklists/05-handover-checklist.md         [Delivery items]
3. templates/08-handover-document-template.md  [Handover doc]
```

## Customizing this for your firm

Before using any of it in a real engagement.

- Replace every `[PLACEHOLDER]` with your own detail
- Put your own name, entity and jurisdiction into the legal templates
- Set your own rates in Schedule A of the retainer and addendum
- Set your own patch windows and thresholds in template 10. The bracketed
  numbers there are starting points, not recommendations
- Have qualified counsel review templates 02, 03 and 10 in your jurisdiction
- Decide your own hosting position and write it into the SOW

**Converting to other formats.** The `pdf-generator/` directory builds the full
PDF set from the Markdown. Print-ready HTML versions of the five most
client-facing templates live in `templates-html/`.

## Diagrams

Six Mermaid diagrams covering master architecture, the hosting decision tree,
the project lifecycle, the security framework, the handover process and the
maintenance cycle. Browse the `.md` files directly rather than the PDFs, since
Mermaid does not always survive PDF conversion.

## Core principles

1. **A gate is something you can fail.** If every check passes every time, it is
   a form, not a gate.
2. **Never automate a broken process.** Automating a 40% exception rate produces
   an automation with a 40% exception rate and a maintenance bill on top.
3. **Ask whether it should be AI at all.** Deterministic costs less to run, never
   hallucinates, and can carry a real SLA. Reach for it first.
4. **Capture the baseline before you touch anything.** That window opens once.
5. **Silence is not health.** A working system reports that it is alive. Only
   broken systems are quiet.
6. **One instance per client.** Required by the licence, and required by blast
   radius.
7. **The client owns the credentials.** Always. Automations run under a named
   service identity the client created.
8. **Say what is unverified.** A cited claim with an honest gap beats a confident
   claim that falls apart in front of a client.

## Evidence standard

Every regulatory, pricing and platform claim in version 3.0 carries a grade.

| Grade | Meaning |
|---|---|
| A | Primary source, quoted and linked |
| B | Law firm, analyst or tier-one press, named and dated |
| C | Secondary reporting, directionally useful |
| U | Unverified. Do not put in front of a client |

Known weaknesses are listed openly at the end of the gap analysis, including
which sources could not be reached and which figures should not be quoted.

## What is still to come

Version 3.0 is a partial pass. The research is complete and the highest-risk
artifacts are written. These are specified in the gap analysis but not yet
written.

- Procurement Readiness Kit, TISAX and NIS2 supplier position
- DORA Article 30 contract annex
- Cost Model and Budget Guard
- Handover pack with per-workflow running cost notes

## Contributing

Issues and pull requests welcome. If you are correcting a fact, include the
primary source and the date. If you are adding a regulatory claim, include the
article or paragraph number.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Dual licensed.

- **Documentation, templates, checklists, guides and diagrams.** Creative
  Commons Attribution 4.0 International. Use it, adapt it, sell work built on it.
  Keep the attribution.
- **Code in `pdf-generator/`.** MIT.

Full terms in [LICENSE](LICENSE).

Suggested attribution.

> Based on the AI Workflow Delivery Framework by Mirza Iqbal, licensed under
> CC BY 4.0. https://github.com/mjmirza/AI-Workflow-Delivery-Framework

## Not legal advice

The contract language, compliance checklists and regulatory summaries here are a
practitioner's starting point, written by a practitioner and not by a lawyer.
Every legal artifact needs review by qualified counsel in the relevant
jurisdiction before it is used in a real engagement. Regulatory dates change.
Verify against the primary source before relying on any date printed here.
