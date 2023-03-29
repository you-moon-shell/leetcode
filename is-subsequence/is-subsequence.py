class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t): return False
        if len(s)==0: return True
        s_pos,t_pos=0,0
        while len(s)>s_pos and len(t)>t_pos:
            if s[s_pos]==t[t_pos]:
                s_pos+=1
            t_pos+=1
        return len(s)==s_pos
