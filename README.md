# Snippets Repo

Welcome! This is maintained snippets repo. 

I want to use this space to share with you code examples that was my `Eureka!` moments.

I hope that some of you will find it usefull, entertaining or teachable.

## Contents

### FastAPI

1. [Custom Error Handling](fastapi/001_custom_error_handling.py)
   
   This code defines a main FastAPI application and a sub-application, each with its own endpoint and exception handler for RequestValidationError. The main app's exception handler returns a 422 status code with a custom error message, while the sub-app's handler returns a 400 status code with a different error message. Two test functions using TestClient verify the exception handling behavior by making POST requests with invalid JSON data and checking the response status codes and messages.

2. [External API Call Mock](fastapi/002_external_api_call_mock.py)
   
   This code sets up a FastAPI application with a single endpoint `/call` that sends a `POST` request to an external API using `httpx.AsyncClient` and returns the response in a specific format. The endpoint constructs a payload using Pydantic's Payload model, sends the payload to `"http://external-api.com"`, receives a response, and returns the formatted result using another Pydantic model Result. A test function uses respx to mock the external API's response and `httpx.ASGITransport` to test the `/call` endpoint, asserting that the response matches the expected output.

3. [URL in Endpoint Path](fastapi/003_url_in_endpoint_path.py)
   
   This code defines two FastAPI endpoints: `/path/{external_path:path}/end` and `/string/{external_path}/end`. Both endpoints accept a path parameter `external_path`, but the former uses a path operation decorator with a type declaration (`path`) while the latter doesn't. The test function `test_get` utilizes `pytest.mark.parametrize` to test both endpoints with various paths, asserting their respective status codes.


### Testing

1. [Generate Fakes from JSON Schema](testing/001_generate_fakes_from_json_schema.py)
   
   This Python code utilizes the JSF library to generate fake data from JSON schemas. The `generate_fakes_from_json_schema` function accepts a JSON schema as a dictionary and returns fake data generated based on that schema. The `test_generate_fakes_from_json_schema` function tests this functionality by asserting that the generated fake data matches the schema's structure and data types. Additionally, there's a similar function `generate_fakes_from_json_schema_file` which generates fake data from a JSON schema file path.

2. [Test With JSON Schema Repository](testing/002_test_with_json_schema_repository.py)
   
   This Python script utilizes `httpx` to fetch a JSON schema from a given URL and then uses the JSF library to generate fake data based on that schema. The `fetch_json_schema` function fetches the schema from the provided URL, while the `generate_fakes` function generates fake data using the fetched schema. The script then prints the generated fake data.


### Logging

1. [Useful logger configuration for debugging](logging/001_utility_func_logging_points_to_caller.py)
   🐍 As Python developers, effective logging is key to debugging and maintaining clean code. Recently, I experimented with Python’s logging module and found a few interesting insights that can significantly improve how we track down issues. Take a look at the code snippet.

   🔑 Key takeaways:

   1️⃣ Where the logger is called matters! In utility_function_1, the logger points to the function itself, whereas in utility_function_2 (with stacklevel=2), it points to where the function is called—offering more insightful debugging information.

   2️⃣ Highlighting Key Warnings. The ZeroDivisionError warning helps us catch logic errors early, making logging essential for stability in production environments.

   3️⃣ Log Formatter. Using detailed formatting like %(pathname)s, %(lineno)s, and %(funcName)s ensures we get the full context of any issue, improving traceability.