import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8

}

symbol_values = {
    "A":5,
    "B":4,
    "C":3,
    "D":2

}


def check_winnings(colums, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = colums[0][line]
        for colum in colums:
            symbol_to_check = colum[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    colums = []
    for _ in range(cols):
        colum = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            colum.append(value)

        colums.append(colum)

    return colums

def print_slots_machine(colums):
    for row in range(len(colums[0])):
        for i, column in enumerate(colums):
            if i != len(colums) - 1:
               print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please ebter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1_"  + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please ebter a number")

    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each lines ? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number")

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines}. Total bet is equal to: {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slots_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You Won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to Play (q to Quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()

