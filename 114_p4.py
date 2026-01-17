import re


def convert_phone_number(phone):
    # Convert US phone numbers from XXX-XXX-XXXX to (XXX) XXX-XXXX
    result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
    return result


# My number is (212) 345-9999.
print(convert_phone_number("My number is 212-345-9999."))
# Please call (888) 555-1234
print(convert_phone_number("Please call 888-555-1234"))
print(convert_phone_number("123-123-12345"))  # 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))
