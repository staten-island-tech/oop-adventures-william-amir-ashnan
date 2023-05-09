import welcome
print('Welcome to the beginning of your journey. Your first opponent will be Doctor Octopus; he has a health level of 125 and attack damage of 15')

answer = input('Are you ready to accept your first challenge?')
if answer == 'yes':
    print('Time to fight!')

else:
     print('You have lost the game')
     exit() 

answer == input('Congrats on defeating Doctor Octopus! Time for the next opponent, Electro, he is slightly harder than Doctor Octopus. He has a health of 150 and attack damage of 20. Are you ready to accept your second challenge?')
if answer == 'yes':
    print('Time to fight!')

else:
     print('You have lost the game')
     exit() 

print('Congrats on defeating Electro! Time for the next opponent, Mysterio, he is slightly harder than Electro. He has a health of 175 and attack damage of 25.')

answer == input('Are you ready to accept your third challenge?')
if answer == 'yes':
    print('Time to fight!')

else:
     print('You have lost the game')
     exit() 
