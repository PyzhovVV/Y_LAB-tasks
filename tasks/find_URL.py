def domain_name(url: str) -> str:
    """Нахождение домена из URL адреса"""
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    url = url.split('.')[0]
    return url


if __name__ == '__main__':
    domain_name()
