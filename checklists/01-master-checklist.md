# Master Checklist
## Complete Project Delivery Checklist

---

## Quick Reference Status Legend

| Symbol | Meaning |
|--------|---------|
|  | Not started |
| @ | In progress |
| [x] | Completed |
|  | Needs attention |
| [REQUIRED] | Required/Critical |
|  | Optional/Recommended |

---

## Phase 1: Pre-Project & Discovery

### 1.1 Lead Qualification
```
 [REQUIRED] Lead source identified
 [REQUIRED] Initial inquiry reviewed
 [REQUIRED] Budget range discussed
 [REQUIRED] Timeline expectations set
  Portfolio/case studies shared
 [REQUIRED] Discovery call scheduled
```

### 1.2 Discovery Call
```
 [REQUIRED] Business context understood
 [REQUIRED] Pain points identified
 [REQUIRED] Current tech stack documented
 [REQUIRED] Integration requirements listed
 [REQUIRED] Data sensitivity discussed
 [REQUIRED] Success criteria defined
  Budget confirmed
  Decision makers identified
```

### 1.3 Proposal & Scoping
```
 [REQUIRED] Scope of Work drafted
     Specific workflows listed
     Integrations specified
     Deliverables defined
     What's NOT included stated
     Success criteria measurable
 [REQUIRED] Pricing prepared
 [REQUIRED] Timeline outlined (phases only)
 [REQUIRED] Payment terms specified
  Maintenance options included
```

### 1.4 Contract & Close
```
 [REQUIRED] Contract/agreement signed
 [REQUIRED] Deposit/first payment received
 [REQUIRED] Project kickoff date set
 [REQUIRED] Communication channels established
  Project management tool set up
```

---

## Phase 2: Kickoff & Environment Setup

### 2.1 Kickoff Call Preparation
```
 [REQUIRED] Kickoff agenda prepared
 [REQUIRED] Pre-call requirements sent to client
     Sample data/examples needed
     Account credentials needed
     Access requirements listed
 [REQUIRED] Kickoff call scheduled
  Recording permission confirmed
```

### 2.2 Kickoff Call Execution
```
 [REQUIRED] Scope reviewed and confirmed
 [REQUIRED] Success criteria reconfirmed
 [REQUIRED] Client expectations aligned
 [REQUIRED] Sample data received
 [REQUIRED] Communication protocol established
 [REQUIRED] n8n setup process explained
  Next steps confirmed
```

### 2.3 n8n Environment Setup
```
 [REQUIRED] Hosting decision made
     n8n Cloud
     Self-hosted VPS
     Local/On-prem
 [REQUIRED] Client creates/owns n8n instance
 [REQUIRED] Client enters billing information
 [REQUIRED] Consultant invited as team member
 [REQUIRED] Consultant access verified
  Test environment created (if separate)
```

### 2.4 Credential & Integration Setup
```
 [REQUIRED] Required integrations listed
 [REQUIRED] Credential setup guide sent (Loom)
 [REQUIRED] Client creates API accounts
 [REQUIRED] Client generates API keys
 [REQUIRED] Credentials entered in n8n
 [REQUIRED] All integrations tested working
  Credential documentation created
```

---

## Phase 3: Development

### 3.1 Architecture & Planning
```
 [REQUIRED] Workflow architecture designed
 [REQUIRED] Data flow mapped
 [REQUIRED] Node structure planned
  Sub-workflows identified
  Reusable components noted
```

### 3.2 Core Build
```
 [REQUIRED] Trigger nodes configured
 [REQUIRED] Core logic implemented
 [REQUIRED] AI components built
     Prompts written
     Model selected
     Response parsing configured
 [REQUIRED] Actions/outputs configured
 [REQUIRED] Workflow tested with sample data
```

### 3.3 Hardening
```
 [REQUIRED] Error handling added
     Try/catch patterns
     Fallback logic
     Graceful degradation
 [REQUIRED] Timeout protection configured
 [REQUIRED] Input validation implemented
 [REQUIRED] Rate limit handling (if applicable)
  Retry logic added
```

### 3.4 Observability
```
 [REQUIRED] Execution logging enabled
 [REQUIRED] Error logging configured
     Google Sheet log (recommended)
     Or other logging destination
 [REQUIRED] Error notifications set up
     Email alerts
     Slack notifications
  AI response logging (for quality)
  Usage/token tracking
```

### 3.5 Workflow Hygiene
```
 [REQUIRED] All nodes properly named
 [REQUIRED] Sticky notes added for logic
 [REQUIRED] No hardcoded secrets
 [REQUIRED] No test data in production
  Color coding used (if applicable)
  Workflow description added
```

---

## Phase 4: Testing & QA

### 4.1 Internal QA
```
 [REQUIRED] Test with sample data (10+ examples)
 [REQUIRED] Edge cases tested
     Empty inputs
     Invalid data
     Duplicate data
     Large payloads
 [REQUIRED] Error handling verified
 [REQUIRED] Timeout behavior tested
 [REQUIRED] All outputs validated
```

