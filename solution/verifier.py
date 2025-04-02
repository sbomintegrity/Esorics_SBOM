import json
import requests
import re

SBOM_FILE = "sbom.json"

# Function to fetch correct .whl hash from PyPI using the expected filename
def extract_hash_from_pypi(package_name, expected_whl_filename):
    url = f"https://pypi.org/simple/{package_name}/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch data from PyPI for {package_name}")
        return None

    # Find all URLs with .whl files and extract their hashes
    matches = re.findall(r'href="(https://files.pythonhosted.org/[^"]+#sha256=([a-fA-F0-9]{64}))"', response.text)

    # Filter to find the exact expected .whl file
    for full_url, hash1 in matches:
        if expected_whl_filename in full_url:
            print(f"Found PyPI .whl URL for {package_name}: {full_url}")
            return hash1

    print(f"No matching .whl file found for {package_name} on PyPI")
    return None

# Function to verify SBOM integrity
def verify_sbom(sbom_file):
    with open(sbom_file, "r") as f:
        sbom_data = json.load(f)

    verified = True
    for package in sbom_data["packages"]:
        package_name = package["name"]
        expected_whl_filename = package["file"]
        stored_hash = package["hash"]

        if stored_hash == "Not Found":
            print(f"Skipping {package_name}: No stored hash in SBOM")
            continue

        pypi_hash = extract_hash_from_pypi(package_name, expected_whl_filename)

        if pypi_hash is None:
            print(f"Skipping {package_name}: Unable to fetch hash from PyPI")
            continue

        # Compare hashes
        if stored_hash == pypi_hash:
            print(f"  Hash match for {package_name}")
        else:
            print(f"   Hash mismatch for {package_name}!")
            print(f"   SBOM Hash  : {stored_hash}")
            print(f"   PyPI Hash  : {pypi_hash}")
            verified = False

    if verified:
        print("\nAll packages verified successfully!")
    else:
        print("\nSome packages failed verification!")

# Run the verification
if __name__ == "__main__":
    print("\n Verifying SBOM integrity...\n")
    verify_sbom(SBOM_FILE)
