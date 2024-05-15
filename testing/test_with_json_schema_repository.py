import httpx
from jsf import JSF


def fetch_json_schema(url):
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


def generate_fakes(schema):
    faker = JSF(schema=schema)
    return faker.generate()


# Fetch schema
url = (
    "https://raw.githubusercontent.com/"
    "macieyng/snippets/main/testing/json_schema.json"
)
schema = fetch_json_schema(url)
fake_data = generate_fakes(schema)
print(fake_data)
