package main

import (
	"encoding/json"
	"fmt"
	"strconv"
)

func main() {
	jsonstr := `{"device_type:0":[0.15924401537616384,0.6960141529502973,0.04294168658187679,0.252801900185213,0.012835568485928511,0.0958821012233532],"gender:1":[0.15521099703583488,0.5234561133560659,0.07419168812238756,0.2251221036688592,-0.011762136228550026,0.11835730600658938],"nt:0":[-0.08890100562135281,0.22480229653147918,-0.15772393512620797,-0.11232052338751329,0.11893588826360987,0.05208063537559671],"ptype:0":[0.09322232513925272,0.426515512197668,0.03081120498669824,0.1890217746202535,-0.16307688347909924,0.08215674364249462],"ptype:1":[0.29008104544133756,0.5876497292300379,0.1207292599632989,0.045267840022913425,0.17568508814078937,0.18378260209627778],"weight_bias":[0.24300362950793353,0.6902553991496964,0.14547294469053304,-0.061761709431365684,0.08727698322452436,0.41649400185985386]}`
	jsonMap := make(map[string][]float64)
	err := json.Unmarshal([]byte(jsonstr), &jsonMap)
	if err != nil {
		fmt.Println("解析错误：%+V", err)
		return
	}
	fmt.Println("jsonMap['device_type:0']:%+v", jsonMap["device_type:0"])
	fmt.Println("解析成功，最终解析完的map:%+V", jsonMap)

	testMap := make(map[string]map[int64]int64)
	key := "s"
	subKey := int64(5)
	testMap[key] = make(map[int64]int64)
	testMap[key][subKey] = 5
	if value, ok := testMap[key]; !ok {
		fmt.Println("key不存在：%v", testMap)
	} else {
		fmt.Println("key存在的 testMap[%v] = %v", key, value)
	}
	fmt.Println("final testMap:", testMap[key])

	a := 5
	fmt.Println(int64(float64(a) * 0.8))
	//string转成int：
	//int, err := strconv.Atoi(string)
	//string转成int64：
	//int64, err := strconv.ParseInt(string, 10, 64)
	//int转成string：
	//string := strconv.Itoa(int)
	//int64转成string：
	//string := strconv.FormatInt(int64,10)
	fmt.Println(strconv.Itoa(888))                 // 默认转换成十进制
	fmt.Println(strconv.FormatInt(int64(100), 2))  // 转换成二进制的字符串
	fmt.Println(strconv.FormatInt(int64(100), 10)) // 转换成十进制的字符串

	testVal, ok := testMap[key][6]
	if ok {
		fmt.Println("testVal:", testVal)
	} else {
		fmt.Println("key 不存在")
	}
	var x float64 = 12.6
	var y int = int(x * 1.1)
	fmt.Println(y)
}
