

test_input = `A Y
B X
C Z`








// use
var data = test_input

// parsing
const split_data = data.split(/\r?\n/)
const parsed_data = []

split_data.forEach(element => {
    element = element.split(" ")
    parsed_data.push(element)
});

console.log(parsed_data)


const rules = {
    "rock": {
        "score": 1,
        "short": ["a","x"],
        "beats": "scissors"
    },
    "paper": {
        "score": 2,
        "short": ["b", "y"],
        "beats": "rock"
    }
}

const P1 = "ABC"
const P2 = "XYZ"

function play(move1, move2) {
    if (move1 == "")
    if (P1.indexOf(move1) > P2.indexOf(move2)) {

    }
}