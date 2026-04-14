function simpleHashed(key,maxValue){
  let total =0;
   for(let i=0; i < key.length; i++){
    console.log(key[i], key[i].charCodeAt(0));
    let asciiCode = key[i].charCodeAt(0);
    total = total + asciiCode;
   }
   console.log("Toatal num is: ", total)
   return total%maxValue;
}

console.log("markram : ",simpleHashed("markram",45));
console.log("markrma : ",simpleHashed("markrma",45));
