import random

def game(comp, opponent):
    if comp == opponent:
        return None
    elif comp == 'r': 
        if  opponent == 'p':
            return True
        elif opponent == 's':
            return False
    elif comp == 'p': 
        if  opponent == 's':
            return True
        elif  opponent== 'r':
            return False
    elif comp == 's': 
        if  opponent == 'r':
            return True
        elif opponent == 'p':
            return False          
print("comp turn : Rock(r) paper(p) scissor(s)")
computer_s_choice = random.randint(1, 3)
if computer_s_choice == 1:
    comp = 'r'
elif computer_s_choice == 2:
    comp  =  'p'
elif computer_s_choice == 3:
    comp  = 's'

opponent = input("Enter r = Rock!, s = scissor! 0, p = paper!  :")
if opponent == ("r"):
    pass
elif opponent == ("s"):
    pass
elif opponent == ("p"):
    pass
else:
    print("you entered the  wrong word or uppercase letter please  check it once:")

a = game(comp, opponent )

print(f"computer chosses {comp}")
print(f"you chosse {opponent}")

if a == None:
    print("This game is Tie because your brain and computer's brain are compratively equaly sharp: ")
elif a == True:
    print("heyy Boss.... you are amazing  you defeat the computer :")
elif a == False:
    print("Better luck next time dear....")      
