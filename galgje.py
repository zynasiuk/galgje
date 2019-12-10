import random
import string
alfa = string.ascii_uppercase
vijf_te_raden_worden = ['green', 'red', 'pink', 'blue', 'white']
kansen = 5
invoer = ""
guessing_word=[]
list_of_tries=[]
geraden = 0
play = True
double_letter = 0

while len(vijf_te_raden_worden) > 0 and play == True:
    te_raden = random.choice(vijf_te_raden_worden)
    woord = te_raden.upper()

    for i in woord:
        i = "_"
        guessing_word.append(i)

    guessing_word_str = ''.join([str(element) for element in guessing_word])
    print(woord)

    print("I'm thinking about some color, it's... Try to guess name of it! Try with 1 letter.")

    while woord != guessing_word_str and kansen > 0:
        print("You have " +str(kansen)+ " tries. " + guessing_word_str)
        invoer = (input("Which color it could be? ")).upper()

        if len(invoer) == 1:
            if invoer in alfa:
                for i in range(len(woord)):
                    if woord[i] == invoer:
                        guessing_word[i] = invoer
                        kansen += 1
                        double_letter = guessing_word.count(invoer)
                        #print(double_letter)
                        if double_letter > 1:
                            kansen -= 1;


                kansen -= 1
                guessing_word_str = ''.join([str(element) for element in guessing_word])
                list_of_tries.append(invoer)
                print("You did try already: " + str(list_of_tries) + " times.")
            else:
                print("not a letter")
        else:
            print("ONLY 1 LETTER!")

    if guessing_word_str == woord :
        print("Yes, it is "+ guessing_word_str +"! Congrats!")
        geraden += 1
        vijf_te_raden_worden.remove(te_raden)
        guessing_word.clear()
        list_of_tries.clear()
        if len(vijf_te_raden_worden) > 0:
            new_game=(input("One more time? Press any key for yes / N for no: ")).upper()
            if new_game == "N":
                play == False
                break


    else:
        print("Sorry, you lost!")
        play = False

if len(vijf_te_raden_worden) == 0:
    print("Yaaaayyyyyy! You won " + str(geraden) + " times ! ! ! You are THE WINNER!!!")
