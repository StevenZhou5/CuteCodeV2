class HashMap(object):
    def __init__(self):
        super(HashMap, self).__init__()

    def max_diff_str(self, str):
        if not str:
            return ""
        hash_map = {}
        max_len = 1
        max_idx = 0
        last_len = 0
        last_idx = 0
        for idx, char in enumerate(str):
            if hash_map.get(char, None) == None:  # 如果没有出现过，加入map，并记录char所在idx
                # print(hash_map.get(char, None))
                hash_map[char] = idx
                last_len += 1
                if last_len > max_len:
                    max_len, max_idx = last_len, last_idx
                continue

            last_char_idx = hash_map[char]
            # print("last_char_idx:", last_char_idx, "last_idx:", last_idx)
            if last_char_idx < last_idx:
                hash_map[char] = idx
                last_len += 1
                if last_len > max_len:
                    max_len, max_idx = last_len, last_idx
                continue

            hash_map[char] = idx
            last_idx = last_char_idx + 1
            # print("last_idx:", last_idx)
            last_len = idx - last_idx + 1
            if last_len > max_len:
                max_len, max_idx = last_len, last_idx
        return str[max_idx:(max_idx + max_len)]



hm = HashMap()
print("res:", hm.max_diff_str("xxdsxex"))
