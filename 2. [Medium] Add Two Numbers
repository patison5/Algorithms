# 2. [Medium] Add Two Numbers

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    prevIntVal = 0
    while True:
        temp_val1 = l1.val if l1 is not None else 0
        temp_val2 = l2.val if l2 is not None else 0
        sum = temp_val1 +  prevIntVal + temp_val2
        mod_value = sum % 10
        int_value = sum // 10
        prevIntVal = int_value

        if l1 is not None:
            l1.val = mod_value

        if (l1 is None) and (l2 is None) and (prevIntVal == 0):
            return l1

        if (prevIntVal == 0) and (l2 is None):
            return l1
        
        if (l1.next is None) and ((prevIntVal != 0) or (l2.next is not None)):
            l1.next = ListNode(0)
        
        if (l1 is not None):
            l1 = l1.next

        if (l2 is not None):
            l2 = l2.next

    

# ll4 = ListNode(9)
ll3 = ListNode(3)
ll2 = ListNode(4, ll3)
ll1 = ListNode(2, ll2)

lll3 = ListNode(5)
lll2 = ListNode(5, lll3)
lll1 = ListNode(5, lll2)


print(ll1.val, ll1.next.val, ll1.next.next.val)
print(lll1.val, lll1.next.val, lll1.next.next.val)
addTwoNumbers(ll1, lll1)
print("-----")
print(ll1.val, ll1.next.val, ll1.next.next.val)


def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    currentNode = firstNode = ListNode(0)
    num1 = num2 = ""

    while l1:
        num1 += str(l1.val)
        l1 = l1.next

    while l2:
        num2 += str(l2.val)
        l2 = l2.next

    res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]

    for i in res:
        currentNode.next = ListNode(i)
        currentNode = currentNode.next
        
    return firstNode.next  
