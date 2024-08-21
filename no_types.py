from typing import Sequence

def average(a: float, b: float) -> float:
    return (a + b) / 2

avg = average(12, 5)
print(avg + 2)



def list_average(nums: Sequence[float]):
    return sum(nums) / len(nums)

in_nums = [2, 3, 5, 20]
avg = list_average(in_nums)
print(avg + 2)

