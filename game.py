import pygame

from const import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square
from piece import *


class Game:
                
    def __init__(self):
                self.next_player = 'white'
                self.hovered_sqr = None
                self.board = Board()
                self.dragger = Dragger()
                self.config = Config()
                self.captured_pieces_white = []
                self.captured_pieces_black = []
                self.piece_types_white = 0
                self.piece_types_black = 0
                self.center_white = 840
                self.center_black = 840

            # blit methods

    def show_bg(self, surface):
        theme = self.config.theme

        for row in range(ROWS):
            for col in range(COLS):
                # color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_side_bar(self, surface):
        # color
        color = (49, 46, 43)
        # rect
        rect = (800, 0, 600, 800)
        # blit
        pygame.draw.rect(surface, color, rect)

    def show_coordinates(self, surface):
        theme = self.config.theme
        x = 80
        y = 780
        _x = 10
        _y = 710
        for col in range(COLS):
            # color
            color = theme.bg.light if col % 2 == 0 else theme.bg.dark
            # font
            font = self.config.font.render(chr(ord('a') + col), True, color)
            # blit
            surface.blit(font, (x, y))
            x += SQSIZE
        for row in range(ROWS):
            # color
            color = theme.bg.light if row % 2 == 0 else theme.bg.dark
            # font
            font = self.config.font.render(chr(ord('1') + row), True, color)
            # blit
            surface.blit(font, (_x, _y))
            _y -= SQSIZE

        
    
    def show_pieces(self, surface):
        for row in range(ROWS):
                for col in range(COLS):
                    # has piece ?
                    if self.board.squares[row][col].has_piece():
                        piece = self.board.squares[row][col].piece

                        # all pieces except dragger
                        if piece is not self.dragger.piece:
                            piece.set_texture(size=90)
                            img = pygame.image.load(piece.texture)
                            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                            piece.texture_rect = img.get_rect(center=img_center)
                            surface.blit(img, piece.texture_rect)

    
    def show_captured(self, surface, piece):        
        self.center_white = 840
        self.center_black = 840

        # white captured
        for item in self.captured_pieces_white:
            if isinstance(item, Pawn):
                self.axis = 100
                self.center_white += 20
                Pawn.set_texture(Pawn('white'), size=40)
                img = pygame.image.load(Pawn('white').texture)
                img_center = self.center_white, self.axis
                Pawn.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Pawn.texture_rect)

        white_first_time = True

        for item in self.captured_pieces_white:            
            if isinstance(item, Knight):
                if white_first_time == True:
                    self.center_white += 50
                self.axis = 100
                self.center_white += 20
                Knight.set_texture(Knight('white'), size=40)
                img = pygame.image.load(Knight('white').texture)
                img_center = self.center_white, self.axis
                Knight.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Knight.texture_rect)
                white_first_time = False
        
        white_first_time = True
                
        for item in self.captured_pieces_white:
            if isinstance(item, Bishop):
                if white_first_time == True:
                    self.center_white += 50
                self.axis = 100
                self.center_white += 20
                Bishop.set_texture(Bishop('white'), size=40)
                img = pygame.image.load(Bishop('white').texture)
                img_center = self.center_white, self.axis
                Bishop.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Bishop.texture_rect)
                white_first_time = False
        
        white_first_time = True
    
        for item in self.captured_pieces_white:
            if isinstance(item, Rook):
                if white_first_time == True:
                    self.center_white += 50
                self.axis = 100
                self.center_white += 20
                Rook.set_texture(Rook('white'), size=40)
                img = pygame.image.load(Rook('white').texture)
                img_center = self.center_white, self.axis
                Rook.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Rook.texture_rect)
                white_first_time = False
        
        white_first_time = True

        for item in self.captured_pieces_white:
            if isinstance(item, Queen):
                if white_first_time == True:
                    self.center_white += 50
                self.axis = 100
                self.center_white += 20
                Queen.set_texture(Queen('white'), size=40)
                img = pygame.image.load(Queen('white').texture)
                img_center = self.center_white, self.axis
                Queen.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Queen.texture_rect)
                white_first_time = False

        # black captured

        for item in self.captured_pieces_black:
            if isinstance(item, Pawn):
                self.axis = 700
                self.center_black += 20
                Pawn.set_texture(Pawn('black'), size=40)
                img = pygame.image.load(Pawn('black').texture)
                img_center = self.center_black, self.axis
                Pawn.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Pawn.texture_rect)
        
        black_first_time = True
                        
        for item in self.captured_pieces_black:            
            if isinstance(item, Knight):
                if black_first_time == True:
                    self.center_black += 50                    
                self.axis = 700
                self.center_black += 20
                Knight.set_texture(Knight('black'), size=40)
                img = pygame.image.load(Knight('black').texture)
                img_center = self.center_black, self.axis
                Knight.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Knight.texture_rect)                
                black_first_time = False
            
        black_first_time = True

        for item in self.captured_pieces_black:
            if isinstance(item, Bishop):
                if black_first_time == True:
                    self.center_black += 50
                self.axis = 700
                self.center_black += 20
                Bishop.set_texture(Bishop('black'), size=40)
                img = pygame.image.load(Bishop('black').texture)
                img_center = self.center_black, self.axis
                Bishop.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Bishop.texture_rect)
                black_first_time = False

        black_first_time = True
    
        for item in self.captured_pieces_black:
            if isinstance(item, Rook):
                if black_first_time == True:
                    self.center_black += 50
                self.axis = 700
                self.center_black += 20
                Rook.set_texture(Rook('black'), size=40)
                img = pygame.image.load(Rook('black').texture)
                img_center = self.center_black, self.axis
                Rook.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Rook.texture_rect)
                black_first_time = False

        black_first_time = True

        for item in self.captured_pieces_black:
            if isinstance(item, Queen):        
                if black_first_time == True:
                    self.center_black += 50     
                self.axis = 700
                self.center_black += 20
                Queen.set_texture(Queen('black'), size=40)
                img = pygame.image.load(Queen('black').texture)
                img_center = self.center_black, self.axis
                Queen.texture_rect = img.get_rect(center=img_center)
                surface.blit(img, Queen.texture_rect)
                black_first_time = False

    def show_highlighted_piece(self, surface):
        theme = self.config.theme
        
        if self.dragger.dragging:
            piece = self.dragger.piece

        for move in piece.moves:
            color = color = theme.trace.light if (move.initial.row + move.initial.col) % 2 == 0 else theme.trace.dark

            rect = (move.initial.col * SQSIZE, move.initial.row * SQSIZE, SQSIZE, SQSIZE)

            pygame.draw.rect(surface, color, rect)

    def show_moves(self, surface):
        theme = self.config.theme

        if self.dragger.dragging:
            piece = self.dragger.piece

            # loop all valid moves

            for move in piece.moves:
                if self.board.squares[move.final.row][move.final.col].isempty():        
                    # circ
                    circ = (move.final.col * SQSIZE + SQSIZE // 2, move.final.row * SQSIZE + SQSIZE // 2)
                    # blit
                    pygame.draw.circle(surface, (0, 0, 0, 50), circ, 20)

                else:
                    # circ
                    circ = (move.final.col * SQSIZE + SQSIZE // 2, move.final.row * SQSIZE + SQSIZE // 2)
                    # blit
                    pygame.draw.circle(surface, (0, 0, 0, 50), circ, 50, 8)

    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect 
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=4)

    # other methods

    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'
    
    def add_captured(self, piece):        
        if piece.color == 'white':
            self.captured_pieces_white.append(piece)
        else:
            self.captured_pieces_black.append(piece)
    
    def clear_captured(self):
        self.captured_pieces_white = []
        self.captured_pieces_black = []

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()
    
    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    def reset(self):
        self.__init__()