# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """

    if not headA or not headB:
      return None

    dummy1, dummy2 = headA, headB

    while dummy1 != dummy2:
      dummy1 = dummy1.next if dummy1 else headB
      dummy2 = dummy2.next if dummy2 else headA

    return dummy1