def phoneLetters(num):

    keyMappings = {"1":"_","2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "0":"-"}
    combinations = [""]
    temp = [""]

    if not num:
        return []
    n = len(num)

    for i in range(n):
        temp = [x + y for x in temp for y in keyMappings[num[i]]]
        combinations = [combo for combo in temp if len(combo) == n]

    if "easter-egg" or "easter_egg" in combinations:
         print('Congratulations! You found the "Easter Egg" combination!')
    else:
         print(combinations)
         print("")
         print('You didn\'t find the "Easter Egg", please try again')
         print("")
