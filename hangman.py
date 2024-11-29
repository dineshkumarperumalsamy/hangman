import random 
guess_words_lists=["apple","orange","yellow","car"]
gw=random.choice(guess_words_lists)
temp=[]
count_l=len(gw)
for i in range(0,count_l,1):
    temp.append("-")

def input_single_char(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1:
            return user_input
        else:
            print("Please enter only one character.")

def checkword(iw):
    if iw in gw:
        for idx, char in enumerate(gw):
            if char == iw:
                temp[idx] = iw
    print(" ".join(temp))

while "-" in temp:
    print(f"\nCurrent word: {' '.join(temp)}")
    iw = input_single_char(f"Guess a letter for the {len(gw)}-letter word: ")
    checkword(iw)

print(f"\nCongratulations! You've guessed the word: {gw}")
