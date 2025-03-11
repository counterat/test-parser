def convert_strings_into_dicts(cookie_string):
    cookies_dict = dict(item.split("=", 1) for item in cookie_string.split("; "))
    return cookies_dict

def get_post_with_link(posts:list, link:str):
    for post in posts:
        if post.get("link") == link:
            return post
    return False

def scroll_until_element_is_fully_visible(actions, element):
    actions.move_to_element(element).click().perform()
