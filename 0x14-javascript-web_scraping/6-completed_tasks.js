#!/usr/bin/node
const quest = require('request');
const url = process.argv[2];

function countTodos (taskList) {
  const retObj = {};
  for (let count = 0; count < taskList.length; count++) {
    const userId = taskList[count].userId;
    const comp = taskList[count].comp;
    if (Object.prototype.hasOwnProperty.call(retObj, userId) && comp) {
      retObj[userId] += 1;
    } else if (comp) {
      retObj[userId] = 1;
    }
  }
  console.log(retObj);
}

quest
  .get(url, (err, res, body) => {
    if (err) { console.log(err); }
    countTodos(JSON.parse(body));
  });
