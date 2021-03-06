class TicTacToe:
    def __init__(self):
        """ build initial empty 3x3 grid for game"""


        row = ["-", "-", "-"]
        # important to use [:] to make a copy of the row each time use
        # in overall grid, otherwise changing a value in one row would
        # change it in all 3!
        self.grid = [row[:], row[:], row[:]]    

    def __str__(self):
        """ create and return formatted string to represent grid
        use "-" for empty square, X/O if already selected """
        print("printing board using __str__ method")
        s = "\n"
        for i in range(3):
            for j in range(3):
                s += " "+self.grid[j][i]+" "
            s += "\n"
        s += "\n"
        return s

    def printBoard(self):
        """ print game grid, 
        use "-" for empty square, X/O if already selected """
        print("printing board using printBoard method")
        print()
        for i in range(3):
            for j in range(3):
                print(self.grid[j][i])
        print()

    # you fix: can we combine playerXTurn and playerYTurn?  They are almost the
    # exact same code!
    def playerXTurn(self):
        """ inputs position X will play and sets grid at that position to "X" """
        # currently no check if move is valid - you can add
        x,y = input("enter coordinates of square to play in form 'x y'").split()
        self.grid[int(x)][int(y)] = "X"

    def playerYTurn(self):
        """ inputs position O will play and sets grid at that position to 'O' """
        # currently no check if move is valid - you can add
        x,y = input("enter coordinates of square to play in form 'x y'").split()
        self.grid[int(x)][int(y)] = "O"

    def isWon(self):
        """ you implement how makes sense to you """
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] and self.grid[0][0] != "_":
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0] and self.grid[0][0] != "_":


        




            return True
        return False
    

def main():
    # example code to show use of class functions
    #for i in range

    ttt = TicTacToe()
    print(ttt)
   
    ttt.playerXTurn()
    print(ttt)
    ttt.playerYTurn()
    print(ttt)
    print("game won?", ttt.isWon())
    while not ttt.isWon():
        print(ttt)
        ttt = TicTacToe()
        ttt.playerXTurn()
        print(ttt)
        ttt.playerYTurn()
        print(ttt)
        print("game won?", ttt.isWon())
        if ttt.isWon():
            print("Player X wins")
            break
    # you implement: game loop, alternate turns between player "X" and player "O"
    # until someone wins, then print out which player won ("X" or "O")
    # if get that working, add ability to handle a tie game
 
main()
