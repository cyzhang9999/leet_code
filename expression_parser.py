#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Chunyu Zhang
@license: 
@file: expression_parser.py
@time: 18/7/12 上午10:15
"""
import sys
import tokenize
import json
from io import StringIO

class Test():

    def __init__(self):
        self.logic_opt_list = ["not","and","or","("]

    def expression_parser(self,text):
        ret = {}
        expression_tokens = self.parse_expr_tokens(text)
        print expression_tokens
        value_stack = []
        opt_stack = []
        for each_token in expression_tokens:
            print "#1",each_token
            print "#2",value_stack
            print "#3",opt_stack
            if each_token == "(":
                opt_stack.append(each_token)
            elif each_token == ")":
                opt_tmp = self.stack_pop(opt_stack)
                while opt_tmp != "(":
                    self.logic_process(opt_tmp,value_stack)
                    opt_tmp = self.stack_pop(opt_stack)
            elif each_token in self.logic_opt_list:
                opt_tmp = ""
                if len(opt_stack)>0:
                    opt_tmp = self.stack_pop(opt_stack)
                if self.cmp_logic_opt(opt_tmp,each_token):
                    self.logic_process(opt_tmp,value_stack)
                else:
                    if opt_tmp:
                        opt_stack.append(opt_tmp)
                    opt_stack.append(each_token)
            else:
                value = each_token[:each_token.find("[")]
                others = each_token[each_token.find("[")+1:each_token.find("]")]
                others_arr = others.split(",")
                key = others_arr[0]
                opt = "include"
                if len(others_arr)>1:
                    opt = others_arr[1]
                highlight = 0
                if len(others_arr)>2:
                    highlight = int(others_arr[2])
                obj_tmp = {
                    "condition":{
                        "key":key,
                        "opt":opt,
                        "value":value,
                        "highlight":highlight
                    }
                }
                value_stack.append(obj_tmp)

        for i in range(len(opt_stack)-1,-1,-1):
            opt_tmp = opt_stack[i]
            self.logic_process(opt_tmp,value_stack)
        ret = self.stack_pop(value_stack)
        return ret

    def logic_process(self,opt,value_stack):
        if opt == "not":
            v1 = self.stack_pop(value_stack)
            obj = {opt:v1}
            value_stack.append(obj)
        else:
            v1 = self.stack_pop(value_stack)
            v2 = self.stack_pop(value_stack)
            left_opt =  v2.keys()[0]
            right_opt = v1.keys()[0]
            obj = {}
            if left_opt == opt and right_opt == opt:
                obj = v2[opt].extend(v1[opt])
            else:
                obj = {opt:[v1,v2]}
            value_stack.append(obj)

    def stack_pop(self,stack):
        ret = ""
        if stack and len(stack)>0:
            ret = stack.pop()
        return ret

    def cmp_logic_opt(self,opt1,opt2):
        ret = False
        if opt1 and opt2:
            i1 = self.logic_opt_list.index(opt1)
            i2 = self.logic_opt_list.index(opt2)
            if i1 < i2:
                ret=True
        return ret

    def parse_expr_tokens(self,text):
        expression_tokens = []
        ori_tokens = tokenize.generate_tokens(StringIO(text.lower().decode("utf-8")).readline)
        tmp = ""
        in_bracket = False
        for each_token in ori_tokens:
            each_token = each_token[1]
            if each_token in ["(",")"]:
                expression_tokens.append(each_token)
                continue
            elif each_token == "[":
                #if len(tmp)>0:
                #    expression_tokens.append(tmp)
                tmp += each_token
                in_bracket = True
                continue
            elif each_token == "]":
                tmp += each_token
                expression_tokens.append(tmp)
                tmp = ""
                in_bracket = False
                continue
            elif each_token in self.logic_opt_list:
                expression_tokens.append(each_token)
            else:
                if in_bracket:
                    tmp += each_token
                else:
                    tmp += " "+each_token
        return expression_tokens

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    #trans = Translator()
    #ret = trans.pretranslate("Concomitant medications were not reported.")
    test = Test()
    ret = test.expression_parser("((gastric cancer[Title,include]) OR NOT gastric cancer[Title/Abstract] OR gastric cancer[keyword]) AND karimi[Author] ")
    print json.dumps(ret,ensure_ascii=False)