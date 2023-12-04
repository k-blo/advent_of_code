
DATA = File.readlines('day_4_input.txt', chomp: true).freeze

EXAMPLE = [
'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
].freeze


def parse_cards(input)
    cards = {}
    input.map.with_index do |card, i|
        nums = card.split(':')[1].split('|')
        cards[i+1] = {
            "winning": nums[0].split.map{|s| s.to_i},
            "mine": nums[1].split.map{|s| s.to_i}
        }
        cards[i+1][:actual_winners] = cards[i+1][:winning].intersection(cards[i+1][:mine])
    end
    cards
end


def part_1(input)
    cards = parse_cards(input)
    cards.map{|key, card| 2**(card[:actual_winners].count-1 ) if card[:actual_winners].count != 0}.compact.sum
end

p 'EXAMPLE 1: ' + part_1(EXAMPLE).to_s
p 'PART 1: ' + part_1(DATA).to_s



def part_2(input)
    $cards = parse_cards(input)
    $card_counter = {}
    $card_counter.default_proc = proc { 0 }

    (1..input.count).to_a.map.with_index do |i|
        _recursive_cards_process(i)
    end
    $card_counter.values.sum
end


def _recursive_cards_process(card_num)
    matching_numbers = $cards[card_num][:actual_winners].count
    $card_counter[card_num] += 1

    next_cards = (1..matching_numbers).to_a.map{|n| n+card_num}
    next_cards.map do |card_index|
        _recursive_cards_process(card_index)
    end
end

p 'EXAMPLE 2: ' + part_2(EXAMPLE).to_s
p 'PART 2: ' + part_2(DATA).to_s