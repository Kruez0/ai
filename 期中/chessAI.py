import random

pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "P": 1}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3

pawnScores = [
    [0.8, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.8],
    [0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75],
    [0.3, 0.35, 0.4, 0.5, 0.5, 0.4, 0.35, 0.3],
    [0.25, 0.3, 0.35, 0.45, 0.45, 0.35, 0.3, 0.25],
    [0.2, 0.25, 0.3, 0.4, 0.4, 0.3, 0.25, 0.2],
    [0.25, 0.2, 0.15, 0.2, 0.2, 0.15, 0.2, 0.25],
    [0.2, 0.3, 0.35, 0.0, 0.0, 0.35, 0.3, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
]

bishopScores = [
    [0.0, 0.2, 0.25, 0.2, 0.2, 0.25, 0.2, 0.0],
    [0.2, 0.3, 0.35, 0.4, 0.4, 0.35, 0.3, 0.2],
    [0.25, 0.35, 0.5, 0.55, 0.55, 0.5, 0.35, 0.25],
    [0.2, 0.4, 0.55, 0.6, 0.6, 0.55, 0.4, 0.2],
    [0.2, 0.4, 0.6, 0.65, 0.65, 0.6, 0.4, 0.2],
    [0.25, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.25],
    [0.2, 0.35, 0.4, 0.45, 0.45, 0.4, 0.35, 0.2],
    [0.0, 0.2, 0.25, 0.2, 0.2, 0.25, 0.2, 0.0]
]
horseScores = [
    [0.0, 0.1, 0.15, 0.2, 0.2, 0.15, 0.1, 0.0],
    [0.1, 0.25, 0.45, 0.5, 0.5, 0.45, 0.25, 0.1],
    [0.15, 0.45, 0.6, 0.65, 0.65, 0.6, 0.45, 0.15],
    [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
    [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
    [0.15, 0.45, 0.6, 0.65, 0.65, 0.6, 0.45, 0.15],
    [0.1, 0.25, 0.45, 0.5, 0.5, 0.45, 0.25, 0.1],
    [0.0, 0.1, 0.15, 0.2, 0.2, 0.15, 0.1, 0.0]
]
rookScores = [
    [0.25, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.25],
    [0.3, 0.5, 0.55, 0.55, 0.55, 0.55, 0.5, 0.3],
    [0.3, 0.4, 0.45, 0.45, 0.45, 0.45, 0.4, 0.3],
    [0.3, 0.4, 0.45, 0.45, 0.45, 0.45, 0.4, 0.3],
    [0.3, 0.4, 0.45, 0.45, 0.45, 0.45, 0.4, 0.3],
    [0.3, 0.4, 0.45, 0.45, 0.45, 0.45, 0.4, 0.3],
    [0.3, 0.5, 0.55, 0.55, 0.55, 0.55, 0.5, 0.3],
    [0.25, 0.3, 0.3, 0.4, 0.4, 0.3, 0.3, 0.25]
]

queenScores = [
    [0.0, 0.2, 0.25, 0.3, 0.3, 0.25, 0.2, 0.0],
    [0.2, 0.4, 0.45, 0.45, 0.45, 0.45, 0.4, 0.2],
    [0.25, 0.45, 0.5, 0.55, 0.55, 0.5, 0.45, 0.25],
    [0.3, 0.45, 0.55, 0.6, 0.6, 0.55, 0.45, 0.3],
    [0.3, 0.45, 0.6, 0.6, 0.6, 0.6, 0.45, 0.3],
    [0.25, 0.55, 0.6, 0.6, 0.6, 0.6, 0.55, 0.25],
    [0.2, 0.4, 0.5, 0.45, 0.45, 0.4, 0.4, 0.2],
    [0.0, 0.2, 0.25, 0.3, 0.3, 0.25, 0.2, 0.0]
]



piece_positionScores = {"wN": horseScores,
                         "bN": horseScores[::-1],
                         "wB": bishopScores,
                         "bB": bishopScores[::-1],
                         "wQ": queenScores,
                         "bQ": queenScores[::-1],
                         "wR": rookScores,
                         "bR": rookScores[::-1],
                         "wP": pawnScores,
                         "bP": pawnScores[::-1]}


def findBestMove(gs, ValidMoves, return_queue):
    global next_move
    next_move = None
    random.shuffle(ValidMoves)
    findMoveNegaMaxAlphaBeta(gs, ValidMoves, DEPTH, -CHECKMATE, CHECKMATE,1 if gs.whiteMoves else -1)
    return_queue.put(next_move)


def findMoveNegaMaxAlphaBeta(gs, ValidMoves, depth, alpha, beta, turn_multiplier):
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(gs)
    maxScore = -CHECKMATE
    for move in ValidMoves:
        gs.makeMove(move)
        next_moves = gs.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(gs, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                next_move = move
        gs.undoMove()
        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta:
            break
    return maxScore

def findRandomMove(ValidMoves):
    return random.choice(ValidMoves)

def scoreBoard(gs):
    if gs.checkmate:
        if gs.whiteMoves:
            return -CHECKMATE  
        else:
            return CHECKMATE  
    elif gs.stalemate:
        return STALEMATE
    score = 0
    for r in range(len(gs.board)):
        for c in range(len(gs.board[r])):
            piece = gs.board[r][c]
            if piece != "--":
                piece_positionScore = 0
                if piece[1] != "K":
                    piece_positionScore = piece_positionScores[piece][r][c]
                if piece[0] == "w":
                    score += pieceScore[piece[1]] + piece_positionScore
                if piece[0] == "b":
                    score -= pieceScore[piece[1]] + piece_positionScore

    return score