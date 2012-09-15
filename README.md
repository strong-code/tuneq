#TuneQ
##A social song queue

##What is it?
TuneQ is a web application that utilizes the Twilio and Youtube API to create a playlist of tracks. Users can add to the playlist queue by texting the appropriate Twilio number.

##How do I use it?
###You will need:
	* A Heroku account
	* A Twilio account and number
* Clone this repo
* Edit config.py as such:
	'''python
	SERVER_NUMBER = 'your Twilio phone number'
	SID = 'your Twilio SID'
	TOKEN = 'your Twilio auth token'
	'''
* Deploy to heroku (or your own server)
* Point your SMS Request URL for your Twilio phone number to the URL of your hosted app
* Now you can text your Twilio number to add tracks to the queue!
	* Use the syntax 'Add [Song Keyword]'. This uses fuzzy string matching, so you can enter a keyword ('Add Rolling Stone'), the track name ('Add Like A Rolling Stone'), or track name and artist name('Add Like A Rolling Stone Bob Dylan'). The more info, the more likely you are to get the correct track.

###[Click here to see a live demo!](http://tuneq.herokuapp.com)