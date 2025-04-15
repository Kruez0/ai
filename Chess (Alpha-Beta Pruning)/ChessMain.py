import pygame as p
import ChessEng, chessAI
import sys
from multiprocessing import Process, Queue

Width = Height = 800
Dimension = 8
squareSize = Height // Dimension
IMAGES = {}
move_width = 250
move_height = Height

def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"ai/期中/Chess/{piece}.png"), (squareSize, squareSize))

def main():
    p.init()
    screen = p.display.set_mode((Width + move_width, Height))
    screen.fill(p.Color("white"))
    clock = p.time.Clock()
    gs = ChessEng.GameState()
    loadImages()  
    move_made = False  
    animate = False  
    ValidMoves = gs.getValidMoves()
    running = True
    SelectedSquare = ()  
    PlayerClick = []  
    GameOver = False
    ai_thinking = False
    MoveUndo = False
    findMove = None
    player_one = False 
    player_two = False
    move_log_font = p.font.SysFont("TimesNewRoman", 20, False, False)


    while running:
        Human = (gs.whiteMoves and player_one) or (not gs.whiteMoves and player_two)
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: 
                    gs.undoMove()
                    move_made = True
                    animate = False
                    GameOver = False
                    if ai_thinking:
                        findMove.terminate()
                        ai_thinking = False
                    MoveUndo = True
                if e.key == p.K_r:  
                    gs = ChessEng.GameState()
                    ValidMoves = gs.getValidMoves()
                    SelectedSquare = ()
                    PlayerClick = []
                    move_made = False
                    animate = False
                    GameOver = False
                    if ai_thinking:
                        findMove.terminate()
                        ai_thinking = False
                    MoveUndo = True
            elif e.type == p.MOUSEBUTTONDOWN:
                if not GameOver:
                    location = p.mouse.get_pos()  
                    c = location[0] // squareSize
                    r = location[1] // squareSize
                    if SelectedSquare == (r, c) or c >= 8:  
                        SelectedSquare = ()
                        PlayerClick = []  
                    else:
                        SelectedSquare = (r, c)
                        PlayerClick.append(SelectedSquare)  
                    if len(PlayerClick) == 2 and Human: 
                        move = ChessEng.Move(PlayerClick[0], PlayerClick[1], gs.board)
                        for i in range(len(ValidMoves)):
                            if move == ValidMoves[i]:
                                gs.makeMove(ValidMoves[i])
                                move_made = True
                                animate = True
                                SelectedSquare = ()  
                                PlayerClick = []
                        if not move_made:
                            PlayerClick = [SelectedSquare]

        if not GameOver and not Human and not MoveUndo:
            if not ai_thinking:
                ai_thinking = True
                return_queue = Queue()  
                findMove = Process(target=chessAI.findBestMove, args=(gs, ValidMoves, return_queue))
                findMove.start()

            if not findMove.is_alive():
                ai_move = return_queue.get()
                if ai_move is None:
                    ai_move = chessAI.findRandomMove(ValidMoves)
                gs.makeMove(ai_move)
                move_made = True
                animate = True
                ai_thinking = False

        if move_made:
            if animate:
                animateMove(gs.move_log[-1], screen, gs.board, clock)
            ValidMoves = gs.getValidMoves()
            move_made = False
            animate = False
            MoveUndo = False

        drawGameState(screen, gs, ValidMoves, SelectedSquare)

        if not GameOver:
            drawMoveLog(screen, gs, move_log_font)

        if gs.checkmate:
            GameOver = True
            if gs.whiteMoves:
                drawEndGameText(screen, "CHECKMATE! BLACK WINS")
            else:
                drawEndGameText(screen, "CHECKMATE! WHITE WINS")

        elif gs.stalemate:
            GameOver = True
            drawEndGameText(screen, "STALEMATE!")

        clock.tick(15)
        p.display.flip()

