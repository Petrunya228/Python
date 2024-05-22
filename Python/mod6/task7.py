class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def restore_tree(log_file_path):
    node_map = {}

    with open(log_file_path, 'r') as file:
        for line in file:
            node_num, left_child_num, right_child_num = map(int, line.strip().split())
            if node_num not in node_map:
                node_map[node_num] = BinaryTreeNode(node_num)
            if left_child_num != -1:
                if left_child_num not in node_map:
                    node_map[left_child_num] = BinaryTreeNode(left_child_num)
                node_map[node_num].left = node_map[left_child_num]
            if right_child_num != -1:
                if right_child_num not in node_map:
                    node_map[right_child_num] = BinaryTreeNode(right_child_num)
                node_map[node_num].right = node_map[right_child_num]

    return node_map[1]  # Возвращаем корень дерева (узел с номером 1)


# Пример построения бинарного дерева
root = BinaryTreeNode(1)
root.left = node2 = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
node2.left = BinaryTreeNode(4)
node2.right = BinaryTreeNode(5)

# Пример записи логов в файл и восстановления дерева
with open('tree_logs.txt', 'w') as file:
    file.write("1 2 3\n2 4 5\n4 -1 -1\n5 -1 -1\n3 -1 -1\n")

restored_root = restore_tree('tree_logs.txt')
