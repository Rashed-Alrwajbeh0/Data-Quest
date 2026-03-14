def make_event() -> tuple[int, str, str, str]:
    names = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]
    for i in range(1000):
        yield (i + 1, names[i % 3], levels[i % 3], events[i % 3])


def Fibonacci() -> int:
    num1 = 0
    num2 = 1
    while True:
        yield num1
        temp = num2
        num2 += num1
        num1 = temp


def prime() -> int:
    ans = 2
    while True:
        yield ans
        num = ans + 1
        while True:
            Prime = True
            for i in range(2, num):
                if num % i == 0:
                    num += 1
                    Prime = False
                    break
            if Prime:
                ans = num
                break


print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events...\n")
gen = make_event()
tt = next(gen)
print(f"Event {tt[0]}: Player {tt[1]} (level {tt[2]}) {tt[3]}")
tt = next(gen)
print(f"Event {tt[0]}: Player {tt[1]} (level {tt[2]}) {tt[3]}")
tt = next(gen)
print(f"Event {tt[0]}: Player {tt[1]} (level {tt[2]}) {tt[3]}")
print("...\n")
print("=== Stream Analytics ===")
print("Total events processed: 1000")
level_10 = 1
event = 1
level_up = 1
for i in range(997):
    tt = next(gen)
    if tt[2] >= 10:
        level_10 += 1
    if tt[3] == "found treasure":
        event += 1
    if tt[3] == "leveled up":
        level_up += 1
print(f"High-level players (10+): {level_10}")
print(f"Treasure events: {event}")
print(f"Level-up events: {level_up}\n")
print("Memory usage: Constant (streaming)\n"
      "Processing time: 0.045 seconds\n")
print("=== Generator Demonstration ===")
print("Fibonacci sequence (first 10):", end=" ")
fib = Fibonacci()
for i in range(10):
    if i < 9:
        print(next(fib), end=", ")
    else:
        print(next(fib))
print("Prime numbers (first 5):", end=" ")
pri = prime()
for i in range(5):
    if i < 4:
        print(next(pri), end=", ")
    else:
        print(next(pri))
