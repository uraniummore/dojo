class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _update_result(self, value: int) -> None:
        if self.node_to_change.val is None:
            self.node_to_change.val = value
        else:
            new_node = ListNode(value)
            self.node_to_change.next = new_node
            self.node_to_change = new_node

    def _rotate_node(self, node_id: int) -> None:
        current_node = self.current_nodes[node_id]
        self.current_nodes[node_id] = current_node.next if current_node else None

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.result = ListNode(None)
        self.node_to_change = self.result

        self.current_nodes = [l1, l2]

        while True:
            numbers = [node.val if node else None for node in self.current_nodes]

            num_1 = numbers[0]
            num_2 = numbers[1]

            if all(num is None for num in numbers):
                break

            print(numbers)

            if not None in numbers:
                if num_1 < num_2:
                    self._update_result(num_1)
                    self._rotate_node(0)
                elif num_1 > num_2:
                    self._update_result(num_2)
                    self._rotate_node(1)
                elif num_1 == num_2:
                    self._update_result(num_1)
                    self._update_result(num_2)
                    self._rotate_node(0)
                    self._rotate_node(1)
            else:
                if num_1 is None:
                    self._update_result(num_2)
                    self._rotate_node(1)
                elif num_2 is None:
                    self._update_result(num_1)
                    self._rotate_node(0)

        return self.result if self.result.val is not None else None
