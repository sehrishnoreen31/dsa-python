def max_pair_product(num_list):
    l = len(num_list)
    max_prod = 0
    for i in range(0, l):
        for j in range(i + 1, l):
            max_prod = max(max_prod, num_list[i] * num_list[j])
    return max_prod

# user input
num_list = list(map(int, input().split()))
print(max_pair_product(num_list))