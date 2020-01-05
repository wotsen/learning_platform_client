# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: in_sdk_body.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import in_sdk_body_user_pb2 as in__sdk__body__user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='in_sdk_body.proto',
  package='insider.sdk',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11in_sdk_body.proto\x12\x0binsider.sdk\x1a\x16in_sdk_body_user.proto\"\x18\n\x07\x43ontent\x12\r\n\x05magic\x18\x01 \x01(\x03\"\x99\x01\n\x04\x42ody\x12\x31\n\x0cuser_session\x18\x01 \x01(\x0b\x32\x1b.insider.sdk.UserSessionMsg\x12\x0b\n\x03url\x18\x02 \x01(\t\x12*\n\x06method\x18\x03 \x01(\x0e\x32\x1a.insider.sdk.OperationType\x12%\n\x07\x63ontent\x18\x05 \x01(\x0b\x32\x14.insider.sdk.Content*7\n\rOperationType\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03PUT\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x62\x06proto3')
  ,
  dependencies=[in__sdk__body__user__pb2.DESCRIPTOR,])

_OPERATIONTYPE = _descriptor.EnumDescriptor(
  name='OperationType',
  full_name='insider.sdk.OperationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=240,
  serialized_end=295,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONTYPE)

OperationType = enum_type_wrapper.EnumTypeWrapper(_OPERATIONTYPE)
GET = 0
POST = 1
PUT = 2
DELETE = 3



_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='insider.sdk.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='magic', full_name='insider.sdk.Content.magic', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=82,
)


_BODY = _descriptor.Descriptor(
  name='Body',
  full_name='insider.sdk.Body',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_session', full_name='insider.sdk.Body.user_session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='insider.sdk.Body.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='insider.sdk.Body.method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='insider.sdk.Body.content', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=238,
)

_BODY.fields_by_name['user_session'].message_type = in__sdk__body__user__pb2._USERSESSIONMSG
_BODY.fields_by_name['method'].enum_type = _OPERATIONTYPE
_BODY.fields_by_name['content'].message_type = _CONTENT
DESCRIPTOR.message_types_by_name['Content'] = _CONTENT
DESCRIPTOR.message_types_by_name['Body'] = _BODY
DESCRIPTOR.enum_types_by_name['OperationType'] = _OPERATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {
  'DESCRIPTOR' : _CONTENT,
  '__module__' : 'in_sdk_body_pb2'
  # @@protoc_insertion_point(class_scope:insider.sdk.Content)
  })
_sym_db.RegisterMessage(Content)

Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), {
  'DESCRIPTOR' : _BODY,
  '__module__' : 'in_sdk_body_pb2'
  # @@protoc_insertion_point(class_scope:insider.sdk.Body)
  })
_sym_db.RegisterMessage(Body)


# @@protoc_insertion_point(module_scope)