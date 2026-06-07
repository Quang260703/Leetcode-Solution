# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = head = ListNode(0)
        while list1 is not None or list2 is not None:
            list1_val = list1.val if list1 is not None else 9999
            list2_val = list2.val if list2 is not None else 9999
            if list1_val < list2_val:
                list3.next  = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next
        return head.next
