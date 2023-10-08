'''
File: battleship.py
Author: Pri Vaghela (CSC 120, 4:00 pm)
Description: The program runs a simulation of the battleship board game,
however it only models one player's side with their battleships and another
player's guesses. It inputs two files for this purpose, one with the battleship
locations and another with the opponent's guesses. 
'''

import sys
# to terminate the program when there are errors

class GridPos:
    '''
    The class GridPos represents the position of the grid with the x,y 
    coordinates, the ship and the guess boolean.
    '''
    def __init__(self, x, y):
        '''
        intializes the x coordinate, the y coordinate, ship and  guess
        '''
        self._x = x
        self._y = y
        self._ship = None
        self._guess = False

    def __str__(self):
        '''
        the str method defines a string representation for a GridPos instance
        '''
        return f"({self._x}, {self._y})"

    def __repr__(self):
        '''
        the repr method defines a string representation for a GridPos instance
        '''
        return self.__str__()

class Ship:
    '''
    The class Ship creates an object that represents a battleship.
    '''
    # a global class dictionry of the battleship abbreviations and their
    # names and sizes
    SHIP_INFO = {
        'A': ("Aircraft carrier", 5),
        'B': ("Battleship", 4),
        'S': ("Submarine", 3),
        'D': ("Destroyer", 3),
        'P': ("Patrol boat", 2)
    }

    def __init__(self, abbreviation, positions):
        '''
        intializes the ship type, size, positions and hits to the ship
        '''
        self._kind, self._size = self.SHIP_INFO[abbreviation]
        self._positions = positions
        self._hits = 0

    def __str__(self):
        '''
        the str method defines a string representation for a Ship instance
        '''
        return f"{self._kind} ({self._size})"

    def __repr__(self):
        '''
        the repr method defines a string representation for a Ship instance
        '''
        return self.__str__()

class Board:
    '''
    The class Board creates an object that represents the battleship board.
    '''
    def __init__(self, placement_file):
        '''
        initializes the grid and appends rows to it. Also intializes the ships
        list.
        '''
        self._grid = []
        for x in range(10):
            row = []
            for y in range(10):
                row.append(GridPos(x, y))
            self._grid.append(row)
        self._ships = []
        self.load_placement(placement_file)

    def load_placement(self, placement_file):
        '''
        The method load_placement reads in a placement file and creates Ship 
        objects and stores them in the self._ships list. The placement file 
        specifies the positions and types of each ship to be placed on the 
        board.
        placement_file - this parameter takes in the placement_file from the
        user.
        '''
        file = open(placement_file, 'r')
        lines = file.readlines()

        if len(lines) != 5:
            # Checking if there are exactly 5 lines in the placement file.
            print("ERROR: fleet composition incorrect")
            sys.exit(0)

        for line in lines:
            # Looping over the lines in the placement file.
            line = line.strip()
            abbreviation, x1, y1, x2, y2 = line.split()
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            if x1 < 0 or x1 > 9 or x2 < 0 or x2 > 9 or \
                y1 < 0 or y1 > 9 or y2 < 0 or y2 > 9:
                # checks if ship is out of bounds 
                print(f"ERROR: ship out-of-bounds: {line}")
                sys.exit(0)

            if x1 != x2 and y1 != y2:
                # checks if ship is diagonal  
                print(f"ERROR: ship not horizontal or vertical: {line}")
                sys.exit(0)

            # calculate the size of the ship based on its coordinates
            size = abs(x2 - x1) + abs(y2 - y1) + 1
            # retrieve the name and expected size of the ship based on its 
            # abbreviation
            kind, expected_size = Ship.SHIP_INFO[abbreviation]

            if size != expected_size:
                print(f"ERROR: incorrect ship size: {line}")
                sys.exit(0)

            # create a list of GridPos objects representing the ship's 
            # positions
            positions = []
            if x1 == x2:
                for y in range(y1, y2 + 1):
                    # check if there is no other ship occupying the same 
                    # position on the board
                    if self._grid[x1][y]._ship is not None:
                        print(f"ERROR: overlapping ship: {line}")
                        sys.exit(0)
                    positions.append(self._grid[x1][y])
            else:
                for x in range(x1, x2 + 1):
                    # check if there is no other ship occupying the same 
                    # position on the board
                    if self._grid[x][y1]._ship is not None:
                        print(f"ERROR: overlapping ship: {line}")
                        sys.exit(0)
                    positions.append(self._grid[x][y1])

            # create a new Ship object with the provided abbreviation and 
            # positions
            ship = Ship(abbreviation, positions)
            # add the ship to the list of ships on the board
            self._ships.append(ship)

            # set the _ship attribute for each GridPos object representing the 
            # ship's position
            for pos in positions:
                pos._ship = ship

    def process_guess(self, x, y):
        '''
        The method process_guess processes the guess by updating the 
        corresponding GridPos object on the board with the guess result, 
        printing out the appropriate message depending on whether the guess was
        a hit or a miss, and whether the hit caused a ship to sink or not.
        x - this paramter takes the guess of the x coordinate
        y - this paramter takes the guess of the y coordinate
        '''
        grid_pos = self._grid[x][y]
        if grid_pos._guess:
            if grid_pos._ship:
                print("hit (again)")
            else:
                print("miss (again)")
        else:
            grid_pos._guess = True
            if grid_pos._ship:
                print("hit")
                grid_pos._ship._hits += 1
                if grid_pos._ship._hits == grid_pos._ship._size:
                    print(f"{grid_pos._ship._kind[0]} sunk")
                    self.check_all_sunk()
            else:
                print("miss")
    
    def check_all_sunk(self):
        '''
        The method check_all_sunk takes a board and returns whether all the 
        ships on the board are sunk.
        '''
        all_sunk = True
        for ship in self._ships:
            if ship._hits != ship._size:
                all_sunk = False
                break
        if all_sunk:
            print("all ships sunk: game over")
            sys.exit(0)


    def __str__(self):
        '''
        the str method defines a string representation for a board instance
        '''
        output = []
        for row in self._grid:
            row_output = []
            for pos in row:
                row_output.append(str(pos))
            output.append(" ".join(row_output))
        return "\n".join(output)

    def __repr__(self):
        '''
        the repr method defines a string representation for a Ship instance
        '''
        return self.__str__()

def main():
    '''
    The main function inputs the placement and the guess file from the user
    and then checks for illegal guesses.
    '''
    placement_file = input()
    guess_file = input()
    board = Board(placement_file)
    file = open(guess_file, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        x_y = line.split()
        if len(x_y) == 2:
            x, y = int(x_y[0]), int(x_y[1])
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("illegal guess")
            else:
                # when legal, process the guess
                board.process_guess(x, y)

main()
# calling main