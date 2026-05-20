// Create a data structure twoStacks that represent two stacks. Implementation of twoStacks should use only one array, i.e., both stacks should use the same array for storing elements. 

// Following functions must be supported by twoStacks.

// push1(int x) --> pushes x to first stack 
// push2(int x) --> pushes x to second stack
// pop1() --> pops an element from first stack and return the popped element 
// pop2() --> pops an element from second stack and return the popped element
// Examples:

// Input: push1(2), push1(3), push2(4), pop1(), pop2(), pop2()
// Output: [3, 4, -1]
// Explanation: push1(2) the stack1 will be [2]
//                         push1(3) the stack1 will be [2,3]
//                         push2(4) the stack2 will be [4]
//                         pop1() the popped element will be 3 from stack1 and stack1 will be [2]
//                         pop2() the popped element will be 4 from stack2 and now stack2 is empty
//                         pop2() the stack2 is now empty hence returned -1

// Input: push1(1), push2(2), pop1(), push1(3), pop1(), pop1()
// Output: [1, 3, -1]
// Explanation: push1(1) the stack1 will be [1]
// push2(2) the stack2 will be [2]
// pop1() the popped element will be 1 
// push1(3) the stack1 will be [3]
// pop1() the popped element will be 3
// pop1() the stack1 is now empty hence returned -1


class TwoStacks {
    constructor(n)
    {
        this.size = n;
        this.arr = new Array(n);
        this.mid = n / 2;
        this.top1 = -1; 
        this.top2 = Math.floor(this.mid) - 1; 
    }

    push1(x)
    {
        if (this.top1 === Math.floor(this.mid) - 1) {
            return;
        }
        this.top1++;
        this.arr[this.top1] = x;
    }

    push2(x)
    {
        if (this.top2 === this.size - 1) {

            return;
        }
        this.top2++;
        this.arr[this.top2] = x;
    }

    pop1()
    {
        if (this.top1 === -1) {
            
            // that means stack1 in empty so return -1
            return -1;
        }
        let ele = this.arr[this.top1];
        this.top1--;
        return ele;
    }

    pop2()
    {
        if (this.top2 === Math.floor(this.mid) - 1) {
            
            // that means stack2 in empty so return -1
            return -1;
        }
        let ele = this.arr[this.top2];
        this.top2--;
        return ele;
    }
}

const ts = new TwoStacks(5);
ts.push1(2);
ts.push1(3);
ts.push2(4);

let res = "";
res += ts.pop1() + " ";
res += ts.pop2() + " ";
res += ts.pop2() + " ";
console.log(res.trim());