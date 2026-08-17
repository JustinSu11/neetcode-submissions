class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let count = new Array()

        for(let num of nums){
            if(!count[num]){
                count[num] = 1
            } else {
                return true
            }
        }
        return false
    }
}
