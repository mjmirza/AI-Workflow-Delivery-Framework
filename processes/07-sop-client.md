# SOP: Client Guide
## What Clients Need to Know and Do

---

## Overview

This guide explains what you, as a client, need to do at each stage of your automation project. Following these steps ensures smooth delivery and the best possible outcome.

---

## Your Role in the Project

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   YOU provide:                        WE provide:                          │
│   • Requirements & samples            • Technical expertise                 │
│   • Access & credentials              • Development & testing               │
│   • Timely feedback                   • Documentation & training            │
│   • Decisions when needed             • Ongoing support                     │
│                                                                             │
│   Together: We build something that works for your business.               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Before Kickoff

### What to Prepare

```
BEFORE THE KICKOFF CALL:

 Sample Data/Examples
   - Real examples of inputs the workflow will receive
   - Edge cases you know about
   - Anonymize sensitive data if needed

 Tool Access Information
   - List of tools we'll integrate with
   - Admin access to relevant systems
   - Any existing documentation

 Team Availability
   - Who should be on kickoff call?
   - Who is the decision maker?
   - Who will provide feedback?

 Questions to Answer
   - What does success look like?
   - What must absolutely work?
   - What's nice-to-have vs essential?
```

### Decision Makers

```
IDENTIFY:

Primary Contact: _________________________
- Day-to-day communication
- Feedback provider
- Testing coordinator

Decision Maker: __________________________
- Approves scope changes
- Signs off on deliverables
- Handles budget decisions

Technical Contact (if different): _________
- Provides system access
- Answers technical questions
- Manages credentials
```

---

## Phase 2: Kickoff

### During Kickoff Call

```
KICKOFF CALL AGENDA:

1. Review scope & deliverables
   - Confirm what we're building
   - Clarify any questions

2. Set up n8n environment
   - Create/access account
   - Invite our team
   - Basic configuration

3. Connect first integrations
   - Walk through credential setup
   - Test connections

4. Establish communication
   - How we'll communicate
   - Expected response times
   - Check-in schedule

5. Confirm next steps
   - What we'll do next
   - What you need to provide
```

### After Kickoff

```
YOUR ACTION ITEMS:

 Provide any remaining sample data
 Complete credential setup (we'll guide you)
 Confirm team access
 Review communication channels
 Save important links/docs
```

---

## Phase 3: n8n Setup

### Creating Your n8n Account

**Option A: n8n Cloud (Recommended)**

```
STEP-BY-STEP:

1. Go to cloud.n8n.io
2. Click "Start Free Trial" or "Sign Up"
3. Use your work email
4. Verify your email
5. Choose a plan (we'll recommend)
6. Enter billing information
7. Go to Settings  Users
8. Invite our email as team member
9. Done!
```

