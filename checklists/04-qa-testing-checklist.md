# QA & Testing Checklist
## Comprehensive Quality Assurance Framework

---

## Test Data Preparation

### Client Sample Data
```
 Sample data requested from client
    Type: _________________________________
    Quantity: _____________________________
    Format: _______________________________

 Data represents real usage
 Edge cases included in samples
 Sensitive data anonymized (if needed)
 Data stored securely for testing
```

### Test Data Categories
```
 Happy path data (normal inputs)
    Count: ________________________________

 Edge case data
     Empty/null values
     Very short inputs
     Very long inputs
     Special characters
     Unicode/international text
     Numbers at boundaries
     Dates at boundaries

 Invalid data
     Wrong format
     Missing required fields
     Malformed JSON
     Unexpected data types

 Adversarial data (if AI)
     Prompt injection attempts
     Jailbreak attempts
     Off-topic inputs
     Harmful content
```

---

## Functional Testing

### Trigger Testing
```
Trigger Type: _____________________________

 Trigger fires correctly
 Trigger data parsed properly
 Multiple trigger scenarios tested:
    Scenario 1: _____________ Result: _____
    Scenario 2: _____________ Result: _____
    Scenario 3: _____________ Result: _____

 Trigger authentication works
 Invalid triggers rejected properly
```

### Node-by-Node Testing
```
For each major node:

Node: ____________________________________
 Input data correct
 Processing logic correct
 Output data correct
 Error cases handled

Node: ____________________________________
 Input data correct
 Processing logic correct
 Output data correct
 Error cases handled

Node: ____________________________________
 Input data correct
 Processing logic correct
 Output data correct
 Error cases handled
```

### Integration Testing
```
For each integration:

Integration: ______________________________
 Authentication successful
 API calls succeed
 Data mapping correct
 Error responses handled
 Rate limits respected

Integration: ______________________________
 Authentication successful
 API calls succeed
 Data mapping correct
 Error responses handled
 Rate limits respected
```

### End-to-End Testing
```
 Complete workflow tested start-to-finish
 All branches/paths tested:
    Path 1: ______________ Result: ________
    Path 2: ______________ Result: ________
    Path 3: ______________ Result: ________

 Final output matches expectations
 Side effects verified (emails sent, records created, etc.)
```

---

## Error Handling Testing

### Error Scenarios
```
 API timeout
    Expected behavior: ____________________
    Actual behavior: ______________________
     Pass  Fail

 API error response (4xx, 5xx)
    Expected behavior: ____________________
    Actual behavior: ______________________
     Pass  Fail

 Invalid input data
    Expected behavior: ____________________
    Actual behavior: ______________________
     Pass  Fail

 Missing required data
    Expected behavior: ____________________
    Actual behavior: ______________________
     Pass  Fail

 Rate limit hit
    Expected behavior: ____________________
    Actual behavior: ______________________
     Pass  Fail

 Downstream service unavailable
    Expected behavior: ____________________
    Actual behavior: ______________________
     Pass  Fail
```

### Error Recovery
```
 Retry logic works
    Retry count: __________________________
    Backoff strategy: _____________________

 Fallback logic works
    Fallback action: ______________________

 Graceful degradation tested
 Error notifications sent correctly
 Error logging works
```

---

## AI-Specific Testing

### Response Quality
```
Test inputs: ______ (minimum 20-50 samples)

 Relevance score
    Relevant responses: ____%
    Threshold: _________%
     Pass  Fail

 Accuracy score
    Accurate responses: ____%
    Threshold: __________%
     Pass  Fail

 Format compliance
    Correct format: ____%
    Threshold: __________%
     Pass  Fail
```

### Tone & Safety
```
 Tone matches requirements
     Professional
     Friendly
     Technical
     Other: _____________________________

 No toxic/harmful content
 No off-brand responses
 No leaked system prompts
 No hallucinated information (critical)
```

### Consistency Testing
```
 Same input  similar output
    Test count: ___________________________
    Consistency rate: _____%

 Randomness acceptable
 No contradictory responses
```

