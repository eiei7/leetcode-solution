"""
Medium-leetcode
"""
class TicTacToe(object):

  def __init__(self, n):
    self.row = [0 for i in range(n)]
    self.col = [0 for i in range(n)]
    self.diag = 0
    self.antidiag = 0
    self.n = n

  def move(self, row, col, player):
    n = self.n
    if player == 1:
      self.row[row] += 1
      if self.row[row] == n: return player
      self.col[col] += 1
      if self.col[col] == n: return player

      if row == col: self.diag += 1
      if self.diag == n: return player
      if row + col == n - 1: self.antidiag += 1
      if self.antidiag == n: return player
    
    if player == 2:
      self.row[row] -= 1
      if self.row[row] == -n: return player
      self.col[col] -= 1
      if self.col[col] == -n: return player

      if row == col: self.diag -= 1
      if self.diag == -n: return player
      if row + col == n - 1: self.antidiag -= 1
      if self.antidiag == -n: return player
   
#TC:O(1)
#SP:O(n)

Solution = TicTacToe(3)
arr = [(0,0,1), (1,0,2), (1,1,1), (2,0,2), (2,2,1)]
for i, j, player in arr:
  if Solution.move(i, j, player): print("player " + str(player) + " wins!")

"""
Hard-Lintcode
"""
import sys

class TicTacToe(object):

  def __init__(self, n):
    self.row = [0 for i in range(n)]
    self.col = [0 for i in range(n)]
    self.diag = 0
    self.antidiag = 0
    self.n = n
    self.flag = 0
    self.board = [[0 for i in range(n)] for i in range(n)]

  def move(self, row, col, player):
    n = self.n
    board = self.board

    if self.flag != 0:
      print("GameEndException")
      self.row = [0 for i in range(n)]
      self.col = [0 for i in range(n)]
      self.diag = 0
      self.antidiag = 0
      self.flag = 0
      self.board = [[0 for i in range(n)] for i in range(n)]
    else:
      if player == 1:
        if board[row][col] != 0:
          print("AlreadyTakenException")
        else:
          board[row][col] = player
          self.row[row] += 1
          if self.row[row] == n: 
            self.flag = player
            print(str(player) + " player wins!")
        
          self.col[col] += 1
          if self.col[col] == n: 
            self.flag = player
            print(str(player) + " player wins!")

          if row == col: self.diag += 1
          if self.diag == n: 
            self.flag = player
            print(str(player) + " player wins!")
          if row + col == n - 1: self.antidiag += 1
          if self.antidiag == n: 
            self.flag = player
            print(str(player) + " player wins!")
        
      if player == 2:
        if board[row][col] != 0:
          print("AlreadyTakenException")
        else:
          board[row][col] = player
          self.row[row] -= 1
          if self.row[row] == -n: 
            self.flag = player
            print(str(player) + " player wins!")
          self.col[col] -= 1
          if self.col[col] == -n: 
            self.flag = player
            print(str(player) + " player wins!")

          if row == col: self.diag -= 1
          if self.diag == -n: 
            self.flag = player
            print(str(player) + " player wins!")
          if row + col == n - 1: self.antidiag -= 1
          if self.antidiag == -n: 
            self.flag = player
            print(str(player) + " player wins!")
        

Solution = TicTacToe(3)
arr = [(0,0,1), (1,0,2), (1,1,1), (2,0,2), (2,2,1), (0,0,1), (0,0,1), (0,0,1), (1,0,2), (1,1,1), (2,0,2), (2,2,1)]
for i, j, player in arr:
  Solution.move(i, j, player)