def drawBoard(screen):
    global colors
    colors = [p.Color("white"), p.Color("pink")]
    for r in range(Dimension):
        for column in range(Dimension):
            color = colors[((r + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * squareSize, r * squareSize, squareSize, squareSize))

def drawGameState(screen, gs, ValidMoves, SelectedSquare):
    drawBoard(screen) 
    highlightSquares(screen, gs, ValidMoves, SelectedSquare)
    drawPieces(screen, gs.board)  

def drawPieces(screen, board):
    for r in range(Dimension):
        for column in range(Dimension):
            piece = board[r][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * squareSize, r * squareSize, squareSize, squareSize))

def highlightSquares(screen, gs, ValidMoves, SelectedSquare):
    if (len(gs.move_log)) > 0:
        last_move = gs.move_log[-1]
        s = p.Surface((squareSize, squareSize))
        s.set_alpha(100)
        s.fill(p.Color('blue'))
        screen.blit(s, (last_move.end_col * squareSize, last_move.end_row * squareSize))
    if SelectedSquare != ():
        r, c = SelectedSquare
        if gs.board[r][c][0] == (
                'w' if gs.whiteMoves else 'b'):  
            s = p.Surface((squareSize, squareSize))
            s.set_alpha(100)  
            s.fill(p.Color('blue'))
            screen.blit(s, (c * squareSize, r * squareSize))
            s.fill(p.Color('yellow'))
            for move in ValidMoves:
                if move.start_row == r and move.start_col == c:
                    screen.blit(s, (move.end_col * squareSize, move.end_row * squareSize))

def drawMoveLog(screen, gs, font):
    move_log_rect = p.Rect(Width, 0, move_width, move_height)
    p.draw.rect(screen, p.Color('black'), move_log_rect)
    move_log = gs.move_log
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = str(i // 2 + 1) + '. ' + str(move_log[i]) + " "
        if i + 1 < len(move_log):
            move_string += str(move_log[i + 1]) + "  "
        move_texts.append(move_string)

    MovesinRow = 1
    padding = 2
    line_spacing = 2
    text_y = padding
    for i in range(0, len(move_texts), MovesinRow):
        text = ""
        for j in range(MovesinRow):
            if i+j < len(move_texts):
                text += move_texts[i+j]

        TextObject = font.render(text, True, p.Color('white'))
        TextLocation = move_log_rect.move(padding, text_y)
        screen.blit(TextObject, TextLocation)
        text_y += TextObject.get_height() + line_spacing


def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvetica", 32, True, False)
    TextObject = font.render(text, False, p.Color("gray"))
    TextLocation = p.Rect(0, 0, Width, Height).move(Width/2 - TextObject.get_width() / 2,Height/2-TextObject.get_height() / 2)
    screen.blit(TextObject, TextLocation)
    TextObject = font.render(text, False, p.Color('black'))
    screen.blit(TextObject, TextLocation.move(2, 2))


def animateMove(move, screen, board, clock):
    global colors
    d_row = move.end_row - move.start_row
    d_col = move.end_col - move.start_col
    framesPerSquare = 10  
    CountFrame = (abs(d_row) + abs(d_col)) * framesPerSquare
    for frame in range(CountFrame + 1):
        r, c = (move.start_row + d_row * frame / CountFrame, move.start_col + d_col * frame / CountFrame)
        drawBoard(screen)
        drawPieces(screen, board)
        color = colors[(move.end_row + move.end_col) % 2]
        end_square = p.Rect(move.end_col * squareSize, move.end_row * squareSize, squareSize, squareSize)
        p.draw.rect(screen, color, end_square)
        if move.piece_captured != '--':
            if move.is_enpassant_move:
                enpassant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = p.Rect(move.end_col * squareSize, enpassant_row * squareSize, squareSize, squareSize)
            screen.blit(IMAGES[move.piece_captured], end_square)
        screen.blit(IMAGES[move.piece_moved], p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))
        p.display.flip()
        clock.tick(200)


if __name__ == "__main__":
    main()