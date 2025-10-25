class Solution(object):
    def judgeCircle(self, moves):
        if moves.count("U") != moves.count("D"): 
            return False
        elif moves.count("R") != moves.count("L"):
            return False
        else:
            return True
