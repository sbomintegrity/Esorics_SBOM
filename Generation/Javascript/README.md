npm init -y \
npm install express bcryptjs jsonwebtoken 


npm install
node index.js

# SBOM Installation and Generation
https://www.npmjs.com/package/@cyclonedx/cyclonedx-npm \
npm install --global @cyclonedx/cyclonedx-npm \
cyclonedx-npm --package-lock-only > sbom.json
