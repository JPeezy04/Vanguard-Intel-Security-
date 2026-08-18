import hashlib

# Vanguard Intel - Oil Data Security Validator
# Checks incoming oil inventory data before it enters the LLM pipeline.

TRUSTED_SOURCES = ["EIA", "API", "VANGUARD_INTEL"]

TRUSTED_HASH = "10dafc75b8b011d09fa44597cd0c3cbd926e6c7b49a69529eb24752bd17f038e"


def generate_data_hash(data):
    data_string = f"{data['source']}|{data['date']}|{data['inventory']}|{data['unit']}"
    return hashlib.sha256(data_string.encode()).hexdigest()

def verify_data_integrity(data):
    current_hash = generate_data_hash(data)
    if current_hash == TRUSTED_HASH:
        return True, "INTEGRITY VERIFIED: Data has not been altered"
    else:
        return False, "INTEGRITY FAILED: Data may have been altered"

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

data_hash = generate_data_hash(oil_data)
print("SHA-256:", data_hash)

integrity_valid, integrity_message = verify_data_integrity(oil_data)
print(integrity_message)