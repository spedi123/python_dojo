/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num2 = 5;
const expected2 = 15;
// Explanation: (1+2+3+4+5)

const num3 = 2.5;
const expected3 = 3;
// Explanation: (1+2)

const num4 = -1;
const expected4 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
// function recursiveSigma(num) {
//     num = Math.floor(num)
//     if (num <= 0){
//         return 0
//     }
//     else{
//         return num + recursiveSigma(num - 1)
//     }
// }
function recursiveSigma(num, i=0) {
    num = Math.floor(num)
    if (num <= 0){
        return 0
    }
    else{
        if (i === num+1) {
            return 0
        }
        return i + recursiveSigma(num, i + 1)
    }
}

// recursive call (pri 0)

console.log(recursiveSigma(num2))
console.log(recursiveSigma(num3))
console.log(recursiveSigma(num4))