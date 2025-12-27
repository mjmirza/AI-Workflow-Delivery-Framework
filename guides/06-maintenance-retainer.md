# Maintenance & Retainer Guide
## Ongoing Support, Billing & Legal Framework

---

## Retainer Models

### Model Comparison

| Model | Best For | Pricing | Pros | Cons |
|-------|----------|---------|------|------|
| **Hours-Based** | Unpredictable needs | $X/hour, X hours/month | Flexible, pay for what you use | Tracking overhead |
| **Fixed Monthly** | Predictable needs | $X/month flat | Predictable, simple | May over/under serve |
| **Hybrid** | Growing clients | Base + hourly overage | Balance of predictable + flexible | More complex |

### Hours-Based Retainer

```
STRUCTURE:

Monthly Hours: X hours
Rate: $X/hour
Rollover: Yes/No (max X hours)
Overage Rate: $X/hour

INCLUDES:
- Bug fixes
- Minor adjustments
- Monitoring
- Monthly check-in
- Priority response

TIME TRACKING:
- Track in 15-min increments
- Log all work
- Monthly report to client
- Unused hours: rollover or forfeit

EXAMPLE:
5 hours/month at $150/hour = $750/month
Rollover max: 5 hours
Overage: $175/hour
```

### Fixed Monthly Retainer

```
STRUCTURE:

Monthly Fee: $X
Scope: Defined activities

INCLUDES:
- Up to X hours of work
- Bug fixes
- Minor tweaks
- Monitoring
- Updates
- Monthly check-in
- Priority support

EXCLUDES (billed separately):
- New features
- New workflows
- Major changes
- New integrations

EXAMPLE:
$1,000/month covers:
- Up to 5 hours of maintenance
- All bug fixes
- Monitoring
- Updates
- Monthly 30-min call
```

### Hybrid Retainer

```
STRUCTURE:

Base Fee: $X/month (includes Y hours)
Overage: $X/hour

INCLUDES IN BASE:
- First Y hours of work
- Monitoring
- Bug fixes
- Monthly check-in

OVERAGE TRIGGERS:
- Beyond Y hours
- Billed at end of month
- Client notified before exceeding

EXAMPLE:
Base: $500/month (includes 3 hours)
Overage: $150/hour
Typical month: $500
Busy month: $500 + (2 extra hours × $150) = $800
```

---

## Service Level Agreement (SLA)

### Response Times

```
SEVERITY LEVELS:

 CRITICAL (System Down)
Definition: Workflow completely broken, major business impact
Response: Within 2-4 hours (business hours)
Resolution Target: Same business day

 HIGH (Significant Issue)
Definition: Partial failure, degraded performance
Response: Within 4-8 hours
Resolution Target: 24 hours

 MEDIUM (Minor Issue)
Definition: Feature not working, workaround exists
Response: Within 24 hours
Resolution Target: 3-5 business days

 LOW (Enhancement/Question)
Definition: Nice-to-have, cosmetic, questions
Response: Within 48 hours
Resolution Target: Next maintenance cycle
```

### SLA Document Template

```markdown
# Service Level Agreement

## Parties
Provider: [Your Company]
Client: [Client Company]
Effective Date: [Date]

## Covered Services
- Workflow monitoring
- Bug fixes
- Minor updates
- Security patches
- Monthly check-ins

## Response Commitments

| Severity | Response Time | Resolution Target |
|----------|---------------|-------------------|
| Critical | 2-4 hours | Same day |
| High | 4-8 hours | 24 hours |
| Medium | 24 hours | 3-5 days |
| Low | 48 hours | 14 days |

## Availability
- Business hours: [M-F, 9am-6pm TZ]
- Emergency contact: [method]
- Holiday schedule: [details]

## Exclusions
- New feature development
- New workflow creation
- Third-party service outages
- Client-caused issues

## Escalation
Level 1: [Contact method]
Level 2: [Phone/urgent email]
Level 3: [Emergency protocol]

## Reporting
- Monthly summary report
- Incident reports for Critical/High
- Quarterly review call

## Terms
- 30-day termination notice
- Monthly billing, due Net 15
- Annual review of terms
```

---

## Maintenance Activities

### Monthly Maintenance Checklist

