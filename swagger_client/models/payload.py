# coding: utf-8

"""
    HRC API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Payload(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'json_string': 'str'
    }

    attribute_map = {
        'json_string': 'json_string'
    }

    def __init__(self, json_string=None):  # noqa: E501
        """Payload - a model defined in Swagger"""  # noqa: E501

        self._json_string = None
        self.discriminator = None

        self.json_string = json_string

    @property
    def json_string(self):
        """Gets the json_string of this Payload.  # noqa: E501


        :return: The json_string of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._json_string

    @json_string.setter
    def json_string(self, json_string):
        """Sets the json_string of this Payload.


        :param json_string: The json_string of this Payload.  # noqa: E501
        :type: str
        """
        if json_string is None:
            raise ValueError("Invalid value for `json_string`, must not be `None`")  # noqa: E501

        self._json_string = json_string

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Payload, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Payload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
