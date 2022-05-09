// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester
{
    public static class GetNetwork
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Harvester = Pulumi.Harvester;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var vlan1 = Output.Create(Harvester.GetNetwork.InvokeAsync(new Harvester.GetNetworkArgs
        ///         {
        ///             Name = "vlan1",
        ///             Namespace = "harvester-public",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetNetworkResult> InvokeAsync(GetNetworkArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNetworkResult>("harvester:index/getNetwork:getNetwork", args ?? new GetNetworkArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Harvester = Pulumi.Harvester;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var vlan1 = Output.Create(Harvester.GetNetwork.InvokeAsync(new Harvester.GetNetworkArgs
        ///         {
        ///             Name = "vlan1",
        ///             Namespace = "harvester-public",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetNetworkResult> Invoke(GetNetworkInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetNetworkResult>("harvester:index/getNetwork:getNetwork", args ?? new GetNetworkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        [Input("namespace")]
        public string? Namespace { get; set; }

        public GetNetworkArgs()
        {
        }
    }

    public sealed class GetNetworkInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        public GetNetworkInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetNetworkResult
    {
        public readonly string Config;
        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A unique name
        /// </summary>
        public readonly string Name;
        public readonly string? Namespace;
        /// <summary>
        /// e.g. 172.16.0.1/24
        /// </summary>
        public readonly string RouteCidr;
        public readonly string RouteConnectivity;
        public readonly string RouteDhcpServerIp;
        /// <summary>
        /// e.g. 172.16.0.1
        /// </summary>
        public readonly string RouteGateway;
        public readonly string RouteMode;
        public readonly string State;
        public readonly ImmutableDictionary<string, object> Tags;
        /// <summary>
        /// e.g. 1-4094
        /// </summary>
        public readonly int VlanId;

        [OutputConstructor]
        private GetNetworkResult(
            string config,

            string description,

            string id,

            string name,

            string? @namespace,

            string routeCidr,

            string routeConnectivity,

            string routeDhcpServerIp,

            string routeGateway,

            string routeMode,

            string state,

            ImmutableDictionary<string, object> tags,

            int vlanId)
        {
            Config = config;
            Description = description;
            Id = id;
            Name = name;
            Namespace = @namespace;
            RouteCidr = routeCidr;
            RouteConnectivity = routeConnectivity;
            RouteDhcpServerIp = routeDhcpServerIp;
            RouteGateway = routeGateway;
            RouteMode = routeMode;
            State = state;
            Tags = tags;
            VlanId = vlanId;
        }
    }
}
