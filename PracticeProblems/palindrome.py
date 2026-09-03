string_1="racecar"
string_2="meowmeow"

print("check 1:",string_1[::-1]==string_1)

print("check 1:",string_2[::-1]==string_2)

string_1="Race car"
string_2="meow meow"

print("check 2:",string_1[::-1]==string_1)

string_1=string_1.replace(" ","").lower()

print("check 2:",string_1[::-1]==string_1)