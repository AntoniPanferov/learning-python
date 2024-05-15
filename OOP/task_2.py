class IPAddress:
    def __init__(self, ip_address="0.0.0.0"):
        self.__ip_address = "0.0.0.0" if not self.__check(ip_address) else ip_address

    def __check(self, ip_address):
        if ip_address.count('.') != 3:
            return False

        for x in ip_address.split('.'):
            if int(x) < 0 or int(x) > 255:
                return False

        return True

    @property
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, new_value):
        if self.__check(new_value):
            self.__ip_address = new_value

ip_obj = IPAddress("192.168.0.2")
print(ip_obj.ip_address)

ip_obj.ip_address = "10.0.0.255"
print(ip_obj.ip_address)
