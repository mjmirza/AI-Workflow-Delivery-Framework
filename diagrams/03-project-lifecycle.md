# Project Lifecycle Diagram
## End-to-End Workflow Delivery Journey

---

## Complete Project Lifecycle

```mermaid
flowchart TB
    subgraph PHASE1[" PHASE 1: DISCOVERY & SALES"]
        direction TB
        P1A["Lead Inquiry"] --> P1B["Discovery Call"]
        P1B --> P1C["Requirements Gathering"]
        P1C --> P1D["Scope Definition"]
        P1D --> P1E["Proposal & Pricing"]
        P1E --> P1F["Contract Signing"]
    end

    subgraph PHASE2[" PHASE 2: KICKOFF & SETUP"]
        direction TB
        P2A["Kickoff Call"] --> P2B["Collect Sample Data"]
        P2B --> P2C["Environment Setup"]
        P2C --> P2D["Credential Configuration"]
        P2D --> P2E["Integration Testing"]
    end

    subgraph PHASE3[" PHASE 3: DEVELOPMENT"]
        direction TB
        P3A["Build Core Workflow"] --> P3B["Add Error Handling"]
        P3B --> P3C["Implement AI Components"]
        P3C --> P3D["Add Logging/Monitoring"]
        P3D --> P3E["Internal Testing"]
    end

    subgraph PHASE4[" PHASE 4: TESTING & QA"]
        direction TB
        P4A["Internal QA Pass"] --> P4B["Edge Case Testing"]
        P4B --> P4C["Client Testing"]
        P4C --> P4D["Feedback Collection"]
        P4D --> P4E["Refinements"]
    end

    subgraph PHASE5[" PHASE 5: DELIVERY"]
        direction TB
        P5A["Documentation"] --> P5B["Training Videos"]
        P5B --> P5C["Handover Call"]
        P5C --> P5D["Credential Transfer"]
        P5D --> P5E["Go-Live"]
    end

    subgraph PHASE6[" PHASE 6: SUPPORT"]
        direction TB
        P6A["Monitoring Period"] --> P6B["Bug Fixes"]
        P6B --> P6C["Final Invoice"]
        P6C --> P6D{"Ongoing Retainer?"}
        P6D -->|"Yes"| P6E["Maintenance Mode"]
        P6D -->|"No"| P6F["Project Close"]
    end

    PHASE1 --> PHASE2 --> PHASE3 --> PHASE4 --> PHASE5 --> PHASE6

    style PHASE1 fill:#e3f2fd
    style PHASE2 fill:#e8f5e9
    style PHASE3 fill:#fff3e0
    style PHASE4 fill:#fce4ec
    style PHASE5 fill:#f3e5f5
    style PHASE6 fill:#e0f7fa
```

---

## Phase 1: Discovery & Sales (Detailed)

```mermaid
flowchart LR
    subgraph DISCOVERY["Discovery Process"]
        direction TB

        LEAD[" Lead Comes In"]
        QUALIFY[" Qualify Lead"]
        DISC_CALL[" Discovery Call"]

        LEAD --> QUALIFY --> DISC_CALL

        subgraph DISC_AGENDA["Discovery Call Agenda"]
            DA1["Understand their business"]
            DA2["Identify pain points"]
            DA3["Assess technical setup"]
            DA4["Discuss budget range"]
            DA5["Set expectations"]
        end

        DISC_CALL --> DISC_AGENDA
    end

    subgraph SCOPING["Scoping Process"]
        direction TB

        REQUIREMENTS[" Requirements Doc"]
        SCOPE[" Scope of Work"]
        PRICING[" Pricing"]

        subgraph SCOPE_ELEMENTS["Scope Must Include"]
            SE1["Specific workflows to build"]
            SE2["Integrations required"]
            SE3["Success criteria"]
            SE4["What's NOT included"]
            SE5["Definition of done"]
        end

        REQUIREMENTS --> SCOPE --> PRICING
        SCOPE --> SCOPE_ELEMENTS
    end

    subgraph CLOSING["Closing"]
        direction TB

        PROPOSAL[" Send Proposal"]
        NEGOTIATE[" Negotiate if needed"]
        CONTRACT[" Contract Signed"]
        DEPOSIT[" Deposit Received"]

        PROPOSAL --> NEGOTIATE --> CONTRACT --> DEPOSIT
    end

    DISCOVERY --> SCOPING --> CLOSING
```

