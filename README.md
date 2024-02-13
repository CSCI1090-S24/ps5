# Problem Set 5
You should feel comfortable with GitHub by now. If you're not, come to office hours with me or the TAs.

If you think you see an error or typo, let me know! I will update [this version of the repo](https://github.com/CSCI1090-S24/ps5) with any corrections you suggest.

The deliverables for this problem set are the following:

* `lemonade.py`

**Remember** I now expect you to write comments in your code! One point will be deducted if you do not provide comments explaining your code. Here's what I would like commented this time:

* Before every function, describe what it does and what its arguments are. Exception: you do not need to explain what `main()` is for.
* Before every variable, explain what value it is holding. Exception: variables that appear after the keyword `for`.
* **NEW** Insert a blank line before each comment. See my sample code for examples.
* **NEW** Insert line breaks in comments to make them readable without horizontal scrolling. See my sample code for examples.

**Remember** Now at the top of every file, you will include your honor pledge. The first four lines (comments) of every Python file should be this information. You will lose one point if you don't include these four lines.

* The name of the file.
* Your name.
* The date.
* "This code is my own work. I did not share my code or look at the code of another student. I did not consult ChatGPT, CoPilot, or another large language model."

**Note** The only libraries you can import are `random()` and `math()`. 

## Lemonade Stand Game
You will write a game in which the user runs a lemonade stand. The user starts with $10. Their goal is to sell enough lemonade in 10 days to double their money to $20. 

A glass of lemonade costs 50 cents to make, and each glass sells for $1. Every day the user is told the chance of rain that day, and they must decide how many glasses of lemonade to make using their available money. If it rains, none of their lemonade will be sold. If it is sunny, all of their lemonade will be sold.

You will let the user play the game, keeping track each day of the number of glasses they make, the number of glasses they sell, the chance of rain that day, and whether or not it was sunny.

I've given you some starter code in `lemonade.py`. I recommend that you use the starter code. You will have two chunks of code to write.

**Chunk 1:** `while()` loop to run the game

While the number of days so far is less than 10:
  * Tell the user the current day.
  * The the user how much money they have right now.
  * Generate a random number between 0 and 1 to serve as the `chance of rain`.
  * Ask the user how many glasses of lemonade they want to make. If they say more glasses than they have money to make, let them know and then ask them again for the number of glasses they want to make until they pick a number that they can afford.
  * Get another random number between 0 and 1.
      - If it's less than the `chance of rain`, it rained. No lemonade was sold, so deduct 50 cents for each glass made from the user's total money.
      - If it's more than the `chance of rain`, it was sunny. All the lemonade was sold, so add 50 cents for each glass ($1 sale price minus 50 cents cost to make the lemonade) to the user's total money.
  * Enter the stats for the day as a list into the list of lists called `stats`: the number of glasses they made, the number of glasses they sold, the chance of rain that day, and whether or not it was sunny.

**Chunk 2:** Calculate and report statistics of the game
* Using a for loop over the `stats` list of lists, calculate
  - (1) the total number of glasses of lemonade made;
  - (2) the total number of glasses of lemonade sold;
  - (3) the average number of glasses sold per day;
  - (4) the number of sunny days; and
  - (5) the average chance of rain over the 10 days. 
* Print out these statistics to the user, using the wording shown in the example below.

Your output will look something like this, though the numbers will be different.

```
Welcome to the lemonade stand!

You have $10.00
It costs 50 cents to make a glass of lemonade.
A glass sells for $1.
If it's sunny, you'll sell all the lemondade you make.
If it rains, you won't sell any lemondade.
Your goal is to get to $20 in 10 days.
Today is day 1.


You have $10.00
The chance of rain is 71%.
How many glasses of lemonade would you like to make today? 300
You don't have enough money to make that much lemonade.
How many glasses of lemonade would you like to make today? 0
It rained! You didn't sell any lemonade.
Today is day 2.


You have $10.00
The chance of rain is 23%.
How many glasses of lemonade would you like to make today? 10
It rained! You didn't sell any lemonade.
Today is day 3.


You have $5.00
The chance of rain is 16%.
How many glasses of lemonade would you like to make today? 10
It was sunny! You sold all your lemonade.
Today is day 4.


You have $10.00
The chance of rain is 75%.
How many glasses of lemonade would you like to make today? 0
It was sunny! You sold all your lemonade.
Today is day 5.


You have $10.00
The chance of rain is 98%.
How many glasses of lemonade would you like to make today? 0
It rained! You didn't sell any lemonade.
Today is day 6.


You have $10.00
The chance of rain is 71%.
How many glasses of lemonade would you like to make today? 0
It rained! You didn't sell any lemonade.
Today is day 7.


You have $10.00
The chance of rain is 96%.
How many glasses of lemonade would you like to make today? 0
It rained! You didn't sell any lemonade.
Today is day 8.


You have $10.00
The chance of rain is 59%.
How many glasses of lemonade would you like to make today? 0
It rained! You didn't sell any lemonade.
Today is day 9.


You have $10.00
The chance of rain is 13%.
How many glasses of lemonade would you like to make today? 10
It was sunny! You sold all any lemonade.
Today is day 10.


You have $15.00
The chance of rain is 81%.
How many glasses of lemonade would you like to make today? 0
It rained! You didn't sell any lemonade.

Thank you for playing Lemonade Stand!
You finished the game with $15.00

~~~~~~~~~~~~~~~~~~
Here are your stats!

You sold 20 glasses of lemonade in total.
You made 30 glasses of lemonade in total.
On average you sold 2.00 glases of lemonade each day.
It was sunny 3 out of 10 days.
The average chance of rain was 0.60.
```

---

## Deadline: Monday, February 19, 2024, at 11:59pm EST

## Deliverables

`lemonade.py`

## Reminder: Important Guidelines
* Points will be deducted if your output does not match the required format.
* Points will be deducted if your files are not named as required.
* Points will be deducted if your files are not in the correct location (i.e., in the top-level directory where you see the `README`.)
* Points will be deducted if you do not include comments as described above.
* Points will be deducted if you do not include your honor pledge at the top of each file.


