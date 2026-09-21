#WAF change_strings(st) that replaces the first character of the string with 'X'
def change_string(s):
    s1='X'+s[1:]
    print(s1)
    
change_string("GitHub")

#Output:XitHub
