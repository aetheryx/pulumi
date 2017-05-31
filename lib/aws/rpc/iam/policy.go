// *** WARNING: this file was generated by the Lumi IDL Compiler (LUMIDL). ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
    "errors"

    pbempty "github.com/golang/protobuf/ptypes/empty"
    pbstruct "github.com/golang/protobuf/ptypes/struct"
    "golang.org/x/net/context"

    "github.com/pulumi/lumi/pkg/resource"
    "github.com/pulumi/lumi/pkg/tokens"
    "github.com/pulumi/lumi/pkg/util/contract"
    "github.com/pulumi/lumi/pkg/util/mapper"
    "github.com/pulumi/lumi/sdk/go/pkg/lumirpc"
)

/* Marshalable InlinePolicy structure(s) */

// InlinePolicy is a marshalable representation of its corresponding IDL type.
type InlinePolicy struct {
    PolicyDocument interface{} `json:"policyDocument"`
    PolicyName string `json:"policyName"`
}

// InlinePolicy's properties have constants to make dealing with diffs and property bags easier.
const (
    InlinePolicy_PolicyDocument = "policyDocument"
    InlinePolicy_PolicyName = "policyName"
)

/* RPC stubs for Policy resource provider */

// PolicyToken is the type token corresponding to the Policy package type.
const PolicyToken = tokens.Type("aws:iam/policy:Policy")

// PolicyProviderOps is a pluggable interface for Policy-related management functionality.
type PolicyProviderOps interface {
    Check(ctx context.Context, obj *Policy) ([]mapper.FieldError, error)
    Create(ctx context.Context, obj *Policy) (resource.ID, error)
    Get(ctx context.Context, id resource.ID) (*Policy, error)
    InspectChange(ctx context.Context,
        id resource.ID, old *Policy, new *Policy, diff *resource.ObjectDiff) ([]string, error)
    Update(ctx context.Context,
        id resource.ID, old *Policy, new *Policy, diff *resource.ObjectDiff) error
    Delete(ctx context.Context, id resource.ID) error
}

// PolicyProvider is a dynamic gRPC-based plugin for managing Policy resources.
type PolicyProvider struct {
    ops PolicyProviderOps
}

// NewPolicyProvider allocates a resource provider that delegates to a ops instance.
func NewPolicyProvider(ops PolicyProviderOps) lumirpc.ResourceProviderServer {
    contract.Assert(ops != nil)
    return &PolicyProvider{ops: ops}
}

func (p *PolicyProvider) Check(
    ctx context.Context, req *lumirpc.CheckRequest) (*lumirpc.CheckResponse, error) {
    contract.Assert(req.GetType() == string(PolicyToken))
    obj, _, decerr := p.Unmarshal(req.GetProperties())
    if decerr == nil || len(decerr.Failures()) == 0 {
        failures, err := p.ops.Check(ctx, obj)
        if err != nil {
            return nil, err
        }
        if len(failures) > 0 {
            decerr = mapper.NewDecodeErr(failures)
        }
    }
    return resource.NewCheckResponse(decerr), nil
}

func (p *PolicyProvider) Name(
    ctx context.Context, req *lumirpc.NameRequest) (*lumirpc.NameResponse, error) {
    contract.Assert(req.GetType() == string(PolicyToken))
    obj, _, decerr := p.Unmarshal(req.GetProperties())
    if decerr != nil {
        return nil, decerr
    }
    if obj.Name == "" {
        if req.Unknowns[Policy_Name] {
            return nil, errors.New("Name property cannot be computed from unknown outputs")
        }
        return nil, errors.New("Name property cannot be empty")
    }
    return &lumirpc.NameResponse{Name: obj.Name}, nil
}

