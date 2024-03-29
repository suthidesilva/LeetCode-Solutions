# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr=head
        count=0
        while count<k and curr!=None:
            curr=curr.next
            count+=1
        if count==k:
            curr=self.reverseKGroup(curr,k)
            while count!=0:
                nextNode=head.next
                head.next=curr
                curr=head
                head=nextNode
                count-=1
            head=curr
        return head
