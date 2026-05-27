//Next Greater Element in Array


// Given an array arr[] of integers, determine the Next Greater Element (NGE) for every element in the array, maintaining the order of appearance.

// The Next Greater Element for an element x is defined as the first element to the right of x in the array that is strictly greater than x.
// If no such element exists for an element, its Next Greater Element is -1.
// Examples: 

// Input: arr[] = [1, 3, 2, 4]
// Output: [3, 4, 4, -1]
// Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.

// Input: arr[] = [6, 8, 0, 1, 3]
// Output: [8, -1, 1, 3, -1]
// Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on right and hence -1.

function nextLargerElement(arr) {

    let n = arr.length;
    let res = new Array(n).fill(-1);

    // Iterate through each element in the array
    for (let i = 0; i < n; i++) {

        // Check for the next greater element
        // in the rest of the array
        for (let j = i + 1; j < n; j++) {
            if (arr[j] > arr[i]) {
                res[i] = arr[j];
                break;
            }
        }
    }

    return res;
}

// Driver Code
let arr1 = [ 6, 8, 0, 1, 3 ];
let res1 = nextLargerElement(arr1);
console.log(res1.join(" "));
let arr2 = [ 1, 5, 8, 5, 3 ];
let res2 = nextLargerElement(arr2);
console.log(res2.join(" "));