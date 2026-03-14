import sys


def convert_to_int(num: str) -> int:
    ans = 0
    for i in num:
        ans *= 10
        if i == '0':
            ans += 0
        elif i == '1':
            ans += 1
        elif i == '2':
            ans += 2
        elif i == '3':
            ans += 3
        elif i == '4':
            ans += 4
        elif i == '5':
            ans += 5
        elif i == '6':
            ans += 6
        elif i == '7':
            ans += 7
        elif i == '8':
            ans += 8
        elif i == '9':
            ans += 9
    return ans


def sep(string: str) -> list:
    num = 1
    for i in string:
        if i == ':':
            return string[:num - 1], convert_to_int(string[num:])
        num += 1


def summ(nums) -> int:
    ans = 0
    for i in nums:
        ans += i
    return ans


def find_max(nums: list) -> int:
    mmax = None
    for i in nums:
        if mmax is None:
            mmax = i
        else:
            if i > mmax:
                mmax = i
    return mmax


def find_min(nums: list) -> int:
    mmin = None
    for i in nums:
        if mmin is None:
            mmin = i
        else:
            if i < mmin:
                mmin = i
    return mmin


dictionary = dict()
args = sys.argv
args_len = len(args)
for i in args[1:]:
    string, num = sep(i)
    dictionary.update({string: num})
print("=== Inventory System Analysis ===")
sum_m = summ(dictionary.values())
print(f"Total items in inventory: {sum_m}")
print(f"Unique item types: {args_len - 1}")
print("\n=== Current Inventory ===")
val = []
key = []
for i in dictionary.keys():
    key += [i]
    print(f"{i}: {dictionary[i]} units ({dictionary[i] / sum_m * 100:.1f}%)")
    val += [dictionary[i]]
print("=== Inventory Statistics ===")
mmax = find_max(val)
mmin = find_min(val)
m_max = None
m_min = None
Moderate = dict()
Scarce = dict()
Restock = []
for i in dictionary.keys():
    if dictionary[i] == mmax and m_max is None:
        m_max = i
    elif dictionary[i] == mmin and m_min is None:
        m_min = i
    if dictionary[i] > 3:
        Moderate.update({i: dictionary[i]})
    else:
        Scarce.update({i: dictionary[i]})
        if dictionary[i] == 1:
            Restock += [i]
print(f"Most abundant: {m_max} ({mmax} units)")
print(f"Least abundant: {m_min} ({mmin} units)")
print("\n=== Item Categories ===")
print(f"Moderate: {Moderate}")
print(f"Scarce: {Scarce}")
print("\n=== Management Suggestions ===")
print(f"• Restock needed: {Restock}")
print("\n=== Dictionary Properties Demo ===")
print(f"Dictionary keys: {key}")
print(f"Dictionary values: {val}")
print(f"Sample lookup - 'sword' in inventory: {'sword' in dictionary}")
