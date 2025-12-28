print("Welcome to odd/even number validator")
entered_no= int(input("Enter your number to check:\n"))
if entered_no % 2 == 1:
  print(f"Your entered value '{entered_no}' is ODD number")
else:
  print(f"Your entered value '{entered_no}' is EVEN number")