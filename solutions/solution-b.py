lines = []

while True:
	try:
		line = input().strip()
		if line:
			lines.append(line)
	except EOFError:
		break
rows = len(lines)
if rows > 0:
	cols = len(lines[0].split())
else:
	cols = 0

print(rows, cols)