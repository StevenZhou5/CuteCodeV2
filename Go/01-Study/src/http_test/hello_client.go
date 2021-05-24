package http_test

import (
	"fmt"
	"net/http"
)

func InitHttpClient(url string) {

	resp, err := http.Get(url)
	if err != nil {
		fmt.Printf("Error: %+v\n", err)
		return
	}
	defer resp.Body.Close()

	fmt.Printf("resp: %+v\n", resp)
	fmt.Printf("resp.Body: %+v\n", resp.Body)

	// body 是byte类型数据
	buff := make([]byte, 4*1024)
	var temp string
	for {
		n, err := resp.Body.Read(buff)
		if err != nil {
			fmt.Printf("resp.Body.Read ERROR : %+v\n", err)
			if err.Error() == "EOF" {
				temp += string(buff[:n])
			}
			break
		}
		temp += string(buff[:n])
	}
	fmt.Printf("string Body : %+v\n", temp)

}
