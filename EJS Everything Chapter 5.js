/*function every(array, test) {
    let result = true;
    for (let i = 0; i < array.length; i++) {
        if (test(array[i]) == true ) {
            result = true;
        } else {
            result = false;
        }
    }
    return result;
  }
  */


  function every(array, test) {
    return !array.some(n => !test(n));
  }


  console.log(every([1, 3, 5], n => n < 10));
  // → true
  console.log(every([2, 4, 16], n => n < 10));
  // → false
  console.log(every([], n => n < 10));
  // → true