**Option B: Self-Hosted (We'll Help)**

```
If you prefer self-hosting:
- We'll provide setup guidance
- You maintain the server
- More control, more responsibility
- Ask us for recommendations
```

### Why You Own the n8n Account

```
YOU OWN IT BECAUSE:

 Your data stays in your control
 You see all costs directly
 No vendor lock-in with us
 Easy to add team members
 You can hire others later
 Compliance stays clean
```

---

## Phase 4: Credential Setup

### What Are Credentials?

```
CREDENTIALS = API KEYS

These are like passwords that let n8n connect to your tools:
- OpenAI (for AI features)
- Google (for Gmail, Calendar)
- Your CRM (HubSpot, Salesforce)
- Other tools we integrate

YOU create these because:
- You control the access
- You see the usage/billing
- You can revoke anytime
- It's more secure
```

### Setting Up Credentials

**We'll send you video guides for each one. General process:**

```
1. Log into the service (e.g., OpenAI)
2. Find API or Developer settings
3. Generate a new API key
4. Copy the key
5. In n8n, add new credential
6. Paste the key
7. Save and test
```

### Sharing Credentials Securely

```
IF YOU NEED TO SHARE A KEY WITH US:

 USE:
- 1Password secure sharing
- Bitwarden Send
- Other encrypted sharing tools

 NEVER:
- Email
- Slack/Teams messages
- Text messages
- Shared documents

We'll provide a secure link for you to share with us.
```

---

## Phase 5: During Development

### Your Responsibilities

```
DURING BUILD PHASE:

 Respond to questions within 24-48 hours
 Provide additional samples if requested
 Make decisions when presented with options
 Review weekly updates
 Attend scheduled check-in calls
```

### Communication Protocol

```
HOW WE'LL COMMUNICATE:

WEEKLY UPDATES:
- We'll send progress updates (video or email)
- Review at your convenience
- Reply with questions/feedback

QUESTIONS FOR YOU:
- We'll email when we need decisions
- Please respond within 48 hours
- Delays in response = delays in project

CHECK-IN CALLS:
- [Frequency as agreed]
- We'll cover progress, questions, next steps
- Bring any concerns or ideas
```

### Providing Feedback

```
WHEN GIVING FEEDBACK:

BE SPECIFIC:
 "The email summary is too long, please limit to 3 sentences"
 "I don't like the emails"

BE CONSTRUCTIVE:
 "Can we add the customer name to the output?"
 "This isn't what I wanted"

BE TIMELY:
 Respond within 48 hours
 Wait a week then share multiple issues

RECORD IF EASIER:
We love Loom videos if that's easier for you!
```

---

## Phase 6: Testing

### Client Testing Period

```
WHEN YOU GET THE WORKFLOW TO TEST:

1. USE IT LIKE YOU NORMALLY WOULD
   - Send real (or realistic) inputs
   - Try different scenarios
   - Think about edge cases

2. EVALUATE THE OUTPUTS
   - Is it correct?
   - Is the format right?
   - Is the tone appropriate?

3. NOTE ANY ISSUES
   - What didn't work?
   - What's close but needs adjustment?
   - What's missing?

4. SHARE FEEDBACK
   - Use our feedback form/method
   - Be specific
   - Prioritize: critical vs nice-to-have
```

### What to Look For

```
TESTING CHECKLIST:

FUNCTIONALITY:
 Does it trigger correctly?
 Does it process properly?
 Is the output correct?

QUALITY:
 Is AI output relevant?
 Is the tone right?
 Is formatting correct?

EDGE CASES:
 What happens with unusual input?
 Any scenarios that might break it?
 Missing data handling?
```

---

## Phase 7: Handover

### Handover Call

```
WHAT HAPPENS:

1. We walk through the live system
2. Show you how to monitor
3. Explain maintenance needs
4. Answer your questions
5. Go live together
6. Celebrate!

PREPARE:
 Available for 60 minutes
 Right stakeholders present
 Production credentials ready
 Questions written down
```

### What You'll Receive

```
DELIVERABLES:

 Live workflow in your n8n
 Backup exports (JSON files)
 Walkthrough video
 Written documentation
 FAQ document
 Credential inventory
 Support period access
```

### After Go-Live

```
FIRST WEEK:

 Monitor outputs
 Report any issues immediately
 Ask questions as needed
 We're watching closely too

SUPPORT PERIOD:
- We'll fix any bugs
- Quick adjustments included
- Duration: [X days per agreement]
```

---

## Phase 8: Ongoing

### If You Have a Retainer

```
WHAT'S INCLUDED:
- Bug fixes
- Minor adjustments
- Monitoring
- Monthly check-in
- Priority support

HOW TO USE:
- Email/Slack for requests
- We'll confirm if in scope
- Included work = just done
- New features = quoted separately

MONTHLY:
- We'll send a report
- Check-in call scheduled
- Review any needs
```

### Getting Support

```
FOR ISSUES:

1. Check the FAQ first
2. Review the documentation
3. Contact us via [method]
4. Describe the issue clearly

WHAT TO INCLUDE:
- What you were doing
- What happened
- Screenshot if possible
- Urgency level
```

---

## Quick Reference

### Your Checklist by Phase

```
BEFORE KICKOFF:
 Sample data ready
 Tool access available
 Team identified

KICKOFF:
 n8n account created
 Our team invited
 First credentials set up

DEVELOPMENT:
 Respond to questions promptly
 Review updates
 Attend check-ins

TESTING:
 Test thoroughly
 Provide specific feedback
 Confirm approval

HANDOVER:
 Attend handover call
 Confirm everything works
 Provide acceptance

ONGOING:
 Report issues
 Attend monthly calls (if retainer)
 Pay invoices on time
```

### Contact Information

```
PRIMARY CONTACT:
Name: ____________________________
Email: ___________________________
Phone: ___________________________

FOR URGENT ISSUES:
Method: __________________________
Available: _______________________

FOR BILLING:
Email: ___________________________
```

---

## FAQs

### General

**Q: Who owns the workflows?**
A: You do! Once paid, everything we build is yours.

**Q: Can I modify the workflows myself?**
A: Yes, but we recommend consulting us for significant changes.

**Q: What if I want to stop using your services?**
A: No problem. We'll provide full handover documentation.

### Technical

**Q: What if something breaks?**
A: During support period: Contact us immediately.
   After: Depends on your retainer agreement.

**Q: Can I add my own team members to n8n?**
A: Absolutely! It's your account.

**Q: What happens to my data?**
A: Your data stays in your systems. We only access what's needed.

### Billing

**Q: When do I pay?**
A: Per our agreement: typically 50% deposit, 50% on completion.

**Q: What's included in the retainer?**
A: Bug fixes, minor adjustments, monitoring. New features are separate.

---

## Getting the Most from This Partnership

```
FOR BEST RESULTS:

1. BE AVAILABLE
   Quick responses = faster delivery

2. BE SPECIFIC
   Clear feedback = better outcomes

3. BE REALISTIC
   Good work takes time

4. BE OPEN
   Share concerns early

5. TRUST THE PROCESS
   We've done this before!
```

---

**Questions? Contact your Project Manager anytime.**
