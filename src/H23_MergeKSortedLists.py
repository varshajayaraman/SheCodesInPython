# from Queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i))
        heapq.heapify(heap)
        # print(heap)
        # heapq.heapify(heap)
        head = None
        if len(lists) == 0:
            return None
        head = None
        while len(heap) > 0:
            # print(heap, head)
            if not head:
                val, ind = heapq.heappop(heap)
                lists[ind] = lists[ind].next
                node = lists[ind]
                # node = node.next
                if node:
                    heapq.heappush(heap, (node.val, ind))
                head = ListNode(val)
                temp = head
            else:
                # print(heap)
                val, ind = heapq.heappop(heap)
                lists[ind] = lists[ind].next
                node = lists[ind]
                # node = node.next
                if node:
                    # print("Node: ", node.val, node, heap)
                    heapq.heappush(heap, (node.val, ind))
                # print("After removing: ", val, ind, "heap: ", heap)
                temp.next = ListNode(val)
                temp = temp.next
        return head
