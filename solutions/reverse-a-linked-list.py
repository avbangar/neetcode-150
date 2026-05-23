# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First solution, can be improved by replacing stack with prev, current and next
        # but I like stacks :)

        # stack = []

        # while head:
        #     stack.append(head)
        #     head = head.next

        # if not stack:
        #     return head

        # head = stack.pop()
        # temp = head

        # while stack:
        #     temp.next = stack.pop()
        #     temp = temp.next
        #     temp.next = None

        # return head

        if not head or not head.next:
            return head

        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
