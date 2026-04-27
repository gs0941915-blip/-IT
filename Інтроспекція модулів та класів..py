from colorama import init, Fore, Style

init()

try:
    count = int(input(Fore.CYAN + "Enter a number: "))
    type_box = input(Fore.CYAN + "Enter a type: ")

    print(Fore.GREEN + f"We got {type_box} in {count}")

    parts = int(input(Fore.CYAN + "Enter amount of parts: "))
    part_count = count // parts

    print(Fore.YELLOW + "Parts per box:", part_count)

except ZeroDivisionError:
    print(Fore.RED + "You can't divide by zero")

except ValueError:
    print(Fore.RED + "Invalid input, try again")

except Exception as e:
    print(Fore.RED + "Something went wrong:", e)

finally:
    print(Style.RESET_ALL + "Goodbye")