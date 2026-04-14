import Queue from "./Queue.js";

const queueInstance = new Queue()

queueInstance.enqueue(45)
queueInstance.enqueue(4)
queueInstance.enqueue(55)
queueInstance.enqueue(75)
queueInstance.enqueue(46)
console.log("Is the Queue is Empty",queueInstance.isEmpty())
console.log("Is the 1st Element on the Queue",queueInstance.peek())
console.log("The 1st Element out from the Queue",queueInstance.dequeue())
console.log("The size of the Queue",queueInstance.size())
queueInstance.enqueue(75)
console.log("The size of the Queue",queueInstance.size())