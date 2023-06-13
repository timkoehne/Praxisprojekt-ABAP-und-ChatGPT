import json
import pyrfc

with open("saplogonLoginDetails.json", "r") as file:
    connection_params = json.loads(file.read())


with pyrfc.Connection(**connection_params) as conn:
    # conn.ping()
    result = conn.call('STFC_CONNECTION', REQUTEXT=u'Hello SAP!')
    print(result)