```
WEEK 1: Monitoring Review
 Review all executions from past week
 Check error rates
 Verify all workflows active
 Review any alerts

WEEK 2: Performance & Cost
 Check API usage/costs
 Review execution times
 Identify optimization opportunities
 Check for rate limit issues

WEEK 3: Updates & Security
 Check for n8n updates
 Review integration updates
 Apply security patches
 Test after any updates

WEEK 4: Client Touchpoint
 Prepare monthly report
 Monthly check-in call
 Address any concerns
 Plan next month
```

### Monthly Report Template

```markdown
# Monthly Maintenance Report

## Client: [Name]
## Period: [Month Year]

---

## Executive Summary
[2-3 sentence overview]

## Workflow Performance

### Execution Statistics
| Metric | This Month | Last Month | Change |
|--------|------------|------------|--------|
| Total Executions | X | X | +/-X% |
| Successful | X (X%) | X | |
| Failed | X (X%) | X | |
| Avg Execution Time | Xs | Xs | |

### API Usage & Costs
| Service | Usage | Cost |
|---------|-------|------|
| OpenAI | X tokens | $X |
| [Other] | X calls | $X |
| **Total** | | **$X** |

## Issues & Resolutions

| Date | Issue | Severity | Resolution | Time Spent |
|------|-------|----------|------------|------------|
| | | | | |

## Work Completed
- [Item 1]
- [Item 2]
- [Item 3]

## Recommendations
1. [Recommendation]
2. [Recommendation]

## Next Month Plan
- [Planned activity]
- [Planned activity]

## Retainer Summary
Hours included: X
Hours used: X
Hours remaining: X
```

### Proactive Monitoring

```
AUTOMATED MONITORING:

1. ERROR RATE ALERTS
   Trigger: Error rate > 10%
   Action: Email/Slack notification

2. EXECUTION FAILURES
   Trigger: 3+ consecutive failures
   Action: Immediate notification

3. API USAGE
   Trigger: Approaching quota/budget
   Action: Warning notification

4. WORKFLOW INACTIVE
   Trigger: No executions in X days
   Action: Check if intentional

MONITORING WORKFLOW:
- Runs daily
- Checks all client workflows
- Logs to monitoring sheet
- Alerts on thresholds
```

---

## Billing & Legal

### Contract Essentials

**Retainer Agreement Must Include:**

```markdown
1. PARTIES
   - Your company details
   - Client company details

2. SERVICES
   - Specific services included
   - What's explicitly excluded
   - Service level commitments

3. TERM
   - Start date
   - Duration (monthly, annual)
   - Auto-renewal terms

4. FEES
   - Monthly/annual fee
   - Payment due date
   - Late payment terms
   - Overage rates

5. TERMINATION
   - Notice period (30 days typical)
   - Exit procedures
   - Final billing

6. INTELLECTUAL PROPERTY
   - Client owns deliverables
   - You retain generic patterns
   - License to pre-existing tools

7. CONFIDENTIALITY
   - Both parties bound
   - Data handling
   - Survival after termination

8. LIABILITY
   - Limitation of liability
   - Indemnification
   - Insurance requirements (if any)

9. GENERAL
   - Governing law
   - Dispute resolution
   - Amendment process
```

### Invoice Template

```
╔═══════════════════════════════════════════════════════════════╗
║                        INVOICE                                ║
╠═══════════════════════════════════════════════════════════════╣

Invoice #: [INV-XXXX]
Date: [Date]
Due: [Due Date]

FROM:
[Your Company Name]
[Address]
[Email]

TO:
[Client Company]
[Contact Name]
[Address]

─────────────────────────────────────────────────────────────────

DESCRIPTION                                              AMOUNT

Monthly Retainer - [Month Year]                         $X,XXX
  Includes: Monitoring, bug fixes, updates

Overage Hours: X hours @ $XXX/hr                          $XXX
  [Brief description of work]

─────────────────────────────────────────────────────────────────
                                          SUBTOTAL      $X,XXX
                                          TAX (X%)        $XXX
                                          ─────────────────────
                                          TOTAL DUE     $X,XXX
─────────────────────────────────────────────────────────────────

PAYMENT METHODS:
- Bank Transfer: [Details]
- Card: [Link]
- Other: [Details]

NOTES:
Thank you for your continued partnership!

╚═══════════════════════════════════════════════════════════════╝
```

### Scope Protection

**What's Included vs Excluded:**

