def most_common(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    # 找出最多次數的數字
    return max(counts, key=counts.get)

print(most_common([1, 2, 2, 3, 4, 4, 4, 5]))