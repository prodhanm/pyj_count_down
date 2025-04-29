def countdown(num):
    if num == 0:
        return 0
    if num < 0:
        print(num)
        return countdown(num+1)
    else:
        print(num)
        return countdown(num-1)
    
def main():
    num = int(input("Enter a number: "))
    print("Blastoff: ")
    result = countdown(num)
    print(0)
    print("Countdown complete!")

if __name__ == "__main__":
    main()