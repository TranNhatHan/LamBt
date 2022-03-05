import pygame

def knight_tour(n):
	board = [[0 for i in range(n)] for j in range(n)]
	knight_move(n, board)
	k = 1
	moves = []
	if board[0][0] == 0:
		print("Không thể thực hiện bài toán này!")
		return
	while k <= n*n:
		for i in range(n):
			for j in range(n):
				if board[i][j] == k:
					moves.append([i,j])
					k += 1
	display_board(n, moves)

def knight_move(n , board, x = 0, y = 0, count = 1):
	if count > n*n:
		return True
	if x < 0 or x >= n or y < 0 or y >= n or board[x][y] != 0:
		return False
	board[x][y] = count
	for x_move, y_move in zip([-2, -2, -1, -1,  1, 1,  2, 2] , [-1,  1, -2,  2, -2, 2, -1, 1]):
		if knight_move(n, board, x + x_move, y + y_move , count + 1):
			return True
	board[x][y] = 0
	return False

def display_board(n, moves):
	pygame.init()
	knight = pygame.image.load("Image/knight.png")
	background = pygame.image.load("Image/chess_board.png")
	icon = pygame.image.load("Image/knight_icon.png")
	screen = pygame.display.set_mode((n*32, n*32))
	pygame.display.set_caption("Knight's Tour")
	pygame.display.set_icon(icon)

	# Text:
	index = 0
	running = True
	font = pygame.font.SysFont("Times New Roman",16)
	text = []
	surface = []

	while running:
		screen.blit(background,(0,0))

		if index < n*n:
			screen.blit(knight, (moves[index][1]*32, moves[index][0]*32))
			text.append(font.render(str(index+1),True,(255,255,255)))
			surface.append(text[index].get_rect())
			surface[index].center = (moves[index][1]*32+16, moves[index][0]*32+16)
			index += 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for i in range(index):
			screen.blit(text[i],surface[i])

		pygame.display.update()
		pygame.time.wait(250)

knight_tour(8)

