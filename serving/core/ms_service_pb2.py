# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ms_service.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ms_service.proto',
  package='ms_serving',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10ms_service.proto\x12\nms_serving\"2\n\x0ePredictRequest\x12 \n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x12.ms_serving.Tensor\"2\n\x0cPredictReply\x12\"\n\x06result\x18\x01 \x03(\x0b\x32\x12.ms_serving.Tensor\"\x1b\n\x0bTensorShape\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x03\"p\n\x06Tensor\x12-\n\x0ctensor_shape\x18\x01 \x01(\x0b\x32\x17.ms_serving.TensorShape\x12)\n\x0btensor_type\x18\x02 \x01(\x0e\x32\x14.ms_serving.DataType\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c*\xc9\x01\n\x08\x44\x61taType\x12\x0e\n\nMS_UNKNOWN\x10\x00\x12\x0b\n\x07MS_BOOL\x10\x01\x12\x0b\n\x07MS_INT8\x10\x02\x12\x0c\n\x08MS_UINT8\x10\x03\x12\x0c\n\x08MS_INT16\x10\x04\x12\r\n\tMS_UINT16\x10\x05\x12\x0c\n\x08MS_INT32\x10\x06\x12\r\n\tMS_UINT32\x10\x07\x12\x0c\n\x08MS_INT64\x10\x08\x12\r\n\tMS_UINT64\x10\t\x12\x0e\n\nMS_FLOAT16\x10\n\x12\x0e\n\nMS_FLOAT32\x10\x0b\x12\x0e\n\nMS_FLOAT64\x10\x0c\x32\x8e\x01\n\tMSService\x12\x41\n\x07Predict\x12\x1a.ms_serving.PredictRequest\x1a\x18.ms_serving.PredictReply\"\x00\x12>\n\x04Test\x12\x1a.ms_serving.PredictRequest\x1a\x18.ms_serving.PredictReply\"\x00\x62\x06proto3'
)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='ms_serving.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_BOOL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_INT8', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_UINT8', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_INT16', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_UINT16', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_INT32', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_UINT32', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_INT64', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_UINT64', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_FLOAT16', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_FLOAT32', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS_FLOAT64', index=12, number=12,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=280,
  serialized_end=481,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
MS_UNKNOWN = 0
MS_BOOL = 1
MS_INT8 = 2
MS_UINT8 = 3
MS_INT16 = 4
MS_UINT16 = 5
MS_INT32 = 6
MS_UINT32 = 7
MS_INT64 = 8
MS_UINT64 = 9
MS_FLOAT16 = 10
MS_FLOAT32 = 11
MS_FLOAT64 = 12



_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='ms_serving.PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ms_serving.PredictRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=32,
  serialized_end=82,
)


_PREDICTREPLY = _descriptor.Descriptor(
  name='PredictReply',
  full_name='ms_serving.PredictReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ms_serving.PredictReply.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=84,
  serialized_end=134,
)


_TENSORSHAPE = _descriptor.Descriptor(
  name='TensorShape',
  full_name='ms_serving.TensorShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='ms_serving.TensorShape.dims', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=136,
  serialized_end=163,
)


_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='ms_serving.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='ms_serving.Tensor.tensor_shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_type', full_name='ms_serving.Tensor.tensor_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ms_serving.Tensor.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=165,
  serialized_end=277,
)

_PREDICTREQUEST.fields_by_name['data'].message_type = _TENSOR
_PREDICTREPLY.fields_by_name['result'].message_type = _TENSOR
_TENSOR.fields_by_name['tensor_shape'].message_type = _TENSORSHAPE
_TENSOR.fields_by_name['tensor_type'].enum_type = _DATATYPE
DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictReply'] = _PREDICTREPLY
DESCRIPTOR.message_types_by_name['TensorShape'] = _TENSORSHAPE
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTREQUEST,
  '__module__' : 'ms_service_pb2'
  # @@protoc_insertion_point(class_scope:ms_serving.PredictRequest)
  })
_sym_db.RegisterMessage(PredictRequest)

PredictReply = _reflection.GeneratedProtocolMessageType('PredictReply', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTREPLY,
  '__module__' : 'ms_service_pb2'
  # @@protoc_insertion_point(class_scope:ms_serving.PredictReply)
  })
_sym_db.RegisterMessage(PredictReply)

TensorShape = _reflection.GeneratedProtocolMessageType('TensorShape', (_message.Message,), {
  'DESCRIPTOR' : _TENSORSHAPE,
  '__module__' : 'ms_service_pb2'
  # @@protoc_insertion_point(class_scope:ms_serving.TensorShape)
  })
_sym_db.RegisterMessage(TensorShape)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'ms_service_pb2'
  # @@protoc_insertion_point(class_scope:ms_serving.Tensor)
  })
_sym_db.RegisterMessage(Tensor)



_MSSERVICE = _descriptor.ServiceDescriptor(
  name='MSService',
  full_name='ms_serving.MSService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=484,
  serialized_end=626,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='ms_serving.MSService.Predict',
    index=0,
    containing_service=None,
    input_type=_PREDICTREQUEST,
    output_type=_PREDICTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='ms_serving.MSService.Test',
    index=1,
    containing_service=None,
    input_type=_PREDICTREQUEST,
    output_type=_PREDICTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSSERVICE)

DESCRIPTOR.services_by_name['MSService'] = _MSSERVICE

# @@protoc_insertion_point(module_scope)