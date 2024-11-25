from groceries import buy_groceries
import random

def check_user_input(prompt):
    '''This confirms that user input is an integer.
    '''
    response = input(prompt)
    done=False
    while done==False:
        try:
            int(response)
            done=True
        except ValueError:
            try:
                response = float(response)
                print("Please enter a whole number.")
                response = input(prompt)
            except ValueError:
                print("Please enter a valid number.")
                response = input(prompt)
    return int(response)
    
def check_user_input_1_or_2(prompt):
    '''This confirms that user input is an integer.
    '''
    response = input(prompt)
    done=False
    while done==False:
        try:
            num = int(response)
            if num in [1, 2]:
                done = True
            else:
                print("Please enter either 1 or 2.")
                response = input(prompt)
        except ValueError:
            try:
                response = float(response)
                print("Please enter a whole number.")
                response = input(prompt)
            except ValueError:
                print("Please enter a valid number.")
                response = input(prompt)
    return int(response)

def pay_gas(values):
    '''This pays the gas.
    '''
    values["funds"] -= 40
    print("You pay for gas. -$40")
    return values

'''There are 8 keys in values:
1. funds - this counts how much money the character has.
2. rent - this counts how much rent is per month.
3. salary - this counts how much money the character makes per month.
4. infractions - this counts how many work infractions the character has.
5. parenting - this counts how good of a parent the character is.
6. child_health - this counts the child's stomach health.
7. tooth_health - this counts the main character's tooth health.
8. groceries - this tracks the groceries bought
'''

def overview(name):
    '''This runs Day 0 of the simulation. Choice: rent and salary.
    '''
    values = {

    }
    print("As a reminder, press enter to continue when the instructions end, " + name + ".")
    input()
    print("You are a single mother living in Chicago in 2022.")
    print("You work at CS Enterprises.")
    print("The default salary is $2,878 per month.")
    choice_salary = check_user_input("Your monthly salary is: ")
    print("You and your child live in an apartment. Rent does not cover utilities.")
    print("The default salary is $1,385 per month.")
    choice_rent = check_user_input("Your monthly rent is: ")
    print()
    print("Win the game by paying rent on Day 30.")
    input()
    values["salary"] = choice_salary
    values["rent"] = choice_rent
    values["current_groceries_cost"] = 0
    values["funds"] = 1000 #POSSIBLY MAKE THIS CHANGEABLE?
    return values

def day_one(values, name):
    '''This runs Day 1 of the simulation. Challenge: no parking.
    '''
    print("It is Day 1. You have $1,000.")
    print("Good luck, " + name + ".")
    input()
    values["infractions"] = 0
    print("You drive ten minutes to the train station.")
    print("There is no parking.")
    print()
    print("Should you:")
    print("1. Park illegally.")
    print("2. Search for a spot.")
    parking_choice = check_user_input_1_or_2("")
    print()
    if parking_choice == 1:
        values["infractions"] += 0
        values["funds"] += 0
        print("You park illegally in an empty gravel lot.")
    if parking_choice == 2:
        values["infractions"] += 1
        values["funds"] += 0
        print("You spend 20 minutes trying to find a spot.")
        print("You are late to work.")
    input()
    print("Work is slow.")
    if parking_choice == 1:
        values["funds"] -= 50
        print("When you get back, you find a parking fine of $50.")
        input()
        print("But, hey, the day is over!")
    else:
        pass
    print("Time to make dinner.")
    print()
    print("Day 1 funds: $" + str(values.get("funds")))
    #  start with empty dict and then add them as they become relevant
    input()
    return values

def day_two(values, name):
    '''This runs Day 2 of the simulation. Challenge: delayed train, sick child.
    '''
    print("Good morning, " + name + ".")
    print("It is Day 2.")
    input()
    print("On the way to work, the Red Line Train is delayed.")
    print("Should you:")
    print("1. Wait for the Red Line.")
    print("2. Take an Uber.")
    transportation_choice = check_user_input_1_or_2("")
    print()
    if transportation_choice == 1:
        values["funds"] += 0
        values["infractions"] += 1
        print("The Red Line takes 30 minutes to resume working.")
        if values["infractions"] >= 2:
            print("Your boss yells at you. This is a warning.")
        elif values["infractions"] == 1:
            print("You are 30 minutes late to work.")
    elif transportation_choice == 2:
        values["funds"] -= 35
        values["infractions"] += 0
        print("You arrive on time to work.")
    print()
    print("Day 2 funds: $" + str(values.get("funds")))
    input()
    return values
        
