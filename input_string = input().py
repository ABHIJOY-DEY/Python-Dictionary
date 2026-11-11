input_string = input()
char_counts = {}
for char in input_string:
    char_counts[char] = char_counts.get(char,0)+1

print("Result",char_counts)