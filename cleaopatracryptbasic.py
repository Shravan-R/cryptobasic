original_message='Hello how are u'
split_each_single_word=list(original_message)
changed_to_crypto=[]
changed_to_crypto1=[]
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


for ch in changed_to_crypto:
    if ch.isalpha():
        base=ord('A') if ch.upper() else ord('a')
        new_char1=chr((ord(ch)-base +shift) % 26 +base)
        changed_to_crypto1.append(new_char1)
    else:
        changed_to_crypto1.append(ch)

encrepted_message=''.join(changed_to_crypto)
encrepted_message1=''.join(changed_to_crypto1)
print(encrepted_message)
print(changed_to_crypto)
print(changed_to_crypto1)
    

