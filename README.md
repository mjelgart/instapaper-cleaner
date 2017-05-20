Instapaper-Cleaner
==================

Cleans out old unread instapaper articles from same website.

Installation
------------

From source: 

    $ git clone https://github.com/mjelgart/instapaper-cleaner.git
    $ cd instapaper-cleaner
    $ python setup.py install

Configuration 
-------------

Rename "cleaner-example.cfg" to "instapaper-cleaner.cfg".
Fill out that configuration file with the indicated values, including the number of articles you'd like to keep from the target websites.

Then rename "targetURLs-example.txt" to "targetURLs.txt"
Fill out a targetURLs.txt with the URLs you want to clean, based on the examples provided.
Copy and paste them with or without the "https://" or "http://", it will not matter. 

Usage
-----
To run the tool: 

    $ python cleaner.py

A message will appear indicating how many articles were deleted if any. 

A more detailed log will appear entitled instapaper-cleaner.log

Written in Python 3.5.
