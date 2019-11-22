Binary Search Tree新增、刪除、查詢、修改功能說明
=
以下直接在每個程式碼後面說明

新增(insert)
=
以下是insert的程式碼<br>

      def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root = TreeNode(val)
            
        else:
            if val != root.val: 如果要新增的值不等於root
                if val < root.val: 新增值 < root
                    if root.left == None: 然後左邊沒有東西
                        root.left = TreeNode(val) 就把新增值加到這個位置
                        return root.left 
                    else:  左邊有東西
                        i = root.left 
                        return self.insert(i,val) 重新找新增值要往哪邊走
                else: 新增值 > root
                    if root.right == None: 然後有邊沒有東西
                        root.right = TreeNode(val) 就把新增值加到這個位置
                        return root.right
                    else:   右邊有東西
                        j = root.right
                        return self.insert(j,val) 重新找新增值要往哪邊走
                        
            else: 如果要新增的值等於root
                if root.left == None: 然後左邊沒有東西
                    root.left = TreeNode(val) 就把新增值加到這個位置
                    return root.left
                else: 左邊有東西
                    o = root.left
                    return self.insert(o,val) 重新找新增值要往哪邊走

刪除(delete)
=
以下是delete的程式碼<br>
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        
        先尋找target是否存在
        delete_node = self.search(root,target)
        if delete_node != None: 代表target存在
            i=root 設一個i是希望它可以一直停留在最上面的root
            pa = root pa是會跑來跑去的root
            
            while target != root.val: 刪除值不等於root
                pa = root 
                if target < root.val: 刪除值 < root
                    root = root.left  root往左邊走

                elif target > root.val: 刪除值 > root
                    root = root.right  root往右邊走


            ##root只有一個右邊的child     
            if root.left is None and root.right:
                if pa.val < root.val: 
                    pa.right = root.right pa往右邊指向原root的right

                elif pa.val > root.val:
                    pa.left = root.right pa往左邊指向原root的left
                    
                !!!當你要刪除的值就是root!!!
                else:
                    root = root.right pa在原本的地方，root開始跑來跑去
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val 把pa的值換掉
                        pa.right = None pa.right直接指向None
                        
                    #root只有右邊的child，代表目前的root就是右樹中最小的值
                    elif root.left is None and root.right:
                        pa.val = root.val 把pa的值換成右樹中最小的值
                        pa.right = root.right 間接把root刪除
                        
                    #root只有左邊的child，那還要再找右樹中最小的值
                    elif root.right is None and root.left:
                        move = root.left
                        movepa = root
                        while move.left: move會是右樹中最小的值
                            movepa = move
                            move = movepa.left
                        
                        if move.right: 但也還有可能會有right小孩
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None 沒有right小孩，也就代表沒有小孩，直接指向None
                        pa.val = move.val 把pa的值換成右樹中最小的值
                        
                    #root有兩個child    
                    else: move會是右樹裡面最小的值
                        move = root.left
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right: 但也還有可能會有right小孩
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None 沒有right小孩，也就代表沒有小孩，直接指向None
                        
                        pa.val = move.val把pa的值換成右樹中最小的值
                        

            ##root只有一個左邊的child
            elif root.right is None and root.left:
                if pa.val < root.val:
                    pa.right = root.left pa往右邊指向原root的left

                elif pa.val > root.val:
                    pa.left = root.left pa往右邊指向原root的left
                    
                !!!當你要刪的值就是root!!!
                else:
                    root = root.left pa在原本的地方，root開始跑來跑去
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val 把pa的值換掉
                        pa.left = None pa.left直接指向None
                        
                    #root只有左邊的child，代表目前的root就是左樹中最大的值
                    elif root.right is None and root.left:
                        pa.val = root.val 把pa的值換掉
                        pa.left = root.left 間接把root刪除
                    
                    #root只有右邊的child，那還要再找左樹中最大的值
                    elif root.left is None and root.right:
                        move = root.right
                        movepa = root
                        while move.right: move會是左樹中最大的值
                            movepa = move
                            move = movepa.right
                        
                        if move.left: 但也還有可能會有left小孩
                            movepa.right = move.left
                        
                        else:
                            movepa.right = None 沒有left小孩，也就代表沒有小孩，直接指向None                     
                        pa.val = move.val 把pa的值換成左樹中最大的值
                        
                    #root有兩個child 
                    else: move會是左樹中最大的值
                        move = root.right
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right: 但也還有可能會有left小孩
                            if movepa.val > move.right.val:
                                movepa.left = move.right
                            elif movepa.val < move.right.val:    
                                movepa.right = move.right
                        else: 沒有left小孩，也就代表沒有小孩，直接指向None 
                            if movepa.val > move.val:
                                movepa.left = None
                            elif movepa.val < move.val:
                                movepa.right = None
                            
                        pa.val = move.val 把pa的值換成左樹中最大的值
                        

            ##root沒有child
            elif root.left is None and root.right is None:
                if pa.val > root.val: 
                    pa.left = None  pa往左邊指向None，間接把root刪除
                elif pa.val < root.val:
                    pa.right = None pa往右邊指向None，間接把root刪除
                    
                else:
                    return

            ##root有兩個child
            else:  找右樹中最小的值
                move = root.right
                movepa = root
                while move.left:
                    movepa = move
                    move = movepa.left

                if move.right: 右樹中最小的值可能有right小孩
                    if movepa.val > move.right.val: 
                        movepa.left = move.right 間接刪除move
                    elif movepa.val < move.right.val:    
                        movepa.right = move.right 間接刪除move
                else: 也有可能沒有小孩
                    if movepa.val > move.val:
                        movepa.left = None movepa指向left=None，間接刪除move
                    elif movepa.val < move.val:
                        movepa.right = None movepa指向right=None，間接刪除move
                root.val = move.val 把root的值換成右樹中最小的值
                 
            self.delete(i,target) 有可能有重複值所以要再檢查
        return root


