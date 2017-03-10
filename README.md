# BinaryTree

## Discription
This is a binary tree representation that allows user to create a binary tree by providing the serialized string representation of the binary tree.
It also provides `preOrderIter`, `inOrderIter`, `postOrderIter` and `bfsIter` iterators that iterates through the elements in a binary in
corresponding manner.

## Usage
*Input*: the result of BFS traversal of the target binary tree, `None` is represented as `#`. For example, the result of BFS traversal of
the binary tree below is: `[8, 3, 10, 1, 6, #, 14, #, #, 4, 7, 13, #, #, #, #, #, #, #]`
<p align="center">
  <a href="http://imgur.com/i2siK9C"><img src="http://i.imgur.com/i2siK9C.png" title="source: imgur.com" /></a>
</p>

to create a binary tree instance of it
```python
from BinaryTree.binaryTree import binaryTree

sampleBT = binaryTree('[8, 3, 10, 1, 6, #, 14, #, #, 4, 7, 13, #, #, #, #, #, #, #]')
```
now we have the binary tree instance, we can iterate through its elements in different manners:

+ default(preorder interation):

```python
for val in sampleBt:
    print(val)
```
result: `8 3 1 6 4 7 10 14 13`
+ preorder iteration:

```python
for val in sampleBt.preOrderIter():
    print(val)
```
result: `8 3 1 6 4 7 10 14 13`
+ inorder iteration:

```python
for val in sampleBt.inOrderIter():
    print(val)
```
result: `1 3 4 6 7 8 10 13 14`
+ postorder iteration:

```python
for val in sampleBt.postOrderIter():
    print(val)
```
result: `1 4 7 6 3 13 14 10 8`

+ BFS iteration:

```python
for val in sampleBt.bfsIter():
    print(val)
```

result:`8 3 10 1 6 14 4 7 13`
