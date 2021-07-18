package main

import (
	"fmt"
	"time"
)

func main() {
	//fmt.Printf("生成随机数：%+v\n", rand.Intn(100))
	//wg_test.Test01()
	fmt.Printf("start\n")
	//for range time.Tick(time.Second * 5) {
	//	fmt.Printf("1111")
	//}
	hour := time.Now().Unix() % 86400 / 3600
	fmt.Printf("end:%v,\n", hour)
}
