# Harvester Resource Provider

The Harvester Resource Provider for Pulumi lets you manage [Harvester](https://harvesterhci.io/) resources in your cloud programs. To use this package, please [install the Pulumi CLI first](https://www.pulumi.com/docs/reference/cli/).

## Installing
Resources plugin are available as tarballs in the [release](https://github.com/huaxk/pulumi-harvester/releases) page, please install first according to the operating system platform.

This package is available in many languages in the standard packaging formats.

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @huaxkxy/harvester
```

or `yarn`:

```bash
yarn add @huaxkxy/harvester
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_harvester
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/huaxk/pulumi-harvester/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.Harvester
```

## Configuration

The following configuration points are available:

- `harvester:kubeconfig` (Optional) - harvester kubeconfig. Defaults to the environment variable `HARVESTER_KUBECONFIG`.