# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: stack.py
# @Desp: 
# @software: vscode
# @author: xuchang0514@sina.com
'''
class Stack:
    '''用顺序表实现栈'''
    def __init__(self):
        self.__list = []  # 用来存放元素的容器，这里使用列表（顺序表）

    def is_empty(self):
        '''判断栈是否为空'''
        return self.__list == []

    def size(self):
        '''返回栈的元素个数'''
        return len(self.__list)

    def push(self, value):
        ''' 将数据元素压入栈的顶端
        这里假设列表的尾部是栈顶，列表的头部是栈底，因为顺序表的尾部插入时间复杂度是O(1)'''
        self.__list.append(value)

    def pop(self):
        '''将栈的顶端数据元素弹出，这里假设列表的尾部是栈顶'''
        return self.__list.pop()

    def peek(self):
        '''仅返回栈顶元素的值，但不弹出它'''
        if self.__list:  # 栈不为空时
            return self.__list[-1]
        else:
            return None


if __name__ == '__main__':
    # 创建空栈
    s = Stack()
    print('*' * 20 + ' 空栈时: ' + '*' * 20)
    print('是否为空栈: ', s.is_empty())
    print('栈的元素个数: ', s.size())

    # 压入一些元素
    s.push(10)
    s.push('Python')
    s.push(23.50)
    s.push('Hello')
    s.push(100)
    print('*' * 20 + ' 压入一些元素后: ' + '*' * 20)
    print('是否为空栈: ', s.is_empty())
    print('栈的元素个数: ', s.size())

    # 弹出栈顶元素
    print('*' * 20 + ' 弹出栈顶元素: ' + '*' * 20)
    print(s.pop())

    # 再次弹出栈顶元素
    print('*' * 20 + ' 再次弹出栈顶元素: ' + '*' * 20)
    print(s.pop())

    # 仅返回栈顶元素的值，但不弹出
    print('*' * 20 + ' 仅返回栈顶元素的值，但不弹出: ' + '*' * 20)
    print(s.peek())

    # 再次弹出栈顶元素
    print('*' * 20 + ' 再次弹出栈顶元素: ' + '*' * 20)
    print(s.pop())
