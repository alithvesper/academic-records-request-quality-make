# Testing Results

| Request | Input condition | Expected result | Actual result | Pass/fail | Notes |
|---|---|---|---|---|---|
| REQ-2001 | Valid record correction | records_office_queue / ready |  |  |  |
| REQ-2002 | No supporting items | review_queue / needs_review |  |  |  |
| REQ-2003 | Authorization pending | review_queue / needs_review |  |  |  |
| REQ-2004 | Valid document request | document_services_queue / ready |  |  |  |
| REQ-2005 | Duplicate request | duplicate_queue / duplicate |  |  |  |
| REQ-2006 | Missing request type | review_queue / needs_review |  |  |  |
| REQ-2007 | Valid program change | program_change_queue / ready |  |  |  |
| REQ-2008 | Sensitive language | review_queue / needs_review |  |  |  |
| AI-01 | Low-confidence AI output | review_queue / needs_review |  |  |  |
| AI-02 | Category conflict | review_queue / needs_review |  |  |  |
| AI-03 | Invalid AI output | review_queue / needs_review |  |  |  |
