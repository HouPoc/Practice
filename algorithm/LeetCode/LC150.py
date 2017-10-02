class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {
            '+': lambda x: lambda y: int(float(x) + float(y)),
            '-': lambda x: lambda y: int(float(x) - float(y)),
            '*': lambda x: lambda y: int(float(x) * float(y)),
            '/': lambda x: lambda y: int(float(x) / float(y))
        }
        stack_n = []
        stack_o = []
        for element in tokens:

            if element in ["+", "-", "*", "/"]:
                stack_o.insert(0, element)
            else:
                stack_n.insert(0, element)

        for operator in stack_o:
            operand_2 = stack_n.pop(0)
            operand_1 = stack_n.pop(0)
            print(operand_1, operand_2)
            result = ops[operator](operand_1)(operand_2)
            print(result)
            stack_n.insert(0, str(int(result)))

        return int(stack_n.pop())

if __name__ == "__main__":
    y = ["-78", "2222", "/"]
    x = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
    a = Solution()
    a.evalRPN(x)
