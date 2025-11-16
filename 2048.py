import tabulate, random, time

Grid = [[None]*4 for _ in range(4)]
EmptyPlaces = []

def PrintGrid():
    print(tabulate.tabulate(Grid, tablefmt = "grid"))

def GenerateRandomTile():
    global Grid, EmptyPlaces
    if not(EmptyPlaces):
        for i in range(len(Grid)):
            for j in range(len(Grid[0])):
                if not(Grid[i][j]):
                    EmptyPlaces.append((i,j))
    NewTile = random.choice([2,4])
    NewTileIndex = random.choice(EmptyPlaces)
    Grid[NewTileIndex[0]][NewTileIndex[1]] = NewTile
    EmptyPlaces.remove(NewTileIndex)

def MoveUp():
    global Grid, EmptyPlaces
    R = C = len(Grid)
    c = [0]*C
    for i in range(R-2, -1, -1):
        for j in range(C):
            if (i+1, j) in EmptyPlaces:
                continue
            elif (i,j) in EmptyPlaces:
                for k in range(i, i+c[j]+1):
                    Grid[k][j] = Grid[k+1][j]
                    Grid[k+1][j] = None
                    EmptyPlaces.remove((k,j))
                    EmptyPlaces.append((k+1,j))
                c[j] = 0
            else:
                if Grid[i][j] == Grid[i+1][j]:
                    Grid[i][j]*=2
                    Grid[i+1][j] = None
                    EmptyPlaces.append((i+1, j))
                else:
                    c[j]+=1

def MoveDown():
    global Grid, EmptyPlaces
    R = C = len(Grid)
    c = [0]*C
    for i in range(1, R):
        for j in range(C):
            if (i-1, j) in EmptyPlaces:
                continue
            elif (i,j) in EmptyPlaces:
                for k in range(i, i-c[j]-1, -1):
                    Grid[k][j] = Grid[k-1][j]
                    Grid[k-1][j] = None
                    EmptyPlaces.remove((k,j))
                    EmptyPlaces.append((k-1,j))
                c[j] = 0
            else:
                if Grid[i][j] == Grid[i-1][j]:
                    Grid[i][j]*=2
                    Grid[i-1][j] = None
                    EmptyPlaces.append((i-1, j))
                else:
                    c[j]+=1
            
def MoveRight():
    global Grid, EmptyPlaces
    R = C = len(Grid)
    c = [0]*R
    for i in range(R):
        for j in range(1, C):
            if (i, j-1) in EmptyPlaces:
                continue
            elif (i,j) in EmptyPlaces:
                for k in range(j, j-c[i]-1, -1):
                    Grid[i][k] = Grid[i][k-1]
                    Grid[i][k-1] = None
                    EmptyPlaces.remove((i,k))
                    EmptyPlaces.append((i,k-1))
                c[i] = 0
            else:
                if Grid[i][j] == Grid[i][j-1]:
                    Grid[i][j]*=2
                    Grid[i][j-1] = None
                    EmptyPlaces.append((i, j-1))
                else:
                    c[i]+=1

def MoveLeft():
    global Grid, EmptyPlaces
    R = C = len(Grid)
    c = [0]*R
    for i in range(R):
        for j in range(C-2, -1, -1):
            if (i, j+1) in EmptyPlaces:
                continue
            elif (i,j) in EmptyPlaces:
                for k in range(j, j+c[i]+1):
                    Grid[i][k] = Grid[i][k+1]
                    Grid[i][k+1] = None
                    EmptyPlaces.remove((i,k))
                    EmptyPlaces.append((i,k+1))
                c[i] = 0
            else:
                if Grid[i][j] == Grid[i][j+1]:
                    Grid[i][j]*=2
                    Grid[i][j+1] = None
                    EmptyPlaces.append((i, j+1))
                else:
                    c[i]+=1

if __name__ == "__main__":
    print("Welcome to 2048")
    print("I hope the rules are clear")
    print("Otherwise, press\nR to view the rules\nS to start the game")
    choice1 = input().lower()
    if choice1 == "r":
        print("Here are the Rules")
        print("""The game is played on a 4 x 4 grid.\n
                Each turn, the player moves tiles in one of four directions: up, down, left, right.\n
                Tiles with the same value that collide during a move merge into a single tile of double the value.\n
                After each valid move, a new tile (either 2 or 4) appears in a random empty cell.\n
                The game ends when no valid moves are possible.\n""")
    elif choice1!="s": print("\nTry again! Invalid Choice Entered")
    time.sleep(1)
    print("""To move your tiles, enter\n
          u to move up
          d to move down
          r to move right
          l to move left
          e to exit the game\n""")
    time.sleep(1)
    GenerateRandomTile()
    print("This is your starter grid")
    time.sleep(1)
    PrintGrid()
    print("Have fun!")
    while EmptyPlaces:
        Move = input("Enter your move: ").lower()
        match Move:
            case "u":
                MoveUp()
            case "d":
                MoveDown()
            case "r":
                MoveRight()
            case "l":
                MoveLeft()
            case "e":
                print("Thank You for playing 2048")
                break
            case _:
                print("Please enter a valid move")
                continue
        GenerateRandomTile()
        PrintGrid()
    print("Game Over")
