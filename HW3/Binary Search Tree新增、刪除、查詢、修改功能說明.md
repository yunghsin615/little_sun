新增
=

      def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root = TreeNode(val)
            
        else:
            if val != root.val:
                if val < root.val:
                    if root.left == None:
                        root.left = TreeNode(val)
                        return root.left
                    else:
                        i = root.left
                        return self.insert(i,val)
                else:
                    if root.right == None:
                        root.right = TreeNode(val)
                        return root.right
                    else:
                        j = root.right
                        return self.insert(j,val)
            else:
                if root.left == None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    o = root.left
                    return self.insert(o,val)

刪除
=
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        
        #先尋找val是否存在
        delete_node = self.search(root,target)
        if delete_node != None:
            i=root
            pa = root
            while target != root.val:
                pa = root
                if target < root.val:
                    root = root.left

                elif target > root.val:
                    root = root.right


            #root只有一個右邊的child     
            if root.left is None and root.right:
                if pa.val < root.val:
                    pa.right = root.right

                elif pa.val > root.val:
                    pa.left = root.right
                    
                #當你要刪的值就是root
                else:
                    root = root.right
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val
                        pa.right = None
                        
                    #root只有右邊的child，代表目前的root就是右樹中最小的值
                    elif root.left is None and root.right:
                        pa.val = root.val
                        pa.right = root.right
                        
                    #root只有左邊的child，那還要再找右樹中最小的值
                    elif root.right is None and root.left:
                        move = root.left
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left
                        
                        if move.right:
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None
                        pa.val = move.val
                        
                    #root有兩個child    
                    else:
                        move = root.left
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right:
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None
                        
                        pa.val = move.val
                        

            #root只有一個左邊的child
            elif root.right is None and root.left:
                if pa.val < root.val:
                    pa.right = root.left

                elif pa.val > root.val:
                    pa.left = root.left
                    
                #當你要刪的值就是root    
                else:
                    root = root.left
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val
                        pa.left = None
                        
                    #root只有左邊的child，代表目前的root就是左樹中最大的值
                    elif root.right is None and root.left:
                        pa.val = root.val
                        pa.left = root.left
                    
                    #root只有右邊的child，那還要再找左樹中最大的值
                    elif root.left is None and root.right:
                        move = root.right
                        movepa = root
                        while move.right:
                            movepa = move
                            move = movepa.right
                        
                        if move.left:
                            movepa.right = move.left
                        
                        else:
                            movepa.right = None                        
                        pa.val = move.val
                        
                    #root有兩個child 
                    else:
                        move = root.right
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right:
                            if movepa.val > move.right.val:
                                movepa.left = move.right
                            elif movepa.val < move.right.val:    
                                movepa.right = move.right
                        else:
                            if movepa.val > move.val:
                                movepa.left = None
                            elif movepa.val < move.val:
                                movepa.right = None
                            
                        pa.val = move.val
                        

            #root沒有child
            elif root.left is None and root.right is None:
                if pa.val > root.val:
                    pa.left = None
                elif pa.val < root.val:
                    pa.right = None
                    
                else:
                    return

            #root有兩個child
            else:
                move = root.right
                movepa = root
                while move.left:
                    movepa = move
                    move = movepa.left

                if move.right:
                    if movepa.val > move.right.val:
                        movepa.left = move.right
                    elif movepa.val < move.right.val:    
                        movepa.right = move.right
                else:
                    if movepa.val > move.val:
                        movepa.left = None
                    elif movepa.val < move.val:
                        movepa.right = None
                root.val = move.val
                 
            self.delete(i,target)
        return root


查詢
=
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root == None:
            return None
        
        else:
            if target != root.val:
                if target < root.val:
                    if root.left == None:
                        return None
                    else:
                        p = root.left
                        return self.search(p,target)
                else:
                    if root.right == None:
                        return None
                    else:
                        k = root.right
                        return self.search(k,target)
            else:
                return root


修改
=
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        i = root
        #先尋找val是否存在
        while self.search(root,target) != None:
            pa = root
            while target != root.val:
                pa = root
                if target < root.val:
                    root = root.left

                elif target > root.val:
                    root = root.right


            #root只有一個右邊的child     
            if root.left is None and root.right:
                if pa.val < root.val:
                    pa.right = root.right

                elif pa.val > root.val:
                    pa.left = root.right
                    
                #當你要刪的值就是root
                else:
                    root = root.right
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val
                        pa.right = None
                        
                    #root只有右邊的child，代表目前的root就是右樹中最小的值
                    elif root.left is None and root.right:
                        pa.val = root.val
                        pa.right = root.right
                        
                    #root只有左邊的child，那還要再找右樹中最小的值
                    elif root.right is None and root.left:
                        move = root.left
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left
                        
                        if move.right:
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None
                        pa.val = move.val
                        
                    #root有兩個child    
                    else:
                        move = root.left
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right:
                            movepa.left = move.right
                        
                        else:
                            movepa.left = None
                        
                        pa.val = move.val
                        

            #root只有一個左邊的child
            elif root.right is None and root.left:
                if pa.val < root.val:
                    pa.right = root.left

                elif pa.val > root.val:
                    pa.left = root.left
                    
                #當你要刪的值就是root    
                else:
                    root = root.left
                    #root沒有child
                    if root.left is None and root.right is None:
                        pa.val = root.val
                        pa.left = None
                        
                    #root只有左邊的child，代表目前的root就是左樹中最大的值
                    elif root.right is None and root.left:
                        pa.val = root.val
                        pa.left = root.left
                    
                    #root只有右邊的child，那還要再找左樹中最大的值
                    elif root.left is None and root.right:
                        move = root.right
                        movepa = root
                        while move.right:
                            movepa = move
                            move = movepa.right
                        
                        if move.left:
                            movepa.right = move.left
                        
                        else:
                            movepa.right = None                        
                        pa.val = move.val
                        
                    #root有兩個child 
                    else:
                        move = root.right
                        movepa = root
                        while move.left:
                            movepa = move
                            move = movepa.left

                        if move.right:
                            if movepa.val > move.right.val:
                                movepa.left = move.right
                            elif movepa.val < move.right.val:    
                                movepa.right = move.right
                        else:
                            if movepa.val > move.val:
                                movepa.left = None
                            elif movepa.val < move.val:
                                movepa.right = None
                            
                        pa.val = move.val
                        

            #root沒有child
            elif root.left is None and root.right is None:
                if pa.val > root.val:
                    pa.left = None
                elif pa.val < root.val:
                    pa.right = None
                    
                else:
                    return

            #root有兩個child
            else:
                move = root.right
                movepa = root
                while move.left:
                    movepa = move
                    move = movepa.left

                if move.right:
                    if movepa.val > move.right.val:
                        movepa.left = move.right
                    elif movepa.val < move.right.val:    
                        movepa.right = move.right
                else:
                    if movepa.val > move.val:
                        movepa.left = None
                    elif movepa.val < move.val:
                        movepa.right = None
                root.val = move.val

            self.insert(i,new_val)
       
        return root
