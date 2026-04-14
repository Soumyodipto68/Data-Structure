
//initialization
const mySet = new Set()

//adding element
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
console.log(mySet)

console.log('------------------')
//Has
console.log(mySet.has(2))
console.log(mySet.has(5))

console.log('------------------')
//delete
mySet.delete(2)
console.log(mySet)

console.log('------------------')
//iterating
mySet.forEach(element => {
  console.log(element)
});

console.log('------------------')
//iterating
for(const value of mySet){
  console.log(value)
}

console.log('------------------')
//celaring my set
mySet.clear()
console.log(mySet)

console.log('------------------')
//use case with array
const arr = [1,2,3,2,4,5,4]
const uniqueNum = [...new Set(arr)]
console.log(uniqueNum);

console.log('------------------')
const setA = new Set([1,2,3])
const setB = new Set([5,4,3])

const unionSet = new Set([...setA,...setB])

console.log('------------------')

const SetAasArray = [...setA]
const intersectionArray = SetAasArray.filter((x)=>setB.has(x))

const intersectionSet = new Set(intersectionArray)
console.log(intersectionSet)

console.log('------------------')
const SetAasArrayD = [...setA]
const intersectionArrayD = SetAasArray.filter((x)=>!setB.has(x))
const intersectionSetD = new Set(intersectionArrayD)
console.log(intersectionSetD)