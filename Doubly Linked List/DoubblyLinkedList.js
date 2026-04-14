class Node{
  constructor(data){
    this.previous = null;
    this.data=data;
    this.next=null;
  }
}

class doublyLinkedList{
  constructor(){
    this.head=null;
    this.tail=null;
  }
  Append(data){
    const newNode = new Node(data);
    if(this.head === null){
      this.head = newNode;
      this.tail = newNode;
    }else{
      const currentLastNode = this.tail;
      currentLastNode.next = newNode;
      newNode.previous = currentLastNode;
      this.tail=newNode;
    }
  }
  Prepend(data){
    const newNode = new Node(data);
    if(this.tail === null){
      this.head = newNode;
      this.tail = newNode;
    }else{
      const currentFirstNode = this.head;
      currentFirstNode.previous = newNode;
      newNode.next = currentFirstNode;
      this.head = newNode;
    }
  }
  travarseFromStart(){
    if(this.head === null){
      return
    }
    let current = this.head;
    do{
      console.log(current.data);
      current=current.next;
    }while(current !== null)
  }

  travarseFromEnd(){
    if(this.tail === null){
      return
    }
    let current = this.tail;
    do{
      console.log(current.data);
      current=current.previous;
    }while(current !== null)
  }

  deleteByValue(dataToDelete){
    if(this.head === null){
      return; 
    }
    let current = this.head;
    while(current !== null){
      if(current.data === dataToDelete){
        if(current === this.head){
          this.head = current.next;
          this.head.previous = null
        }
        if(current.data === this.tail){
          this.tail = current.previous;
          this.tail.next=null;
        }
        if(current.previous){
          current.previous.next = current.next;
        }
        if(current.next){
          current.next.previous = current.previous;
        }
      }
      current=current.next;
    }
  }

  searchElem(dataToSearch){
    if(this.head === null){
      return false;
    }

    let current = this.head
    if(current.data === dataToSearch){
      return true;
    }

    while(current.next !== null){
      current = current.next;
      if(current.data === dataToSearch){
      return true;
      }     
    }
    return false
  }

  length(){
    if(this.head === null){
      return 0;
    }
    let count = 1;
    let current = this.head
    while(current.next !== null){
      current = current.next;
      count++;
    }
    return count;
  }
}

export default doublyLinkedList;