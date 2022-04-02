import requests
r = requests.get("https://www.google.com")
r.status_code
r.headers
r.text
r=request.get("https://opentdb.com/api.php?amount=10")
r.status_code
r.text
type(r.text)
import json
question = json.loads(r.text)
type(question)
import pprint
pprint.pprint(question)
question['results'][0]['category']
question['results'][0]['incorrect_answer']
person = {'Name':'John','Age':30}
person_json = json.dumps(person)
type(person_json)

import pprint
import random
import html
import json
score_correct = 0
score_incorrect = 0
url = "https://opentdb.com/api.php?amount=10"
endGame= ""
while endGame != "quit":
	r = requests.get(url)
	if (r.status_code != 200):
		endGame = input("Sorry, there was a problem retriveing")
	else:
		valid_answer = False
		answer_number = 1 
		data = json.loads(r.text)
		question - data['results'][0]['question']
		answers = data['results'][0]['incorrect_answer']
		correct_answers = data['results'][0]['correct_answer']
		answers.append(correct_answer)
		random.shuffle(answers)
		print(html.unescape(question) + "\n")
		for answer in answers:
			print(str(answer_number) + "" + html.unescape(answer))
			answer_number += 1 
        while valid_answer == False:
        	user_answer = input("\n Type the number of of correct")
        	try:
        		user_answer = int(user_answer)
        		if user_answer > len(answers) or user_answer <=0:
        			print("Invalid Answer")
        		else:
        			valid_enter = True
        	except:
        		print("Invalid answer. Use only numbers")
		user_answer = input("\n type the number of correct")
		user_answer = answers[int(user_answer)-1]
		if user_answer == correct_answer:
			print("\n congrats!")
			score_correct += 1 
		else:
			print("Sorry," + html.unescape(user_answer)+ "is incorrect")
            score_incorrect += 1  		
        endGame = input("\nPress enter to play again or type quit")
print("\n Thanks for playing")