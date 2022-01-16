# -*- coding:utf-8 -*-
# @Time    : 2022/1/16 16:25
# Author   : wills
# @Software: PyCharm



# 公式运算服务
class FormulaOperations(object):
    def __init__(self):
        self.uni_operators = ['+', '-', '*', '/', '^', '(', ')']
        self.operator_levels = {'+':1, '-':1, '*': 2, '/': 2, '^': 3}
        self.operands = []
        self.operators = []
        self.brack_levels = {}
        self.level = 0
        self.right_level = 0

    # 去除多余的括弧
    def del_extra_bracks(self, mid_brack_cont):

        for ct in mid_brack_cont:
            if ct in ['(']:
                self.level += 1
            elif ct in ')':
                if not self.right_level:
                    self.level += 1
                    self.right_level += 1
                self.level -= 1
            if self.level not in self.brack_levels:
                self.brack_levels[self.level] = []

            if ct not in self.brack_levels[self.level]:
                self.brack_levels[self.level].append(ct)

        print('---------------------------------------------')
        print(self.brack_levels)




    # 识别公式中的操作数和运算符
    def get_formula_operands_and_operators(self, formula_cont):
        formula_cont = formula_cont.replace(' ', '')

        #
        cur = ''
        bef = ''
        for word in formula_cont:
            if word in self.uni_operators:
                pass

            if bef not in self.uni_operators:
                cur = bef + cur

            if word in self.uni_operators:
                if bef:
                    self.operands.append(bef)
                cur = word
                self.operators.append(cur)
                bef = ''
            else:
                bef += word


        print(self.operators)
        print(self.operands)


if __name__ == '__main__':
    from formula_oper_process.mid_post_expressions import MidToPostExpression, PostToMidExpression
    mid2post_model = MidToPostExpression()
    post2mid_model = PostToMidExpression()

    model = FormulaOperations()
    cont = 'a+b*(c-d)+(c-a)*c'

    post_cont = mid2post_model(cont)
    print('+++++++++++++++++++++++++++++++++++++++++++++++')
    print(post_cont)
    mid_cont = post2mid_model.tran_post_to_mid(post_cont)
    model.del_extra_bracks(mid_cont)

    print('+++++++++++++++++++++++++++++++++++++++++++++++')
    # print(post_cont)
    print(mid_cont)

    model.get_formula_operands_and_operators(cont)