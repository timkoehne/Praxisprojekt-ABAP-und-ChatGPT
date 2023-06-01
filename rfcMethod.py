import json
import pyrfc

with open("saplogonLoginDetails.txt", "r") as file:
    loginDetails = json.loads(file.read())

connection_params = {
    'ashost': loginDetails.ashost,
    'sysnr': loginDetails.sysnr,
    'client': loginDetails.client,
    'user': loginDetails.user,
    'passwd': loginDetails.passwd,
    'lang': loginDetails.lang,
}
connection = pyrfc.Connection(**connection_params)

abap_code = """
WRITE: 'Hello, world!'.
"""
result = connection.call("RFC_EXECUTE_PROGRAM", PROGRAM_NAME='Z_MY_ABAP_PROGRAM', PROGRAM_TEXT=abap_code)