#!/usr/bin/node

function esrever (list) {
  const res = []

  for (const each of list) {
    res.unshift(each)
  }

  return res
}

module.exports = { esrever }
