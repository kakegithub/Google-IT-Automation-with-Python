import re


def secure_website_domain(website):
    pattern = r"^https://www\.(\w+)\.co(m)?$"  # matches https://www.<domain>.co or .com
    result = re.search(pattern, website)  # use re.search to find the pattern
    if result is None:
        return ""
    return result.group(1)  # return the captured domain part


print(secure_website_domain("http://www.text.com"))  # Should return nothing
print(secure_website_domain("https://www.text.com"))  # Should return text
print(secure_website_domain("http://www.text.co"))  # Should return nothing
print(secure_website_domain("https://www.text.co"))  # Should return text
