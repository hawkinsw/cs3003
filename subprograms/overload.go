package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

func minimum[T constraints.Ordered](a T, b T) T {
	if a < b {
		return a
	} else {
		return b
	}
}

func main() {
	fmt.Printf("min(5, 4): %v\n", minimum(5, 4))
	fmt.Printf("min('a', 'b'): %v\n", minimum("a", "b"))
}
