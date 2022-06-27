from tasks import convert_to_IP


assert convert_to_IP.int32_to_ip(2154959208) == "128.114.17.104"
assert convert_to_IP.int32_to_ip(0) == "0.0.0.0"
assert convert_to_IP.int32_to_ip(2149583361) == "128.32.10.1"
