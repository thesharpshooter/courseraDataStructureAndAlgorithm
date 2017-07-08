# python3

import sys, threading
sys.setrecursionlimit(10**6) 
threading.stack_size(2**27)  

class TreeOrders:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		self.array = []
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a
			self.left[i] = b
			self.right[i] = c
			self.array.append(a)

	def inOrder(self):
		result = []
		
		def inOrderRecursive(i,result):
			if self.left[i] != -1:
				inOrderRecursive(self.left[i], result)
			result.append(self.key[i])
			if self.right[i] != -1:
				inOrderRecursive(self.right[i], result)
		inOrderRecursive(0, result)
					
		return result

	def preOrder(self):
		result = []
		
		def preOrderRecursive(i,result):
			result.append(self.key[i])
			if self.left[i] != -1:
				preOrderRecursive(self.left[i], result)
			if self.right[i] != -1:
				preOrderRecursive(self.right[i], result)
		preOrderRecursive(0, result)
					
		return result

	def postOrder(self):
		result = []
		def postOrderRecursive(i,result):
			if self.left[i] != -1:
				postOrderRecursive(self.left[i], result)
			if self.right[i] != -1:
				postOrderRecursive(self.right[i], result)
			result.append(self.key[i])
		postOrderRecursive(0, result)
					
		return result

def main():
	tree = TreeOrders()
	tree.read()
	if tree.n == 0:
		print ("CORRECT")
	elif tree.inOrder() == sorted(tree.array):
		print ("CORRECT")
	else:
		print ("INCORRECT")
	

threading.Thread(target=main).start()