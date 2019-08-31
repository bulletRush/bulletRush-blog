#!/usr/bin/env python3
import unittest


def solve(n, a):
    ans = 0
    min = 100000000
    i = n - 1
    while i >= 0:
        if a[i] > min:
            ans += 1
            # print("xxxx", i, a[i], min, ans)
        elif a[i] < min:
           min = a[i]
        i -= 1
    return ans


class TestCase(unittest.TestCase):
    def test1(self):
        n = 10
        x = [31, 41, 59, 26, 53, 58, 97, 93, 23, 84]
        self.assertEqual(solve(n, x), 8)


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(solve(n, a))
