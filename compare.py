import hashlib
correct = open("b64_out.txt").read()
# Read attempt from file
attempt = open("attempt.txt").read().strip()
print(f"Correct length: {len(correct)}")
print(f"Attempt length: {len(attempt)}")
if len(correct) != len(attempt):
    print(f"LENGTH MISMATCH: diff = {len(correct) - len(attempt)}")
    # Find where they diverge
    minlen = min(len(correct), len(attempt))
    diffs = []
    for i in range(minlen):
        if correct[i] != attempt[i]:
            diffs.append((i, correct[i], attempt[i]))
    print(f"Differences in shared range: {len(diffs)}")
    if diffs:
        for pos, c, a in diffs[:50]:
            print(f"  pos {pos}: correct='{c}'(ord {ord(c)}) attempt='{a}'(ord {ord(a)})")
else:
    diffs = []
    for i in range(len(correct)):
        if correct[i] != attempt[i]:
            diffs.append((i, correct[i], attempt[i]))
    print(f"Differences: {len(diffs)}")
    for pos, c, a in diffs[:50]:
        print(f"  pos {pos}: correct='{c}'(ord {ord(c)}) attempt='{a}'(ord {ord(a)})")
