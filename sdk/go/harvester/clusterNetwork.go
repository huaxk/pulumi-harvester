// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package harvester

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ClusterNetwork struct {
	pulumi.CustomResourceState

	DefaultPhysicalNic pulumi.StringPtrOutput `pulumi:"defaultPhysicalNic"`
	// Any text you want that better describes this resource
	Description pulumi.StringPtrOutput `pulumi:"description"`
	Enable      pulumi.BoolOutput      `pulumi:"enable"`
	// A unique name
	Name  pulumi.StringOutput `pulumi:"name"`
	State pulumi.StringOutput `pulumi:"state"`
	Tags  pulumi.MapOutput    `pulumi:"tags"`
}

// NewClusterNetwork registers a new resource with the given unique name, arguments, and options.
func NewClusterNetwork(ctx *pulumi.Context,
	name string, args *ClusterNetworkArgs, opts ...pulumi.ResourceOption) (*ClusterNetwork, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Enable == nil {
		return nil, errors.New("invalid value for required argument 'Enable'")
	}
	var resource ClusterNetwork
	err := ctx.RegisterResource("harvester:index/clusterNetwork:ClusterNetwork", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetClusterNetwork gets an existing ClusterNetwork resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetClusterNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterNetworkState, opts ...pulumi.ResourceOption) (*ClusterNetwork, error) {
	var resource ClusterNetwork
	err := ctx.ReadResource("harvester:index/clusterNetwork:ClusterNetwork", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ClusterNetwork resources.
type clusterNetworkState struct {
	DefaultPhysicalNic *string `pulumi:"defaultPhysicalNic"`
	// Any text you want that better describes this resource
	Description *string `pulumi:"description"`
	Enable      *bool   `pulumi:"enable"`
	// A unique name
	Name  *string                `pulumi:"name"`
	State *string                `pulumi:"state"`
	Tags  map[string]interface{} `pulumi:"tags"`
}

type ClusterNetworkState struct {
	DefaultPhysicalNic pulumi.StringPtrInput
	// Any text you want that better describes this resource
	Description pulumi.StringPtrInput
	Enable      pulumi.BoolPtrInput
	// A unique name
	Name  pulumi.StringPtrInput
	State pulumi.StringPtrInput
	Tags  pulumi.MapInput
}

func (ClusterNetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterNetworkState)(nil)).Elem()
}

type clusterNetworkArgs struct {
	DefaultPhysicalNic *string `pulumi:"defaultPhysicalNic"`
	// Any text you want that better describes this resource
	Description *string `pulumi:"description"`
	Enable      bool    `pulumi:"enable"`
	// A unique name
	Name *string                `pulumi:"name"`
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a ClusterNetwork resource.
type ClusterNetworkArgs struct {
	DefaultPhysicalNic pulumi.StringPtrInput
	// Any text you want that better describes this resource
	Description pulumi.StringPtrInput
	Enable      pulumi.BoolInput
	// A unique name
	Name pulumi.StringPtrInput
	Tags pulumi.MapInput
}

func (ClusterNetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterNetworkArgs)(nil)).Elem()
}

type ClusterNetworkInput interface {
	pulumi.Input

	ToClusterNetworkOutput() ClusterNetworkOutput
	ToClusterNetworkOutputWithContext(ctx context.Context) ClusterNetworkOutput
}

func (*ClusterNetwork) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterNetwork)(nil))
}

func (i *ClusterNetwork) ToClusterNetworkOutput() ClusterNetworkOutput {
	return i.ToClusterNetworkOutputWithContext(context.Background())
}

func (i *ClusterNetwork) ToClusterNetworkOutputWithContext(ctx context.Context) ClusterNetworkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterNetworkOutput)
}

func (i *ClusterNetwork) ToClusterNetworkPtrOutput() ClusterNetworkPtrOutput {
	return i.ToClusterNetworkPtrOutputWithContext(context.Background())
}

func (i *ClusterNetwork) ToClusterNetworkPtrOutputWithContext(ctx context.Context) ClusterNetworkPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterNetworkPtrOutput)
}

type ClusterNetworkPtrInput interface {
	pulumi.Input

	ToClusterNetworkPtrOutput() ClusterNetworkPtrOutput
	ToClusterNetworkPtrOutputWithContext(ctx context.Context) ClusterNetworkPtrOutput
}

type clusterNetworkPtrType ClusterNetworkArgs

func (*clusterNetworkPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterNetwork)(nil))
}

func (i *clusterNetworkPtrType) ToClusterNetworkPtrOutput() ClusterNetworkPtrOutput {
	return i.ToClusterNetworkPtrOutputWithContext(context.Background())
}

func (i *clusterNetworkPtrType) ToClusterNetworkPtrOutputWithContext(ctx context.Context) ClusterNetworkPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterNetworkPtrOutput)
}

// ClusterNetworkArrayInput is an input type that accepts ClusterNetworkArray and ClusterNetworkArrayOutput values.
// You can construct a concrete instance of `ClusterNetworkArrayInput` via:
//
//          ClusterNetworkArray{ ClusterNetworkArgs{...} }
type ClusterNetworkArrayInput interface {
	pulumi.Input

	ToClusterNetworkArrayOutput() ClusterNetworkArrayOutput
	ToClusterNetworkArrayOutputWithContext(context.Context) ClusterNetworkArrayOutput
}

