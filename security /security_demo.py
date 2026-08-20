import data_validator
import sbom_scanner
import access_control

print("=" * 40)
print("VANGUARD INTEL SECURITY DEMO")
print("=" * 40)
print()
print("1. Oil Data Validation")
print("2. Integrity / Tamper Detection")
print("3. SBOM Security Scan")
print("4. Authenticiation & Access Control")
print("5. Run Full Security Demo")

choice = input("\nSelect option: ")
if choice == "1":
    print("\nRunning Oil Data Validation")
    print(data_validator.validate_oil_data(data_validator.oil_data))

elif choice == "2":
     print("\nRunning Integrity / Tamper Detection")
     print(data_validator.verify_data_integrity(data_validator.oil_data))

elif choice == "3":
     print("\nRunning SBOM Security Scan")
     sbom_scanner.scan_sbom(sbom_scanner.SBOM)

elif choice == "4":
     print("\nRunning Authentication & Access Control")
     username = input("Username: ")
     password = input("Password: ")
     success, message = access_control.authenticate(username, password)
     print(message)

elif choice == "5":
     print("\nRunning Full Vanguard Intel Security Demo")
     print("\n[1/4] Checking Oil Data")
     print(data_validator.validate_oil_data(data_validator.oil_data))
     print("\n[2/4] Checking Data Integrity")
     print(data_validator.verify_data_integrity(data_validator.oil_data))
     print("\n[3/4] Scanning SBOM Dependencies")
     sbom_scanner.scan_sbom(sbom_scanner.SBOM)
     print("\n[4/4] Testing Authentication")
     username = input("Username: ")
     password = input("Password: ")
     success, message = access_control.authenticate(username, password)
     print(message)

     print("\n" + "=" * 40)
     print("VANGUARD INTEL SECURITY DEMO COMPLETE")
     print("=" * 40)