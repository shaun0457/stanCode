"""
File: similarity.py (extension)
Name:
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    """
    a = str(input('Please give me a DNA to research: '))
    a = a.upper()
    # print(long_sequence())
    # dna = long_sequence(a)
    b = str(input('What DNA do you want to match?:  '))
    b = b.upper()
    match = match_process(a, b)
    pass

# def long_sequence(a):
#     a = a.upper()
#     print(a)
#     return a

def match_process(a, b):
    max = 0
    dna_max = ''
    for i in range(len(a)-len(b)+1):
        a_1 = 0
        alp = a[0+i:len(b)+i]
        for j in range(len(b)):
            if alp[j] == b[j]:
                a_1 += 1
                if a_1 > max:
                    max = a_1
                    dna_max = alp
    print(max/len(b))
    print('The best match is: ' + str(dna_max))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
