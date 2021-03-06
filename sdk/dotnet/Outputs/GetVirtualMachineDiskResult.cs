// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester.Outputs
{

    [OutputType]
    public sealed class GetVirtualMachineDiskResult
    {
        public readonly string AccessMode;
        public readonly bool AutoDelete;
        public readonly int? BootOrder;
        public readonly string Bus;
        public readonly string? ContainerImageName;
        public readonly string? ExistingVolumeName;
        public readonly bool HotPlug;
        public readonly string? Image;
        /// <summary>
        /// A unique name
        /// </summary>
        public readonly string Name;
        public readonly string? Size;
        public readonly string StorageClassName;
        public readonly string? Type;
        public readonly string VolumeMode;
        public readonly string VolumeName;

        [OutputConstructor]
        private GetVirtualMachineDiskResult(
            string accessMode,

            bool autoDelete,

            int? bootOrder,

            string bus,

            string? containerImageName,

            string? existingVolumeName,

            bool hotPlug,

            string? image,

            string name,

            string? size,

            string storageClassName,

            string? type,

            string volumeMode,

            string volumeName)
        {
            AccessMode = accessMode;
            AutoDelete = autoDelete;
            BootOrder = bootOrder;
            Bus = bus;
            ContainerImageName = containerImageName;
            ExistingVolumeName = existingVolumeName;
            HotPlug = hotPlug;
            Image = image;
            Name = name;
            Size = size;
            StorageClassName = storageClassName;
            Type = type;
            VolumeMode = volumeMode;
            VolumeName = volumeName;
        }
    }
}
