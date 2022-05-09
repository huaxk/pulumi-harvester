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
    public sealed class VirtualMachineNetworkInterface
    {
        public readonly string? InterfaceName;
        public readonly string? IpAddress;
        public readonly string? MacAddress;
        public readonly string? Model;
        /// <summary>
        /// A unique name
        /// </summary>
        public readonly string Name;
        public readonly string? NetworkName;
        public readonly string? Type;

        [OutputConstructor]
        private VirtualMachineNetworkInterface(
            string? interfaceName,

            string? ipAddress,

            string? macAddress,

            string? model,

            string name,

            string? networkName,

            string? type)
        {
            InterfaceName = interfaceName;
            IpAddress = ipAddress;
            MacAddress = macAddress;
            Model = model;
            Name = name;
            NetworkName = networkName;
            Type = type;
        }
    }
}
