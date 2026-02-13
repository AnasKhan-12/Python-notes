import random

choices=('r','s','p')
userchoice=input("Enter choice (r/p/s): ").lower()
compchoice= random.choice(choices)

while userchoice not in choices:
    print("enter a valid choice")
    userchoice=input("Enter choice (r/p/s): ").lower()

print(f'User chose {userchoice}')
print(f'Computer chose {compchoice}')

if userchoice == compchoice:
    print ("Its a tie")
elif ((userchoice == 'r' and compchoice == 's') or
      (userchoice == 's' and compchoice == 'p') or
      (userchoice == 'p' and compchoice == 'r')):
    print("User win ")
else:
    print("you lose")