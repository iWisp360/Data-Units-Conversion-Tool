import formulas
import sys

x = None # Source Unit
y = None # Conversion Unit

while (y != "b" or y != "kb" or y != "mb" or y != "gb" or y != "tb"): 

    x = input("In what unit will you express your number?(B, Kb, Mb, Gb, Tb)\n").lower()

    y = input("To which unit do you want to convert your number?\n").lower()

# vars x and y will be used to call the conversion functions in the formulas module

# Below there are conditionals that will use the correct conversion function depending on your input

    if (x == y):
        sys.exit("Restart the program, converting 2 same units doesn't make sense")

# b2units
    if (x == "b"): 
        if (y == "kb"):
            formulas.b2kb()
            exit(0)
    if (x == "b"): 
        if (y == "mb"):
            formulas.b2mb()
            exit(0)
    if (x == "b"):
        if (y == "gb"):
            formulas.b2gb()
            exit(0)
    if (x == "b"):
        if (y == "tb"):
            formulas.b2tb()
            exit(0)
# kb2units
    if (x == "kb"): 
        if (y == "b"):
            formulas.kb2b()
            exit(0)
    if (x == "kb"): 
        if (y == "mb"):
            formulas.kb2mb()
            exit(0)
    if (x == "kb"):
        if (y == "gb"):
            formulas.kb2gb()
            exit(0)
    if (x == "kb"):
        if (y == "tb"):
            formulas.kb2tb()
            exit(0)
# mb2units
    if (x == "mb"): 
        if (y == "kb"):
            formulas.mb2kb()
            exit(0)
    if (x == "mb"): 
        if (y == "b"):
            formulas.mb2b()
            exit(0)
    if (x == "mb"):
        if (y == "gb"):
            formulas.mb2gb()
            exit(0)
    if (x == "mb"):
        if (y == "tb"):
            formulas.mb2tb()
            exit(0)
# gb2units
    if (x == "gb"): 
        if (y == "kb"):
            formulas.gb2kb()
            exit(0)
    if (x == "gb"): 
        if (y == "mb"):
            formulas.gb2mb()
            exit(0)
    if (x == "gb"):
        if (y == "b"):
            formulas.gb2b()
            exit(0)
    if (x == "gb"):
        if (y == "tb"):
            formulas.gb2tb()
            exit(0)
# tb2units
    if (x == "tb"): 
        if (y == "kb"):
            formulas.tb2kb()
            exit(0)
    if (x == "tb"): 
        if (y == "mb"):
            formulas.tb2mb()
            exit(0)
    if (x == "tb"):
        if (y == "gb"):
            formulas.tb2gb()
            exit(0)
    if (x == "tb"):
        if (y == "b"):
            formulas.tb2b()
            exit(0)
    print("Enter a valid input for source and/or conversion unit\n")   