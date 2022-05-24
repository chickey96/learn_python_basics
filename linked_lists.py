class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def recurSearchForMiddleNode(head, count=0):
    if(not head):
        return count // 2
    
    middle = recurSearchForMiddleNode(head.next, count + 1)

    if(type(middle).__name__ == 'int' and middle == count):
        return head
    else:
        return middle 


head = ListNode(5)
curr_node = head 

for i in range(7, 10):
    curr_node.next = ListNode(i)
    curr_node = curr_node.next 

# 5 => 7 => 8 => 9

print("check middleNode for even number nodes")
print(f"middle node val is {recurSearchForMiddleNode(head).val} should be 8")

for i in range(12, 15):
    curr_node.next = ListNode(i)
    curr_node = curr_node.next

# 5 => 7 => 8 => 9 => 12 => 13 => 14

print("check middleNode for odd number nodes")
print(f"middle node val is {recurSearchForMiddleNode(head).val} should be 9")

