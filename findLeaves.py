# Time:O(n) traversal+ depth+ dict
# Space:O(n) dict
# Leetcode: Yes


from collections import defaultdict
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        self.res = defaultdict(list)        # add new empty arrays
        self.helper(root,0)
        return list(self.res.values())
    def helper(self,root,depth):
        #base
        if not root:                        # beyond level 0 // max(-1,-1)+1 = 0
            return -1
        #logc
        left = self.helper(root.left,depth+1)
        right = self.helper(root.right,depth+1)
        depth =  max(left,right) +1
        self.res[depth].append(root.val)    # append root.val instead of root
        return depth
