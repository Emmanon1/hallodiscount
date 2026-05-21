import base64, hashlib
with open("slider.html", "rb") as f:
    data = f.read()
b64 = base64.b64encode(data).decode()
print(len(b64))
print(hashlib.md5(b64.encode()).hexdigest().upper())
with open("b64_out.txt", "w") as f:
    f.write(b64)
print("DONE")
