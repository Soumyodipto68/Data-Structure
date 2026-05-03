class Node{
  constructor(data){
    this.data = data;
    this.left = null;
    this.right = null;
    this.height = 1;
  }
}
class AVLTree{
  constructor(){
    this.root = null;
  }

  getHeight(node){
    return node ? node.height : 0;
  }

  getBalanceFactor(node){
    return this.getHeight(node.left) - this.getHeight(node.right)
  }

  rightRotate(y){
    const x = y.left;
    const T3 = x.right;

    x.right = y;
    y.left = T3;    

    y.height = Math.max(this.getHeight(y.left),this.getHeight(y.right)) + 1;
    x.height = Math.max(this.getHeight(x.left),this.getHeight(x.right)) + 1;

    return x;
  }

  leftRotate(x){
    const y = x.left;
    const T2 = y.right;

    y.left = x;
    x.right = T2

    y.height = Math.max(this.getHeight(y.left),this.getHeight(y.right)) + 1;
    x.height = Math.max(this.getHeight(x.left),this.getHeight(x.right)) + 1;

    return y;
  }

  insert(node,data){
    if(!node) {
      return new Node(data);
    }
    if(data < node.data){
      node.left = this.insert(node.left,data);
    }else if(data > node.data){
      node.right = this.insert(node.right,data)
    }else{
      return node;
    }
    node.height = 1 +  Math.max(this.getHeight(node.left),this.getHeight(node.right))

    const balance = this.getBalanceFactor(node)
    //left heavy
    if(balance > 1){
      if(data < node.left.data){
        return this.rightRotate(node);
      }else{
        node.left = this.leftRotate(node.left)
        return this.rightRotate(node);
      }
    }
    //right heavy
    if(balance < -1){
      if(data > node.left.data){
        return this.leftRotate(node)
      }else{
        node.right = this.rightRotate(node.right);
        return this.leftRotate(node)
      }
    }
    return node;
  }
  add(data){
    this.root = this.insert(this.root,data)
  }
}

