function reverseArray(arrayToReverse){
    let newArray = [];
    for (let i = arrayToReverse.length - 1; i > -1; i--){
        newArray.push(arrayToReverse[i]);
    }
    return newArray;
}

function reverseArrayInPlace(arrayToModify) {
    let staticLength = arrayToModify.length;
    let tempArray = [];
    for (let i = 0; i < staticLength; i++) {
        tempArray.push(arrayToModify.pop());
    }
    for (let i = 0; i < staticLength; i++){
        arrayToModify.unshift(tempArray.pop());
    }
    return arrayToModify;
}



console.log(reverseArray(["A", "B", "C"]));
// → ["C", "B", "A"];
let arrayValue = [1, 2, 3, 4, 5];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);
// → [5, 4, 3, 2, 1]