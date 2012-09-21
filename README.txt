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

No known bugs.


History:
========

21/09/2012 - Fixed a URL-reading bug.
02/08/2012 - Added !isup functionality and pushed to github