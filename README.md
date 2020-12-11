# SBDC_dealership

========== how to run ==========

Inorder to protect this projects secret key one file must be added before running the server.
my_site/secrets.json must created and contain a json object with the key "secret_key" and a string value.

`{ "secret_key": "Random_string_here" }`

Next, `manage.py migrate` should be run.

Finally, the server may be run
