# Wordle Scraper

## About:
This program scrapes Twitter account [@wordleanswerguy](https://mobile.twitter.com/wordleanswerguy) for the correct Wordle for the day. A bot then automatically inputs the answer in [Wordle](https://www.nytimes.com/games/wordle/index.html) to get it correct on the first try.

## Getting Started:
1. Clone this repository: `git clone git@github.com:ishuagrawal/wordle-scraper.git`
2. Change directory to the repo: `cd wordle-scraper`
3. Install the following packages to your Python3 interpreter. 
    - selenium
    - webdriver-manager
    - dotenv
    - tweepy

4. Obtain the Twitter API Key:
    - [Apply](https://developer.twitter.com/) for a Twitter Developer Account.
    - Create a new project and apply for Elevated access on the Developer Portal.
    - Copy the created project's consumer keys and authentication tokens and store them in their respective environmental variables in `.env_sample`.
5. Run the program.

