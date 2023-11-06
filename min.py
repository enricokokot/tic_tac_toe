import functools

nums = [1,2,3,4]

result = list(map(
            lambda x: functools.reduce(
                lambda a, b: a*b, list(filter(
                    lambda j: j != x, nums))), nums))

# prefix = [1] * len(nums)
# for idx, num in enumerate(nums):
#     if idx == 0:
#         prefix[idx] = nums[idx]
#     else:
#         prefix[idx] = prefix[idx - 1] * nums[idx]

# postfix = [1] * len(nums)
# reversed_nums = list(reversed(nums))
# for idx, num in enumerate(reversed_nums):
#     if idx == 0:
#         postfix[idx] = reversed_nums[idx]
#     else:
#         postfix[idx] = postfix[idx - 1] * reversed_nums[idx]
# postfix = list(reversed(postfix))

# result = [1] * len(nums)
# for idx, num in enumerate(nums):
#     if idx == 0:
#         result[idx] = postfix[idx + 1]
#     elif idx == len(nums) - 1:
#         result[idx] = prefix[idx - 1]
#     else:
#         result[idx] = prefix[idx - 1] * postfix[idx + 1]

print(result)