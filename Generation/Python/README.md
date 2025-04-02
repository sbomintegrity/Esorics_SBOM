# Installation and Initialization on Ubuntu
mkdir PyCryptoDemo \
cd PyCryptoDemo \
python3 -m venv venv \
source venv/bin/activate \
pip3 install pycryptodome \
pip3 freeze > requirements.txt

# Sbom Tool Installation and Generation
https://github.com/CycloneDX/cyclonedx-python \
cyclonedx-py --help \
cyclonedx-py requirements requirements.txt 


