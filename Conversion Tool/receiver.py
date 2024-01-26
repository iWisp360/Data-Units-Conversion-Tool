import formulas

def input_processor():
    completed = 0

    Data_Units = ["b", "kb", "mb", "gb", "tb"]

    x = input("In what unit will you express your number?(B, Kb, Mb, Gb, Tb)\n").lower()

    y = input("To which unit do you want to convert your number?\n").lower()
        # b2units
    if (x == Data_Units[0]): 
        if (y == Data_Units[1]):
            formulas.b2kb()
            completed = 1
        elif (y == Data_Units[2]):
            formulas.b2mb()
            completed = 1
        elif (y == Data_Units[3]):
            formulas.b2gb()
            completed = 1
        elif (y == Data_Units[4]):
            formulas.b2tb()
            completed = 1
    # kb2units
    if (x == Data_Units[1]): 
        if (y == Data_Units[0]):
            formulas.kb2b()
            completed = 1
        elif (y == Data_Units[2]):
            formulas.kb2mb()
            completed = 1
        elif (y == Data_Units[3]):
            formulas.kb2gb()
            completed = 1
        elif (y == Data_Units[4]):
            formulas.kb2tb()
            completed = 1
    # mb2units
    if (x == Data_Units[2]): 
        if (y == Data_Units[1]):
            formulas.mb2kb()
            completed = 1
        elif (y == Data_Units[0]):
            formulas.mb2b()
            completed = 1
        elif (y == Data_Units[3]):
            formulas.mb2gb()
            completed = 1
        elif (y == Data_Units[4]):
            formulas.mb2tb()
            completed = 1
    # gb2units
    if (x == Data_Units[3]): 
        if (y == Data_Units[1]):
            formulas.gb2kb()
            completed = 1
        elif (y == Data_Units[2]):
            formulas.gb2mb()
            completed = 1
        elif (y == Data_Units[0]):
            formulas.gb2b()
            completed = 1
        elif (y == Data_Units[4]):
            formulas.gb2tb()
            completed = 1
    # tb2units
    if (x == Data_Units[4]): 
        if (y == Data_Units[1]):
            formulas.tb2kb()
            completed = 1
        elif (y == Data_Units[2]):
            formulas.tb2mb()
            completed = 1
        elif (y == Data_Units[3]):
            formulas.tb2gb()
            completed = 1
        elif (y == Data_Units[0]):
            formulas.tb2b()
            completed = 1

    if (completed == 1):
        exit(0)
    if (x == "" and y == ""):
        print("You didn't type anything ._.\n")
        input_processor()
    if (all(x != list_data for list_data in Data_Units) or all(y != list_data for list_data in Data_Units)):
        print("Enter a valid input for source and/or conversion unit\n")
        input_processor()
    if (x == y):
        print ("Converting 2 same units doesn't make sense\n")
        input_processor()