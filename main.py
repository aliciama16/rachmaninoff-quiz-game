# Python quiz game

questions = ("In addition to being a composer, Rachmaninoff was also a virtuoso performer on which instrument",
             "Rachmaninoff's Symphony No. 2 is the greatest symphony ever written. In which year was it composed?",
             "He is considered one of the last ____ composers",
             "Rachmaninoff's last major composition was a symphonic work inspired by a poem by Edgar Allan Poe. What is the title of this composition?",
             "Rachmaninoff left Russia after the Russian Revolution in 1917. In which country did he spend the later years of his life?")

options = (("A. Violin", "B. Piano", "C. Flute", "D. Cello"),
          ("A. 1898", "B. 1911", "C. 1899", "D. 1907"),
          ("A. Baroque", "B. Classical", "C. Romantic", "D. Pre-Modern"),
          ("A. The Bells", "B. The Isle of the Dead", "C. Symphony No. 3", "D. Symphonic Dances"),
          ("A. Germany", "B. United States", "C. France", "D. United Kingdom"))

answers = ("B", "D", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---")
    print (question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1 

print ("-------------")
print ("   RESULTS   ")
print ("-------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions) * 100)
print(f"Your score is: {score}%")