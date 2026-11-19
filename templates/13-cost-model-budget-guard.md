# Template 13. Cost Model and Budget Guard

The sheet you fill before go-live, and the controls you actually switch on.
Attach it to the handover. Keep it current through the retainer.

Clause 5 of `templates/10-ai-maintenance-addendum.md` says the fees exclude
consumption, that the client owns the accounts, and that a monthly budget, an
alert and a cost-per-outcome baseline will exist. This template is how that
clause becomes true. A limit written in a contract and never configured is not
a limit.

**Verified against primary docs on 2026-11-19.** Platform behaviour moves.
Re-read the linked pages before you quote a number to a client. Anything this
file does not confirm from those pages is marked.

## Why this exists

The build fee is bounded. Consumption is not. Model calls, tool APIs and
platform executions are driven partly by the client's own volume, and an agent
that loops can spend that volume in an afternoon.

n8n does not have a currency cap on model spend. The cap lives at the provider,
or, on two Cloud plans, in a prepaid credit balance. This sheet records which
one is in use, the number, who is told, and what the workflow does when the
number is hit.

## The three bills

Keep them in separate rows. Adding them into one "AI cost" hides which brake
you can pull.

| Bill | What it meters | Where the brake is |
|---|---|---|
| Model and tool APIs | Tokens, requests, tool calls | The provider console, on a project or a workspace. Not on a single key |
| n8n executions | Production runs of a published workflow | The plan's execution quota, plus timeout and iteration caps inside the workflow |
| Gateway credits, if used | Per-request charges on n8n's gateway, prepaid | A monthly auto top-up limit in the Cloud console. One balance for the whole instance |

Storage, egress and the SaaS products a workflow calls sit in the first row
when they are metered, and in their own row when they are a flat subscription.
Say which.

## Part A. The cost model

One row per delivered workflow. Fill it from a measured sample, not from a
guess you made in the sales call. Run a representative batch on the test
project, read the provider's usage page, and scale.

| Field | What to write |
|---|---|
| Workflow | Name, and the n8n workflow id |
| Outcome | The unit a business owner recognises. One classified ticket. One invoice posted. Not "one execution" |
| Volume | Expected outcomes per month, and the source of that number |
| Trigger | What starts a production run, and how often |
| Billing path | Own provider key, or Gateway credits |
| Model calls per outcome | Measured, including retries and agent rounds |
| Tokens per outcome | Input and output, measured |
| Other metered calls | Search, scrape, parse, paid SaaS. Count and price |
| Provider estimate | Currency per month |
| n8n executions | Parent production runs per month. See the counting rules below |
| n8n allocation | How the plan fee is attributed to this workflow |
| Cost per outcome | The formula in Part E, computed |
| Cap | The hard limit that applies, and where it is configured |
| Owner | Named human who receives the alert |

### Worked example

Numbers below are an illustration of the arithmetic. They are not a price, a
benchmark, or a quote.

| Field | Example |
|---|---|
| Workflow | Ticket classifier, id `abc123` |
| Outcome | One ticket labelled and written back to the helpdesk |
| Volume | 4,000 tickets a month, from the client's helpdesk export for the last full month |
| Trigger | Webhook, one inbound request per ticket |
| Billing path | Client's OpenAI project `ticket-classifier`, own key |
| Model calls per outcome | 1.2 measured, the extra 0.2 from a tool round on a fifth of tickets |
| Tokens per outcome | 900 input, 120 output, measured on 50 tickets |
| Provider estimate | 4,000 times the published price for that model and that token mix |
| n8n executions | 4,000 parent production runs. Manual tests during the sample are excluded |
| n8n allocation | Plan fee times 4,000 divided by the instance's total production runs |
| Cost per outcome | Provider estimate plus n8n allocation, divided by 4,000 |

### How n8n counts an execution

From the executions documentation, read 2026-11-19. Only **production**
executions count toward a paid plan's quota. A production execution is a run
started by a trigger, a schedule or a poll.

| Starts a run | Counts toward the quota |
|---|---|
| Schedule Trigger | Every time it fires, including a run that does nothing useful |
| Polling trigger | Only when it finds new data. An empty poll does not count |
| Webhook | Every request that starts the workflow, including an empty body. A request rejected before the workflow starts does not count |
| Manual run from the editor | No |
| Execute Sub-workflow | No. Only the parent run counts |
| Error workflow | No |

