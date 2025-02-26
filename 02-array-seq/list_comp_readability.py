# build a list using loop
symbols = '$¢£¥€¤'

codes = []
for symbol in symbols:
	codes.append(ord(symbol))
print(codes)

# build a list usinf listcomp
codes = [ord(symbol) for symbol in symbols]
print(codes)
