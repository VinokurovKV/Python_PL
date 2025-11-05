from collections import Counter, defaultdict

class Spiral:
    def __init__(self, s):
        self.counter = Counter(s)
        self.order = []
        for char in s:
            if char not in self.order:
                self.order.append(char)

    def __add__(self, other):
        new_counter = self.counter + other.counter
        new_order = self.order.copy()
        for char in other.order:
            if char not in new_order:
                new_order.append(char)
        result = Spiral("")
        result.counter = new_counter
        result.order = new_order
        return result

    def __sub__(self, other):
        new_counter = self.counter - other.counter
        new_order = [char for char in self.order if new_counter[char] > 0]
        result = Spiral("")
        result.counter = new_counter
        result.order = new_order
        return result

    def __mul__(self, n):
        new_counter = Counter({char: count * n for char, count in self.counter.items()})
        result = Spiral("")
        result.counter = new_counter
        result.order = self.order.copy()
        return result

    def __str__(self):
      if not self.order:
          return ""

      sequences = ''.join(char * self.counter[char] for char in self.order)
      n = len(sequences)
      if n == 1:
          return sequences
      rows = n // 2
      cols = n // 2 + 1
      
      directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
      current_dir = 0
      step_length = 2
      steps_taken = 0
      x, y = n // 4, n // 4
      row_chars = defaultdict(dict)
      
      for char in sequences:
          dx, dy = directions[current_dir]
          x += dx
          y += dy
          
          if 0 <= x < rows and 0 <= y < cols:
              row_chars[x][y] = char
              
          steps_taken += 1
          if steps_taken == step_length:
              steps_taken = 1
              current_dir = (current_dir + 1) % 4
              step_length += 1

      result = []
      for i in sorted(row_chars.keys()):
          line_chars = [' '] * cols
          
          for j, char in row_chars[i].items():
              if j < cols:
                  line_chars[j] = char

          line = ''.join(line_chars).rstrip()
          if line:
              result.append(line)

      if result:
          left_spaces = min(len(result[0]) - len(result[0].lstrip()), len(result[-1]) - len(result[-1].lstrip()))
          return '\n'.join(item[left_spaces:] for item in result)
      
      return ""

    def __iter__(self):
        for char in self.order:
            for _ in range(self.counter[char]):
                yield char

'''import random, string
random.seed(42)
A, B =(Spiral("".join(sorted(random.choices(string.ascii_letters, k=1000)))) for i in range(2))
print(A+Spiral(""))
print(B+Spiral("1"))
print(Spiral("2")+A+B)
print(Spiral("3")+A-B*2)
print(B*2-A*3+Spiral("0"))
print("".join(A)+"".join(B))'''
