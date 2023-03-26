# Web Fetcher
This is a web scraper app built with Python and Flask. It scrapes data from a website using Selenium and displays the results on a web page.

### Installation

To run this app, you need to have Docker installed on your system. Clone this repository and run the following command:

```commandline
docker build -t web-fetcher .
```
This will build a Docker image for the app. Once the image is built, run the following command to start the app:

```commandline
 docker run -p 5000:5000 --dns 8.8.8.8 --name web-scraper  webfetcher:latest
```
This will start the app on port 5000. You can then access the app by navigating to http://localhost:5000 in your web browser.

### Usage
Once the app is running, you can enter the URL of the website you want to scrape in the url field in the request 

```commandline
curl --location --request POST 'localhost:5000/retrieve' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url" : "https://www.google.com"
}
```