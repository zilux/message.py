#!/usr/bin/env python
""" just to know OO """

import json
import sys


class SeverityError(Exception):
    """ Own Exception """


class Message:
    """ example class """

    __number_of_messages_send = 0
    __number_of_created_objects = 0
    __number_of_active_objects = 0

    def __init__(self, severity=None, payload=None):
        self.severity = severity
        self.payload = payload
        # type(self) = Message = __class__
        type(self).__number_of_created_objects += 1

    def __del__(self):
        __class__.__number_of_active_objects -= 1

    def __repr__(self):
        return f"Message('{self.__severity}','{self.__payload}')"

    def __str__(self):
        return f"message --> {self.__severity}: '{self.__payload}'"

    @property
    def severity(self):
        """ return severity """
        return self.__severity

    @property
    def payload(self):
        """ return payload """
        return self.__payload

    @severity.setter
    def severity(self, severity):
        """ check on valid severity """

        if not severity:
            severity = "info"

        sev = ["info", "normal", "warning", "error", "fatal"]

        if severity in sev:
            self.__severity = severity
        else:
            raise SeverityError(f'"{severity}" not allowed as severity')

    @payload.setter
    def payload(self, payload):
        """ return payload """
        self.__payload = payload

    def send(self):
        """ send a messages """

        to_send = {"message": {self.__severity: self.__payload}}

        jdump = json.dumps(to_send, indent=4)
        type(self).__number_of_messages_send += 1
        print(jdump)

    @classmethod
    def message_send(cls):
        """ return #messages send """
        return cls.__number_of_messages_send

    @classmethod
    def created_objects(cls):
        """ return #objects created """
        return cls.__number_of_created_objects

    @classmethod
    def active_objects(cls):
        """ return created objects """
        return cls.__number_of_active_objects


def main():
    """ some testing on Message class """

    mes1 = Message(payload="just testing", severity="normal")
    mes1.severity = "warning"
    mes1.send()

    mes2 = Message()
    mes2.severity = "info"
    mes2.payload = "just another mes"
    mes2.send()

    print("------------------")
    print(mes1)
    print(repr(mes1))
    print("------------------")
    del mes1
    del mes2

    print(f"number of messages send: {Message.message_send()}")
    print(f"number of created objects: {Message.created_objects()}")
    print(f"number of active objects: {Message.active_objects()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
