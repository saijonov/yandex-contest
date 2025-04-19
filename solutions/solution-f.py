def count_good_subarrays(n, arr):
    count = 0
    diff = 0
    diff_count = {0: 1} 
    
    for i in range(n):
        if i % 2 == 0:
            diff += arr[i]
        else:
            diff -= arr[i]
            
        count += diff_count.get(diff, 0)
        diff_count[diff] = diff_count.get(diff, 0) + 1
    
    return count

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    
    result = count_good_subarrays(n, arr)
    print(result)


main()