import binascii
import pyperclip

n = input("n: ")
e = input("e: ")
d = input("d: ")
c_num = input("c_num: ")
ans = ""

'''
n = 2108147221
e = 1405360563
d = 3
c = 1180571841
'''

for i in range(int(c_num)):
    c = input(f"c{i+1}: ")
    m = pow(int(c), int(d), int(n))
    ans += binascii.unhexlify(hex (m) [2:]).decode('utf-8')

print(ans)
pyperclip.copy(ans)