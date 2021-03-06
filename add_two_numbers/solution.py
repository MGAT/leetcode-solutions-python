"""
You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list:

Input: (2 -> 4 -> 3)  + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for single-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		carry = 0
		res = None 
		res_end = None
		while l1 is not None and l2 is not None:
			temp = l1.val + l2.val +carry
			digit = temp % 10
			carry = temp / 10
			if res is None:
				res = ListNode(digit)
				res_end = res
			else:
				res_end.next = ListNode(digit)
				res_end = res_end.next
			rem = None
			if l1 is not None:
				rem = l1
			else:
				rem = l2
			while rem is not None:
				temp = rem.val + carry
				digit = temp % 10
				carry = temp / 10
				if res is None:
					res = ListNode(digit)
					res_end = res
				else:
					res_end.next = ListNode(digit)
					res_end = res_end.next
				rem = rem.next
			if carry == 1:
				res_end.next = ListNode(1)
				res_end = res_end.next
			return res

