'''
Created on May 11, 2016

@author: Saurabh
'''

'''
Minimax: Designed for perfect information game like Chess or Checkers

Stick pick-up game:
11 sticks given. Player picking the last stick wins
'''

from sys import maxsize
#=========================================================================
'''
Define the tree and its nodes
'''

class Node(object):
    
    def __init__(self, i_depth, i_sticks_remaining, i_player_num, i_value = 0):
        self.i_depth = i_depth
        self.i_sticks_remaining = i_sticks_remaining
        self.i_player_num = i_player_num
        self.i_value = i_value
        self.children = []
        self.create_children()
        
        
    def create_children(self):
        if self.i_depth >= 0:
            for i in range(1,3):
                v = self.i_sticks_remaining - i
                self.children.append(Node(self.i_depth - 1, v, 
                                          - self.i_player_num,
                                          self.real_val(v)))
                
    
    def real_val(self, value):
        if value == 0:
            return maxsize * self.i_player_num
        elif value < 0:
            return maxsize * - self.i_player_num
        return 0
    
#==============================================================================
'''
Implementing the minimax algorithm
'''

def minimax(node, i_depth, i_player_num):
    if i_depth == 0 or (abs(node.i_value) == maxsize):
        return node.i_value
    
    i_best_value = maxsize * - i_player_num
    
    for i in range(len(node.children)):
        child = node.children[i]
        i_val = minimax(child, i_depth - 1, - i_player_num)
        if (abs(maxsize * i_player_num - i_val)) < (abs (maxsize * i_player_num - i_best_value)):
            i_best_value = i_val
            
    return i_best_value

#===============================================================================
'''
Checking for Win condition
'''

def win_check(i_sticks_remaining, i_player_num):
    if i_sticks_remaining <= 0:
        if i_player_num > 0:
            if i_sticks_remaining == 0:
                print "You win"
            else:
                print "You lose, you cannot choose that many sticks"
                
        else:
            if i_sticks_remaining == 0:
                print "Comp wins"
            else:
                print "Comp Error"
        return 0
    return 1

#=================================================================================
'''
Defining the main method
'''

if __name__ == '__main__':
    i_depth = 4
    i_total_sticks = 11
    i_curr_player = 1
    
    print "------------Time to play the game-----------"
    
    while (i_total_sticks > 0):
        print "Total Sticks Remaining: ", i_total_sticks
        choice = raw_input("Enter how many sticks you wanna choose (1 or 2)")
        i_total_sticks -= int(float(choice))
        
        if win_check(i_total_sticks, i_curr_player):
            i_curr_player *= -1
            node = Node(i_depth, i_total_sticks, i_curr_player)
            i_best_choice = -100
            i_best_value = maxsize * -i_curr_player
            
            for i in range(len(node.children)):
                child = node.children[i]
                i_val = minimax(child, i_depth, -i_curr_player)
                if (abs (maxsize * i_curr_player - i_val)) <= (abs(maxsize * i_curr_player - i_best_value)):
                    i_best_value = i_val
                    i_best_choice = i
                    
            i_best_choice += 1
            print "Comps choice is: ", i_best_choice
            i_total_sticks -= i_best_choice
            win_check(i_total_sticks, i_curr_player)
            i_curr_player *= -1
                
                