// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./clusterNetwork";
export * from "./getClusterNetwork";
export * from "./getImage";
export * from "./getNetwork";
export * from "./getSSHKey";
export * from "./getVirtualMachine";
export * from "./getVolume";
export * from "./image";
export * from "./network";
export * from "./provider";
export * from "./sshkey";
export * from "./virtualMachine";
export * from "./volume";

// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

// Import resources to register:
import { ClusterNetwork } from "./clusterNetwork";
import { Image } from "./image";
import { Network } from "./network";
import { SSHKey } from "./sshkey";
import { VirtualMachine } from "./virtualMachine";
import { Volume } from "./volume";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "harvester:index/clusterNetwork:ClusterNetwork":
                return new ClusterNetwork(name, <any>undefined, { urn })
            case "harvester:index/image:Image":
                return new Image(name, <any>undefined, { urn })
            case "harvester:index/network:Network":
                return new Network(name, <any>undefined, { urn })
            case "harvester:index/sSHKey:SSHKey":
                return new SSHKey(name, <any>undefined, { urn })
            case "harvester:index/virtualMachine:VirtualMachine":
                return new VirtualMachine(name, <any>undefined, { urn })
            case "harvester:index/volume:Volume":
                return new Volume(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("harvester", "index/clusterNetwork", _module)
pulumi.runtime.registerResourceModule("harvester", "index/image", _module)
pulumi.runtime.registerResourceModule("harvester", "index/network", _module)
pulumi.runtime.registerResourceModule("harvester", "index/sSHKey", _module)
pulumi.runtime.registerResourceModule("harvester", "index/virtualMachine", _module)
pulumi.runtime.registerResourceModule("harvester", "index/volume", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("harvester", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:harvester") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
