package main
 
import "fmt"
 
func solve(n int, a []int) int {
	var ans int = 0
	var min int = 100000000
    for i := n-1; i >= 0; i-- {
		if a[i] > min {
			ans += 1
		} else if a[i] < min {
			min = a[i]
		}
	}
	return ans
}


func main() {
    var t int
    fmt.Scanf("%d\n", &t)
    for i := 0; i < t; i++ {
		var n int
		var a []int

		fmt.Scanf("%d\n", &n)

		for j:=0; j < n; j++ {
			var ai int
			fmt.Scanf("%d", &ai)
			a = append(a, ai)
		}
		ret := solve(n, a)
		fmt.Println(ret)
    }
}