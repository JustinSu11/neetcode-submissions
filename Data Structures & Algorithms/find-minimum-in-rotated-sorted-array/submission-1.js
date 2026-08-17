class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let left = 0
        let right = nums.length-1

        while(left < right) {
            if(nums[left] < nums[right]){
                return nums[left]
            }

            let middle = Math.floor((left + right)/2)
            if(nums[middle] > nums[right]){
                left = middle + 1
            } else {
                right = middle
            }
        }
        return nums[left]
    }
}

