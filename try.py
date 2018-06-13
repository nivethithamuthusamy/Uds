lines = []
word = "crane"
with open("wsd_data/crane.definition", 'rt') as f:
    for line in f:
        if(line.startswith('#DEFINITION')):
            lines.append(line)
print(lines)

