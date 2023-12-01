import re

#find multiple
find_multiple_patterns = re.findall(r'\d|one', "123one")
print(find_multiple_patterns)

# catch overlapping with lookahead
find_multiple_overlapping_patterns = re.findall(r'(?=(\d|one|two|eight))', "123twoneight")
print(find_multiple_overlapping_patterns)