def day_three(values, name):
    '''This runs Day 3 of the simulation. Challenge: sick child.
    '''
    print("It's a sunny 40 degrees in Chicago, " + name + "!")
    print("Welcome to Day 3.")
    input()
    print("The school calls you at work.")
    print("Should you:")
    print("1. Pick up.")
    print("2. Ignore.")
    call_choice = check_user_input_1_or_2("")
    values["parenting"] = 0
    print()
    if call_choice == 1:
        values["infractions"] += 1
        values["parenting"] += 1
        print("Bring-bring-bring!")
        print("Your child was sent to the nurse's office with a severe stomachache.")
        input()
        print("You drive them home.")
    if call_choice == 2:
        values["infractions"] += 0
        values["parenting"] += 0
        print("Your boss is watching.")
        print("You ignore the call and get back to work.")
        input()
        print("Hours later, you drive your kid home. They have a severe stomachache.")
    input()
    print("You may select a treatment plan:")
    print("1. Give them Pepto Bismol.")
    print("2. Take them to the hospital.")
    sick_child_choice = check_user_input_1_or_2("")
    print()
    values["child_health"] = 0
    if sick_child_choice == 1:
        values["funds"] += 0
        values["child_health"] += 0
        values["parenting"] += 0
        if values["parenting"] > 0:
            print("With medicine, they go to sleep.")
            print("Your child calls you a good mom.")
        if values["parenting"] == 0:
            print("With medicine, they go to sleep.")
            print("But they are upset that you didn't take them home.")
    elif sick_child_choice == 2:
        values["funds"] -= 1150
        values["child_health"] += 1
        values["parenting"] += 1
        print("A doctor visits you and your child and performs an x-ray.")
        print("Unfortunately, you do not have health care.")
        print("-$1,150.")
        input()
        if values["parenting"] > 0:
            print("Your child is healthy. You follow the doctor's advice, and they go to sleep.")
            print("Your child calls you a good mom.")
        if values["parenting"] == 0:
            print("Your child is healthy. You follow the doctor's advice, and they go to sleep.")
            print("But they are upset that you didn't take them home.")
    print()
    print("Day 3 funds: $" + str(values.get("funds")))
    input()
    return values

def day_four(values, name):
    '''This runs Day 2 of the simulation. Event: employee of the month.
    '''
    print("Breaking news! Cardi B splits from Offset.")
    print("Welcome to Day 4, " + name + ".")
    input()
    print("Your car is low on gas. You stop at a gas station.")
    pay_gas(values)
    input()
    print("At your work, your boss announces Employee of the Month.")
    print("Employee of the Month receives a $100 bonus.")
    input()
    if values["infractions"] == 0:
        values["funds"] += 100
        print("Congratulations! You are Employee of the Month.")
    elif values["infractions"] == 1 or 2:
        values["funds"] += 0
        print("Unfortunately, you are not Employee of the Month.")
    elif values["infractions"] <= 3:
        values["funds"] += 100
        print("You are not Employee of the Month, and your boss delivers you another warning.")
    input()
    print("Day 4 funds: $" + str(values.get("funds")))
    input()
    return values

def day_five(values, name):
    '''This runs Day 5 of the simulation. Challenge: groceries.
    '''
    print("It's Day 5, " + name + ".")
    print("You wake up to an empty fridge.")
    input()
    day_5_funds = values.get("funds")
    print("After work, it's time to get groceries.")
    print("Your kid asks for mangoes.")
    input()
    values["groceries"] = ""
    buy_groceries(values)
    print("You finish shopping.")
    if values["groceries"] == "":
        print("You bought nothing.")
    else:
        print("And hey, the cashier throws in a bag of chips for free!")
        input()
        day_5_groceries_cost = day_5_funds - values.get("funds") + 10
        values["funds"] -= 10
        print("You spent $" + str(day_5_groceries_cost) + " on groceries. Not bad at all.")
        print("You bought " + str(values.get("groceries")) + "and a bag of chips.")
    input()
    print("Day 5 funds: $" + str(values.get("funds")))
    input()
    return values

