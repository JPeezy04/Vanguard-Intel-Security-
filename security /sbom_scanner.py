# Vanguard Intel - SBOM Security Scanner
# Checks software dependecies for security risks

import json 

SBOM = {
    "application": "Vanguard Intel",
    "components": [
        {"name": "Python", "version": "3.12"},
        {"name": "requests", "version": "2.32.3"}
    ]
}

KNOWN_VULNERABILITIES = {
    "requests": {
        "2.32.3": "CVE-DEMO-001"
    }
}



def scan_sbom(sbom):
    print("Vanguard Intel SBOM Security Scan")

    for component in sbom["components"]:
        name = component["name"]
        version = component["version"]

        print(f"Checking {name} version {version}...")

        if name in KNOWN_VULNERABILITIES:
            if version in KNOWN_VULNERABILITIES[name]:
                vulnerability = KNOWN_VULNERABILITIES[name][version]
                print(f"VULNERABLE: {name} {version} - {vulnerability}")
            else:
                print(f"SAFE: {name} {version}")
        else:
            print(f"SAFE: {name} {version}")

scan_sbom(SBOM)
