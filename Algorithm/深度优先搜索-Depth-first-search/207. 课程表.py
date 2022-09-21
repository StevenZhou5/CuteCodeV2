# 207. 课程表
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
# 提示：
#
# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 递归（DFS）+ Map
        # 时间复杂度：O(m + n ) ,m 是图中的节点数-即课程数，n是图的边数-即为先修课程的要求数
        # 空间复杂度：O(m + n), 题目中是以列表形式给出的先修课程关系，为了对图进行深度优先搜索，我们需要存储成邻接表的形式，空间复杂度为 O(n+m)。在深度优先搜索的过程中，我们需要最多 O(n) 的栈空间（递归）进行深度优先搜索，因此总空间复杂度为 O(n+m)。

        course_map = {}
        for course, pre in prerequisites:
            # print(course, pre)
            course_map.setdefault(course, [])
            course_map[course].append(pre)
        # print(course_map)
        learned_course = set()

        def recursion(course, next_set):
            if course in learned_course:
                return True
            if course not in course_map:  # 如果没有前置课程，可以学习
                learned_course.add(course)
                return True
            next_set.add(course)
            for pre in course_map[course]:
                if pre in learned_course:
                    continue
                if pre in next_set:  # 前继课程中有后继课程，发生冲突
                    return False
                if not recursion(pre, next_set):  # 前继课程无法学习，返回false
                    return False
            next_set.remove(course)  # 回溯
            learned_course.add(course)
            # course_map.pop(course)
            return True

        for key in course_map.keys():
            if not recursion(key, set()):
                return False
        return True
