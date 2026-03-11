#!/usr/bin/env python3
"""Z-algorithm — linear-time string matching via Z-array.

One file. Zero deps. Does one thing well.

Z[i] = length of the longest substring starting at i that matches a prefix of s.
Pattern matching: concatenate pattern + "$" + text, find Z[i] == len(pattern).
"""
import sys

def z_array(s):
    n = len(s)
    if n == 0: return []
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

def z_search(text, pattern):
    concat = pattern + "$" + text
    z = z_array(concat)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(concat)) if z[i] == m]

def main():
    text = "abcabcabcabc"
    pattern = "abcabc"
    print(f"Text:    '{text}'")
    print(f"Pattern: '{pattern}'")
    matches = z_search(text, pattern)
    print(f"Matches at: {matches}")
    z = z_array(text)
    print(f"\nZ-array of '{text}':")
    print(f"  {z}")
    # Distinct substrings via Z
    s = "aabaa"
    z2 = z_array(s)
    distinct = sum(len(s) - i - z2[i] for i in range(len(s)))
    # +1 for empty? No, just count non-empty
    # Actually: n*(n+1)/2 - sum(z[i]) for i>0... simplified:
    print(f"\nZ-array of '{s}': {z2}")

if __name__ == "__main__":
    main()
