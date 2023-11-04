def solution(self, moves: str) -> bool:
    pt_x = 0
    pt_y = 0

    for move in moves:
        if move == "U":
            pt_y += 1
        elif move == "D":
            pt_y += -1
        elif move == "R":
            pt_x += 1
        elif move == "L":
            pt_x -= 1

    if pt_x == 0 and pt_y == 0:
        return True
    return False
