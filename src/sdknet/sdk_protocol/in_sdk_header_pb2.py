# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: in_sdk_header.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='in_sdk_header.proto',
  package='insider.sdk',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13in_sdk_header.proto\x12\x0binsider.sdk\"L\n\x04Host\x12*\n\nip_version\x18\x01 \x01(\x0e\x32\x16.insider.sdk.IpVersion\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\n\n\x02ip\x18\x03 \x01(\t\"-\n\x08\x44\x61taTime\x12\x0f\n\x07in_time\x18\x01 \x01(\x03\x12\x10\n\x08out_time\x18\x02 \x01(\x03\"\xab\x02\n\x06Header\x12(\n\tmsg_magic\x18\x01 \x01(\x0e\x32\x15.insider.sdk.SdkMagic\x12(\n\x07version\x18\x02 \x01(\x0e\x32\x17.insider.sdk.SdkVersion\x12\x0f\n\x07pack_id\x18\x03 \x01(\x03\x12#\n\x04time\x18\x04 \x01(\x0b\x32\x15.insider.sdk.DataTime\x12\'\n\x08\x64\x61ta_dir\x18\x05 \x01(\x0e\x32\x15.insider.sdk.DataFlow\x12\x1f\n\x04host\x18\x06 \x01(\x0b\x32\x11.insider.sdk.Host\x12\x1f\n\x04\x64\x65st\x18\x07 \x01(\x0b\x32\x11.insider.sdk.Host\x12,\n\x0btrans_proto\x18\x08 \x01(\x0e\x32\x17.insider.sdk.TransProto*7\n\nTransProto\x12\x17\n\x13TRANS_PROTO_INVALID\x10\x00\x12\x07\n\x03TCP\x10\x01\x12\x07\n\x03UDP\x10\x02*7\n\tIpVersion\x12\x16\n\x12IP_VERSION_INVALID\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02*%\n\x08\x44\x61taFlow\x12\x0b\n\x07\x44\x41TA_IN\x10\x00\x12\x0c\n\x08\x44\x41TA_OUT\x10\x01*/\n\x08SdkMagic\x12\x11\n\rSDK_NON_MAGIC\x10\x00\x12\x10\n\tSDK_MAGIC\x10\xef\x9b\xaf\r*9\n\nSdkVersion\x12\x13\n\x0fSDK_NON_VERSION\x10\x00\x12\x16\n\x0fSDK_CUR_VERSION\x10\x86\xaf\xd0\tb\x06proto3')
)

_TRANSPROTO = _descriptor.EnumDescriptor(
  name='TransProto',
  full_name='insider.sdk.TransProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANS_PROTO_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TCP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UDP', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=463,
  serialized_end=518,
)
_sym_db.RegisterEnumDescriptor(_TRANSPROTO)

TransProto = enum_type_wrapper.EnumTypeWrapper(_TRANSPROTO)
_IPVERSION = _descriptor.EnumDescriptor(
  name='IpVersion',
  full_name='insider.sdk.IpVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IP_VERSION_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV4', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV6', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=520,
  serialized_end=575,
)
_sym_db.RegisterEnumDescriptor(_IPVERSION)

IpVersion = enum_type_wrapper.EnumTypeWrapper(_IPVERSION)
_DATAFLOW = _descriptor.EnumDescriptor(
  name='DataFlow',
  full_name='insider.sdk.DataFlow',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA_IN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_OUT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=577,
  serialized_end=614,
)
_sym_db.RegisterEnumDescriptor(_DATAFLOW)

DataFlow = enum_type_wrapper.EnumTypeWrapper(_DATAFLOW)
_SDKMAGIC = _descriptor.EnumDescriptor(
  name='SdkMagic',
  full_name='insider.sdk.SdkMagic',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SDK_NON_MAGIC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SDK_MAGIC', index=1, number=28036591,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=616,
  serialized_end=663,
)
_sym_db.RegisterEnumDescriptor(_SDKMAGIC)

