#!/usr/bin/env python3
import unittest


def solve(n, x):
    cnto = cnte = 0
    for i in x:
        if i % 2 == 0:
            cnto += 1
        else:
            cnte += 1
    return min(cnto, cnte)


class TestCase(unittest.TestCase):
    def test1(self):
        n = 3
        x = [1, 2, 2]
        self.assertEqual(solve(n, x), 1)


if __name__ == "__main__":
    n = int(input())
    x = [int(i) for i in input().split()]
    print(solve(n, x))
