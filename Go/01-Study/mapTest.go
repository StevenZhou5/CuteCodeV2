package main

func main() {

	testMap := make(map[int64]int)
	testMap[5] = 10

	println(testMap[5], testMap[10]) // 如果k不在的话返回默认值0，并不会报错

	for key, val := range testMap {
		println(key, val)
	}

}
