class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let count = new Array(26)
        if(s.length !== t.length) {
            return false
        }

        for(let c of s){
            let charLocation = c.charCodeAt(0) - 'a'.charCodeAt(0)
            if(!count[charLocation]){
                count[charLocation] = 1
            } else {
                count[charLocation]++
            }
        }
        
        for(let c of t){
            let charLocation = c.charCodeAt(0) - 'a'.charCodeAt(0)
            if(!count[charLocation]){
                return false
            } else count[charLocation]--
        }
        return true
    }
}
