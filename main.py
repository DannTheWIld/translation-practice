import streamlit as st
import sys

# ANSI color codes
BLACK = "\033[30m"  # Correct letters
RED = "\033[31m"  # Incorrect letters
GREEN = "\033[32m"  # Missing letters
RESET = "\033[0m"  # Reset to default color

points = 0  # Initialize points

theEWord = ["Acquire", "Amateur", "Argument", "Faith", "Calendar", "Category", "Cemetery", "Changeable", "Collectibles", "Column", "Commitment", "Conscience", "Conscious", "Definite", "Discipline", "Solid", "Equipment", "Exaggerate", "Excellent", "Existence", "Experience", "Foreign", "Friend", "Grammar", "Harass", "Height", "Independence", "Indispensable", "Intelligence", "Jewelry", "Review", "Knowledge", "Contact", "License", "Maintenance", "Maneuver", "Millennium", "Misspelling", "Necessary", "Noticeable", "Occasion", "Preferred", "Endurance", "Privilege", "Public", "Receive", "Recommend"]
theSWord = ["Få", "Amatör", "Argument", "Tro", "Kalender", "Kategori", "Kyrkogård", "Föränderlig", "Samlarobjekt", "Kolumn", "Engagemang", "Samvete", "Medveten", "Definitivt", "Disciplin", "Gensamt", "Utrustning", "Överdriva", "Utmärkt", "Existens", "Erfarenhet", "Utländsk", "Vän", "Grammatik", "Trakassera", "Höjd", "Oberoende", "Oumbärlig", "Intelligens", "Smycken", "Omdöme", "Kunskap", "Kontakt", "Licens", "Underhåll", "Manöver", "Millennium", "Felstavning", "Nödvändigt", "Märkbart", "Tillfälle", "Föredragen", "Uthållighet", "Privilegium", "Offentligt", "Ta emot", "Rekommendera"]

length = len(theEWord)  # Get the length once, outside the function

Input = input('Length? (1-10) 1 is the långest and 10 is the shortest: ').lower()  # Convert input to lowercase
Input = int(Input)
length = int(length / Input)
print(f"Translate {length} words")  

    

def getWord(num):
    global eWord, sWord  # Declare global so it's accessible outside the function
    eWord = theEWord[num].lower()  # Convert to lowercase
    sWord = theSWord[num]

def highlight_differences(correct, user_input):
    highlighted_text = ""
    max_length = max(len(correct), len(user_input))

    for i in range(max_length):
        if i < len(correct) and i < len(user_input):
            if correct[i] == user_input[i]:  # ✅ Correct letter
                highlighted_text += f"{BLACK}{correct[i]}{RESET}"
            else:  # ❌ Wrong letter
                highlighted_text += f"{RED}{user_input[i]}{RESET}"
        elif i < len(correct):  # 🟩 Missing letter
            highlighted_text += f"{GREEN}{correct[i]}{RESET}"
        elif i < len(user_input):  # Extra letters (also red)
            highlighted_text += f"{RED}{user_input[i]}{RESET}"

    return highlighted_text

def Translate():
    global points  # Declare global so it can be modified inside the function
    Input = input(f'Translate {sWord}: ').lower()  # Convert input to lowercase

    if Input == eWord:  
        points += 1  
        print(f"✅ Good! One point, total: {points}")  
    else:
        print(f"❌ Incorrect! Expected: '{eWord}'")
        print("Your answer:  " + highlight_differences(eWord, Input))

count = 0
while count < length:  # Loops based on the number of words
    getWord(count)  # Pass the current count to select different words
    Translate()
    count += 1  # Increment count

print(f"🎉 Well done! You got {points} points out of {length}")
