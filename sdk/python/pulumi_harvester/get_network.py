# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetNetworkResult',
    'AwaitableGetNetworkResult',
    'get_network',
    'get_network_output',
]

@pulumi.output_type
class GetNetworkResult:
    """
    A collection of values returned by getNetwork.
    """
    def __init__(__self__, config=None, description=None, id=None, name=None, namespace=None, route_cidr=None, route_connectivity=None, route_dhcp_server_ip=None, route_gateway=None, route_mode=None, state=None, tags=None, vlan_id=None):
        if config and not isinstance(config, str):
            raise TypeError("Expected argument 'config' to be a str")
        pulumi.set(__self__, "config", config)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if route_cidr and not isinstance(route_cidr, str):
            raise TypeError("Expected argument 'route_cidr' to be a str")
        pulumi.set(__self__, "route_cidr", route_cidr)
        if route_connectivity and not isinstance(route_connectivity, str):
            raise TypeError("Expected argument 'route_connectivity' to be a str")
        pulumi.set(__self__, "route_connectivity", route_connectivity)
        if route_dhcp_server_ip and not isinstance(route_dhcp_server_ip, str):
            raise TypeError("Expected argument 'route_dhcp_server_ip' to be a str")
        pulumi.set(__self__, "route_dhcp_server_ip", route_dhcp_server_ip)
        if route_gateway and not isinstance(route_gateway, str):
            raise TypeError("Expected argument 'route_gateway' to be a str")
        pulumi.set(__self__, "route_gateway", route_gateway)
        if route_mode and not isinstance(route_mode, str):
            raise TypeError("Expected argument 'route_mode' to be a str")
        pulumi.set(__self__, "route_mode", route_mode)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vlan_id and not isinstance(vlan_id, int):
            raise TypeError("Expected argument 'vlan_id' to be a int")
        pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter
    def config(self) -> str:
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Any text you want that better describes this resource
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="routeCidr")
    def route_cidr(self) -> str:
        """
        e.g. 172.16.0.1/24
        """
        return pulumi.get(self, "route_cidr")

    @property
    @pulumi.getter(name="routeConnectivity")
    def route_connectivity(self) -> str:
        return pulumi.get(self, "route_connectivity")

    @property
    @pulumi.getter(name="routeDhcpServerIp")
    def route_dhcp_server_ip(self) -> str:
        return pulumi.get(self, "route_dhcp_server_ip")

    @property
    @pulumi.getter(name="routeGateway")
    def route_gateway(self) -> str:
        """
        e.g. 172.16.0.1
        """
        return pulumi.get(self, "route_gateway")

    @property
    @pulumi.getter(name="routeMode")
    def route_mode(self) -> str:
        return pulumi.get(self, "route_mode")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> int:
        """
        e.g. 1-4094
        """
        return pulumi.get(self, "vlan_id")


class AwaitableGetNetworkResult(GetNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkResult(
            config=self.config,
            description=self.description,
            id=self.id,
            name=self.name,
            namespace=self.namespace,
            route_cidr=self.route_cidr,
            route_connectivity=self.route_connectivity,
            route_dhcp_server_ip=self.route_dhcp_server_ip,
            route_gateway=self.route_gateway,
            route_mode=self.route_mode,
            state=self.state,
            tags=self.tags,
            vlan_id=self.vlan_id)


def get_network(name: Optional[str] = None,
                namespace: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_harvester as harvester

    vlan1 = harvester.get_network(name="vlan1",
        namespace="harvester-public")
    ```


    :param str name: A unique name
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['namespace'] = namespace
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('harvester:index/getNetwork:getNetwork', __args__, opts=opts, typ=GetNetworkResult).value

    return AwaitableGetNetworkResult(
        config=__ret__.config,
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        namespace=__ret__.namespace,
        route_cidr=__ret__.route_cidr,
        route_connectivity=__ret__.route_connectivity,
        route_dhcp_server_ip=__ret__.route_dhcp_server_ip,
        route_gateway=__ret__.route_gateway,
        route_mode=__ret__.route_mode,
        state=__ret__.state,
        tags=__ret__.tags,
        vlan_id=__ret__.vlan_id)


@_utilities.lift_output_func(get_network)
def get_network_output(name: Optional[pulumi.Input[str]] = None,
                       namespace: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_harvester as harvester

    vlan1 = harvester.get_network(name="vlan1",
        namespace="harvester-public")
    ```


    :param str name: A unique name
    """
    ...
