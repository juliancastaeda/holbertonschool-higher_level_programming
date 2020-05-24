#!/usr/bin/node
// script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// You must use the module request
const request = require('request');
const completed = {};
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    for (const tasks of JSON.parse(body)) {
      if (tasks.completed === true) {
        if (!(tasks.userId in completed)) {
          completed[tasks.userId] = 1;
        } else {
          completed[tasks.userId] += 1;
        }
      }
    }
    console.log(completed);
  }
});
