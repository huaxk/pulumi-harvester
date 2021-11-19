package main

import (
	"github.com/huaxk/pulumi-harvester/sdk/go/harvester"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		image, err := harvester.NewImage(ctx, "ubuntu20cloudimg", &harvester.ImageArgs{
			Name:        pulumi.String("ubuntu20cloudimg"),
			DisplayName: pulumi.String("ubuntu20cloudimg"),
			SourceType:  pulumi.String("download"),
			Url:         pulumi.String("http://cloud-images.ubuntu.com/releases/focal/release/ubuntu-20.04-server-cloudimg-amd64.img"),
		})
		if err != nil {
			return err
		}

		sshKey, err := harvester.NewSSHKey(ctx, "mysshkey", &harvester.SSHKeyArgs{
			Description: pulumi.String("My ssh key"),
			Name:        pulumi.String("mysshkey"),
			PublicKey:   pulumi.String("ssh-rsa xxxxxxxx you ssh key here xxxxxxxxxx"),
		})
		if err != nil {
			return err
		}

		const userData = pulumi.String(`#cloud-config
user: ubuntu
password: ubuntu
chpasswd: { expire: false }
ssh_pwauth: true
`)

		vm, err := harvester.NewVirtualMachine(ctx, "ubuntu20", &harvester.VirtualMachineArgs{
			Name:        pulumi.String("ubuntu20"),
			Description: pulumi.String("Test raw image"),
			Tags:        pulumi.Map{"ssh-user": pulumi.String("ubuntu")},
			Cpu:         pulumi.Int(2),
			Memory:      pulumi.String("2Gi"),
			Start:       pulumi.Bool(true),
			Hostname:    pulumi.String("ubuntu-dev"),
			MachineType: pulumi.String("q35"),
			SshKeys:     pulumi.StringArray{sshKey.Name},

			Disks: harvester.VirtualMachineDiskArray{
				harvester.VirtualMachineDiskArgs{
					Name:       pulumi.String("rootdisk"),
					Type:       pulumi.String("disk"),
					Size:       pulumi.String("10Gi"),
					Bus:        pulumi.String("virtio"),
					BootOrder:  pulumi.Int(1),
					Image:      image.ID(),
					AutoDelete: pulumi.Bool(true),
				},
			},

			NetworkInterfaces: harvester.VirtualMachineNetworkInterfaceArray{
				harvester.VirtualMachineNetworkInterfaceArgs{
					Name:  pulumi.String("default"),
					Model: pulumi.String("virtio"),
					Type:  pulumi.String("masquerade"),
				},
			},

			Cloudinit: harvester.VirtualMachineCloudinitArgs{
				UserData: userData,
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("imageName", image.ID())
		ctx.Export("sshKey", sshKey.PublicKey)
		ctx.Export("virtualMachine", vm.ID())
		ctx.Export("userData", vm.Cloudinit.UserData())
		ctx.Export("vm ip address", vm.NetworkInterfaces.ApplyT(func(networkInterface []harvester.VirtualMachineNetworkInterface) string {
			return *networkInterface[0].IpAddress
		}))
		ctx.Export("vm ip address directly", vm.NetworkInterfaces.Index(pulumi.Int(0)).IpAddress().Elem())

		return nil
	})
}
