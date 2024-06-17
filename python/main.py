import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enumerations_pb2
import proto.oneofs_pb2 as oneofs_pb2


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


if __name__ == "__main__":
    print("Simple message:")
    print(simple())
    print('Complex message:')
    print(complex())
    print("Enums:")
    print(enums())
    print("OneOfs:")
    oneofs()
