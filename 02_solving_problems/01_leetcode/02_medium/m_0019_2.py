# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = ListNode(val=None, next=head)
        left = temp_head 
        right = head
        
        for _ in range(n):
            right = right.next

        while right: 
            right = right.next
            left = left.next

        left.next = left.next.next 

        return temp_head.next

#OK, 14%, 7%