---

## Phase 2: Kickoff & Setup (Detailed)

```mermaid
sequenceDiagram
    participant C as  Client
    participant Y as  You
    participant N as  n8n

    Note over C,N: KICKOFF CALL

    Y->>C: Schedule kickoff call
    Y->>C: Send pre-call checklist

    rect rgb(230, 245, 255)
        Note over C,Y: Kickoff Call Agenda
        Y->>C: Review scope & timeline
        Y->>C: Explain what you need from them
        C->>Y: Share sample data/examples
        Y->>C: Walk through n8n signup
    end

    Note over C,N: ENVIRONMENT SETUP

    C->>N: Create n8n account
    C->>N: Choose hosting option
    C->>N: Complete billing setup
    C->>N: Invite you as team member
    N->>Y: Invitation received

    Y->>N: Accept & verify access

    Note over C,N: CREDENTIAL SETUP

    rect rgb(255, 245, 230)
        Y->>C: Send credential setup guide (Loom)
        C->>C: Sign up for required APIs
        C->>C: Generate API keys
        C->>N: Enter credentials in n8n
        Y->>N: Verify integrations work
    end

    Note over Y,N: Ready for Development!
```

---

## Phase 3: Development (Detailed)

```mermaid
flowchart TB
    subgraph DEV_CYCLE["Development Cycle"]
        direction LR

        subgraph BUILD[" Build"]
            B1["Create workflow structure"]
            B2["Add trigger nodes"]
            B3["Build core logic"]
            B4["Add AI components"]
            B5["Implement actions"]
        end

        subgraph HARDEN[" Harden"]
            H1["Add error handling"]
            H2["Implement retries"]
            H3["Add fallback logic"]
            H4["Timeout protection"]
            H5["Input validation"]
        end

        subgraph OBSERVE[" Observe"]
            O1["Add execution logging"]
            O2["Error notifications"]
            O3["Usage tracking"]
            O4["AI response logging"]
        end

        BUILD --> HARDEN --> OBSERVE
    end

    subgraph BEST_PRACTICES["Best Practices During Development"]
        BP1[" Use clear node names"]
        BP2[" Add sticky notes for logic"]
        BP3[" Test each section independently"]
        BP4[" Use sub-workflows for reusability"]
        BP5[" Version control with exports"]
        BP6[" Document as you build"]
    end

    DEV_CYCLE --> BEST_PRACTICES
```

---

## Phase 4: Testing & QA (Detailed)

```mermaid
flowchart TB
    subgraph INTERNAL_QA[" Internal QA (You)"]
        direction TB

        IQ1["Test with sample data"]
        IQ2["Run edge cases"]
        IQ3["Intentionally break inputs"]
        IQ4["Verify error handling"]
        IQ5["Check AI output quality"]
        IQ6["Log all results"]

        IQ1 --> IQ2 --> IQ3 --> IQ4 --> IQ5 --> IQ6
    end

    subgraph SCALE_TEST[" Scale Testing"]
        ST1["Run 10+ sample inputs"]
        ST2["Check for consistency"]
        ST3["Monitor execution time"]
        ST4["Verify rate limits"]
    end

    subgraph CLIENT_QA[" Client QA"]
        CQ1["Provide simple testing interface"]
        CQ2["Collect structured feedback"]
        CQ3["Document issues found"]
        CQ4["Prioritize fixes"]
    end

    subgraph REFINEMENT[" Refinement"]
        R1["Fix reported bugs"]
        R2["Tune prompts/models"]
        R3["Adjust formatting"]
        R4["Final verification"]
    end

    INTERNAL_QA --> SCALE_TEST --> CLIENT_QA --> REFINEMENT

    style INTERNAL_QA fill:#e8f5e9
    style SCALE_TEST fill:#fff3e0
    style CLIENT_QA fill:#e3f2fd
    style REFINEMENT fill:#f3e5f5
```

---

## Phase 5: Delivery (Detailed)

