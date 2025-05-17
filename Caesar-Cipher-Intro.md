# Cryptography Fundamentals
1. **_Encryption_** => Process of transforming plain text (readable data) into ciphertext (unreadable data) using an algorithm and a secret key. Makes the informating unintelligible to anyone with the key.
2. **_Decryption_** => Uses the same algorithm and the decryption key to convert cipher text back to its original plain text form.
3. **_Plaintext_** => Original message or data in its readable form before encryption.
4. **_Ciphertext_** => Scrambled and unreadable form of the message after encryption. Appears like gibberish to anyone without the decryption key
5. **_Keys_** => Act like passwords that control how data is transformed.
6. **_Symmetric Key_** => A single key is used for both encryption and decryption. Both sender and receiver need to share this secret key securely
7. **_Asymmetric Key_** => Involves a pair of mathematically linked keys i.e. Public and Private Key. Public key is widely distirbuted for encryption, while the private key is kept secret and used for decryption.
8. **_Ciphers_** => Algorithms that define the specific rules for how plaintext is transformed into cipher text and vice verse
9. **_Substitution Ciphers_** => Ciphers replace letters or groups of letters in the plaintext with different letters or symbols according to a set rule
10. **_Transposition Ciphers_** => Rearranges the order of the letters in the plaintext without changing the letters themselves.
11. **_Modern Ciphers_** => More complex algorithms that often comvine elements of substitution and transposition, and use mathematical operations to achieve much strongs encryption.

# Caesar Cipher Algorithm
## Encryption
1. Take plaintext message (string) and shift value (integer between 1 and 25) as input
2. For every character in the plaintext, check if the character is an alphabet.
3. Convert the character to its numerical position in the alphabet
4. Add the shift value to the numerical position
5. Apply the modulo operation with 26 to ensure the result stays within the alphabetical range. Accounts for wrapping around the alphabet.
6. Convert the resulting number back to its corresponding character.
7. Output the encrypted ciphertext message

## Decryption
1. Take cipher text message (string) and shift value (key for encryption) as input
2. For every character in the plaintext, check if the character is an alphabet.
3. Convert the character to its numerical position in the alphabet.
4. Subtract the shift value from the numerical position
5. Apply the modulo operation with 26 to ensure the result stays within the alphabetical range
6. Conver the resulting number back to its corresponding character
7. Output the decrypted plaintext message

# Caesar Cipher
- It's a type of substitution cipher, which means it scrambles messages by replacing letters with different ones according to a fixed rule.
- Each letter in the message is shifted by a certain number of positions down the alphabet. It also wraps around the alphabet.
- For example; 'X' is shifted by 3 to become 'A'

## Advantages/Benefits of Caesar Cipher
- **_Easy to implement and use_** => Caesar Cipher uses basic math operations and requires minimal knowledge to understand.
- **_Low resource Requirements_** => Algorithm's efficiency and minimal computing power requirements make it suitable for low-tech environments or situations with limited resources
- **_Simple Key Management_** => Uses only a single short key i.e. Shift Value making it easy to remember and share among trusted individuals
- **_Physical Implementation_** => Can be implemented with physical tools like rotating discs or cards
- **_Foundation for More Complex Ciphers_** => More secure variations of the algorithm can be created by combining multiple Caesar Ciphers with different shift values or using keywords.

## Disadvantages/Drawbacks of Caesar Cipher
- **_Weak Security_** => With only 26 possible shift values, a brute-force attack can easily crack the code by trying all possibel shifts until a decipherable message is found.
- **_Limited Keyspace_** => Total number of possible keys isvery limited, making it significantly easier to creack compared to ciphers with much larger keyspaces
- **_Susceptible to Frequency Analysis_** => Statistical analysis of the encrypted text can reveal patterns in letter frequencies, which can be used to identify the shift value and decrypt the message
- **_Not suitable for modern security_** => Unsuitable for protecting sensitive information in today's world with more sophisticated encryption algorithms offering stronger security.
