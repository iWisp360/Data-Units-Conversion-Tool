import formulas
import sys

x = None

x = input("In what unit will you express your number?(B, Kb, Mb, Gb, Tb)\n")
    
if (x != "B" or x != "b" or x != "kb" or x != "Kb" or x != "mb" or x != "Mb" or x != "gb" or x != "Gb" or x != "tb" or x != "Tb"):
    while (x != "B" or x != "b" or x != "kb" or x != "Kb" or x != "mb" or x != "Mb" or x != "gb" or x != "Gb" or x != "tb" or x != "Tb"):    
        if (x == "B" or x == "b" or x == "kb" or x == "Kb" or x == "mb" or x == "Mb" or x == "gb" or x == "Gb" or x == "tb" or x == "Tb"):
            break
        if (x != "B" or x != "b" or x != "kb" or x != "Kb" or x != "mb" or x != "Mb" or x != "gb" or x != "Gb" or x != "tb" or x != "Tb"):
            x = input("Type a Data Unit(B, Kb, Mb, Gb, Tb)\n")

y = input("To which unit do you want to convert your number?\n")

if (y != "B" or y != "b" or y != "kb" or y != "Kb" or y != "mb" or y != "Mb" or y != "gb" or y != "Gb" or y != "tb" or y != "Tb"):
    while (y != "B" or y != "b" or y != "kb" or y != "Kb" or y != "mb" or y != "Mb" or y != "gb" or y != "Gb" or y != "tb" or y != "Tb"):    
        if (y == "B" or y == "b" or y == "kb" or y == "Kb" or y == "mb" or y == "Mb" or y == "gb" or y == "Gb" or y == "tb" or y == "Tb"):
            break
        if (y != "B" or y != "b" or y != "kb" or y != "Kb" or y != "mb" or y != "Mb" or y != "gb" or y != "Gb" or y != "tb" or y != "Tb"):
            y = input("Type a Data Unit(B, Kb, Mb, Gb, Tb)\n")

# vars x and y will be used to call the conversion functions in the formulas module

# Below there are conditionals that will use the correct conversion function depending on your input

if (x == y):
    sys.exit("Restart the program, converting 2 same units doesn't make sense")

#b2units
if (x == "b" or x == "B"): 
    if (y == "kb" or y == "Kb"):
        formulas.b2kb()
if (x == "b" or x == "B"): 
    if (y == "mb" or y == "Mb"):
        formulas.b2mb()
if (x == "b" or x == "B"):
    if (y == "Gb" or y == "gb"):
        formulas.b2gb()
if (x == "b" or x == "B"):
    if (y == "Tb" or y == "tb"):
        formulas.b2tb()
#kb2units
if (x == "kb" or x == "Kb"): 
    if (y == "B" or y == "b"):
        formulas.kb2b()
if (x == "kb" or x == "Kb"): 
    if (y == "mb" or y == "Mb"):
        formulas.kb2mb()
if (x == "kb" or x == "Kb"):
    if (y == "Gb" or y == "gb"):
        formulas.kb2gb()
if (x == "kb" or x == "Kb"):
    if (y == "Tb" or y == "tb"):
        formulas.kb2tb()
#mb2units
if (x == "mb" or x == "Mb"): 
    if (y == "kb" or y == "Kb"):
        formulas.mb2kb()
if (x == "mb" or x == "Mb"): 
    if (y == "b" or y == "B"):
        formulas.mb2b()
if (x == "mb" or x == "Mb"):
    if (y == "Gb" or y == "gb"):
        formulas.mb2gb()
if (x == "mb" or x == "Mb"):
    if (y == "Tb" or y == "tb"):
        formulas.mb2tb()
#gb2units
if (x == "gb" or x == "Gb"): 
    if (y == "kb" or y == "Kb"):
        formulas.gb2kb()
if (x == "gb" or x == "Gb"): 
    if (y == "mb" or y == "Mb"):
        formulas.gb2mb()
if (x == "gb" or x == "Gb"):
    if (y == "b" or y == "B"):
        formulas.gb2b()
if (x == "gb" or x == "Gb"):
    if (y == "Tb" or y == "tb"):
        formulas.gb2tb()
#tb2units
if (x == "tb" or x == "Tb"): 
    if (y == "kb" or y == "Kb"):
        formulas.tb2kb()
if (x == "tb" or x == "Tb"): 
    if (y == "mb" or y == "Mb"):
        formulas.tb2mb()
if (x == "tb" or x == "Tb"):
    if (y == "Gb" or y == "gb"):
        formulas.tb2gb()
if (x == "tb" or x == "Tb"):
    if (y == "b" or y == "B"):
        formulas.tb2b()