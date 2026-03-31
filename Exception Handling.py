# # Runtime is also called as execption
# try:
#     a=int(input("Enter a value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except ZeroDivisionError :
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer only")

#can we handle multiple different kinds of exception with single block(yes)
# try:
#     a=int(input("Enter a value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError ) as message:
#      print(message)

#The concept of default execpt block,genrally we used for writting normal message or showing normal error
# try:
#     a=int(input("Enter a value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError ) as message:
#     print("Enter the correct number",message)
# except:
#     print("This is default part of except block")

# try:
#     a=int(input("Enter a value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError ) as message:
#     print("Enter the correct number",message)
# else:
#     print("Everything is ok")

    #Finally block will always executed whether try block genrate error or not
# try:
#     a=int(input("Enter a value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError ) as message:
#     print("Enter the correct number",message)
# finally:
#     print("I will allways executed")

   # nested try ecxcept block
# try:
#     a=int(input("Enter a value of a:"))
#     b=int(input("Enter the value of b:"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)

      #user define exception by raise keyword
# bank_bal=500
# if bank_bal<2000:
#      raise Exception("your account balance is below a accesing limit")
# else:
#     print("your amount has withdrawal")
