from Target import Target

targets = [
 Target("dinner-menu", "This Week's House Dinner Menu", "https://dining.caltech.edu/student-meal-plan"),
 Target("browne-comfort-eq", "Comfort Equation Specials", "https://dining.caltech.edu/where-to-eat-"),
 Target("browne-breakfast-lunch-menu", "Breakfast & Lunch Grill, Weekend Brunch Menu","https://dining.caltech.edu/where-to-eat-"),
 Target("browne-pizza-menu", "Wood Fired Pizza Oven Menu", "https://dining.caltech.edu/where-to-eat-"),
 Target("reddoor-food-menu", "Red Door Menu Items", "https://dining.caltech.edu/where-to-eat-"),
 Target("reddoor-drink-menu", "Red Door Drink Menu", "https://dining.caltech.edu/where-to-eat-"),
 Target("broad-breakfast-menu", "Breakfast Menu", "https://dining.caltech.edu/where-to-eat-"),
 Target("broad-lunch-menu", "Lunch Menu", "https://dining.caltech.edu/where-to-eat-"),
 Target("broad-drink-menu", "Broad Drink Menu", "https://dining.caltech.edu/where-to-eat-"),
 Target("avery-ramen", "Ramen Menu", "https://dining.caltech.edu/where-to-eat-"),
]

for target in targets:
 target.scrape()
 print(target)