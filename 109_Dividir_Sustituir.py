import re
result1 = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
result2 = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
result3 = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]",
                 "Received an email for go_nuts95@my.example.com")
result4 = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

print(result1)
print(result2)
print(result3)
print(result4)
