
'''
堆是一种特殊的树结构，其中每个父节点小于或等于其子节点。然后它被称为Min Heap。
如果每个父节点大于或等于其子节点，则称它为最大堆。实施优先级队列是非常有用的，
在该队列中，具有较高权重的队列项目在处理中具有更高的优先级。有关堆的详细讨论，请访问我们的网站。
如果你是头部数据结构的新手，请先研究它。在本章中，我们将看到使用python实现堆数据结构。
创建一个堆

堆是通过使用python内建的名为heapq的库创建的。该库具有对堆数据结构进行各种操作的相关功能。以下是这些功能的列表。

    heapify - 此函数将常规列表转换为堆。在结果堆中，最小的元素被推到索引位置0.但其余的数据元素不一定被排序。
    heappush - 这个函数在堆中添加一个元素而不改变当前堆。
    heappop - 该函数返回堆中最小的数据元素。
    heapreplace - 该函数用函数中提供的新值替换最小的数据元素。
'''

'''
创建一个堆

通过简单地使用具有heapify函数的元素列表来创建堆。在下面的例子中，我们提供了一个元素列表，heapify函数重新排列了元素到最初位置的元素。

'''

import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

'''
插入堆

将数据元素插入堆总是在最后一个索引处添加元素。但是，只有在值最小的情况下，
您才可以再次应用heapify函数将新添加的元素添加到第一个索引。在下面的例子中，我们插入数字8。
'''
import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)

'''
从堆中移除

您可以使用此功能在第一个索引处移除元素。在下面的例子中，函数将始终删除索引位置1处的元素。
'''


import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)

'''

Python - 堆

    Python - 搜索树
    Python - 图形

堆是一种特殊的树结构，其中每个父节点小于或等于其子节点。然后它被称为Min Heap。如果每个父节点大于或等于其子节点，则称它为最大堆。实施优先级队列是非常有用的，在该队列中，具有较高权重的队列项目在处理中具有更高的优先级。有关堆的详细讨论，请访问我们的网站。如果你是头部数据结构的新手，请先研究它。在本章中，我们将看到使用python实现堆数据结构。
创建一个堆

堆是通过使用python内建的名为heapq的库创建的。该库具有对堆数据结构进行各种操作的相关功能。以下是这些功能的列表。

    heapify - 此函数将常规列表转换为堆。在结果堆中，最小的元素被推到索引位置0.但其余的数据元素不一定被排序。
    heappush - 这个函数在堆中添加一个元素而不改变当前堆。
    heappop - 该函数返回堆中最小的数据元素。
    heapreplace - 该函数用函数中提供的新值替换最小的数据元素。
'''
'''
创建一个堆

通过简单地使用具有heapify函数的元素列表来创建堆。在下面的例子中，我们提供了一个元素列表，heapify函数重新排列了元素到最初位置的元素。
'''
import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
'''


插入堆

将数据元素插入堆总是在最后一个索引处添加元素。但是，只有在值最小的情况下，您才可以再次应用heapify函数将新添加的元素添加到第一个索引。在下面的例子中，我们插入数字8。
'''
import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)


'''

从堆中移除

您可以使用此功能在第一个索引处移除元素。在下面的例子中，函数将始终删除索引位置1处的元素。
'''
import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)

'''

替换堆

heapreplace函数总是删除堆中最小的元素，并在未被任何顺序修复的地方插入新的传入元素。
'''

import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)

