#!/usr/bin/env python3


'''
Main script that cleans the instapaper account.

'''

from instapaper import Instapaper as ipaper
import configparser
import logging

logging.basicConfig(filename='instapaper-cleaner.log',level=logging.DEBUG)

#Read in the configuration folder
config = configparser.ConfigParser()
config.read('instapaper-cleaner.cfg')

#Log into instapaper with OAuth and email/password
i = ipaper(config['Instapaper OAuth']['ID'], config['Instapaper OAuth']['Secret'])
i.login(config['Instapaper Login']['email'], config['Instapaper Login']['password'])

#Get Max URL Count from config file
maxURLCount = int(config['DEFAULT']['MaxURLCount'])

#Get list of unread bookmarks
marks = i.bookmarks(limit=100)

#Read file of target URLs to clean
targetURLs = open('targetURLs.txt', 'r')

url_counter= {}

for url in targetURLs:
    url_counter[url.strip()]=0
targetURLs.close()

for article in marks:
    for target in url_counter.keys():
        if article.url.startswith(target):
            url_counter[target] += 1
            if url_counter[target] > maxURLCount:
                
                #delete this bookmark
                logging.info('Deleting article "'+article.title+'" with url '+article.url+'.')
                article.delete()

     
                    
for target in url_counter.keys():
    summary_string = ''
    if url_counter[target] > maxURLCount:
        summary_string= (str(url_counter[target]-maxURLCount) + ' articles deleted with url "'+target+'".')
    else:
        summary_string= '0 articles deleted with url "'+target+'".'
        
    logging.info(summary_string)
    print(summary_string)
    

