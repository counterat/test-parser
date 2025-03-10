def convert_strings_into_dicts(cookie_string):
    cookies_dict = dict(item.split("=", 1) for item in cookie_string.split("; "))
    return cookies_dict

