from flask import *
import speech_recognition as sr 
import pyttsx3 
from joiner import join

r = sr.Recognizer()  
engine = pyttsx3.init()

app = Flask(__name__)

@app.route('/')
def home():
	return send_file('index.html')
@app.route('/voice')
def joinbyvoice():
	id_done=False
	while(1):
		if id_done==False:     
		    try:
		        a=("What is your meeting ID?")
		        engine.say(str(a))
		        engine.runAndWait()
		        with sr.Microphone() as source2: 
		                r.adjust_for_ambient_noise(source2, duration=0.2)
		                while 1:
		                    try:
		                        a=("Waiting for input")
		                        engine.say(str(a))
		                        engine.runAndWait()
		                        audio2 = r.listen(source2)
		                        MyText = r.recognize_google(audio2) 
		                        break
		                    except:
		                        a=("Try again")
		                        engine.say(str(a))
		                        engine.runAndWait()

		                MyText = MyText.lower() 
		      
		                a=("Did you say "+MyText)
		                engine.say(str(a))
		                q=MyText

		                while 1:
		                    try:
		                        audio2 = r.listen(source2)
		                        MyText = r.recognize_google(audio2) 
		                        break
		                    except:
		                        a=("Try again")
		                        engine.say(str(a))
		                        engine.runAndWait()

		                MyText = MyText.lower() 
		      
		                if "yes" in MyText.lower():
		                    meet_id=q
		                    id_done=True
		    except:
		        a=("Try again.")
		        engine.say(str(a))
		        engine.runAndWait()
		else:
			break

	pswd_done=False
	while(1):
		if pswdd_done==False:     
		    try:
		        a=("What is your meeting password?")
		        engine.say(str(a))
		        engine.runAndWait()
		        with sr.Microphone() as source2: 
		                r.adjust_for_ambient_noise(source2, duration=0.2)
		                while 1:
		                    try:
		                        a=("Waiting for input")
		                        engine.say(str(a))
		                        engine.runAndWait()
		                        audio2 = r.listen(source2)
		                        MyText = r.recognize_google(audio2) 
		                        break
		                    except:
		                       a=("Try again")
		                        engine.say(str(a))
		                        engine.runAndWait()


		                MyText = MyText.lower() 
		      
		                a=("Did you say "+MyText)
		                engine.say(str(a))
		                q=MyText

		                while 1:
		                    try:
		                        audio2 = r.listen(source2)
		                        MyText = r.recognize_google(audio2) 
		                        break
		                    except:
		                        a=("Try again")
		                        engine.say(str(a))
		                        engine.runAndWait()

		                MyText = MyText.lower() 
		      
		                if "yes" in MyText.lower():
		                    password=q
		                    pswd_done=True
		    except:
		        a=("Try again.")
		        engine.say(str(a))
		        engine.runAndWait()
		else:
			break
	join(meet_id,password)
	return send_file('joined.html')

if __name__ == '__main__':
    app.run(debug = False)
