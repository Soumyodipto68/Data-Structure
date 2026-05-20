// Delete Middle of a Stack
// Given a stack s, remove the middle element of it without using any additional data structure.

// Input: s = [10, 20, 30, 40, 50]
// Output: s = [10, 20, 40, 50]
// Explanation: After deleting the mid which is 30, stack will look like [10, 20, 40, 50].

// Input: s = [1, 2, 3, 4]
// Output:  s = [1, 3, 4]
// Explanation: The stack has 10 elements (even), there are two mid elements 2 and 3, we delete the first of the two.



function deleteMiddle(stack) {
    const elements = [];
    while (stack.length > 0) {
        elements.push(stack.pop());
    }
    const midIndex = Math.floor(elements.length / 2);
    elements.splice(midIndex, 1);
    for (let i = elements.length - 1; i >= 0; i--) {
        stack.push(elements[i]);
    }
}
const stack = [];
stack.push(10);
stack.push(20);
stack.push(30);
stack.push(40);
stack.push(50);

deleteMiddle(stack);

while (stack.length > 0) {
    console.log(stack.pop() + " ");
}
