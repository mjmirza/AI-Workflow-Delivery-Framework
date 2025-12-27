# Client Onboarding Guide
## Complete Process for Bringing New Clients On Board

---

## Overview

This guide covers the complete onboarding process from first contact through development kickoff. A well-executed onboarding sets the foundation for project success.

---

## Phase 1: Pre-Engagement

### 1.1 Lead Qualification

Before investing time in a discovery call, qualify the lead:

**Must-Haves:**
- Clear business problem to solve
- Budget authority or access to decision maker
- Realistic timeline expectations
- Responsiveness (responds within 24-48 hours)

**Red Flags:**
- Can't articulate the problem
- "We don't have budget but..."
- Need it done yesterday
- Unresponsive during initial contact

**Qualification Questions (via email/form):**
```
1. What business problem are you trying to solve?
2. What's your approximate budget range for this project?
3. What's your ideal timeline?
4. Who will be the decision maker for this project?
5. What tools/systems are you currently using?
```

### 1.2 Discovery Call Preparation

**Before the Call:**
1. Research the company (website, LinkedIn, industry)
2. Review any materials they've sent
3. Prepare your discovery questions
4. Have 2-3 relevant case studies ready
5. Test your video/audio

**Discovery Call Agenda (30-45 min):**

| Time | Section | Goal |
|------|---------|------|
| 0-5 min | Intro | Set expectations |
| 5-20 min | Their Situation | Understand problem |
| 20-30 min | Technical Discovery | Assess requirements |
| 30-40 min | Scope & Next Steps | Align expectations |
| 40-45 min | Q&A | Address concerns |

**Key Questions to Ask:**

```
BUSINESS CONTEXT:
- Tell me about your business
- What's the problem you're trying to solve?
- What's the current process look like?
- What's the impact of this problem (time, money, frustration)?
- What would success look like?

TECHNICAL:
- What tools/systems are you currently using?
- Any integrations required?
- How sensitive is the data involved?
- Any compliance requirements (GDPR, HIPAA)?

PRACTICAL:
- What's your budget range?
- What's your timeline?
- Who are the stakeholders?
- Have you tried to solve this before?
```

### 1.3 Proposal & Scoping

**Scope of Work Structure:**

```markdown
# PROJECT NAME - Scope of Work

## 1. Project Overview
[2-3 paragraphs describing the project and business context]

## 2. Objectives
- Objective 1
- Objective 2
- Objective 3

## 3. Deliverables

### Workflow 1: [Name]
- Trigger: [How it starts]
- Process: [What it does]
- Output: [What happens]
- Integrations: [Systems involved]

### Workflow 2: [Name]
[Same structure]

### Documentation
- Walkthrough video
- Technical documentation
- FAQ document

## 4. Success Criteria
How we'll know the project is complete:
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## 5. What's NOT Included
To protect scope:
- Item 1
- Item 2
- Item 3

## 6. Client Responsibilities
What we need from you:
- Sample data/examples
- Access to systems
- Timely feedback
- Decision authority

## 7. Timeline
- Phase 1: Setup (X days)
- Phase 2: Development (X days)
- Phase 3: Testing (X days)
- Phase 4: Delivery (X days)

## 8. Investment
Total: $X,XXX

Payment Schedule:
- 50% deposit to begin
- 50% upon completion

## 9. Terms
- Revisions: X rounds included
- Support: X days post-launch
- Changes: Quoted separately
```

### 1.4 Contract & Deposit

**Essential Contract Elements:**
- Parties identified
- Scope of Work referenced
- Payment terms
- Intellectual property
- Confidentiality
- Termination clause
- Limitation of liability

**Before Starting Work:**
1. Contract signed by both parties
2. Deposit payment received (verify in bank)
3. Kickoff date scheduled
4. Communication channels established

---

## Phase 2: Kickoff

### 2.1 Pre-Kickoff Email

Send 2-3 days before kickoff call:

```
Subject: Kickoff Call Preparation - [Project Name]

Hi [Name],

Looking forward to our kickoff call on [Date] at [Time]!

TO PREPARE:
1. Sample data/examples ready to share
2. List of systems we'll integrate with
3. Any documentation about current processes
4. The right team members on the call

ACCOUNTS TO SET UP:
1. n8n account (I'll walk you through this on the call)
2. [Any other accounts needed]

AGENDA:
- Review scope and timeline
- Walk through n8n setup
- Configure credentials
- Discuss communication protocol
- Q&A

Duration: ~60 minutes

See you soon!
```

### 2.2 Kickoff Call Execution

**Agenda Breakdown:**

**1. Scope Review (10 min)**
- Confirm deliverables
- Reconfirm success criteria
- Set expectations for timeline
- Discuss communication protocol

**2. Sample Data Collection (10 min)**
- Receive sample data/examples
- Clarify any questions about the data
- Discuss edge cases

**3. n8n Environment Setup (20 min)**
- Walk through account creation
- Help choose hosting option
- Configure initial settings
- Get consultant access

**4. Integration Setup (15 min)**
- List all required credentials
- Walk through first integration
- Explain credential security

**5. Next Steps (5 min)**
- Confirm what you'll do next
- Set next check-in date
- Exchange any final info

### 2.3 n8n Setup Guide for Clients

**Option A: n8n Cloud (Recommended for Most)**

