#!/bin/bash
# This script is for local development and is used to download in the app path the necessary chromedriver
# Need to have a google-chrome installed, will automatically fetch the required

version=$(google-chrome --version | awk '{print $3}')
url="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$version/linux64/chromedriver-linux64.zip" # for version < 115
#url="https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip" # for version >= 115

echo "Downloading Chromedriver version $version..."
wget -q $url -O chromedriver.zip
unzip -q chromedriver.zip -d .
[ -d chromedriver-linux64 ] && mv chromedriver-linux64/chromedriver .
rm -rf chromedriver-linux64
rm chromedriver.zip

echo "Chromedriver version $version downloaded and saved to $(pwd)/chromedriver"