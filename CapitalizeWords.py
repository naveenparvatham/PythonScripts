# lines = []
# while True:
#     l = input("Enter sequence of lines: ")
#     if l:
#         lines.append(l.upper())
#     else:
#         break
#
# for l in lines:
#     print(l)


# Program that accepts a sentence and calculate the number of upper case letters and lower case letters
sentence = input("Type a sentence: ")
sentence = list(sentence)

u, l = 0, 0
for i in sentence:
    if i.isupper():
        u = u + 1
    if i.islower():
        l = l + 1
    else:
        pass

print("UPPER CASE:", u)
print("LOWER CASE:", l)


