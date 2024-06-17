import proto.simple_pb2 as simple_pb2


def simple():
    return simple_pb2.Simple(
        id = 42,
        is_simple = True,
        name = "Beto",
        simple_list = [1, 2, 3]
    )


if __name__ == "__main__":
    print(simple())