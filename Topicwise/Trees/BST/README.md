# Binary Search Tree (BST)

## 1. Validate BST
**Idea:** Perform an inorder traversal and check if the values are in sorted (strictly increasing) order.  
**Time Complexity:** O(n) (visit all nodes once)  
**Space Complexity:** O(h) (recursion stack, h = height of tree)

---

## 2. Construct BST (from a sorted list)
**Idea:** Always pick the middle element of the list/sublist as the root to ensure balance.  
**Time Complexity:** O(n)  
**Space Complexity:** O(log n) (recursion stack for balanced tree)

**Pseudocode:**
```python
def construct(arr, start, end):
    if start > end:
        return None

    mid = start + (end - start) // 2
    root = Node(arr[mid])

    root.left = construct(arr, start, mid - 1)
    root.right = construct(arr, mid + 1, end)

    return root
```

---

## 3. Search in BST
**Idea:**  
- If value is smaller than root → search left.  
- If value is greater than root → search right.  
- If value equals root → found.

**Time Complexity:** O(h) (h = height of tree, O(log n) if balanced, O(n) if skewed)  
**Space Complexity:** O(h) (recursion stack)

**Pseudocode:**
```python
def search(root, key):
    if root is None or root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)
```

---

## 4. Insert into BST
**Idea:** Traverse down the tree.  
- If value < node → go left.  
- If value > node → go right.  
- Insert when None is reached.

**Time Complexity:** O(h)  
**Space Complexity:** O(h)

**Pseudocode:**
```python
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root
```

---

## 5. Delete a Node from BST
**Cases:**  
- Node is a leaf → just remove it.  
- Node has one child → replace node with its child.  
- Node has two children →  
  - Find the inorder successor (smallest in right subtree).  
  - Replace node’s value with successor’s value.  
  - Delete successor node.

**Time Complexity:** O(h)  
**Space Complexity:** O(h)

**Pseudocode:**
```python
def deleteNode(root, key):
    if root is None:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Node found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Find inorder successor (smallest in right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left

        # Replace value
        root.val = successor.val

        # Delete successor
        root.right = deleteNode(root.right, successor.val)

    return root
```

---
