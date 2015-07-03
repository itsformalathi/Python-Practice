#Extract a Review from Flipkart.com and Analyse the Sentiment using Alchemy API
#About alchemy api -  http://www.alchemyapi.com/products/alchemylanguage/sentiment-analysis

import requests, pickle
from bs4 import BeautifulSoup as BS
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

def GetRequest(url):
    """ send request to the given URL for access """
    return requests.get(url)

def GetReview(resp):
    """ Extract the required review from the given url """
    soup = BS(resp.text)
    review = [soup.find("span", {"class": "review-text-full"})]
    return review

def GetSentiment(review):
    """  Analyze the sentiment of the given Review """
    sentiment = alchemyapi.sentiment("text", review)
    return sentiment

url = "http://www.flipkart.com/apple-iphone-5s/p/itme76pyyanhyzpq?pid=MOBDPP    ZZVUJRG582&cmpid=content_mobile_8965229628_gmc_pla&tgi=sem%2C1%2CG%2C1121400    2%2Cg%2Csearch%2C%2C50314728260%2C1o1%2C%2C%2Cc%2C%2C%2C%2C%2C%2C%2C&gclid=C    Lz60p_h2sUCFQWTjgodmlEAzA"

def main():
    resp = GetRequest(url)
    review = GetReview(resp)
    print(review)
    sentiment = GetSentiment(review)
    print("Sentiment: ", sentiment["docSentiment"]["type"])

main()

