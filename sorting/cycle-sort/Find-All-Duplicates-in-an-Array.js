//  problem link https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function (nums) {
  let arr = [];
  for (let i = 0; i < nums.length; ) {
    if (nums[i] != nums[nums[i] - 1]) {
      [nums[i], nums[nums[i] - 1]] = [nums[nums[i] - 1], nums[i]];
    } else {
      i++;
    }
  }
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i + 1) {
      arr.push(nums[i]);
    }
  }
  return [...new Set(arr)];
};
