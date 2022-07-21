/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
  let answer = {};
  const coins = {
    quarter: 25,
    dime: 10,
    nickel: 5,
    penny: 1,
  };

  for (let key in coins) {
    if (cents >= coins[key]) {
      answer[key] = Math.floor(cents / coins[key]);
      cents = cents % coins[key];
    }
  }
  return answer;
}

// console.log(fewestCoinChange(cents1)); // { quarter: 1 }
// console.log(fewestCoinChange(cents2)); // { quarter: 2 }
// console.log(fewestCoinChange(cents3)); // { nickel: 1, penny: 4 }
console.log(fewestCoinChange(cents4)); // { quarter: 3, dime: 2, penny: 4 }
/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

const numsA = [3, 0, 1];
const expectedA = 2;

const numsB = [3, 0, 1, 2];
const expectedB = null;
// Explanation: nothing is missing

/* 
  Bonus: now the lowest value can now be any integer (including negatives),
  instead of always being 0. 
*/

const numsC = [2, -4, 0, -3, -2, 1];
const expectedC = -1;

const numsD = [5, 2, 7, 8, 4, 9, 3];
const expectedD = 6;
``;
/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums) {
  var lowest = unorderedNums[0];
  var highest = unorderedNums[0];
  var sum1 = 0;

  for (var i = 0; i < unorderedNums.length; i++) {
    if (unorderedNums[i] < lowest) {
      lowest = unorderedNums[i];
    } else if (unorderedNums[i] > highest) {
      highest = unorderedNums[i];
    }
    sum1 += unorderedNums[i];
  }

  var sum2 = 0;
  for (var k = lowest; k <= highest; k++) {
    sum2 += k;
  }

  return sum2 - sum1;
}

// console.log(missingValue(numsA)); // 2
// console.log(missingValue(numsB)); // null
// console.log(missingValue(numsC)); // -1
// console.log(missingValue(numsD)); // 6
