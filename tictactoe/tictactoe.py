"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    qtdX = 0
    qtdO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                qtdX +=1
            elif board[i][j] == O:
                qtdO += 1
    if qtdX > qtdO:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    gameActions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                gameActions.add((i, j))

    return gameActions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possibleActions = actions(board)
    if action not in possibleActions:
        raise Exception("Invalid movement")

    boardCopy = copy.deepcopy(board)
    i, j = action
    boardCopy[i][j] = player(board)

    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    try:
    #check line
        for i in range(3):
            qtdX = 0
            qtdO = 0
            for j in range(3):
                if board[i][j] == X:
                    qtdX += 1
                elif board[i][j] == O:
                    qtdO += 1
            if qtdX == 3:
                return X
            elif qtdO == 3:
                return O


        #check column
        for j in range(3):
            qtdX = 0
            qtdO = 0
            for i in range(3):
                if board[i][j] == X:
                    qtdX += 1
                elif board[i][j] == O:
                    qtdO += 1
            if qtdX == 3:
                return X
            elif qtdO == 3:
                return O

        #check first diagonal
        qtdX = 0
        qtdO = 0
        for i in range(3):
            if board[i][i] == X:
                qtdX += 1
            elif board[i][i] == O:
                qtdO += 1
        if qtdX == 3:
                return X
        elif qtdO == 3:
            return O

        #check second diagonal
        qtdX = 0
        qtdO = 0
        for i in range(3):
            if board[i][2 - i] == X:
                qtdX += 1
            elif board[i][2 - i] == O:
                qtdO += 1
        if qtdX == 3:
                return X
        elif qtdO == 3:
            return O

        return None

    except: NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board, is_root=True):
    if terminal(board):
        if is_root:
            return None
        else:
            return utility(board)

    current_player = player(board)
    melhorAcao = None

    if current_player == X:
        melhorJogo = -math.inf
        for action in actions(board):
            copyBoard = result(board, action)
            value = minimax(copyBoard, False)
            if value > melhorJogo:
                melhorJogo = value
                melhorAcao = action
    else:
        melhorJogo = math.inf
        for action in actions(board):
            copyBoard = result(board, action)
            value = minimax(copyBoard, False)
            if value < melhorJogo:
                melhorJogo = value
                melhorAcao = action

    if is_root:
        return melhorAcao  
    else:
        return melhorJogo  
