import re


def find_isbn(list):
    pattern = r"^(\d{3})-(\d{1})-(\d{2})-(\d{6})-(\d{1})$"  # 3-1-2-6-1 digit groups
    result = re.search(pattern, list)  # use re.search to find a match
    if result is None:
        return ""
    return result.group(4)  # return the 6-digit group


print(find_isbn("123-4-12-098754-0"))  # Should return 098754
print(find_isbn("223094-AB-30"))  # result should be blank
print(find_isbn("1123-4-12-098754-0"))  # result should be blank
