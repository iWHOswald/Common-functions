import re


# some code to find substrings between two strings. saves in a text file
d = []
for i, line in enumerate(open('stencil_txt.txt',encoding='utf-8-sig')):
    for match in re.finditer('<ROI name="(.+?)" st', line):
        d.append(str(match.group())[11:-4])
        print('Found on line %s: %s' % (i+1, match.group()))
print(d)

with open('OUTTER.txt', 'w',encoding='utf-8-sig') as f:
    for item in d:
        f.write("%s\n" % item)

