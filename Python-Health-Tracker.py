steps = 0 #Declaring the steps variable, then prompting the user to input their starting steps.

steps = int(input("Enter starting number of steps:"))


while steps < 10: #Enter a while loop to check if the user has met their minimum.
    more_steps = int(input('Take more steps! How many steps would you like to add?'))
    steps = steps + more_steps

print ("You've taken enough steps for today!") #The user exits the loop and their total steps are printed.
print ("Total steps taken:", steps)

water = 0 #Declaring the water variable, then prompting the user to enter their starting water.

water = int(input("Now, we need to track your water. How many glasses have you had today?"))

while water < 8: #Enter a while loop to check if the user has met their minimum.
    more_water = int (input("You need to drink more water. How many glasses would you like to add?"))
    water = water + more_water

print ("You've had enough water AND enough steps today. Well done!") #Exit the while loop and print daily totals for steps and water.
print ("Here are your totals for today:")
print ("Steps:", " ", steps, " ", "Water:", water)

sleep_hours = 0 #Declaring the sleep_hours variable, then prompting the user to enter their total sleep.

sleep_hours =  float(input("Finally, let's track your sleep. How many hours did you sleep last night?"))

if sleep_hours > 7: #If/else to determine if the user has slept over 7 hours.
    print("Great job. Sleeping is important!")

else:
    print ("Tonight, try to focus on getting more sleep! Aim for 8 hours or more.")

grand_total_data = input("Would you like your daily health report? (Enter yes or no)").lower() #Yes/No to determine if the user wants their total stats.

if grand_total_data == "yes": #If yes, print stats.
    print("\n--- DAILY HEALTH REPORT ---")
    print ("Steps:", " ", steps, " ", "Water:", water, "and", sleep_hours, "Of Sleep. Bravo!")

else: #If no, exit the program.
    print("No problem, have a great day!")