# Guide 12. n8n Platform Reality 2026

**Last verified 2026-07-28. Every claim traces to a primary n8n source, linked
inline. Anything not confirmable from an n8n page is marked UNVERIFIED and must
not be quoted to a client.**

The platform changed underneath the rest of this framework between December 2025
and July 2026. Three of those changes alter what you may legally sell, what you
must re-test before an upgrade, and how you price the work.

## 1. The licensing exposure most agencies do not know they have

Read this before you quote another retainer.

n8n ships under the **Sustainable Use License, Version 1.0**, adopted
2022-03-17. It is not open source. The operative limitation, quoted from
[the license file](https://github.com/n8n-io/n8n/blob/master/LICENSE.md):

> You may use or modify the software only for your own internal business
> purposes or for non-commercial or personal use.

n8n's own support article,
[Which license do I need](https://support.n8n.io/article/can-i-use-your-license-for-my-use-case),
answers the consultancy question directly.

| What you are doing | n8n's stated answer |
|---|---|
| Helping a client set up and run **their own** n8n instance | "no commercial license would be required on your part" |
| Hosting the client's workflows and credentials **inside your own** instance | "an Enterprise license would be required" |
| Embedding n8n into your own product | "a white-labeled Embed license would be necessary" |

**The trap.** The common agency pattern of running one n8n box and putting
several clients' workflows and credentials on it is, by n8n's own answer, an
Enterprise license scenario. Many agencies are doing this today without one.

**The safe delivery model.** The client owns the instance. You build on it. You
are then a consultant providing services, which the license
[explicitly permits](https://docs.n8n.io/privacy-and-security/sustainable-use-license):

> Providing consulting services related to n8n, for example building workflows,
> custom features closely connect to n8n

This is also the right answer for the security reasons in section 3 and the
handover reasons in Guide 05. One instance per client is not only cleaner, it is
the licensed position.

Licensing questions go to license@n8n.io or sales@n8n.io. Get the answer in
writing before you sign a multi-tenant hosting arrangement.

**UNVERIFIED.** The figure of 50,000 USD per year for an Embed license
circulates on third party blogs. It appears on no n8n page this research could
fetch. Do not quote it. Ask sales.

### The Embed licence discrepancy, verified 2026-07-29

n8n's two sources now disagree with each other, and you should know that before
you rely on either.

On **2026-04-08** n8n landed a commit on the licence documentation page whose
subject was `fix(embed)`, removing the embed content and restructuring the page.
The page moved again in a docs restructure on 2026-06-24. As of 2026-07-29 the
[live licence page](https://docs.n8n.io/privacy-and-security/sustainable-use-license)
lists three limitations and two examples lists, and **contains no mention of an
Embed licence at all**. Under what is allowed it now says only this.

> Embedding n8n as a backend when using company credentials, not user credentials

Meanwhile the [support article](https://support.n8n.io/article/can-i-use-your-license-for-my-use-case)
still states that embedding n8n into your product to manage client workflows and
credentials means "a white-labeled Embed license would be necessary".

Both `docs.n8n.io/embed/` and `n8n.io/oem/` still return HTTP 200.

**What to do with that.** Do not present the Embed licence as settled either
way. The three consultancy scenarios in the table above are still confirmed live
on the support article, and those are safe to rely on. But for anything touching
embedding or white-labelling, get the position **in writing from
license@n8n.io** before you sign, and keep that email. A vendor whose own two
pages disagree is a vendor whose verbal answer is worth nothing later.

`LICENSE.md` in the n8n repository itself is unchanged since 2024-12-24, so the
underlying licence text has not moved. What moved is how n8n explains it.

## 2. The n8n 2.0 cut, and why an upgrade is a paid engagement

n8n 2.0 landed in December 2025. The changelog lists 2.0.0 on 2025-12-05, while
the [announcement post](https://blog.n8n.io/introducing-n8n-2-0/) describes a
beta on 2025-12-08 and stable on 2025-12-15. Both dates are recorded here rather
than resolved.

**1.x support ended around March 2026**, three months after the 2.0 release, per
that same post. Any client still on 1.x runs unsupported software, which matters
a great deal given section 3.

### The breaking changes that hit delivered client work

All from the
[official v2.0 breaking changes page](https://docs.n8n.io/changelog/v20-breaking-changes).

**Security defaults that flipped**

- Environment variable access is **blocked** in Code nodes,
  `N8N_BLOCK_ENV_ACCESS_IN_NODE=true`. Any workflow reading `process.env` fails.
  Move those values into credentials.
- `$evaluateExpression()` no longer works in Code nodes under secure mode.
- **ExecuteCommand and LocalFileTrigger are disabled** by default. Re-enable via
  `NODES_EXCLUDE` only with a documented reason.
- File access is restricted to `~/.n8n-files` by default via
  `N8N_RESTRICT_FILE_ACCESS_TO`. Affects ReadWriteFile and ReadBinaryFiles.
- **OAuth callback now requires authentication.**
  `N8N_SKIP_AUTH_ON_OAUTH_CALLBACK` flipped from true to false. Every OAuth
  credential needs retesting after the upgrade.
- Config file permissions enforced at 0600.
- Git node bare repositories blocked.

**Infrastructure**

- **MySQL and MariaDB support dropped entirely.** Migrate to PostgreSQL or
  SQLite.
- In-memory binary data mode removed. Plan disk capacity.
- The Pyodide Python Code node is replaced by a Python task runner that does not
  support the built-in variables or dot access notation the old one had.
- `n8n --tunnel` removed. Use ngrok, localtunnel or Cloudflare Tunnel.
- Release channels renamed from `latest` and `next` to `stable` and `beta`. n8n
  recommends pinning exact versions.

**Behaviour that breaks runbooks and training**

- **Activate and Deactivate became Publish and Unpublish.** Save preserves edits
  without touching production. Publish deploys. Any runbook, client training
  video or internal doc that equates "active workflow" with "live" is now wrong.
- The `--all` flag was removed from CLI publishing to prevent accidental mass
  production deploys. Any bulk deploy script you wrote is broken.
- **Sub-workflows now return the child's output** rather than its input when the
  child enters a waiting state. Any parent workflow expecting input breaks.
- The Start node is gone. Replace with Manual Trigger or Execute Workflow
  Trigger.
- **Four nodes deleted outright.** Spontit, crowd.dev, Kitemaker, Automizy.

### How to sell the migration

Treat it as a discrete, scoped engagement, not a favour inside a retainer. The
scoping artifact already exists. n8n ships a **Migration Report** at Settings
then Migration Report, for global admins on
[n8n 1.119.0 or later](https://docs.n8n.io/migration-tool-v2/). It must run
**before** the upgrade, on the 1.x instance. Run it, price from its output.

## 3. Security. The reason per client isolation is not optional

n8n disclosed multiple severe vulnerabilities in 2026. This turns shared hosting
from a preference into a liability.

| CVE | CVSS | Note |
|---|---|---|
| CVE-2026-21877 | 10.0 | Authenticated RCE. Cloud and self hosted |
| CVE-2026-25049 | 10.0 | Sandbox escape |
| CVE-2026-21858 | 10.0 | **Unauthenticated** RCE |
| CVE-2026-54052 | 9.6 | n8n-mcp IDOR, cross tenant credential theft |

A successful compromise exposes `N8N_ENCRYPTION_KEY` and therefore **every
credential stored on that instance**. On a shared agency instance that is a cross
client breach, and it converts a technical incident into a notification
obligation across your whole client base at once.

Three rules follow.

1. **One instance per client.** Required by the license in section 1. Now also
   required by blast radius.
2. **A patch SLA belongs in the retainer, with a named owner.** Security forces
   upgrades. Upgrades break delivered workflows per section 2. Somebody pays for
   that remediation and the contract must say who. This is the most common
   unpriced obligation in automation retainers.
3. **Secret sanitisation in agent memory only landed 2026-07-28** in v2.33.0.
   Any agent deployed before that date may have persisted secrets into memory.
   Audit existing agent deployments.

## 4. Evaluations. Your new acceptance criteria vocabulary

n8n has workflow evaluations built in. This is the most sellable new artifact in
the platform, because it turns "the AI works" from an argument into a number.

Supported metrics, from
[the metrics documentation](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality.md):

| Metric | Scale | Use |
|---|---|---|
| Correctness | 1 to 5, AI judged | Is the output right |
| Helpfulness | 1 to 5, AI judged | Is the output useful |
| String Similarity | 0 to 1 | Deterministic text comparison |
| Categorization | 1 or 0 | Exact match classification |
| Tools Used | 0 to 1 | Did the agent call the right tools |
| Custom | any | Your own metric |

**Tier gating to surface at scoping, not at delivery.** Quoted from that page,
"Metric-based evaluation is available on Pro and Enterprise plans." Community and
Starter get it for a single workflow only. Test case concurrency runs 1
sequential on Community and Pro, 3 on Business, 5 on Enterprise.

Note this is a **different tier axis** from Source Control, which is Business and
Enterprise. Do not conflate the two when advising a client on plan choice.

n8n's own guidance is to build the dataset from **real historical execution
data** rather than hand written happy paths.

The `Check If Evaluating` operation on the Evaluation node is the primitive that
matters most in delivery. It lets you branch to mocks during an evaluation run so
a test never touches the client's live CRM.

The evaluation run page shows trend deltas against the previous run. **That delta
is a defensible regression gate for a retainer SLA.**

## 5. Handover primitives that now exist

### Workflow packages, the `.n8np` file

Shipped in v2.27 on 2026-06-16.
[Documentation](https://docs.n8n.io/build/manage-workflows/n8n-packages).

A `.n8np` file is a tar archive containing `manifest.json` and a `workflows/`
directory. Note, quoted from the docs, "n8n never includes credential secrets in
a package." Credential stubs carry only ID, name and type for matching on the
target instance.

```
n8n-cli package export --workflow-id=<id> --output=export.n8np
n8n-cli package import --file=export.n8np --conflict-policy=fail
```

**Do not make this your only handover mechanism yet.** It is Beta, the docs warn
that "breaking changes may occur without a major version bump", and it does not
support sub-workflows, error workflows, data tables, folders or projects. Pair it
with Git source control, which requires the Business plan.

### The Community Edition path, when the client has no Business plan

Most SMB clients sit on Community or Starter, where Source Control does not
exist. The CLI is the fallback and it works everywhere.

```
n8n export:workflow --backup --output=backups/latest/
n8n import:workflow --separate --input=backups/latest/ --activeState=fromJson
```

Two landmines, both documented.

- Export includes IDs. Quoted from the docs, "If you have workflows and
  credentials with the same IDs in your existing database, they will be
  overwritten." **ID collision is the number one promotion hazard.**
- `import:workflow` **deactivates every imported workflow by default** unless
  `--activeState=fromJson`, which itself requires multi-main or queue mode.

Version history retention is also tier-dependent. 24 hours for everyone including
Community, 5 days on Cloud Pro, full history on Enterprise. **Below Enterprise,
Git is the only real rollback mechanism.** That is the concrete argument for
source control in a proposal.

### Permission scopes that make handover safe

- `workflow:execute` became a separate scope in v2.11.0 on 2026-03-02. A client
  can run workflows without being able to edit or publish them. This is the scope
  you want for most client users at handover.
- Personal space policies arrived in v2.8.3 on 2026-02-13, controlling sharing
  and publishing from personal spaces. Use them to stop shadow automation
  accumulating outside the project.
- Granular workflow permissions in custom project roles, v2.2.0 on 2025-12-22,
  separate editing from publishing.

All Enterprise tier.

### The ownership transfer trap

From [share with others](https://docs.n8n.io/build/manage-workflows/share-with-others).
**Moving a workflow or credential removes all existing sharing.** Transfer
ownership at handover and you silently sever every share you configured. Verify
access after every move, and put that verification in the handover checklist.

## 6. Observability is now built in

- **OpenTelemetry traces** for workflow executions shipped in v2.15.0 on
  2026-03-30, via `N8N_OTEL_ENABLED` and an OTLP endpoint. Span attributes
  include workflow ID, execution ID, status, duration, node count and project.
  UI configuration followed in v2.27 on 2026-06-16.
- **Insights retention** rose to 365 days, configurable to 730 via
  `N8N_INSIGHTS_MAX_AGE_DAYS`, in v2.20.0 on 2026-05-05.
- **Prometheus metrics** on `/metrics` via `N8N_METRICS=true`. Self hosted only,
  not available on n8n Cloud.

Caveat for every proposal. The OpenTelemetry GenAI semantic conventions are still
pre stable, with most `gen_ai.*` attributes carrying Development stability
badges. Promise the client an OpenTelemetry **shaped** trace schema with a
documented migration allowance, never a "standards compliant" one. Budget for a
re-instrumentation event.

**Configure the Insights time-saved figure at handover.** It is the single most
client-legible number n8n produces, and if you skip it the client never sees ROI
in the product they are already paying for.

## 7. Task runners. The Code node became infrastructure

From
[the task runner documentation](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners).

Internal mode runs the runner as a child process sharing the same user ID and is
documented as unsuitable for production. **External mode is the production
posture**, using a separate `n8nio/runners` sidecar container.

Constraints that bite.

- The runners image **must match the n8n version exactly**.
- Requires n8n 1.111.0 or later. Extended images need 1.121.0 or later.
- Python dependencies install by extending the base image and are allowlisted
  with `N8N_RUNNERS_STDLIB_ALLOW` and `N8N_RUNNERS_EXTERNAL_ALLOW`.

**Commercial consequence.** Any client running Python in a Code node now needs a
maintained container build pipeline, pinned to their n8n version, rebuilt on
every upgrade. That is a standing DevOps obligation. Price it into the retainer
rather than absorbing it.

## 8. MCP in delivered systems

One click MCP servers arrived in v2.22.0 on 2026-05-19 covering Apify, Linear,
monday.com, Notion and PostHog. OAuth for the MCP Server Trigger followed in
v2.25.1 on 2026-06-02. In v2.33.0 on 2026-07-28, MCP connection failures became
non blocking for agents.

**Two things for the architecture document.**

1. **Queue mode routing constraint.** With multiple webhook replicas, all
   `/mcp*` requests must route to a single dedicated replica. nginx needs proxy
   buffering off, gzip off, chunked encoding off, and an empty Connection header.
   This is an infrastructure requirement, not a workflow detail. Source,
   [the MCP Server Trigger docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger).
2. **The MCP specification changed on 2026-07-28**, moving to a stateless core.
   Any MCP server you ship is a versioned dependency with a breaking change in
   flight. Pin it, record its provenance in the deliverable inventory, and review
   any third party MCP server for supply chain risk. Malicious MCP packages have
   been confirmed in the wild since September 2025.

## 9. Community nodes carry named risk

From
[the community node risk page](https://docs.n8n.io/integrations/community-nodes/risks/),
unverified community nodes are "unverified code from a public source" with three
named risks, system access, data access, and breaking changes. Verified community
nodes are vetted by n8n and "must meet a set of data and system security
requirements for approval".

Self hosted instances can disable them entirely with
`N8N_COMMUNITY_PACKAGES_ENABLED=false`. For a regulated client that should be the
default, with named exceptions approved in writing.

Every community node in a delivered workflow belongs in the deliverable inventory
with its version pinned and its maintenance status noted.

## 10. Commercial context for a DACH sales conversation

**SAP made a strategic investment in n8n on 2026-05-12 at a 5.2 billion USD
valuation**, more than double the prior 2.5 billion, and plans to embed n8n
directly inside Joule Studio. Source,
[n8n's own announcement](https://blog.n8n.io/n8n-sap/).

That same post states 1.7 million monthly active builders and over 1,400
enterprise customers.

For a German enterprise procurement conversation this is the strongest asset in
this guide. It moves n8n from "an open source tool the team likes" to "the
automation layer SAP is embedding", which is a very different discussion with a
risk-averse buyer.

**UNVERIFIED and not to be quoted.** The reported 60 million USD investment
figure and the Q3 2026 Joule Studio timing come from secondary coverage. ARR
figures circulating between 40 million and 100 million USD are third party,
mutually contradictory, and unsourced.

## 11. Cloud pricing as of 2026-07-28

From [n8n.io/pricing](https://n8n.io/pricing/), annual billing.

| Plan | Price | Executions per month | Projects | Insights | Notable |
|---|---|---|---|---|---|
| Starter | 20 EUR | 2,500 | 1 shared | none | 2,300 AI credits |
| Pro | 50 EUR | 10,000 | 3 shared | 7 day | admin roles, workflow history |
| Business | 667 EUR | 40,000 | 6 shared | 30 day | **SSO, SAML, LDAP, Git version control** |
| Enterprise | custom | custom | unlimited | 365 day | dedicated support with SLA |

Two things to say in every proposal.

- **Pricing is per execution, not per step.** Quoted from the pricing page, "An
  execution is a single run of your entire workflow. It doesn't matter how many
  steps are in the workflow or how much data it processes, it's still a single
  execution." That is the standing competitive argument against Make and Zapier
  and it belongs in your comparison slide.
- **The Pro to Business jump is where environments live.** Git version control
  and SSO first appear on Business at 667 EUR per month. Any client who wants
  dev, staging and production, or source control, is a Business client minimum.
  Surface that at scoping. Discovering it at delivery is a painful conversation.

**AI credits fund n8n's own Assistant, not the client's agents.** The client's AI
Agent nodes bill separately against their own provider keys. State this
explicitly in the proposal or you will be asked why the OpenAI invoice arrived.

## 12. The tier-fit matrix, a one page proposal asset

Capability gating is spread across three different plan axes. Put this in the
proposal so the client picks a plan with open eyes.

| Capability | Minimum requirement |
|---|---|
| Metric-based evaluations | Pro. Single workflow only on Community and Starter |
| Git source control and environments | Business |
| SSO, SAML, LDAP | Business |
| Full version history and rollback | Enterprise |
| External secrets vaults | Enterprise self hosted or Enterprise Cloud |
| Log streaming to SIEM | Enterprise |
| Scoped API keys | Enterprise |
| Granular project roles, personal space policies | Enterprise |
| Prometheus `/metrics` endpoint | Self hosted, any tier. Not on Cloud |
| Worker visibility in the UI | Self hosted Enterprise |

Below Enterprise an API key is effectively full-instance admin, because scoped
API keys are Enterprise-only. That belongs in the client's security briefing.

## 13. The documentation restructure, a cheap audit worth running

The n8n docs site was reorganised during this window. These paths now 404.

- `/release-notes/` moved to `/changelog/`
- `/advanced-ai/` moved to `/build/integrate-ai/`
- `/sustainable-use-license/` moved to `/privacy-and-security/`
- `/hosting/scaling/` and `/hosting/configuration/` moved to `/deploy/host-n8n/`

Any client runbook, wiki page, onboarding document or SOW annex linking the old
paths is broken right now. Grep your delivered documentation for
`docs.n8n.io/release-notes`, `docs.n8n.io/hosting` and `docs.n8n.io/advanced-ai`.
Fifteen minutes of work with high client-visible value.

## 14. Model provider changes inside n8n

From the [changelog](https://docs.n8n.io/changelog/).

| Provider | Version, date | Change |
|---|---|---|
| Moonshot Kimi | 2.17, 2026-04-13 | New. Chat, tools, web search, thinking mode |
| Alibaba Model Studio | 2.17, 2026-04-13 | New. Qwen family, vision, image, video |
| MiniMax | 2.18, 2026-04-21 | New. Chat, image, video, speech |
| Google Gemini | 2.19, 2026-04-28 | Defaults moved to gemini-3-flash-preview |
| AWS Bedrock | 2.26, 2026-06-09 | Assume Role via STS, removes long lived keys |
| Anthropic | 2.27, 2026-06-16 | Opt in SSE streaming |
| xAI Grok | 2.30, 2026-07-07 | Reasoning effort and priority options |
| AWS Bedrock | 2.32, 2026-07-21 | **Max Retries fix for agents hanging indefinitely** |

That last one matters operationally. A hanging agent burns executions and
presents to the client as an outage. It is a concrete reason to push clients past
2.32.

For regulated clients, **Bedrock Assume Role via STS should be the default**
because it removes long lived AWS keys from the credential store.

## Cross references

- `docs/GAP-ANALYSIS-2026.md` for the full findings register behind this guide
- `guides/02-security-implementation.md` for the credential posture
- `guides/05-handover-delivery.md` for the handover package

## Verification note

Compiled 2026-07-28 from primary n8n sources. The platform moves weekly. Before
quoting any version number, price or date to a client, re-check the linked
source. Items marked UNVERIFIED were not confirmable from an n8n page and must
not appear in client facing documents.
