## 트리구조

- 트리는 하나의 루트 노드를 갖는다.
- 루트 노드는 0개 이상의 자식 노드를 갖고 있다
- 그 자식 노드 또한 0개 이상의 자식 노드를 갖고 있고, 이는 반복적으로 정의된다.



<img src="C:\Users\배태한\Desktop\work\02_mine\TIL\00_Documents\img\tree.png" style="zoom: 50%;" />

- 루트 노드: 부모가 없는 노드로 단 하나만 존재할 수 있다.
- 단말 노드(leaf node): 자식이 없는 노드. 말단 노드, 잎 노드라고도 한다.
- 내부 노드(internal node): 단말 노드가 아닌 노드
- 간선(edge): 노드를 연결하는 선
- 형제 노드(siblings): 같은 부모를 가지는 노드
- 노드의 크기(size): 자신을 포함한 모든 자손 노드의 개수
- 노드의 깊이(depth): 루트에서 어떤 노드에 도달하기 위해 거쳐야 하는 간선의 수
- 노드의 레벨(level): 트리의 특정 깊이를 가지는 노드의 집합
- 노드의 차수(degree): 각 노드가 지닌 가지의 수
- 트리의 차수: 트리의 최대 차수 (트리에 포함된 노드들 중 가장 많은 차수를 가진 노드의 차수)
- 트리의 높이: 루트 노드에서 가장 아래에 있는 노드의 깊이



## 이진트리

- 각 노드가 최대 두개의 자식을 갖는 트리
- 모든 트리가 이진 트리는 아니다
- 트리 순회 방법



![](C:\Users\배태한\Desktop\work\02_mine\TIL\00_Documents\img\tree2.png)

```python
class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = self.right = None
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
```



### 1. 전위 순회

- 자식 노드를 확인하기 전에 서브 트리의 루트를 먼저 확인한 후 자식 노드를 확인하는 순회 방법이다.
- 자식 노드를 확인할 때는 왼쪽 노드부터 확인한다.

```python
def preorder(self):
        def _preorder(node):
            print(node.item, end=' ')
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
        
# preorder
# 1 2 4 8 5 3 6 7
```



### 2. 중위 순회

- 중위 순회는 왼쪽 자식 노드, 루트 노드, 오른쪽 자식 노드 순으로 값을 확인하는 방법이다.
- 자식 노드를 확인하고 밑에 자손 노드들이 있다면 자손 노드들도 동일한 방식으로 확인한다.

```python
def inorder(self):
    def _inorder(node):
        if node.left:
            _inorder(node.left)
        print(node.item, end=' ')
        if node.right:
            _inorder(node.right)
    _inorder(self.root)

# inorder
# 8 4 2 5 1 6 3 7
```



### 3. 후위 순회

- 후위 순회는 자식 노드를 모두 확인한 후에 루트 노드를 확인하는 순회 방법이다.
- 자식 노드의 자손 노드가 존재한다면 동일한 방식으로 모두 확인한다.

```python
def postorder(self):
    def _postorder(node):
        if node.left:
            _postorder(node.left)
        if node.right:
            _postorder(node.right)
        print(node.item, end=' ')
    _postorder(self.root)
    
# postorder
# 8 4 5 2 6 7 3 1
```



