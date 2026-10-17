# Academic Records Change-Request Quality and Routing System

## Project status

Practice project / synthetic-data prototype.

## Problem

Academic-services teams may receive incomplete, duplicate, inconsistent,
or difficult-to-route change requests.

## Goal

Demonstrate a controlled workflow for administrative validation,
classification, routing, and human review.

## Safety boundary

This project does not approve or deny academic requests, determine
transfer-credit equivalency, interpret academic policy, change student
records, or process real student data.

## Synthetic-data statement

All records use fictional identifiers and synthetic values.
No student information, institutional credentials, or student-system
access were used.

## Workflow summary

1. Receive synthetic JSON request by webhook.
2. Normalize request fields.
3. Create an Airtable request record and supporting-item records.
4. Check duplicates.
5. Validate required fields and supporting items.
6. Check authorization status.
7. Detect sensitive or high-risk language.
8. Send eligible requests to AI classification.
9. Validate structured AI output.
10. Route complete requests or create human-review items.
11. Record workflow outcomes.

## Why Make

Make supports webhook intake, variable transformation, iteration over
supporting-item arrays, Router-based branching, Airtable operations,
AI modules, and structured-output validation.

## Scenario split

Scenario A performs intake, normalization, validation, duplicate checks,
and safety screening.

Scenario B performs AI classification, AI-output validation, category-conflict
checking, and final routing.

## Deterministic logic

- Missing required fields route to review.
- Zero supporting items route to review.
- Unconfirmed authorization routes to review.
- Duplicate keys route to the duplicate queue.
- Sensitive or high-risk language routes to review.
- Valid requests route by request category.
- Uncertain, invalid, conflicting, or unmatched AI results route to review.

## AI role

The AI classifies the request type, normalizes the requested change,
summarizes the request, and identifies ambiguity.

The AI does not approve, deny, or make an academic decision.

## Data model

- Academic Requests
- Supporting Items
- Workflow Runs
- Review Queue

## Error handling

The workflow handles missing fields, zero supporting items, unconfirmed
authorization, duplicates, sensitive language, invalid AI output, category
conflicts, unmatched routes, and integration failures.

## Testing

See `docs/testing-results.md`.

## Measured prototype results

Report only results actually observed from the test runs.

## Limitations

- Synthetic data only.
- No production deployment.
- No student information system integration.
- No academic decision support.
- No security or compliance certification.
- Duplicate detection is limited to the documented key.
- AI classification requires human review when uncertain.

## Future improvements

- Stronger authentication.
- Formal schema validation.
- More robust idempotency.
- Role-based access controls.
- Privacy review.
- Secure deployment.
- Integration testing with approved systems.
- Operational monitoring.
