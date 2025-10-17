# Basic Tree Traversal Solutions

This document contains Python solutions for basic tree traversal problems, including recursive and iterative approaches for preorder, inorder, postorder, and zigzag traversals, as well as N-ary tree traversals.

---

## 1. Preorder Traversal (Recursive)

```python
def preordertraversal(root):
    if not root:
        return
    print(root.data)
    preordertraversal(root.left)
    preordertraversal(root.right)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
```

---

## 2. Inorder Traversal (Recursive)

```python
def inordertraversal(root):
    if not root:
        return
    inordertraversal(root.left)
    print(root.data)
    inordertraversal(root.right)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
```

---

## 3. Postorder Traversal (Recursive)

```python
def postordertraversal(root):
    if not root:
        return
    postordertraversal(root.left)
    postordertraversal(root.right)
    print(root.data)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
```

---

## 4. Preorder Traversal (Iterative)

```python
# Python program to perform iterative preorder traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iterativePreorder(root):
    if root is None:
        return
    nodeStack = []
    nodeStack.append(root)
    while (len(nodeStack) > 0):
        node = nodeStack.pop()
        print(node.data, end=" ")
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

def preorderApproach2(root):
    stack = []
    curr = root
    ans = []
    while stack or curr:
        if curr:
            ans.append(curr.data)
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack.pop()
            curr = temp.right
    return ans
```

---

## 5. Inorder Traversal (Iterative)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack.pop()
            print(temp.data)
            curr = temp.right
```

---

## 6. Postorder Traversal (Iterative)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorderApproach2(root):
    stack = []
    curr = root
    ans = []
    while stack or curr:
        if curr:
            ans.append(curr.data)
            stack.append(curr)
            curr = curr.right
        else:
            temp = stack.pop()
            curr = temp.left
    return ans[::-1]
```

---

## 7. Zigzag Level Order Traversal

```python
import collections
class Solution:
    def zigzagLevelOrder(self, root):
        ans=[]
        flag=0
        q=collections.deque()
        q.append(root)
        while q:
            level=[]
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if flag:
                    ans.append(level[::-1])
                    flag=0
                else:
                    ans.append(level)
                    flag=1
        return ans
```

---

## 8. N-ary Tree Preorder Traversal

```python
class Solution:
    def preorder(self, root):
        if not root:
            return None
        stack = []
        ans = []
        stack.append(root)
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            stack.extend(temp.children[::-1])
        return ans
```

---

## 9. N-ary Tree Postorder Traversal

```python
class Solution:
    def postorder(self, root):
        if not root:
            return None
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.val)
                stack.extend(temp.children)
        return ans[::-1]
```
