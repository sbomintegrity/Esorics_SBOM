# Build the Project
mvn compile

# SBOM Generation
mvn install cyclonedx:makeAggregateBom

# Config
In the pom.xml, junit and cyclonedx maven configs have already been added.
