user = input('What is your name? ')
age = int(input('What is your age' + " " + user + '? ')) #input for user name and age
if age >= 18 and age < 65:
    print('Hello', user, 'your ticket will cost $15.')
elif age >= 65:
    print('Hello', user, 'you qualify for the senior discount your ticket will cost $5.')
else:
    print('Sorry', user, 'you are not old enough to see this movie.')
    #Prints if user can go to the movie and what the price of the ticket is


