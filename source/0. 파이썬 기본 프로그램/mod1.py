def sum(a, b):
    return a + b


def safe_sum(a,b):
    if type(a) != type(b):
        print('자료형이 다르므로 계산할 수 없습니다.')
        return
    else:
        return sum(a, b)