A chat workflow is not "one execution a month". It is one production execution
per conversation that the trigger starts, and a model call on every turn inside
it. Estimate both, or the execution quota and the token bill will surprise
different people.

**Do not read Insights as the invoice.** Insights is an observability view. It
includes figures the quota excludes, and the date range on Pro is short. The
number you put in this sheet comes from the execution list filtered to
production runs, and from the provider's usage page.

Plan names and included execution counts move, and n8n's pricing page and its
Cloud support articles have not always used the same tier names. Read the
client's plan in the Cloud admin on the day you quote. Do not copy a tier out
of an old proposal.

## Part B. Where the cap actually lives

### Own keys, which is the default

The client owns the provider account. Guide 03 and clause 5.2 already say this.
The structure under that account is what stops one use case spending another's
money.

**OpenAI.** A hard spend limit is set on an organization or a **project**, not
on a key. A second key in the same project shares the project's budget. Spend
alerts send a notification and let traffic continue. Traffic stops only when
**Enforce a hard limit** is on. At that point requests fail with HTTP 429 and
`project_spend_limit_exceeded` or `organization_spend_limit_exceeded`.
Enforcement is not instantaneous, so recorded spend can sit slightly over the
number. Source: OpenAI spend limits, read 2026-11-19.

One project per use case. Test and production are different projects, and the
test project's hard limit is small enough that a forgotten evaluation run
cannot matter. Put one key in each project. Record the project id, the monthly
amount, and that the hard limit is on.

**Anthropic.** The equivalent boundary is a **workspace** monthly spend limit,
set in the Claude Console under Spend limits. It cannot be higher than the
organization limit. A limit you set returns HTTP 400, `invalid_request_error`,
with a message that begins "You have reached your specified API usage limits"
or the workspace variant of that sentence. The tier cap Anthropic sets (Start,
Build, Scale, and no monthly cap on Custom) is a separate control and returns
429. A spend limit on the default workspace does not reliably stop console,
Claude Code or managed-agent usage in that workspace. Do not put a production
workflow on the default workspace and call it capped. Source: Anthropic rate
limits and workspaces, read 2026-11-19.

**Every other provider.** Find the hard monthly cap in that console and paste
its URL into the register. Do not assume a per-key budget exists. If the only
control you can find is an email alert, write "alert only, no hard cap" in the
cap column and do not tell the client the downside is bounded.

### Gateway credits, Cloud Starter and Pro only

From n8n 2.36.0, Cloud Starter and Pro can run supported models and tool
services by selecting **Use Gateway credits** on the node, with no provider
key. n8n bills a prepaid balance at the rates on its service pricing page.
Enterprise and self-hosted do not have this. Assistant credits are a different
balance and do not pay for workflow nodes.

Treat this as a deliberate choice, recorded in the sheet, not as the default.

- The balance is **one pool for the instance**. A loop in one workflow spends
  the credit the others were going to use. You cannot isolate use cases the way
  an OpenAI project can.
- When the balance hits zero, nodes on Gateway credits fail. Nodes on your own
  keys keep running. In-flight requests are allowed to finish, and the
  overspend is taken off the next top-up, so the balance can dip below zero.
- **Auto top-up without a monthly limit is an open card.** Turn auto top-up on
  only with **Monthly auto top-up limit** set to the Consumption Budget in
  Schedule A. When that limit is reached, auto top-up pauses until next month.
  That pause is the hard cap. A prepaid balance on its own is not, because
  anyone with the owner's payment method can keep filling it.
- Top-ups are final, expire after 12 months, and are forfeited if the n8n
  account is closed. The client owns the Cloud instance, so the client owns
  that balance.
- Prompts sent this way go out under n8n's provider account. The provider sees
  the content and not the client's identity. For a client with a DPA or a works
  council in scope, that path is a sub-processor question. Own keys keep the
  provider relationship in the client's name. Flag it at scoping. Do not decide
  it for them.

Source: n8n Gateway credits, top-up, and use-gateway-credits docs, read
2026-11-19.

### The n8n execution quota

