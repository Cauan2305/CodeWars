class IPv4Address:
    def __init__(self, parts):
        """
        Creates an object representing an IPv4 address

        :param parts: a list of 4 integers
        """
        self._parts = parts

    def __verify_lenght_ipv4(self):
        if len(self._parts) > 4:
            raise ValueError("Should not create IPv4Address with more than 4 parts")
        elif len(self._parts) < 4:
            raise ValueError("Should not create IPv4Address with less than 4 parts")

    def __verify_value_ipv4(self):
        invalid_caracter = list(i for i in self._parts if type(i) != int)
        if invalid_caracter:
            raise ValueError("Should not create IPv4Address with non-integer parts")

    def __verify_range_ipv4(self):
        invalid_caracter = list(i for i in self._parts if i > 255)
        if invalid_caracter:
            raise ValueError(
                "Should not create IPv4Address with parts outside 0-255 range"
            )

        if self._parts[0] == 0:
            raise ValueError("Should not create IPv4Address where first part is 0")

    def __format_ipv4(self) -> str:
        return ".".join(str(i) for i in self._parts)

    @staticmethod
    def from_string(parts:str) -> str:
        return parts

    def start_process(self):
        self.__verify_lenght_ipv4()
        self.__verify_value_ipv4()
        self.__verify_range_ipv4()
        self.__verify_range_ipv4()
        return "Should create IPv4Address when 4 valid integers provided"

    def __repr__(self) -> str:
        return self.start_process()


