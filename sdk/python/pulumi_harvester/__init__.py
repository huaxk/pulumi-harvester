# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .cluster_network import *
from .image import *
from .network import *
from .provider import *
from .ssh_key import *
from .virtual_machine import *
from .volume import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_harvester.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_harvester.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "harvester",
  "mod": "index/clusterNetwork",
  "fqn": "pulumi_harvester",
  "classes": {
   "harvester:index/clusterNetwork:ClusterNetwork": "ClusterNetwork"
  }
 },
 {
  "pkg": "harvester",
  "mod": "index/image",
  "fqn": "pulumi_harvester",
  "classes": {
   "harvester:index/image:Image": "Image"
  }
 },
 {
  "pkg": "harvester",
  "mod": "index/network",
  "fqn": "pulumi_harvester",
  "classes": {
   "harvester:index/network:Network": "Network"
  }
 },
 {
  "pkg": "harvester",
  "mod": "index/sSHKey",
  "fqn": "pulumi_harvester",
  "classes": {
   "harvester:index/sSHKey:SSHKey": "SSHKey"
  }
 },
 {
  "pkg": "harvester",
  "mod": "index/virtualMachine",
  "fqn": "pulumi_harvester",
  "classes": {
   "harvester:index/virtualMachine:VirtualMachine": "VirtualMachine"
  }
 },
 {
  "pkg": "harvester",
  "mod": "index/volume",
  "fqn": "pulumi_harvester",
  "classes": {
   "harvester:index/volume:Volume": "Volume"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "harvester",
  "token": "pulumi:providers:harvester",
  "fqn": "pulumi_harvester",
  "class": "Provider"
 }
]
"""
)
