# 21.	The 'university' variable contains the name of university where you study. Write a program that displays the contents of the variable with an extra space between characters (add a space between each character).
# UEK w Krakowie
# U E K   w   K r a k o w i e  

s = "UEK w Krakowie"
result = ''
for ch in s:
    result = result + ch + ' '
print(" ".join(s))