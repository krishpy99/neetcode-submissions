class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '[' or i == '{' or i == '(':
                st.append(i)
            else:
                f = 0
                if i == ']' and (len(st) > 0 and st[-1] == '['):
                    f = 1
                    st.pop()
                if i == ')' and (len(st) > 0 and st[-1] == '('):
                    f = 1
                    st.pop()
                if i == '}' and (len(st) > 0 and st[-1] == '{'):
                    f = 1
                    st.pop()
                if f != 1:
                    st.append(i)
        if len(st) > 0:
            return False
        return True