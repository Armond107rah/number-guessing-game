import random


def generate_random_numbers(start_num, end_number):
    """
    Generates number between starting num and ending num passed by the user
    :param start_num: number where randomly generated number should start from
    :param end_number: number where randomly generated number should end to
    :return: randomly generated number between the passed parameter
    """
    return random.randint(start_num, end_number)


def get_starting_ending_num():
    """
    Function to get valid starting and ending numbers from user
    :return: starting_num,ending_num
    """
    while True:
        try:
            starting_num = int(input("Enter starting number:"))
            break
        except ValueError:
            print("Invalid starting number entered, please try again.")
    while True:
        try:
            ending_num = int(input("Enter ending number:"))
            break
        except ValueError:
            print("Invalid ending number entered, please try again.")

    # if starting and ending num are same we will call the same function
    if starting_num == ending_num:
        print("Starting number and ending number cannot be same, please try again..")
        get_starting_ending_num()

    return starting_num, ending_num


def ask_user_number(start_num, end_num):
    """
    Function that takes valid guess from the user
    :return:
    """
    while True:
        try:
            user_num = int(input("Enter your guess :"))

            # checking if user guess is out of bounds or not
            if user_num < start_num or user_num > end_num:
                raise Exception("Guess is out of bounds")
            break
        except ValueError:
            print("Invalid ending number entered, please try again.")
        except Exception:
            print("The number is out of bounds of starting or ending number,please try again.")

    return user_num


def guess_number(random_number, no_of_steps, start_num, end_num,hints):
    """
    Function to check if user guesses the number correctly
    :param random_number: the number to guess
    :param no_of_steps: the number of steps it took to guess correctly
    :param start_num: starting range of randomly generated number
    :param end_num: ending range of randomly generated number
    :param hints: param to check if to turn hints on or off
    :return:
    """
    while True:
        user_guess = ask_user_number(start_num, end_num)

        # MAIN LOGIC FOR GAME
        # if user guess is larger
        if user_guess > random_number:
            if hints == True:
                print("Guess smaller number.")
            else:
                print("Your guess is incorrect. Please try again..")
            no_of_steps = no_of_steps + 1
        # if user guess is smaller
        elif user_guess < random_number:
            if hints == True:
                print("Guess larger number.")
            else:
                print("Your guess is incorrect. Please try again..")

            no_of_steps = no_of_steps + 1
        # else if guess and random number matches
        else:
            print("")
            print("-------------------------------")
            print("Congratulations, you have correctly guessed the number.")
            print(f"You guessed the number in {no_of_steps} guesses.")
            print("-------------------------------")
            print("")
            return


def display_menu():
    print("")
    print("-------------------------------")
    print("1. Start New Game")
    print("2. End Game")
    print("-------------------------------")
    print("")


def main():
    print("WELCOME TO NUMBER GUESSING GAME")
    print("-------------------------------")
    while True:
        display_menu()
        user_option = input("Select option [1,2]: ")

        if user_option == "1":
            user_difficulty = input("Do you want hints [y/n]: ")
            if user_difficulty.lower() == 'n':
                hints = False
            else:
                hints = True

            num_of_steps = 0
            start_num, end_num = get_starting_ending_num()
            master_guess_number = generate_random_numbers(start_num, end_num)
            guess_number(master_guess_number, num_of_steps, start_num, end_num,hints)

        elif user_option == "2":
            print("Thank you for playing...Quitting the game now.")
            break


if __name__ == '__main__':
    main()