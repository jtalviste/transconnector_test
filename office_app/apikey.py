import os
import hashlib
import base64

API_KEY_ENV_PROP_NAME = "TRANS_CONNECTOR_API_KEY_HASH"

if os.getenv(API_KEY_ENV_PROP_NAME) is None:
    os.environ[API_KEY_ENV_PROP_NAME] = "O6GFX73m4tIviuv8YtYcJwGy6awVSsb2QxG7iLjSfU8="

def printApiKeyInstructions(apiKey):
    print("Env var should be set "+API_KEY_ENV_PROP_NAME+"="+getApiKeyHash(apiKey))

def checkAccessApiKey(apiKey):
    return os.getenv(API_KEY_ENV_PROP_NAME) == getApiKeyHash(apiKey)

def getApiKeyHash(apiKey):
    if apiKey is None:
        return None
    salt = 'transconnectorapikeyGHS'
    return str(base64.b64encode(sha3_with_salt(apiKey, salt)).decode());

def sha3_with_salt(string, salt):
    # Convert strings to bytes
    string_bytes = string.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Create a SHA3 hash object
    sha3_digester = hashlib.sha3_256()

    # Combine the string and salt
    hashed_data = sha3_digester.update(string_bytes)
    hashed_data = sha3_digester.update(salt_bytes)

    # Get the SHA3 hash value
    sha3_hash = sha3_digester.digest()

    return sha3_hash

def main(apiKey):
    printApiKeyInstructions(apiKey)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])