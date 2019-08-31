#!/usr/bin/env python3
import unittest

LOOP_TABLE = [
    [0],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [2, 4, 6, 8, 0],
    [3, 6, 9, 2, 5, 8, 1, 4, 7, 0],
    [4, 8, 2, 6, 0],
    [5, 0],
    [6, 2, 8, 4, 0],
    [7, 4, 1, 8, 5, 2, 9, 6, 3, 0],
    [8, 6, 4, 2, 0],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]

def solve(n, m):
    if n < m:
        return 0
    ans = 0
    final_digit = m % 10
    if final_digit == 0:
        return 0
    tab = LOOP_TABLE[final_digit]
    ans = n // m // len(tab) * sum(tab)
    # print("ZZZZZZ", ans, sum(tab), n // m // len(tab))
    ans += sum(tab[:n // m % len(tab)])
    return ans


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(solve(1, 1), 1)

    def test2(self):
        self.assertEqual(solve(10, 1), 45)
    
    def test3(self):
        self.assertEqual(solve(100, 3), 153)

    def test4(self):
        self.assertEqual(solve(1024, 14), 294)

    def test5(self):
        self.assertEqual(solve(998244353, 1337), 3359835)
    
    def test6(self):
        self.assertEqual(solve(123, 144), 0)

    def test7(self):
        self.assertEqual(solve(1234312817382646, 13), 427262129093995)


if __name__ == "__main__":
    q = int(input())
    for _ in range(0, q):
        n, m = [int(i) for i in input().split()]
        print(solve(n, m))
