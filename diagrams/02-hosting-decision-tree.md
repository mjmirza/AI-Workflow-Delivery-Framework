# Hosting Decision Tree
## Choose the Right Hosting Model for Every Client

---

## Primary Decision Flowchart

```mermaid
flowchart TB
    START([" START: New Client Project"]) --> Q1

    Q1{"Will client need to<br/>access n8n directly?"}
    Q1 -->|"Yes, they need to<br/>see/edit workflows"| CLIENT_HOST
    Q1 -->|"No, they just want<br/>the end result"| Q2

    Q2{"Are you delivering a<br/>recurring service or<br/>one-time deliverable?"}
    Q2 -->|"One-time deliverable<br/>(JSON + docs)"| EXPORT_MODEL
    Q2 -->|"Recurring service<br/>(ongoing delivery)"| Q3

    Q3{"Does client need to<br/>connect their own<br/>credentials/data?"}
    Q3 -->|"Yes"| CLIENT_HOST
    Q3 -->|"No, you control<br/>all data sources"| INTERNAL_HOST

    subgraph CLIENT_HOST[" CLIENT HOSTS N8N"]
        direction TB
        CH1["Client owns n8n instance"]
        CH2["You're invited as team member"]
        CH3["Client pays for all APIs"]
        CH4["Clean handover possible"]

        CH1 --> CH2 --> CH3 --> CH4

        CH_OPTIONS{"Which n8n option?"}
        CH_CLOUD["n8n Cloud<br/>Easiest setup"]
        CH_VPS["Self-hosted VPS<br/>More control"]
        CH_LOCAL["Local/On-prem<br/>Maximum privacy"]

        CH4 --> CH_OPTIONS
        CH_OPTIONS --> CH_CLOUD
        CH_OPTIONS --> CH_VPS
        CH_OPTIONS --> CH_LOCAL
    end

    subgraph INTERNAL_HOST[" INTERNAL HOSTING"]
        direction TB
        IH1["You host for internal ops"]
        IH2["Client never sees n8n"]
        IH3["You deliver end results"]
        IH4["Careful: Not for SaaS"]

        IH1 --> IH2 --> IH3 --> IH4
    end

    subgraph EXPORT_MODEL[" EXPORT MODEL"]
        direction TB
        EM1["Build in your environment"]
        EM2["Export as JSON"]
        EM3["Deliver with Loom guide"]
        EM4["Client imports themselves"]

        EM1 --> EM2 --> EM3 --> EM4
    end

    style CLIENT_HOST fill:#c8e6c9,stroke:#2e7d32
    style INTERNAL_HOST fill:#fff9c4,stroke:#f9a825
    style EXPORT_MODEL fill:#e3f2fd,stroke:#1565c0
```

---

## Detailed Decision Matrix

```mermaid
flowchart LR
    subgraph CRITERIA[" Decision Criteria"]
        C1["Client Technical Level"]
        C2["Data Sensitivity"]
        C3["Ongoing Relationship"]
        C4["Budget"]
        C5["Compliance Requirements"]
    end

    subgraph OPTIONS["Hosting Options"]
        subgraph CLOUD["n8n Cloud"]
            CLOUD_PROS[" Easy setup<br/> Managed updates<br/> Quick start"]
            CLOUD_CONS[" Monthly cost<br/> Less control<br/> Data in cloud"]
        end

        subgraph VPS["Self-Hosted VPS"]
            VPS_PROS[" Full control<br/> Custom config<br/> One-time setup"]
            VPS_CONS[" Tech required<br/> Maintenance<br/> Security burden"]
        end

        subgraph LOCAL["Local/On-Prem"]
            LOCAL_PROS[" Max privacy<br/> No cloud deps<br/> Full control"]
            LOCAL_CONS[" Complex setup<br/> No remote access<br/> Hardware costs"]
        end
    end

    style CLOUD fill:#e3f2fd
    style VPS fill:#fff3e0
    style LOCAL fill:#f3e5f5
```

