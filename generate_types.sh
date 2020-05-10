python3 -m sgqlc.introspection --exclude-deprecated http://genetics-api.opentargets.io/graphql schema.json
sgqlc-codegen schema.json graphql_types.py
