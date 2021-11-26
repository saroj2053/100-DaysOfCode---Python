# Love Score Calculator
name1 = input("Please enter your name?\n")
name2 = input("Please enter another name?\n")

lowerName1 = name1.lower();
lowerName2 = name2.lower();
name = lowerName1 + lowerName2
count_t = name.count("t")
count_r = name.count("r")
count_u = name.count("u")
count_e = name.count("e")
count_true = count_t + count_r + count_u + count_e

count_l = name.count('l')
count_o = name.count("o")
count_v = name.count("v")

count_love = count_l + count_o + count_v + count_e

print(f"Your love score is {count_true}{count_love} %.")
