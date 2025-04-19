def min_opened_links(n, orders):
    orders.sort()
    
    extra_links = 0 
    opened_links = 0 
    
    while orders:
        if extra_links >= orders[0]:
            extra_links -= orders[0]
            orders.pop(0)
        elif len(orders) >= 2:
            opened_links += 1
            extra_links += 1
            orders.pop() 
        else:
            opened_links += 1
            orders.pop()
    
    return opened_links

def main():
    n = int(input().strip())
    orders = list(map(int, input().strip().split()))
    
    result = min_opened_links(n, orders)
    print(result)

main()