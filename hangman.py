from words import *
import random

#take valid word from user 

def difficulty():
    level= input("Difficulty level: [E/M/H] : ").upper()
    if level == "E":
        return easy_words
    elif level== "M" :
        return medium_words
    elif level =="H":
        return hard_words
    else:
        return word_list

def letter_position(letter, word):
    for index , lett  in enumerate(word):
        if letter ==lett :
            return index 
    
    
def choose_word():
    words = difficulty()
    return random.choice(words)

def is_gameover(word, attempts):
    if set(word) == attempts:
        return True


    

def play():
    word = choose_word()
    attemps= 5 
    guessed_letters= set()

    while attemps >0:  
        
          
        for ch in word: 
            if ch in guessed_letters:
                print(ch, end=" ")
            else:
                print("_", end=" ")
        
        if is_gameover(word, guessed_letters) :
            print(f"\n You won ")
            break    
             

        letter=input(f"\nEnter letter [Attemps remaining {attemps}]: ")
        if letter in word:
            guessed_letters.add(letter)
            
        if letter not in word:
            attemps-=1
         
    if attemps<=0 :
        print(f"\n\n!!!...Game Over...!!!\nCorrect word was : {word}\nTry again!!!")         

        
def main():
    play()


if __name__== "__main__":
    main()
    