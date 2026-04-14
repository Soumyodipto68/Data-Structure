import Stack from './Stack.js';

const stack = new Stack();

stack.push(10)
stack.push(14)
stack.push(18)

console.log('The last Element in Stack is', stack.peek())
console.log('The Poping Element in Stack is', stack.pop())
console.log('The last Element in Stack is', stack.peek())
console.log('The Size in Stack is', stack.size())
console.log('The Stack is Empty or Not', stack.isEmpty())
