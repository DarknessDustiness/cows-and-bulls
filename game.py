import random

number_of_times_played=0
#rangome nubmber generator (4 digit number) as a string

def random_number_generator(x):
    numbers=[0,1,2,3,4,5,6,7,8,9]
    result=""
    for i in range(x):
        y=random.choice(numbers)
        numbers.remove(y)
        result+=str(y)
    return result

def moo_or_boo(guess, answer):
    bull=0  
    cow=0
    for i in range(len(guess)):
        if guess[i]==answer[i]:
            bull+=1
        elif guess[i] in answer:
            cow+=1
    return cow,bull

def difficulty():
    trys=0
    length=0
    y=input('Set Difficulty level: E(easy), M(medium), H(hard)').lower()
    if y == 'e':
        trys,length=12,3
    elif y == 'm':
        trys,length=10,4
    elif y == "h":
        trys,length=8,5
    else:
        print("invalid input, try again")
        trys,length=difficulty()
    return trys, length

def take_guess(length):
    guess=str(input('Plese enter your guess: '))
    if not guess.isdigit() or len(guess)!=length or len(set(guess))!=length :
        print('Guess invalid, please try again!')
        return take_guess(length)
    return guess

def play_game():
    if number_of_times_played==0:  
        play=str(input('Do You want to play a game?(y/n)')).lower()
    else:
        play=input('Play again?(y/n)')
    if play  not in ['y','n']:
        print('Guess invalid, please try again!')
        return play_game()
    else:
        if play == 'y':
            return 1
        else:
            return 0

def game():
    print("**********   COWS AND BULLS   **********")
    print("This is a number guessing game. A number will be generated and you will be given tried and a number length based on difficulty")
    print("- Easy-3 digit number, 12 tries \n- Medium - 4 digit number, 10 tries \n- Hard - 5 digit number, 8 tries")
    print("You have to guess the number in alloted tried")
    print('Number generated will have unique (non repeating) digits')
    print('based on your input guess, you will be told how many cows and bulls you got')
    print('bull corresponds to getting the right number on the right place,\nwhile cow corresponds to a correct number but on the wrong place')
    trys,length=difficulty()
    answer=random_number_generator(length)
    won=False
    for i in range(trys):
        print('This is attempt ', i+1)
        print(trys-i, ' tries remain')
        guess=take_guess(length)
        cow,bull=moo_or_boo(guess=guess,answer=answer)
        print('You got', cow,'cows and ',bull,'bulls')
        if guess==answer:
            print('congrats, you won the game')
            won=True
            break
        else:
            print('onto the next guess!!')
    if won:
        print('You are a genius, you beat the game!')
    else:
        print('You lost. Btter luck next time!!!!!!!!!!')
        print("the answer was ", answer)


while play_game():
    game()
    number_of_times_played+=1