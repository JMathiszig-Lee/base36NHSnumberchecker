
SwearWords = [w.upper().strip() 
              for w in open('badwords.csv', 'r').readlines()]


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
    numbers = [int(c) for c in str(number)]

    total = 0
    for idx in range(0,9):
        multiplier = 10 - idx
        total += (numbers[idx] * multiplier)

    _, modtot = divmod(total, 11)
    checkdig = 11 - modtot

    if checkdig == 11:
        checkdig = 0

    return checkdig == numbers[9]


def checkNHSnumber(min, max):
    for num in range(min, max+1):
        #check is valid NHS number
        if validateNHSnumber(num) == True:
            newNHSno = base36encode(num)
            for i in SwearWords:
                if i in newNHSno:
                    print '%d %s %s' % (num, newNHSno, i)

lownum = 1952813321
highnum = 1952813341

checkNHSnumber(lownum, highnum)
