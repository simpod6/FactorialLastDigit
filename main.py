from LastFactDigit import LastFactDigit

def main():    
    while 1==1:
        num = int(input("Num: "))
        if num == 0:
            break
        n = LastFactDigit.calcLastFactDigit(num)
        print("The last non zero digit of {}! is: {}".format(num, int(n)))


if __name__ == "__main__":
    main()
