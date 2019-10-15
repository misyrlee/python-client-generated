# swagger_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/misyrlee/hrc-server/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_db_request**](DefaultApi.md#create_db_request) | **POST** /db | 
[**create_edge_by_keys**](DefaultApi.md#create_edge_by_keys) | **POST** /db/root/edge | 
[**create_node_by_key**](DefaultApi.md#create_node_by_key) | **POST** /db/root/node | 
[**delete_edge_by_keys**](DefaultApi.md#delete_edge_by_keys) | **DELETE** /db/root/edge | 
[**delete_node_by_key**](DefaultApi.md#delete_node_by_key) | **DELETE** /db/root/node | 
[**get_descendants**](DefaultApi.md#get_descendants) | **GET** /db/root/descendants | 
[**get_node_by_key**](DefaultApi.md#get_node_by_key) | **GET** /db/root/node | 
[**parse_payload**](DefaultApi.md#parse_payload) | **POST** /db/root/payload | 
[**patch_node_by_key**](DefaultApi.md#patch_node_by_key) | **PATCH** /db/root/node | 
[**put_node_by_key**](DefaultApi.md#put_node_by_key) | **PUT** /db/root/node | 


# **create_db_request**
> InlineResponse200 create_db_request(db=db)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
db = swagger_client.Db() # Db |  (optional)

try:
    api_response = api_instance.create_db_request(db=db)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_db_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | [**Db**](Db.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edge_by_keys**
> Edge create_edge_by_keys(edge=edge)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
edge = swagger_client.Edge() # Edge |  (optional)

try:
    api_response = api_instance.create_edge_by_keys(edge=edge)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_edge_by_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge** | [**Edge**](Edge.md)|  | [optional] 

### Return type

[**Edge**](Edge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_by_key**
> Node create_node_by_key(node=node)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
node = swagger_client.Node() # Node |  (optional)

try:
    api_response = api_instance.create_node_by_key(node=node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_node_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | [**Node**](Node.md)|  | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_edge_by_keys**
> Edge delete_edge_by_keys(edge=edge)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
edge = swagger_client.Edge() # Edge |  (optional)

try:
    api_response = api_instance.delete_edge_by_keys(edge=edge)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_edge_by_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge** | [**Edge**](Edge.md)|  | [optional] 

### Return type

[**Edge**](Edge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_by_key**
> delete_node_by_key(node=node)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
node = swagger_client.Node() # Node |  (optional)

try:
    api_instance.delete_node_by_key(node=node)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_node_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | [**Node**](Node.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_descendants**
> QueryResults get_descendants(key=key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
key = 'key_example' # str |  (optional)

try:
    api_response = api_instance.get_descendants(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_descendants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_by_key**
> Node get_node_by_key(key=key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
key = 'key_example' # str |  (optional)

try:
    api_response = api_instance.get_node_by_key(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_payload**
> Payload parse_payload(json_payload=json_payload)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
json_payload = swagger_client.Payload() # Payload |  (optional)

try:
    api_response = api_instance.parse_payload(json_payload=json_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->parse_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_payload** | [**Payload**](Payload.md)|  | [optional] 

### Return type

[**Payload**](Payload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_node_by_key**
> patch_node_by_key(node=node)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
node = swagger_client.Node() # Node |  (optional)

try:
    api_instance.patch_node_by_key(node=node)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_node_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | [**Node**](Node.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_node_by_key**
> put_node_by_key(node=node)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
node = swagger_client.Node() # Node |  (optional)

try:
    api_instance.put_node_by_key(node=node)
except ApiException as e:
    print("Exception when calling DefaultApi->put_node_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | [**Node**](Node.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

