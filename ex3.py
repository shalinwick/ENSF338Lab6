import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_node(op_stack, num_stack):
    op = op_stack.pop()
    right_child = num_stack.pop()
    left_child = num_stack.pop()
    parent = TreeNode(op)
    parent.left = left_child
    parent.right = right_child
    num_stack.append(parent)

def parse_expression(expression_tokens):
    numbers = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    for token in expression_tokens:
        if token.isdigit():
            numbers.append(TreeNode(token))
        elif token in "+-*/":
            while operators and precedence[operators[-1]] >= precedence[token]:
                create_node(operators, numbers)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                create_node(operators, numbers)
            operators.pop()

    while operators:
        create_node(operators, numbers)

    return numbers.pop()

def eval_tree(node):
    if node.value.isdigit():
        return int(node.value)
    else:
        left = eval_tree(node.left)
        right = eval_tree(node.right)
        if node.value == '+':
            result = left + right
        elif node.value == '-':
            result = left - right
        elif node.value == '*':
            result = left * right
        elif node.value == '/':
            result = left / right

        return int(result) if result.is_integer() else result

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py '<expression>'")
        sys.exit(1)

    tokens = sys.argv[1].split()
    root = parse_expression(tokens)
    print(eval_tree(root))

if __name__ == "__main__":
    main()