```mermaid
flowchart TB
    subgraph PREPARATION[" Preparation"]
        P1["Create production copy"]
        P2["Remove test data/credentials"]
        P3["Enable all logging"]
        P4["Set up backups"]
        P5["Final workflow cleanup"]
    end

    subgraph DOCUMENTATION[" Documentation"]
        D1["Workflow overview document"]
        D2["Loom walkthrough video"]
        D3["Credential setup guide"]
        D4["Troubleshooting FAQ"]
        D5["Contact/support info"]
    end

    subgraph HANDOVER_CALL[" Handover Call"]
        H1["Walk through live system"]
        H2["Show how to monitor"]
        H3["Explain maintenance needs"]
        H4["Answer questions"]
        H5["Confirm acceptance"]
    end

    subgraph GO_LIVE[" Go-Live"]
        G1["Swap test  production creds"]
        G2["Enable workflow"]
        G3["Monitor first executions"]
        G4["Verify everything works"]
        G5["Client confirmation"]
    end

    PREPARATION --> DOCUMENTATION --> HANDOVER_CALL --> GO_LIVE
```

---

## Phase 6: Support & Maintenance (Detailed)

```mermaid
flowchart TB
    subgraph POST_LAUNCH[" Post-Launch (First 7 Days)"]
        PL1["Monitor all executions"]
        PL2["Watch for errors"]
        PL3["Be available for questions"]
        PL4["Quick bug fixes"]
    end

    subgraph CLOSURE[" Project Closure"]
        CL1["Review against scope"]
        CL2["Confirm acceptance"]
        CL3["Send final invoice"]
        CL4["Collect testimonial"]
        CL5["Archive project"]
    end

    subgraph RETAINER_DECISION{"Ongoing Retainer?"}
    end

    subgraph RETAINER_YES[" Maintenance Retainer"]
        RY1["Define SLA"]
        RY2["Monthly check-ins"]
        RY3["Proactive monitoring"]
        RY4["Regular updates"]
        RY5["Bug fixes included"]
    end

    subgraph RETAINER_NO[" No Retainer"]
        RN1["Final handover"]
        RN2["Documentation complete"]
        RN3["Support period ends"]
        RN4["Future work = new project"]
    end

    POST_LAUNCH --> CLOSURE --> RETAINER_DECISION
    RETAINER_DECISION -->|"Yes"| RETAINER_YES
    RETAINER_DECISION -->|"No"| RETAINER_NO
```

---

## Timeline Visualization (Without Time Estimates)

```mermaid
gantt
    title Project Phases (Sequential, No Time Estimates)
    dateFormat  YYYY-MM-DD
    axisFormat  Phase %W

    section Discovery
    Lead Qualification       :done, d1, 2025-01-01, 1d
    Discovery Call          :done, d2, after d1, 1d
    Requirements & Scope    :done, d3, after d2, 1d
    Contract & Deposit      :done, d4, after d3, 1d

    section Setup
    Kickoff Call            :active, s1, after d4, 1d
    Environment Setup       :s2, after s1, 1d
    Credentials Config      :s3, after s2, 1d

    section Development
    Core Build              :dev1, after s3, 1d
    Hardening              :dev2, after dev1, 1d
    Observability          :dev3, after dev2, 1d

    section Testing
    Internal QA             :t1, after dev3, 1d
    Client Testing          :t2, after t1, 1d
    Refinements            :t3, after t2, 1d

    section Delivery
    Documentation           :del1, after t3, 1d
    Handover               :del2, after del1, 1d
    Go-Live                :del3, after del2, 1d

    section Support
    Monitoring Period       :sup1, after del3, 1d
    Project Close          :milestone, after sup1, 0d
```

---

## Milestone Checkpoints

```mermaid
flowchart LR
    M1([" Contract Signed"])
    M2([" Environment Ready"])
    M3([" Core Build Complete"])
    M4([" QA Passed"])
    M5([" Handover Done"])
    M6([" Project Closed"])

    M1 --> M2 --> M3 --> M4 --> M5 --> M6

    style M1 fill:#e3f2fd
    style M2 fill:#e8f5e9
    style M3 fill:#fff3e0
    style M4 fill:#fce4ec
    style M5 fill:#f3e5f5
    style M6 fill:#c8e6c9
```

---

## Phase Exit Criteria

| Phase | Exit Criteria |
|-------|---------------|
| **Discovery** | Contract signed, deposit received, scope document approved |
| **Setup** | n8n access confirmed, all credentials working, integrations tested |
| **Development** | Core workflow functional, error handling in place, logging active |
| **Testing** | Internal QA passed, client testing complete, all critical bugs fixed |
| **Delivery** | Documentation complete, training delivered, client accepts |
| **Support** | Monitoring period complete, final invoice paid, testimonial collected |

---

**Next**: See `04-security-framework.md` for security architecture details.
