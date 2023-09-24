"""
  __  __       _   _        _____                          
 |  \/  |     | | | |      / ____|                         
 | \  / | __ _| |_| |__   | (___   ___ _ ____   _____ _ __ 
 | |\/| |/ _` | __| '_ \   \___ \ / _ \ '__\ \ / / _ \ '__|
 | |  | | (_| | |_| | | |  ____) |  __/ |   \ V /  __/ |   
 |_|  |_|\__,_|\__|_| |_| |_____/ \___|_|    \_/ \___|_| 
"""
import sys
from operator import add, sub, mul, truediv

e = None

ops = {
  '/': truediv,
  '*': mul,
  '+': add,
  '-': sub
}

def print_exc(*args):
  global e
  if len(args) == 0:
    if e is not None:
      exc = e.__class__
      msg = e.args[0]
    else:
      exc = sys.exc_info()[0]
      msg = sys.exc_info()[1].args[0]
  else:
    exc = args[0]
    msg = args[1]
  print(exc.__name__ + ':', msg)

def calculate(s: str):
  for op in ops.keys():
    if op in s:
      left, right = s.split(op, 1)
      return ops[op](calculate(left), calculate(right))
  if s.isdigit():
    return int(s)
  else:
    try:
      return float(s)
    except ValueError:
      raise ValueError

def main():
  global e
  print(__doc__)
  for _ in range(3):
    try:
      s = input('>>> ')
    except EOFError:
      break
    except KeyboardInterrupt:
      break
    except BaseException:
      break
    if s == 'exit':
      break
    try:
      print(calculate(s))

    # Let's just catch all the exceptions
    # and test out all the different syntaxes python allows!
    except ValueError:
      print_exc(sys.exc_info()[0], 'Invalid input')
    except ZeroDivisionError:
      print_exc(sys.exc_info()[0], 'Cannot divide by zero')
    except FloatingPointError as e:
      print_exc()
    except OverflowError as e:
      print_exc()
    except LookupError:
      print_exc()
    except Exception:
      print_exc()
  else:
    print('Goodbye!')
    sys.exit(0)

try:
  main()
except Exception:
  with open("flag.txt") as f:
    print(f.read())