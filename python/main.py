import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2


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

if __name__ == "__main__":
    print("Simple message:")
    print(simple())
    print('Complex message:')
    print(complex())