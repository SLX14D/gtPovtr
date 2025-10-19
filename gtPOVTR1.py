# Задание 1.
# text = input("Введите строку: ")

# clean_text = text.replace(" ", "").lower()
# reversed_text = ""

# for ch in clean_text:
#     reversed_text = ch + reversed_text

# if clean_text == reversed_text:
#     print("YES")
# else:
#     print("NO")

#Задание 2.
text = input("Введите строку соо скобками:")

stack = []
pairs = {')': '(', ']': '[', '}': '{'}
ok = True

for ch in text:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if not stack or stack[-1] != pairs[ch]:
            ok = False
            break
        stack.pop()

if ok and not stack:
    print("YES")
else:
    print("NO")
