package main

import (
	"testing"
)

func TestSolve(t *testing.T) {
	var n int = 6
	x := [...]int{3, 9, 4, 6, 7, 5}
	ret := solve(n, x[:])
	if ret != 3 {
		t.Error("failed")
	}
}

func TestSolve1(t *testing.T) {
	var n int = 1
	x := [...]int{1000000}
	ret := solve(n, x[:])
	if ret != 0 {
		t.Error("failed")
	}
}

func TestSolve2(t *testing.T) {
	var n int = 10
	x := [...]int{31, 41, 59, 26, 53, 58, 97, 93, 23, 84}
	ret := solve(n, x[:])
	if ret != 8 {
		t.Error("failed", ret)
	}
}