---

## n8n Cloud vs Self-Hosted Decision

```mermaid
flowchart TB
    START(["Choose n8n Deployment"]) --> Q1

    Q1{"Client's technical<br/>capability?"}
    Q1 -->|"Non-technical"| CLOUD_PATH
    Q1 -->|"Has IT team"| Q2
    Q1 -->|"Developer/Technical"| Q3

    Q2{"Data sensitivity<br/>requirements?"}
    Q2 -->|"Standard business data"| CLOUD_PATH
    Q2 -->|"Highly sensitive/regulated"| SELF_HOST_PATH

    Q3{"Budget for<br/>infrastructure?"}
    Q3 -->|"Prefers OpEx (monthly)"| CLOUD_PATH
    Q3 -->|"Prefers CapEx (one-time)"| SELF_HOST_PATH

    subgraph CLOUD_PATH["n8n CLOUD"]
        CLOUD1["Sign up at cloud.n8n.io"]
        CLOUD2["Choose plan based on executions"]
        CLOUD3["Invite consultant as team member"]
        CLOUD4["Configure credentials"]
        CLOUD1 --> CLOUD2 --> CLOUD3 --> CLOUD4
    end

    subgraph SELF_HOST_PATH["SELF-HOSTED"]
        SH1{"Which platform?"}

        subgraph DOCKER["Docker Option"]
            D1["Provision VPS<br/>(DigitalOcean, AWS, etc.)"]
            D2["Install Docker"]
            D3["Deploy n8n container"]
            D4["Configure SSL/domain"]
        end

        subgraph RAILWAY["Railway/Render"]
            R1["One-click deploy"]
            R2["Auto-scaling"]
            R3["Managed container"]
        end

        subgraph K8S["Kubernetes"]
            K1["Enterprise scale"]
            K2["Helm charts"]
            K3["High availability"]
        end

        SH1 -->|"Simple"| DOCKER
        SH1 -->|"Medium"| RAILWAY
        SH1 -->|"Enterprise"| K8S
    end

    style CLOUD_PATH fill:#e3f2fd,stroke:#1565c0
    style SELF_HOST_PATH fill:#fff3e0,stroke:#ff6f00
```

---

## License Compliance Checker

```mermaid
flowchart TB
    START([" Check License Compliance"]) --> Q1

    Q1{"Who is using the<br/>n8n instance?"}
    Q1 -->|"Single business"| SINGLE
    Q1 -->|"Multiple clients"| MULTI

    SINGLE --> Q2{"Who owns/pays for<br/>the instance?"}
    Q2 -->|"The business using it"| COMPLIANT1
    Q2 -->|"Third party (consultant)"| Q3

    Q3{"Does the business<br/>log in to n8n?"}
    Q3 -->|"No, never"| INTERNAL_OK
    Q3 -->|"Yes"| NEEDS_LICENSE

    MULTI --> NEEDS_LICENSE

    COMPLIANT1([" COMPLIANT<br/>Standard client hosting"])
    INTERNAL_OK([" COMPLIANT<br/>Internal agency use"])
    NEEDS_LICENSE([" NEEDS LICENSE<br/>Commercial/Enterprise required"])

    style COMPLIANT1 fill:#c8e6c9,stroke:#2e7d32
    style INTERNAL_OK fill:#c8e6c9,stroke:#2e7d32
    style NEEDS_LICENSE fill:#ffcdd2,stroke:#c62828
```

---

## Client Readiness Assessment

