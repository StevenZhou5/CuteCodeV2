package test

import (
	"errors"
	"fmt"
)

func Test() {
	a := 5
	fmt.Println("Value is: %d", a)

	s := "hello" // 字符串默认是不可按位置改变的
	s = s + "c"
	fmt.Println(s)

	c := []byte(s)
	c[0] = 'c'
	fmt.Println(c)

	s2 := string(c)
	fmt.Println(s2)

	// 字符串可以切片,但是不能像python一样用负数
	fmt.Println(s2[0:])
	fmt.Println(s2[0:1])

	// 字符串可以相加
	fmt.Println(s2[0:1] + s2[len(s2)-1:])

	// Printf 可以用%xxx的占位符输出
	fmt.Printf("%s 的类型为: %t\n", s2, s2) // Printf才可以用%s来做占位

	// ``可以实现多行字符串的输出
	m := `hello
			word`
	fmt.Println(m)

	m2 := "hello \n word" // 也可以用转义字符换行
	fmt.Println(m2)

	// error类型，用于抛出错误
	err := errors.New("发生错误")
	if err != nil {
		fmt.Println(err)
	}

	// 分组初始化
	const (
		c1 = 100
		c2 = 2.0
		c3 = "c3"
	)
	fmt.Println(c1, c2, c3)

	var (
		v1 = 100 // var 分组初始化不能 :=
		v2 = 2.0
		v3 = "v3"
	)
	v1 = 1
	fmt.Println(v1, v2, v3)

	// iota
	const (
		iota1               = iota
		iota2, iota3, iota4 = iota, iota, iota
		iota5               = iota
	)
	fmt.Println(iota1, iota2, iota3, iota4, iota5)
}
