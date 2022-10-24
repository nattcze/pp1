# 26.	The payment card is secured with a four-digit PIN code (0805). Write a program that checks if the PIN code entered in the payment terminal is correct. The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked. Sample result:
# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.


# pin= "0805"
# first_try = int(input("Enter the PIN code: "))
# if first_try == pin:
#     print("Correct <3")
# else:
#     print("Incorrect...")
#     second_try= int(input("Try again: "))
#     if second_try == pin :
#         print("Correct <3")
#     else:
#         print("Incorrect...")
#         third_try = int(input("Try again: "))
#         if third_try == pin:
#             print("Correct")
#         else:
#             print("Acces denied D; contact your bank")


pin = "0805"

for i in range(0,3):
    user_input = int(input("Enter the PIN code: "))

    if user_input == pin:
        print("Correct")
        exit()

    print("Incorrect")

print("Sorry, access denied D:")










