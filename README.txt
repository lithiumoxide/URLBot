URLBot
Conor Farrell
======

An IRC bot written in Python to shorten URLs and to check whether a domain is up or not.


Usage:
======

Initial setup:
- Change the IRC server, port, channel name, nick, and owner as appropriate. To run, enter 'python urlbot.py' at the command line.

In channel:
- Tinyurl function is automatically triggered once it finds a string starting with http or https.
- '!isup <url>' will contact isup.me to test the URL given, and return the appropriate response.


Known bugs:
===========

The TinyURL bit reads in the entire line. So, a user might have a short URL with added text after, such that the full line is over testlen, even if the url is less. This triggers the function and returns a tinyurl. This should be fixed with a split, and finding the resulting list entry with a URL in it. This will be the next update.


History:
========

02/08/2012 - Added !isup functionality and pushed to github