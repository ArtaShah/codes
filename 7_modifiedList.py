class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next:
            if curr.next.val in num_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