def day_six(values, name):
    '''This runs Day 6 of the simulation. Challenge: dentist visit (wisdom teeth surgery).
    '''
    print("Hello, " + name + ". It's already Day 6!")
    print()
    print("You are able to take time off of work to see the dentist. Your tooth has been bothering you.")
    print("There's good news. And then there's bad news.")
    input()
    print("The dentist informs you that you will need wisdom teeth surgery.")
    print("But good news! They can see you in only 2 weeks.")
    input()
    print("Great.")
    input()
    print("You will need to ask your boss for a few days off.")
    print("And you will need to scrounge up extra money.")
    input()
    print("$3000, to be exact.")
    input()
    print("Day 6 funds: $" + str(values.get("funds")))
    input()
    return values

def day_seven(values):
    '''This runs Day 7 of the simulation. Challenge: child's soccer party.
    '''
    print("You wake up to a beautiful sunrise. Happy Day 7.")
    print("The weekend at last.")
    input()
    print("You want to spend the day with your kid.")
    print("They want to attend a soccer party.")
    print("")
    print("Should you send your kid with a gift?")
    print("1. Yes. $20")
    print("2. No. $0")
    gift_choice = check_user_input_1_or_2("")
    print()
    if gift_choice == 1:
        values["funds"] -= 20
        values["parenting"] += 1
        print("Your child thanks you.")
        print("At the party, they have a great time.")
    if gift_choice == 2:
        values["funds"] += 0
        values["parenting"] += 0
        print("Your child goes embarrassed to not have a gift.")
    input()
    print("You miss them on your day off.")
    input()
    print("Day 7 funds: $" + str(values.get("funds")))
    input()
    return values

def day_nine(values):
    '''This runs Day 9 of the simulation. Event: going out on a date.
    '''
    print("It's Sunday.")
    print("At church, someone asks you out on a date.")
    input()
    print("They ask if you will go to a nice restaurant with them.")
    print("What should you do?")
    print("1. Say yes and go on the date. $20")
    print("2. Say no and save money. $0")
    print("3. Suggest another date. $0")
    date_choice = check_user_input("")
    print()
    if date_choice == 1:
        values["funds"] -= 20
        values["parenting"] += 0
        print("You dress up for the nice restaurant, and the food is amazing.")
        print("Your date tells you that you look beautiful.")
        print("You bring home leftovers for your kid.")
    elif date_choice == 2:
        values["funds"] += 0
        values["parenting"] += 1
        print("You stay in and watch Moana with your kid.")
        print("You go to bed early.")
    elif date_choice == 3:
        values["funds"] -= 0
        values["parenting"] += 0
        print("You invite them to read at the Harold Washington Library together.")
        print("At the library, you have fun, but you miss your kid.")
    input()
    print("Day 9 funds: $" + str(values.get("funds")))
    input()
    return values

def day_twelve(values, name):
    '''This runs Day 12 of the simulation. Challenge: groceries. I/a, additional challenge: sick child stomachache.
    '''
    print("Rise and shine, " + name + ".")
    print("You are out of food.")
    input()
    print("You drive to the grocery store after work.")
    print("Like last time, your kid asks for frozen mango.")
    input()
    day_12_funds = values.get("funds")
    values["groceries"] = ""
    buy_groceries(values)
    print("You finish shopping.")
    print("The cashier recognizes you. Here's a lollipop for your kid.")
    input()
    if values["groceries"] == "":
        print("You bought nothing.")
    else:
        day_12_groceries_cost = day_12_funds - values.get("funds") + 8
        values["funds"] -= 8
        print("You only spent $" + str(day_12_groceries_cost) + " on groceries.")
        print("You bought " + str(values.get("groceries")) + "and a lollipop.")
    input()
    if values["child_health"] == 0:
        values["funds"] -= 1150
        values["child_health"] += 1
        print("You get home.")
        print("Your kid's stomache returns, worse this time.")
        print("You take them to the hospital.")
        input()
        print("A doctor visits you and your child and performs an x-ray.")
        print("Unfortunately, you do not have health care.")
        print("-$1,150.")
        input()
    print("Day 12 funds: $" + str(values.get("funds")))
    input()
    return values

def day_thirteen(values, name):
    '''This runs Day 13 of the simulation. Event: pay day and student loans
    '''
    print(name + ", it's almost half way.")
    print("And would you look at what came in the mail?")
    input()
    print("What should you open first?")
    print("1. Your paycheck.")
    print("2. The scary-looking envelope.")
    envelope_choice = check_user_input_1_or_2("")
    print()
    if envelope_choice == 1:
        print("You open your paycheck.")
        print("It's $" + str(values.get("salary")/2) + "!")
        values["funds"] += (values.get("salary")/2)
        input()
        print("You open the scary-looking envelope.")
        print("It's student loans.")
        print("They cost $500.")
        values["funds"] -= 500
    elif envelope_choice == 2:
        print("You open the scary-looking envelope.")
        print("It's student loans.")
        print("They cost $500.")
        values["funds"] -= 500
        input()
        print("You open your paycheck.")
        print("It's $" + str(values.get("salary")/2) + "!")
        values["funds"] += (values.get("salary")/2)
    input()
    print("Day 13 funds: $" + str(values.get("funds")))
    input()
    return values

