# LEETCODE_2196-Create-Binary-Tree-From-Descriptions
Level: Medium, Language: Python, Concept: Binary Tree

This repository contains a Python implementation to create a binary tree from a given set of descriptions. The descriptions specify parent-child relationships and whether the child is a left or right child of the parent.

## Problem Description

Given a list of descriptions, where each description is a list of three integers `[parent, child, is_left]`:

- `parent` is the value of the parent node.
- `child` is the value of the child node.
- `is_left` is a boolean (1 or 0) that indicates whether the child is a left child (1) or a right child (0).

The goal is to create a binary tree from these descriptions and return the root node of the tree.

## Solution

The solution involves the following steps:

1. Parse the descriptions to create nodes and track child nodes.
2. Identify the root node as the node that is never a child in any description.
3. Construct the binary tree by linking parent and child nodes based on the descriptions.

## Code

### TreeNode Class

The `TreeNode` class is used to create nodes for the binary tree.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
