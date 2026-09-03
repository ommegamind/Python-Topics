string="this is a string"

new_1=string[::-1]
print(new_1)

new_2=""
for i in range(len(string)-1,-1,-1):
    new_2+=string[i]

print(new_2)