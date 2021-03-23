def odd_nums(n):
    for x in range(1, n + 1, 2):
        yield print(x)
    # nums = (x for x in range(1, n + 1, 2))
    # for i in nums:
    #     yield print(i)


odd_to_15 = odd_nums(15)
while True:
    next(odd_to_15)
