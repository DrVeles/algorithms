# На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?

first_str_set = set(input() + input())

print("YES" if len(first_str_set) == 10 else "NO")