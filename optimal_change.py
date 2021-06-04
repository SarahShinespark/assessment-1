"""
Sarah Dellheim's Assessment 1
Optimal Change
"You are writing a computer program for an electronic vending machine to give you the optimal change for an item's cost."
"""

#Prints a string with optimal change given cost and payment
#For debugging, returns an array with the amount of each denomination in the change
def optimal_change(item_cost, amount_paid):
    #Edge cases first
    #Make sure they paid enough
    if amount_paid < item_cost:
        print("*waits patiently for more change* uwu")
        return -1
    #Make sure money values make sense
    if item_cost < 0 or amount_paid < 0:
        print("I cannot handle negative money. Please wait for assistance at customer service.")
        return -2
    #Removed edge case for if money has 3+ digit decimal because it was catching false positives with 2 digit decimals
    
    #Trivial case
    if amount_paid == item_cost:
        print("Here is your item. Have a nice day!")
        return 0

    #Change due (dictionary); used to construct the output   
    #This relies on dictionaries being ordered, so please use Python 3.6 or later
    change = {100: 0,
              50:  0,
              20:  0,
              10:  0,
              5:   0,
              1:   0,
              0.25:0,
              0.1: 0,
              0.05:0,
              0.01:0}

    #Change due (floating point)
    due = amount_paid - item_cost
    
    # Count how much of each denomination
    for i, denom in enumerate(change.items()):
        step = denom[0]
        times = 0
        # Added a negligible amount to account for stupid floating points so I don't have to import Decimal
        # Otherwise I get an off-by-one error with the pennies because apparently 0.02 - 0.01 is 0.00999999
        # Originally this was modulo, but it doesn't feel kosher using % for decimal numbers
        while due + 0.0001 >= step:
            due -= step
            times += 1
        change[denom[0]] = times

    #Trim change and remove anything we have 0 of from the result
    change = trim_change_dict(change)

    #Begin displaying change
    print(f"The optimal change for an item that costs {print_money(item_cost)} with an amount paid of {print_money(amount_paid)} is ", end = "")
    if len(change) == 1:
        #Edge case: No commas
        # Convert single entry to a tuple
        # This took a lot of research to find something that worked, maybe there's a simpler way?
        for x in change.items():
            pronounce_money(x)
        print(".")
    if len(change) == 0:
        print("...absolutely NOTHING!")
    else:
        #Loop through change and use helper to pronounce each entry
        for i, x in enumerate(change.items()):
            if i == len(change)-1:
                #Last entry is spoken differently
                print("and ", end="")
                pronounce_money(x)
                print(".")
            else:
                pronounce_money(x)
                print(", ", end="")
    return change

#Takes a float and RETURNS it with $ and two decimal places
# 5.5 -> returns $5.50
#Optional hide_decimal = True results in 5 -> $5
def print_money(amount, hide_decimal = False):
    if not hide_decimal:
        return "${:,.2f}".format(amount)
    return "${:.0f}".format(amount)

#Takes <denom_arr>, an array of a denomination and its quantity
#i.e. [5,2] represents $5 x 2
def pronounce_money(denom_arr):
    change_words = {
         100: ["bill","bills"],
          50: ["bill","bills"],
          20: ["bill","bills"],
          10: ["bill","bills"],
           5: ["bill","bills"],
           1: ["bill","bills"],
        0.25: ["quarter","quarters"],
         0.1: ["dime","dimes"],
        0.05: ["nickel","nickels"],
        0.01: ["penny","pennies"]}
    #Build the output by finding the denomination [0] in the list and using its quantity [1]
    if denom_arr[0] in change_words:
        output = str(denom_arr[1])
        output+= " "
        #Print $ value if over a dollar
        if denom_arr[0] >= 1:
            output+= print_money(denom_arr[0], hide_decimal = True)
            output+= " "
        #If plural use the second word ("pennies"), if singular use the first ("penny")
        output+= change_words[denom_arr[0]][1] if denom_arr[1] > 1 else change_words[denom_arr[0]][0]
        print(output, end="")
        return output
    #Shouldn't run; if denom_arr isn't a bill or coin on the list
    print("this pile of loose change", end="")
    return "this pile of loose change"

def trim_change_dict(change):
    # I had to look up this comprehension, (thanks thispointer.com)
    # but basically making a new dict with no zero items.
    # Nobody wants to know they didn't get a $100 bill back, nor a $50, nor a $20...
    return {key: value for key, value in change.items() if value is not 0}
    

