// Copyright 2016-2023, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"errors"
	"fmt"

	"github.com/spf13/cobra"

	"github.com/pulumi/pulumi/pkg/v3/backend"
	"github.com/pulumi/pulumi/pkg/v3/backend/display"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/cmdutil"
	"github.com/pulumi/pulumi/sdk/v3/go/common/workspace"
)

func newDeployCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "deploy",
		Short: "Manage Deployments",
		Long:  "Manage Deployments configuration.\n",
		Args:  cmdutil.NoArgs,
	}

	cmd.AddCommand(newSetDeploymentSettingsCmd())

	return cmd
}

func newSetDeploymentSettingsCmd() *cobra.Command {
	/*
		1. parse yaml
		2. merge with params
		3. call api
		4. update yaml if params

		pulumi deploy settings source --type=github --repository=... --branch=... --folder=...
		pulumi deploy settings source --type=git ...
		pulumi deploy settings operation --skip-intermediate-deployments=true --skip-install-dependencies=false

	*/
	cmd := &cobra.Command{
		Use:   "settings",
		Args:  cmdutil.NoArgs,
		Short: "",
		Long:  "",
	}

	cmd.AddCommand(newDeploymentSourceCmd())

	return cmd
}

func newDeploymentSourceCmd() *cobra.Command {
	var stack string
	input := DeploymentSourceInput{}

	cmd := &cobra.Command{
		Use:   "source",
		Args:  cmdutil.ExactArgs(0),
		Short: "",
		Long:  "",
		Run: cmdutil.RunFunc(func(cmd *cobra.Command, args []string) error {
			ctx := commandContext()
			displayOpts := display.Options{
				Color: cmdutil.GetGlobalColorization(),
			}

			project, _, err := readProject()
			if err != nil && !errors.Is(err, workspace.ErrProjectNotFound) {
				return err
			}

			currentBe, err := currentBackend(ctx, project, displayOpts)
			if err != nil {
				return err
			}

			if !currentBe.SupportsDeployments() {
				return fmt.Errorf("backends of this type %q do not support deployments",
					currentBe.Name())
			}

			// Ensure the stack exists.
			s, err := requireStack(ctx, stack, stackOfferNew|stackSetCurrent, displayOpts)
			if err != nil {
				return err
			}

			ps, err := loadProjectStack(project, s)
			if err != nil {
				return err
			}

			mergedInput := mergeDeploymentSourceInput(ps.Deploy.SourceContext, input)

			sourceType, err := getSourceHandler(mergedInput.vcsType)

			if err != nil {
				return err
			}

			err = sourceType.validateInput(mergedInput)

			if err != nil {
				return err
			}

			err = sourceType.update(currentBe, ps, mergedInput)

			if err != nil {
				return err
			}

			if input.isEmpty() {
				return nil
			}

			return sourceType.save(s, ps, mergedInput)
		}),
	}

	cmd.PersistentFlags().StringVar(&input.vcsType, "type", "", "")
	cmd.PersistentFlags().StringVar(&input.repository, "repository", "", "")
	cmd.PersistentFlags().StringVar(&input.branch, "branch", "", "")
	cmd.PersistentFlags().StringVar(&input.folder, "folder", "", "")

	return cmd
}

type DeploymentSourceInput struct {
	repository string
	branch     string
	folder     string
	vcsType    string
}

func (i *DeploymentSourceInput) isEmpty() bool {
	return i.repository == "" && i.branch == "" && i.folder == ""
}

func mergeDeploymentSourceInput(configuration map[string]string, input DeploymentSourceInput) DeploymentSourceInput {
	merged := DeploymentSourceInput{
		vcsType:    configuration["type"],
		repository: configuration["repository"],
		branch:     configuration["branch"],
		folder:     configuration["folder"],
	}

	if input.vcsType != "" {
		merged.vcsType = input.vcsType
	}

	if input.repository != "" {
		merged.repository = input.repository
	}

	if input.branch != "" {
		merged.branch = input.branch
	}

	if input.folder != "" {
		merged.folder = input.folder
	}

	return merged
}

func getSourceHandler(sourceType string) (sourceTypeInterface, error) {
	switch sourceType {
	case "github":
		return githubSourceType(0), nil
	case "git":
		return nil, nil
	default:
		return nil, fmt.Errorf("Invalid source type %q", sourceType)
	}
}

type sourceTypeInterface interface {
	validateInput(input DeploymentSourceInput) error
	update(backend backend.Backend, ps *workspace.ProjectStack, input DeploymentSourceInput) error
	save(s backend.Stack, ps *workspace.ProjectStack, input DeploymentSourceInput) error
}

type githubSourceType int

func (githubSourceType) validateInput(input DeploymentSourceInput) error {
	if input.repository == "" {
		return fmt.Errorf("--repository is required")
	}
	if input.branch == "" {
		return fmt.Errorf("--branch is required")
	}
	if input.folder == "" {
		return fmt.Errorf("--folder is required")
	}
	return nil
}

func (githubSourceType) update(backend backend.Backend, ps *workspace.ProjectStack, input DeploymentSourceInput) error {
	// return backend.SetDeploymentSettingsSource(project, "github", input)
	return nil
}

func (githubSourceType) save(s backend.Stack, ps *workspace.ProjectStack, input DeploymentSourceInput) error {
	ps.Deploy.SourceContext = map[string]string{
		"type":       "github",
		"repository": input.repository,
		"branch":     input.branch,
		"folder":     input.folder,
	}

	return saveProjectStack(s, ps)
}
