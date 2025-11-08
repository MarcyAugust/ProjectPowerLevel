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
    [Symbol.iterator]() {
        return new GroupIterator(this);
    };
  }

  class GroupIterator {
      constructor (o) {
          this.i = 0;
          this.group = o.group;
      }

      next () {
          if (this.i == this.group.length || this.i > 10) return {done: true};
        
          let value = this.group[this.i];
          this.i++;
          return {value, done: false};
      }
  }

for (let value of Group.from(["a", "b", "c"])) {
    console.log(value);
  }
  // → a
  // → b
  // → c