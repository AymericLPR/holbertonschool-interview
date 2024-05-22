#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    n = len(boxes)
    keys = set(boxes[0])
    unlocked = {0}
    visited = set()

    while keys:
        key = keys.pop()
        if key < n and key not in visited:
            unlocked.add(key)
            visited.add(key)
            keys.update(boxes[key])

    return len(unlocked) == n
