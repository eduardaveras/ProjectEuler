def isPalindrome(x):
  if str (x) == str (x)[::-1]:
    return True
  else:
    return False

def largestPalindrome(n):
  maxNum = 10**n - 1
  minNum = 10**(n-1)
  vec = []

  for i in range(minNum, maxNum):
    for j in range (minNum, maxNum):
      num = i * j
      if isPalindrome(num):
        vec.append(num)


  return max(vec)


print(largestPalindrome(3))

  
  
