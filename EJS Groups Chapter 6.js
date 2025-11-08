// With help from:
// https://gist.github.com/jonurry/48ad237b6ef95b31abd11304ea58b731

class Group {
    constructor(group) {
        this.group = [];
    }
    add(value){
        if (!this.group.includes(value)) {
            this.group.push(value);
        }
    }
    delete(value){
        let index = this.group.indexOf(value);
        if (index !== -1) {
            this.group.splice(index, 1);
        }
    }
    has(value) {
        return this.group.includes(value);
    }
    static from(i) {
        let g = new Group();
        for (let item of i) {
            g.add(item);
          }
          return g;
    }
  }
  
  let group = Group.from([10, 20]);
  console.log(group.has(10));
  // → true
  console.log(group.has(30));
  // → false
  group.add(10);
  group.delete(10);
  console.log(group.has(10));
  // → false