# 切题四件套：
# 1：clarification：读题、理解；询问题目细节、边界条件、可能的极端(错误)情况；
# 2：Possible Solution：所有可能的解法一一沟通；Compare Time & Space Complexity(时间复杂度和空间复杂度)；Optimal Solution（最优解）
# 3:coding：写代码；
# 4:Test cases：测试用例;

# 递归：自顶向下
def recursion(level, param1, param2, **kargs):
    # 1、 recursion terminator:递归的终止条件
    # if level > MAX_LEVEL:
    #     print(res)
    #     return

    # 2、 当前层的处理逻辑
    # data_process(level,data...)

    # 3、 drill down：调用下一层递归
    # recursion(level + 1, newp1,newp2,...)

    # 4、 如果需要的话做状态还原
    # reverse_state(level)

    return


# Dynamic Programming：自底向上
def dynamic_programming(m, n):
    # 1、状态的定义：初始状态:根据最优子结构可以减少状态的存储
    dp = [[0] * n] * m
    dp[0][0] = 0
    dp[0][1] = 1

    # 2、状态转义方程:遍历方向依赖 状态转义方程的依赖关系
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]  # 最优解


# 二分查找模板
def search(nums, target):
    # 1、初始确定左右边界
    left, right = 0, len(nums) - 1

    while left <= right:  # 2、一定是小于等于
        # 3、中间索引计算
        mid = left + (right - left >> 1)  # 整数情况下,注意位运算的优先级低，一定要用括号括起来
        # mid = left + (right - left) / 2 # 浮点数情况：比如开根号

        # 4、判断
        if nums[mid] == target:  # 4-1：找到
            return mid
        # 4-*：注意，如果存在重复元素，或者找第一个大于或者第一个小于目标值的时候，== 的判断要视情况和某一个大于/等于条件在一起
        if nums[mid] > target:  # 4-2：中间值大了，更新右边界
            right = mid - 1
        else:  # 中间值小了更新左边界
            left = mid + 1

    return -1


# 递归版的DFS
# visited = set()
def dfs_recursion(cur_node, visited):
    # 1 递归终止条件
    if not cur_node:
        return

    # 2: 数据处理
    visited.add(cur_node)
    for child_node in cur_node.childs:
        if child_node not in visited:
            # 3:drill down
            dfs_recursion(child_node, visited)
            # 4: reverse_state: 这里不需要


# 使用堆栈的深度优先
def dfs_stack(root_node):
    # 1、初始化堆栈
    stack = [root_node]
    visited = set()
    while stack:
        # 2、出栈
        cur_node = stack.pop()
        visited.add(cur_node)
        print(cur_node.val)
        # 3、儿子们入栈
        for child_node in cur_node.childs:
            if child_node not in visited:
                stack.append(child_node)


# 广度优先遍历:一个一个遍历
def bfs_single(root_node):
    # 1、初始化队列
    from collections import deque
    queue = deque()
    queue.append(root_node)

    visited = set()
    while queue:
        # 2、 一个一个出队列
        cur_node = queue.popleft()
        visited.add(cur_node)
        print(cur_node.val)

        # 3、当前一个结点的儿子们入队列
        for child_node in cur_node.childs:
            if child_node not in visited:
                queue.append(child_node)


# 广度优先遍历：一批一批遍历
def bfs_batch(root_node):
    # 1、初始化队列
    from collections import deque
    queue = deque()
    queue.append(root_node)

    visited = set()
    while queue:
        # 2、一批一批出
        for _ in range(len(queue)):  # 一次把队列中的所有元素都取出来
            cur_node = queue.popleft()
            visited.add(cur_node)
            print(cur_node.val)

            # 3、当前结点的儿子入队列
            for child_node in cur_node.childs:
                if child_node not in visited:
                    queue.append(child_node)

# 位运算:
# 1、判断奇数偶数： 奇数 if x & 1 ele 偶数
# 2、删除掉二进制为的最后一个1： x & (x-1)
# 3、只保留二进制位的最后一个1:  x & -x  ; 负数的二进制 = 正数的二进制的补码 =  正数的二进制的反码(0变1，1变0) + 1；
# a 的补码是 -a 不论a为正负都成立 (除了a为最大负数时，如果a为最大负数时a=2^(n-1) 那么 a 的补码 = a 本身)
# 4、把第k+1位变为1； a | (1<<k);  001 | (1 << 2) = 101 = 5;
# 5、把第k+1位取反(第k+1位1变0，0变1)； a ^ (1<<k); 5 = 101 ^ (1<<2) = 001 = 1; 5 = 101 ^ (1<<1) = 111 = 7;
# 6、判断第k+1为是否为1; (a >> k) & 1 == 1
# 7、取出后k为的值： a - ((a>>k) << k); 35 =0010 0011 - ((0010 0011 >> 4) << 4) = 0011 = 3; # 取出了后4位的值
