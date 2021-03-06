// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester
{
    public static class GetVolume
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
        ///         var ubuntu20_dev_mount_disk = Output.Create(Harvester.GetVolume.InvokeAsync(new Harvester.GetVolumeArgs
        ///         {
        ///             Name = "ubuntu20-dev-mount-disk",
        ///             Namespace = "default",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetVolumeResult> InvokeAsync(GetVolumeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVolumeResult>("harvester:index/getVolume:getVolume", args ?? new GetVolumeArgs(), options.WithDefaults());

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
        ///         var ubuntu20_dev_mount_disk = Output.Create(Harvester.GetVolume.InvokeAsync(new Harvester.GetVolumeArgs
        ///         {
        ///             Name = "ubuntu20-dev-mount-disk",
        ///             Namespace = "default",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetVolumeResult> Invoke(GetVolumeInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetVolumeResult>("harvester:index/getVolume:getVolume", args ?? new GetVolumeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVolumeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        [Input("namespace")]
        public string? Namespace { get; set; }

        public GetVolumeArgs()
        {
        }
    }

    public sealed class GetVolumeInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        public GetVolumeInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetVolumeResult
    {
        public readonly string AccessMode;
        public readonly string AttachedVm;
        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Image;
        /// <summary>
        /// A unique name
        /// </summary>
        public readonly string Name;
        public readonly string? Namespace;
        public readonly string Phase;
        public readonly string Size;
        public readonly string State;
        public readonly string StorageClassName;
        public readonly ImmutableDictionary<string, object> Tags;
        public readonly string VolumeMode;

        [OutputConstructor]
        private GetVolumeResult(
            string accessMode,

            string attachedVm,

            string description,

            string id,

            string image,

            string name,

            string? @namespace,

            string phase,

            string size,

            string state,

            string storageClassName,

            ImmutableDictionary<string, object> tags,

            string volumeMode)
        {
            AccessMode = accessMode;
            AttachedVm = attachedVm;
            Description = description;
            Id = id;
            Image = image;
            Name = name;
            Namespace = @namespace;
            Phase = phase;
            Size = size;
            State = state;
            StorageClassName = storageClassName;
            Tags = tags;
            VolumeMode = volumeMode;
        }
    }
}