func (p *PolicyProvider) Create(
    ctx context.Context, req *lumirpc.CreateRequest) (*lumirpc.CreateResponse, error) {
    contract.Assert(req.GetType() == string(PolicyToken))
    obj, _, decerr := p.Unmarshal(req.GetProperties())
    if decerr != nil {
        return nil, decerr
    }
    id, err := p.ops.Create(ctx, obj)
    if err != nil {
        return nil, err
    }
    return &lumirpc.CreateResponse{Id: string(id)}, nil
}

func (p *PolicyProvider) Get(
    ctx context.Context, req *lumirpc.GetRequest) (*lumirpc.GetResponse, error) {
    contract.Assert(req.GetType() == string(PolicyToken))
    id := resource.ID(req.GetId())
    obj, err := p.ops.Get(ctx, id)
    if err != nil {
        return nil, err
    }
    return &lumirpc.GetResponse{
        Properties: resource.MarshalProperties(
            nil, resource.NewPropertyMap(obj), resource.MarshalOptions{}),
    }, nil
}

func (p *PolicyProvider) InspectChange(
    ctx context.Context, req *lumirpc.InspectChangeRequest) (*lumirpc.InspectChangeResponse, error) {
    contract.Assert(req.GetType() == string(PolicyToken))
    id := resource.ID(req.GetId())
    old, oldprops, decerr := p.Unmarshal(req.GetOlds())
    if decerr != nil {
        return nil, decerr
    }
    new, newprops, decerr := p.Unmarshal(req.GetNews())
    if decerr != nil {
        return nil, decerr
    }
    var replaces []string
    diff := oldprops.Diff(newprops)
    if diff != nil {
        if diff.Changed("name") {
            replaces = append(replaces, "name")
        }
    }
    more, err := p.ops.InspectChange(ctx, id, old, new, diff)
    if err != nil {
        return nil, err
    }
    return &lumirpc.InspectChangeResponse{
        Replaces: append(replaces, more...),
    }, err
}

func (p *PolicyProvider) Update(
    ctx context.Context, req *lumirpc.UpdateRequest) (*pbempty.Empty, error) {
    contract.Assert(req.GetType() == string(PolicyToken))
    id := resource.ID(req.GetId())
    old, oldprops, err := p.Unmarshal(req.GetOlds())
    if err != nil {
        return nil, err
    }
    new, newprops, err := p.Unmarshal(req.GetNews())
    if err != nil {
        return nil, err
    }
    diff := oldprops.Diff(newprops)
    if err := p.ops.Update(ctx, id, old, new, diff); err != nil {
        return nil, err
    }
    return &pbempty.Empty{}, nil
}

func (p *PolicyProvider) Delete(
    ctx context.Context, req *lumirpc.DeleteRequest) (*pbempty.Empty, error) {
    contract.Assert(req.GetType() == string(PolicyToken))
    id := resource.ID(req.GetId())
    if err := p.ops.Delete(ctx, id); err != nil {
        return nil, err
    }
    return &pbempty.Empty{}, nil
}

func (p *PolicyProvider) Unmarshal(
    v *pbstruct.Struct) (*Policy, resource.PropertyMap, mapper.DecodeError) {
    var obj Policy
    props := resource.UnmarshalProperties(nil, v, resource.MarshalOptions{RawResources: true})
    result := mapper.MapIU(props.Mappable(), &obj)
    return &obj, props, result
}

/* Marshalable Policy structure(s) */

// Policy is a marshalable representation of its corresponding IDL type.
type Policy struct {
    Name string `json:"name"`
    PolicyDocument interface{} `json:"policyDocument"`
    PolicyName string `json:"policyName"`
    Groups *[]resource.ID `json:"groups,omitempty"`
    Roles *[]resource.ID `json:"roles,omitempty"`
    Users *[]resource.ID `json:"users,omitempty"`
}

// Policy's properties have constants to make dealing with diffs and property bags easier.
const (
    Policy_Name = "name"
    Policy_PolicyDocument = "policyDocument"
    Policy_PolicyName = "policyName"
    Policy_Groups = "groups"
    Policy_Roles = "roles"
    Policy_Users = "users"
)


