# Binary Tree Problems – LeetCode Study Guide
## HINTS

1. Always remember the return type. Same should be present in base as well as every return statement.
2. 

This repository contains solutions to common **Binary Tree** problems on LeetCode.  
Each entry includes the problem (linked), difficulty, a short hint, and a link to the local solution file.

---

## Problems

| Sl. No. | Problem | Description | Difficulty | Hint | Solution File |
|---------|----------|-------------|------------|------|---------------|
| 1 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Flip every node's left and right children. | Easy | Recursively or iteratively swap left and right child nodes. | [01_invert_binary_tree.py](01_invert_binary_tree.py) |
| 2 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Number of nodes along the longest path from root to farthest leaf. | Easy | Depth = `1 + max(depth(left), depth(right))`. | [02_max_depth_of_binary_tree.py](02_max_depth_of_binary_tree.py) |
| 2.1 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Minimum nodes from root to nearest leaf (handle single-child cases). | Easy | Handle - If one child is None, we must go through the other coz min is always 0 in base case. | [02_max_depth_of_binary_tree.py](02_max_depth_of_binary_tree.py) |
| 3 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Maximum length of a path between two nodes in a binary tree is the number of edges between the nodes. | Easy | Track `max(leftDepth + rightDepth)` at each node. | [03_diameter_of_binary_tree.py](03_diameter_of_binary_tree.py) |
| 4 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Every node's left and right subtree heights differ by at most 1. | Easy | Check if subtrees are balanced and height difference ≤ 1. | [04_balanced_binary_tree.py](04_balanced_binary_tree.py) |
| 5 | [Same Tree](https://leetcode.com/problems/same-tree/) | Check if two trees are structurally identical and have equal node values. | Easy | Recursively check structure and values of both trees. | [05_same_tree.py](05_same_tree.py) |
| 6 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Determine if one tree is a subtree of another by matching subtrees. | Easy | For each node, check if it matches `subRoot` using `isSameTree`. | [06_subtree_of_another_tree.py](06_subtree_of_another_tree.py) |
| 7 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Find lowest common ancestor using BST ordering properties. | Medium | Use BST property: decide left/right, else current root is LCA. | [07_lca_of_bst.py](07_lca_of_bst.py) |
| 8 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Return tree nodes level-by-level (breadth-first). | Medium | BFS with queue, process nodes level by level. | [08_level_order_traversal.py](08_level_order_traversal.py) |
| 9 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Nodes visible when viewing the tree from the right side. | Medium | BFS and record last node of each level. | [09_right_view.py](09_right_view.py) |
| 10 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Count nodes greater than or equal to max value along the root→node path. | Medium | Node is "good" if it’s ≥ max value along root→node path. | [10_count_good_nodes.py](10_count_good_nodes.py) |
| 11 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Ensure each node satisfies BST min/max constraints for its subtree. | Medium | Ensure all nodes lie within `(min, max)` range recursively. | [11_validate_bst.py](11_validate_bst.py) |
| 12 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Return the k-th smallest value using inorder traversal. | Medium | Inorder traversal gives sorted order → track k-th element. | [12_kth_smallest_elem_in_bst.py](12_kth_smallest_elem_in_bst.py) |
| 13 | [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Reconstruct the binary tree using preorder for root order and inorder for left/right partitioning. | Medium | Preorder gives root; use inorder index map for left/right. | [13_construct_binary_from_inorder_preorder.py](13_construct_binary_from_inorder_preorder.py) |
| 14 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Maximum path sum across any path in the tree (path can start/end at any node). | Hard | Max path = max gain left + right + node value. Track global max. | [14_binary_tree_maximum_path_sum.py](14_binary_tree_maximum_path_sum.py) |
| 15 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Encode a tree to a string and rebuild it using `None` markers for missing children. | Hard | Use BFS/DFS with `None` markers to store and rebuild tree. | [15_serialize_deserialize_bst.py](15_serialize_deserialize_bst.py) |

---

## How to Run
Each problem’s solution is available in its respective Python file under this folder.  

Run with:

```bash
python3 problem_file.py
