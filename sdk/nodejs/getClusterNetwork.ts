// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as harvester from "@pulumi/harvester";
 *
 * const vlan = pulumi.output(harvester.getClusterNetwork({
 *     name: "vlan",
 * }));
 * ```
 */
export function getClusterNetwork(args: GetClusterNetworkArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterNetworkResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("harvester:index/getClusterNetwork:getClusterNetwork", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getClusterNetwork.
 */
export interface GetClusterNetworkArgs {
    /**
     * A unique name
     */
    name: string;
}

/**
 * A collection of values returned by getClusterNetwork.
 */
export interface GetClusterNetworkResult {
    readonly defaultPhysicalNic: string;
    /**
     * Any text you want that better describes this resource
     */
    readonly description: string;
    readonly enable: boolean;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A unique name
     */
    readonly name: string;
    readonly state: string;
    readonly tags: {[key: string]: any};
}

export function getClusterNetworkOutput(args: GetClusterNetworkOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetClusterNetworkResult> {
    return pulumi.output(args).apply(a => getClusterNetwork(a, opts))
}

/**
 * A collection of arguments for invoking getClusterNetwork.
 */
export interface GetClusterNetworkOutputArgs {
    /**
     * A unique name
     */
    name: pulumi.Input<string>;
}
