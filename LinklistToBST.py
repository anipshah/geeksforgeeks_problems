# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# convert Linklist to BST
# using DFS
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        #create list from link list
        temp=[]
        while head:
            temp.append(head.val)
            head=head.next
        ans = self.helper_dfs(temp)
        return ans
    def helper_dfs(self,l):
        if not l:
            return
        mid=len(l)//2
        root = TreeNode(l[mid])
        root.left = self.helper_dfs(l[:mid])
        root.right = self.helper_dfs(l[mid+1:])
        return root