```mermaid
flowchart TB
    subgraph ASSESSMENT[" Client Readiness Matrix"]
        direction LR

        subgraph TECH["Technical Readiness"]
            T1["Has IT support?"]
            T2["Manages own servers?"]
            T3["Uses cloud services?"]
            T4["Has developer access?"]
        end

        subgraph DATA["Data Considerations"]
            D1["Data sensitivity level"]
            D2["Compliance requirements"]
            D3["Existing integrations"]
            D4["Data volume"]
        end

        subgraph BIZ["Business Factors"]
            B1["Budget type (OpEx/CapEx)"]
            B2["Long-term commitment"]
            B3["Growth expectations"]
            B4["Internal resources"]
        end
    end

    subgraph SCORING["Scoring"]
        HIGH["High Readiness<br/> Self-hosted VPS"]
        MEDIUM["Medium Readiness<br/> n8n Cloud"]
        LOW["Low Readiness<br/> n8n Cloud + Support"]
    end

    ASSESSMENT --> SCORING
```

---

## Hosting Setup Workflows

### For n8n Cloud Setup

```mermaid
sequenceDiagram
    participant Consultant as  Consultant
    participant Client as  Client
    participant N8N as n8n Cloud

    Note over Consultant,N8N: n8n Cloud Setup Flow

    Consultant->>Client: Send setup instructions<br/>(Loom video recommended)
    Client->>N8N: Create account at cloud.n8n.io
    Client->>N8N: Choose subscription plan
    Client->>N8N: Enter billing information

    N8N->>Client: Account active

    Client->>N8N: Go to Settings > Users
    Client->>N8N: Invite consultant email

    N8N->>Consultant: Invitation email

    Consultant->>N8N: Accept invitation
    Consultant->>N8N: Verify access to workspace

    Note over Consultant: Ready to build!
```

### For Self-Hosted Setup

```mermaid
sequenceDiagram
    participant Consultant as  Consultant
    participant Client as  Client
    participant VPS as VPS Provider
    participant N8N as  n8n Instance

    Note over Consultant,N8N: Self-Hosted Setup Flow

    Consultant->>Client: Recommend VPS provider
    Client->>VPS: Create account & provision server
    Client->>VPS: Configure SSH access

    alt Consultant Assists
        Client->>Consultant: Share temporary access
        Consultant->>VPS: Install Docker & n8n
        Consultant->>VPS: Configure SSL & domain
        Consultant->>Client: Transfer credentials back
    else Client Self-Service
        Consultant->>Client: Send detailed guide
        Client->>VPS: Follow installation steps
        Client->>N8N: Verify installation
    end

    Client->>N8N: Create admin account
    Client->>N8N: Invite consultant as user

    N8N->>Consultant: Access granted

    Note over Consultant: Ready to build!
```

---

## Quick Reference Table

| Scenario | Recommended Hosting | Licensing | Notes |
|----------|---------------------|-----------|-------|
| Client wants to see/manage workflows | Client hosts (Cloud or VPS) | Standard | Most common |
| Client just wants results delivered | Your internal n8n | Standard | Don't expose n8n |
| Selling workflow as JSON export | Either | Standard | One-time delivery |
| Building SaaS/platform | Your hosting | **Commercial** | Contact n8n sales |
| Enterprise with compliance needs | Client self-hosted | Standard | On-prem option |
| Quick prototype/POC | Your internal | Standard | For testing only |

---

## Red Flags to Watch For

```mermaid
flowchart TB
    subgraph REDFLAGS["RED FLAGS - Needs Commercial License"]
        RF1["Multiple clients accessing same n8n"]
        RF2["Charging for n8n access/seats"]
        RF3["Reselling n8n as a product"]
        RF4["Marking up n8n hosting costs"]
        RF5["White-labeling n8n interface"]
    end

    subgraph OKAY[" OKAY - Standard License"]
        OK1["One client per n8n instance"]
        OK2["Billing for consulting/development"]
        OK3["Internal agency automations"]
        OK4["Client pays own hosting"]
        OK5["Exporting workflows as deliverables"]
    end

    style REDFLAGS fill:#ffcdd2
    style OKAY fill:#c8e6c9
```

---

**Next**: See `03-project-lifecycle.md` for the complete project delivery flow.
