def b2kb():
    try:
        b = input("Express a number in Bytes: ")  
        kb = (int(b) / 1024)
        print("\n" + str(b) + " bytes are " + str(kb) + " Kb :)")
    except ValueError:
        print ("When you type bytes, only integers are allowed")
        exit(1)

def b2mb():
    try:
        b = input("Express a number in Bytes: ")
        mb = (int(b) / 1024 ** 2)
        print("\n" + str(b) + " bytes are " + str(mb) + " Mb :)")
    except ValueError:
        print ("When you type bytes, only integers are allowed")
        exit(1)

def b2gb():
    try:
        b = input("Express a number in Bytes: ")
        gb = (int(b) / 1024 ** 3)
    except ValueError:    
        print ("When you type bytes, only integers are allowed")
        exit(1)

    print("\n" + str(b) + " bytes are " + str(gb) + " Gb :)")

def b2tb():
    try:
        b = input("Express a number in Bytes: ")
        tb = (int(b) / 1024 ** 4)
    except ValueError:    
        print ("When you type bytes, only integers are allowed")
        exit(1)

    print("\n" + str(b) + " bytes are " + str(tb) + " Tb :)")

def kb2b():
    try:
        b = input("Express a number in Kilobytes: ")
        kb = (float(b) * 1024)
        kb = round(kb)
        print("\n" + str(b) + " kilobytes are " + str(kb) + " bytes :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def kb2mb():
    try:
        kb = input("Express a number in Kilobytes: ")
        mb = (float(kb) / 1024)
        print("\n" + str(kb) + " kilobytes are " + str(mb) + " Mb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def kb2gb():
    try:
        kb = input("Express a number in Kilobytes: ")
        gb = (float(kb) / 1024 ** 2)
        print("\n" + str(kb) + " kilobytes are " + str(gb) + " Gb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def kb2tb():
    try:
        kb = input("Express a number in Kilobytes: ")
        tb = (float(kb) / 1024 ** 3)
        print("\n" + str(kb) + " kilobytes are " + str(tb) + " Tb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def mb2kb():
    try:
        mb = input("Express a number in megabytes: ")
        kb = (float(mb) * 1024)
        print("\n" + str(mb) + " megabytes are " + str(kb) + " Kb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def mb2b():
    mb = input("Express a number in megabytes: ")
    try:
        b = (float(mb) * 1024 ** 2)
        b = round(b)
        print("\n" + str(mb) + " megabytes are " + str(b) + " bytes :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def mb2gb():
    try:
        mb = input("Express a number in megabytes: ")
        gb = (float(mb) / 1024)
        print("\n" + str(mb) + " megabytes are " + str(gb) + " Gb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def mb2tb():
    try:
        mb = input("Express a number in megabytes: ")
        tb = (float(mb) / 1024 ** 2)
        print("\n" + str(mb) + " megabytes are " + str(tb) + " Tb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def gb2kb():
    try:
        gb = input("Express a number in Gigabytes: ")
        kb = (float(gb) * 1024 ** 2)
        print("\n" + str(gb) + " gigabytes are " + str(kb) + " Kb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def gb2mb():
    try:
        gb = input("Express a number in Gigabytes: ")
        mb = (float(gb) * 1024)
        print("\n" + str(gb) + " gigabytes are " + str(mb) + " Mb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def gb2b():
    try:
        b = input("Express a number in Gigabytes: ")
        gb = (float(b) * 1024 ** 3)
        gb = round(gb)
        print("\n" + str(b) + " gigabytes are " + str(gb) + " bytes :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def gb2tb():
    try:
        gb = input("Express a number in Gigabytes: ")
        tb = (float(gb) / 1024)
        print("\n" + str(gb) + " gigabytes are " + str(tb) + " Tb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def tb2kb():
    try:
        tb = input("Express a number in Terabytes: ")
        kb = (float(tb) * 1024 ** 3)
        print("\n" + str(tb) + " Terabytes are " + str(kb) + " Kb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def tb2mb():
    try:
        tb = input("Express a number in Terabytes: ")
        mb = (float(tb) * 1024 ** 2)
        print("\n" + str(tb) + " terabytes are " + str(mb) + " Mb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def tb2gb():
    try:
        tb = input("Express a number in Terabytes: ")
        gb = (float(tb) * 1024)
        print("\n" + str(tb) + " Terabytes are " + str(gb) + " Gb :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)

def tb2b():
    try:
        tb = input("Express a number in Terabytes: ")
        b = (float(tb) * 1024 ** 4)
        b = round(b)
        print("\n" + str(tb) + " Terabytes are " + str(b) + " bytes :)")
    except ValueError:
        print("Only numbers are allowed")
        exit(1)