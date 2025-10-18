words = []
line = input().strip()
while line:
    words.extend(line.split())
    line = input().strip()

sets = {'ALL': set(words)}

line = input().strip()
while line:
    parts = line.split()
    
    if parts[0] == 'print':
        names = parts[1].split(',')
        result_set = set()
        for name in names:
          result_set |= sets[name]
        print(' '.join(sorted(result_set)))
    
    elif parts[0] == 'search':
        if parts[2] == 'where':
            source = set()
            for n in parts[1].split(','):
                source |= sets[n]
            sets[parts[5]] = {w for w in source if parts[3] in w}
        
        else:
            source = set()
            for n in parts[1].split(','):
                source |= sets[n]
            search = set()
            for n in parts[3].split(','):
                search |= sets[n]
            sets[parts[5]] = source & search
    
    line = input().strip()