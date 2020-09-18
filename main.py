#Author: Nireeha Veeraballi -nzv5126@psu.edu

def digit_sum(a):
  if a==0:
    return 0
  else:
    return int((a%10) + digit_sum(a//10))

def run():
  getInp = int(input("Enter an int: "))
  print(f"sum of digits of {getInp} is {digit_sum (getInp)}.")

if __name__ == "__main__":  
  run()




