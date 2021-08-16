python3 -m sgqlc.introspection --exclude-deprecated https://api.genetics.opentargets.org/graphql schema.json
sgqlc-codegen schema.json graphql_types.py
