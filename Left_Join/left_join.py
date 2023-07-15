def left_join(hashmap1, hashmap2):
    result = set()
    for key in hashmap1:
        if key in hashmap2:
            result.add((key, hashmap1[key], hashmap2[key]))
        else:
            result.add((key, hashmap1[key], None))
    
    return result
hashmap1 = {
    'happy': 'joyful',
    'sad': 'unhappy',
    'big': 'large',
    'small': 'tiny'
}

hashmap2 = {
    'happy': 'sad',
    'big': 'small',
    'small': 'big',
    'fast': 'slow'
}
print(left_join(hashmap1,hashmap2))