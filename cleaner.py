from instapaper import Instapaper as ipaper
import configparser

'''
Main script that cleans the instapaper account.

'''

#Read in the configuration folder
config = configparser.ConfigParser()
config.read('instapaper-cleaner.cfg')

#Log into instapaper with OAuth and email/password
i = ipaper(config['Instapaper OAuth']['ID'], config['Instapaper OAuth']['Secret'])
i.login(config['Instapaper Login']['email'], config['Instapaper Login']['password'])

#Get list of unread bookmarks
marks = i.bookmarks(limit=100)

#Read file of target URLs to clean
targetURLs = open('targetURLs.txt', 'r')

url_counter= {}

for url in targetURLs:
    url_counter[url.strip()]=0
targetURLs.close()

for article in marks:
    for target in url_counter.keys:
        if article.url.startswith(target):
            url_counter[target]+=1

            if [url_counter[target]> config['DEFAULT']['MaxURLCount']


