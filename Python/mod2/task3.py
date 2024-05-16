import sys

def decrypt(s):
    new_str = []
    skip_next = False
    for i in range(len(s)):
        if skip_next:
            skip_next = False
            continue
        if s[i:i+2] == "..":
            if new_str:
                new_str.pop()
            skip_next = True
        elif s[i] == ".":
            continue
        else:
            new_str.append(s[i])

    return "".join(new_str)

if __name__=='__main__':
    for line in sys.stdin:
        print(decrypt(line.strip()))
