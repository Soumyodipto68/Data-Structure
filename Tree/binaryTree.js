class Node {
    constructor(value) {
        this.value = value;
        this.left = null;  
        this.right = null; 
    }
}
class BinaryTree {
    constructor() {
        this.root = null;
    }
    insert(value) {
        const newNode = new Node(value);

        if (this.root === null) {
            this.root = newNode;
            return;
        }

        let current = this.root;
        while (true) {
            if (value === current.value) {
                console.warn(`Value ${value} already exists. Skipping insert.`);
                return; 
            }
            if (value < current.value) {
                if (!current.left) {
                    current.left = newNode;
                    return;
                }
                current = current.left;
            } else {
                if (!current.right) {
                    current.right = newNode;
                    return;
                }
                current = current.right;
            }
        }
    }

    search(value) {
        let current = this.root;
        while (current) {
            if (value === current.value) return true;
            current = value < current.value ? current.left : current.right;
        }
        return false;
    }

    inorder(node = this.root) {
        if (!node) return;
        this.inorder(node.left);
        process.stdout.write(node.value + " ");
        this.inorder(node.right);
    }
    preorder(node = this.root) {
        if (!node) return;
        process.stdout.write(node.value + " ");
        this.preorder(node.left);
        this.preorder(node.right);
    }

    postorder(node = this.root) {
        if (!node) return;
        this.postorder(node.left);
        this.postorder(node.right);
        process.stdout.write(node.value + " ");
    }
}
const tree = new BinaryTree();
tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(3);
tree.insert(7);
tree.insert(12);
tree.insert(18);

console.log("Search 7:", tree.search(7)); 
console.log("------------------------------");
console.log("Search 20:", tree.search(20)); 
console.log("------------------------------");
console.log("In-order:"); tree.inorder(); console.log();
console.log("------------------------------");
console.log("Pre-order:"); tree.preorder(); console.log();
console.log("------------------------------");
console.log("Post-order:"); tree.postorder(); console.log();