import csv
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "request_id",
    "submitted_at",
    "requester_token",
    "request_type",
    "program_code",
    "campus_code",
    "requested_change",
    "authorization_status",
]

ALLOWED_REQUEST_TYPES = {
    "record_correction",
    "enrollment_status_update",
    "transfer_credit_review",
    "document_request",
    "program_change_request",
}

SENSITIVE_TERMS = {
    "falsified",
    "fraud",
    "threat",
    "harassment",
    "discrimination",
    "legal action",
}

ROUTE_MAP = {
    "record_correction": "records_office_queue",
    "enrollment_status_update": "enrollment_services_queue",
    "transfer_credit_review": "transfer_credit_queue",
    "document_request": "document_services_queue",
    "program_change_request": "program_change_queue",
}

def normalize(value):
    return (value or "").strip().lower()

def validate_row(row, seen_keys):
    errors = []

    for field in REQUIRED_FIELDS:
        if not normalize(row.get(field)):
            errors.append(f"missing:{field}")

    try:
        item_count = int(row.get("supporting_item_count") or 0)
    except ValueError:
        item_count = -1
        errors.append("invalid:supporting_item_count")

    if item_count == 0:
        errors.append("missing:supporting_items")

    if normalize(row.get("authorization_status")) != "confirmed":
        errors.append("review:authorization_not_confirmed")

    request_type = normalize(row.get("request_type"))
    if request_type and request_type not in ALLOWED_REQUEST_TYPES:
        errors.append("invalid:request_type")

    duplicate_key = "|".join(
        [
            normalize(row.get("requester_token")),
            normalize(row.get("program_code")),
            normalize(row.get("campus_code")),
            request_type,
        ]
    )

    duplicate = duplicate_key in seen_keys and duplicate_key != "||||"
    if duplicate:
        errors.append("duplicate:possible_duplicate")

    seen_keys.add(duplicate_key)

    text = normalize(row.get("requested_change")) + " " + normalize(row.get("notes"))
    sensitive_terms = sorted(term for term in SENSITIVE_TERMS if term in text)

    if sensitive_terms:
        errors.append("review:sensitive_language")

    if duplicate:
        status = "duplicate"
        route = "duplicate_queue"
    elif errors:
        status = "needs_review"
        route = "review_queue"
    else:
        status = "ready"
        route = ROUTE_MAP.get(request_type, "review_queue")

    return {
        "request_id": row.get("request_id"),
        "status": status,
        "route": route,
        "errors": errors,
        "sensitive_terms": sensitive_terms,
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python validate_requests.py data/academic_requests_test_cases.csv")

    path = Path(sys.argv[1])
    seen_keys = set()
    results = []

    with path.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            results.append(validate_row(row, seen_keys))

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
