# -*- coding:utf-8 -*-
# @Time    : 2022/1/16 14:49
# Author   : wills
# @Software: PyCharm

import sympy as sym

# 交换律
def commutative_law(pre, post, oper_sym: str):
    result = '{} {} {} = {} {} {}'.format(pre, oper_sym, post, post, oper_sym, pre)
    return result

# 结合律
def associative_law(pre, mid, post, oper_sym: str):
    result = '({} {} {}) {} {} = {} {} ({} {} {})'.format(pre, oper_sym, mid, oper_sym, post, pre, oper_sym, mid,
                                                          oper_sym, post)
    return result


def distributive_law(pre, mid, post, out_oper_sym:str, in_oper_sym:str):
    result = '{} {} ({} {} {}) = {} {} {} {} {} {} {}'.format(pre, out_oper_sym, mid, in_oper_sym, post, pre,
                                                              out_oper_sym, mid, in_oper_sym,
                                                              pre, out_oper_sym, post)
    return result


# 将减号转为加号
def tran_minus_to_add(pre, post, oper_sym:str):
    if oper_sym in ['-']:
        post = '({}{})'.format(oper_sym, post)
        oper_sym = '+'
    return pre, post, oper_sym


from math_formulas.addition_operation import AdditionOperations
add_model = AdditionOperations()

a = 'a'
b = 'b'
c = 'c'
oper1 = '+'
oper2 = '*'
com_res = commutative_law(a, b, '*')
ass_res = associative_law(a, b, c, '*')
dis_res = distributive_law(a, b, c, oper2, oper1)
print(com_res)
print(ass_res)
print(dis_res)

oper3 = '-'
pre, post, oper_sym = tran_minus_to_add(a, b, oper3)
res = '{} {} {}'.format(pre, oper_sym,post)
print(res)

res1 = add_model.commutative_law(a,b,oper3)
print(res1)

# res2 = add_model.associative_law(a,b,c,oper3)
# print(res2)