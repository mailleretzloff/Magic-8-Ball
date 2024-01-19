#Maille Retzloff
#1/19/2024
#Magic 8 Ball

responses = ["yes definitely", "most likely", "ask again later", "very doubtful", "don't count on it", "my reply is no", "without a doubt", "maybe", "outlook not so good", "yes"]
import random

def magic8ball():
    while True:
        question = input("ask a yes or no question")
        if question.endswith("?"):
            print(random.choice(responses))
            playagain = input("do you want to ask another question? type y for yes and n for no")
            if playagain == "y":
                magic8ball()
            if playagain == "n":
                break
        else:
            print("reenter question and use a ?")
            magic8ball()

magic8ball()

