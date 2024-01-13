def decode(message_file):

    memo = {}
    maxi = 0
    final_string = ''
    with open(message_file, 'r') as file:
        lines = file.readlines()
        for item in lines:
            number, word = item.split(' ')
            word = word.replace('\n', '')
            number = int(number)
            if maxi < number:
                maxi = number
            memo.update({number: word})

    i = 1
    index = 1

    while index < maxi:
        index = i * (i+1) / 2
        final_string += memo.get(index, "!!fail!!") + " "
        i += 1

    final_string = final_string[:-1]
    if "!!fail!!" in final_string:
        return -1
    else:
        return final_string


print(decode('coding_qual_input.txt'))