SdkMagic = enum_type_wrapper.EnumTypeWrapper(_SDKMAGIC)
_SDKVERSION = _descriptor.EnumDescriptor(
  name='SdkVersion',
  full_name='insider.sdk.SdkVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SDK_NON_VERSION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SDK_CUR_VERSION', index=1, number=20191110,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=665,
  serialized_end=722,
)
_sym_db.RegisterEnumDescriptor(_SDKVERSION)

SdkVersion = enum_type_wrapper.EnumTypeWrapper(_SDKVERSION)
TRANS_PROTO_INVALID = 0
TCP = 1
UDP = 2
IP_VERSION_INVALID = 0
IPV4 = 1
IPV6 = 2
DATA_IN = 0
DATA_OUT = 1
SDK_NON_MAGIC = 0
SDK_MAGIC = 28036591
SDK_NON_VERSION = 0
SDK_CUR_VERSION = 20191110



_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='insider.sdk.Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_version', full_name='insider.sdk.Host.ip_version', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='insider.sdk.Host.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='insider.sdk.Host.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=36,
  serialized_end=112,
)


_DATATIME = _descriptor.Descriptor(
  name='DataTime',
  full_name='insider.sdk.DataTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='in_time', full_name='insider.sdk.DataTime.in_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_time', full_name='insider.sdk.DataTime.out_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=114,
  serialized_end=159,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='insider.sdk.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_magic', full_name='insider.sdk.Header.msg_magic', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='insider.sdk.Header.version', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pack_id', full_name='insider.sdk.Header.pack_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='insider.sdk.Header.time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_dir', full_name='insider.sdk.Header.data_dir', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='insider.sdk.Header.host', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest', full_name='insider.sdk.Header.dest', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trans_proto', full_name='insider.sdk.Header.trans_proto', index=7,
      number=8, type=14, cpp_type=8, label=1,
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
  serialized_start=162,
  serialized_end=461,
)

_HOST.fields_by_name['ip_version'].enum_type = _IPVERSION
_HEADER.fields_by_name['msg_magic'].enum_type = _SDKMAGIC
_HEADER.fields_by_name['version'].enum_type = _SDKVERSION
_HEADER.fields_by_name['time'].message_type = _DATATIME
_HEADER.fields_by_name['data_dir'].enum_type = _DATAFLOW
_HEADER.fields_by_name['host'].message_type = _HOST
_HEADER.fields_by_name['dest'].message_type = _HOST
_HEADER.fields_by_name['trans_proto'].enum_type = _TRANSPROTO
DESCRIPTOR.message_types_by_name['Host'] = _HOST
DESCRIPTOR.message_types_by_name['DataTime'] = _DATATIME
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.enum_types_by_name['TransProto'] = _TRANSPROTO
DESCRIPTOR.enum_types_by_name['IpVersion'] = _IPVERSION
DESCRIPTOR.enum_types_by_name['DataFlow'] = _DATAFLOW
DESCRIPTOR.enum_types_by_name['SdkMagic'] = _SDKMAGIC
DESCRIPTOR.enum_types_by_name['SdkVersion'] = _SDKVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Host = _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
  'DESCRIPTOR' : _HOST,
  '__module__' : 'in_sdk_header_pb2'
  # @@protoc_insertion_point(class_scope:insider.sdk.Host)
  })
_sym_db.RegisterMessage(Host)

DataTime = _reflection.GeneratedProtocolMessageType('DataTime', (_message.Message,), {
  'DESCRIPTOR' : _DATATIME,
  '__module__' : 'in_sdk_header_pb2'
  # @@protoc_insertion_point(class_scope:insider.sdk.DataTime)
  })
_sym_db.RegisterMessage(DataTime)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'in_sdk_header_pb2'
  # @@protoc_insertion_point(class_scope:insider.sdk.Header)
  })
_sym_db.RegisterMessage(Header)


# @@protoc_insertion_point(module_scope)