def day_fifteen(values):
    '''This runs Day 15 of the simulation. Challenge: car crash, random!.
    '''
    print("You have a great morning with your kid.")
    print("On the way to work, you sing Tangled to yourself.")
    input()
    print("Suddenly, the car in front of you brakes.")
    print("You rear-end them.")
    input()
    print("You pull over. Fortunately, no one is injured, and they are not upset.")
    print("Your car is more beat-up than theirs.")
    input()
    car_accident_cost = [50, 65, 75, 95, 150, 345, 520, 820, 1900]
    current_car_accident_cost = random.choice(car_accident_cost)
    print("The cost of the accident is $" + str(current_car_accident_cost) + ".")
    input()
    values["infractions"] += 1
    values["funds"] -= current_car_accident_cost
    print("Day 15 funds: $" + str(values.get("funds")))
    input()
    return values

def day_seventeen(values, name):
    '''This runs Day 17 of the simulation. Event: school field trip.
    '''
    print("Hello, " + name + ".")
    print("Your child is going on a school field trip to the zoo.")
    input()
    print("The school asks for your participation. What should you do?")
    print("1. Serve as a chaperone.")
    print("2. Donate $20.")
    print("3. Do nothing.")
    field_trip_choice = check_user_input("")
    print()
    if field_trip_choice == 1:
        values["funds"] += 0
        values["parenting"] += 1
        values["infractions"] += 1
        print("You go the zoo. You have fun.")
        print("You miss work.")
    elif field_trip_choice == 2:
        values["funds"] -= 20
        values["parenting"] += 1
        values["infractions"] += 0
        print("You donate $20 and miss the fieldtrip.")
        print("Your kid tells you all about the tiger they saw.")
    elif field_trip_choice == 3:
        values["funds"] += 0
        values["parenting"] += 0
        values["infractions"] += 0
        print("You do nothing. The PTA sends you an email.")
        print("Your kids tells you all about the elephant they saw.")
    input()
    print("Day 17 funds: $" + str(values.get("funds")))
    input()
    return values

def day_eighteen(values, name):
    '''This runs Day 18 of the simulation. Challenge: extra ways to make $$$.
    '''
    print("You are low on gas again. You stop for some on the way to work.")
    pay_gas(values)
    input()
    print("Let's face it, " + name + ".")
    print("You are running low on money.")
    input()
    print("Let's see how you can make extra money.")
    input()
    if values["parenting"] >= 3:
        print("You've been a good mom. Your kid lets you sell some of their clothes.")
        values["funds"] += 230
        input()
    print("Would you like to ask your boss for a bonus?")
    print("1. Yes.")
    print("2. No.")
    bonus_choice = check_user_input_1_or_2("")
    print()
    if bonus_choice == 1:
        if values["infractions"] <= 2:
            values["funds"] += 100
            print("Your boss gives you an $100 bonus.")
        else:
            print("Your boss tells you to work harder.")
            print("No bonus.")
    elif bonus_choice == 2:
        pass
    input()
    print("Would you like to make extra money?")
    print("1. Yes.")
    print("2. No.")
    extra_money_choice = check_user_input_1_or_2("")
    print()
    if extra_money_choice == 1:
        values["funds"] += 300
        values["infractions"] += 1
        print("You pet sit all night.")
        print("You make extra money, and your kid loves the pets.")
    elif extra_money_choice == 2:
        values["funds"] += 0
        print("You spend your evening playing with your kid.")
        print("You did not make any more money.")
    input()
    print("Day 18 funds: $" + str(values.get("funds")))
    input()
    return values

