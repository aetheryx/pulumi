# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pulumi/provider.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import plugin_pb2 as pulumi_dot_plugin__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pulumi/provider.proto\x12\tpulumirpc\x1a\x13pulumi/plugin.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"#\n\x10GetSchemaRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\"#\n\x11GetSchemaResponse\x12\x0e\n\x06schema\x18\x01 \x01(\t\"\xda\x01\n\x10\x43onfigureRequest\x12=\n\tvariables\x18\x01 \x03(\x0b\x32*.pulumirpc.ConfigureRequest.VariablesEntry\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\racceptSecrets\x18\x03 \x01(\x08\x12\x17\n\x0f\x61\x63\x63\x65ptResources\x18\x04 \x01(\x08\x1a\x30\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"s\n\x11\x43onfigureResponse\x12\x15\n\racceptSecrets\x18\x01 \x01(\x08\x12\x17\n\x0fsupportsPreview\x18\x02 \x01(\x08\x12\x17\n\x0f\x61\x63\x63\x65ptResources\x18\x03 \x01(\x08\x12\x15\n\racceptOutputs\x18\x04 \x01(\x08\"\x92\x01\n\x19\x43onfigureErrorMissingKeys\x12\x44\n\x0bmissingKeys\x18\x01 \x03(\x0b\x32/.pulumirpc.ConfigureErrorMissingKeys.MissingKey\x1a/\n\nMissingKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x80\x01\n\rInvokeRequest\x12\x0b\n\x03tok\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructJ\x04\x08\x03\x10\x07R\x08providerR\x07versionR\x0f\x61\x63\x63\x65ptResourcesR\x11pluginDownloadURL\"d\n\x0eInvokeResponse\x12\'\n\x06return\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\"\xa8\x04\n\x0b\x43\x61llRequest\x12\x0b\n\x03tok\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x44\n\x0f\x61rgDependencies\x18\x03 \x03(\x0b\x32+.pulumirpc.CallRequest.ArgDependenciesEntry\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x19\n\x11pluginDownloadURL\x18\r \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\r\n\x05stack\x18\x07 \x01(\t\x12\x32\n\x06\x63onfig\x18\x08 \x03(\x0b\x32\".pulumirpc.CallRequest.ConfigEntry\x12\x18\n\x10\x63onfigSecretKeys\x18\t \x03(\t\x12\x0e\n\x06\x64ryRun\x18\n \x01(\x08\x12\x10\n\x08parallel\x18\x0b \x01(\x05\x12\x17\n\x0fmonitorEndpoint\x18\x0c \x01(\t\x1a$\n\x14\x41rgumentDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a\x63\n\x14\x41rgDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.pulumirpc.CallRequest.ArgumentDependencies:\x02\x38\x01\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x02\n\x0c\x43\x61llResponse\x12\'\n\x06return\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12K\n\x12returnDependencies\x18\x02 \x03(\x0b\x32/.pulumirpc.CallResponse.ReturnDependenciesEntry\x12)\n\x08\x66\x61ilures\x18\x03 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\x1a\"\n\x12ReturnDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a\x65\n\x17ReturnDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.pulumirpc.CallResponse.ReturnDependencies:\x02\x38\x01\"\x95\x01\n\x0c\x43heckRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12%\n\x04olds\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x16\n\x0esequenceNumber\x18\x04 \x01(\x05\x12\x12\n\nrandomSeed\x18\x05 \x01(\x0c\"c\n\rCheckResponse\x12\'\n\x06inputs\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\"0\n\x0c\x43heckFailure\x12\x10\n\x08property\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\x8b\x01\n\x0b\x44iffRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12%\n\x04olds\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\rignoreChanges\x18\x05 \x03(\t\"\xaf\x01\n\x0cPropertyDiff\x12*\n\x04kind\x18\x01 \x01(\x0e\x32\x1c.pulumirpc.PropertyDiff.Kind\x12\x11\n\tinputDiff\x18\x02 \x01(\x08\"`\n\x04Kind\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\x0f\n\x0b\x41\x44\x44_REPLACE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\x12\n\x0e\x44\x45LETE_REPLACE\x10\x03\x12\n\n\x06UPDATE\x10\x04\x12\x12\n\x0eUPDATE_REPLACE\x10\x05\"\xfa\x02\n\x0c\x44iffResponse\x12\x10\n\x08replaces\x18\x01 \x03(\t\x12\x0f\n\x07stables\x18\x02 \x03(\t\x12\x1b\n\x13\x64\x65leteBeforeReplace\x18\x03 \x01(\x08\x12\x34\n\x07\x63hanges\x18\x04 \x01(\x0e\x32#.pulumirpc.DiffResponse.DiffChanges\x12\r\n\x05\x64iffs\x18\x05 \x03(\t\x12?\n\x0c\x64\x65tailedDiff\x18\x06 \x03(\x0b\x32).pulumirpc.DiffResponse.DetailedDiffEntry\x12\x17\n\x0fhasDetailedDiff\x18\x07 \x01(\x08\x1aL\n\x11\x44\x65tailedDiffEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.pulumirpc.PropertyDiff:\x02\x38\x01\"=\n\x0b\x44iffChanges\x12\x10\n\x0c\x44IFF_UNKNOWN\x10\x00\x12\r\n\tDIFF_NONE\x10\x01\x12\r\n\tDIFF_SOME\x10\x02\"k\n\rCreateRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x0f\n\x07preview\x18\x04 \x01(\x08\"I\n\x0e\x43reateResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"|\n\x0bReadRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06inputs\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"p\n\x0cReadResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06inputs\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xaf\x01\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12%\n\x04olds\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07timeout\x18\x05 \x01(\x01\x12\x15\n\rignoreChanges\x18\x06 \x03(\t\x12\x0f\n\x07preview\x18\x07 \x01(\x08\"=\n\x0eUpdateResponse\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"f\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\"\xce\x05\n\x10\x43onstructRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05stack\x18\x02 \x01(\t\x12\x37\n\x06\x63onfig\x18\x03 \x03(\x0b\x32\'.pulumirpc.ConstructRequest.ConfigEntry\x12\x0e\n\x06\x64ryRun\x18\x04 \x01(\x08\x12\x10\n\x08parallel\x18\x05 \x01(\x05\x12\x17\n\x0fmonitorEndpoint\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0e\n\x06parent\x18\t \x01(\t\x12\'\n\x06inputs\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct\x12M\n\x11inputDependencies\x18\x0b \x03(\x0b\x32\x32.pulumirpc.ConstructRequest.InputDependenciesEntry\x12\x0f\n\x07protect\x18\x0c \x01(\x08\x12=\n\tproviders\x18\r \x03(\x0b\x32*.pulumirpc.ConstructRequest.ProvidersEntry\x12\x0f\n\x07\x61liases\x18\x0e \x03(\t\x12\x14\n\x0c\x64\x65pendencies\x18\x0f \x03(\t\x12\x18\n\x10\x63onfigSecretKeys\x18\x10 \x03(\t\x1a$\n\x14PropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aj\n\x16InputDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0b\x32\x30.pulumirpc.ConstructRequest.PropertyDependencies:\x02\x38\x01\x1a\x30\n\x0eProvidersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xab\x02\n\x11\x43onstructResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12N\n\x11stateDependencies\x18\x03 \x03(\x0b\x32\x33.pulumirpc.ConstructResponse.StateDependenciesEntry\x1a$\n\x14PropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1ak\n\x16StateDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.pulumirpc.ConstructResponse.PropertyDependencies:\x02\x38\x01\"\x8c\x01\n\x17\x45rrorResourceInitFailed\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07reasons\x18\x03 \x03(\t\x12\'\n\x06inputs\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct2\xe9\x08\n\x10ResourceProvider\x12H\n\tGetSchema\x12\x1b.pulumirpc.GetSchemaRequest\x1a\x1c.pulumirpc.GetSchemaResponse\"\x00\x12\x42\n\x0b\x43heckConfig\x12\x17.pulumirpc.CheckRequest\x1a\x18.pulumirpc.CheckResponse\"\x00\x12?\n\nDiffConfig\x12\x16.pulumirpc.DiffRequest\x1a\x17.pulumirpc.DiffResponse\"\x00\x12H\n\tConfigure\x12\x1b.pulumirpc.ConfigureRequest\x1a\x1c.pulumirpc.ConfigureResponse\"\x00\x12?\n\x06Invoke\x12\x18.pulumirpc.InvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x12G\n\x0cStreamInvoke\x12\x18.pulumirpc.InvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x30\x01\x12\x39\n\x04\x43\x61ll\x12\x16.pulumirpc.CallRequest\x1a\x17.pulumirpc.CallResponse\"\x00\x12<\n\x05\x43heck\x12\x17.pulumirpc.CheckRequest\x1a\x18.pulumirpc.CheckResponse\"\x00\x12\x39\n\x04\x44iff\x12\x16.pulumirpc.DiffRequest\x1a\x17.pulumirpc.DiffResponse\"\x00\x12?\n\x06\x43reate\x12\x18.pulumirpc.CreateRequest\x1a\x19.pulumirpc.CreateResponse\"\x00\x12\x39\n\x04Read\x12\x16.pulumirpc.ReadRequest\x1a\x17.pulumirpc.ReadResponse\"\x00\x12?\n\x06Update\x12\x18.pulumirpc.UpdateRequest\x1a\x19.pulumirpc.UpdateResponse\"\x00\x12<\n\x06\x44\x65lete\x12\x18.pulumirpc.DeleteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12H\n\tConstruct\x12\x1b.pulumirpc.ConstructRequest\x1a\x1c.pulumirpc.ConstructResponse\"\x00\x12:\n\x06\x43\x61ncel\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12@\n\rGetPluginInfo\x12\x16.google.protobuf.Empty\x1a\x15.pulumirpc.PluginInfo\"\x00\x12;\n\x06\x41ttach\x12\x17.pulumirpc.PluginAttach\x1a\x16.google.protobuf.Empty\"\x00\x42\x30Z.github.com/pulumi/pulumi/v3/proto/go/pulumirpcb\x06proto3')



