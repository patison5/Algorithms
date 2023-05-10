# 19. [Easy] Remove Nth Node From End of List

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (not head.next and n == 1):
            return None

        current = head
        size = 0
        while current and current.next:
            current = current.next
            size += 1
        
        removed_index = size - n
        current = head

        if removed_index < 0:
            head = head.next
            return head            

        while removed_index:
            removed_index -= 1
            current = current.next

        current.next = current.next.next
        return head