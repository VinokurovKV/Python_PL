lines = []
while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

graph = {}
names = []
for line in lines:
    if ": " in line:
        name, rest = line.split(": ", 1)
        plan = [x.strip() for x in rest.split(", ")] if rest.strip() else []
    else:
        name = line.rstrip(":")
        plan = []
    graph[name] = plan
    names.append(name)

all_names = set(names)
for name, plan in graph.items():
    for p in plan:
        if p not in all_names:
            print("UNKNOWN")
            exit()

def c3_linearize(name, graph, visited, cache):
    if name in cache:
        return cache[name]
    if name in visited:
        raise ValueError("CYCLE")
    visited.add(name)
    
    direct = graph[name]
    
    if not direct:
        result = [name]
        cache[name] = result
        visited.remove(name)
        return result
    
    mros = [c3_linearize(n, graph, visited, cache) for n in direct]
    
    result = [name]
    mros_work = [list(mro) for mro in mros]
    direct_work = list(direct)
    
    while True:
        candidate = None
        all_seqs = mros_work + [direct_work]
        
        for seq in all_seqs:
            if seq:
                potential = seq[0]
                valid = True
                for other_seq in all_seqs:
                    if other_seq and potential in other_seq[1:]:
                        valid = False
                        break
                if valid:
                    candidate = potential
                    break
        
        if candidate is None:
            if any(seq for seq in all_seqs):
                raise ValueError("INEFFECTIVE")
            break
            
        result.append(candidate)
        
        for seq in all_seqs:
            if seq and seq[0] == candidate:
                del seq[0]
    
    visited.remove(name)
    cache[name] = result
    return result

try:
    full_plans = {}
    for name in names:
        cache = {}
        mro = c3_linearize(name, graph, set(), cache)
        full_plans[name] = mro[1:]
except ValueError as e:
    if str(e) == "CYCLE":
        print("CYCLE")
    elif str(e) == "INEFFECTIVE":
        print("INEFFECTIVE")
    exit()

for name in names:
    print(f"{name}: {', '.join(full_plans[name])}")