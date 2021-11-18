// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester
{
    [HarvesterResourceType("harvester:index/volume:Volume")]
    public partial class Volume : Pulumi.CustomResource
    {
        [Output("accessMode")]
        public Output<string?> AccessMode { get; private set; } = null!;

        [Output("attachedVm")]
        public Output<string> AttachedVm { get; private set; } = null!;

        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("image")]
        public Output<string?> Image { get; private set; } = null!;

        /// <summary>
        /// A unique name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("namespace")]
        public Output<string?> Namespace { get; private set; } = null!;

        [Output("phase")]
        public Output<string> Phase { get; private set; } = null!;

        [Output("size")]
        public Output<string?> Size { get; private set; } = null!;

        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        [Output("storageClassName")]
        public Output<string> StorageClassName { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        [Output("volumeMode")]
        public Output<string?> VolumeMode { get; private set; } = null!;


        /// <summary>
        /// Create a Volume resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Volume(string name, VolumeArgs? args = null, CustomResourceOptions? options = null)
            : base("harvester:index/volume:Volume", name, args ?? new VolumeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Volume(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
            : base("harvester:index/volume:Volume", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Volume resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Volume Get(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
        {
            return new Volume(name, id, state, options);
        }
    }

    public sealed class VolumeArgs : Pulumi.ResourceArgs
    {
        [Input("accessMode")]
        public Input<string>? AccessMode { get; set; }

        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("image")]
        public Input<string>? Image { get; set; }

        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        [Input("size")]
        public Input<string>? Size { get; set; }

        [Input("storageClassName")]
        public Input<string>? StorageClassName { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        [Input("volumeMode")]
        public Input<string>? VolumeMode { get; set; }

        public VolumeArgs()
        {
        }
    }

    public sealed class VolumeState : Pulumi.ResourceArgs
    {
        [Input("accessMode")]
        public Input<string>? AccessMode { get; set; }

        [Input("attachedVm")]
        public Input<string>? AttachedVm { get; set; }

        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("image")]
        public Input<string>? Image { get; set; }

        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        [Input("phase")]
        public Input<string>? Phase { get; set; }

        [Input("size")]
        public Input<string>? Size { get; set; }

        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("storageClassName")]
        public Input<string>? StorageClassName { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        [Input("volumeMode")]
        public Input<string>? VolumeMode { get; set; }

        public VolumeState()
        {
        }
    }
}
