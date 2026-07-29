# Template 10. AI and Maintenance Addendum

**Attach to the Retainer Agreement (Template 03) and reference from the SOW.**

This addendum exists because the base retainer template was written for
deterministic integration work. It does not say who pays when a security patch
breaks a delivered workflow, what happens when a model is retired, or how a
probabilistic system is accepted. Those three gaps are where automation
retainers lose money.

Everything below is drafting language for counsel to review, not legal advice.
Bracketed values are the ones to negotiate.

## 1. The security patch obligation

**The problem this closes.** Platform vendors ship severe vulnerabilities.
Patching forces an upgrade. The upgrade breaks delivered workflows. Without this
clause, the Supplier absorbs that remediation forever, or argues about it with
the Client every time.

> **1.1 Patch classification.** A Security Patch means a vendor release that
> remediates a vulnerability rated High or above by the vendor or by CVSS.
>
> **1.2 Notification.** The Supplier will notify the Client of any Security
> Patch affecting the delivered systems within **[2 business days]** of the
> vendor's disclosure.
>
> **1.3 Application window.** Unless the Client directs otherwise in writing,
> Security Patches will be applied within **[5 business days]** for Critical
> severity and **[15 business days]** for High severity, measured from
> disclosure.
>
> **1.4 Remediation of consequential breakage.** Where applying a Security Patch
> causes a delivered workflow to fail, malfunction or require rework, the
> remediation is **[chargeable at the rates in Schedule A / included up to
> [N] hours per quarter, chargeable beyond]**.
>
> **1.5 Client deferral.** If the Client directs that a Security Patch not be
> applied, that direction will be recorded in writing, and the Supplier's
> obligations under clause [X, availability] are suspended for the affected
> systems until the patch is applied.

**Negotiating note.** Clause 1.4 is the one that matters. Pick one of the two
options and say it out loud in the sales conversation rather than hiding it. An
included quarterly allowance is easier to sell than pure chargeable, and it caps
the Client's downside while protecting yours.

**Named owner.** Every retainer names one person on each side who owns patch
decisions. Write them into Schedule A. A patch decision with no owner does not
get made.

## 2. Model deprecation and substitution

**The problem this closes.** A delivered system pinned to a model has a hard
expiry date set by a third party. Anthropic commits to 60 days notice for public
models. OpenAI gives six months for GA models and as little as two weeks for
preview models. Somebody has to migrate, and it is billable work.

> **2.1 Model Register.** The Supplier maintains a Model Register listing each
> model in use, its provider, its published retirement date where known, and a
> nominated fallback.
>
> **2.2 Notification.** The Supplier will notify the Client within
> **[5 business days]** of a provider announcing the deprecation or retirement
> of a model in the Register.
>
> **2.3 Migration.** Migration to a replacement model is **[chargeable at the
> rates in Schedule A]**, and includes re-running the Acceptance Evaluation Set
> defined in clause 4 and reporting the result before and after.
>
> **2.4 No warranty of parity.** The Parties acknowledge that a replacement
> model may produce different output. The Supplier warrants only that the
> migrated system meets the thresholds in clause 4, not that behaviour is
> identical to the prior model.

**Commercial note.** Clause 2 is the strongest argument for a retainer that
exists in 2026. Without it the Client is one provider announcement away from a
broken system and no contracted route to fix it. Say that plainly in the sale.

## 3. Upstream change and schema drift

**The problem this closes.** The Client upgrades their CRM. Your workflow breaks.
You get blamed and repair it unpaid.

> **3.1 Integration Register.** The Supplier maintains a register of upstream
> systems the delivered workflows consume, listing the fields relied upon and
> their expected types.
>
> **3.2 Client notification duty.** The Client will give the Supplier
> **[10 business days]** notice of any planned change to an upstream system in
> the Integration Register, including version upgrades, field changes and
> permission changes.
>
> **3.3 Chargeable remediation.** Work required as a result of a change to an
> upstream system is a Change, chargeable at the rates in Schedule A, and is not
> covered by the warranty at clause [Y].
>
> **3.4 Undisclosed change.** Where an upstream change is made without the
> notice in clause 3.2, any resulting downtime is excluded from the availability
> commitment at clause [X].

## 4. Acceptance and service levels for probabilistic components

**The problem this closes.** You cannot write "the system shall correctly
classify tickets" for a probabilistic system without signing an unbounded
warranty. Deterministic acceptance language applied to an AI component is the
single most expensive drafting error available.

> **4.1 Split of components.** The delivered system comprises Deterministic
> Components and Probabilistic Components, identified in Schedule B. Different
> acceptance and service commitments apply to each.
>
> **4.2 Deterministic Components** are accepted on binary functional test, and
> carry the availability, latency and error-rate commitments at clause [X], with
> service credits as set out there.
>
> **4.3 Acceptance Evaluation Set.** For each Probabilistic Component the
> Parties will agree a fixed evaluation set of **[N]** cases drawn from the
> Client's real historical data, jointly owned, and frozen at the date of
> signature. Changes to the evaluation set require written agreement by both
> Parties.
>
> **4.4 Acceptance thresholds.** A Probabilistic Component is accepted when it
> meets or exceeds the thresholds in Schedule B when run against the Acceptance
> Evaluation Set. Thresholds are expressed as scores on named metrics, not as an
> absence of error.
>
> **4.5 Ongoing service level.** For Probabilistic Components the Supplier
> commits to a **service level objective**, not a service level agreement with
> credits. Where a monthly evaluation run falls below the threshold in
> Schedule B, the Supplier will investigate and remediate within
> **[10 business days]**. The remedy is remediation, not a service credit or
> refund.
>
> **4.6 Escalation rate.** Where the component routes to a human, the Parties
> agree an expected escalation rate in Schedule B. A rate materially above that
> figure is treated as a defect. A rate below it is not, of itself, evidence of
> quality.
>
> **4.7 No warranty of correctness.** The Supplier does not warrant that any
> individual output of a Probabilistic Component is correct. The Client
> acknowledges that such systems produce statistically distributed results and
> agrees that the thresholds in Schedule B are the measure of conformance.