def day_twenty(values, name):
    '''This runs Day 20 of the simulation. Challenge: groceries.
    '''
    print("It's Day 20! Two thirds of the way over, " + name + ".")
    input()
    print("At work, your boss asks you if you can work more hours per week.")
    print("More hours... less time with your kid.")
    input()
    print("What should you say?")
    print("1. 'Yes, I will work more hours.'")
    print("2. 'No, I will not work more hours.'")
    work_choice = check_user_input_1_or_2("")
    print()
    if work_choice == 1:
        values["infractions"] += 1
        values["parenting"] += 0
        values["funds"] += 500
        print("Your boss is very grateful.")
    elif work_choice == 2:
        values["infractions"] += 0
        values["parenting"] += 1
        print("Your boss is annoyed.")
    input()
    print("It's grocery time again! Your favorite time of the week.")
    input()
    print("You stop by the grocery store.")
    print("Your kid asks for their favorite")
    input()
    day_20_funds = values.get("funds")
    values["groceries"] = ""
    buy_groceries(values)
    print("You step outside with your groceries.")
    print("You find a $5 bill on the sidewalk.")
    values["funds"] += 5
    input()
    if values["groceries"] == "":
        print("You bought nothing.")
    else:
        print("You leave with " + str(values.get("groceries")) + "and a $5 bill.")
        day_20_groceries_cost = day_20_funds - values.get("funds") + 8
        print("You spent $" + str(day_20_groceries_cost) + " on groceries.")
        values["funds"] -= 8
    input()
    print("Day 20 funds: $" + str(values.get("funds")))
    input()
    return values

def day_twenty_one(values, name):
    '''This runs Day 21 of the simulation. Challenge: WT surgery.
    '''
    values["tooth_health"] = 0
    print("It is time for your wisdom teeth surgery, " + name + ".")
    input()
    print("Would you like to have the surgery?")
    print("1. Yes.")
    print("2. No.")
    tooth_choice = check_user_input_1_or_2("")
    print()
    if tooth_choice == 1:
        values["tooth_health"] += 1
        values["funds"] -= 3000
        values["infractions"] += 1
        print("You have the surgery and take one day off, recovering over the weekend.")
        print("It takes a chunk out of your bank account.")
        print("But you feel much better.")
    elif tooth_choice == 2:
        values["tooth_health"] += 0
        values["funds"] += 0
        values["infractions"] += 0
        print("You do not have the surgery and go to work instead.")
        print("Your tooth hurts.")
    input()
    print("What a long day.")
    input()
    print("Day 21 funds: $" + str(values.get("funds")))
    input()
    return values

def day_twenty_two(values):
    '''This runs Day 22 of the simulation. Event: child's drawing.
    '''
    if values["parenting"] >= 4:
        print("You have been a good mother.")
        print("Your child makes you a drawing.")
        for row in range(0, 9):
            for slope in range(0, 9-row):
                print(" ", end="")
            for slope2 in range(0, 2*row+1):
                print("*", end="")
            print("*")
    return values

def day_twenty_four(values, name):
    '''This runs Day 22 of the simulation. Event: utilities. Challenge: cable.
    '''
    print("It's your favorite thing, " + name + "!")
    print("More mail.")
    input()
    print("You read the utilities bill, which costs $169.96 for electricity, heating, water and garbage costs.")
    values["funds"] -= 169
    input()
    print("You pay it.")
    input()
    print("Should you pay the internet bill?")
    print("1. Yes. $60")
    print("2. No. $0")
    cable_bill_choice = check_user_input_1_or_2("")
    print()
    if cable_bill_choice == 1:
        print("You pay the internet bill.")
        values["funds"] -= 60
    elif cable_bill_choice == 2:
        print("You do not pay the internet bill.")
        print("In addition to losing internet access, not paying the internet bill can result in financial penalties.")
        print("You cannot work at home anymore.")
        values["funds"] -= 0
        values["infractions"] += 1
    input()
    print("Day 22 funds: $" + str(values.get("funds")))
    input()
    return values

def day_twenty_seven(values, name):
    '''This runs Day 27 of the simulation. Event: birthday.
    '''
    print("Happy birthday, " + name + "!")
    print("Your family and friends send you money.")
    values["funds"] += 100
    input()
    print("You get home late from work and spend the night with your child.")
    input()
    print("Day 27 funds: $" + str(values.get("funds")))
    input()
    return values

def day_twenty_eight(values): #weekend
    '''This runs Day 28 of the simulation. Challenge: friend's wedding.
    '''
    print("It is the weekend and your friend's wedding.")
    print("You really want to go.")
    print("But let's look at the numbers.")
    input()
    print("You need to buy a gift and pay for gas.")
    print("Their gift registry is long and nothing is inexpensive for you.")
    print()
    print("Should you go?")
    print("1. Yes. $90")
    print("2. No. $0")
    wedding_choice = check_user_input_1_or_2("")
    print()
    if wedding_choice == 1:
        print("On the way to the wedding, you stop for gas.")
        pay_gas(values)
        input()
        print("The wedding is so much fun.")
        print("You dance with all of your friend2.")
        values["funds"] -= 50
    if wedding_choice == 2:
        print("You really miss your friends.")
        print("At least you didn't spend money.")
        input()
        print("You clean your apartment and run chores.")
    input()
    print("Day 28 funds: $" + str(values.get("funds")))
    input()
    return values

