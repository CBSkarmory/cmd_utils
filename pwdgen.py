import random, os

def gen(length):
    tmp = [None] * length
    for c in range(length):
        tmp[c] = chars[random.randint(0,len(chars)-1)]
    return ''.join(tmp)

if __name__ == "__main__":
    print("================================\n   Random Password Generator\n================================")
    print("recommendation: length > 8")
    length = int(input("length:"))
    reps = int(input("reps:"))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    sysout = open("out.txt",'w')#opens out.txt in write mode
    for i in range(reps):
        sysout.write(gen(length))
        sysout.write("\n")
    sysout.close()
    print("\nresults are in out.txt")
    print("close file before you press enter.")
    a = input("press <RET> (enter) to CLEAR FILE and exit")
    sysout = open("out.txt",'w')#opens out.txt in write mode
    sysout.truncate()
    sysout.close()
    os.remove("out.txt")
