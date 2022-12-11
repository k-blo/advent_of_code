test_input = `    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`


// load file
var fs = require("fs");
var text = fs.readFileSync("./day_5_input.txt", "utf-8");



// define
input = test_input
input = text

// parsefest

// 1. parse crates
parsed = input.split("\n")

crates = []
for (let i=0; i<parsed.length; i++) {
    if (parsed[i].includes("1")) {
        stacknumbers_parse = i 
        break; 
    } else { crates.push(parsed[i]) }
}
number_of_stacks = parsed[stacknumbers_parse].replaceAll(' ','')


var ordered_stacks = {}
number_of_stacks.split('').forEach( num => {int = parseInt(num) ; ordered_stacks[int] = []})

// parse: order the stacks
crates.forEach(function(crate_stack) { 
    count = 0
    for (let i=1; i < crate_stack.length; i+=4) {
        count ++
        if (crate_stack[i] != ' ') {
            ordered_stacks[count].push(crate_stack[i])
        }
    }
})





// parse instructions
function parse_instructions(instruction_string) {
    how_many = parseInt(instruction_string.replace("move ", "").split(" ")[0])
    var [from, to] = instruction_string.split("from ")[1].split(" to ")
    return [how_many, from, to]
}


function move_crates(how_many, from, to) {
    for (let i=0; i < how_many; i++) {
        movedCrate = reorder_crates[from].shift()
        reorder_crates[to].unshift(movedCrate)
    }
}


reorder_crates = structuredClone(ordered_stacks)

// move crates
for (let i=stacknumbers_parse+2; i < parsed.length; i++) {
    var [how_many, from, to] = parse_instructions(parsed[i])
    move_crates(how_many, from, to) // part 1
}

//console.log(ordered_stacks)

// part 1
lowest_stack = ""
for (const [key, value] of Object.entries(reorder_crates)) {
    lowest_stack += value[0]
}

console.log("part 1: ", lowest_stack)



// part 2
reorder_crates = structuredClone(ordered_stacks)

function move_crates_together(how_many, from, to) {
    moveCrates = reorder_crates[from].splice(0, how_many)
    moveCrates.reverse()
    moveCrates.forEach( crate => reorder_crates[to].unshift(crate))
}


for (let i=stacknumbers_parse+2; i < parsed.length; i++) {
    var [how_many, from, to] = parse_instructions(parsed[i])
    move_crates_together(how_many, from, to) // part 2
}

lowest_stack = ""
for (const [key, value] of Object.entries(reorder_crates)) {
    lowest_stack += value[0]
}

console.log("part 2: ", lowest_stack)