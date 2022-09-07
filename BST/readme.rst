
Binary Search Tree 

  1. Validate BST - 
      Do inoder trasal and check if it is sorted.

  2. Construct BST - using a given sorted list
      Take the mid element in given list. Construct root with it.
      Pseudocode - 
          construct(list, start, end):
            if start > end:
              return None
            
            root = (list[mid])
            mid = start + (end-start)//2
            root.left = construct(list, start, mid-1)
            root.right = construct(list, mid+1, end)
            return root
            
  3. Search BST
  
  4. Insert into BST.
  5. Delete a node from BST.
