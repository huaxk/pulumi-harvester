// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Image extends pulumi.CustomResource {
    /**
     * Get an existing Image resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ImageState, opts?: pulumi.CustomResourceOptions): Image {
        return new Image(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'harvester:index/image:Image';

    /**
     * Returns true if the given object is an instance of Image.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Image {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Image.__pulumiType;
    }

    /**
     * Any text you want that better describes this resource
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly displayName!: pulumi.Output<string>;
    /**
     * A unique name
     */
    public readonly name!: pulumi.Output<string>;
    public readonly namespace!: pulumi.Output<string | undefined>;
    public /*out*/ readonly progress!: pulumi.Output<number>;
    public /*out*/ readonly size!: pulumi.Output<number>;
    public readonly sourceType!: pulumi.Output<string>;
    public /*out*/ readonly state!: pulumi.Output<string>;
    public /*out*/ readonly storageClassName!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * supports the `raw` and `qcow2` image formats which are supported by
     * [qemu](https://www.qemu.org/docs/master/system/images.html#disk-image-file-formats). Bootable ISO images can also be
     * used and are treated like `raw` images.
     */
    public readonly url!: pulumi.Output<string | undefined>;

    /**
     * Create a Image resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ImageArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ImageArgs | ImageState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ImageState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["namespace"] = state ? state.namespace : undefined;
            inputs["progress"] = state ? state.progress : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["sourceType"] = state ? state.sourceType : undefined;
            inputs["state"] = state ? state.state : undefined;
            inputs["storageClassName"] = state ? state.storageClassName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as ImageArgs | undefined;
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            if ((!args || args.sourceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceType'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["namespace"] = args ? args.namespace : undefined;
            inputs["sourceType"] = args ? args.sourceType : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["url"] = args ? args.url : undefined;
            inputs["progress"] = undefined /*out*/;
            inputs["size"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["storageClassName"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Image.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Image resources.
 */
export interface ImageState {
    /**
     * Any text you want that better describes this resource
     */
    description?: pulumi.Input<string>;
    displayName?: pulumi.Input<string>;
    /**
     * A unique name
     */
    name?: pulumi.Input<string>;
    namespace?: pulumi.Input<string>;
    progress?: pulumi.Input<number>;
    size?: pulumi.Input<number>;
    sourceType?: pulumi.Input<string>;
    state?: pulumi.Input<string>;
    storageClassName?: pulumi.Input<string>;
    tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * supports the `raw` and `qcow2` image formats which are supported by
     * [qemu](https://www.qemu.org/docs/master/system/images.html#disk-image-file-formats). Bootable ISO images can also be
     * used and are treated like `raw` images.
     */
    url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Image resource.
 */
export interface ImageArgs {
    /**
     * Any text you want that better describes this resource
     */
    description?: pulumi.Input<string>;
    displayName: pulumi.Input<string>;
    /**
     * A unique name
     */
    name?: pulumi.Input<string>;
    namespace?: pulumi.Input<string>;
    sourceType: pulumi.Input<string>;
    tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * supports the `raw` and `qcow2` image formats which are supported by
     * [qemu](https://www.qemu.org/docs/master/system/images.html#disk-image-file-formats). Bootable ISO images can also be
     * used and are treated like `raw` images.
     */
    url?: pulumi.Input<string>;
}