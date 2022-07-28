package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func test01() {
	cnt := 0
	all_cnt := 10000
	for i := 0; i < all_cnt; i++ {
		cur_time := time.Now().UnixNano()
		fmt.Println(cur_time)
		random := rand.New(rand.NewSource(cur_time))
		r := random.NormFloat64()
		r = r * 0.3333333
		if r > 1.0 || r < -1.0 {
			cnt = cnt + 1
		}
		fmt.Println(r, cnt)
	}
}
func test02() {
	i := 5
	for i > 0 {
		fmt.Println(i)
		i -= 1
	}
}

type item struct {
	name string
	age  int64
}

func test03() {
	a := []item{{"a", 1}, {"b", 2}, {"c", 3}, {"d", 4}, {"e", 5}, {"f", 6}}
	//a = append(a[:1], a[2:]...)
	var tmp item
	tmp = a[0]
	a = a[1:]
	fmt.Println(a, tmp)
}

func test04(tmpMap map[int64]int, tmpList *[]int, tmpInt *int) {
	tmpMap[0] += 1
	tmpMap[1] += 2
	*tmpInt += 1

	*tmpList = append(*tmpList, 5)

}

func test04B() {
	tmpMap := make(map[int64]int)
	tmpList := []int{}
	tmpInt := 5
	test04(tmpMap, &tmpList, &tmpInt)
	fmt.Println(tmpMap)
	fmt.Println(tmpList)
	fmt.Println(tmpInt)
}

func test05() {
	a := []item{{"a", 1}, {"b", 2}, {"c", 3}, {"d", 4}, {"e", 5}, {"f", 6}}

	a = append(a[:6], append([]item{{"A", 10}}, a[6:]...)...)
	fmt.Println(a)
}

func test06() {
	a := map[int64]bool{
		100: true,
	}
	if a[102] {
		fmt.Println("哈哈哈")
	}
	if a[100] {
		fmt.Println("嘿嘿嘿")
	}

	f1 := float64(100-10) / 100
	f2 := float64((100 - 10) / 100)
	fmt.Println("f1:", f1, ";f2:", f2)
	ss := map[int64]float64{}
	fmt.Println("ss:", ss[102])
	fmt.Println("rand:", rand.Float64())
	fmt.Println("randInt:", rand.Intn(5)+5)
	//fmt.Println(TestCount)
	////TestCount = 5
	//fmt.Println(TestCount)
	d := math.Min(float64(1)/float64(5)/float64(0.1), 1)
	fmt.Println("a:", d)
	fmt.Println(fmt.Sprintf("%s","192.168.0.1"))
}
func TmpTest() {
	//test05()
	//fmt.Println(strings.Contains("ssdDurContinue", "dur"))
	rand.Seed(time.Now().UnixNano())
	test06()

}

func main() {
	TmpTest()
}
