original_message='Hello how are u'
split_each_single_word=list(original_message)
changed_to_crypto=[]
print(original_message)
print(split_each_single_word)

shift=3

for ch in split_each_single_word:
    if ch.isalpha():
        base=ord('A') if ch.upper() else ord('a')
        new_char=chr((ord(ch)-base+shift) % 26 +base)
        changed_to_crypto.append(new_char)
    else:
        changed_to_crypto.append(ch)

encrepted_message=''.join(changed_to_crypto)

print(encrepted_message)
print(changed_to_crypto)
    

