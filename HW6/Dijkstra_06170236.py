
from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        self.graph.append([w,u,v]) 
        
    def Dijkstra(self, s): 
        test = [False] * self.V 
        dist = [float('inf')] * self.V
        
        dist[s] = 0
        
        while test != [True] * self.V:
            for i in range(self.V):
                if self.graph[s][i] != 0 and dist[s] + self.graph[s][i] < dist[i]:
                    dist[i] = dist[s] + self.graph[s][i]
                           
            m = float('inf')
            for k in range(self.V):
                if test[k] == False and dist[k] < m :
                    m = dist[k]
                    s = k         
            test[s] = True
            
            diction = {} 
            if test == [True] * self.V:
                for i in range(self.V):
                    diction[str(i)] = dist [i]
                return diction
            
    def Kruskal(self):
        g.graph.sort()
        root = []
        test = []
        diction={} 

        for i in range(self.V):
            root.append(-1)
        
        for i in range(0,len(g.graph)):
                
            if root[self.graph[i][1]] != root[self.graph[i][2]]:
                if root[self.graph[i][1]] == -1:
                    root[self.graph[i][1]] = root[self.graph[i][2]]
          
                elif root[self.graph[i][2]] == -1:
                    root[self.graph[i][2]] = root[self.graph[i][1]]

                else:
                    if root[self.graph[i][1]] > root[self.graph[i][2]]:
                        h = root[self.graph[i][1]]
                        for k in range(self.V):
                            if root[k] == h:
                                root[k] = root[self.graph[i][2]]
 
                    else:
                        h = root[self.graph[i][2]]
                        for k in range(self.V):
                            if root[k] == h:
                                root[k] = root[self.graph[i][1]]
  
            elif root[self.graph[i][1]] == root[self.graph[i][2]]:
                if root[self.graph[i][1]] == -1:
                    if self.graph[i][1] < self.graph[i][2]:
                        root[self.graph[i][2]] = self.graph[i][1]
                        root[self.graph[i][1]] = self.graph[i][1]

                    else:
                        root[self.graph[i][1]] = self.graph[i][2]
                        root[self.graph[i][2]] = self.graph[i][2]
                        
                else:
                    continue
            a = str(self.graph[i][1])
            b = str(self.graph[i][2])
            c = str(a+'-'+b)
            test.append(self.graph[i][0])
            diction[c]= test[-1]

            if len(test) == (len(root)-1):   
                return diction
            
            


# 參考資料<br>
# https://blog.csdn.net/hellojoy/article/details/81077019 #無限大寫法<br>
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/<br> 
# https://ithelp.ithome.com.tw/m/articles/10209593<br>
# https://blog.csdn.net/ychw365/article/details/8662993 #sort list<br>
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/ #addedge<br>
