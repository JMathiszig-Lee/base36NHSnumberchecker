import csv
SwearWords = []
with open('badwords.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    #SwearWords = list(reader)
    for row in reader:
        word = row[0].replace(',', '')
        word = word.upper()
        SwearWords.append(word)

def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36

def validateNHSnumber(number):
    numbers = []
    for d in str(number):
        numbers.append(int(d))

    #this is a horrible way of doing things, please send a pull request with a more elegant way
    a = numbers[0] * 10
    b = numbers[1] * 9
    c = numbers[2] * 8
    d = numbers[3] * 7
    e = numbers[4] * 6
    f = numbers[5] * 5
    g = numbers[6] * 4
    h = numbers[7] * 3
    i = numbers[8] * 2

    tot = a + b + c + d + e + f + g + h + i

    i, modtot = divmod(tot, 11)
    checkdig = 11 - modtot

    if checkdig == 11:
        checkdig = 0

    if checkdig == numbers[9]:
        #nhs number is valid
        return True
    else:
        return False



def checkNHSnumber(min, max):
    while min < max:
        #check is valid NHS number
        if validateNHSnumber(min) == True:
            newNHSno = base36encode(min)
            for i in SwearWords:
                if i in newNHSno:
                    print '%d %s %s' % (min, newNHSno, i)
            min += 1
        else:
            min +=1

lownum = 1952813321
highnum = 1952813341

checkNHSnumber(lownum, highnum)
