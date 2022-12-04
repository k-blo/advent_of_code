

test_input = `A Y
B X
C Z`




var fs = require("fs");
var text = fs.readFileSync("./day_2_input.txt", "utf-8");





// use
var data = test_input
var data = text

// parsing
const split_data = data.split(/\r?\n/)
const parsed_data = []

split_data.forEach(element => {
    element = element.split(" ")
    parsed_data.push(element)
});






const P1 = "ABC"
const P2 = "XYZ"

function play(opponent, you) {
    var o_move = P1.indexOf(opponent) + 1
    var y_move = P2.indexOf(you) + 1
    var outcome = 0 // you lose - default assumption

    // value correction for case scissors / rock
    if (y_move == 1 && o_move == 3) {
        y_move = 4
    }
    if (y_move == 3 && o_move == 1) {
        o_move = 4
    }
    // you win
    if (y_move > o_move) {
        outcome = 6
    // tie
    } else if (y_move === o_move) {
        outcome = 3
    }
    return outcome + P2.indexOf(you) + 1
}


var score = 0
parsed_data.forEach(game => {
    score += play(game[0], game[1])
})

console.log("part 1: ", score)


// part 2: second column is outcome, not your move
function play_rigged(opponent, rigged_outcome) {
    var o_move = P1.indexOf(opponent) + 1
    var outcome = P2.indexOf(rigged_outcome) * 3

    // tie
    var y_move = o_move

    // lose
    if (outcome == 0) {
        y_move = o_move - 1
        if (y_move == 0)
            y_move = 3
    }

    // win
    if (outcome == 6) {
        y_move = o_move + 1
        if (y_move == 4)
            y_move = 1
    }

    return outcome + y_move
}

var score = 0
parsed_data.forEach(game => {
    score += play_rigged(game[0], game[1])
})

console.log("part 2: ", score)

// cleaner solution:
// convert ABC and XYZ to 012
// Part 1: result = (vals[1] - vals[0] + 1) % 3 # 0->loss, 1->draw, 2->win
// Part 2: throw = (vals[0] + vals[1] - 1) % 3 # 0->rock, 1->paper, 2->scissors



// function play(opponent, you) {
//     var o_move = P1.indexOf(opponent) + 1
//     var y_move = P2.indexOf(you) + 1
//     var outcome = (y_move - o_move + 1) % 3

//     return outcome*3 + P2.indexOf(you) + 1
// }