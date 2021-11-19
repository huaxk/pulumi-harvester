import * as pulumi from "@pulumi/pulumi";
import * as harvester from '@huaxk/pulumi-harvester'

const image = new harvester.Image("ubuntu20cloudimg", {
  name: "ubuntu20cloudimg",
  displayName: "ubuntu20cloudimg",
  sourceType: "download",
  url: "http://cloud-images.ubuntu.com/releases/focal/release/ubuntu-20.04-server-cloudimg-amd64.img",
});

const sshKey = new harvester.SSHKey("mysshkey", {
  name: "mysshkey",
  publicKey: "ssh-rsa xxxxxxxx you ssh key here xxxxxxxxxx"
})

const vm = new harvester.VirtualMachine("ubuntu20", {
  name: "ubuntu20",
  description: "test raw image",

  tags: {
    "ssh-user": "ubuntu"
  },

  cpu: 2,
  memory: "2Gi",

  start: true,
  hostname: "ubuntu-dev",
  machineType: "q35",

  sshKeys: [
    sshKey.name
  ],

  disks: [{
    name: "rootdisk",
    type: "disk",
    size: "10Gi",
    bus: "virtio",
    bootOrder: 1,
    image: image.id,
    autoDelete: true,
  }],

  networkInterfaces: [{
    name: "default",
    model: "virtio",
    type: "masquerade",
  }],

  cloudinit: {
    userData: `
      #cloud-config
      user: ubuntu
      password: ubuntu
      chpasswd: { expire: false }
      ssh_pwauth: true
    `
  }
})

export const imageName = image.id
export const sshkey = sshKey.publicKey
export const virtualMachine = vm.id
export const ip = vm.networkInterfaces.apply(nis => nis[0].ipAddress)