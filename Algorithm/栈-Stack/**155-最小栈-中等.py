# 155. 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现 MinStack 类:
#
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
#
#
# 示例 1:
#
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
# 提示：
#
# -231 <= val <= 231 - 1
# pop、top 和 getMin 操作总是在 非空栈 上调用
# push, pop, top, and getMin最多被调用 3 * 104 次

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []  # 需要一个额外的最小栈，和原始栈大小样，里面记录的是在加入每个元素后，当前站内的最小值

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = val
        if self.stack_min and cur_min > self.stack_min[-1]:
            cur_min = self.stack_min[-1]
        self.stack_min.append(cur_min)  # 如果新来元素最小，那么加入新来元素，否则还是原来栈顶的最小值

    def pop(self) -> None:
        self.stack_min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
