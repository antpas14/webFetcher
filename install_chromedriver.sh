#!/bin/bash
# This script is for local development and is used to download in the app path the necessary chromedriver

version=$(cat chromedriver_version.txt)
url="https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip"

echo "Downloading Chromedriver version $version..."
wget -q $url -O chromedriver.zip
unzip -q chromedriver.zip -d .
rm chromedriver.zip

echo "Chromedriver version $version downloaded and saved to $(pwd)/chromedriver"