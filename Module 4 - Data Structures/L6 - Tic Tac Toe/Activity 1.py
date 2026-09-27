board = {
    '7':' ',  '8':' ',  '9': ' ',
    '4':' ',  '5':' ',  '6': ' ',
    '1':' ',  '2':' ',  '3': ' ',
}

board_keys = []

for k in board:
    board_keys.append(k)

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = "X"
    count = 0

    for i in range(10):
        print_board(board)
        print(f"It's your turn,{turn}.Make your move:")
        move = input()

        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("Already taken.Choose another spot.")
            continue

        if count >= 5:
            #check across the top row
            if board['7'] == board ['8'] == board['9'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break

            #across the middle
            elif board['4'] == board ['5'] == board['6'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break

            elif board['1'] == board ['2'] == board['3'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break
            elif board['7'] == board ['4'] == board['1'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break
            elif board['8'] == board ['5'] == board['2'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break
            elif board['9'] == board ['6'] == board['3'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break
            elif board['7'] == board ['5'] == board['3'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break
            elif board['1'] == board ['5'] == board['9'] != '' :
                print_board(board)
                print("Game over!")
                print(f"Player {turn} won!")
                break

        if count == 9:
            print("game over")
            print("Its a tie...")   

        turn = "O" if turn == "X" else "X"

    restart = input("Do you wanna play again (y/n:)")
    if restart.lower() == "y" :
        for key in board_keys:
            board[key] = " "
        game()

# Call the game function to start the game

game()


              
