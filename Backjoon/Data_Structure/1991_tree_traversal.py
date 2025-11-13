"""
backjoon_1991 - 트리 순회 - S1

문제
- 이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회한 결과를 출력

풀이
- 노드 값들이 주어지기 때문에 트리에 값들을 먼저 넣는다.
- 그리고 순회 방식에 따른 결과를 출력한다.
"""

# 이진 트리 클래스 생성
class Binary_tree:
    def __init__(self, len):
        self.tree = {}
    
    def new_node(self, parent, left, right):
        self.tree.setdefault(parent, (left, right))

    def preorder(self, root):
        if root not in self.tree and root == '.':
            return
        print(root, end='')
        left, right = self.tree[root]
        self.preorder(left)
        self.preorder(right)
    
    def inorder(self, root):
        if root not in self.tree and root == '.':
            return
        left, right = self.tree[root]
        self.inorder(left)
        print(root, end='')
        self.inorder(right)
    
    def postorder(self, root):
        if root not in self.tree and root == '.':
            return
        left, right = self.tree[root]
        self.postorder(left)
        self.postorder(right)  
        print(root, end='')

N = int(input())

# 클래스 변수 선언
my_tree = Binary_tree(N)
for _ in range(N):
    parent, left, right = input().split()
    my_tree.new_node(parent, left, right)

my_tree.preorder('A')
print()
my_tree.inorder('A')
print()
my_tree.postorder('A')
print()
