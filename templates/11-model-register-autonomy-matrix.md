# Template 11. Model Register and Autonomy Matrix

Two registers that belong in every delivered AI system. Both are short. Both are
the artifact a client, an auditor or a works council will ask you for, and
neither can be reconstructed after the fact.

Attach both to the handover document and keep them current through the retainer.

## Part A. The Model Register

**Why this exists.** A delivered system pinned to a model has a hard expiry date
set by a third party, not by you or the client. Anthropic commits to 60 days
notice for public models. OpenAI gives six months for GA models, three for
specialised variants, and as little as two weeks for previews. The April 2026
announcement ending the GPT-4 era was the largest single deprecation notice any
provider has issued.

Without this register, the first anyone knows about a retirement is a production
failure.

### The register

| Field | Why it is here |
|---|---|
| Component | Which workflow or agent uses it |
| Model id | Exact string, not a family name |
| Provider | Who retires it |
| Version pinned | Yes or no. If no, say what floats |
| Announced retirement | Date, or "none announced" |
| Notice period | What the provider commits to |
| Fallback model | What we swap to |
| Fallback tested | Date the swap was last rehearsed |
| Evaluation score | Current and fallback, on the frozen set |
| Owner | Named human |

### Worked example

| Component | Model id | Provider | Pinned | Retirement | Fallback | Tested | Owner |
|---|---|---|---|---|---|---|---|
| Ticket classifier | | | Yes | none announced | | | |
| Summary generator | | | Yes | | | | |
| Extraction agent | | | No, floats on latest | n/a | | | |

**The floats-on-latest row is a decision, not an accident.** Floating means the
client accepts silent behaviour change in exchange for never doing a migration.
Pinning means predictable behaviour and a scheduled migration cost. Write down
which one the client chose, and have them acknowledge it.

### Operating rules

- [ ] The register is reviewed **monthly**, not on incident
- [ ] Any provider deprecation notice is recorded within 5 business days
- [ ] A fallback is **rehearsed** at least once before it is needed, and the
      rehearsal date is recorded
- [ ] Migration re-runs the frozen evaluation set and records the score before
      and after
- [ ] Migration is chargeable work under the maintenance addendum, clause 2

### The sales point

This register is the strongest argument for a retainer that exists. Without it,
the client is one provider announcement away from a broken system and no
contracted route to fix it. That is a concrete, dated, external risk that has
nothing to do with your competence, which makes it easy to talk about.

## Part B. The Autonomy Matrix

**Why this exists.** Prompt injection is OWASP's number one LLM risk, and the
2026 Top 10 was rewritten for the agentic era with tool-call hijacking as a new
entry. The structural point is that a model processes one token stream with no
hardware boundary between instruction and data, so injection is **not fixable by
prompt engineering**. Defence has to be architectural.

That means autonomy is a **per-action decision**, not a permissions setting you
apply once to an agent.

### The matrix

One row per tool the agent can call.

| Field | Question it answers |
|---|---|
| Tool | What the agent can invoke |
| Action type | Read, write, send, delete, pay, or execute |
| Reversible | Can we undo it, and how, and how fast |
| Blast radius | Worst realistic case if it fires wrongly |
| Approval | None, notify-after, or human-approves-before |
| Rate limit | Maximum invocations per period |
| Credential scope | Least privilege actually applied |
| Audited | Does the log show who and what |

### Worked example

| Tool | Type | Reversible | Blast radius | Approval | Rate limit |
|---|---|---|---|---|---|
| Search knowledge base | Read | n/a | None | None | 100/hr |
| Draft reply | Write | Yes, draft only | None until sent | None | 50/hr |
| Send email to customer | Send | **No** | Reputation, one customer | **Human approves** | 20/hr |
| Update CRM record | Write | Yes, with history | One record | Notify after | 200/hr |
| Issue refund | Pay | **No** | Money, unbounded | **Human approves** | 5/hr |
| Delete record | Delete | **No** | Data loss | **Human approves** | Denied |

### The decision rule

Work it in this order. Stop at the first that applies.

1. **Irreversible and unbounded blast radius.** Deny the tool, or require human
   approval with the full payload shown before execution.
2. **Irreversible, bounded blast radius.** Human approves before execution.
3. **Reversible, but externally visible.** Notify after, with a one-click undo
   and a named human on the notification.
4. **Reversible and internal only.** Autonomous, rate limited, audited.

n8n supports tool-level human approval on the AI Agent node, and the Chat node
gained wait-for-response actions in v2.5.0 on 2026-01-20. Use them rather than
building an approval flow by hand.

### Operating rules

- [ ] Every tool the agent can reach has a row. No exceptions, including tools
      reached indirectly through an MCP server
- [ ] Any third party MCP server is reviewed for supply chain risk before it is
      added. Malicious MCP packages have been confirmed in the wild since
      September 2025
- [ ] Each credential is scoped to the minimum the tool needs, and that scoping
      is verified rather than assumed
- [ ] The matrix is re-reviewed whenever a tool is added, which is the moment it
      normally gets skipped
- [ ] `maxIterations` on the agent is capped, 5 to 10 is the usual range, to
      bound a runaway loop

### What the matrix is really for

Two conversations get much easier once it exists.

**With the client.** "Which of these should the agent do without asking you"
is a question a business owner can answer. "What permissions should the agent
have" is not.

**With a works council or auditor.** A signed matrix showing that irreversible
actions require a human is the single most persuasive artifact you can bring to
that meeting. It converts an abstract fear into a reviewed control.

## Cross references

- `checklists/07-scoping-gate.md` for the classification that precedes both
- `templates/10-ai-maintenance-addendum.md` clause 2 for model migration terms
- `checklists/08-silent-failure.md` for catching it when a tool stops working
- `guides/12-n8n-platform-reality-2026.md` for the platform features referenced
- `docs/GAP-ANALYSIS-2026.md` sections 3.3 and 3.4 for the evidence
