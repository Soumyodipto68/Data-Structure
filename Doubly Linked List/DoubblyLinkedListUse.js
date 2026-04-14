import doublyLinkedList from "./DoubblyLinkedList.js";

const doubly = new doublyLinkedList()

doubly.Append(45)
doubly.Append(55)
doubly.travarseFromStart()
doubly.Prepend(12)
doubly.Prepend(15)
console.log("after Prepend")
doubly.travarseFromStart()
console.log("---------------")
doubly.travarseFromEnd()
doubly.Append(25)
doubly.Append(95)
console.log("---------------")
doubly.travarseFromStart()
doubly.deleteByValue(55)
console.log("---------------")
doubly.travarseFromStart()
console.log("---------------")
console.log("Searching Elem", doubly.searchElem(45));
console.log("---------------")
console.log("Searching Elem", doubly.length());