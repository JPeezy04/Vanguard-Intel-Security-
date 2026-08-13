# Vanguard Intel - Oil Data Security Validator
# Checks incoming oil invenotry data before it enters the LLM pipeline.

TRUSTED_SOURCES = ["EIA", "API", "VANGUARD_INTEL"]

def validate_oil_data(data):
    required_fields = ["source", "date", "inventory", "unit"]

    for field in required_fields:
        if field not in data:
            return False, f"REJECTED: Missing required field: {field}"
    if data["source"].upper() not in TRUSTED_SOURCES:
        return False, "REJECTED: Untrusted data source"

    if not isinstance(data["inventory"], (int, float)):
        return False, "REJECTED: Inventory value must be numeric"

    if data["unit"].lower() != "barrels":
        return False, "REJECTED: Invalid inventory unit"

    return True, "ACCEPTED: Oil data passed security validation"

oil_data = {
    "source": "EIA",
    "date": "2026-08-13",
    "inventory": 50000,
    "unit": "barrels"
}

valid, message = validate_oil_data(oil_data)
print(message)