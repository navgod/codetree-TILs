n = int(input())

MAX_NUM = 19

dp = [0 for _ in range(MAX_NUM + 1)]

def get_num_of_unique_bst(n):
    number_of_unique_bst = 0
    
    for i in range(n):
        number_of_unique_bst += dp[i] * dp[n - i - 1]
        
    return number_of_unique_bst


dp[0] = dp[1] = 1

for i in range(2, n + 1):
    dp[i] = get_num_of_unique_bst(i)
    
print(dp[n])