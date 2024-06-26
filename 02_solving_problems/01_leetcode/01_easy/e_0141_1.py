

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        sad_set = set()

        while head:
            if head in sad_set:
                return True
            sad_set.add(head)
            head = head.next

        return False