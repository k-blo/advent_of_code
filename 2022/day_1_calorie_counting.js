
// helper functions
// remove item
function remove(list, item) {
    const index = list.indexOf(item);
    const x = list.splice(index, 1);
}
// sum
function sum(list) {
    return list.reduce((partialSum, a) => partialSum + a, 0);
}


// open file
var fs = require("fs");
var text = fs.readFileSync("./day_1_input.txt", "utf-8");


// test data
test_data = `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000`


// decide which data to use
var data = test_data
var data = text


// parsing
var split_data = data.split(/\r?\n/)

let parsed_data = [[]]
var elf = 0

for (const line of split_data){
    if (line == '') {
        elf += 1
        parsed_data.push([])
    }
    else {
        parsed_data[elf].push(parseInt(line))
    }
}


// part 1: find fattest elf
const sums_array = []

parsed_data.forEach(elf_snacks => {
    const calories = sum(elf_snacks)
    sums_array.push(calories)
})

console.log("PART 1: ", Math.max(...sums_array));



// part 2: find the 3 fattest elves
const three_fattest = []
for (var i = 0; i < 3; i++) {
    var fattest = Math.max(...sums_array)
    three_fattest.push(fattest)
    remove(sums_array, fattest)
}

console.log("part 2: ", sum(three_fattest))