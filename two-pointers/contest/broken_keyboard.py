t = int(input())
for _ in range(t):
    chars = list(input())
    i=0
    if len(chars) == 1:
        print(''.join(chars))
    else:

        while i+1 < len(chars):
            if chars[i] == chars[i+1]:
                chars.pop(i)
                chars.pop(i)
            else:
                i+=1
        result = sorted(set(chars))

        print(''.join(result))