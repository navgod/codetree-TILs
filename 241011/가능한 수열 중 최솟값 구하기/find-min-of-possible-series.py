n = int(input())

selected_nums = []
tof= False
def select(idx):
    global tof
    if tof:
        return
    if idx == n:
        tof = True
        print(''.join(selected_nums))
        return
    ## 4545 4
    for i in range(4,7):
        if len(selected_nums)>=1 and selected_nums[-1] == str(i):
            continue
        else:
            if len(selected_nums) <2:
                if len(selected_nums)==1 and selected_nums[-1] == str(i):
                    continue
                else:
                    selected_nums.append(str(i))
                    select(idx+1)
                    selected_nums.pop()
            else:
                k = len(selected_nums)//2
                is_pass = True
                for j in range(k+1):
                    if ''.join(selected_nums[-1-j:-2-2*j:-1][::-1]) == ''.join(selected_nums[-1:-1-j:-1][::-1]) +str(i):
                        is_pass = False
                        break
                if is_pass:
                    selected_nums.append(str(i))
                    select(idx+1)
                    selected_nums.pop()
select(0)