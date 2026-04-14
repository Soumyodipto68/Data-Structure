class HashTable{
  constructor(size = 50){
    this.keyMap = new Array(50);
  }
  simpleHashed(key,maxValue){
  let total =0;
   for(let i=0; i < key.length; i++){
    let asciiCode = key[i].charCodeAt(0);
    total = total + asciiCode;
   }
   return total%maxValue;
  }

  set(key,value){
    const hashcode = this.simpleHashed(key,this.keyMap.length);
    if(!this.keyMap[hashcode]){
      this.keyMap[hashcode] = [];
    }
    console.log("hashcode",hashcode)
    this.keyMap[hashcode].push([key,value])
  }

  get(key){
     const hashcode = this.simpleHashed(key,this.keyMap.length);
     const result = this.keyMap[hashcode];
     for (let pair of result){
      if(pair[0] === key){
        return pair[1];
      }
     }
     console.log(result);
     return undefined;
  }
}

const hashTable = new HashTable();
hashTable.set("markram","SA")
console.log("Value of markram is ",hashTable.get("markram"))
hashTable.set("markrma","LSG")
console.log("Value of markrma is ",hashTable.get("markrma"))
console.log("Value of markrma is ",hashTable.get("marrkma"))