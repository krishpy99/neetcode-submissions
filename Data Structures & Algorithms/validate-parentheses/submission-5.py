class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        # "{": "}"
        for i in s:
            if i in "[({":
                st.append(i)
                continue
            
            if i == ']':
                if len(st) == 0 or st[-1] != '[':
                    return False
            if i == '}':
                if len(st) == 0 or st[-1] != '{':
                    return False
            if i == ')':
                if len(st) == 0 or st[-1] != '(':
                    return False
            
            st.pop()
        
        if st:
            return False
        
        return True