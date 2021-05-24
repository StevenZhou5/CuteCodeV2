package interfacetest

import (
	"errors"
	"fmt"
)

type Animal interface {
	Run()
}

type Men interface {
	Animal // 接口的继承也是通过匿名函数
	SayHi()
	Sing(song string)
}

type Person struct {
	name string
	age  byte
}

type Student struct {
	Person
}

func (s Student) Run() {
	fmt.Printf(" %s Running\n", s.name)
}

func (s Student) SayHi() {
	fmt.Printf("Hello I'm %s\n", s.name)
}
func (s Student) Sing(sang string) {
	fmt.Printf("%s 不会唱 %s\n", s.name, sang)
}

type Singer struct {
	Person
}

func (s Singer) Run() {
	fmt.Printf("%s Running\n", s.name)
}

func (s Singer) SayHi() {
	fmt.Printf("Hello I'm %s\n", s.name)
}

func (s Singer) Sing(song string) {
	fmt.Printf("%s sing %s\n", s.name, song)
}

func sing(m Men) {
	m.Run()
	m.SayHi()
	m.Sing("你好世界")
}

func Test01() {
	stu := Student{Person{name: "周振武"}}

	sing(stu)

	sin := Singer{Person{name: "周杰伦"}}
	sing(sin)
}

func Test02() {
	// 空接口可以保存任意类型的值
	var v1 interface{} = 1
	fmt.Printf("v1 = %+v\n", v1)

	v1 = "str"
	fmt.Printf("v1 = %+v\n", v1)
}

func errorTest(a, b int) (res int, err error) {
	if b == 0 {
		err = errors.New("分母不能为零")
	} else {
		res = a / b
	}
	return
}
func Test03() {
	res1, err1 := errorTest(5, 2)
	fmt.Printf("res1:%+v; err1:%+v\n", res1, err1)

	res2, err2 := errorTest(5, 0)
	fmt.Printf("res2:%+v;err2:%+v\n", res2, err2)
}
