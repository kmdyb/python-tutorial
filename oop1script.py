from oop1 import RocketBoard


board = RocketBoard(3)

# board.rockets[0].pos_y = 5
print("\nWywołanie board.rockets[0]")
print(board.rockets[0])
print("\nWywołanie board[0]")
print(board[0])         # __getitem__ does the work here

print("\nUstawiam paliwo rakiety pierwszej")
board[0] = 60        # item assignment thanks to __setitem__
print(board[0])
board[0].start()
print(board[0])

print("\nDystans między rakietami 2 i 3: ", board.get_distance(board[1], board[2]))
print("Przesuwam rakietę drugą w bok o trzy jednostki")
board[1].pos_x = 3
print("Dystans między rakietami 2 i 3: ", board.get_distance(board[1], board[2]))

print("Wielkość tablicy z rakietami:", len(board))
