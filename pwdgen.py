import random, os, sys

SELF_FILENAME = "pwdgen.py"
OUT_FILE = "generator_out.txt"
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

ERRORCODE_NUM_ARGS = 2
ERRORCODE_PARSEINT = 1

def gen(length):
    tmp= [None] * length #empty array
    for c in range(length):
        tmp[c]= CHARS[random.randint(0,len(CHARS)-1)]
    return ''.join(tmp)

if __name__ == "__main__":
    argv= sys.argv
    argc= len(argv)
    try:
        if argc == 1:
            print("================================\n   Random Password Generator\n================================")
            print("recommendation: length > 8")
            length= int(input("length:"))
            reps= int(input("reps:"))
        elif argc == 3:
            length= int(argv[1])
            reps= int(argv[2])
        else:
            print("[ERROR] Invalid number of arguments")
            print("[NOTE]  Usage is as follows: (python) %s [length] [reps]" % SELF_FILENAME)
            sys.exit(ERRORCODE_NUM_ARGS)
    except ValueError:
        print("[ERROR] Invalid argument detected; expected 2 numbers")
        print(SELF_FILENAME)
        sys.exit(ERRORCODE_PARSEINT)

    sysout= open(OUT_FILE, 'w')#opens out.txt in write mode
    for i in range(reps):
        sysout.write(gen(length))
        sysout.write("\n")
    sysout.close()
    print("\nresults are in %s" % OUT_FILE)
    print("close file before you press enter.")
    a = input("press <RET> (enter) to CLEAR FILE and exit")
    sysout = open(OUT_FILE, 'w')#opens out.txt in write mode
    sysout.truncate()
    sysout.close()
    os.remove(OUT_FILE)
