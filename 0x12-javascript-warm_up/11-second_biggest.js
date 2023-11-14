#!/usr/bin/node

const argvL = process.argv.length - 2
const argv = process.argv

if (argvL > 1) {
  const ans = [...argv.slice(2)].sort().reverse()[1]
  console.log(ans)
} else {
  console.log(0)
}
