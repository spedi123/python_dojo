/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true; //1 for bonus

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true; //1 for bonus

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {
  if (sortedNums.length == 0) {
    return false;
  } else if (sortedNums.length == 1 && sortedNums[0] != searchNum) {
    return false;
  } else if (sortedNums.length == 1 && sortedNums[0] == searchNum) {
    return true;
  }
  var halfway = Math.floor(sortedNums.length / 2);
  if (sortedNums[halfway] == searchNum) {
    return true;
  } else if (sortedNums[halfway] > searchNum) {
    return binarySearch(sortedNums.slice(0, halfway), searchNum);
  } else if (sortedNums[halfway] < searchNum) {
    return binarySearch(sortedNums.slice(halfway), searchNum);
  }
}

console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true (1 for bonus)
console.log(binarySearch(nums3, searchNum3)); // true (1 for bonus)

function binarySearch2(
  sortedNums,
  searchNum,
  l = 0,
  r = sortedNumsNums.length
) {
  if (sortedNums.length < 1) {
    // return false;
    // return a number if you're looking for the index over true/false
    return -1;
  }

  // as long as our indices are at least 2 elements apart, continue recursion
  if (r - 1 > 1) {
    // declare midpoint
    var mid = Math.floor((r + l) / 2);

    if (sortedNums[mid] == searchNum) {
      // return true;
      // to return index:
      return mid;
    }
    if (searchNum < sortedNums[mid]) {
      return binarySearch2(sortedNums, searchNum, l, mid);
    }

    return binarySearch2(sortedNums, searchNum, mid + 1, r);
  }

  // return sortedNums[l] == searchNum ? true : false;
  // returns the index if true or -1 if false
  return sortedNums[l] == searchNum ? l : -1;
}
