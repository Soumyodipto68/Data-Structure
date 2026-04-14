class Stack {
  #items = [];
  constructor() {}
  push(item) {
    this.#items.push(item);
  }
  pop() {
    if (this.#items.length === 0) {
      throw new Error('No Item To Pop');
    }
    return this.#items.pop();
  }
  push(elem){
    return this.#items.push(elem);
  }
  peek(){
    if(this.#items.length === 0){
      throw new Error('No Item To Peek');
    }
    return this.#items[this.#items.length - 1];
  }

  size(){
    return this.#items.length;
  }
  isEmpty(){
    return this.#items.length === 0
  }
}

export default Stack;
