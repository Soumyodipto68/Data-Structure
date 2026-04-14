import LinkedList from "./linkedList.js";

const LinkedListinstance = new LinkedList()

LinkedListinstance.insertAtEnd(45)
LinkedListinstance.insertAtEnd(55)
LinkedListinstance.insertAtEnd(65)
LinkedListinstance.insertAtEnd(75)
LinkedListinstance.travarse()
LinkedListinstance.deleteByValue(45)
console.log('Deleting 45');
LinkedListinstance.travarse()
console.log("Adding Something..");
LinkedListinstance.insertAtEnd(85)
LinkedListinstance.insertAtEnd(95)
LinkedListinstance.insertAtEnd(105)
LinkedListinstance.insertAtEnd(115)
LinkedListinstance.travarse()
console.log("Deleting 105")
LinkedListinstance.deleteByValue(105)
LinkedListinstance.travarse()
console.log("Searching for data",LinkedListinstance.search(85))
console.log("Searching for data",LinkedListinstance.search(45))
console.log("leangth of linkedList",LinkedListinstance.length())
LinkedListinstance.insertAtEnd(125)
LinkedListinstance.insertAtEnd(135)
console.log("leangth of linkedList",LinkedListinstance.length())
LinkedListinstance.insertAtBeggining(145)
LinkedListinstance.travarse()
console.log("Adding in Begining");
LinkedListinstance.insertAtBeggining(155)
LinkedListinstance.travarse()
console.log("leangth of linkedList",LinkedListinstance.length())