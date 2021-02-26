from app import conversion_calcs


def main():
    while True:
        x = input("Enter a base 10 integer: ")
        try:
            print(binary_convert(x))
        except ValueError:
            print("This program only accepts integers. Please enter a valid number.")
            continue

        while True:
            response = input("Would you like to enter another integer? Enter 'y' or 'n': ")
            if response == "y":
                break
            elif response == "n":
                print("Program ending.")
                exit()
            else:
                print("That was not a valid input. Please try again")
                continue


def binary_convert(base10: int) -> str:
    """Convert base10 into a signed binary integer

    param base10: int
    return: str
    """
    num = int(base10)
    if num == 0:
        return 0
    elif num < 0:
        binary = conversion_calcs.find_binary(-num)
        return int(conversion_calcs.twos_complement(binary))
    else:
        binary = conversion_calcs.find_binary(num)
        return int(binary)


if __name__ == "__main__":
    main()
