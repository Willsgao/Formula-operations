# -*- coding:utf-8 -*-
# @Time    : 2022/1/16 14:59
# Author   : wills
# @Software: PyCharm

# 加法运算
class AdditionOperations(object):
    def __init__(self):
        self.operator_levels = {'+':1, '-':1, '*':2, '/':2, '^':3, }
        self.trans_opers = {'-':'+'}

    # 交换律
    def commutative_law(self, pre, post, oper_sym:str):
        result = '{} {} {} = {} {} {}'.format(pre, oper_sym, post, post, oper_sym, pre)
        return result

    # 结合律
    def associative_law(self, pre, mid, post, oper_sym:str):
        result = '({} {} {}) {} {} = {} {} ({} {} {})'.format(pre, oper_sym, mid, oper_sym, post, pre, oper_sym, mid,
                                                              oper_sym, post)
        return result

    # 分配律
    def distributive_law(self, pre, mid, post, out_oper_sym:str, in_oper_sym:str):
        result = '{} {} ({} {} {}) = {} {} {} {} {} {} {}'.format(pre, out_oper_sym, mid, in_oper_sym, post, pre,
                                                                  out_oper_sym, mid, in_oper_sym,
                                                                  pre, out_oper_sym, post)
        return result

    # 将减号转为加号
    def tran_same_level_opers(self, pre, post, ori_oper_sym:str):
        oper_sym = ori_oper_sym
        if ori_oper_sym in self.trans_opers:
            tar_oper_sym = self.trans_opers[ori_oper_sym]
            post = '({}{})'.format(ori_oper_sym, post)
            oper_sym = tar_oper_sym
        return pre, post, oper_sym


    #











