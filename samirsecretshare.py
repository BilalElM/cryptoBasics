from cryptography.fernet import Fernet
from secretsharing import SecretSharer
import requests
import binascii


key = Fernet.generate_key()
cipher_suite = Fernet(key)
sentence = "Geheime zin"
cipher_text = cipher_suite.encrypt(sentence.encode())


key_hex = binascii.hexlify(key).decode('utf-8')


shares = SecretSharer.split_secret(key_hex, 2, 3)


paste_data = {
    "sections": [
        {
            "name": "Ciphertext and First Share",
            "syntax": "text",
            "contents": f"Ciphertext: {cipher_text.decode()}\nFirst share: {shares[0]}"
        }
    ]
}
response = requests.post("https://api.paste.ee/v1/pastes",
                         json=paste_data, headers={"X-Auth-Token": "geen secret te vinden hier"})


if response.status_code == 201:
    paste_url = response.json().get("link").replace("\\/", "/")
    print(f"Link naar paste.ee: {paste_url}")
else:
    print("Failed to upload to paste.ee, status code:", response.status_code)


print("\n--- Rapportage ---")
print(f"Shamir-sleutel share (deel 2) voor het verslag: {shares[1]}")
