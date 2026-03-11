import sys
args = sys.argv
num = len(args)
if num == 1:
    print(f"No scores provided. Usage: python3 {args[0]} <score1><score2>...")
else:
    scores = []
    checker = 0
    for i in args[1:]:
        try:
            number = int(i)
            scores += [number]
            checker += 1
        except ValueError:
            print(f"ValueError : cann't convert str ({i}) to int")
    if checker == num - 1:
        print("=== Player Score Analytics ===\n"
              f"Scores processed: {scores}\n"
              f"Total players: {checker}\n"
              f"Total score: {sum(scores)}\n"
              f"Average score: {sum(scores) / checker:.1f}\n"
              f"High score: {max(scores)}\n"
              f"Low score: {min(scores)}\n"
              f"Score range: {max(scores) - min(scores)}")
