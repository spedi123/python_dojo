/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
  yo: true,
  abc: 42,
  3: "wassup",
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

const keys3 = ["abc", 3, "yo"];
const vals3 = [42, "wassup", true, "something"];

// const expected3 = False;

const keys4 = ["abc", 3, "yo", "something"];
const vals4 = [42, "wassup", true];
const expected4 = {
  yo: true,
  abc: 42,
  3: "wassup",
  something: "",
};

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {
  var object = {};
  if (values.length > keys.length) {
    return false;
  } else {
    for (var i = 0; i < keys.length; i++) {
      if (values[i] == undefined) {
        object[keys[i]] = "";
      } else {
        object[keys[i]] = values[i];
      }
    }
  }
  console.log(object);
}

// zipArraysIntoMap(keys4, vals4);

/* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const two_obj2 = {
  name: "Zaphod",
  charm: "high",
  morals: "dicey",
  something: 1,
};
const two_expected2 = {
  Zaphod: "name",
  high: "charm",
  dicey: "morals",
  1: "something",
};

const two_obj3 = {
  name: "Zaphod",
  charm: "high",
  morals: "dicey",
  something: "dicey",
};
const two_expected3 = {
  Zaphod: "name",
  high: "charm",
  dicey: ["morals", "something"],
};

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */

// function invertObj(obj) {
//   var newobj = {};
//   for (var key in obj) {
//     // console.log(key);
//     // console.log(obj[key]);
//     newobj[key] = obj[key];
//     newobj(key[value]) = key;
//   }
//   return newobj;
// }

// invertObj(two_obj1);

function invertedHash(obj) {
  oldKeys = Object.keys(obj);
  oldVals = Object.values(obj);
  answer = {};
  for (var i = 0; i < oldVals.length; i++) {
    if (answer[oldVals[i]] != undefined) {
      if (Array.isArray(answer[oldVals[i]])) {
        answer[oldVals[i]].push(oldKeys[i]);
        continue;
      }
      var repeat = [];
      repeat.push(answer[oldVals[i]]);
      repeat.push(oldKeys[i]);
      answer[oldVals[i]] = repeat;
      continue;
    }
    answer[oldVals[i]] = oldKeys[i];
  }
  return answer;
}
// console.log(invertedHash(two_obj1));
// console.log(invertedHash(two_obj2));
// console.log(invertedHash(two_obj3));
