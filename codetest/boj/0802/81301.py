dic = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
def solution(s):
    res = ''
    ch = ''
    for i in s:
        if i.isalpha():
            ch += i
        else:
            res += i
        
        for key, val in dic.items():
            if val == ch:
                res += str(key)
                ch = ''
            
    return int(res)