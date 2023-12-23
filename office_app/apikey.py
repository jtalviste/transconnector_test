import os


API_KEY_PROP_NAME = "TEST_CONNECTOR_API_KEY"

def getAccessApiKey():
    return os.environ[API_KEY_PROP_NAME]