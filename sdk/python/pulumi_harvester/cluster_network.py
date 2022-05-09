# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ClusterNetworkArgs', 'ClusterNetwork']

@pulumi.input_type
class ClusterNetworkArgs:
    def __init__(__self__, *,
                 enable: pulumi.Input[bool],
                 default_physical_nic: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a ClusterNetwork resource.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        pulumi.set(__self__, "enable", enable)
        if default_physical_nic is not None:
            pulumi.set(__self__, "default_physical_nic", default_physical_nic)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter(name="defaultPhysicalNic")
    def default_physical_nic(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_physical_nic")

    @default_physical_nic.setter
    def default_physical_nic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_physical_nic", value)

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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ClusterNetworkState:
    def __init__(__self__, *,
                 default_physical_nic: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering ClusterNetwork resources.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        if default_physical_nic is not None:
            pulumi.set(__self__, "default_physical_nic", default_physical_nic)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="defaultPhysicalNic")
    def default_physical_nic(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_physical_nic")

    @default_physical_nic.setter
    def default_physical_nic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_physical_nic", value)

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
    def enable(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable", value)

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
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class ClusterNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_physical_nic: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        ## Import

        # There is a vlan clusternetwork in Harvester clusters by default # Import it before manage it # And don't destroy it after imported

        ```sh
         $ pulumi import harvester:index/clusterNetwork:ClusterNetwork vlan vlan
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        # There is a vlan clusternetwork in Harvester clusters by default # Import it before manage it # And don't destroy it after imported

        ```sh
         $ pulumi import harvester:index/clusterNetwork:ClusterNetwork vlan vlan
        ```

        :param str resource_name: The name of the resource.
        :param ClusterNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_physical_nic: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = ClusterNetworkArgs.__new__(ClusterNetworkArgs)

            __props__.__dict__["default_physical_nic"] = default_physical_nic
            __props__.__dict__["description"] = description
            if enable is None and not opts.urn:
                raise TypeError("Missing required property 'enable'")
            __props__.__dict__["enable"] = enable
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["state"] = None
        super(ClusterNetwork, __self__).__init__(
            'harvester:index/clusterNetwork:ClusterNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_physical_nic: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'ClusterNetwork':
        """
        Get an existing ClusterNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Any text you want that better describes this resource
        :param pulumi.Input[str] name: A unique name
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterNetworkState.__new__(_ClusterNetworkState)

        __props__.__dict__["default_physical_nic"] = default_physical_nic
        __props__.__dict__["description"] = description
        __props__.__dict__["enable"] = enable
        __props__.__dict__["name"] = name
        __props__.__dict__["state"] = state
        __props__.__dict__["tags"] = tags
        return ClusterNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultPhysicalNic")
    def default_physical_nic(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_physical_nic")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Any text you want that better describes this resource
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