_GETSCHEMAREQUEST = DESCRIPTOR.message_types_by_name['GetSchemaRequest']
_GETSCHEMARESPONSE = DESCRIPTOR.message_types_by_name['GetSchemaResponse']
_CONFIGUREREQUEST = DESCRIPTOR.message_types_by_name['ConfigureRequest']
_CONFIGUREREQUEST_VARIABLESENTRY = _CONFIGUREREQUEST.nested_types_by_name['VariablesEntry']
_CONFIGURERESPONSE = DESCRIPTOR.message_types_by_name['ConfigureResponse']
_CONFIGUREERRORMISSINGKEYS = DESCRIPTOR.message_types_by_name['ConfigureErrorMissingKeys']
_CONFIGUREERRORMISSINGKEYS_MISSINGKEY = _CONFIGUREERRORMISSINGKEYS.nested_types_by_name['MissingKey']
_INVOKEREQUEST = DESCRIPTOR.message_types_by_name['InvokeRequest']
_INVOKERESPONSE = DESCRIPTOR.message_types_by_name['InvokeResponse']
_CALLREQUEST = DESCRIPTOR.message_types_by_name['CallRequest']
_CALLREQUEST_ARGUMENTDEPENDENCIES = _CALLREQUEST.nested_types_by_name['ArgumentDependencies']
_CALLREQUEST_ARGDEPENDENCIESENTRY = _CALLREQUEST.nested_types_by_name['ArgDependenciesEntry']
_CALLREQUEST_CONFIGENTRY = _CALLREQUEST.nested_types_by_name['ConfigEntry']
_CALLRESPONSE = DESCRIPTOR.message_types_by_name['CallResponse']
_CALLRESPONSE_RETURNDEPENDENCIES = _CALLRESPONSE.nested_types_by_name['ReturnDependencies']
_CALLRESPONSE_RETURNDEPENDENCIESENTRY = _CALLRESPONSE.nested_types_by_name['ReturnDependenciesEntry']
_CHECKREQUEST = DESCRIPTOR.message_types_by_name['CheckRequest']
_CHECKRESPONSE = DESCRIPTOR.message_types_by_name['CheckResponse']
_CHECKFAILURE = DESCRIPTOR.message_types_by_name['CheckFailure']
_DIFFREQUEST = DESCRIPTOR.message_types_by_name['DiffRequest']
_PROPERTYDIFF = DESCRIPTOR.message_types_by_name['PropertyDiff']
_DIFFRESPONSE = DESCRIPTOR.message_types_by_name['DiffResponse']
_DIFFRESPONSE_DETAILEDDIFFENTRY = _DIFFRESPONSE.nested_types_by_name['DetailedDiffEntry']
_CREATEREQUEST = DESCRIPTOR.message_types_by_name['CreateRequest']
_CREATERESPONSE = DESCRIPTOR.message_types_by_name['CreateResponse']
_READREQUEST = DESCRIPTOR.message_types_by_name['ReadRequest']
_READRESPONSE = DESCRIPTOR.message_types_by_name['ReadResponse']
_UPDATEREQUEST = DESCRIPTOR.message_types_by_name['UpdateRequest']
_UPDATERESPONSE = DESCRIPTOR.message_types_by_name['UpdateResponse']
_DELETEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRequest']
_CONSTRUCTREQUEST = DESCRIPTOR.message_types_by_name['ConstructRequest']
_CONSTRUCTREQUEST_PROPERTYDEPENDENCIES = _CONSTRUCTREQUEST.nested_types_by_name['PropertyDependencies']
_CONSTRUCTREQUEST_CONFIGENTRY = _CONSTRUCTREQUEST.nested_types_by_name['ConfigEntry']
_CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY = _CONSTRUCTREQUEST.nested_types_by_name['InputDependenciesEntry']
_CONSTRUCTREQUEST_PROVIDERSENTRY = _CONSTRUCTREQUEST.nested_types_by_name['ProvidersEntry']
_CONSTRUCTRESPONSE = DESCRIPTOR.message_types_by_name['ConstructResponse']
_CONSTRUCTRESPONSE_PROPERTYDEPENDENCIES = _CONSTRUCTRESPONSE.nested_types_by_name['PropertyDependencies']
_CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY = _CONSTRUCTRESPONSE.nested_types_by_name['StateDependenciesEntry']
_ERRORRESOURCEINITFAILED = DESCRIPTOR.message_types_by_name['ErrorResourceInitFailed']
_PROPERTYDIFF_KIND = _PROPERTYDIFF.enum_types_by_name['Kind']
_DIFFRESPONSE_DIFFCHANGES = _DIFFRESPONSE.enum_types_by_name['DiffChanges']
GetSchemaRequest = _reflection.GeneratedProtocolMessageType('GetSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSCHEMAREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.GetSchemaRequest)
  })
