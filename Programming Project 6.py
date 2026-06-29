import re


def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.fullmatch(pattern, phone) is not None


def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.fullmatch(pattern, ssn) is not None


def validate_zip(zip_code):
    pattern = r'^\d{5}$'
    return re.fullmatch(pattern, zip_code) is not None


def main():
    phone = input("Enter a phone number (###-###-####): ")
    ssn = input("Enter a Social Security Number (###-##-####): ")
    zip_code = input("Enter a ZIP Code (#####): ")

    if validate_phone(phone):
        print("Phone Number: Valid")
    else:
        print("Phone Number: Invalid")

    if validate_ssn(ssn):
        print("Social Security Number: Valid")
    else:
        print("Social Security Number: Invalid")

    if validate_zip(zip_code):
        print("ZIP Code: Valid")
    else:
        print("ZIP Code: Invalid")


main()