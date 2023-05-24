// 448. [Easy] Find All Numbers Disappeared in an Array

// Given an array nums of n integers where nums[i] is in the range [1, n], 
// return an array of all the integers in the range [1, n] that do not 
// appear in nums.

class Solution {
    // 1. Сделать все позиции на которых могли бы стоять числа отрицательными
    // 2. Вывести все позиции, на которых стоят не отрицательные числа

    func findDisappearedNumbers(_ nums: [Int]) -> [Int] {
        var nums = nums
        for (i, number) in nums.enumerated() {
            let includedPosition: Int = abs(number) - 1;
            nums[includedPosition] = -1 * abs(nums[includedPosition]);
        }
        var result: [Int] = [];
        for (index, number) in nums.enumerated() {
            if number > 0 {
                result.append(index+1);
            }
        }
        return result;
    }
}