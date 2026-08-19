def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    original = x
    reversed_num = 0

    while x > 0:
      reversed_num = reversed_num * 10 + x % 10
      x //= 10

    if reversed_num > 2**31 - 1:
      return False

    return original == reversed_num