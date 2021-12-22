class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []
        
        result = []
        queue = [ root ]

        while len(queue) > 0:

            n = len(queue)
            sum = 0.0
            for i in range(n):
                current = queue.pop(0)
                sum += current.val
                if(current.left != None):
                    queue.append(current.left)
                
                if(current.right != None):
                    queue.append(current.right)
            
            result.append(sum / n)

        return result



solution = Solution()
solution.averageOfLevels()
