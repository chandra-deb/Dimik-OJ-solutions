T = int(input())
result_list = []
result = ''

for case_no in range(1, T+1):
    N = int(input())
    for i in range(1, N+1):
        if N % i == 0:
            result_list.append(str(i))
    result = ' '.join(result_list)
    print('Case', str(case_no) + ': ' + result, end='')
    result_list = []
    print()
