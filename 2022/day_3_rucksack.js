test_input = `vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`


// load file
var fs = require("fs");
var text = fs.readFileSync("./day_3_input.txt", "utf-8");


// define
var data = test_input
var data = text


// parsing
const split_data = data.split(/\r?\n/)

// part 1
ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHA = ALPHABET_LOWER + ALPHABET_LOWER.toUpperCase()

priority_sum = 0

split_data.forEach(contents => {
    len = contents.length / 2
    compartments = [contents.slice(0,len).split(""), contents.slice(len, len*2).split("")]
    shared_item = compartments[0].filter(value => compartments[1].includes(value))[0]
    priority_sum += ALPHA.indexOf(shared_item)+1
});

console.log("part 1: ", priority_sum)


// part 2
priority_sum = 0

for (i = 0; i < split_data.length; i=i+3) {
    var [rucksack1, rucksack2, rucksack3] = [split_data[i], split_data[i+1], split_data[i+2]]
    elf_group = [rucksack1.split(""), rucksack2.split(""), rucksack3.split("")]
    shared_item = elf_group.reduce((a, b) => a.filter(c => b.includes(c)))[0]
    priority_sum += ALPHA.indexOf(shared_item)+1
}

console.log("part 2: ", priority_sum)