_sym_db.RegisterMessage(GetSchemaRequest)

GetSchemaResponse = _reflection.GeneratedProtocolMessageType('GetSchemaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSCHEMARESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.GetSchemaResponse)
  })
_sym_db.RegisterMessage(GetSchemaResponse)

ConfigureRequest = _reflection.GeneratedProtocolMessageType('ConfigureRequest', (_message.Message,), {

  'VariablesEntry' : _reflection.GeneratedProtocolMessageType('VariablesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGUREREQUEST_VARIABLESENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureRequest.VariablesEntry)
    })
  ,
  'DESCRIPTOR' : _CONFIGUREREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureRequest)
  })
_sym_db.RegisterMessage(ConfigureRequest)
_sym_db.RegisterMessage(ConfigureRequest.VariablesEntry)

ConfigureResponse = _reflection.GeneratedProtocolMessageType('ConfigureResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURERESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureResponse)
  })
_sym_db.RegisterMessage(ConfigureResponse)

ConfigureErrorMissingKeys = _reflection.GeneratedProtocolMessageType('ConfigureErrorMissingKeys', (_message.Message,), {

  'MissingKey' : _reflection.GeneratedProtocolMessageType('MissingKey', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGUREERRORMISSINGKEYS_MISSINGKEY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureErrorMissingKeys.MissingKey)
    })
  ,
  'DESCRIPTOR' : _CONFIGUREERRORMISSINGKEYS,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ConfigureErrorMissingKeys)
  })
