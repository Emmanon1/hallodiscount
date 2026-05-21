b64 = open("b64_out.txt").read()
# Replace ambiguous chars with unique patterns
# 0(zero) -> {0}, O(capital O) -> {O}, l(lowercase L) -> {l}, I(capital I) -> {I}, 1(one) -> {1}
safe = ""
for c in b64:
    if c == '0': safe += '{0}'
    elif c == 'O': safe += '{O}'
    elif c == 'l': safe += '{l}'
    elif c == 'I': safe += '{I}'
    elif c == '1': safe += '{1}'
    else: safe += c
# Write 76-char lines of the ORIGINAL b64 (not safe) to verify
# But output the safe version in 76-char groups
lines = [safe[i:i+100] for i in range(0, len(safe), 100)]
for i, line in enumerate(lines):
    print(f"{i:02d}:{line}")
