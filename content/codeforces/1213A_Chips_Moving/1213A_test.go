package main

import (
	"testing"
)

func TestSolve(t *testing.T) {
	var n int = 3
	x := [...]int{1, 2, 3}
	ret := solve(n, x[:])
	if ret != 1 {
		t.Error("failed")
	}
}

func TestSolve1(t *testing.T) {
	var n int = 5
	x := [...]int{2, 2, 2, 3, 3}
	ret := solve(n, x[:])
	if ret != 2 {
		t.Error("failed")
	}
}

func TestSolve2(t *testing.T) {
	var n int = 9
	x := [...]int{586353869, 450116253, 427810003, 492840095, 862100173, 363622697, 535556487, 364988743, 637564323, 411267865}
	ret := solve(n, x[:])
	if ret != 0 {
		t.Error("failed")
	}
}