//
test_input = `2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`


// load file
var fs = require("fs");
var text = fs.readFileSync("./day_4_input.txt", "utf-8");


// data
input = test_input
input = text

// parse
splitted = input.split(/\r?\n/)
parsed = []
splitted.forEach( list => {
    ranges = list.split(",")
    ranges.forEach(function(range, i) { 
        new_range = []
        ranges[i] = range.split("-").forEach(e => { new_range.push(parseInt(e)) })
        parsed.push( new_range ) 
    })    
})

// part 1
count_contained = 0
for (i = 0; i < parsed.length; i=i+2) {
    i1 = parsed[i]
    i2 = parsed[i+1]
    if (contained(i1, i2) || contained(i2, i1) ) { count_contained++ }
}

function contained(r1, r2) {
    if (r1[0] >= r2[0] && r1[1] <= r2[1]) return true
}

console.log("part 1: ", count_contained)


// part 2
count_overlap = 0
for (i = 0; i < parsed.length; i=i+2) {
    i1 = parsed[i]
    i2 = parsed[i+1]
    if (overlap(i1, i2) || overlap(i2, i1) ) { count_overlap++ }
}

function overlap(r1, r2) {
    if (betwen(r1[0], r2[0], r2[1]) || betwen(r1[1], r2[0], r2[1]) ) return true
}

function betwen(num, low, high) {
    if (num >= low && num <= high) return true
}

console.log("part 2: ", count_overlap)