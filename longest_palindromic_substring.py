def longestPalindrome( s: str) -> str:
    n, max_len, ans = len(s), 0, ''
    def expand_around_center(l, r):
        if r < n and s[l] != s[r]:
            return '' # Index out of range or elements unequal(for even sized palindromes) thus return empty string
        while l >= 0 and r < n and s[l] == s[r]: # Till the s[l], s[r] elements are in range and same, the palindrome continues to grow
            l, r = l - 1, r + 1
        return s[l + 1:r] # Return the palindrome formed
    for i in range(n):
        a, b = expand_around_center(i, i), expand_around_center(i, i + 1) # (i,i) for odd and (i,i+1) for even sized palindromes
        main = a if len(a) > len(b) else b # Check which one of a, b is larger
        if len(main) > max_len: # Check if palindrome with i as center is larger than previous entries then update if necessary
            max_len, ans = len(main), main
    return ans

if __name__ == '__main__':

    lst = "babad"
    print("longest palindromic is: ",  longestPalindrome(lst))