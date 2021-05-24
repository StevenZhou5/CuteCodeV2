package main

import (
	"fmt"
	"test"
	"time"
)

func test1(input [10]int) (result int) {
	result = input[0]
	input[0] = 10 // 这里修改的并不是main中的arr，而是arr的copy的副本
	return
}

func test2(input_slice []int) {
	input_slice[0] = 186 // slice为引用类型，这里修改会修改原来的数据
	return
}

func main() {
	//固定长度的数组array
	arr := [10]int{}
	arr[0] = 5
	arr[1] = 10
	fmt.Println(test1(arr))
	fmt.Println(arr)
	fmt.Println(arr[0:5])
	fmt.Printf("%T\n", arr)

	// 多维数组
	arr2 := [2][4]int{{1, 2, 3, 4}, {5, 6, 7, 8}}
	fmt.Println(arr2, arr2[1][1])
	fmt.Printf("%T\n\n", arr2)

	// slice 不定常数组
	sli := []int{0, 1, 2, 3}
	sli = append(sli, 6)
	fmt.Println(sli[0:2])
	fmt.Printf("%T\n", sli)

	test2(sli)
	fmt.Println(sli)

	test.Test()

	todayDate := time.Now()

	weekday := int64(todayDate.Weekday())
	fmt.Printf("weekday :%+v\n", weekday)

	ts := todayDate.Unix()
	fmt.Printf("ts : %+v\n", ts)

	// INT((((ups.expose_t - 1578240000)%(7*86400))/86400 % 7) + 1) AS expose_week
	exposeWeek := ((ts-1578240000)%(7*86400))/86400%7 + 1
	fmt.Printf("exposeWeek : % +v\n", exposeWeek)
	//INT((expose_t%(86400*7))/86400) AS expose_week
	fmt.Printf("exposeWeek2 : %+v\n", ((ts % (86400 * 7)) / 86400))

	//exposeHour := parseExposeHour()
	//// INT((ups.expose_t%86400)/900) AS expose_quarter
	//exposeQuarter := ts % 86400 / 900
	//// INT((ups.expose_t%86400)/60) AS expose_minute
	//exposeMinute := ts % 86400 / 60
}
