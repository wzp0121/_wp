class Vector {
    constructor(c) { this.c = c; }
    add(o) { return new Vector(this.c.map((v, i) => v + o.c[i])); }
    subtract(o) { return new Vector(this.c.map((v, i) => v - o.c[i])); }
    dot(o) { return this.c.reduce((s, v, i) => s + v * o.c[i], 0); }
}

let a = new Vector([1, 2, 3]);
let b = new Vector([4, 5, 6]);

console.log(a.add(b));
console.log(a.subtract(b));
console.log(a.dot(b));