查詢(search)
=
以下是search的程式碼<br>
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root == None: 如果沒有root就代表沒有tree
            return None
        
        else: 代表有tree裡面有值
            if target != root.val: 查詢值不等於root
                if target < root.val: 查詢值 < root，往左走
                    if root.left == None: 左邊沒東西
                        return None 代表查詢值不存在
                    else: 左邊有東西
                        p = root.left 往左邊再搜尋一次位置
                        return self.search(p,target)
                        
                else:  查詢值 > root
                    if root.right == None: 右邊沒東西
                        return None 代表查詢值不存在
                    else: 右邊有東西
                        k = root.right 往右邊再搜尋一次位置
                        return self.search(k,target)
            else: 查詢值等於root
                return root


修改(modify)
=
以下是modify的程式碼<br>
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        
        先尋找target是否存在
        delete_node = self.search(root,target)
        if delete_node != None: 代表target存在
            i=root 設一個i是希望它可以一直停留在最上面的root
            pa = root pa是會跑來跑去的root
            
            while target != root.val: 刪除值不等於root
                pa = root 
                if target < root.val: 刪除值 < root
                    root = root.left  root往左邊走

                elif target > root.val: 刪除值 > root
                    root = root.right  root往右邊走


            ##root只有一個右邊的child     
            if root.left is None and root.right:
                if pa.val < root.val: 
                    pa.right = root.right pa往右邊指向原root的right

                elif pa.val > root.val:
                    pa.left = root.right pa往左邊指向原root的left
                    
                !!!當你要刪除的值就是root!!!
                else:
                    root = root.right pa在原本的地方，root開始跑來跑去
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val 把pa的值換掉
                        pa.right = None pa.right直接指向None
                        
                    #root只有右邊的child，代表目前的root就是右樹中最小的值
                    elif root.left is None and root.right:
                        pa.val = root.val 把pa的值換成右樹中最小的值
                        pa.right = root.right 間接把root刪除
                        
                    #root只有左邊的child，那還要再找右樹中最小的值
                    elif root.right is None and root.left:
                        move = root.left
                        movepa = root
                        while move.left: move會是右樹中最小的值
                            movepa = move
                            move = movepa.left
                        
                        if move.right: 但也還有可能會有right小孩
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None 沒有right小孩，也就代表沒有小孩，直接指向None
                        pa.val = move.val 把pa的值換成右樹中最小的值
                        
                    #root有兩個child    
                    else: move會是右樹裡面最小的值
                        move = root.left
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right: 但也還有可能會有right小孩
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None 沒有right小孩，也就代表沒有小孩，直接指向None
                        
                        pa.val = move.val把pa的值換成右樹中最小的值
                        

            ##root只有一個左邊的child
            elif root.right is None and root.left:
                if pa.val < root.val:
                    pa.right = root.left pa往右邊指向原root的left

                elif pa.val > root.val:
                    pa.left = root.left pa往右邊指向原root的left
                    
                !!!當你要刪的值就是root!!!
                else:
                    root = root.left pa在原本的地方，root開始跑來跑去
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val 把pa的值換掉
                        pa.left = None pa.left直接指向None
                        
                    #root只有左邊的child，代表目前的root就是左樹中最大的值
                    elif root.right is None and root.left:
                        pa.val = root.val 把pa的值換掉
                        pa.left = root.left 間接把root刪除
                    
                    #root只有右邊的child，那還要再找左樹中最大的值
                    elif root.left is None and root.right:
                        move = root.right
                        movepa = root
                        while move.right: move會是左樹中最大的值
                            movepa = move
                            move = movepa.right
                        
                        if move.left: 但也還有可能會有left小孩
                            movepa.right = move.left
                        
                        else:
                            movepa.right = None 沒有left小孩，也就代表沒有小孩，直接指向None                     
                        pa.val = move.val 把pa的值換成左樹中最大的值
                        
                    #root有兩個child 
                    else: move會是左樹中最大的值
                        move = root.right
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right: 但也還有可能會有left小孩
                            if movepa.val > move.right.val:
                                movepa.left = move.right
                            elif movepa.val < move.right.val:    
                                movepa.right = move.right
                        else: 沒有left小孩，也就代表沒有小孩，直接指向None 
                            if movepa.val > move.val:
                                movepa.left = None
                            elif movepa.val < move.val:
                                movepa.right = None
                            
                        pa.val = move.val 把pa的值換成左樹中最大的值
                        

            ##root沒有child
            elif root.left is None and root.right is None:
                if pa.val > root.val: 
                    pa.left = None  pa往左邊指向None，間接把root刪除
                elif pa.val < root.val:
                    pa.right = None pa往右邊指向None，間接把root刪除
                    
                else:
                    return

            ##root有兩個child
            else:  找右樹中最小的值
                move = root.right
                movepa = root
                while move.left:
                    movepa = move
                    move = movepa.left

                if move.right: 右樹中最小的值可能有right小孩
                    if movepa.val > move.right.val: 
                        movepa.left = move.right 間接刪除move
                    elif movepa.val < move.right.val:    
                        movepa.right = move.right 間接刪除move
                else: 也有可能沒有小孩
                    if movepa.val > move.val:
                        movepa.left = None movepa指向left=None，間接刪除move
                    elif movepa.val < move.val:
                        movepa.right = None movepa指向right=None，間接刪除move
                root.val = move.val 把root的值換成右樹中最小的值
                

            self.insert(i,new_val) 每search到target一次，就delete一次 ;
                                   每delete一次，就insert new_val一次
       
        return root
     
     
<br>
<br>
<br>
參考資料:<br>
https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm<br>
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html<br>
http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html<br>
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/<br>
https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533<br>
