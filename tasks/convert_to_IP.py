def int32_to_ip(int32: int) -> str:
    """Перевод целого числа в формат IPv4"""
    octet1 = str(int32 // 16777216)
    octet2 = str(int(int32 / 65536) % 256)
    octet3 = str(int(int32 / 256) % 256)
    octet4 = str(int32 % 256)
    return f"{octet1}.{octet2}.{octet3}.{octet4}"


if __name__ == '__main__':
    int32_to_ip()
