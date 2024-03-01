import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Define a dummy head for the merged list
        dummy_head = ListNode()
        current = dummy_head
        
        # Priority queue to store (node.val, node) tuples
        min_heap = []
        
        # Add the head nodes of all lists to the min heap
        for head_node in lists:
            if head_node:
                heapq.heappush(min_heap, (head_node.val, head_node))
        
        # Merge lists
        while min_heap:
            # Extract the minimum node from the heap
            val, node = heapq.heappop(min_heap)
            
            # Append the node to the merged list
            current.next = node
            current = current.next
            
            # Add the next node of the extracted node to the heap if it exists
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        
        return dummy_head.next


