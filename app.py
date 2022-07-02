##### Mechanics Outline #####
# blank board
# right click places flag on unrevealed cells
# left click reveals cells
# LC a cell that has 1 or more bombs next to it shows number of bombs near
# LC a cell with no bombs adjacent reveals all others that have no bombs adjacent until it reaches a cell with a number in
# LC a cell with a bomb. Game Over
#


##### Possible ideas #####
# ##To generate a board.##
# user picks pre defiend or custome size then that many BUTTON objects are created and added to a list. x amount of those objects are given the mine flag. 
# They are then randomly chosen from the list to form a grid of the required size.

# grid builder function


# cell object needs:
# number:int
# has mine: bool 
# adjacent mines : int
        # function to check if mines are near and fills out adjacent mins
# revealed: bool
        # functions when LC
# flagged: bool
        # functions when RC
