#!/usr/bin/env python3
"""Z-algorithm — linear time string matching."""
import sys

def z_function(s):
    n = len(s); z = [0] * n; z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r: z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        if i + z[i] > r: l = i; r = i + z[i]
    return z

def z_search(text, pattern):
    combined = pattern + "$" + text
    z = z_function(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        pattern, text = sys.argv[1], sys.argv[2]
    else:
        text = "abcxabcdabxabcdabcdabcy"
        pattern = "abcdabcy"
    positions = z_search(text, pattern)
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at positions: {positions}")
    z = z_function(pattern)
    print(f"Z-array of pattern: {z}")
