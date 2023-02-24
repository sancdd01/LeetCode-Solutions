# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_as_num = ll_to_num(l1)
        l2_as_num = ll_to_num(l2)
        total = l1_as_num + l2_as_num
       
        return num_to_ll(total)

def ll_to_num(ll):
    sum = 0
    factor = 1
    current = ll
    while current:
        sum += current.val * factor
        factor *= 10

        current = current.next 

    return sum

def num_to_ll(num):
    num_as_ll = ListNode()
    current = num_as_ll
    
    while num != 0:
        current.val = num % 10
        num = num // 10
        if num != 0:
            current.next = ListNode()
            current = current.next

    return num_as_ll