# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x08messages\"\xac\x01\n\x07Request\x12%\n\x05steps\x18\x01 \x03(\x0b\x32\x16.messages.Request.Step\x12\x14\n\x07step_id\x18\x02 \x01(\x05H\x00\x88\x01\x01\x1aX\n\x04Step\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\tparent_id\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x08\x64uration\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\tB\x0c\n\n_parent_idB\n\n\x08_step_id\"\xf9\x01\n\x08Response\x12>\n\x11hierarchical_step\x18\x01 \x01(\x0b\x32#.messages.Response.HierarchicalStep\x12\x1e\n\x16max_duration_step_name\x18\x02 \x01(\t\x12\"\n\x1amax_duration_step_duration\x18\x03 \x01(\x05\x1ai\n\x10HierarchicalStep\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12\x35\n\x08\x63hildren\x18\x03 \x03(\x0b\x32#.messages.Response.HierarchicalStepb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=29
  _REQUEST._serialized_end=201
  _REQUEST_STEP._serialized_start=101
  _REQUEST_STEP._serialized_end=189
  _RESPONSE._serialized_start=204
  _RESPONSE._serialized_end=453
  _RESPONSE_HIERARCHICALSTEP._serialized_start=348
  _RESPONSE_HIERARCHICALSTEP._serialized_end=453
# @@protoc_insertion_point(module_scope)
