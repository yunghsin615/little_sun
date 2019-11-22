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


查詢
=


修改
=
