import random

# groceryList = ['Frsoted Flakes', 'Tangerines', 'Nutella', 'String Cheese', 'Green Beans', 'Rice Cakes']

# for myFavorite in groceryList:
#     print 'My least favorite groceries are ' + myFavorite
#
# for index in range(len(groceryList)):
#     print index
#

# guess = int(raw_input('Enter a number between 1 and 100 >:) \n(quit to exit)\n'))
numGuess = 0
random_num = random.randint(0, 101)
maxGuesses = 10
print random_num

while numGuess < 10:
    guess = int(raw_input('Enter a number between 1 and 100 \n(quit to exit)\n'))
    if guess > random_num:
        print 'too high, guess lower'
    elif guess == random_num:
        print 'You are right'
        quit()
    else:
        print 'too low, guess higher!'
    # guess = int(raw_input('Enter a number between 1 and 100 >:) \n(quit to exit)\n'))
    numGuess +=1

if numGuess == maxGuesses:
    print 'you lose'
    quit()




    # else:


# while random_num > 0:
#     print 'Isaac ',
#     random_num = random_num - 1


# print random_num



# anotherList = 'wow this is scary'
# for i in anotherList:
#     print i

# random_num = random.randint(0, 99)
# print random_num



#
# randomly gen number
# use raw input to generate guesses from user
# use conditionals and loops to make it
#
# user keeps guessing a number until they match a genreated number
