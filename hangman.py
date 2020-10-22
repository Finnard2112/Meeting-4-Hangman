
answer = input("what's the word")
answer_list = list(answer) #list version of the original word
presentation = []
for i in range(len(answer_list)):
    presentation.append("_") #makes a list that shows the progress of the player during the game

incorrect = 0 #number of allowed guesses
completion = False # condition for end game
while completion == False:
    attempt = input('guess')
    ind = 0 #index of the guess that appears in answer_list
    count = 0 #number of occurences of the guess in answer_list
    for x in answer_list: #searches for all occurences of the guess in answer_list and change presentation accordingly
        if x == attempt:
            num = answer_list.index(attempt)
            presentation[num] = attempt
            answer_list[num] = 0 #if there is an occurence, replace that occurence with 0 in answer_list
            count += 1
    if count>0:
        print ("Your guess is correct, there was/were {} matches in the word".format(count))
        print(presentation)
    elif count == 0:
        incorrect += 1

    if incorrect == 5:
        print("You lost")
        break
    
    if any(answer_list) == False: #since all 0 have a negative truthy value, we can use any() to check if any element has a truthy value 
        print("Congrats, you got everything correct")
        completion = True
        break

