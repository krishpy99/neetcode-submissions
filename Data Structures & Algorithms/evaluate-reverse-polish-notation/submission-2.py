import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            #print(st)
            if i not in ['+', '-', '*', '/']:
                #print(i,'-add')
                st.append(int(i))
            else:
                #print(i,'-pop')
                a = st[-1]
                st.pop()
                b = st[-1]
                st.pop()
                if i == '+':
                    st.append(a + b)
                elif i == '-':
                    st.append(b - a)
                elif i == '*':
                    st.append(a * b)
                else:
                    st.append(math.trunc(b / a))
        return st[-1]
                