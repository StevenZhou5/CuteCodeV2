package wg_test

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func Test01() {
	wg := sync.WaitGroup{}

	wg.Add(1)
	go func() {
		defer wg.Done()
		count := rand.Intn(20)
		fmt.Printf("任务一的执行次数：%+v\n", count)
		for i := 0; i < count; i++ {
			fmt.Printf("任务1执行中：%+v\n", i)
			time.Sleep(time.Second)
		}
	}()

	wg.Add(1)
	go func() {
		wg.Done()
		count := rand.Intn(20)
		fmt.Printf("任务二的执行次数：%+v\n", count)
		for i := 0; i < count; i++ {
			fmt.Printf("任务2执行中：%+v\n", i)
			time.Sleep(time.Second)
		}
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		count := rand.Intn(20)
		fmt.Printf("任务三的执行次数：%+v\n", count)
		for i := 0; i < count; i++ {
			fmt.Printf("任务3执行中：%+v\n", i)
			time.Sleep(time.Second)
		}
	}()

	wg.Wait()
	fmt.Printf("所有任务都执行完毕！\n")
}
