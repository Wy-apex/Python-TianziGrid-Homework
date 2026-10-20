
# Python程序练习题5.1：字符田字格绘制

# 定义田字格绘制函数，width表示小格子的宽度
def draw_grid(width):

    # 检查宽度是否为正整数
    if type(width) != int or width <= 0:
        print("错误：田字格宽度必须是正整数！")
        return

    # 设置田字格为4行4列
    size = 4

    # 生成横线，例如：+----+----+----+----+
    horizontal = ("+" + "-" * width) * size + "+"

    # 生成竖线，例如：|    |    |    |    |
    vertical = ("|" + " " * width) * size + "|"

    # 循环绘制4行格子
    for i in range(size):

        # 每行格子上方的横线
        print(horizontal)

        # 每个格子的高度与宽度相同
        for j in range(width):
            print(vertical)

    # 绘制最后一条横线
    print(horizontal)


# 主程序
if __name__ == "__main__":

    # 让用户输入田字格宽度
    try:
        width = int(input("请输入田字格宽度："))
        draw_grid(width)

    except ValueError:
        print("错误：请输入一个整数！")
