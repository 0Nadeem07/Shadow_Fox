import random 
from hangman import stages
from words import word_list

# initial values
lives = 6
isOver =False 

word = random.choice(word_list) 
print(word)
progStr = " "


# progress
progress = []
for i in range(len(word)):
    progress.append('_')


# intial display
print(stages[lives])
print(progStr.join(progress))




# user logic

while(not isOver):
    user_guess = input("Guess a letter: ")
    print('\n')
# check if letter is already used
    if(user_guess in progress):
         print("Already guessed! ")
         pass
# if guessed word it correct update progress
    for i in range(len(word)):
        if(word[i]==user_guess):
            progress[i]=user_guess

# if guessed word is not correct reduce a life
    if(user_guess not in progress):
            lives-=1   
            print(f"Incorrect! || {lives} left")

    
    print(progStr.join(progress))
    print(stages[lives])


# winning condition
    if('_' not in progress):
         print("You Won!!") 
         isOver =True
                
    
# losing condition
    if(lives == 0):
        print("You Lost!!")
        isOver = True
        # break
        

