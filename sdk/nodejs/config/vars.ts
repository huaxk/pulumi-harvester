// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("harvester");

/**
 * harvester kubeconfig
 */
export declare const kubeconfig: string | undefined;
Object.defineProperty(exports, "kubeconfig", {
    get() {
        return __config.get("kubeconfig");
    },
    enumerable: true,
});

