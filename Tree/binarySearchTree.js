class Node {
  constructor(value){
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree{
  constructor(){
    this.root = null;
  }
// --------------------------------------------Print method------------------------------------------  
  print(){
    console.log(this.root);
  }
// --------------------------------------------Insert method------------------------------------------  
  insert(value){
    const newNode = new Node(value);
    if (this.root == null){
      this.root = newNode;
      return;
    }
  let  current = this.root;
  
  while(true){
    if(value === current.value){
      return
      // return console.warn(`Value ${value} already exists. Skipping insert.`);
    }
    else if(value < current.value){
      if(current.left == null){
        current.left = newNode;
      }else{
        current = current.left;
      }
    }
    else{
      if(current.right == null){
        current.right = newNode;
      }else{
        current = current.right;
      }
    }
  }
  }
// --------------------------------------------Search method------------------------------------------ 
  search(value){
    if(this.root === null){
      return false;
    }
    let current = this.root;
    while(current){
      if(value === current.value){
        return true;
      }else if(value < current.value){
        current = current.left;
      }else{
        current = current.right;
      }
    }
    return false;
  }
  // --------------------------------------------Traversal methods------------------------------------------
  levelOrder(){
    const result = [];
    if(this.root === null){
      return result;
    }
    const queue = [this.root];
    while(queue.length > 0){
      const current = queue.shift();
      result.push(current.value);
      if(current.left){
        queue.push(current.left);
      }
      if(current.right){
        queue.push(current.right);
      }
    }
    return result;
  }

  preOrder(node = this.root,result = []){
     if(node){
      result.push(node.value);
      this.preOrder(node.left,result);
      this.preOrder(node.right,result);
     }
     return result;
  }

  inOrder(node = this.root,result = []){
     if(node){
      this.inOrder(node.left,result);
      result.push(node.value);
      this.inOrder(node.right,result);
     }
     return result;
  }

  postOrder(node = this.root,result = []){
     if(node){
      this.postOrder(node.left,result);
      this.postOrder(node.right,result);
      result.push(node.value);
     }
    
     return result;
    }
}

// --------------------------------------------Testing the Binary Search Tree------------------------------------------
const bst = new BinarySearchTree();
bst.insert(10);
bst.insert(5);
bst.insert(15);
bst.insert(3);
bst.insert(7);
bst.print();
console.log("Search 10:", bst.search(10)); // true
console.log("Search 1:", bst.search(1)); // false
console.log("Level Order Traversal:", bst.levelOrder()); // [10, 5, 15, 3, 7]
console.log("Pre Order Traversal:", bst.preOrder()); // [10, 5, 3, 7, 15]
console.log("In Order Traversal:", bst.inOrder()); // [3, 5, 7, 10, 15]
console.log("Post Order Traversal:", bst.postOrder()); // [3, 7, 5, 15, 10]