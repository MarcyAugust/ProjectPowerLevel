function range(start, end, step = 1) { 
    let totalRange = [];
    if (start < end){
        for(let i = start; i < end + 1; i+= step){
            totalRange.push(i);
    } 
        } else {
            for (let i = start; i > end - 1; i+= step){
                totalRange.push(i);
        }
    } return totalRange;
 } 

 function sum(numbers){
     let sumRange = 0;
     for (let i = 0; i < numbers.length; i++){
        sumRange += numbers[i];
     }
     
     return sumRange;
 }

/* 
function range(start, end, step) { 
    let totalRange = 0;
    for( let i = start; i < end + 1; i+= step){
        totalRange += i;
    }
    return totalRange;
}
*/
console.log(range(1,10,1));
console.log(range(5, 2, -1));
console.log(sum(range(1, 10)));