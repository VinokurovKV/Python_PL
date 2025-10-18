galaxies = []
while True:
    line = input().strip()
    if not line or line == '.':
        break
    parts = line.split()
    if len(parts) == 4:
        x, y, z = map(float, parts[:3])
        name = parts[3]
        galaxies.append((x, y, z, name))

def distance_sq(gal1, gal2):
    dx = gal1[0] - gal2[0]
    dy = gal1[1] - gal2[1]
    dz = gal1[2] - gal2[2]
    return dx*dx + dy*dy + dz*dz

pairs = [(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i + 1, len(galaxies))]
gal1, gal2 = max(pairs, key=lambda pair: distance_sq(pair[0], pair[1]))

print(*sorted([gal1[3], gal2[3]]))