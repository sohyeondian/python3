import random

def rsp(user, com):
    if user == com:
        return 'draw'
    if (user == 2 and com == 0):
        return 'lose'
    if (user == 0 and com == 2):
        return 'win'
    if user > com:
        return 'win'
    return 'lose'


rsp_dic = {'가위': 0, '바위': 1, '보': 2}
rev_rsp_dic = {v: k for k, v in rsp_dic.items()}

for _ in range(5):
    user = input('입력(가위/바위/보) : ')
    if user in rsp_dic.keys():
        com = random.randint(0, 2)
        result = rsp(rsp_dic[user], com)
        print('상대 -', rev_rsp_dic[com], ':', result)
    else:
        print('잘못입력하셨습니다.')