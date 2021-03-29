a_list = ["Glad", "Påsk", "Forefront", "2021", "Från", "Felix Tran"]

def printlist():
    new_list = []
    new_list.append('*************')
    for x in a_list:
        new_list.append('* '+ x +' *')
    new_list.append('*************')
    for y in new_list:
        print(y)

printlist()