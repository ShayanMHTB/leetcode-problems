'''
    Given a string, find the length of the longest substring without repeating characters.

    Example:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
'''


def lengthOfLongestSubstring(s: str) -> int:
    result = ""
    substring = ""
    for i in range(len(s) - 1):
        substring += s[i]
        for j in range(i + 1, len(s)):
            if (s[j] not in substring):
                substring += s[j]
                if len(substring) > len(result):
                    result = substring
            else:
                substring = ""
                break
    if (len(result) == 0):
        return 1
    else:
        return len(result)


def main():
    print(
        lengthOfLongestSubstring("pwwkew")
    )
    return 0


if __name__ == '__main__':
    main()