```
 INCLUDED IN RETAINER:

Maintenance:
- Bug fixes
- Error resolution
- Performance tweaks
- Security updates

Monitoring:
- Execution oversight
- Error alerting
- Log review

Support:
- Questions answered
- Troubleshooting
- Minor adjustments

Communication:
- Monthly check-in call
- Monthly report
- Email support

 NOT INCLUDED (Bill Separately):

New Development:
- New workflows
- New features
- New integrations
- Major redesigns

Consulting:
- Strategy sessions
- Architecture planning
- Process design

Training:
- New team members
- Deep dives
- Workshops

Emergency:
- Outside business hours
- Weekend work
- Holiday work
```

**Handling Out-of-Scope Requests:**

```
WHEN CLIENT ASKS FOR MORE:

1. ACKNOWLEDGE
   "That's a great idea!"

2. CLARIFY
   "Let me make sure I understand what you need..."

3. EXPLAIN
   "That would be outside our current retainer scope,
    which covers [included items]."

4. OFFER OPTIONS
   "I can:
    a) Quote this as a separate project
    b) Add it to our next project phase
    c) Include it if we upgrade your retainer"

5. DOCUMENT
   Log the request for future reference
```

---

## Communication Cadence

### Regular Touchpoints

```
WEEKLY:
- Monitoring review (internal)
- Status update if issues

MONTHLY:
- Check-in call (30 min)
- Written report
- Invoice

QUARTERLY:
- Strategy review (60 min)
- Retainer assessment
- Roadmap planning

ANNUALLY:
- Contract renewal discussion
- Rate review
- Relationship check
```

### Monthly Check-In Agenda

```
MONTHLY CALL (30 min)

1. PERFORMANCE REVIEW (10 min)
   - Executions summary
   - Any issues/resolutions
   - Costs overview

2. UPCOMING WORK (5 min)
   - Planned maintenance
   - Known updates coming

3. CLIENT FEEDBACK (10 min)
   - How's it going?
   - Any concerns?
   - New needs arising?

4. NEXT STEPS (5 min)
   - Action items
   - Next call date
```

---

## Retainer Transitions

### Starting a Retainer

```
POST-PROJECT  RETAINER:

1. PROPOSE
   "Now that the project is complete, I offer ongoing
    maintenance retainers. Here's what that looks like..."

2. PRESENT OPTIONS
   - Option A: [Basic]
   - Option B: [Standard]
   - Option C: [Premium]

3. AGREE ON TERMS
   - Scope
   - SLA
   - Pricing
   - Start date

4. DOCUMENT
   - Retainer agreement signed
   - Expectations documented

5. TRANSITION
   - Move from project mode to retainer mode
   - Set up regular touchpoints
```

### Upgrading/Downgrading

```
RETAINER ADJUSTMENT:

When client needs change:
1. Assess current usage
2. Discuss new needs
3. Propose adjusted scope
4. Update agreement
5. Adjust billing

UPGRADE TRIGGERS:
- Consistently exceeding hours
- New workflows added
- Higher support needs
- Business growth

DOWNGRADE TRIGGERS:
- Underusing hours
- Budget constraints
- Reduced complexity
```

### Ending a Retainer

```
RETAINER TERMINATION:

1. NOTICE RECEIVED
   - Document the request
   - Confirm termination date
   - Review contract terms

2. TRANSITION PLAN
   - What needs to happen before end
   - Knowledge transfer if new provider
   - Final documentation updates

3. FINAL PERIOD
   - Complete outstanding work
   - Final maintenance tasks
   - Handover preparation

4. EXIT DELIVERABLES
   - Updated documentation
   - Final backups
   - Access removed

5. FINAL BILLING
   - Pro-rated amount (if applicable)
   - Any outstanding invoices

6. RELATIONSHIP CLOSE
   - Thank you
   - Feedback request
   - Door open for future
```

---

## Quick Reference

### Retainer Pricing Guidelines

```
TYPICAL RANGES (adjust for your market):

BASIC (Small, simple)
- 2-3 hours/month
- $300-500/month

STANDARD (Medium complexity)
- 5-8 hours/month
- $750-1,200/month

PREMIUM (Complex, critical)
- 10+ hours/month
- $1,500-3,000/month

ENTERPRISE (Custom)
- Dedicated support
- Custom SLAs
- $3,000+/month
```

### Retainer Health Indicators

```
HEALTHY RETAINER:
 Regular communication
 Issues resolved quickly
 Client satisfied
 Scope respected
 Payments on time
 Growing relationship

UNHEALTHY RETAINER:
 Scope creep accepted
 Client never available
 Late payments
 Constant complaints
 Underutilized
 Relationship strained
```

---

**Next**: See `07-offboarding-guide.md` for exit processes.
