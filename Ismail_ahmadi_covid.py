age = int(input('how old are you? '))



if age < 18 :
   print('You are not old engough') 
else:
   covid_question = input('Are you curretly having covid-19 illness? (y/n)')
   if covid_question == 'y':
        print('You can not take the vaccine')
   elif covid_question == 'n':
        print('You are elibible to take vaccine')
   else:
        print('Wrong input!')