There is no per-workflow currency cap on executions. The quota is for the
instance. A webhook an attacker, or a buggy client system, can call will spend
the month's executions for every workflow on that instance.

The brakes that do exist are in the workflow, below, and in the plan's
concurrency and maximum duration. Those plan figures live on the current
pricing page. Copy them into the sheet from that page, with the date you read
it.

## Part C. Caps inside the workflow

Set each of these explicitly. An unset option uses a default, and a later node
version can change what "unset" means. The value belongs in the register.

**Max Iterations on every AI Agent node.** The Tools Agent option defaults to
10. This framework's range is 5 to 10. Start at the low end. Record the number
you actually saved on the node.

When the cap is hit the node stops the run. Current source throws
`Max iterations (N) reached. The agent could not complete the task within the
allowed number of iterations.` That failure means the agent is not converging.
Turn on **Return Intermediate Steps**, see which tool it is calling again, and
fix the tool description or the system message. Raising the cap because the run
hit it is how a loop becomes a bill. Raise it only when the task genuinely
needs more rounds, with the new number and the reason written on this sheet.

Max Iterations counts n8n agent rounds. It does not count tokens. On the OpenAI
Chat Model node, **Use Responses API** lets the model run its own tool loop
inside a single request, so one round can still be an expensive call. Read the
provider usage, not only the iteration count.

**Workflow timeout.** On self-hosted n8n, `EXECUTIONS_TIMEOUT` defaults to `-1`,
which is no timeout. Set a default in seconds, and set a shorter timeout on
each agent workflow, up to `EXECUTIONS_TIMEOUT_MAX` (default 3600). On Cloud,
the plan's maximum execution duration is the ceiling. A timeout stops further
work. It does not refund model calls already made.

**No retry around a spend-limit error.** A 429 or 400 from a spend cap is the
brake working. Retrying it in a loop defeats the brake and, where the provider
enforcement lags, keeps spending. Retry transient rate limits with a small,
finite count. Do not retry `project_spend_limit_exceeded`,
`organization_spend_limit_exceeded`, an Anthropic usage-limit 400, or a Gateway
credits balance of zero.

**Paid tools go through the Autonomy Matrix.** A tool that spends money, sends
something, or cannot be undone is a human-approval tool. n8n can gate tool
calls on the AI Agent node. The decision rule is in template 11. A rate limit
on that row is a cost control as well as a safety control.

**Evaluation runs use the test project.** Metric-based evaluations call the
model and can run on a schedule. Point them at the test credential, on the test
project's small hard limit. A nightly evaluation against the production key is
a second production bill nobody put in the model.

## Part D. When the cap trips

The workflow fails. That is the correct outcome. Silence, or a success status
with nothing done, is the failure mode checklist 08 exists to catch.

- The error workflow routes a spend-limit failure to the named owner the same
  day. It does not swallow it, and it does not retry it.
- Raising the limit is the client's decision, written down, before anyone
  changes the console. It is not a favour done on a Friday so the queue clears.
- Clause 5.4 declines supplier liability for consumption above the budget where
  the overrun comes from client volume or client configuration. That exclusion
  does not cover a loop, an unbounded retry, or a missing cap that the supplier
  shipped. If the sheet shows the cap was never turned on, the conversation is
  yours.

## Part E. Cost per outcome

Record this at acceptance, on the frozen window you agree, and report it on the
cadence in clause 5.5. The default there is quarterly. You cannot reconstruct
the acceptance window later.

```
cost per outcome
  = (provider spend + gateway-credit spend + allocated n8n plan fee
     + other metered pass-through)
    / count of accepted outcomes in the same window
```

State the allocation method in the sheet and do not change it between reports.
Two that stay comparable:

- Flat plan fee. This workflow's share is the fee times its production
  executions divided by the instance's production executions.
- Overage priced per thousand. Use the overage rate for executions above the
  included amount, and the flat-fee method for the included amount.

An outcome that a human rejected, or that the evaluation threshold failed, is
not in the denominator. Those still sit in the numerator. That is the point. A
unit cost that only counts the successes you liked will fall as quality falls.

The client signs the baseline. The retainer is then a comparison against a
number both sides already accepted, which is the conversation guide 08 section
1.0.4 is describing.

