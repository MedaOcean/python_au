
+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)<---end.markdown links--->

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

``` python
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    leftN = self.maxDepth(root.left)
    rightN = self.maxDepth(root.right)
    return max(leftN, rightN)+1
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

``` python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return []
    if root.left is None:
        l = []
    else:
        l = self.inorderTraversal(root.left)
    if root.right is None:
        r = []
    else:
        r = self.inorderTraversal(root.right)
    return l + [root.val] + r
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

``` python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root is None:
        return None
    else:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

``` python
def __init__(self, root: TreeNode):
    self.nodes_sorted = []
    self.index = -1
    self._inorder(root)
def _inorder(self, root):
    if root is None:
        return
    self._inorder(root.left)
    self.nodes_sorted.append(root.val)
    self._inorder(root.right)
def next(self) -> int:
    self.index += 1
    return self.nodes_sorted[self.index]
def hasNext(self) -> bool:
      return self.index + 1 < len(self.nodes_sorted)

```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

``` python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return None
    cur = []
    cur.append(root)
    temp = []
    val = []
    res = []
    while cur:
        for node in cur:
            val.append(node.val)
            if node.left is not None:
                temp.append(node.left)
            if node.right is not None:
                temp.append(node.right)
        res.append(val)
        cur = temp
        val = []
        temp = []
    return res
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

``` python
def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack = []
    while root:
        stack.append(root)
        root = root.left
    root = stack.pop()
    k -= 1
    if not k:
        return root.val
    root = root.right
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

``` python
def isValidBST(self, root: TreeNode) -> bool:
    traversed = self.inorder(root)
    if len(traversed) == len(set(traversed)):
        traversed = sorted(traversed)
        return traversed
    else:
        return False
def inorder(self, root):
    if root is None:
        return []
    return self.inorder(root.left) + [root.val] + self.inorder(root.right)

```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

``` python
def isSymmetric(self, root: TreeNode) -> bool:
    return self.ismirror(root,root)
def ismirror(self,tree_1:TreeNode, tree_2:TreeNode):
    if tree_1 is None and tree_2 is None:
        return True
    elif tree_1 is None or tree_2 is None:
        return False
    return (tree_1.val == tree_2.val) and self.ismirror(tree_1.right, tree_2.left) and self.ismirror(tree_1.left, tree_2.right)

```