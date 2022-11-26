import queue
from typing import List
from collections import deque

class Graph: 

  def __init__ (self, n):
    self.M = [[0 for _ in range(n)] for _ in range(n)]
    self.L = [[] for _ in range(n)] 

branco = 0
cinza = 1
preto = 2

class Graph: 

  def __init__ (self, n):
    self.n = n
    self.M = [[0 for _ in range(n)] for _ in range(n)]
    self.L = [[] for _ in range(n)]  

    self.pai = [None for _ in range(n)]
    self.d = [-1 for _ in range(n)]
  
  def bfs(self, source):
    cor = [branco for _ in range(self.n)]
    cor[source] = cinza 
    self.d[source] = 0
    Q = queue.Queue()
    Q.put(source)

  def dfs_visit(self, u):
    self.cor[u] = cinza
    for v in self.L[u]:
      if(self.cor[v] == branco):
        self.pai[v] = u
        self.dfs_visit(v)

  def dfs(self):
    self.cor = [branco for _ in range(self.n)]
    for u in range(self.n):
      self.pai[u] = -1
    for u in range(self.n):
      if (self.cor[u] == branco):
        self.dfs_visit(u)
    
    Q = queue.Queue()
    
    while (Q.empty() == False):
      u = Q.get()
      for v in self.L[u]:
        if self.cor[v] == branco:
          self.cor[v] = cinza
          self.d[v] = self.d[v] + 1
          self.pai[v] = u
          Q.put(v)
        self.cor[u] = preto
        
    print(self.d)
    print(self.pai)


def load_from(filename):
  with open(filename, "r") as file:
    lines = file.readlines()
    n = file.readline()
    #print(n)
    g = Graph(50)
    #print(lines)
    l = 0
    for line in lines[1:]:
      c = 0
      #print(line)
      for i in line.split("\t"):
        if i != "\n":
          g.M[l][c] = int(i)
          if(g.M[l][c] > 0):
              g.L[l].append(c)
          c += 1
        else:
          break
      l+=1
    
  print(g.M)
  print("\n")
  print(g.L)

  return g

gr = load_from("pcv50.txt")
gr.bfs(0)