_sym_db.RegisterMessage(ConfigureErrorMissingKeys)
_sym_db.RegisterMessage(ConfigureErrorMissingKeys.MissingKey)

InvokeRequest = _reflection.GeneratedProtocolMessageType('InvokeRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.InvokeRequest)
  })
_sym_db.RegisterMessage(InvokeRequest)

InvokeResponse = _reflection.GeneratedProtocolMessageType('InvokeResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOKERESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.InvokeResponse)
  })
_sym_db.RegisterMessage(InvokeResponse)

CallRequest = _reflection.GeneratedProtocolMessageType('CallRequest', (_message.Message,), {

  'ArgumentDependencies' : _reflection.GeneratedProtocolMessageType('ArgumentDependencies', (_message.Message,), {
    'DESCRIPTOR' : _CALLREQUEST_ARGUMENTDEPENDENCIES,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.CallRequest.ArgumentDependencies)
    })
  ,

  'ArgDependenciesEntry' : _reflection.GeneratedProtocolMessageType('ArgDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CALLREQUEST_ARGDEPENDENCIESENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.CallRequest.ArgDependenciesEntry)
    })
  ,

  'ConfigEntry' : _reflection.GeneratedProtocolMessageType('ConfigEntry', (_message.Message,), {
    'DESCRIPTOR' : _CALLREQUEST_CONFIGENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.CallRequest.ConfigEntry)
    })
  ,
  'DESCRIPTOR' : _CALLREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CallRequest)
  })
