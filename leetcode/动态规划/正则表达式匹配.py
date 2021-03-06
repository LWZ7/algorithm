'''
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""
            #p为空的时候，判断s是否为空，s为空返回True，s不为空返回False
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == ".")
            #如果s的长度为1，p[0]==s[0]或者p[0]=="." , 返回True
        if p[1] != "*":
            if s == "":
                return False
                #如果p[1]!="*",且s是空字符串，返回False
            return (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:] , p[1:])
        
        while s and (s[0] == p[0] or p[0] == "."):
            #到了while循环，说明p[1]为*，所以递归调用匹配s和p[2](*之后的匹配规则)
            #用于跳出函数，当s循环到和*不匹配的时候，则开始去匹配p[2:]之后的规则
            if self.isMatch(s , p[2:]):
                return True
            #当匹配字符串和匹配规则*都能匹配的时候，去掉第一个字符成为新的匹配字符串，
            s = s[1:]
        #假如第一个字符串和匹配规则不匹配，则去判断之后的是否匹配
        return self.isMatch(s , p[2:])
