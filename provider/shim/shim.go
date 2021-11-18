package shim

import (
	"github.com/harvester/terraform-provider-harvester/internal/provider"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

func NewProvider() *schema.Provider {
	return provider.Provider()
}
