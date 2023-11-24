from copy import *

class PuzzleState:
    
    def __init__(self,initial_state, parent=None, action=None) -> None:
        self.puzzle = initial_state
        self.parent = parent
        self.action = action
        self.blank_box_position = self.find_blank_box()
        
    def find_blank_box(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i,j
            
    def find_possible_moves(self):
        moves = []
        row,column = self.blank_box_position
        if row > 0:
            moves.append("up")
        if row < 2:
            moves.append("down")
        if column > 0:
            moves.append("left")
        if column < 2:
            moves.append("right")
        return moves
    
    def move_box(self,move):
        current_state = self.puzzle
        new_state = deepcopy(self.puzzle)
        # new_state = [list(row) for row in self.puzzle]
        row,column = self.blank_box_position
        if move == "up":
            new_state[row][column],new_state[row-1][column] = current_state[row-1][column],current_state[row][column]
        elif move == "down":
            new_state[row][column],new_state[row+1][column] = current_state[row+1][column],current_state[row][column]
        elif move == "left":
            new_state[row][column],new_state[row][column-1] = current_state[row][column-1],current_state[row][column]
        elif move == "right":
            new_state[row][column],new_state[row][column+1] = current_state[row][column+1],current_state[row][column]
        return PuzzleState(new_state,parent=self,action=move)
        
def solve_8_puzzle(initial_state,goal_state):
    depth_limit = 0
    while True:
        result = depth_limited_search(initial_state,goal_state,depth_limit)
        if result:
            return get_solution_path(result)
        depth_limit += 1
                
def depth_limited_search(initial_state,goal_state,depth_limit):
    
    stack = [(PuzzleState(initial_state),0)]
    visited = set()
    while stack:
        current_state,current_depth = stack.pop()
        visited.add(current_state)
        if current_state.puzzle == goal_state:
            return current_state
        if current_depth < depth_limit:
            possible_moves = current_state.find_possible_moves()    
            for move in possible_moves:
                new_state = current_state.move_box(move)
                if new_state not in visited:
                    stack.append((new_state,current_depth+1))
    return None
            
def get_solution_path(final_state):
    path = []
    current_state = final_state
    while current_state:
        path.append(current_state.action)
        current_state = current_state.parent
    return list(reversed(path))[1::]

if __name__ == "__main__":
    
    initial_state = [
        [1,2,3],
        [0,4,6],
        [7,5,8]
    ]
    
    goal_state = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ]
    
    solution = solve_8_puzzle(initial_state,goal_state)
    
    if solution:
        print("Solution Path", solution)
    else:
        print("No Solution Found")


