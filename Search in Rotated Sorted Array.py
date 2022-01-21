class Solution:
    def search(self, nums: list[int], target: int) -> int:
        print(self.find_pivot_point(nums))


    def find_pivot_point(self, nums: list[int]) -> int:
        length = len(nums)

        first = length // 2
        half = length

        while nums[first] < nums[first + 1]:
            half //= 2
            print("First ", first)
            if nums[first] > nums[0]:
                next_first = first + half // 2
                if next_first + 1 < length:
                    first = next_first
                else:
                    break
            else:

                first = half // 2

        return first + 1


solution = Solution()
result = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
result = solution.search([4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 1, 2], 0)

# print(result)
