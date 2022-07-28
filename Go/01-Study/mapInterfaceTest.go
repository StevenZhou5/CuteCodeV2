package main

import (
	"fmt"
	"reflect"
)

type MapTestSt map[string]interface{}

func (m *MapTestSt) GetFloat(key string) float64 {
	(*m)["35"] = float64(0.5)
	return float64(0.5)
}
func main() {

	mapInterface := make(map[interface{}]interface{})
	mapString := make(map[string]string)

	mapInterface["k1"] = 1
	mapInterface[3] = "hello"
	mapInterface["world"] = 1.05
	mapInterface["rt"] = true
	mapInterface["innerMap"] = make(map[interface{}]interface{})
	mapInnerInterface := mapInterface["innerMap"].(map[interface{}]interface{})
	mapInnerInterface["innter_key"] = "innter_val"

	for key, value := range mapInterface {
		strKey := fmt.Sprintf("%v", key)
		strValue := fmt.Sprintf("%v", value)

		mapString[strKey] = strValue
	}

	fmt.Printf("%#v\n", mapString)
	fmt.Printf("%v", mapInnerInterface["innter_key"])
	var bol []int
	bol = nil
	if bol != nil {
		fmt.Println("ssss")
	}

	m := MapTestSt{}
	//orival, ori_ok := m["35"]
	fmt.Println("m:%v ", m["35"])
	fmt.Println("%v", m.GetFloat(""))
	fmt.Println("%v", m)

	m["11"] = float64(22)
	fmt.Println("xxx:%v", m)
	for key, _ := range m {
		m[key] = float64(1)
	}

	fmt.Println("---:%v", m)
	m["feas"] = []string{"a", "b", "c"}
	//m["feas"] = "a b c"
	fmt.Println("map:%v", m)
	fmt.Println(reflect.TypeOf(m["feas"]))
	fmt.Println("feas:%v", m.GetValueStringSlice("feas", nil))
}

func (m *MapTestSt) GetValueStringSlice(key string, v []string) []string {
	if value, ok := (*m)[key]; ok {
		if op, ok := value.([]string); ok {
			return op
		}
	}
	return v
}
