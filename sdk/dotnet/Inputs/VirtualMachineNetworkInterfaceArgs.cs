// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Harvester.Inputs
{

    public sealed class VirtualMachineNetworkInterfaceArgs : Pulumi.ResourceArgs
    {
        [Input("interfaceName")]
        public Input<string>? InterfaceName { get; set; }

        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        [Input("model")]
        public Input<string>? Model { get; set; }

        /// <summary>
        /// A unique name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("networkName")]
        public Input<string>? NetworkName { get; set; }

        [Input("type")]
        public Input<string>? Type { get; set; }

        public VirtualMachineNetworkInterfaceArgs()
        {
        }
    }
}
