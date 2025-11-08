let arrays = [[1, 2, 3], [4, 5], [6]];

//Code found online
console.log(arrays.reduce(function(flat, current) {
  return flat.concat(current);
}, []));
// → [1, 2, 3, 4, 5, 6]