function isEven(x) {
    function find(current) {
      if (current == 0) {
          return true;
      } else if (current == 1 || x < 0) {
        return false;
      } else {
        return find(current - 2);
      }
    }
    return find(x);
  }
  
console.log(isEven(50));
console.log(isEven(75));
console.log(isEven(-1));