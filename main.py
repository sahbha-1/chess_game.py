import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move
from piece import Piece
from board import Board

class Main:
    
	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.screen = pygame.display.set_mode((WIDTH+600, HEIGHT))
		pygame.display.set_caption('Chess')
		self.game = Game()
		self.surface = pygame.Surface((WIDTH+600, HEIGHT), pygame.SRCALPHA)
		self.background = pygame.Surface((WIDTH+600, HEIGHT))

	def mainloop(self):
		screen = self.screen
		game = self.game
		board = self.game.board
		dragger = self.game.dragger
		surface = self.surface
		background = self.background

		clicked_row = dragger.mouseY // SQSIZE
		clicked_col = dragger.mouseX // SQSIZE

		piece = board.squares[clicked_row][clicked_col].piece

		while True:
			# show methods
			screen.blit(background, (0,0))
			game.show_bg(screen)
			game.show_last_move(screen)
			screen.blit(surface, (0, 0))
			game.show_moves(surface)
			game.show_pieces(screen)
			game.show_side_bar(background)
			game.show_coordinates(screen)

			game.show_hover(screen)

			if dragger.dragging:
				dragger.update_blit(screen)

			for event in pygame.event.get():
				
				# click event
				if event.type == pygame.MOUSEBUTTONDOWN:

					dragger.update_mouse(event.pos)

					if dragger.mouseX < 800:

						clicked_row = dragger.mouseY // SQSIZE
						clicked_col = dragger.mouseX // SQSIZE

					else: 
						break

					# checking if clicked square has a valid move in it
					
					if board.squares[clicked_row][clicked_col].isempty():
						for move in piece.moves:
							if clicked_row == move.final.row:
								if clicked_col == move.final.col:
									if board.valid_move(piece, move):
										captured = False

										# make move
										board.move(piece, move)
										piece.moved = True

										board.set_true_en_passant(piece)

										# sounds
										game.play_sound(captured)
										# show methods
										game.show_bg(screen)
										game.show_bg(surface)
										game.show_last_move(surface)
										game.show_last_move(screen)
										game.show_pieces(screen)
										game.show_pieces(surface)
										game.show_coordinates(screen)
										# next turn							
										game.next_turn()
									piece.clear_moves()
								# hide possible moves
								else:
									game.show_bg(screen)
									game.show_bg(surface)
									game.show_last_move(surface)
									game.show_last_move(screen)
									game.show_pieces(screen)
									game.show_pieces(surface)
									game.show_coordinates(screen)
							# hide possible moves
							else:
								game.show_bg(screen)
								game.show_bg(surface)
								game.show_last_move(surface)
								game.show_last_move(screen)
								game.show_pieces(screen)
								game.show_pieces(surface)
								game.show_coordinates(screen)

					# checking if clicked square has a valid move in it where it captures a piece
					if board.squares[clicked_row][clicked_col].has_enemy_piece(game.next_player):
						for move in piece.moves:
							if clicked_row == move.final.row:
								if clicked_col == move.final.col:
									if board.valid_move(piece, move):	

										# normal moves									
										captured = board.squares[clicked_row][clicked_col].has_piece()
										captured_piece = board.squares[clicked_row][clicked_col].piece
										if board.squares[clicked_row][clicked_col].has_enemy_piece(piece.color):
											game.show_side_bar(background)
											game.show_side_bar(surface)
											game.add_captured(captured_piece)
											game.show_captured(surface, captured_piece)
										# make move
										board.move(piece, move)
										piece.moved = True

										board.set_true_en_passant(piece)

										# sounds
										game.play_sound(captured)
										# show methods
										game.show_bg(screen)
										game.show_bg(surface)
										game.show_last_move(surface)
										game.show_last_move(screen)
										game.show_pieces(screen)
										game.show_pieces(surface)
										game.show_coordinates(screen)
										# next turn							
										game.next_turn()
									piece.clear_moves()
								# hide possible moves
								else:
									game.show_bg(screen)
									game.show_bg(surface)
									game.show_last_move(surface)
									game.show_last_move(screen)
									game.show_pieces(screen)
									game.show_pieces(surface)
									game.show_coordinates(screen)
							# hide possible moves
							else:
								game.show_bg(screen)
								game.show_bg(surface)
								game.show_last_move(surface)
								game.show_last_move(screen)
								game.show_pieces(screen)
								game.show_pieces(surface)
								game.show_coordinates(screen)

					# if the clicked square has a piece
					if board.squares[clicked_row][clicked_col].has_piece():
						piece = board.squares[clicked_row][clicked_col].piece						
						piece.clear_moves()
						# valid piece (color)?
						if piece.color == game.next_player:
												
							
							board.calc_moves(piece, clicked_row, clicked_col, bool=True)
							dragger.save_initial(event.pos)
							dragger.drag_piece(piece)
							# show methods
							screen.blit(background, (0, 0))
							screen.blit(surface, (0, 0))
							game.show_bg(screen)
							game.show_bg(surface)
							game.show_highlighted_piece(screen)
							game.show_highlighted_piece(surface)
							game.show_last_move(surface)
							game.show_last_move(screen)
							game.show_coordinates(screen)
							game.show_moves(surface)
							game.show_pieces(screen)
						

				# mouse motion event
				elif event.type == pygame.MOUSEMOTION:
					motion_row = event.pos[1] // SQSIZE
					motion_col = event.pos[0] // SQSIZE
					
					
					if motion_row >= 0:
						if motion_col >= 0:
							if motion_row <= 7:
								if motion_col <= 7:
									game.set_hover(motion_row, motion_col)

					if dragger.dragging:
						board.calc_moves(piece, clicked_row, clicked_col)
						dragger.update_mouse(event.pos)
						# show methods
						screen.blit(background, (0, 0))
						game.show_bg(screen)
						game.show_highlighted_piece(screen)
						game.show_highlighted_piece(surface)
						game.show_last_move(screen)
						screen.blit(surface, (0, 0))						
						game.show_moves(surface)
						game.show_pieces(screen)
						game.show_coordinates(screen)
						game.show_hover(screen)
						dragger.update_blit(screen)

				# click release event
				elif event.type == pygame.MOUSEBUTTONUP:
					
					if dragger.dragging:

						released_row = dragger.mouseY // SQSIZE
						released_col = dragger.mouseX // SQSIZE

						# create possible move
						initial = Square(dragger.initial_row, dragger.initial_col)
						final = Square(released_row, released_col)
						move = Move(initial, final)

						game.show_bg(surface)
						game.show_coordinates(surface)

						# valid move?
						if board.valid_move(dragger.piece, move):
							# normal captures
							captured = board.squares[released_row][released_col].has_piece()
							captured_piece = board.squares[released_row][released_col].piece
							if board.squares[released_row][released_col].has_enemy_piece(piece.color):
								game.show_side_bar(background)
								game.show_side_bar(surface)
								game.add_captured(captured_piece)
								game.show_captured(surface, captured_piece)								
								
							board.move(dragger.piece, move)
							piece.moved = True

							board.set_true_en_passant(dragger.piece)
							# sounds
							game.play_sound(captured)
							# show methods
							game.show_bg(screen)
							game.show_bg(surface)
							game.show_last_move(surface)
							game.show_last_move(screen)
							game.show_pieces(screen)
							game.show_coordinates(screen)
							if board.squares[released_row][released_col].has_enemy_piece(piece.color):
								game.show_side_bar(background)
								game.show_side_bar(surface)
								game.add_captured(captured_piece)
								game.show_captured(surface, captured_piece)
							# next turn							
							game.next_turn()
							piece.clear_moves()
						else:
							game.show_bg(screen)
							game.show_bg(surface)
							game.show_highlighted_piece(screen)
							game.show_highlighted_piece(surface)
							game.show_last_move(screen)
							game.show_last_move(surface)
							game.show_pieces(screen)
							game.show_moves(surface)
							game.show_coordinates(screen)
						dragger.update_mouse(event.pos)
					dragger.undrag_piece()

				# key press
				elif event.type == pygame.KEYDOWN:

					# changing themes
					if event.key == pygame.K_t:
						game.change_theme()
						game.show_bg(screen)
						game.show_bg(surface)
						game.show_last_move(screen)
						game.show_last_move(surface)
						game.show_pieces(screen)
						game.show_coordinates(screen)

					# restart game
					if event.key == pygame.K_r:
						game.reset()
						game = self.game
						board = self.game.board
						dragger = self.game.dragger
						game.show_bg(screen)
						game.show_bg(surface)
						game.clear_captured()
						game.show_coordinates(screen)
						game.show_side_bar(screen)
						game.show_side_bar(surface)
						
				# quit application
				elif event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()

main = Main()
main.mainloop()