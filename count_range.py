def count_range(n):
    if n == 0:
        return [0]
    elif n < 0:
        return count_range(n + 1) + [n]
    else:
        return count_range(n - 1) + [n]

def main():
    num = int(input("Enter a number: "))
    print("Blastoff: ")
    result = count_range(num)
    print(result)
    print("Countdown complete!")

if __name__ == "__main__":
    main()