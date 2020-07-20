import sys

class Solution:
    def __init__(self, word_1, word_2):
        self.w_1 = word_1
        self.w_2 = word_2
    
    def o_of_n(self):
        if(len(self.w_1) != len(self.w_2)): return False
        word_map = {}
        for i in self.w_1:
            if(i in word_map): word_map[i] += 1
            else: word_map[i] = 1
            
        for j in self.w_2:
            print(word_map)
            if(j in word_map):
                if(word_map[j] <= 0): return False
                word_map[j] -= 1
            else: return False
            
        return True
    
print("input the first word")
word1 = input()
print("input the second word")
word2 = input()

sol = Solution(word1, word2)
print(sol.o_of_n())
