#! /usr/bin/env python3

MAX_FRAMES = 10
def score(line):
  # Keep track of how many rolls have been taken
  roll = 0
  # How many points have been collected so far
  total = 0
  # Calculate how many points each roll is worth, so we can easily figure out how many points spares and strikes are worth.
  rollScores = list(map(pointValue, line))

  for frame in range(MAX_FRAMES):
    if line[roll] == "X":
      # Collect points for this roll, plus two future rolls. The extra +1 is because the interval is open on the right.
      total += sum(rollScores[roll:roll+2 + 1])
      roll += 1
    else:
      # Not a strike, so make two attempts and count up the points.
      thisFrameScore = 0
      for attempt in range(2):
        if line[roll].isnumeric() or line[roll] == "-":
          # Earn additional points for number of pins knocked down.
          thisFrameScore += rollScores[roll]
        elif line[roll] == "/":
          # Collect points for this roll, plus the next one. Previously accumulated points are discarded.
          thisFrameScore = sum(rollScores[roll:roll+1 + 1])
        roll += 1
      total += thisFrameScore
    
  return total

def pointValue(mark):
  if mark == "X": return 10
  if mark == "/": return 10
  if mark == "-": return 0
  if mark.isnumeric(): return int(mark, 10)
  raise RuntimeError("Invalid mark")
