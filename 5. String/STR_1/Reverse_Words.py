s = "  a good   example  "


def reverseWords(s):
  words = s.split()

  reversed_words = words[::-1]

  return " ".join(reversed_words)


print(reverseWords(s))
