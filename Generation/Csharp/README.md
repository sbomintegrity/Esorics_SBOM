# Dotnet Installation on Ubuntu
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
sudo dpkg -i packages-microsoft-prod.deb \
rm packages-microsoft-prod.deb \
sudo apt update \
sudo apt install dotnet-sdk-8.0 -y \
dotnet --version

# Create an Application
dotnet new console -o HelloDotNet \
cd HelloDotNet

# Add a Sample Dependency
dotnet add package Newtonsoft.Json

# Build and Run your updated application
dotnet build \
dotnet run

# Install Cyclonedx Dotnet and Generate SBOM
https://github.com/CycloneDX/cyclonedx-dotnet \
dotnet tool install --global CycloneDX \
dotnet-CycloneDX \
dotnet-CycloneDX HelloDotNet.csproj \
You should give the csproj path as an argument
