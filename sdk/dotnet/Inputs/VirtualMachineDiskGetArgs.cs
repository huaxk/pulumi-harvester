// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester.Inputs
{

    public sealed class VirtualMachineDiskGetArgs : Pulumi.ResourceArgs
    {
        [Input("accessMode")]
        public Input<string>? AccessMode { get; set; }

        [Input("autoDelete")]
        public Input<bool>? AutoDelete { get; set; }

        [Input("bootOrder")]
        public Input<int>? BootOrder { get; set; }

        [Input("bus")]
        public Input<string>? Bus { get; set; }

        [Input("containerImageName")]
        public Input<string>? ContainerImageName { get; set; }

        [Input("existingVolumeName")]
        public Input<string>? ExistingVolumeName { get; set; }

        [Input("image")]
        public Input<string>? Image { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("size")]
        public Input<string>? Size { get; set; }

        [Input("storageClassName")]
        public Input<string>? StorageClassName { get; set; }

        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("volumeMode")]
        public Input<string>? VolumeMode { get; set; }

        [Input("volumeName")]
        public Input<string>? VolumeName { get; set; }

        public VirtualMachineDiskGetArgs()
        {
        }
    }
}