def reverse(self, x:int) -> int:
    res = int(str(abs(x))[::-1]) * (-1 if x<0 else 1)
    return res if -2 (31) <= res <= 2 (31) - 1 else 0
'''
    Here the Negative max range is -2 (31), and Positive Max range is 2 (31).
    Making sure that the integer values are 32 bit
'''
