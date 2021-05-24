package main

import (
	"fmt"
	tf "github.com/tensorflow/tensorflow/tensorflow/go"
	"github.com/tensorflow/tensorflow/tensorflow/go/op"
)

func main() {
	for _, str := range []string{"serving", "serving2"} {
		fmt.Println(str)
	}
	//tf.LoadSavedModel("", []string{"serving"}, nil)
	s := op.NewScope()
	c := op.Const(s, "Hello from TensorFlow version"+tf.Version())
	graph, err := s.Finalize()
	if err != nil {
		panic(err)
	}

	sess, err := tf.NewSession(graph, nil)
	if err != nil {
		panic(err)
	}

	output, err := sess.Run(nil, []tf.Output{c}, nil)
	if err != nil {
		panic(err)
	}

	fmt.Println(output[0].Value())
}
