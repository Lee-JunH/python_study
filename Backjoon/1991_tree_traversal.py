"""
backjoon_1991 - 트리 순회 - S1

문제
- 이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회한 결과를 출력

풀이
- 노드 값들이 주어지기 때문에 트리에 값들을 먼저 넣는다.
- 그리고 순회 방식에 따른 결과를 출력한다.
"""

class tree_traversal():
    def __init__(self):
        pass
    
    def preorder(self, tree):
        pass
    
    def inorder(self):
        pass
    
    def postorder(self):
        pass

def inorder(t):
    


N = int(input())

node = [0 for _ in range(N+1)]
# 노드를 딕셔너리에 저장
tree = {}
for _ in range(N):
    parent, left, right = input().split()
    tree.setdefault(parent, [])
    if left != '.' and right != '.':
        tree[parent].extend([left, right])
    elif left != '.':
        tree[parent].append(left)
    elif right != '.':
        tree[parent].append(right)

bin_tree = tree_traversal()

bin_tree.preorder(tree)
bin_tree.inorder(tree)
bin_tree.postorder(tree)

