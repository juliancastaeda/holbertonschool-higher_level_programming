#!/usr/bin/node

const mylist = require('./100-data').mylist;
const newList = mylist.map((val, indx) => { return val * indx; });

console.log(mylist);
console.log(newList);
