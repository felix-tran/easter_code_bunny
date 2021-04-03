import sys

def phoneLetters(num):
    
    keyMappings = {"1":"_","2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "0":"_"}
    combinations = [""]
    temp = [""]

    if not num:
        return []
    if len(num) > 10:
        print("You have used more than 10 characters. Please try again")
        sys.exit()
        
    n = len(num)

    try:
        for i in range(n):
           temp = [x + y for x in temp for y in keyMappings[num[i]]]
           combinations = [combo for combo in temp if len(combo) == n]

        if "easter_egg" in combinations:
            print('Congratulations! You found the "Easter Egg" combination!')
        else:
            print(combinations)
            print("")
            print('You didn\'t find the "Easter Egg". Please try again')
            print("")
    except:
        print("Only numbers can be used. Please try again")
