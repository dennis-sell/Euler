names = open("names.txt", "r").read().split(",")
names = [name.replace("\"","") for name in names]
sorted_names = sorted(names)

total_score = 0
for i in range(len(sorted_names)):
  word_score = sum(ord(c) - 64 for c in sorted_names[i])
  position = i
  total_score += word_score * (position + 1)
print total_score
