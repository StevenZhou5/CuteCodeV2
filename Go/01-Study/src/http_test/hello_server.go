package http_test

import (
	"fmt"
	"net/http"
)

func InitHttpServerClient() {
	// 注册处理函数，用户连接，自动调用指定的处理函数
	http.HandleFunc("/hello", HelloServer)

	// 绑定监听的端口
	http.ListenAndServe(":8000", nil)
}

func HelloServer(writer http.ResponseWriter, request *http.Request) {
	// writer: 给客户端回复数据
	// request: 读取客户端发送的数据

	writer.Write([]byte("hello go")) // 给客户端回复数据

	fmt.Printf("Methon: %+v\n", request.Method)
	fmt.Printf("URL: %+v\n", request.URL)
	fmt.Printf("Herader: %+v\n", request.Header)
	fmt.Printf("Body: %+v\n", request.Body)

}
