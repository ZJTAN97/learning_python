class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        
        queue = [ root ]
        depth = 1

        while len(queue) > 0:

            n = len(queue)
            for i in range(n):
                current = queue.pop(0)
                if current.left is None and current.right is None:
                    return depth

                if current.left != None:
                    queue.append(current.left)
                
                if current.right != None:
                    queue.append(current.right)
            
            depth += 1

        return depth



solution = Solution()
solution.averageOfLevels()
