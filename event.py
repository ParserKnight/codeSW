
import re

class Event():

    def __init__(self,
     timestamp:int, 
     response_header_bytes:float, 
     client_ip:str,
     http_response_code:str,
     response_size_bytes:float,
     http_method:str,
     url:str,
     username:str,
     type_of_access_and_destination_ip:str,
     response_type:str):

        self.timestamp = timestamp
        self.response_header_bytes = response_header_bytes
        self.client_ip = client_ip
        self.http_response_code = http_response_code
        self.response_size_bytes = response_size_bytes
        self.http_method = http_method
        self.url = url 
        self.username = username
        self.type_of_access = type_of_access_and_destination_ip
        self.destination_ip = type_of_access_and_destination_ip
        self.response_type = response_type
        
    @property
    def timestamp(self):
        return self._timestamp

    @property
    def response_header_bytes(self):
        return self._response_header_bytes

    @property
    def client_ip(self):
        return self._client_ip

    @property
    def http_response_code(self):
        return self._http_response_code

    @property
    def response_size_bytes(self):
        return self._response_size_bytes

    @property
    def http_method(self):
        return self._http_method

    @property
    def url(self):
        return self._url

    @property
    def username(self):
        return self._username

    @property
    def type_of_access(self):
        return self._type_of_access

    @property
    def destination_ip(self):
        return self._destination_ip

    @property
    def response_type(self):
        return self._response_type

    @timestamp.setter
    def timestamp(self,value):
        try:
            self._timestamp=float(value)
        except ValueError:
            raise ValueError("Timestamp must be float")

        self._timestamp

    @response_header_bytes.setter
    def response_header_bytes(self,value):
        try:
            self._response_header_bytes=float(value)
        except ValueError:
            raise ValueError("Response header bytes must be float")
        self._response_header_bytes

    @client_ip.setter
    def client_ip(self,value):

        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",value):
            raise ValueError("client_ip must be an ip")
        self._client_ip=value

    @http_response_code.setter
    def http_response_code(self,value):
        try:
            value=next(iter(value.split("/")[-1:]))
        except AttributeError:
            raise AttributeError("Not valid hrrp response code XXXX/XXX")
        if value not in [
            "100", "101", "102", "103", "200", "201", "202", "203", "204", "205", "206", "207", "208",
	        "226", "300", "301", "302", "303", "304", "305", "307", "308", "400", "401", "402", "403", 
            "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", 
            "417", "418", "421", "422", "423", "424", "425", "426", "428", "429", "431", "451", "500", 
            "501", "502", "503", "504", "505", "506", "507", "508", "510", "511"
            ]:
            raise ValueError("Value need to be a valid HTTP response code")
        self._http_response_code = value

    @response_size_bytes.setter
    def response_size_bytes(self,value):
        try:
            self._response_size_bytes=float(value)
        except ValueError:
            raise ValueError("Response Size_Bytes  must be float")
        
    @http_method.setter
    def http_method(self,value):
        if value not in ["POST", "GET", "PUT", "PATCH", "DELETE","CONNECT"]:
            raise ValueError("Method need to be valid")
        self._http_method = value

    @url.setter
    def url(self,value):
        if not isinstance(value,str):
            raise ValueError("Url must be a URL")
        self._url=value

    @username.setter
    def username(self,value):
        if not isinstance(value,str):
            raise ValueError("username must be str")
        self._username=value

    @type_of_access.setter
    def type_of_access(self,value):
        try:
            value=next(iter(value.split("/")[:-1]))
        except AttributeError:
            raise AttributeError("Not valid type_of_access value, Example: DIRECT/68.142.231.252")
        if not isinstance(value,str):
            raise ValueError("type_of_access must be str")
        self._type_of_access=value

    @destination_ip.setter
    def destination_ip(self,value):
        try:
            value=next(iter(value.split("/")[-1:]))
        except AttributeError:
            raise AttributeError("Not valid destination_ip value, Example: DIRECT/68.142.231.252")
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",value) and not "-":
            raise ValueError("destination_ip must be an ip")
        self._destination_ip = value

    @response_type.setter
    def response_type(self,value):
        self._response_type=value