```
STEP-BY-STEP:

1. Go to cloud.n8n.io
2. Click "Start Free Trial" or "Sign Up"
3. Create account with work email
4. Verify email
5. Choose your plan based on execution needs
6. Enter billing information
7. Go to Settings  Users
8. Click "Invite User"
9. Enter consultant email: [your email]
10. Select role: "Admin" or "Editor"
11. Send invitation
```

**Option B: Self-Hosted (For Technical Clients)**

```
REQUIREMENTS:
- VPS (DigitalOcean, AWS, Linode, etc.)
- Docker installed
- Domain name (optional but recommended)
- SSL certificate (Let's Encrypt)

BASIC SETUP:
1. Provision VPS (minimum 2GB RAM)
2. Install Docker
3. Run n8n container
4. Configure reverse proxy (nginx)
5. Set up SSL
6. Configure environment variables
7. Create admin account
8. Invite consultant
```

### 2.4 Credential Setup Guide

**Walk Clients Through Each Integration:**

Example for OpenAI:

```
OPENAI CREDENTIAL SETUP:

1. Go to platform.openai.com
2. Sign in or create account
3. Go to API Keys section
4. Click "Create new secret key"
5. Name it (e.g., "n8n Production")
6. Copy the key IMMEDIATELY (you won't see it again)
7. In n8n, go to Credentials
8. Click "Add Credential"
9. Search for "OpenAI"
10. Paste your API key
11. Click "Save"
12. Test the connection
```

**Best Practice: Create a Loom video for each integration**

---

## Phase 3: Communication Protocol

### 3.1 Communication Channels

Establish clear channels:

| Type | Channel | Response Time |
|------|---------|---------------|
| Urgent issues | Phone/SMS | Same day |
| Project questions | Slack/Email | 24 hours |
| Feedback | Slack/Loom | 48 hours |
| Meetings | Zoom | As scheduled |

### 3.2 Check-In Cadence

**During Development:**
- Weekly async update (Loom video)
- Bi-weekly sync call (optional)
- Ad-hoc as needed

**Update Format:**
```
Hi [Name],

Here's this week's update:

 COMPLETED:
- Item 1
- Item 2

 IN PROGRESS:
- Item 3 (70% done)

 NEXT WEEK:
- Item 4
- Item 5

 NEED FROM YOU:
- [Anything blocking]

Questions? Reply or let's schedule a quick call.
```

### 3.3 Feedback Collection

**How to Request Feedback:**

```
Hi [Name],

The [feature] is ready for your review!

VIDEO: [Loom link showing how it works]

PLEASE TEST:
1. [Test scenario 1]
2. [Test scenario 2]
3. [Test scenario 3]

FEEDBACK FORMAT:
- What works well?
- What needs adjustment?
- Any edge cases I missed?

Reply with your thoughts or record a Loom response!
```

---

## Phase 4: Managing Expectations

### 4.1 Timeline Management

**Set Realistic Expectations:**
- Phases, not specific dates
- Buffer for the unexpected
- Clear dependencies on client

**If Delays Occur:**
```
Hi [Name],

Quick update on timeline:

CURRENT STATUS:
[What's happening]

REASON FOR ADJUSTMENT:
[Honest explanation]

REVISED PLAN:
[New approach/timeline]

IMPACT:
[What this means for them]

Let me know if you have concerns.
```

### 4.2 Scope Protection

**When Requests Come In:**

1. Listen and document
2. Compare to original scope
3. Respond appropriately:

**If In Scope:**
```
"Great idea! That's within our current scope,
so I'll add it to the build."
```

**If Out of Scope:**
```
"I love that idea! It's outside our current scope,
but I can add it to the backlog for a future phase.

For now, let's focus on getting [current deliverables]
live and working well. Then we can discuss adding
this as a separate project.

Does that work for you?"
```

### 4.3 Difficult Conversations

**When Something Goes Wrong:**

```
Hi [Name],

I want to be transparent about something.

WHAT HAPPENED:
[Clear explanation]

IMPACT:
[What it means for the project]

MY PLAN:
[How you'll fix it]

PREVENTION:
[How you'll prevent it in future]

I take full responsibility and am committed to
making this right. Let me know if you want to
discuss on a call.
```

---

## Onboarding Checklist Summary

```
PRE-ENGAGEMENT
 Lead qualified
 Discovery call completed
 Scope of Work created
 Proposal sent
 Contract signed
 Deposit received

KICKOFF
 Pre-kickoff email sent
 Kickoff call completed
 n8n environment set up
 Consultant access granted
 Sample data received
 Credentials configured
 Integrations tested

COMMUNICATION
 Channels established
 Check-in cadence agreed
 Feedback method set
 Escalation path clear

READY TO BUILD
 All requirements clear
 All access in place
 All credentials working
 Development can begin
```

---

## Common Onboarding Mistakes to Avoid

| Mistake | Prevention |
|---------|------------|
| Starting without contract | Never start without signed agreement |
| Starting without deposit | Payment = commitment |
| Vague scope | Specific deliverables + exclusions |
| No sample data | Require before kickoff |
| Wrong stakeholders on calls | Ask who should be there |
| Scope creep begins early | Document everything, refer to SOW |
| Communication chaos | Establish channels day 1 |

---

**Next**: See `02-security-implementation.md` for security best practices.
