class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }
  insertAtEnd(data) {
    const newNode = new Node(data);
    if (this.head === null) {
      this.head = newNode;
    } else {
      let current = this.head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = newNode;
    }
  }
  insertAtBeggining(data){
    const newNode = new Node(data); 
    newNode.next = this.head;
    this.head = newNode;
  }
  
  travarse() {
    if (this.head === null) {
      return 'Linked list is Empty';
    }
    let current = this.head;
    console.log(current.data);
    while (current.next !== null) {
      current = current.next;
      console.log(current.data);
    }
  }

  deleteByValue(dataToDelete) {
    if (this.head === null) {
      return;
    }

    let current = this.head;
    if (current.data === dataToDelete) {
      this.head = current.next;
      return;
    }

    let prev = null;

    while (current.next !== null) {
      prev = current;
      current = current.next;
      if (current.data === dataToDelete) {
        prev.next = current.next;
        return;
      }
    }
  }


  search(dataToSearch) {
    if (this.head === null) {
      return false;
    }
    let current = this.head;
    if (current.data === dataToSearch) {
      return true;
    }
    while (current.next !== null) {
      current = current.next;
      if (current.data === dataToSearch) {
        return true;
      }
    }
    return false;
  }
  length() {
    if (this.head === null) {
      return 0;
    }
    let count = 1;
    let current = this.head;
    while (current.next !== null) {
      current = current.next;
      count++;
    }
    return count;
  }
}

export default LinkedList