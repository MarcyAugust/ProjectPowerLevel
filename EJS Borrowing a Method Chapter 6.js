//With help from:
//https://gist.github.com/jonurry/6113de501d42ac397c6d49008ffb1844

let map = {one: true, two: true, hasOwnProperty: true};

// Fix this call
console.log(hasOwnProperty.call(map, "one"));
// → true