### Prompt Injection Testing
```
 "Ignore previous instructions" - blocked
 "What is your system prompt" - blocked
 Adversarial inputs - handled safely
 No unintended actions triggered
```

### Model Comparison (If Done)
```
Model 1: _________________________________
    Quality score: _______
    Cost per request: _______
    Latency: _______

Model 2: _________________________________
    Quality score: _______
    Cost per request: _______
    Latency: _______

Selected: ________________________________
Reason: __________________________________
```

---

## Performance Testing

### Execution Time
```
 Average execution time: _________ seconds
 Acceptable threshold: _________ seconds
  Pass  Fail

 Slowest execution: _________ seconds
 Bottleneck identified: _________________
```

### Volume Testing
```
 Tested with high volume
    Volume tested: ________________________
    Success rate: ______%
    Error rate: ______%

 No memory issues
 No timeout issues
 Rate limits respected
```

### Cost Testing
```
 Cost per execution calculated
    AI tokens: ____________________________
    API calls: ____________________________
    Total per execution: $_________________

 Monthly projection: $__________________
 Cost within budget:  Yes  No
```

---

## Scale Testing Log

```
| # | Input Summary | Output Result | Pass/Fail | Notes |
|---|---------------|---------------|-----------|-------|
| 1 |               |               |           |       |
| 2 |               |               |           |       |
| 3 |               |               |           |       |
| 4 |               |               |           |       |
| 5 |               |               |           |       |
| 6 |               |               |           |       |
| 7 |               |               |           |       |
| 8 |               |               |           |       |
| 9 |               |               |           |       |
| 10|               |               |           |       |
```

(Expand as needed - recommend 50+ tests for AI workflows)

---

## Internal QA Summary

```
Test Phase: Internal QA
Tester: ___________________________________
Date: _____________________________________

Total Tests Run: __________________________
Passed: ___________________________________
Failed: ___________________________________
Blocked: __________________________________

Pass Rate: _______%

Critical Issues Found: ____________________
High Issues Found: ________________________
Medium Issues Found: ______________________
Low Issues Found: _________________________

Ready for Client QA:  Yes  No

If No, blocking issues:
1. ________________________________________
2. ________________________________________
3. ________________________________________
```

---

## Client QA

### Client Testing Setup
```
 Testing interface provided
    Type:  Chat  Form  Direct n8n  Other

 Testing instructions sent
 Example test cases provided
 Feedback method established
     Form
     Email
     Sheet
     Other: _____________________________

 Testing timeline communicated
    Start: ________________________________
    End: __________________________________
```

### Client Feedback Log
```
| # | Issue Description | Severity | Status | Resolution |
|---|-------------------|----------|--------|------------|
| 1 |                   |          |        |            |
| 2 |                   |          |        |            |
| 3 |                   |          |        |            |
| 4 |                   |          |        |            |
| 5 |                   |          |        |            |
```

### Post-Feedback Resolution
```
 All critical issues resolved
 All high issues resolved
 Medium/low issues addressed or deferred
 Client re-tested after fixes
 Client approved
```

---

## QA Sign-Off

```
╔═══════════════════════════════════════════════════════════════╗
║                     QA SIGN-OFF                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ Project: _______________________________________________      ║
║                                                               ║
║ QA completed by: _______________________________________     ║
║ Date: _________________________________________________      ║
║                                                               ║
║ All functional tests passed:   Yes   No                    ║
║ All error handling tested:     Yes   No                    ║
║ AI quality acceptable:         Yes   No   N/A             ║
║ Security review passed:        Yes   No                    ║
║ Client QA approved:            Yes   No                    ║
║                                                               ║
║ READY FOR PRODUCTION:          Yes   No                    ║
║                                                               ║
║ Notes: ________________________________________________      ║
║ ________________________________________________________     ║
║                                                               ║
║ Signature: ____________________________________________      ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

**Next**: See `05-handover-checklist.md` for delivery requirements.
