#! /usr/local/bin/python

# Import libraries
import irclib
import urllib2
import string
import sys
import re
from lxml import etree
import StringIO

network = 'YOUR.NETWORK.HERE'
port = 6667
channel = '#channel'
nick = 'URLBot'
name = 'URLBot'
owner = 'user'
apiurl = "http://tinyurl.com/api-create.php?url="
isupurl = "http://www.isup.me/"
testlen = 95

irc = irclib.IRC()
s = irc.server()
s.connect(network, port, nick, ircname=name)
s.join(channel)

def handleTiny(connection, event):
	if event.arguments()[0].lower().find('http') == 0:
		line = event.arguments()[0]
		if len(line) > testlen:
			u = re.match(r'https?:\/\/([\w.]+\/?)\S*', line, re.M|re.I)
			url = u.group()
			tinyurl = urllib2.urlopen(apiurl + url).read()
			s.privmsg(channel, tinyurl)
			
def handleIsUp(connection, event):
  if event.arguments()[0].lower().find('!isup') == 0:
		try:
			line = string.split(event.arguments()[0])
			data = isupurl + line[1]
			htmldata = urllib2.urlopen(data)
			html = htmldata.read()
			
			parser = etree.HTMLParser()
			tree = etree.parse(StringIO.StringIO(html), parser)
			
			xpath = '//*[@id="container"]/text()'
						
			pre_result1 = ' '.join(tree.xpath(xpath))
			pre_result = pre_result1.strip()
			
			decode_pre_result = pre_result.decode('string_escape')
			
			if pre_result.find('!') < 0:
				result = "It's just you. " + line[1] + " appears to be up."
			else:
				result = "It's not just you! " + line[1] + " looks down from here."
					
			s.privmsg(channel, result)
			
		except:
			pass
			
irc.add_global_handler('pubmsg', handleTiny)
irc.add_global_handler('pubmsg', handleIsUp)
		
irc.process_forever()