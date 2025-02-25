package main

import (
	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := random.NewRandomPet(ctx, "foo", nil, pulumi.RetainOnDelete(true))
		if err != nil {
			return err
		}
		return nil
	})
}
