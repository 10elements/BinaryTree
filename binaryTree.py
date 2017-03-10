from .treeNode import treeNode
from collections import deque

class binaryTree(object):
	""" 
	A binary tree representation that supports deserialization from strings of serialized bianry trees, preOrder, inOrder and postOrder itertation.
	"""

	def __init__(self, data = None):
		if data == None:
			self.root = None
		else:
			try:
				self.root = binaryTree.serialize(data)
			except Exception as e:
				raise e

	def __iter__(self):
		"""
		default iterator set to preorder itertator
		"""
		return self.preOrderIter()

	@staticmethod
	def serialize(data):
		"""
		Decodes your encoded data to construct a binary tree.

		:type data: str
		:rtype: treeNode
		"""
		if data == None:
			raise TypeError('input can not be None')
		if not isinstance(data, str):
			raise TypeError('input must be str')
		if len(data) < 3 or not data.startswith('[') or not data.endswith(']'):
			raise TypeError('input must be surrounded by brackets and can not be empty')
		data = data[1:-1]
		datas = data.split(', ')
		if datas[0] == '#':
		    return None
		i = 1
		l = len(datas)
		root = treeNode(datas[0])
		frontier = [root]
		while i < l:
		    t = []
		    for n in frontier:
		        if datas[i] != '#':
		            n.left = treeNode(datas[i])
		            t.append(n.left)
		        i += 1
		        if datas[i] != '#':
		            n.right = treeNode(datas[i])
		            t.append(n.right)
		        i += 1
		    frontier = t
		return root

	def inOrderIter(self):
		"""
		inOrder iterator
		"""
		if self.root:
			stack = [self.root]
			visited = {}
			while len(stack):
				cur = stack[-1]
				if not cur.left or cur.left in visited:
					stack.pop()
					visited[cur] = True
					yield cur.val
					if cur.right:
						stack.append(cur.right)
				else:
					stack.append(cur.left)
		raise StopIteration

	def preOrderIter(self):
		"""
		preOrder iterator
		"""
		if self.root:
			stack = [self.root]
			while len(stack):
				cur = stack.pop()
				yield cur.val
				if cur.right:
					stack.append(cur.right)
				if cur.left:
					stack.append(cur.left)
		raise StopIteration

	def postOrderIter(self):
		"""
		postOrder iterator
		"""
		if self.root:
			stack = [self.root]
			visited = {}
			while len(stack):
				cur = stack[-1]
				if (not cur.left or cur.left in visited) and (not cur.right or cur.right in visited):
					stack.pop()
					visited[cur] = True
					yield cur.val
				elif cur.left and cur.left not in visited:
					stack.append(cur.left)
				else:
					stack.append(cur.right)
		raise StopIteration

	def bfsIter(self):
		"""
		bfs iterator
		"""
		if self.root:
			queue = deque([self.root])
			while len(queue):
				front =  queue.popleft()
				yield front.val
				if front.left:
					queue.append(front.left)
				if front.right:
					queue.append(front.right)
		raise StopIteration

