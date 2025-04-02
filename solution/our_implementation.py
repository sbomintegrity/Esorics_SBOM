import os
import hashlib
import json
import re

# Define the directory where .whl files are located
WHL_DIRECTORY = "./wheels"  # Change this to your actual directory

# Function to parse requirements.txt
def parse_requirements(requirements_file="requirements.txt"):
    packages = []
    with open(requirements_file, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):  # Ignore comments and empty lines
                if "==" in line:  # Extract name and version
                    name, version = line.split("==")
                else:
                    name, version = line, "latest"
                packages.append({"name": name, "version": version})
    return packages

# Function to compute SHA-256 hash of a file
def compute_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    print(f"The hash is {hasher.hexdigest()}")        
    return hasher.hexdigest()

# Function to find and hash .whl files
def find_whl_files(directory):
    whl_hashes = {}
    for file in os.listdir(directory):
        if file.endswith(".whl"):
            filepath = os.path.join(directory, file)
            whl_hashes[file] = compute_hash(filepath)
    print(f"whl hashes are {whl_hashes}")
    return whl_hashes

# Function to generate SBOM
def generate_sbom(requirements, whl_hashes, output_file="sbom.json"):
    sbom = {
        "metadata": {
            "tool": "Custom Python SBOM Generator",
            "format": "JSON",
        },
        "packages": []
    }

    for package in requirements:
        package_name = package["name"]
        package_version = package["version"]

        # 🛠 Find the closest matching .whl file
        matching_whl = None
        for whl_file in whl_hashes.keys():
            if re.match(rf"^{package_name}-{package_version}.*\.whl$", whl_file):
                matching_whl = whl_file
                break

        package_entry = {
            "name": package_name,
            "version": package_version,
            "file": matching_whl if matching_whl else f"{package_name}-{package_version}.whl",
            "hash": whl_hashes.get(matching_whl, "Not Found"),
        }

        sbom["packages"].append(package_entry)

    # Save SBOM to a file
    with open(output_file, "w") as f:
        json.dump(sbom, f, indent=4)

    print(f"SBOM saved to {output_file}")

# Main execution
if __name__ == "__main__":
    print("Parsing requirements.txt...")
    requirements = parse_requirements()

    print("Searching for .whl files...")
    whl_hashes = find_whl_files(WHL_DIRECTORY)

    print("Generating SBOM...")
    generate_sbom(requirements, whl_hashes)

    print("SBOM generation completed!")
