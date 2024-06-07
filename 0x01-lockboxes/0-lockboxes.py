#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    We have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys to the other
    boxes.
    This function determines if all the boxes can be opened.

    Parameters:
    boxes: The list of boxes with some keys in each one (list of lists).

    Return:
    True if all boxes can be opened, False otherwise.
    """
    opened_boxes = [0]
    n = len(boxes)
    for opened_box in opened_boxes:
        for key in boxes[opened_box]:
            if key not in opened_boxes and 0 < key < n:
                opened_boxes.append(key)

    if len(opened_boxes) == n:
        return True
    return False
