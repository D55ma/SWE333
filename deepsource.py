

def append(number, number_list=[]):
    number_list.append(number)
    print(number_list)
    return number_list

append(5) # expecting: [5]
append(7) # expecting: [7]
append(2) # expecting: [2]
