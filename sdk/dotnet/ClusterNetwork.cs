// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester
{
    /// <summary>
    /// ## Import
    /// 
    /// # There is a vlan clusternetwork in Harvester clusters by default # Import it before manage it # And don't destroy it after imported
    /// 
    /// ```sh
    ///  $ pulumi import harvester:index/clusterNetwork:ClusterNetwork vlan vlan
    /// ```
    /// </summary>
    [HarvesterResourceType("harvester:index/clusterNetwork:ClusterNetwork")]
    public partial class ClusterNetwork : Pulumi.CustomResource
    {
        [Output("defaultPhysicalNic")]
        public Output<string?> DefaultPhysicalNic { get; private set; } = null!;

        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("enable")]
        public Output<bool> Enable { get; private set; } = null!;

        /// <summary>
        /// A unique name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterNetwork resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterNetwork(string name, ClusterNetworkArgs args, CustomResourceOptions? options = null)
            : base("harvester:index/clusterNetwork:ClusterNetwork", name, args ?? new ClusterNetworkArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ClusterNetwork(string name, Input<string> id, ClusterNetworkState? state = null, CustomResourceOptions? options = null)
            : base("harvester:index/clusterNetwork:ClusterNetwork", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ClusterNetwork resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterNetwork Get(string name, Input<string> id, ClusterNetworkState? state = null, CustomResourceOptions? options = null)
        {
            return new ClusterNetwork(name, id, state, options);
        }
    }

    public sealed class ClusterNetworkArgs : Pulumi.ResourceArgs
    {
        [Input("defaultPhysicalNic")]
        public Input<string>? DefaultPhysicalNic { get; set; }

        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("enable", required: true)]
        public Input<bool> Enable { get; set; } = null!;

        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ClusterNetworkArgs()
        {
        }
    }

    public sealed class ClusterNetworkState : Pulumi.ResourceArgs
    {
        [Input("defaultPhysicalNic")]
        public Input<string>? DefaultPhysicalNic { get; set; }

        /// <summary>
        /// Any text you want that better describes this resource
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("enable")]
        public Input<bool>? Enable { get; set; }

        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ClusterNetworkState()
        {
        }
    }
}
