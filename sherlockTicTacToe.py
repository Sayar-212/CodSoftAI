import tkinter
import re
def printBoard(xState, zState):
    board = []
    for i in range(9):
        if xState[i]:
            board.append('X')
        elif zState[i]:
            board.append('O')
        else:
            board.append(str(i))
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
def checkWin(state):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for win in wins:
        if state[win[0]] and state[win[0]] == state[win[1]] == state[win[2]]:
            return True
    return False
def minimax(xState, zState, depth, alpha, beta, isMaximizing):
    if checkWin(xState):
        return -1
    if checkWin(zState):
        return 1
    if all(xState[i] or zState[i] for i in range(9)):
        return 0
    if isMaximizing:
        maxEval = -float('inf')
        for i in range(9):
            if xState[i] == 0 and zState[i] == 0:
                zState[i] = 1
                eval = minimax(xState, zState, depth + 1, alpha, beta, False)
                zState[i] = 0
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval
    else:
        minEval = float('inf')
        for i in range(9):
            if xState[i] == 0 and zState[i] == 0:
                xState[i] = 1
                eval = minimax(xState, zState, depth + 1, alpha, beta, True)
                xState[i] = 0
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval

def bestMove(xState, zState):
    for i in range(9):
        if xState[i] == 0 and zState[i] == 0:
            zState[i] = 1
            if checkWin(zState):
                return i
            zState[i] = 0
    for i in range(9):
        if xState[i] == 0 and zState[i] == 0:
            xState[i] = 1
            if checkWin(xState):
                xState[i] = 0
                return i
            xState[i] = 0
    bestScore = -float('inf')
    move = 0
    for i in range(9):
        if xState[i] == 0 and zState[i] == 0:
            zState[i] = 1
            score = minimax(xState, zState, 0, -float('inf'), float('inf'), False)
            zState[i] = 0
            if score > bestScore:
                bestScore = score
                move = i
    return move

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    matches_played = 0
    user_wins = 0
    ai_wins = 0
    draws = 0

    print("Welcome to Tic Tac Toe. You are competing against the Best AI in this game. Wish you all the best.")
    
    while True:
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1 
        match_over = False
        
        while not match_over:
            printBoard(xState, zState)
            if turn == 1:
                print(f"{user_name}'s Chance")
                value = int(input("Please enter a value: "))
                if value < 0 or value > 8 or xState[value] or zState[value]:
                    print("Invalid move! Try again.")
                    continue
                xState[value] = 1
            else:
                print("SherlockAI's Chance")
                value = bestMove(xState, zState)
                zState[value] = 1
            
            if checkWin(xState):
                printBoard(xState, zState)
                print(f"{user_name} won the match!")
                user_wins += 1
                match_over = True
            elif checkWin(zState):
                printBoard(xState, zState)
                print("SherlockAI won the match!")
                ai_wins += 1
                match_over = True
            elif all(xState[i] or zState[i] for i in range(9)):
                printBoard(xState, zState)
                print("It's a draw!")
                draws += 1
                match_over = True
            
            turn = 1 - turn
        
        matches_played += 1
        print(f"Matches played: {matches_played}, {user_name} wins: {user_wins}, SherlockAI wins: {ai_wins}, Draws: {draws}")
        
        cont = input("Do you want to play another match? (yes/no): ").strip().lower()
        if cont != 'yes':
            user_win_percentage = (user_wins / matches_played) * 100 if matches_played > 0 else 0
            ai_win_percentage = (ai_wins / matches_played) * 100 if matches_played > 0 else 0
            draw_percentage = (draws / matches_played) * 100 if matches_played > 0 else 0
            print(f"\nFinal Results:\nMatches played: {matches_played}\n{user_name} wins: {user_wins} ({user_win_percentage:.2f}%)\nSherlockAI wins: {ai_wins} ({ai_win_percentage:.2f}%)\nDraws: {draws} ({draw_percentage:.2f}%)")
            print("Thanks for playing!")
            break

