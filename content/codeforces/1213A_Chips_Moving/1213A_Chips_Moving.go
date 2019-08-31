package main
 
import "fmt"
 
func solve(n int, x []int) int {
	var co int = 0 
	var ce int = 0
    for i := 0; i < n; i++ {
		if x[i] % 2 == 0 {
			co += 1
		} else{
			ce += 1
		}
	}
	if co >= ce {
		return ce
	}
	return co
}


func main() {
    var n int
    var x []int
    fmt.Scanf("%d\n", &n)
    for i := 0; i < n; i++ {
		var xi int
		// 抄示例输入抄了一个scanf %x...
        fmt.Scanf("%d", &xi)
        x = append(x, xi)
    }
	ret := solve(n, x)
    fmt.Println(ret)
}