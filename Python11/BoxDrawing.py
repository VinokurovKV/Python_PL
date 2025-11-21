def get_box_chars(v_thick, h_thick):
    if v_thick == "LIGHT" and h_thick == "LIGHT":
        return {
            'hline': '─', 'vline': '│',
            'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘',
            'ml': '├', 'mr': '┤', 'tm': '┬', 'bm': '┴', 'cross': '┼'
        }
    elif v_thick == "HEAVY" and h_thick == "LIGHT":
        return {
            'hline': '─', 'vline': '┃',  
            'tl': '┎', 'tr': '┒', 'bl': '┖', 'br': '┚',
            'ml': '┠', 'mr': '┨', 'tm': '┰', 'bm': '┸', 'cross': '╂'
        }
    elif v_thick == "LIGHT" and h_thick == "HEAVY":
        return {
            'hline': '━', 'vline': '│',
            'tl': '┍', 'tr': '┑', 'bl': '┕', 'br': '┙',
            'ml': '┝', 'mr': '┥', 'tm': '┯', 'bm': '┷', 'cross': '┿'
        }
    else: 
        return {
            'hline': '━', 'vline': '┃',
            'tl': '┏', 'tr': '┓', 'bl': '┗', 'br': '┛',
            'ml': '┣', 'mr': '┫', 'tm': '┳', 'bm': '┻', 'cross': '╋'
        }

text = input().strip()
width, v_thick, h_thick = input().split()
width = int(width)

chars = get_box_chars(v_thick, h_thick)

words = text.split()
lines = []
current_line = []
current_length = 0

for word in words:
    word_length = len(word)
    separator_length = 1 if current_line else 0  
    
    if current_line and current_length + separator_length + word_length <= width - 2:
        current_line.append(word)
        current_length += separator_length + word_length
    else:
        if current_line:
            lines.append(current_line)
        current_line = [word]
        current_length = word_length

if current_line:
    lines.append(current_line)

cell_widths = []
for line in lines:
    widths = [len(word) for word in line]
    total_used = sum(widths) + len(line) - 1 
    if total_used < width - 2:
        widths[-1] += (width - 2 - total_used)
    cell_widths.append(widths)

def create_middle_line(upper_cells, lower_cells, upper_widths, lower_widths):
    # Собираем все границы
    all_boundaries = set()
    
    pos = 0
    for w in upper_widths:
        pos += w
        if pos < width - 2:  
            all_boundaries.add(pos)
        pos += 1  
    
    pos = 0
    for w in lower_widths:
        pos += w
        if pos < width - 2: 
            all_boundaries.add(pos)
        pos += 1  
    
    all_boundaries = sorted(all_boundaries)
    
    line_parts = [chars['ml']]
    current_pos = 0
    
    for boundary in all_boundaries:
        if boundary >= width - 2:  
            break
            
        segment_length = boundary - current_pos
        line_parts.append(chars['hline'] * segment_length)
        
        upper_has_boundary = boundary in [sum(upper_widths[:i+1]) + i for i in range(len(upper_widths))]
        lower_has_boundary = boundary in [sum(lower_widths[:i+1]) + i for i in range(len(lower_widths))]
        
        if upper_has_boundary and lower_has_boundary:
            line_parts.append(chars['cross'])
        elif upper_has_boundary:
            line_parts.append(chars['bm'])
        elif lower_has_boundary:
            line_parts.append(chars['tm']) 
        else:
            line_parts.append(chars['hline'])
        
        current_pos = boundary + 1
    
    remaining = width - 2 - current_pos
    if remaining > 0:
        line_parts.append(chars['hline'] * remaining)
    
    line_parts.append(chars['mr'])
    
    result = ''.join(line_parts)
    
    if len(result) != width:
        result = result[:width]
    
    return result

top_line = chars['tl']
for i, w in enumerate(cell_widths[0]):
    top_line += chars['hline'] * w
    if i < len(cell_widths[0]) - 1:
        top_line += chars['tm']
top_line += chars['tr']
print(top_line)

for i, line_words in enumerate(lines):
    line_str = chars['vline']
    for j, word in enumerate(line_words):
        line_str += word.ljust(cell_widths[i][j])
        if j < len(line_words) - 1:
            line_str += chars['vline']
    line_str += chars['vline']
    print(line_str)
    
    if i < len(lines) - 1:
        middle_line = create_middle_line(
            lines[i], lines[i + 1], 
            cell_widths[i], cell_widths[i + 1]
        )
        print(middle_line)

bottom_line = chars['bl']
for i, w in enumerate(cell_widths[-1]):
    bottom_line += chars['hline'] * w
    if i < len(cell_widths[-1]) - 1:
        bottom_line += chars['bm']
bottom_line += chars['br']
print(bottom_line)