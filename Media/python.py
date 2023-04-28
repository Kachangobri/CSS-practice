# secure_password = "Badmus"
# password = input("Please insert password")

# trial = 0
# while (trial < 3) and (password != secure_password):
#        print("Error re-put password")
#        trial += 1
#        password = input("Enter password again")
# else:
#     if trial >= 3:
#           print("Too many password attemps! phone locked.")
#           exit()
#     else:
#           print("Phone unlucked!")



print("Welcome to my quiz game")
playing = input("Do you wanna play?")
if playing == "yes":
    print("Let's start the game")
elif playing != "yes":
    quit()

score = 0

q1 = input("What does CPU stands for?")
if q1 == ("central processing unit"):
    print("Congratulation! you are correct")

score += 1

else :
    print("You failed! it's incorrect.")

q1 = input("What does UPS stands for?")
if q1 == ("undistricted power supply"):
print("Congratulation! you aer correct")
score += 1
else :
print("You failed! it's incorrect.")

q1 = input("What does IP stands for?")
if q1 == ("internet protocols"):
print("Congratulation! you aer correct")
score += 1
else :
print("You failed! it's incorrect.")

q1 = input("What does WIFI stands for?")
if q1 == ("wireless fidelity"):
print("Congratulation! you aer correct")
score += 1
else :
print("You failed! it's incorrect.")

print("You got " + str(score) + "questions correct")
print("average " str(score / 3) * 100) + "%"








              
