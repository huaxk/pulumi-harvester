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
 * const mysshkey = pulumi.output(harvester.getSSHKey({
 *     name: "mysshkey",
 *     namespace: "default",
 * }));
 * ```
 */
export function getSSHKey(args: GetSSHKeyArgs, opts?: pulumi.InvokeOptions): Promise<GetSSHKeyResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("harvester:index/getSSHKey:getSSHKey", {
        "name": args.name,
        "namespace": args.namespace,
    }, opts);
}

/**
 * A collection of arguments for invoking getSSHKey.
 */
export interface GetSSHKeyArgs {
    /**
     * A unique name
     */
    name: string;
    namespace?: string;
}

/**
 * A collection of values returned by getSSHKey.
 */
export interface GetSSHKeyResult {
    /**
     * Any text you want that better describes this resource
     */
    readonly description: string;
    readonly fingerprint: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A unique name
     */
    readonly name: string;
    readonly namespace?: string;
    readonly publicKey: string;
    readonly state: string;
    readonly tags: {[key: string]: any};
}

export function getSSHKeyOutput(args: GetSSHKeyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSSHKeyResult> {
    return pulumi.output(args).apply(a => getSSHKey(a, opts))
}

/**
 * A collection of arguments for invoking getSSHKey.
 */
export interface GetSSHKeyOutputArgs {
    /**
     * A unique name
     */
    name: pulumi.Input<string>;
    namespace?: pulumi.Input<string>;
}
