from tasks import find_bananas


assert find_bananas.bananas("banann") == set()
assert find_bananas.bananas("banana") == {"banana"}
assert find_bananas.bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert find_bananas.bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert find_bananas.bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
