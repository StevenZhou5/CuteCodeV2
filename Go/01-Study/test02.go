package main

import (
	"fmt"
	"time"
)

func newTask(i int) {
	for {
		fmt.Printf("newTask:%d\n", i)
		time.Sleep(time.Second)
	}
}

func main() {
	for _, val := range []int{0, 1} {
		fmt.Println(val)
	}
	for i := 0; i < 10; i++ {
		go newTask(i) // 使用go关键字即可创建协程
	}

	i := 0
	for {
		i++
		fmt.Println("this is a main goroutine")
		time.Sleep(time.Second)

		if i > 2 {
			break // 如果主协程退出，子协程也会全部退出
		}
	}

}
