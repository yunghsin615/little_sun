#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 

class Graph:
 
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v)
 
    def BFS(self, s): 
        status1 = []
        status2 = []
        
        status2.append(s)
        i = 0    
        while i < len(self.graph[s]):
            if self.graph[s][i] != None:
                status1.append(self.graph[s][i])
                i += 1
        s = status1[0]
                    
        while len(status1) > 0:
            for i in self.graph[s]:
                if i not in status1 and i not in status2:
                    status1.append(i)
                    
                elif i not in status1 or i not in status2:
                    continue
                
            status2.append(status1[0])
            status1.remove(status1[0])   
            if status1:
                s = status1[0]
                
        return status2
    
    def DFS(self, s):
        status1 = []
        status2 = []
        
        status2.append(s)
        i = 0    
        while i < len(self.graph[s]):
            if self.graph[s][i] != None:
                status1.append(self.graph[s][i])
                i += 1
        s = status1[-1]
                    
        while len(status1) > 0:
            s = status1.pop(-1) 
            status2.append(s)
            for i in self.graph[s]:
                if i not in status1 and i not in status2:
                    status1.append(i)
                    
                elif i not in status1 or i not in status2:
                    continue
                            
            if status1:
                s = status1[-1]
                
        return status2


# 參考資料<br>
# https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_0 #上課講義<br>
# http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html #BFS<br>
# https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_0 #上課講義<br>
# http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html #DFS<br>
# https://magiclen.org/dfs-bfs/<br>
# https://www.shs.edu.tw/works/essay/2017/03/2017033023453259.pdf<br>
