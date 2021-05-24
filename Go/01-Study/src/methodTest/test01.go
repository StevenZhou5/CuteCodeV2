package methodtest

import (
	"fmt"
	"math"
)

// 长方形结构体
type Rectangle struct {
	width, height float64
}

// 为长方形结构体增加面积方法
func (r Rectangle) area() (res float64) {
	res = r.width * r.height
	return
}

// 圆形结构体
type Circle struct {
	radius float64
}

// 为圆形结构体增加面积方法，虽然area这个名字相同，但是他们是不同结构体中的方法
func (r Circle) area() (res float64) {
	res = r.radius * r.radius * math.Pi
	return
}

func Test01() {
	fmt.Println("methodtest Test01")

	r1 := Rectangle{3, 5}
	fmt.Println("当前r1长方形的面积为：", r1.area())

	c1 := Circle{radius: 5}
	fmt.Println("当前c1圆形的面积为：", c1.area())
}
