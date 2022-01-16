# -*- coding:utf-8 -*-
# @Time    : 2022/1/16 17:00
# Author   : wills
# @Software: PyCharm


import logging
import functools

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Node():
    def __init__(self, data=None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    def __str__(self):
        return 'Node:<data: %s><quote: %s>' % (self._data, self._next)


def change_length(control):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kw):
            result = func(self, *args, **kw)
            if control == 'add':
                self._length += 1
            elif control == 'reduce':
                self._length -= 1
            else:
                raise ValueError('The %s is wrong' % control)
            return result

        return wrapper

    return decorator


class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __bool__(self):
        return bool(self._length)

    def __str__(self):
        linkedlist = self._data2list()
        return 'linkedlist: %s' % str(linkedlist)  # 将str的打印方式委托给了list的__str__

    def __contains__(self, value):
        linkedlist = self._data2list()
        return value in linkedlist

    @property
    def head(self):
        return self._head

    def generate_node(self):
        node = self._head
        while node != None:
            yield node
            node = node.next

    def _data2list(self):
        return [x.data for x in self.generate_node() if x != None]

    @change_length('add')
    def add_tail(self, value):
        node = Node(value)
        if self._length == 0:
            self._head = node
            self._tail = self._head
            return None
        self._tail.next = node
        self._tail = node

    @change_length('add')
    def add(self, value):
        logger.debug('the <%s> has put in the stack' % value)
        node = Node(value)
        node.next = self._head
        self._head = node

    @change_length('reduce')
    def pop(self, remain=0):
        if self._length > remain:
            data = self._head.data
            self._head = self._head.next
            logger.debug('the <%s> has move out from the stack' % data)
            return data
        else:
            print('the linkedlist is empty')

    @change_length('reduce')
    def deleted(self, value):
        assert self.__contains__(value) == True, 'there is no value %s' % value
        if value == self._head.data:
            self._head = self._head.next
        else:
            nodes = list(self.generate_node())  # list代码清晰，但是空间会占用大些
            for index in range(self._length):
                cur_node = nodes[index]
                if cur_node.data == value:
                    pre_node = nodes[index - 1]
                    if index == self._length - 1:
                        next_node = None
                    else:
                        next_node = nodes[index + 1]
                    pre_node.next = next_node
                    logger.info('the data: %s has been deleted, and the pre node is %s' %
                                (cur_node.data, pre_node.data))

    @change_length('reduce')
    def superdele(self, node):
        assert node.next != None, 'must not be the tail'
        node.data = node.next.data
        node.next = node.next.next

# 后缀表达式
class MidToPostExpression():
    def __init__(self):
        self._operators = LinkedList()
        self._operators.add('#')
        self._commas = {'#': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 10, ')': 10}
        self._special_commas = ['(', ')']
        self._result = []
        self._remain = 1

    def __call__(self, expression):
        expression = expression.replace(' ', '')
        commas_keys = self._commas.keys()
        for i in expression:
            if i in commas_keys:
                # 处理遇到右括号的情况，把堆栈中的左括号以上都拿出来
                if i == self._special_commas[1]:
                    self._output(lambda x: x.data != self._special_commas[0])
                    self._operators.pop(remain=self._remain)
                # 对运算符进行入栈
                elif self._commas[i] > self._commas[self._operators.head.data]:
                    self._operators.add(i)
                    if i == self._special_commas[0]:
                        self._commas[i] = 0
                # 对运算符进行出栈
                else:
                    self._output(lambda x: self._commas[i] < self._commas[x.data])
                    self._operators.add(i)
            else:
                self._result.append(i)
                logger.debug('the result is: %s' % str(self._result))

        # 对剩余的运算符进行出栈
        self._output(lambda _: len(self._operators) != self._remain)
        result = ''.join(self._result)

        return result

    def _output(self, func):
        generate_node = self._operators.generate_node()
        for node in generate_node:
            if func(node):
                self._result.append(self._operators.pop(remain=self._remain))
                logger.debug('the result is: %s' % str(self._result))
            else:
                return None


# 后缀表达式转为中缀表达式
class PostToMidExpression(object):
    def __init__(self):
        self.uni_operaters = '+-*/^'
        self.oper_rp_syms = {'/':'1/', '-':'-'}
        self.rp_opers = {'-':'+', '/':'*'}
        self.operand_vals = {}
        self.operand_ids = []
        self.operators = []

    def tran_post_to_mid(self, expression):
        i = 0
        for ex in expression:
            if ex not in self.uni_operaters:
                val = ex
            else:
                print('-------------->>>', ex, self.operand_ids, self.operand_vals)
                oper_sym = ex
                post_id = self.operand_ids.pop()
                pre_id = self.operand_ids.pop()
                pre = self.operand_vals[pre_id]
                post = self.operand_vals[post_id]

                if oper_sym in self.rp_opers:
                    rp_sym = self.oper_rp_syms[oper_sym]
                    post = '({}{})'.format(rp_sym, post)
                    oper_sym = self.rp_opers[oper_sym]
                val = '({}{}{})'.format(pre, oper_sym, post)
            self.operand_ids.append(i)
            self.operand_vals[i] = val
            i += 1

        print(self.operand_ids)
        result = ''
        if self.operand_ids:
            result = self.operand_vals[self.operand_ids[0]]

        return result




