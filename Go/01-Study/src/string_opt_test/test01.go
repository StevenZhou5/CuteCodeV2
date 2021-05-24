package string_opt_test

import (
	"fmt"
	"strings"
)

func Test01() {
	contains := func(str, substr string) {
		fmt.Printf("%s 中是否包含 %s:%+v\n", str, substr, strings.Contains(str, substr))
	}
	contains("asdfs", "df")
	contains("sddfs", "sdef")

	join := func(str_list []string, sep string) {
		fmt.Printf("%+v join后的值为 %s\n", str_list, strings.Join(str_list, sep))
	}
	join([]string{"a", "b", "c"}, ",")
}
