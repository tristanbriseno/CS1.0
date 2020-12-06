from random import choice
def get_translation(user_response):
  
  Monday = ["lunes"]

  Tuesday = ["martes"]
 
  Thursday = ["jueves"]

  if user_response == "Monday" :
    return choice(Monday)
  if user_response == "Tuesday" :
    return choice(Tuesday)
  if user_response == "Thursday" :
    return choice(Thursday)
  else:
    return "I don't recognize that word."

print(" I can say Monday, Tuesday and Thursday in spanish.")

user_response = ""

while True:
  user_response = input(" What day do you want me to say in spanish?: ")

  if user_response == "done":
    break
 
  translation_result = get_translation(user_response)
  print(translation_result)