_sym_db.RegisterMessage(CallRequest)
_sym_db.RegisterMessage(CallRequest.ArgumentDependencies)
_sym_db.RegisterMessage(CallRequest.ArgDependenciesEntry)
_sym_db.RegisterMessage(CallRequest.ConfigEntry)

CallResponse = _reflection.GeneratedProtocolMessageType('CallResponse', (_message.Message,), {

  'ReturnDependencies' : _reflection.GeneratedProtocolMessageType('ReturnDependencies', (_message.Message,), {
    'DESCRIPTOR' : _CALLRESPONSE_RETURNDEPENDENCIES,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.CallResponse.ReturnDependencies)
    })
  ,

  'ReturnDependenciesEntry' : _reflection.GeneratedProtocolMessageType('ReturnDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CALLRESPONSE_RETURNDEPENDENCIESENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.CallResponse.ReturnDependenciesEntry)
    })
  ,
  'DESCRIPTOR' : _CALLRESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CallResponse)
  })
_sym_db.RegisterMessage(CallResponse)
_sym_db.RegisterMessage(CallResponse.ReturnDependencies)
_sym_db.RegisterMessage(CallResponse.ReturnDependenciesEntry)

CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CheckRequest)
  })
_sym_db.RegisterMessage(CheckRequest)

CheckResponse = _reflection.GeneratedProtocolMessageType('CheckResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKRESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CheckResponse)
  })
_sym_db.RegisterMessage(CheckResponse)

CheckFailure = _reflection.GeneratedProtocolMessageType('CheckFailure', (_message.Message,), {
  'DESCRIPTOR' : _CHECKFAILURE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CheckFailure)
  })
_sym_db.RegisterMessage(CheckFailure)

DiffRequest = _reflection.GeneratedProtocolMessageType('DiffRequest', (_message.Message,), {
  'DESCRIPTOR' : _DIFFREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.DiffRequest)
  })
_sym_db.RegisterMessage(DiffRequest)

PropertyDiff = _reflection.GeneratedProtocolMessageType('PropertyDiff', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYDIFF,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.PropertyDiff)
  })
_sym_db.RegisterMessage(PropertyDiff)

DiffResponse = _reflection.GeneratedProtocolMessageType('DiffResponse', (_message.Message,), {

  'DetailedDiffEntry' : _reflection.GeneratedProtocolMessageType('DetailedDiffEntry', (_message.Message,), {
    'DESCRIPTOR' : _DIFFRESPONSE_DETAILEDDIFFENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.DiffResponse.DetailedDiffEntry)
    })
  ,
  'DESCRIPTOR' : _DIFFRESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.DiffResponse)
  })
_sym_db.RegisterMessage(DiffResponse)
_sym_db.RegisterMessage(DiffResponse.DetailedDiffEntry)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.CreateResponse)
  })
_sym_db.RegisterMessage(CreateResponse)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

ConstructRequest = _reflection.GeneratedProtocolMessageType('ConstructRequest', (_message.Message,), {

  'PropertyDependencies' : _reflection.GeneratedProtocolMessageType('PropertyDependencies', (_message.Message,), {
    'DESCRIPTOR' : _CONSTRUCTREQUEST_PROPERTYDEPENDENCIES,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConstructRequest.PropertyDependencies)
    })
  ,

  'ConfigEntry' : _reflection.GeneratedProtocolMessageType('ConfigEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONSTRUCTREQUEST_CONFIGENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConstructRequest.ConfigEntry)
    })
  ,

  'InputDependenciesEntry' : _reflection.GeneratedProtocolMessageType('InputDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConstructRequest.InputDependenciesEntry)
    })
  ,

  'ProvidersEntry' : _reflection.GeneratedProtocolMessageType('ProvidersEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONSTRUCTREQUEST_PROVIDERSENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConstructRequest.ProvidersEntry)
    })
  ,
  'DESCRIPTOR' : _CONSTRUCTREQUEST,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ConstructRequest)
  })
