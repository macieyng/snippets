from jsf import JSF


def generate_fakes_from_json_schema(schema):
    """Generate fake data from a JSON schema defined as a dictionary"""
    faker = JSF(schema=schema)
    return faker.generate()


def generate_fakes_from_json_schema_file(file_path):
    """Generate fake data from a JSON schema file"""
    faker = JSF.from_json(file_path)
    return faker.generate()


def test_generate_fakes_from_json_schema():
    fake_data = generate_fakes_from_json_schema(
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "age": {"type": "integer"},
                "email": {"type": "string", "format": "email"},
            },
            "required": ["email", "age", "id"],
        }
    )

    assert fake_data["age"] is not None and isinstance(fake_data["age"], int)
    assert fake_data["email"] is not None and isinstance(fake_data["email"], str)
    assert fake_data["id"] is not None and isinstance(fake_data["id"], str)
