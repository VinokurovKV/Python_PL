import sys

data = sys.stdin.buffer.read()
first_null = data.find(b'\x00')
if first_null == -1:
    exit()
main_text = data[:first_null].decode('utf-8')
remaining = data[first_null + 1:]
results = []
encodings = ['koi8-r', 'cp866', 'cp1251', 'iso-8859-5']
while remaining:
    next_null = remaining.find(b'\x00')
    if next_null == -1:
        break
    fragment_bytes = remaining[:next_null]
    found = False
    for encoding in encodings:
        try:
            decoded = fragment_bytes.decode(encoding)
            if decoded in main_text:
                results.append("Yes")
                found = True
                break
        except UnicodeDecodeError:
            continue
    if not found:
        results.append("No")
    remaining = remaining[next_null + 1:]
for result in results:
    print(result)