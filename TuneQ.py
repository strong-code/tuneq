from flask import Flask, request, redirect, session
from twilio.rest import TwilioRestClient
import twilio.twiml
import os

SERVER_NUMBER = '14155084527'
SID = 'AC03706901f9c1fe2bda57e15395da6a0d'
TOKEN = '0a1f88c479541c3ff4b1769c5651b964'
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def replyToSMS():

	from_number = request.values.get('From', None)
	from_contents = request.values.get('Body', None)

	if from_contents is not None and from_number is not None:
		resp = twilio.twiml.Response()
		resp.sms('You texted from ' + from_number + 'with the text ' + from_contents)
		return str(resp)
	else:
		return 'You are viewing from a web browser, no text for you!'

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug = True)