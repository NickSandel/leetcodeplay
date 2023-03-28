# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        vals = []
        carry = 0
        while l1:
            if l2:
                total = l1.val + l2.val + carry
            else:
                total = l1.val + carry
            # No point looking higher as it's single digits most we can get is 9 + 9 + 1 = 19
            if total > 9:
                carry = 1
                total = total - 10
            else:
                carry = 0
            vals.append(total)
            l1 = l1.next
            if l2:
                l2 = l2.next

        while l2:
            total = l2.val + carry 
            if total > 9:
                carry = 1
                total = total - 10
            else:
                carry = 0
            vals.append(total)
            l2 = l2.next
        if carry:
            vals.append(carry)
        print(vals)
        nodeOutput = ListNode()
        for val in reversed(vals):
            nodeOutput.next = ListNode(val, nodeOutput.next)
        return nodeOutput.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution().addTwoNumbers(l1, l2)
print(solution)

l1 = ListNode(0)
l2 = ListNode(0)
solution = Solution().addTwoNumbers(l1, l2)
print(solution)

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
solution = Solution().addTwoNumbers(l1, l2)
print(solution)