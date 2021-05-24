package methodtest

import "fmt"

type Person struct {
	age  int
	name string
}

type Student struct {
	Person // 通过匿名来实现继承
	school string
}

// 子类没有SayHi时调用父类的SayHi
func (p *Person) SayHi() {
	fmt.Printf("来自父类的SayHi:%+v,%+v\n", p.name, p.age)
}

// 子类有SayHi时调用子类的SayHi
func (s *Student) SayHi() {
	fmt.Printf("来自子类的SayHi：%s,%d\n", s.name, s.age)
}

func Test02() {
	s1 := Student{Person{name: "周振武", age: 28}, "电子科大"}
	s1.SayHi()
}
