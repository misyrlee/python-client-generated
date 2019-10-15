from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import uuid
# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient())
db = swagger_client.Db(name='ObjectHierarchy')
with open('/Users/mmisyrlis/Documents/payload.json', 'r') as payload_file:
    payload_file_json = payload_file.read()
json_payload = swagger_client.Payload(json_string=payload_file_json)
# node = swagger_client.Node(key="{'c1': 'P1', 'c2': 'appadmin', 'c3': 'providers', 'c4':'products'}", metadata="asdf",
#                          hrc_rul='hr')

try:
    api_response = api_instance.create_db_request(db=db)
    pprint(api_response)
    response = api_instance.parse_payload(json_payload=json_payload)
    pprint(response.json_string)
    # node = api_instance.get_node_by_key(key='/root/provideradmin/apps/*')
    # pprint(node.key)
    node = api_instance.get_node_by_key(key='/root/superadmin/helptexts/suboptimal')
    node = api_instance.get_node_by_key(key=str(uuid.UUID('d7420cd8-938c-11e9-8578-0242ac11000f')))
    node.metadata = 'metastr'
    api_response = api_instance.create_node_by_key(node=node)
    query_results_list = api_instance.get_descendants(key="/root/provideradmin")
    for node in query_results_list:
        print(node['key'])
except ApiException as e:
    print("Exception when calling DefaultApi->create_db_request: %s\n" % e)
