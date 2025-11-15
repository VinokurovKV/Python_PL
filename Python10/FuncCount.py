from functools import wraps

def counter(func):
  count = 0

  @wraps(func)
  def wrapped(*args, **kwargs):
    nonlocal count
    count += 1
    return func(*args, **kwargs)
  
  def get_count():
        return count

  wrapped.counter = get_count
  return wrapped


'''
@counter
def fun(a, b):
  return a * 1 + b

print(fun.counter())
res = sum(fun(i, i + 1) for i in range(5))
print(fun.counter(), res)
'''
