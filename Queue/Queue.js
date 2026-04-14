class Queue {
    #items=[]
    constructor(){}
    enqueue(elem){
      this.#items.unshift(elem);
    }

    dequeue(){
      if(this.#items.length === 0){
        throw new Error("The Queue is Empty")
      }
      return this.#items.pop()
    }

    peek(){
      if(this.#items.length === 0){
        throw new Error("The Queue is Empty")
      }
      return this.#items[this.#items.length-1];
    }
    size(){
      return this.#items.length;
    }

    isEmpty(){
      return this.#items.length === 0;
    }
}

export default Queue;