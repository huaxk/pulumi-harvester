// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester
{
    public static class GetSSHKey
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
        ///         var mysshkey = Output.Create(Harvester.GetSSHKey.InvokeAsync(new Harvester.GetSSHKeyArgs
        ///         {
        ///             Name = "mysshkey",
        ///             Namespace = "default",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSSHKeyResult> InvokeAsync(GetSSHKeyArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSSHKeyResult>("harvester:index/getSSHKey:getSSHKey", args ?? new GetSSHKeyArgs(), options.WithDefaults());

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
        ///         var mysshkey = Output.Create(Harvester.GetSSHKey.InvokeAsync(new Harvester.GetSSHKeyArgs
        ///         {
        ///             Name = "mysshkey",
        ///             Namespace = "default",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetSSHKeyResult> Invoke(GetSSHKeyInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSSHKeyResult>("harvester:index/getSSHKey:getSSHKey", args ?? new GetSSHKeyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSSHKeyArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        [Input("namespace")]
        public string? Namespace { get; set; }

        public GetSSHKeyArgs()
        {
        }
    }

    public sealed class GetSSHKeyInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        public GetSSHKeyInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSSHKeyResult
    {
        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        public readonly string Description;
        public readonly string Fingerprint;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A unique name
        /// </summary>
        public readonly string Name;
        public readonly string? Namespace;
        public readonly string PublicKey;
        public readonly string State;
        public readonly ImmutableDictionary<string, object> Tags;

        [OutputConstructor]
        private GetSSHKeyResult(
            string description,

            string fingerprint,

            string id,

            string name,

            string? @namespace,

            string publicKey,

            string state,

            ImmutableDictionary<string, object> tags)
        {
            Description = description;
            Fingerprint = fingerprint;
            Id = id;
            Name = name;
            Namespace = @namespace;
            PublicKey = publicKey;
            State = state;
            Tags = tags;
        }
    }
}
