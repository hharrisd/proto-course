# Commands to decode and encode messages using the Protobuf compiler

## Decode raw 
Reads raw content from the standar input and retrieves the decoded message:

```shell
cat simple.bin | protoc --decode_raw
```

## Decode
Reads content from standar input but use a message definition and returns the content more readable

```shell
cat simple.bin | protoc --decode=Simple simple.proto
```

If there is a package, it must be provided.

## Encode
Reads a text content and generates the correspondent binary content

```shell
cat simple.txt | protoc --encode=Simple simple.proto > simple.pb
```

The command diff could be used to check the difference between files
```shell
diff simple.bin simple.pb
```
