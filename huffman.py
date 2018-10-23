from heapq import heappush, heappop
def BinaryTreeToString(root):
  if root.symbol is not None: return root.symbol
  else: return "(%s%s)"%(BinaryTreeToString(root.left), BinaryTreeToString(root.right))
# Represents a Huffman tree for use in encoding/decoding strings.
# A sample usage is as follows:
#
# h = HuffmanTree([('A', 2), ('B', 7), ('C', 1)])
# assert(h.encode('ABC') == '01100')
# assert(h.decode(h.encode('ABC')) == 'ABC')
class HuffmanTree:
  # Helper object for building the Huffman tree.
  # You may modify this constructor but the grading script rlies on the left, right, and symbol fields.
  class TreeNode:
    def __init__ (self, symbol = None, min_element = None):
      self.left = None
      self.right = None
      self.symbol = symbol
      self.min_element = min_element

  # The `symbol_list` argument should be a list of tuples `(symbol, weight)`,
  # where `symbol` is a symbol that can be encoded, and `weight` is the
  # the unnormalized probabilitiy of that symbol appearing.
  def __init__(self, symbol_list):
    assert(len(symbol_list) >= 2)
    #Creating a tuple of three
    #First element: weight
    #Second element: lexographic symbol
    #Third element: a tree node
    symbol_list = map(lambda x: (x[1], x[0], self.TreeNode(x[0], x[0])), symbol_list)

    heap = []

    for item in symbol_list:
      heappush(heap, item)

    while len(heap) > 1:
      left = heappop(heap)
      right = heappop(heap)

      node = self.TreeNode()
      if left[0] == right[0]:
          if left[1] < right[1]:
              node.left = left[2]
              node.right = right[2]
          else:
              node.left = right[2]
              node.right = left[2]
      else:
          node.left = left[2]
          node.right = right[2]

      if left[1] < right[1]:
          node.min_element = left[1]
      else:
          node.min_element = right[1]

      node = (left[0] + right[0], node.min_element, node)

      heappush(heap, node)


    # Tree is done

    # Each stack element has three items
    # First element: TreeNode
    # Left visited: boolean
    # Right visited: boolean
    root = [heappop(heap)[2], False, False]

    self.root = root[0]

    stack = []
    path = ''
    self.encoding = {}

    stack.append(root)

    while stack:
      current_node = stack[-1] # (node, False, False)

      # The case when the current_node is a leaf node
      if current_node[0].left == None:
        self.encoding[current_node[0].symbol] = path
        path = path[:-1]
        stack.pop(-1)

      # The case when the current_node is not a leaf node
      else:
        if current_node[1] == False:
          next_node = current_node[0].left
          stack[-1][1] = True
          stack.append([next_node, False, False])
          path += '0'

        elif current_node[2] == False:
          next_node = current_node[0].right
          stack[-1][2] = True
          stack.append([next_node, False, False])
          path += '1'

        else:
          stack.pop(-1)
          path = path[:-1]

  # Encodes a string of characters into a string of bits using the
  # symbol/weight list provided.
  def encode(self, s):
    assert(s is not None)
    output = ""
    for char in s:
      output += self.encoding[char]

    return output

  # Decodes a string of bits into a string of characters using the
  # symbol/weight list provided.
  def decode(self, s):
    assert(s is not None)
    output = ""
    self.decoding = {v: k for k, v in self.encoding.items()}
    temp = ""
    for char in s:
      temp += char
      if temp in self.decoding.keys():
        output += self.decoding[temp]
        temp = ""
    if len(temp) > 0:
        output = None

    return output
