import google.protobuf.json_format as json_format

import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enumerations_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.maps_pb2 as maps_pb2
import proto.addressbook_pb2 as addressbook_pb2


def simple():
    return simple_pb2.Simple(
        id = 42,
        is_simple = True,
        name = "Beto",
        simple_list = [1, 2, 3]
    )


def complex():
    message = complex_pb2.Complex()
    message.one_dummy.id = 42
    message.one_dummy.name = "Loki"

    message.multiple_dummies.add(id=43, name="Jira")
    message.multiple_dummies.add(id=44, name="Jenny")
    message.multiple_dummies.add(id=45, name="Axel")

    return message


def enums():
    return enumerations_pb2.Enumeration(
        color = enumerations_pb2.EYE_COLOR_GREEN
        # color = 3  # Using ordinal number (the tag number in .proto file) Is not explicit
    )


def oneofs():
    message  = oneofs_pb2.Result(message="a message")
    print(message)

    message.id = 42
    print(message)


def maps():
    message = maps_pb2.MapExample()
    message.ids["myid"].id = 42
    message.ids["myid2"].id = 43
    message.ids["myid3"].id = 44

    print(message)


def file(message):
    path = "simple.bin"

    print("Write to a file")
    print(message)
    with open(path, "wb") as f:
        bytes_as_str = message.SerializeToString()
        f.write(bytes_as_str)

    print("Read from file")
    with open(path, "rb") as f:
        t = type(message)
        message2 = t().FromString(f.read())
    print(message2)


def to_json(message):
    return json_format.MessageToJson(message=message, indent=3, preserving_proto_field_name=True)


def from_json(json_str, type):
    return json_format.Parse(text=json_str, message=type(), ignore_unknown_fields=True)


def fill_addressbook():
    addressbook = addressbook_pb2.AddressBook()

    person1 = addressbook.people.add()
    person1.id=1
    person1.name="Beto" 
    person1.email="beto@proto.com"
    person1.phones.add(number="9921614", type=addressbook_pb2.Person.PhoneType.WORK)
    person1.phones.add(number="8722298", type = addressbook_pb2.Person.PhoneType.HOME)


    person2 = addressbook.people.add()
    person2.id=2
    person2.name="Loki" 
    person2.email="loki@proto.com"
    person2.phones.add(number="2020", type = addressbook_pb2.Person.PhoneType.MOBILE)
    person2.phones.add(number="3030", type = addressbook_pb2.Person.PhoneType.HOME)

    return addressbook


if __name__ == "__main__":
    # print("Simple message:")
    # print(simple())
    # print('Complex message:')
    # print(complex())
    # print("Enums:")
    # print(enums())
    # print("OneOfs:")
    # oneofs()
    # print("Maps:")
    # maps()
    # file(simple())

    # json_str = to_json(complex())
    # print(json_str)

    # print(from_json(json_str, complex_pb2.Complex))
    
    # print("Testing the unknow fields are ignored: ")
    # print(from_json('{"id": 42, "unknown": "test"}', simple_pb2.Simple))

    # AddressBook Exercise
    print(fill_addressbook())

    print(to_json(fill_addressbook()))
