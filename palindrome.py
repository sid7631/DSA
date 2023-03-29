""" Module providing function for palindrome"""
def is_palindrome(arr):
    """ Returns True if array or string is palindrome else False"""
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True
