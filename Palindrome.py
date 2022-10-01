new_val=int(input())
new_reverse = int(str(new_val)[::-1])

if new_val == new_reverse:
  print("True")
else:
  print("False")