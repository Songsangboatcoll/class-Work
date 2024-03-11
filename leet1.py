roman = {"I":1, "V": 5,"X":10,"L": 50,"C":100, "D":500,"M":1000}
Result = 0

for i in range(len(s)):
    if i + 1< len(s) and roman [s[i]]< roman:
        Result -= roman[s[i]]
    else:
        Result += roman[s[i]]

return Result
