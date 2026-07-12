class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        # "{": "}"
        for i in s:
            st.append(i)
            
            if len(st) > 1 and st[-2] + st[-1] in ["[]", "()", "{}"]: 
                st.pop()
                st.pop()
        
        if not st:
            return True
        
        return False
        