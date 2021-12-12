


with open('/Users/kevin/PycharmProjects/advent of code/day_5_input.txt', 'r') as text_document:
    data = text_document.read().splitlines()


def convert_binary(string):
    for letter, binary in [("F", "0"), ("B", "1"), ("L", "0"), ("R", "1")]:
        string = string.replace(letter, binary)
    return string


def Decode(highest, code):
    a = list(range(0,highest)) ### highest is 128 or 8
    for binary in code:
        a = [a[:len(a)//2], a[len(a)//2:]]
        a = a[int(binary)]
    return a


def Rows_and_Seats(binary):
    rows = Decode(128, binary[:7])
    seats = Decode(8, binary[-3:])
    return [rows[0], seats[0]]

def Seat_Id(rows_seats):
    return (rows_seats[0] * 8 + rows_seats[1]) 

def Decode_Improved(string): #### since the seat_id is nothing but the binary translated to decimal
    for letter, binary in [("F", "0"), ("B", "1"), ("L", "0"), ("R", "1")]:
        string = string.replace(letter, binary)
    seat_id = int(string,2)
    return seat_id

def scanned_seat_ids(data):
    # return list(Seat_Id( Rows_and_Seats( convert_binary(boarding_pass) ))
    #                     for boarding_pass in data
    #                     )
    return list(Decode_Improved(boarding_pass) 
                        for boarding_pass in data
                        )

def part_1(data):
    return max(scanned_seat_ids(data)) 
               



def all_seat_ids():
    return list( row * 8 + seat 
                    for row in range(0, 128) 
                    for seat in range(0,8) 
                    )


def ids_missing():
    return (set(all_seat_ids()) - set(scanned_seat_ids(data)) )
    

def part_2(data):
    for seat_id in ids_missing():
        if seat_id+1 not in ids_missing() and seat_id-1 not in ids_missing():
            return seat_id


# def part_2(data):
#     return [seat_id for seat_id in ids_missing() 
#             if seat_id+1 not in ids_missing() and seat_id-1 not in ids_missing()
#             ][0]
        

print (  "part 1 solution: " + str(part_1(data)))
print (  "part 2 solution: " + str(part_2(data)))










### pro way
def part_1(data):
    return max(calculate_id(line) for line in data)


def part_2(data):
    seats = set(calculate_id(line) for line in data)

    for seat_id in range(127 * 8):
        if seat_id not in seats and seat_id + 1 in seats and seat_id - 1 in seats:
            return seat_id


def calculate_id(seat):
    # Just convert the seat string into binary...
    # return int(seat.translate(str.maketrans("FLBR", "0011")), 2)
    seat_id = 0
    for i, c in enumerate(seat):
        if c == "B" or c == "R":
            seat_id += 2**(9-i)
    return seat_id 


if __name__ == '__main__':
    with open('/Users/kevin/PycharmProjects/advent of code/day_5_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))

