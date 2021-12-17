from Crypto.Cipher import AES

# 16의 배수가 아니라면 '['로 채우기
def pad(entry):
    padded = entry+(16-len(entry)%16)*'['
    return padded
plain_text = 'Bail is paradise'
