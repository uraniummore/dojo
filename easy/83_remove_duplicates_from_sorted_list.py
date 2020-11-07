class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = node_to_modify = None
        occurrences = []
        current_node = head

        while not current_node is None:
            current_value = current_node.val

            if current_value not in occurrences:
                occurrences.append(current_value)
                if not (result and node_to_modify):
                    result = node_to_modify = ListNode(current_value)
                else:
                    new_node = ListNode(current_value)
                    node_to_modify.next = new_node
                    node_to_modify = node_to_modify.next
                    current_node = current_node.next
            else:
                current_node = current_node.next

        return result


if __name__ == '__main__':
    node_1 = ListNode(1)
    node_2 = ListNode(1)
    node_3 = ListNode(2)

    node_1.next = node_2
    node_2.next = node_3

    Solution().deleteDuplicates(node_1)
