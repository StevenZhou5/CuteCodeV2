package main

import "http_test"

func main() {
	//http_test.InitHttpServerClient()
	//url := "http://www.baidu.com"
	url := "http://127.0.0.1:8000/hello"
	http_test.InitHttpClient(url)
}
