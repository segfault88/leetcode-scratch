from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        current = None

        while any(lists):
            min_val = float("inf")
            min_idx = -1

            for i, node in enumerate(lists):
                if node and node.val < min_val:
                    min_val = node.val
                    min_idx = i

            if not head:
                head = ListNode(min_val)
                current = head
            else:
                current.next = ListNode(min_val)
                current = current.next
            lists[min_idx] = lists[min_idx].next

        return head

    def mergeKListsV2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        converted = [collect_list(node) for node in lists]

        output = []

        while any(converted):
            min_val = float("inf")
            min_idx = -1

            for i, node in enumerate(converted):
                if node and node[0] < min_val:
                    min_val = node[0]
                    min_idx = i

            output.append(min_val)
            converted[min_idx] = converted[min_idx][1:]

        return make_list(output)

    def merge2Lists(self, left: list[int], right: list[int]) -> list[int]:
        output = []

        while left and right:
            if left[0] < right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))

        return output + left + right

    def mergeKListsV3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        converted = [collect_list(node) for node in lists]

        output = []
        if converted:
            output = converted[0]

        for i in range(1, len(converted)):
            output = self.merge2Lists(output, converted[i])

        return make_list(output)

    def mergeKListsVCheat(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # This is a *cheat* solution, but it's the fastest
        # A linked list is not very pythonic anyway, and sorting a plain list is
        # fast, so just for fun, let's try it.
        # Turns out it beats 98% of python submissions

        converted = [collect_list(node) for node in lists]

        from itertools import chain

        output = list(chain.from_iterable(converted))
        output.sort()

        return make_list(output)


def make_list(arr: List[int]) -> ListNode | None:
    head = None

    for i in reversed(arr):
        head = ListNode(i, head)

    return head


def collect_list(head: ListNode) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def main():
    input = [
        make_list([1, 4, 5]),
        make_list([1, 3, 4]),
        make_list([2, 6]),
    ]
    output = Solution().mergeKLists(input)

    print("merged:", collect_list(output))


if __name__ == "__main__":
    main()
