import functools

def combinationSum4(nums, target) -> int:
    # potential optimization
    # nums.sort()

    @functools.lru_cache(maxsize = None)
    def combs(remain):
        if remain == 0:
            return 1

        result = 0
        for num in nums:
            if remain - num >= 0:
                result += combs(remain - num)
            # potential optimization
            # else:
            #     break

        return result

    return combs(target)

if __name__ == '__main__':
    print(combinationSum4([1,2,3],4))