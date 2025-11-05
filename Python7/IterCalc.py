def itercalc():
  stack = []
  cmd = yield

  while True:
    if cmd == '?':
      if stack:
        res = stack[-1]
      else:
        print("Insufficient stack")
        res = None
      cmd = yield res
    else:
      operations = {'+', '-', '*', '/'}
      if cmd.isdigit() or (cmd.startswith('-') and cmd[1:].isdigit()):
        num = int(cmd)
        stack.append(num)
        cmd = yield None
      elif cmd in operations:
        if len(stack) < 2:
          print("Insufficient stack")
          cmd = yield None
        else:
          b = stack.pop()
          a = stack.pop()
          if cmd == '+':
            res = a + b
            stack.append(res)
          elif cmd == '-':
            res = a - b
            stack.append(res)
          elif cmd == '*':
            res = a * b
            stack.append(res)
          else:
            if b == 0:
              print('Zero division')
              stack.append(a)
              stack.append(b)
            else:
              res = a // b
              stack.append(res)
          cmd = yield None
      else: 
        print("Unknown command")
        cmd = yield None

'''
calc = itercalc()
next(calc)
for cmd in "? 3 -2 - what 5 * 2 / ?".split():
    if (res := calc.send(cmd)) is not None:
        print(res)
'''