## Part F. The anomaly watch

The 80 percent alert in clause 5.4 tells you the month is filling up. It does
not tell you that Tuesday was twenty times a normal Tuesday. A generous monthly
cap can be exhausted in a day, and the alert arrives after the money is gone.

Run both.

| Signal | Starting point | What it is not |
|---|---|---|
| Budget threshold | Alert at **[80 percent]** of the monthly hard limit | Not a cap. The hard limit is the cap |
| Daily rate | Provider spend, or this workflow's production executions, above **[3 times]** the acceptance-week daily average | Not a breach. A prompt to look the same business day |

The bracketed figures are the ones clause 5 uses as a starting point. Replace
them in Schedule A and use the same numbers here.

The watch itself is retainer work under clause 5. A loop caused by a provider
outage, a client data change, or a model that started calling a tool twice, is
investigated and reported. Repair that is a build change is quoted. Do not
absorb it into "keeping an eye on things".

Review monthly even when nothing tripped. Read the provider usage page and the
production execution count. Write the actuals next to the estimate. A model
that has drifted to twice the tokens per outcome is a register event for
template 11 as well as a cost event.

## Go-live gate

This one can fail. Do not publish the workflow while any line is open.

- [ ] Billing path chosen and written down. Own keys, or Gateway credits
- [ ] Client owns the provider account, and the n8n instance
- [ ] One OpenAI project or Anthropic workspace per use case, production
      separate from test, production not on a default workspace
- [ ] Hard limit on, not an alert alone. Amount matches Schedule A
- [ ] If Gateway credits: monthly auto top-up limit on, equal to the budget.
      Auto top-up with no monthly limit is a NO-GO
- [ ] Alert at the agreed percentage, to a named human
- [ ] Daily rate watch configured, with the multiple and the baseline week
- [ ] `maxIterations` set explicitly on every AI Agent node, value recorded
- [ ] Workflow timeout set
- [ ] No retry on a spend-limit error
- [ ] Paid and irreversible tools gated, per template 11
- [ ] Evaluation runs pointed at the test project
- [ ] Cost model row filled from a measured sample
- [ ] Cost-per-outcome baseline computed and signed
- [ ] Error workflow routes a cap failure to the named owner
- [ ] Test credentials removed from the production workflows

**Verdict.** GO / NO-GO
**Client.** ______________ **Date.** ______________
**Supplier.** ______________ **Date.** ______________

## Sources

Read 2026-11-19.

- n8n, Tools Agent, Max Iterations default of 10.
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent
- n8n source, the error thrown when the iteration cap is reached.
  `packages/@n8n/nodes-langchain/nodes/agents/Agent/agents/ToolsAgent/V3/helpers/checkMaxIterations.ts`
- n8n, how executions count toward a quota.
  https://docs.n8n.io/build/understand-workflows/understand-executions
- n8n, workflow timeout environment variables. `EXECUTIONS_TIMEOUT` default
  `-1`, `EXECUTIONS_TIMEOUT_MAX` default `3600`.
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-workflow-timeouts
- n8n, Gateway credits, including plan availability from 2.36.0 and the single
  shared balance.
  https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits
- n8n, auto top-up and the optional monthly auto top-up limit.
  https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits/top-up-gateway-credits
- OpenAI, spend alerts versus hard spend limits, project and organization scope.
  https://developers.openai.com/api/docs/guides/spend-limits
- Anthropic, organization and workspace spend limits, and the errors each
  returns.
  https://platform.claude.com/docs/en/api/rate-limits
- Anthropic, workspace limits cannot exceed the organization, and the default
  workspace caveat.
  https://platform.claude.com/docs/en/manage-claude/workspaces

## Cross references

- `templates/10-ai-maintenance-addendum.md` clause 5, the contract language
- `guides/08-pricing-estimation-guide.md` section 1.0, why the build fee does
  not absorb this
- `guides/03-api-key-management.md`, client-owned accounts and the test versus
  production split
- `templates/11-model-register-autonomy-matrix.md`, the per-tool decision that
  caps paid actions
- `checklists/08-silent-failure.md`, so a capped run is visible rather than quiet
- `docs/GAP-ANALYSIS-2026.md` section 2.3
