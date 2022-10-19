from cgi import print_arguments


def count(value):
    con = 0
    vow = 0
    for i in range(len(value)):
        if value [i] in ['a', 'e', 'i', 'o', 'u']:
            vow = vow + 1
        else:
            con = con + 1
    
    print('The count of vowel is:', vow)
    print('The count of consonant is:', con)

x = input('Input any word:')
count(x)