### 4.2 AI-Specific Testing
```
 [REQUIRED] AI responses checked for:
     Relevance & correctness
     Tone & safety
     Consistency across runs
 [REQUIRED] Prompt injection tested
 [REQUIRED] Jailbreak attempts tested
  Multiple prompts/models evaluated
  Evaluation data documented
```

### 4.3 Scale Testing
```
 [REQUIRED] Run 50+ sample inputs
 [REQUIRED] Check consistency
 [REQUIRED] Monitor execution time
 [REQUIRED] Verify rate limits not hit
  Cost projection calculated
```

### 4.4 Client QA
```
 [REQUIRED] Testing interface provided
 [REQUIRED] Testing instructions given
 [REQUIRED] Client testing period allowed
 [REQUIRED] Feedback collected
 [REQUIRED] Issues documented
 [REQUIRED] Fixes implemented
 [REQUIRED] Re-testing completed
```

---

## Phase 5: Security Review

### 5.1 Credential Security
```
 [REQUIRED] No credentials in workflow JSON
 [REQUIRED] No secrets in sticky notes
 [REQUIRED] Credentials reference by name only
 [REQUIRED] Client owns all API keys
 [REQUIRED] Secure transfer method used
```

### 5.2 Webhook Security
```
 [REQUIRED] HTTPS only
 [REQUIRED] Signature verification (if available)
 [REQUIRED] Token authentication (if needed)
  Rate limiting considered
  IP whitelisting (if applicable)
```

### 5.3 Data Protection
```
 [REQUIRED] Data minimization practiced
 [REQUIRED] PII handling documented
 [REQUIRED] Execution logs auto-prune enabled
 [REQUIRED] No sensitive data in URLs
  GDPR considerations addressed
```

### 5.4 Access Control
```
 [REQUIRED] Role-based access configured
 [REQUIRED] Only necessary permissions granted
 [REQUIRED] Credential sharing restricted
  Audit logging enabled
```

---

## Phase 6: Handover & Delivery

### 6.1 Documentation
```
 [REQUIRED] Workflow overview document
 [REQUIRED] Loom walkthrough video (5-10 min)
 [REQUIRED] Credential setup guide
 [REQUIRED] Troubleshooting FAQ
  Architecture diagram
  Data flow diagram
```

### 6.2 Pre-Handover Preparation
```
 [REQUIRED] Production workflow created
 [REQUIRED] Test data removed
 [REQUIRED] All nodes labeled
 [REQUIRED] Backup exported
 [REQUIRED] Handover call scheduled
```

### 6.3 Handover Call
```
 [REQUIRED] Scope reviewed
 [REQUIRED] Live demo conducted
 [REQUIRED] Monitoring explained
 [REQUIRED] Maintenance discussed
 [REQUIRED] Questions answered
 [REQUIRED] Credentials swapped (test  prod)
 [REQUIRED] Workflow enabled
```

### 6.4 Post-Handover
```
 [REQUIRED] Call recording shared
 [REQUIRED] Documentation sent
 [REQUIRED] First executions verified
 [REQUIRED] Client acceptance received
 [REQUIRED] Final invoice sent
```

---

## Phase 7: Project Close & Support

### 7.1 Project Closure
```
 [REQUIRED] All deliverables verified against scope
 [REQUIRED] Client sign-off received
 [REQUIRED] Final payment received
  Testimonial/case study requested
  Referral opportunity discussed
```

### 7.2 Post-Launch Support
```
 [REQUIRED] Support period defined (7-14 days)
 [REQUIRED] Monitoring active
 [REQUIRED] Quick response to issues
 [REQUIRED] Bug fixes applied
 [REQUIRED] Support period closed
```

### 7.3 Retainer Decision
```
 [REQUIRED] Retainer options presented
 [REQUIRED] Scope defined (if proceeding)
     What's included
     What's excluded
     SLA terms
     Pricing
 [REQUIRED] Retainer agreement signed (if proceeding)
  Or clean exit documented
```

### 7.4 Archive
```
 [REQUIRED] Project files organized
 [REQUIRED] Backups stored securely
 [REQUIRED] Lessons learned documented
  Templates updated for future
```

---

## Quick Checklists by Role

### For Consultants/Developers
```
 Environment access verified
 All integrations tested
 Workflow built and tested
 Error handling complete
 Documentation ready
 Handover prepared
```

### For Project Managers
```
 Contract signed
 Kickoff completed
 Milestones tracked
 Client communication managed
 Scope protected
 Invoice sent
```

### For Clients
```
 n8n account created
 API keys generated
 Team access configured
 Testing completed
 Acceptance confirmed
 Support understood
```

---

## Emergency Quick Reference

### If Workflow Breaks
```
1.  Check execution logs
2.  Identify error point
3.  Disable workflow if needed
4.  Notify client (if critical)
5.  Diagnose and fix
6.  Test thoroughly
7.  Re-enable
8.  Monitor closely
```

### If Client Wants Changes
```
1.  Document the request
2.  Compare against scope
3.  If in scope  implement
4.  If out of scope  quote new work
5.  Get approval before proceeding
```

---

**Next**: See individual phase checklists for more detail.
