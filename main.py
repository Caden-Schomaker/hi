import random
def number_game():
  game_on=True
  answer=random.randint(0,100)
  while(game_on == True):
    guess = int(input('ChatterBot3000: What is your guess? '))
    if(guess == answer):
      print('ChatterBot3000: '+ str(answer) + ' is the number I was thinking of! Good Job! ')
      game_on = False
    elif(guess>100):
      print('ChatterBot3000: My number is less than or equal to 100!')
    elif(guess==-1):
      game_on= False
      print('ChatterBot3000: Ok! We can be done! See ya soon! ')
    elif(guess<0 and guess != -1):
       print('ChatterBot3000: My number is greater than or equale to 0')
    elif(guess>answer):
       print('ChatterBot3000: '+ str(guess) + ' is too high!')
    elif(guess<answer):
       print('ChatterBot3000: '+ str(guess) + ' is too low!')
    else:
      print('ChatterBot3000: Please enter a number!')

print('~~~At any point if you are done, type in -1 to end the program~~~')
print('ChatterBot3000: Hi! My name is ChatterBot3000. What is your name? ')
# res = responce
res_one = input('You: ')
if (res_one == '-1'):
  print('ChatterBot3000: See ya soon!')
  quit()
print('ChatterBot3000: Nice to meet you ' + res_one+ '!')
ice_breakers =  ['What is you favorite color?', 'What is you favorite animal?', 'I like coding. Do you like to code? ']
sen_one = random.randint(0,2)
ice_choice = (ice_breakers[sen_one])
print('ChatterBot3000: '+ ice_choice)
res_two = input('You: ')
if (res_two == '-1'):
  print('ChatterBot3000: See ya soon!')
  quit()
#chooses response based on what you said
if(sen_one == 0):
  print('ChatterBot3000: I agree, ' + res_two +' is a very pretty color!')
elif(sen_one == 1):
  print('ChatterBot3000: Wow! That is really cool that you like '+ res_two +'!')
elif(sen_one == 2):
  if(res_two == 'yes'):
    print('ChatterBot3000: It is cool we both like to code! ')
  elif(res_two == 'no'):
    print('ChatterBot3000: That is okay! We can still be freinds! ')
  else:
    print('Cool! ')
print('ChatterBot3000: Ask me a question now! Im still learning, so please only ask me yes or no questions! ')
my_question = input('You: ')
if (my_question == '-1'):
  print('ChatterBot3000: See ya soon!')
  quit()
question_response = random.randint(0,1)
if (question_response == 0):
  print('ChatterBot3000: Yes! ')
else:
  print('ChatterBot3000: No! ')
print('ChatterBot3000: Would you like to play a game? ')

good_response = False
while(good_response == False):
  game_res = input('You: ')
  game_res= game_res.lower()
  if(game_res == 'yes'):
    good_response = True
    print('ChatterBot3000: Cool! Here is how you play...')
    print('ChatterBot3000: I will pick a number between 0 and 100 and you have to guess it! If you give up just type in -1.')
    number_game()
  elif(game_res == 'no'):
    print('ChatterBot3000: Ok! Maybe we can play latter! See ya soon!')
    quit()
  else:
    print('ChatterBot3000: Please say yes or no. ')
again=True
while (again == True):
  play_again = input('ChatterBot3000:Want to play again? ')
  play_again = play_again.lower()
  if (play_again == 'yes'):
    number_game()
    again = False
  elif (play_again =='no'):
    print('ChatterBot3000: See ya soon!')
    quit()
  else:
     print('ChatterBot3000: Please say yes or no. ')
print('ChatterBot3000: It was nice talking with you. See you soon! ')







































