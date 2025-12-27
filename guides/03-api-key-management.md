# API Key Management Guide
## Complete Guide to Credential Handling & Billing

---

## Core Principle

```
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   CLIENT OWNS ALL API KEYS                                        ║
║   CLIENT PAYS FOR ALL USAGE                                       ║
║   YOU NEVER SEE RAW CREDENTIAL VALUES (WHEN POSSIBLE)             ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

This creates:
- Transparent billing
- Clean ownership
- Easy handover
- No disputes

---

## Client API Account Setup

### Step-by-Step Process

**1. Identify Required Services**
```
Common Services for AI Workflows:
 OpenAI / Anthropic (AI models)
 Google Workspace (Gmail, Calendar, Drive)
 Microsoft 365 (Outlook, Calendar)
 CRM (HubSpot, Salesforce, Pipedrive)
 Communication (Slack, Discord, Twilio)
 Databases (Airtable, Notion, Supabase)
 Payment (Stripe)
 Other: _____________________________
```

**2. Create Setup Guide for Each**

For each service, create a Loom video showing:
- How to sign up
- How to find API settings
- How to generate key
- Where to paste in n8n
- How to verify it works

**3. Send Instructions to Client**

```
Email Template:

Subject: API Account Setup - [Project Name]

Hi [Name],

Before we can build your automation, you'll need to set up
accounts and API keys for the following services:

REQUIRED:
1. OpenAI - for AI processing
   Video guide: [Loom link]

2. Google Workspace - for email/calendar
   Video guide: [Loom link]

3. HubSpot - for CRM integration
   Video guide: [Loom link]

