function deepEqual(value1, value2) {
    let value1Keys = Object.keys(value1);
    let value2Keys = Object.keys(value2);
    for (let i = 0; i < value1Keys + 1; i++){
        if (value1[i] === value2[i]) {
            return true;
        }
    }
}


let obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
// → true
console.log(deepEqual(obj, {here: 1, object: 2}));
// → false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
// → true