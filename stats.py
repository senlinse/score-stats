"""score-stats：极简成绩统计工具。

代码刻意保持简单，用于《程序设计实践》小作业1
「基于 Git 的团队协作工作流实践」的演示仓库。
"""


def total(scores):
    """返回成绩列表的总分。"""
    return sum(scores)


def average(scores):
    """返回成绩列表的平均分。"""
    return total(scores) / len(scores)


def highest(scores):
    """返回成绩列表中的最高分。"""
    return max(scores)


def pass_rate(scores, line=60):
    """返回及格率，单位为百分比。"""
    passed = [s for s in scores if s > line]
    return len(passed) / len(scores) * 100


if __name__ == "__main__":
    sample = [85, 92, 78, 60, 95]
    print("成绩：", sample)
    print("总分：", total(sample))
    print("平均分：", round(average(sample), 2))
    print("最高分：", highest(sample))
