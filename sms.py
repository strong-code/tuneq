'''
Handle the sms portions of the ap
'''
from twilio.rest import TwilioRestClient
import twilio.twiml
from bs4 import BeautifulSoup
import urllib2, re

URLqueue = []

def replyToSMS(from_number, from_contents, queueLength):

	#(Boolean, Sing Title, URL Link) tuple
	trackInfo = findTrack(from_contents)

	resp = twilio.twiml.Response()

	if trackInfo[0] == True:
		URLqueue.append(trackInfo[2])
		print '>>> added ' + str(trackInfo[2]) + ' to queue'
		resp.sms(str(trackInfo[1] + ' has been added to the queue! You are ' + str(queueLength + 1) + ' in the queue'))
	else:
		resp.sms('Couldn\'t find that track. Did you spell it correctly?')

	return str(resp)

def findTrack(from_contents):
	#by default, this will search only in the Music category and return a single result (ordered by relevance to search query)
	#This can be changed to your liking as per Youtube's API available at:
	#https://developers.google.com/youtube/2.0/developers_guide_protocol#Retrieving_and_searching_for_videos

	msg = from_contents.split()

	if msg[0] == 'add':
		track = ' '.join(msg[1:])

	queryURL = "https://gdata.youtube.com/feeds/api/videos?q=%s&category=music&orderby=relevance&max-results=1&v2" % track.replace(' ', '%20')

	try:
		XMLresponse = urllib2.urlopen(queryURL)
		soup = BeautifulSoup(XMLresponse.read())
		ytcode = soup.entry.link['href'].split('v=')
		trailing = re.sub('&.*$', '?autoplay=1', ytcode[1])
		link = 'http://www.youtube.com/embed/%s' % trailing
		title = soup.entry.title.string
		return (True, title, link)
	except:
		return (False, None, None)