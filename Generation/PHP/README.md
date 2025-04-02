## Install PHP
sudo apt install php8.1-cli \
sudo apt install php8.1-xml

## Install Composer
https://getcomposer.org/download/

## Install Dependencies
composer install

## Run the application
php -S localhost:8000 \
http://localhost:8000/

## SBOM Generation
https://github.com/CycloneDX/cyclonedx-php-composer \
composer require --dev cyclonedx/cyclonedx-php-composer \
composer cyclonedx:make-sbom