_sym_db.RegisterMessage(ConstructRequest)
_sym_db.RegisterMessage(ConstructRequest.PropertyDependencies)
_sym_db.RegisterMessage(ConstructRequest.ConfigEntry)
_sym_db.RegisterMessage(ConstructRequest.InputDependenciesEntry)
_sym_db.RegisterMessage(ConstructRequest.ProvidersEntry)

ConstructResponse = _reflection.GeneratedProtocolMessageType('ConstructResponse', (_message.Message,), {

  'PropertyDependencies' : _reflection.GeneratedProtocolMessageType('PropertyDependencies', (_message.Message,), {
    'DESCRIPTOR' : _CONSTRUCTRESPONSE_PROPERTYDEPENDENCIES,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConstructResponse.PropertyDependencies)
    })
  ,

  'StateDependenciesEntry' : _reflection.GeneratedProtocolMessageType('StateDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY,
    '__module__' : 'pulumi.provider_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.ConstructResponse.StateDependenciesEntry)
    })
  ,
  'DESCRIPTOR' : _CONSTRUCTRESPONSE,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ConstructResponse)
  })
_sym_db.RegisterMessage(ConstructResponse)
_sym_db.RegisterMessage(ConstructResponse.PropertyDependencies)
_sym_db.RegisterMessage(ConstructResponse.StateDependenciesEntry)

ErrorResourceInitFailed = _reflection.GeneratedProtocolMessageType('ErrorResourceInitFailed', (_message.Message,), {
  'DESCRIPTOR' : _ERRORRESOURCEINITFAILED,
  '__module__' : 'pulumi.provider_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ErrorResourceInitFailed)
  })
_sym_db.RegisterMessage(ErrorResourceInitFailed)

