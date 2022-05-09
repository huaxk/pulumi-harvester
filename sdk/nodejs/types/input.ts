// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface VirtualMachineCloudinit {
    networkData?: pulumi.Input<string>;
    networkDataBase64?: pulumi.Input<string>;
    networkDataSecretName?: pulumi.Input<string>;
    type?: pulumi.Input<string>;
    userData?: pulumi.Input<string>;
    userDataBase64?: pulumi.Input<string>;
    userDataSecretName?: pulumi.Input<string>;
}

export interface VirtualMachineDisk {
    accessMode?: pulumi.Input<string>;
    autoDelete?: pulumi.Input<boolean>;
    bootOrder?: pulumi.Input<number>;
    bus?: pulumi.Input<string>;
    containerImageName?: pulumi.Input<string>;
    existingVolumeName?: pulumi.Input<string>;
    hotPlug?: pulumi.Input<boolean>;
    image?: pulumi.Input<string>;
    /**
     * A unique name
     */
    name: pulumi.Input<string>;
    size?: pulumi.Input<string>;
    storageClassName?: pulumi.Input<string>;
    type?: pulumi.Input<string>;
    volumeMode?: pulumi.Input<string>;
    volumeName?: pulumi.Input<string>;
}

export interface VirtualMachineNetworkInterface {
    interfaceName?: pulumi.Input<string>;
    ipAddress?: pulumi.Input<string>;
    macAddress?: pulumi.Input<string>;
    model?: pulumi.Input<string>;
    /**
     * A unique name
     */
    name: pulumi.Input<string>;
    networkName?: pulumi.Input<string>;
    type?: pulumi.Input<string>;
}
