from tasks import find_URL


assert find_URL.domain_name("http://google.com") == "google"
assert find_URL.domain_name("http://google.co.jp") == "google"
assert find_URL.domain_name("www.xakep.ru") == "xakep"
assert find_URL.domain_name("https://youtube.com") == "youtube"
