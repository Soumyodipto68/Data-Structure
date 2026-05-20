// Given string str, we need to print the reverse of individual words.

// Examples:

// Input: Hello World
// Output: olleH dlroW
// Explanation: Each word in "Hello World" is reversed individually, preserving the original order, resulting in "olleH dlroW".

function reverseWords(str)
{
    let st = [];
    let result = "";

    for (let i = 0; i < str.length; ++i) {
        if (str[i] !== " ")
            st.unshift(str[i]);
        else {
            while (st.length !== 0) {
                result += st.shift();
            }
            result += " ";
        }
    }
    while (st.length !== 0) {
        result += st.shift();
    }

    return result;
}

let str = "Hello World";
console.log(reverseWords(str));