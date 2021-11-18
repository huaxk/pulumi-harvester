# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 access_mode: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 storage_class_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 volume_mode: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        if access_mode is not None:
            pulumi.set(__self__, "access_mode", access_mode)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if storage_class_name is not None:
            pulumi.set(__self__, "storage_class_name", storage_class_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if volume_mode is not None:
            pulumi.set(__self__, "volume_mode", volume_mode)

    @property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "access_mode")

    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_mode", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Any text you want that better describes this resource
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="storageClassName")
    def storage_class_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_class_name")

    @storage_class_name.setter
    def storage_class_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_class_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="volumeMode")
    def volume_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume_mode")

    @volume_mode.setter
    def volume_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_mode", value)


@pulumi.input_type
class _VolumeState:
    def __init__(__self__, *,
                 access_mode: Optional[pulumi.Input[str]] = None,
                 attached_vm: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 phase: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 storage_class_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 volume_mode: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Volume resources.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        if access_mode is not None:
            pulumi.set(__self__, "access_mode", access_mode)
        if attached_vm is not None:
            pulumi.set(__self__, "attached_vm", attached_vm)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if phase is not None:
            pulumi.set(__self__, "phase", phase)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if storage_class_name is not None:
            pulumi.set(__self__, "storage_class_name", storage_class_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if volume_mode is not None:
            pulumi.set(__self__, "volume_mode", volume_mode)

    @property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "access_mode")

    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_mode", value)

    @property
    @pulumi.getter(name="attachedVm")
    def attached_vm(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "attached_vm")

    @attached_vm.setter
    def attached_vm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attached_vm", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Any text you want that better describes this resource
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def phase(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "phase")

    @phase.setter
    def phase(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phase", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="storageClassName")
    def storage_class_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_class_name")

    @storage_class_name.setter
    def storage_class_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_class_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="volumeMode")
    def volume_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume_mode")

    @volume_mode.setter
    def volume_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_mode", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_mode: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 storage_class_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 volume_mode: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Volume resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VolumeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Volume resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_mode: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 storage_class_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 volume_mode: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            __props__.__dict__["access_mode"] = access_mode
            __props__.__dict__["description"] = description
            __props__.__dict__["image"] = image
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["size"] = size
            __props__.__dict__["storage_class_name"] = storage_class_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["volume_mode"] = volume_mode
            __props__.__dict__["attached_vm"] = None
            __props__.__dict__["phase"] = None
            __props__.__dict__["state"] = None
        super(Volume, __self__).__init__(
            'harvester:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_mode: Optional[pulumi.Input[str]] = None,
            attached_vm: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            image: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            phase: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            storage_class_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            volume_mode: Optional[pulumi.Input[str]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeState.__new__(_VolumeState)

        __props__.__dict__["access_mode"] = access_mode
        __props__.__dict__["attached_vm"] = attached_vm
        __props__.__dict__["description"] = description
        __props__.__dict__["image"] = image
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["phase"] = phase
        __props__.__dict__["size"] = size
        __props__.__dict__["state"] = state
        __props__.__dict__["storage_class_name"] = storage_class_name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["volume_mode"] = volume_mode
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "access_mode")

    @property
    @pulumi.getter(name="attachedVm")
    def attached_vm(self) -> pulumi.Output[str]:
        return pulumi.get(self, "attached_vm")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Any text you want that better describes this resource
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def image(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def phase(self) -> pulumi.Output[str]:
        return pulumi.get(self, "phase")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageClassName")
    def storage_class_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "storage_class_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="volumeMode")
    def volume_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "volume_mode")

