# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maps.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmaps.proto\x12\x0c\x65xample.maps\"\x16\n\x08IdWraper\x12\n\n\x02id\x18\x01 \x01(\r\"\x80\x01\n\nMapExample\x12.\n\x03ids\x18\x01 \x03(\x0b\x32!.example.maps.MapExample.IdsEntry\x1a\x42\n\x08IdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.example.maps.IdWraper:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'maps_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPEXAMPLE_IDSENTRY._options = None
  _MAPEXAMPLE_IDSENTRY._serialized_options = b'8\001'
  _IDWRAPER._serialized_start=28
  _IDWRAPER._serialized_end=50
  _MAPEXAMPLE._serialized_start=53
  _MAPEXAMPLE._serialized_end=181
  _MAPEXAMPLE_IDSENTRY._serialized_start=115
  _MAPEXAMPLE_IDSENTRY._serialized_end=181
# @@protoc_insertion_point(module_scope)
