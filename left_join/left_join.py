def left_join(hashmap1, hashmap2):
    result = {}
    for key in hashmap1:
        if key in hashmap2:
            result[key] = [hashmap1[key], hashmap2[key]]
        else:
            result[key] = [hashmap1[key], None]
    return result
