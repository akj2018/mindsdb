# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mindsdb.grpc.db.common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x64\x62.proto\x1a\x0c\x63ommon.proto\"O\n\x0eHandlerContext\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\t\x12\x14\n\x0chandler_type\x18\x02 \x01(\t\x12\x16\n\x0ehandler_params\x18\x03 \x01(\t\"E\n\x12NativeQueryContext\x12 \n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x0f.HandlerContext\x12\r\n\x05query\x18\x02 \x01(\t\"E\n\x12\x42inaryQueryContext\x12 \n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x0f.HandlerContext\x12\r\n\x05query\x18\x02 \x01(\x0c\"A\n\x0e\x43olumnsContext\x12 \n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x0f.HandlerContext\x12\r\n\x05table\x18\x02 \x01(\t2\xdc\x02\n\tDBService\x12-\n\x07\x43onnect\x12\x0f.HandlerContext\x1a\x0f.StatusResponse\"\x00\x12\x35\n\x0f\x43heckConnection\x12\x0f.HandlerContext\x1a\x0f.StatusResponse\"\x00\x12\x30\n\nDisconnect\x12\x0f.HandlerContext\x1a\x0f.StatusResponse\"\x00\x12/\n\x0bNativeQuery\x12\x13.NativeQueryContext\x1a\t.Response\"\x00\x12/\n\x0b\x42inaryQuery\x12\x13.BinaryQueryContext\x1a\t.Response\"\x00\x12)\n\tGetTables\x12\x0f.HandlerContext\x1a\t.Response\"\x00\x12*\n\nGetColumns\x12\x0f.ColumnsContext\x1a\t.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'db_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HANDLERCONTEXT._serialized_start=26
  _HANDLERCONTEXT._serialized_end=105
  _NATIVEQUERYCONTEXT._serialized_start=107
  _NATIVEQUERYCONTEXT._serialized_end=176
  _BINARYQUERYCONTEXT._serialized_start=178
  _BINARYQUERYCONTEXT._serialized_end=247
  _COLUMNSCONTEXT._serialized_start=249
  _COLUMNSCONTEXT._serialized_end=314
  _DBSERVICE._serialized_start=317
  _DBSERVICE._serialized_end=665
# @@protoc_insertion_point(module_scope)