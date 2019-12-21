# 크로아티아 알파벳

cralpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()


for t in cralpha:
    word = word.replace(t, '*')

print(len(word))