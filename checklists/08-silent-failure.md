# Checklist 08. Silent Failure

**Silence is not health. A working system reports that it is alive. Only broken
systems are quiet.**

This is the most reported production problem in the n8n practitioner community.
The shape is always the same. The workflow reports success, the client discovers
the breakage, and you find out last.

> your HubSpot node failed, your CRM row was never created, your client never
> got the email, and n8n's execution log shows success

Every item here is a real, documented way a delivered workflow dies without
telling anyone. Run this before handover, and again quarterly on every retainer.

## The nine silent deaths

Work through these per workflow. Each one has produced a live client incident.

| # | Failure | Check | Fixed |
|---|---|---|---|
| 1 | **No error workflow attached** | Settings, Error Workflow is set on this specific workflow | [ ] |
| 2 | **Workflow unpublished** | It is Published, not merely Saved | [ ] |
| 3 | **Manual test passed, schedule fails** | Triggered it on its real schedule at least once | [ ] |
| 4 | **Multiple cron expressions in one trigger** | One Schedule Trigger, one expression | [ ] |
| 5 | **No timezone set** | Timezone is explicit, not inherited | [ ] |
| 6 | **Alternate entry point skips validation** | Every entry path hits the same validation | [ ] |
| 7 | **The instance itself died** | External uptime check exists | [ ] |
| 8 | **Credentials expired** | Expiry date recorded, renewal reminder set | [ ] |
| 9 | **Upstream data changed shape** | Shape validation on input, fails loudly | [ ] |

Number 1 is the one people forget. **The error workflow node alone does nothing.**
It is a passive listener. Every production workflow must point at it individually
under Settings, Error Workflow. A repo full of error workflows nobody attached is
the most common version of this whole problem.

## The garbage-success trap

The nastiest case is not an error. It is a run that completes cleanly having done
nothing.

- [ ] Zero items processed is treated as a failure, not a success, wherever zero
      is not a legitimate outcome
- [ ] The workflow asserts the **shape** of what it produced, not only that it
      finished
- [ ] `Continue On Fail` is used deliberately, and every place it is set has a
      downstream check that catches the swallowed error
- [ ] A `Stop And Error` node routes business-rule violations into the same
      alerting path as technical failures

Quoting a practitioner on the worst variant, the scheduled workflow that never
fired at all, **nothing reads as zero because nothing executed**. That is what
heartbeat monitoring exists to catch.

## The error workflow pattern

Build it once, attach it everywhere.

**Primary error workflow.**

- [ ] Error Trigger, then alert to the channel the client actually watches
- [ ] Also writes to a durable log, so patterns are visible over time
- [ ] Includes workflow name, execution URL, failing node, and the error message
- [ ] Does not include credential values or personal data in the alert body

**Backup error workflow.** The primary one can fail too.

- [ ] A second, minimal workflow whose only job is a plain email
- [ ] Set as the error workflow **of the primary error workflow**
- [ ] Tested by deliberately breaking the primary alert channel once

n8n does not recursively trigger error workflows, so this cannot loop.

**Know the payload shape.** The Error Trigger receives a different object when
the failure is in the trigger node itself. Handle both.

- [ ] Handles the normal shape with `execution.id` and `execution.url`
- [ ] Handles the trigger-failure shape, where those fields are absent
- [ ] Does not assume `execution.url` exists. It requires the execution to have
      been saved to the database

## The conformance monitor

This is the check with no published competitor, and it turns the pattern above
from a convention into a guarantee.

Build a meta-workflow that runs weekly and reports any workflow which conforms to
neither the global nor a local error pattern.

- [ ] Lists every workflow on the instance via the public API
- [ ] Flags any with no error workflow assigned
- [ ] Flags any that is unpublished but was expected to be live
- [ ] Flags any schedule-triggered workflow with no timezone
- [ ] Sends one digest per week, to a named owner
- [ ] Its own failures route to the backup error workflow

Without this, item 1 in the nine deaths regresses quietly every time somebody
adds a workflow.

## Heartbeat monitoring

Metrics answer whether the instance is healthy. They do not answer whether the
6am invoice sync actually ran. That needs a dead man's switch, where **silence is
treated as failure**.

- [ ] Every schedule-triggered workflow has a push URL, from Healthchecks.io,
      Uptime Kuma or equivalent
- [ ] The expected window matches the real schedule, with a sensible grace period
- [ ] The ping is the **last** step, so it only fires on a genuine full success
- [ ] The ping fires after the shape assertion, not before it
- [ ] A register lists every workflow, its schedule, its push URL and its owner

**The register is the deliverable.** A monitor nobody can enumerate is a monitor
nobody maintains.

| Workflow | Schedule | Timezone | Push URL | Grace | Owner |
|---|---|---|---|---|---|
| | | | | | |

## Alert routing

Alert volume is what kills alerting. Split by severity or the client stops
reading.

- [ ] **Immediate.** Client-visible failure, money or data at risk. Goes to a
      channel a human watches, now
- [ ] **Daily digest.** Transient errors that self-recovered, retry successes,
      approaching quota
- [ ] **Weekly.** The conformance monitor output, cost trend, evaluation drift
- [ ] Each route has a **named human**, not a shared inbox nobody owns
- [ ] The client has been told which is which, in the handover session

## Before handover

- [ ] Every workflow passes the nine deaths table
- [ ] The conformance monitor is live and has produced one clean run
- [ ] The heartbeat register is complete and every entry has fired once
- [ ] The alert routing map is signed off by the client
- [ ] The client has seen a **deliberately triggered failure** end to end, and
      watched the alert arrive
- [ ] The runbook covers the top three expected failures per workflow

That second-to-last item matters more than the rest. A client who has never seen
the alerting work does not believe in it, and will not act on it at 3am.

## Quarterly, on every retainer

- [ ] Re-run the nine deaths table on any workflow changed since last quarter
- [ ] Review the conformance monitor digest for anything flagged more than twice
- [ ] Confirm every heartbeat has fired inside its window all quarter
- [ ] Check credential expiry dates against the register
- [ ] Confirm alert routing still points at people who still work there

## Cross references

- `checklists/04-qa-testing-checklist.md` for the pre-delivery test pass
- `guides/11-troubleshooting-guide.md` for diagnosing what the alerts surface
- `templates/10-ai-maintenance-addendum.md` for who pays when this finds something
- `docs/GAP-ANALYSIS-2026.md` section 3.1 for the evidence behind this checklist
