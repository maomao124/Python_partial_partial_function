"""
 * Project name(项目名称)：Python_partial偏函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 21:02
 * Version(版本): 1.0
 * Description(描述)： 简单的理解偏函数，它是对原始函数的二次封装，是将现有函数的部分参数预先绑定为指定值，
 从而得到一个新的函数，该函数就称为偏函数。相比原函数，偏函数具有较少的可变参数，从而降低了函数调用的难度。
 定义偏函数，需使用 partial 关键字（位于 functools 模块中）
偏函数名 = partial(func, *args, **kwargs)
其中，func 指的是要封装的原函数，*args 和 **kwargs 分别用于接收无关键字实参和关键字实参。
 """

# 定义个原函数
from functools import partial


def display(name, age):
    print("name:", name, "age:", age)


def f3(a, b):
    """
    相乘
    :param a:
    :param b:
    :return:
    """
    return a * b


if __name__ == '__main__':
    # 定义偏函数，其封装了 display() 函数，并为 name 参数设置了默认参数
    f2 = partial(display, name='张三')
    # 由于 name 参数已经有默认值，因此调用偏函数时，可以不指定
    f2(age=18)

    f4 = partial(f3, 20)
    print(f3(20, 4))
    print(f4(4))
