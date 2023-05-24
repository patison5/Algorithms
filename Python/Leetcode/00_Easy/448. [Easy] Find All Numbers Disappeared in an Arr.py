# 448. [Easy] Find All Numbers Disappeared in an Array

class Solution:
    # [4,3,2,7,8,2,3,1]
    # [8,3,2,7,4,2,3,1]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            1. Используем вспомогательный булевый массив
            2. Все позиции, на которые могли бы встать числа отмечаем True
            3. Выводим индексы позиций, где значение False
        """
        boolean_result = [False] * len(nums)
        for number in nums:
            boolean_result[number - 1] = True
        result = []
        for index in range(len(boolean_result)):
            exist = boolean_result[index]
            if not exist:
                result.append(index + 1)
        return result

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            1. Отмечаем все позиции, на которых могли бы встать числа 
            отрицательным значением.
            2. Выводим индексы не отрицательных чисел
        """
        for index, number in enumerate(nums):
            presented_index = abs(number) - 1
            nums[presented_index] = -abs(nums[presented_index])
        result = []
        for index, number in enumerate(nums):
            if number > 0:
                result.append(index + 1)
        return result

