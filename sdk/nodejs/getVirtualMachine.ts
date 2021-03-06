// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as harvester from "@pulumi/harvester";
 *
 * const ubuntu20_dev = pulumi.output(harvester.getVirtualMachine({
 *     name: "ubuntu-dev",
 *     namespace: "default",
 * }));
 * ```
 */
export function getVirtualMachine(args: GetVirtualMachineArgs, opts?: pulumi.InvokeOptions): Promise<GetVirtualMachineResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("harvester:index/getVirtualMachine:getVirtualMachine", {
        "name": args.name,
        "namespace": args.namespace,
    }, opts);
}

/**
 * A collection of arguments for invoking getVirtualMachine.
 */
export interface GetVirtualMachineArgs {
    /**
     * A unique name
     */
    name: string;
    namespace?: string;
}

/**
 * A collection of values returned by getVirtualMachine.
 */
export interface GetVirtualMachineResult {
    readonly cloudinits: outputs.GetVirtualMachineCloudinit[];
    readonly cpu: number;
    /**
     * Any text you want that better describes this resource
     */
    readonly description: string;
    readonly disks: outputs.GetVirtualMachineDisk[];
    readonly hostname: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly machineType: string;
    readonly memory: string;
    /**
     * A unique name
     */
    readonly name: string;
    readonly namespace?: string;
    readonly networkInterfaces: outputs.GetVirtualMachineNetworkInterface[];
    readonly nodeName: string;
    readonly sshKeys: string[];
    readonly start: boolean;
    readonly state: string;
    readonly tags: {[key: string]: any};
}

export function getVirtualMachineOutput(args: GetVirtualMachineOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVirtualMachineResult> {
    return pulumi.output(args).apply(a => getVirtualMachine(a, opts))
}

/**
 * A collection of arguments for invoking getVirtualMachine.
 */
export interface GetVirtualMachineOutputArgs {
    /**
     * A unique name
     */
    name: pulumi.Input<string>;
    namespace?: pulumi.Input<string>;
}