def day_twenty_nine(values):
    '''This runs Day 29 of the simulation. Challenge: pet sitting (unless n/ WTS). Event: winning the lottery
    '''
    print("One of your distant relatives wins the lottery.")
    print("Should you buy a ticket?")
    print("1. Yes. $2")
    print("2. No.")
    lottery_choice = check_user_input_1_or_2("")
    print()
    if lottery_choice == 1:
        winning_lottery_ticket = random.randint(1, 300000000)
        if winning_lottery_ticket == 3200:
            values["funds"] += 2344298
            print("Congratulations, you won the lottery!")
        elif winning_lottery_ticket != 3200:
            print("You didn't win the lottery.")
            print("It was a 1:300 million chance anyways.")
    elif lottery_choice == 2:
        print("It was a 1:300 million chance anyways.")
    input()
    if values["tooth_health"] == 1:
        print("You need extra money.")
        print("Should you work instead of spending time with your kid?")
        print("1. Yes.")
        print("2. No.")
        pet_sit_choice = check_user_input_1_or_2("")
        print()
        if pet_sit_choice == 1:
            print("You work all day and night.")
            print("When you come home, your kid is already in bed.")
            values["funds"] += 200
            values["parenting"] += 0
            values["infractions"] += 1
        elif pet_sit_choice == 2:
            print("You read your child Harry Potter.")
            print("You cuddle together. You are really grateful for this time with them.")
            values["funds"] += 0
            values["parenting"] += 1
    elif values["tooth_health"] != 1:
        print("Your tooth hurts too bad to get work done.")
        values["parenting"] += 0
        values["infractions"] += 1
    input()
    print("Day 29 funds: $" + str(values.get("funds")))
    input()
    return values

def day_thirty(values, name):
    '''This runs Day 30 of the simulation. Challenge: paycheck and paying rent.
    It also tracks how well you have scored at work (infractions, out of 11), with your child (parenting, out of 12).
    '''
    print(name + ", it's day 30!")
    print("It's payday.")
    print("Here's $" + str(values.get("salary")/2) + ".")
    input()
    print("Let's see how good of a mother you were.")
    input()
    values["funds"] += (values.get("salary")/2)
    if 0 <= values["parenting"] <= 3:
        print("You were a poor mother to your child.")
        print("Spend more time with your kid.")
    elif 4 <= values["parenting"] <= 7:
        print("You were an okay mother to your child.")
        print("You spent some time with them.")
    elif 8 <= values["parenting"]:
        print("You were a fantastic mother to your child.")
        print("You spent so much time and energy on your kid.")
    input()
    print("Fine, how good of a worker were you?")
    input()
    if 0 <= values["infractions"] <= 3:
        print("You were a fantastic employee.")
        print("Your boss offers you a bonus of $100.")
        values["funds"] += 100
    elif 4 <= values["infractions"] <= 7:
        print("You were an adequate employee.")
        print("You kept your job.")
    if 8 <= values["infractions"] <= 10:
        print("You were a terrible employee.")
        print("Your boss fires you at the end of the workday.")
    input()
    print("And now, rent is due.")
    input()
    print("$" + str(values.get("rent")) + ", to be exact.")
    print("You have $" + str(values.get("funds")) + ".")
    if values.get("funds") >= values.get("rent"):
        print("You can afford rent.")
        print()
        print("Congratulations! You have won the game.")
        values["funds"] -= values["rent"]
        print("You have $" + str(values.get("funds")) + " left.")
        input()
        print("Now, can you afford groceries, car maintenance, and living expenses?")
    elif values.get("funds") < values.get("rent"):
        print("You cannot afford rent.")
        print("Bad news. You have lost the game.")
        values["funds"] -= values["rent"]
        input()
        print("You have $" + str(values.get("funds")) + " left.")
        input()
        print("Now, can you afford groceries, car maintenance, and living expenses?")
    if values["tooth_health"] == 0:
        input()
        print("And you still need wisdom tooth surgery.")
    input()
    return values
