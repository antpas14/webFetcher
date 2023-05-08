#!/bin/bash
# This script is for local development and is used to download in the app path the necessary chromedriver
# Need to be passed a version of desired chromedriver. It MUST be the same version of chrome used locally (it must be downloaded again if chrome is updated)

if [ "$#" -ne 1 ]; then
    echo "Need to provide version number of chromedriver to download"
    exit 1
fi

version=$1
url="https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip"

echo "Downloading Chromedriver version $version..."
wget -q $url -O chromedriver.zip
unzip -q -f chromedriver.zip -d .
rm chromedriver.zip

echo "Chromedriver version $version downloaded and saved to $(pwd)/chromedriver"