**Drafting note.** Clause 4.5 is the distinction that clients respect once it is
explained. Uptime gets a credit because it is binary and controllable. Output
quality gets a remediation obligation because it is statistical. Blending the two
either exposes you to unbounded credits or leaves the Client with no remedy at
all.

## 5. Consumption costs and budget control

**The problem this closes.** Fixed-bid pricing does not survive open-ended agent
usage. Token and execution spend is variable, driven partly by Client behaviour,
and not something a Supplier can responsibly absorb.

> **5.1 Excluded costs.** The Fees exclude model inference charges, API charges,
> platform execution charges, storage and egress. These are Consumption Costs.
>
> **5.2 Account ownership.** Consumption Costs are incurred on accounts owned by
> the **[Client]**, billed directly to the Client. Where the Supplier's accounts
> are used, Consumption Costs are recharged at **[cost / cost plus N percent]**.
>
> **5.3 Budget limit.** The Parties agree a monthly Consumption Budget in
> Schedule A. The Supplier will configure spend limits and anomaly alerting to
> that figure.
>
> **5.4 Overrun.** The Supplier will notify the Client on reaching
> **[80 percent]** of the Consumption Budget within a billing period. The
> Supplier is not liable for Consumption Costs above the Budget where the
> overrun results from Client-initiated volume, changes to Client data, or
> Client changes to configuration.
>
> **5.5 Cost baseline.** The Supplier will record a cost-per-outcome baseline at
> acceptance and report against it **[quarterly]**.

**Note on runaway spend.** Agent loops are a documented failure mode capable of
producing very large bills in a short period. Clause 5.3 is not paperwork, it is
the control that stops it. Configure the limit before go-live, not after.

## 6. Credential custody and offboarding

> **6.1 Ownership.** All credentials used by the delivered systems are created
> by and belong to the Client. The Supplier will not embed credentials issued to
> a natural person, and will not use Supplier-owned credentials in production.
>
> **6.2 Service identity.** Each delivered automation runs under a named service
> identity created by the Client, so that actions are attributable.
>
> **6.3 Rotation on exit.** On termination, or on any change of Supplier
> personnel with production access, the Client will rotate every credential the
> departing party held or could have accessed. The Supplier will provide a list
> of affected credentials within **[2 business days]** of the trigger event.
>
> **6.4 Access removal confirmation.** Within **[5 business days]** of
> termination the Supplier will confirm in writing that all Supplier access to
> Client systems has been removed. The Client is entitled to verify this.

**Why 6.4 matters commercially.** Buyer-side vetting content names supplier
credential retention after delivery as a hard stop. Offering the confirmation as
a signed artifact removes a live objection before it is raised.

## 7. Platform dependency disclosure

> **7.1 Platform.** The delivered systems depend on **[platform name and
> version range]**, licensed under **[licence name]**.
>
> **7.2 Hosting.** The systems are hosted on **[the Client's instance / the
> Supplier's instance]**. Where hosted by the Supplier, the Supplier warrants it
> holds the licence entitlement required for that arrangement.
>
> **7.3 Version support.** The Supplier will notify the Client when the deployed
> platform version approaches end of vendor support, and will quote for the
> upgrade as a separate engagement.

**Note.** Clause 7.2 is not boilerplate. Several platform licences distinguish
between building on a client's own instance and hosting a client's workflows and
credentials on the supplier's. Confirm the entitlement in writing with the vendor
before signing a hosted arrangement.

## Schedule B skeleton

| Component | Type | Metric | Acceptance threshold | Monthly SLO | Escalation rate |
|---|---|---|---|---|---|
| | Deterministic | Functional pass | 100% | 99.[N]% uptime | n/a |
| | Probabilistic | Correctness | [4.0 of 5] | [3.8 of 5] | [15%] |
| | Probabilistic | Categorization | [0.92] | [0.90] | [10%] |

## Cross references

- `templates/03-retainer-agreement-template.md` for the base agreement
- `checklists/07-scoping-gate.md` for the checks that precede signature
- `guides/12-n8n-platform-reality-2026.md` for the platform facts behind clause 7
- `docs/GAP-ANALYSIS-2026.md` for the evidence behind each clause

## Legal note

Drafting language only. Every clause here needs review by qualified counsel in
the governing jurisdiction. German B2B contracts in particular limit what a
liability cap may say under §307 BGB, and the Werkvertrag versus Dienstvertrag
distinction changes the warranty position substantially. Do not sign any of this
without that review.
