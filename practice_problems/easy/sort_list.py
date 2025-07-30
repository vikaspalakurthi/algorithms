class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head    
        slow, fast = head, head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, list1, list2):
        tail = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
