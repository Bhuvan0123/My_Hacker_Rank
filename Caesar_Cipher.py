# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
def caesarCipher(s, k):
    res=""
    for i in s:
        if i.isalpha():
            if i.isupper():
                res+=chr(((ord(i)-65+k)%26)+65)
            else:
                res+=chr(((ord(i)-97+k)%26)+97)
        else:
            res+=i
    return res