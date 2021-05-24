package main

import (
	"fmt"
	"interfacetest"
	"methodtest"
	"string_opt_test"
)

func main() {
	fmt.Printf("hello")

	// 方法操作测试
	methodtest.Test01()
	methodtest.Test02()

	// 结构操作测试
	interfacetest.Test01()
	interfacetest.Test02()
	interfacetest.Test03()

	// 字符串操作测试
	string_opt_test.Test01()

	// Json
	//json_opt_test.Test01()
	//json_opt_test.Test02()
	//json_opt_test.Test03()

	fmt.Sprintf("%[3]*.[2]*[1]f", 12.0, 2, 6)

	// map的引用类型
	map_test1 := make(map[int]*TestSt)
	a := &TestSt{"张三", 18}
	map_test1[1] = a
	a.Age = 20
	fmt.Println(map_test1[1])
}

type TestSt struct {
	Name string
	Age  int
}
