import jsonschema
import json


class Helpers():

    def evaluate_schema(self, json_object, schema):
        with open(schema, 'r') as f:
            schema_data = f.read()
        schema = json.loads(schema_data)
        jsonschema.validate(json_object, schema)