STEPS FOR EACH:
1. Create account (or use existing)
2. Go to API settings
3. Generate new API key
4. Enter directly in n8n (I'll show you)

IMPORTANT:
- You'll own these accounts and pay for usage directly
- This gives you full visibility into costs
- You can revoke access anytime

Let me know when ready and we'll configure together!
```

---

## Service-Specific Setup Guides

### OpenAI

```
OPENAI API KEY SETUP:

1. Go to: platform.openai.com
2. Sign in or create account
3. Add billing info (Settings  Billing)
4. Set usage limits (important!)
5. Go to: API Keys
6. Click: "Create new secret key"
7. Name it: "n8n Production"
8. Copy key IMMEDIATELY (shown once only)
9. In n8n:
   - Go to Credentials
   - Add Credential  OpenAI
   - Paste key
   - Save
10. Test connection

BILLING TIPS:
- Set monthly budget limit
- Set usage alerts
- Monitor dashboard regularly
- Start with GPT-3.5 before GPT-4
```

### Anthropic (Claude)

```
ANTHROPIC API KEY SETUP:

1. Go to: console.anthropic.com
2. Sign in or create account
3. Complete verification
4. Go to: API Keys
5. Click: "Create Key"
6. Name it: "n8n Production"
7. Copy key IMMEDIATELY
8. In n8n:
   - Add Credential  Anthropic
   - Paste key
   - Save
9. Test connection

BILLING:
- Pre-purchase credits
- Monitor usage in console
```

### Google Workspace

```
GOOGLE API SETUP:

For OAuth (Gmail, Calendar, Drive):

1. Go to: console.cloud.google.com
2. Create new project
3. Enable required APIs:
   - Gmail API
   - Google Calendar API
   - Google Drive API
4. Configure OAuth consent screen
5. Create OAuth 2.0 credentials
6. Download client ID and secret
7. In n8n:
   - Add Google credential type
   - Enter client ID and secret
   - Authorize with Google account
8. Test connection

FOR SERVICE ACCOUNTS (Server-to-Server):
- Create service account
- Download JSON key
- Grant access to resources
- Configure in n8n
```

### HubSpot

```
HUBSPOT API KEY SETUP:

1. Log in to HubSpot
2. Go to: Settings (gear icon)
3. Navigate to: Integrations  Private Apps
4. Create a private app
5. Select required scopes:
   - contacts (read/write)
   - deals (read/write)
   - etc.
6. Generate access token
7. Copy token
8. In n8n:
   - Add Credential  HubSpot
   - Select "Access Token"
   - Paste token
   - Save
9. Test connection
```

### Slack

```
SLACK API SETUP:

1. Go to: api.slack.com/apps
2. Create new app
3. Choose "From scratch"
4. Select workspace
5. Add Bot Token Scopes:
   - chat:write
   - channels:read
   - users:read
   - etc.
6. Install to workspace
7. Copy Bot User OAuth Token
8. In n8n:
   - Add Credential  Slack
   - Paste token
   - Save
9. Test by sending message
```

---

## Secure Credential Transfer

### When Client Must Share With You

**Preferred Methods (In Order):**

```
1. PASSWORD MANAGER (Best)
   - 1Password
   - Bitwarden
   - LastPass

   Process:
   a. Client creates shared vault
   b. OR creates one-time share link
   c. Link sent via Slack/email
   d. You access and enter in n8n
   e. Link expires

2. DIRECT ENTRY (Second Best)
   - Schedule video call
   - Client types credentials
   - You never see the value
   - Credentials go directly to n8n

3. ENCRYPTED MESSAGE
   - Client sends via Signal
   - Or uses encrypted email
   - Delete after entering

NEVER:
- Plain text email
- Slack/Teams message
- Shared Google Doc
- Screenshot
- Text message
```

### One-Time Share Link Setup (1Password)

```
1PASSWORD SECURE SHARING:

1. Client opens 1Password
2. Find or create credential entry
3. Click Share
4. Choose "Anyone with link"
5. Set expiration: "1 hour"
6. Set view limit: "1 view"
7. Copy link
8. Send link to you
9. You click link, copy value
10. Enter in n8n
11. Link auto-expires
```

### Bitwarden Send

```
BITWARDEN SEND SETUP:

1. Client opens Bitwarden
2. Go to "Send"
3. Create new Send
4. Select "Text" type
5. Enter credential value
6. Set options:
   - Deletion date: 1 hour
   - Max access count: 1
   - Password protect (optional)
7. Create Send
8. Copy link
9. Send to you
10. You access, copy, enter in n8n
```

---

## Credential Organization in n8n

### Naming Convention

```
FORMAT: [Service] - [Environment] - [Purpose]

EXAMPLES:
 OpenAI - Production - Main
 OpenAI - Testing - Development
 Google - Production - Gmail Access
 HubSpot - Production - CRM

 API Key 1
 New credential
 test123
```

### Credential Documentation

Create a credential inventory (store securely, not in workflow):

```markdown
# Credential Inventory - [Project Name]

## Production Credentials

| Name in n8n | Service | Owner | Created | Last Rotated |
|-------------|---------|-------|---------|--------------|
| [Service] - Production | [Service] | Client | 2025-01-15 | 2025-01-15 |
| Google - Production | Google | Client | 2025-01-15 | 2025-01-15 |
| HubSpot - Production | HubSpot | Client | 2025-01-16 | 2025-01-16 |

## Test Credentials (If Separate)

| Name in n8n | Service | Owner | Notes |
|-------------|---------|-------|-------|
| OpenAI - Testing | OpenAI | Consultant | Temporary, remove at handover |

## Credential Rotation Schedule

| Credential | Next Rotation | Responsible |
|------------|---------------|-------------|
| All credentials | Every 90 days | Client |
```

---

## Billing Transparency

### Why Client-Owned Billing Matters

```
BENEFITS:

For Client:
- See exactly what they pay
- Understand usage patterns
- Control spending limits
- No markup concerns
- Direct relationship with vendor

For You:
- No billing disputes
- No cash flow issues
- No usage explanations needed
- Clean separation of concerns
- Easier offboarding
```

### Usage Monitoring Dashboard

Help clients set up monitoring:

```
FOR OPENAI:

1. platform.openai.com  Usage
2. Set monthly budget limit
3. Set alert thresholds
4. Review daily/weekly
5. Track by API key if multiple

FOR OTHER SERVICES:
- Share dashboard access
- Set up alerts
- Create monthly review process
```

### Cost Estimation Template

```
MONTHLY COST ESTIMATE

Service: OpenAI
Model: GPT-4
Estimated requests/month: 1,000
Average tokens per request: 2,000
Estimated cost: ~$X/month

Service: [Other]
Estimated usage: [X]
Estimated cost: $X/month

TOTAL ESTIMATED: $X/month

Notes:
- Actual usage may vary
- Monitor and adjust as needed
- Costs are client's responsibility
```

---

## Test vs Production Credentials

### Best Practice: Separate Environments

```
TEST ENVIRONMENT:
- Consultant-owned credentials (temporary)
- Limited budget/usage
- Sandboxed data
- For development only

PRODUCTION ENVIRONMENT:
- Client-owned credentials
- Full budget as needed
- Real data
- For live use

AT HANDOVER:
- Remove all test credentials
- Ensure only production creds remain
- Client verifies access
```

### Credential Swap Process

```
HANDOVER CREDENTIAL SWAP:

1. Identify test credentials to remove:
    OpenAI - Testing
    [Other test creds]

2. Verify production credentials exist:
    OpenAI - Production
    [All required prod creds]

3. Update workflow to use production:
   - Open each node using credentials
   - Change from test to production
   - Save workflow

4. Test workflow with production creds:
    Trigger test execution
    Verify all nodes work
    Check no errors

5. Remove test credentials:
    Go to Credentials
    Delete each test credential
    Verify not in use

6. Revoke test API keys in services:
    OpenAI: Delete test key
    [Other services]
```

---

## Common Issues & Solutions

### Issue: Client Can't Create API Key

```
SOLUTION:
1. Verify they have correct permissions
2. Check account is verified
3. Billing may need to be set up first
4. Try different browser/incognito
5. Contact service support
```

### Issue: Credential Not Working

```
TROUBLESHOOTING:
1. Copy key again (no extra spaces)
2. Check key hasn't expired
3. Verify correct key type
4. Check API scopes/permissions
5. Test in Postman/curl first
6. Check rate limits/billing
```

### Issue: Client Worried About Security

```
REASSURANCE:
- Credentials encrypted in n8n
- You don't see raw values (in workflow)
- They can revoke anytime
- They control the account
- Standard industry practice
```

### Issue: Client Wants You to Own Credentials

```
RESPONSE:
"I understand you want to simplify things! However,
having you own the credentials is actually better
because:

1. You see exactly what you're paying
2. You have full control
3. If we ever stop working together, there's no
   transition needed
4. It's cleaner for security and compliance

I'll make the setup super easy with video guides!"
```

---

## Quick Reference

### Credential Setup Checklist

```
FOR EACH REQUIRED SERVICE:

 Service: _____________________________
 Client has account
 Billing configured
 API key generated
 Appropriate permissions/scopes
 Key entered in n8n
 Connection tested
 Naming convention followed
 Documented in inventory
```

### Handover Credential Checklist

```
 All test credentials removed from n8n
 All test API keys revoked in services
 Only production credentials remain
 All credentials are client-owned
 Credential inventory delivered
 Client knows how to rotate keys
 Client knows how to monitor usage
```

---

**Next**: See `04-testing-qa-framework.md` for testing methodology.
