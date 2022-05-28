from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import tweepy
from dotenv import load_dotenv
import os


# Load env vars
load_dotenv()
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEAR_TOKEN = os.getenv("BEAR_TOKEN")


# Setup chrome driver
def create_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    return driver


# Setup Twitter API
def setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


api = setup()
userID = "wordleanswerguy"
tweets = api.user_timeline(screen_name=userID, count=3, include_rts=False, exclude_replies=True)
# for tweet in tweets:
#     print(tweet.text)
#     print("-------------------------")

for tweet in tweets:
    tweet = tweet.text
    tweet = tweet.replace('\n', ' ')
    if not tweet.startswith("Today’s #Wordle answer is"):
        continue
    print(tweet)
    break

first = tweets[0].text
first = first.replace('\n', ' ')
words = first.split(" ")
words = list(filter(lambda x: len(x) == 5, words))
print(words)



# driver.get("https://www.nytimes.com/games/wordle/index.html")
# page = driver.find_element(By.TAG_NAME, "body")
# page.click()
# page.send_keys("soare")
# page.send_keys(Keys.RETURN)
