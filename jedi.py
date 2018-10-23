from heapq import heappush, heappop

heap = []
data = [(1, 'F'), (1,'H'), (1,'I'), (1,'L'), (1,'N'), (1,'R'), (1,'U'), (2,'A'), (2,'S'), (2,' '), (3,'T'), (5, "E")]
for item in data:
    heappush(heap, item)

for i in range(10):
    left = heappop(heap)
    print left
    right = heappop(heap)

    print right
    root = (left[0] + right[0], left[1])
    print root, "---------------------", i

    heappush(heap, root)

print "---------------------"

# left = heappop(heap)
# print left
# right = heappop(heap)
#
# print right
# root = (left[0] + right[0], left[1])
# print root, "---------------------"
#
# heappush(heap, root)
#
# left = heappop(heap)
# print left
# right = heappop(heap)
#
# print right
# root = (left[0] + right[0], left[1])
# print root, "---------------------"
#
# heappush(heap, root)

while heap:
    print(heappop(heap))
