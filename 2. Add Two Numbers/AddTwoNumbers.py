'''
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def valuefy(l: Optional[ListNode]):
        if (l.next != None):
            return str(l.val) + valuefy(l.next)
        else:
            return str(l.val)

    def nodefy(value):
        if (len(value) == 1):
            return ListNode(val=int(value), next=None)
        else:
            return ListNode(val=int(value[0]), next=nodefy(value[1:]))

    sum = str(int(valuefy(l1)[::-1]) + int(valuefy(l2)[::-1]))[::-1]

    sumNode = nodefy(sum)
    return sumNode


def main():
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=9, next=None)))
    l2 = ListNode(val=5, next=ListNode(
        val=6, next=ListNode(val=4, next=ListNode(val=9, next=None))))
    result = addTwoNumbers(ListNode, l1, l2)
    return 0


if __name__ == '__main__':
    main()