type ClusterNetworkArray []ClusterNetworkInput

func (ClusterNetworkArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ClusterNetwork)(nil)).Elem()
}

func (i ClusterNetworkArray) ToClusterNetworkArrayOutput() ClusterNetworkArrayOutput {
	return i.ToClusterNetworkArrayOutputWithContext(context.Background())
}

func (i ClusterNetworkArray) ToClusterNetworkArrayOutputWithContext(ctx context.Context) ClusterNetworkArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterNetworkArrayOutput)
}

// ClusterNetworkMapInput is an input type that accepts ClusterNetworkMap and ClusterNetworkMapOutput values.
// You can construct a concrete instance of `ClusterNetworkMapInput` via:
//
//          ClusterNetworkMap{ "key": ClusterNetworkArgs{...} }
type ClusterNetworkMapInput interface {
	pulumi.Input

	ToClusterNetworkMapOutput() ClusterNetworkMapOutput
	ToClusterNetworkMapOutputWithContext(context.Context) ClusterNetworkMapOutput
}

type ClusterNetworkMap map[string]ClusterNetworkInput

func (ClusterNetworkMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ClusterNetwork)(nil)).Elem()
}

func (i ClusterNetworkMap) ToClusterNetworkMapOutput() ClusterNetworkMapOutput {
	return i.ToClusterNetworkMapOutputWithContext(context.Background())
}

func (i ClusterNetworkMap) ToClusterNetworkMapOutputWithContext(ctx context.Context) ClusterNetworkMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterNetworkMapOutput)
}

type ClusterNetworkOutput struct{ *pulumi.OutputState }

func (ClusterNetworkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterNetwork)(nil))
}

func (o ClusterNetworkOutput) ToClusterNetworkOutput() ClusterNetworkOutput {
	return o
}

func (o ClusterNetworkOutput) ToClusterNetworkOutputWithContext(ctx context.Context) ClusterNetworkOutput {
	return o
}

func (o ClusterNetworkOutput) ToClusterNetworkPtrOutput() ClusterNetworkPtrOutput {
	return o.ToClusterNetworkPtrOutputWithContext(context.Background())
}

func (o ClusterNetworkOutput) ToClusterNetworkPtrOutputWithContext(ctx context.Context) ClusterNetworkPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ClusterNetwork) *ClusterNetwork {
		return &v
	}).(ClusterNetworkPtrOutput)
}

type ClusterNetworkPtrOutput struct{ *pulumi.OutputState }

func (ClusterNetworkPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterNetwork)(nil))
}

func (o ClusterNetworkPtrOutput) ToClusterNetworkPtrOutput() ClusterNetworkPtrOutput {
	return o
}

func (o ClusterNetworkPtrOutput) ToClusterNetworkPtrOutputWithContext(ctx context.Context) ClusterNetworkPtrOutput {
	return o
}

func (o ClusterNetworkPtrOutput) Elem() ClusterNetworkOutput {
	return o.ApplyT(func(v *ClusterNetwork) ClusterNetwork {
		if v != nil {
			return *v
		}
		var ret ClusterNetwork
		return ret
	}).(ClusterNetworkOutput)
}

type ClusterNetworkArrayOutput struct{ *pulumi.OutputState }

func (ClusterNetworkArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ClusterNetwork)(nil))
}

func (o ClusterNetworkArrayOutput) ToClusterNetworkArrayOutput() ClusterNetworkArrayOutput {
	return o
}

func (o ClusterNetworkArrayOutput) ToClusterNetworkArrayOutputWithContext(ctx context.Context) ClusterNetworkArrayOutput {
	return o
}

func (o ClusterNetworkArrayOutput) Index(i pulumi.IntInput) ClusterNetworkOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ClusterNetwork {
		return vs[0].([]ClusterNetwork)[vs[1].(int)]
	}).(ClusterNetworkOutput)
}

type ClusterNetworkMapOutput struct{ *pulumi.OutputState }

func (ClusterNetworkMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]ClusterNetwork)(nil))
}

func (o ClusterNetworkMapOutput) ToClusterNetworkMapOutput() ClusterNetworkMapOutput {
	return o
}

func (o ClusterNetworkMapOutput) ToClusterNetworkMapOutputWithContext(ctx context.Context) ClusterNetworkMapOutput {
	return o
}

func (o ClusterNetworkMapOutput) MapIndex(k pulumi.StringInput) ClusterNetworkOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) ClusterNetwork {
		return vs[0].(map[string]ClusterNetwork)[vs[1].(string)]
	}).(ClusterNetworkOutput)
}

func init() {
	pulumi.RegisterOutputType(ClusterNetworkOutput{})
	pulumi.RegisterOutputType(ClusterNetworkPtrOutput{})
	pulumi.RegisterOutputType(ClusterNetworkArrayOutput{})
	pulumi.RegisterOutputType(ClusterNetworkMapOutput{})
}
