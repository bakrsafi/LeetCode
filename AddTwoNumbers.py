
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def build_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


#def convert_num_to_linkedlist(arr):
    

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        while l1.val is not None and l2.val is not None:
            ll=ListNode(0)
            ll.val=l1.val+l2.val
            if ll.val > 9:
                ll=ll.next
                ll.val=1
            else:
                ll=ll.next
            l1=l1.next
            l2=l2.next
            
        print(ll)
        

        
        
l1 = build_list([2,4,3])
l2 = build_list([5,6,4])
# 342 + 465 = 807   
# Expected output: [7,0,8]
solution = Solution()
print(solution.addTwoNumbers(l1, l2))