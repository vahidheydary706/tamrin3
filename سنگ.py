import random

itens = ["Rock","Paper","Scissor"]

camputar_score = 0
user_score = 0

camputar_choice = random.choice(itens)

print("0_ Rock")
print("1_ Paper")
print("2_ Scissor")
print("3_ Exit")

user_choice_index = int(input())
user_choice = itens [user_choice_index]

if camputar_choice =="Rock" and user_choice =="Scissor":
    print("camputar wins")
    camputar_score += 1

elif camputar_choice =="Rock" and user_choice =="Paper":
    print("user wins")
    user_score += 1

elif camputar_choice =="Rock" and user_choice =="Rock":
    print("Equal")

elif camputar_choice =="Paper" and user_choice =="Scissor":
    print("camputar wins")
    user_score += 1

elif camputar_choice =="Paper" and user_choice =="Rock":
    print("camputar wins")
    camputar_score += 1

elif camputar_choice =="Paper" and user_choice =="Paper":
    print("Equal")

elif camputar_choice =="Scissor" and user_choice =="Rock":
    print("camputar wins")
    user_score += 1

elif camputar_choice =="Scissor" and user_choice =="Paper":
    print("camputar wins")
    camputar_score += 1
elif camputar_choice =="Scissor" and user_choice =="Scissor":
    print("Equal")