_RESOURCEPROVIDER = DESCRIPTOR.services_by_name['ResourceProvider']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/pulumi/pulumi/v3/proto/go/pulumirpc'
  _CONFIGUREREQUEST_VARIABLESENTRY._options = None
  _CONFIGUREREQUEST_VARIABLESENTRY._serialized_options = b'8\001'
  _CALLREQUEST_ARGDEPENDENCIESENTRY._options = None
  _CALLREQUEST_ARGDEPENDENCIESENTRY._serialized_options = b'8\001'
  _CALLREQUEST_CONFIGENTRY._options = None
  _CALLREQUEST_CONFIGENTRY._serialized_options = b'8\001'
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._options = None
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._serialized_options = b'8\001'
  _DIFFRESPONSE_DETAILEDDIFFENTRY._options = None
  _DIFFRESPONSE_DETAILEDDIFFENTRY._serialized_options = b'8\001'
  _CONSTRUCTREQUEST_CONFIGENTRY._options = None
  _CONSTRUCTREQUEST_CONFIGENTRY._serialized_options = b'8\001'
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._options = None
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._serialized_options = b'8\001'
  _CONSTRUCTREQUEST_PROVIDERSENTRY._options = None
  _CONSTRUCTREQUEST_PROVIDERSENTRY._serialized_options = b'8\001'
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._options = None
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._serialized_options = b'8\001'
  _GETSCHEMAREQUEST._serialized_start=116
  _GETSCHEMAREQUEST._serialized_end=151
  _GETSCHEMARESPONSE._serialized_start=153
  _GETSCHEMARESPONSE._serialized_end=188
  _CONFIGUREREQUEST._serialized_start=191
  _CONFIGUREREQUEST._serialized_end=409
  _CONFIGUREREQUEST_VARIABLESENTRY._serialized_start=361
  _CONFIGUREREQUEST_VARIABLESENTRY._serialized_end=409
  _CONFIGURERESPONSE._serialized_start=411
  _CONFIGURERESPONSE._serialized_end=526
  _CONFIGUREERRORMISSINGKEYS._serialized_start=529
  _CONFIGUREERRORMISSINGKEYS._serialized_end=675
  _CONFIGUREERRORMISSINGKEYS_MISSINGKEY._serialized_start=628
  _CONFIGUREERRORMISSINGKEYS_MISSINGKEY._serialized_end=675
  _INVOKEREQUEST._serialized_start=678
  _INVOKEREQUEST._serialized_end=806
  _INVOKERESPONSE._serialized_start=808
  _INVOKERESPONSE._serialized_end=908
  _CALLREQUEST._serialized_start=911
  _CALLREQUEST._serialized_end=1463
  _CALLREQUEST_ARGUMENTDEPENDENCIES._serialized_start=1279
  _CALLREQUEST_ARGUMENTDEPENDENCIES._serialized_end=1315
  _CALLREQUEST_ARGDEPENDENCIESENTRY._serialized_start=1317
  _CALLREQUEST_ARGDEPENDENCIESENTRY._serialized_end=1416
  _CALLREQUEST_CONFIGENTRY._serialized_start=1418
  _CALLREQUEST_CONFIGENTRY._serialized_end=1463
  _CALLRESPONSE._serialized_start=1466
  _CALLRESPONSE._serialized_end=1780
  _CALLRESPONSE_RETURNDEPENDENCIES._serialized_start=1643
  _CALLRESPONSE_RETURNDEPENDENCIES._serialized_end=1677
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._serialized_start=1679
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._serialized_end=1780
  _CHECKREQUEST._serialized_start=1783
  _CHECKREQUEST._serialized_end=1932
  _CHECKRESPONSE._serialized_start=1934
  _CHECKRESPONSE._serialized_end=2033
  _CHECKFAILURE._serialized_start=2035
  _CHECKFAILURE._serialized_end=2083
  _DIFFREQUEST._serialized_start=2086
  _DIFFREQUEST._serialized_end=2225
  _PROPERTYDIFF._serialized_start=2228
  _PROPERTYDIFF._serialized_end=2403
  _PROPERTYDIFF_KIND._serialized_start=2307
  _PROPERTYDIFF_KIND._serialized_end=2403
  _DIFFRESPONSE._serialized_start=2406
  _DIFFRESPONSE._serialized_end=2784
  _DIFFRESPONSE_DETAILEDDIFFENTRY._serialized_start=2645
  _DIFFRESPONSE_DETAILEDDIFFENTRY._serialized_end=2721
  _DIFFRESPONSE_DIFFCHANGES._serialized_start=2723
  _DIFFRESPONSE_DIFFCHANGES._serialized_end=2784
  _CREATEREQUEST._serialized_start=2786
  _CREATEREQUEST._serialized_end=2893
  _CREATERESPONSE._serialized_start=2895
  _CREATERESPONSE._serialized_end=2968
  _READREQUEST._serialized_start=2970
  _READREQUEST._serialized_end=3094
  _READRESPONSE._serialized_start=3096
  _READRESPONSE._serialized_end=3208
  _UPDATEREQUEST._serialized_start=3211
  _UPDATEREQUEST._serialized_end=3386
  _UPDATERESPONSE._serialized_start=3388
  _UPDATERESPONSE._serialized_end=3449
  _DELETEREQUEST._serialized_start=3451
  _DELETEREQUEST._serialized_end=3553
  _CONSTRUCTREQUEST._serialized_start=3556
  _CONSTRUCTREQUEST._serialized_end=4274
  _CONSTRUCTREQUEST_PROPERTYDEPENDENCIES._serialized_start=4033
  _CONSTRUCTREQUEST_PROPERTYDEPENDENCIES._serialized_end=4069
  _CONSTRUCTREQUEST_CONFIGENTRY._serialized_start=1418
  _CONSTRUCTREQUEST_CONFIGENTRY._serialized_end=1463
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._serialized_start=4118
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._serialized_end=4224
  _CONSTRUCTREQUEST_PROVIDERSENTRY._serialized_start=4226
  _CONSTRUCTREQUEST_PROVIDERSENTRY._serialized_end=4274
  _CONSTRUCTRESPONSE._serialized_start=4277
  _CONSTRUCTRESPONSE._serialized_end=4576
  _CONSTRUCTRESPONSE_PROPERTYDEPENDENCIES._serialized_start=4033
  _CONSTRUCTRESPONSE_PROPERTYDEPENDENCIES._serialized_end=4069
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._serialized_start=4469
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._serialized_end=4576
  _ERRORRESOURCEINITFAILED._serialized_start=4579
  _ERRORRESOURCEINITFAILED._serialized_end=4719
  _RESOURCEPROVIDER._serialized_start=4722
  _RESOURCEPROVIDER._serialized_end=5851
# @@protoc_insertion_point(module_scope)
