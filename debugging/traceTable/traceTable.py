import sys

def trace(frame, event, argUnused):
  print(event, frame.f_lineno, frame.f_locals)
  return trace

def main():
  for x in range(0,3):
    print(x)


sys.settrace(trace)
main()
sys.settrace(None)