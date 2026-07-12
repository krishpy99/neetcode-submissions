class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nextMove = ['R', 'D', 'L', 'U']
        fr, fc, lr, lc = 0, 0, len(matrix), len(matrix[0])
        def newCord(i, j, move):
            match move:
                case 'R':
                    return i, j+1
                case 'D':
                    return i+1, j
                case 'L':
                    return i, j-1
                case 'U':
                    return i-1, j
                case _:
                    return "Bruh what move is this?"
            return "how did we get here?"
        
        def validMove(i, j, move):
            ii, jj = newCord(i, j, nextMove[move])
            if ii < fr or jj < fc or ii >= lr or jj >= lc:
                return False
            return True
        
        res = []
        move = 0
        i, j = 0, 0

        while True:
            #print(i, j, matrix[i][j])
            res.append(matrix[i][j])
            #print(newCord(i, j, nextMove[move]), validMove(i, j, move))
            if not validMove(i, j, move):
                match move:
                    case 0:
                        fr += 1
                    case 1:
                        lc -= 1
                    case 2:
                        lr -= 1
                    case 3:
                        fc += 1
                    case _:
                        print("how can this be?")
                
                move += 1
                move %= 4
                
                if not validMove(i, j, move):
                    return res
            i, j = newCord(i, j, nextMove[move])
        
        return res