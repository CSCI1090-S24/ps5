# Richard Obeakemhe.
# 2/19/2023.
# "This code is my own work. I did not share my code or look at the code of another student. I did not consult ChatGPT, CoPilot, or another large language model."

import random

# These are variables where you will store info
# that gets updated on each turn through the while loop.

# Current amount of money, starts at $10.
startmoney = 10

# Day counter to keep track of how many days.
day = 0

# List of lists where you will store the stats for each day:
# number of lemonades made, number of lemondades sold,
# chance of rain that day, whether that day was sunny.
stats = []


# Here is the welcome message explaining how the game works
print("Welcome to the lemonade stand!")
print(f"\nYou have ${startmoney:.2f}")    
print("It costs 50 cents to make a glass of lemonade.")
print("A glass sells for $1.")
print("If it's sunny, you'll sell all the lemondade you make.")
print("If it rains, you won't sell any lemondade.")
print(f"Your goal is to get to $20 in 10 days.")    


while day < 10:
    day += 1
    chance = random.random()
    chance_percent = chance * 100
    print(f"\nToday is day {day}.")
    print(f"You have ${startmoney}.")
    print(f"The chance of rain is {chance_percent:.0f}%.")
    glasses_made = int(input("How many glasses would you like to make today? "))
    
# Ensure the user can afford the number of glasses they want to make
    while glasses_made * 0.5 > startmoney:  # Check if cost of glasses exceeds available money
        print("You don't have enough money to make that many glasses.")  # Notify user of insufficient funds
        glasses_made = int(input("How many glasses would you like to make today? "))  # Prompt user to input valid number of glasses
    
    # Determine if it's sunny or rainy
    random_number = random.random()  # Generate random number between 0 and 1
    if random_number < chance:  # Compare random number with chance of rain
        print("Unfortunately, it rained today. No lemonade was sold.")  # Notify user of rainy weather
        startmoney -= glasses_made * 0.5  # Deduct cost of glasses made from available money
        glasses_sold = 0  # No glasses sold due to rain
    else:
        print("It's sunny today! All lemonade was sold!")  # Notify user of sunny weather
        startmoney += glasses_made * 0.5  # Add revenue from sold glasses to available money
        glasses_sold = glasses_made  # All glasses made are sold
    
    # Update stats for the day
    stats.append([glasses_made, glasses_sold, chance, "Sunny" if random_number > chance else "Rainy"])  # Record stats for the day as a sublist

# Initialize variables to store statistics
total_glasses_made = 0  # Initialize total glasses made 
total_glasses_sold = 0  # Initialize total glasses sold 
total_sunny_days = 0  # Initialize total sunny days
total_chance_of_rain = 0  # Initialize total chance of rain

# Iterate over each sublist in the stats list
for stat in stats:
    # Increment the total glasses made by the number of glasses made on the current day
    total_glasses_made += stat[0]
    
    # Increment the total glasses sold by the number of glasses sold on the current day
    total_glasses_sold += stat[1]

    # Calculate the average number of glasses sold per day
    average_glasses_sold_per_day = total_glasses_sold / len(stats)

    # Check if the day was sunny and increment total sunny days
    if stat[3] == "Sunny":
        total_sunny_days += 1
    
    # Add the chance of rain on the current day to the total chance of rain
    total_chance_of_rain += stat[2]

    # Calculate the average chance of rain over the 10 days
    average_chance_of_rain = total_chance_of_rain / len(stats)

# Summary message
print("\nThank you for playing Lemonade Stand!")
print(f"You finished the game with ${startmoney:.2f}")

print("\n~~~~~~~~~~~~~~~~~~")
print("Here are your stats!\n")
print(f"You sold {total_glasses_sold} glasses of lemonade in total.")
print(f"You made {total_glasses_made} glasses of lemonade in total.")
print(f"On average you sold {average_glasses_sold_per_day:.2f} glasses of lemonade each day")
print(f"It was sunny {total_sunny_days} out of 10 days")
print(f"The average chance of rain was {average_chance_of_rain:.2f}")

