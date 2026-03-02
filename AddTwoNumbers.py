# Add Two Numbers
# the objective is to add two numbers represented as linked lists, where each node contains a single digit and the digits are stored in reverse order. The result should also be returned as a linked list in reverse order.


def build_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def convert_linkedlist_to_num(ll):
    num = 0
    multiplier = 1
    while ll:
        num += ll.val * multiplier
        multiplier *= 10
        ll = ll.next
    return num

#def convert_num_to_linkedlist(arr):
    

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = convert_linkedlist_to_num(l1)
        l2 = convert_linkedlist_to_num(l2)
        arr =l1 + l2
        #print(arr)
        arr = list(map(int, str(arr)[::-1]))
        #print(arr)
        return build_list(arr)
            
        
