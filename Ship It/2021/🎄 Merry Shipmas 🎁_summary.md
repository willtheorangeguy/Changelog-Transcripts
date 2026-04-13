• CI/CD Lego set (PR395) for changelog.com
• Continuous CPU profiling (PR396)
• Auto-restoring Kubernetes clusters (PR399)
• Dagger, a universal deployment engine introduced in episode 23
• Implementation and challenges of integrating Dagger with changelog's infrastructure
• Benefits of using Dagger for CI/CD pipelines
• Interactions between Q and BuildKit and how they're applied to BuildKit states
• Improvements in the new pipeline for compiling dependencies and running tests in parallel
• Use of caching mechanisms and ephemeral databases
• Changes to the API to make it more explicit and intuitive
• Integration with GitHub Actions and its potential use in the pipeline
• Overview of Dagger's current state and improvements being made
• Pipeline execution in parallel
• Caching of steps to speed up pipeline execution
• Dagger's ability to use caching for faster builds
• Comparison of Dagger and Docker build times
• OpenTracing integration for visualization of pipeline execution
• Flexibility to run pipelines on any CI setup, including GitHub Actions and CircleCI
• Demonstration of Dagger's cached run and its performance
• Discussion on using BuildKit to enable parallel execution of fine-grained steps
• Explanation of how GitHub Actions integration works with Dagger
• Breakdown of a specific GitHub Actions config file, including environment variables, jobs, and actions used
• Description of using Tailscale Tunnel for remote Docker access
• Discussion on committing secrets and using SOPS for encryption
• Transitioning from "environment" to "plan" or "DAG"
• Using CI package for tasks and automation
• Docker-based workflow with encrypted credentials
• Providing inputs for environment/plan/DAG, including source code and dependencies
• Explanation of queue configuration language and its features (schema definition, data validation)
• DAG or pipeline stages (app image, test container, etc.)
• Depths compile as a way to describe and apply structures in other places
• Discussion of the advantages of Queue over other configuration management tools like YAML and Helm
• Explanation of how Queue's schema definition feature can define the shape of a particular configuration, including constraints on different fields
• Example use case for Kubernetes deployments with CPU field constraints
• Description of how Queue's compiler errors steer users in the right direction
• Discussion of potential future developments in the Queue community, including a language server
• Mention of upcoming changes with Europa that will simplify and improve the user experience
• Profiling has been a key tool for developers since software engineering began
• Traditional profiling was expensive and only done when necessary
• Sampling profiling introduced a more efficient method, recording stack traces at statistically significant intervals (e.g., 100 times per second)
• This allows for detailed analysis of CPU usage and optimization opportunities
• Parca is an implementation that provides near real-time flame graphs and comparative CPU profiles for Kubernetes workloads
• It uses EVPF technology to minimize overhead and record stack traces directly in the kernel
• Benefits include saving money, improving performance, and understanding system bottlenecks.
• The Parca agent sends CPU profiles to the Parca server for analysis and visualization.
• The PPF (Profiling Format) standard is used for profiling data, allowing integration with other tooling and workflows.
• The server ingests CPU profiles from the agent and allows downloading in PPF format for external use.
• The Parca UI displays flame graphs, showing cumulative values of CPU usage for each span.
• Garbage collection can be a significant contributor to CPU spikes due to memory allocation and deallocation.
• Continuous profiling and symbolization can contribute to garbage collection spikes.
• Optimizations such as buffer reuse can help reduce memory allocations.
• The discussion begins with examining a Postgres database and its compiled binary, observing that it only shows memory addresses due to debug information being intentionally removed for size optimization.
• A workaround is mentioned using Debug Info D, a project hosting servers for on-demand debug symbol retrieval.
• Parker doesn't currently support this feature, but the developers are working on implementing it.
• The discussion moves on to examining an Erlang VM and its interpreted code, noting that it has a just-in-time compiler.
• A comparison is made with other dynamic languages and virtual machines, highlighting the need for runtime-specific implementation in Parker.
• The use of perf maps in Erlang is mentioned as a potential solution for symbolizing memory addresses on the fly.
• There are issues with implementing this feature for Erlang, but support is expected to be added in the future.
• The discussion concludes with an overview of the compare view in Parker, which allows users to compare two profiles side by side.
• Observations of CPU cycles and stack traces
• Analysis of performance metrics using a diff function
• Discussion of memory address symbolization
• Investigation into a memory address with unknown origin
• Use of Linux procfs to inspect binary code memory mapping
• Attempt to identify the source of an unknown memory address
• Discussion of a table that shows executable code coming from the binary
• Explanation of how the stack can sometimes be too tall when retrieving stack trace snapshots from eBPF
• Theoretical possibility of executing code on the stack in Erlang VM
• Proposal to ask Lucas Larson for expertise on the matter
• Mention of pull request 396 and a plan to follow up on it
• Review of Parca discussion and agreement to fix issue R
• Plan to use cross-plane to provision Linode Kubernetes cluster using TerraJet tool
• Discussion of testing generated provider with cross-plane control plane or local kind cluster
• Proposal to start with production setup, including installing cross-plane in the production environment
• discussion about providing a kubeconfig to access a cluster
• mention of TerraJet and its use in generating providers for crossplane
• confirmation that version 1.3 of crossplane is sufficient for using TerraJet
• demonstration of connecting to a system using TerraJet
• discussion of the TerraJet generation process and collaboration with other team members
• introduction of ProviderJet, a template for creating new repositories
• instructions on how to use the ProviderJet template to create a new repository
• Specifying provider name lower and upper case in a command
• Replacing all instances of template with the specified commands
• Understanding Terraform provider source and download name in Docker files
• Clarifying that Terraform provider source and download name are not the same thing
• Identifying the correct URL for the Linode Terraform provider
• Finding the changelog for the Terraform provider Linode
• Examining GitHub as a potential example of the V4 version
• Discussion about determining if a Linode provider is using an old version
• Importance of checking the Git repo for the Terraform provider to confirm version
• Realization that the V4 version is available as a Go package and can be imported
• Identifying the line in the Go module that needs to be updated or replaced
• Understanding how to use replace statements in the Go module to update dependencies
• Setting up credentials for Linode using environment variables and CLI tokens
• Clarification on where the Linode token is obtained
• Key username and its origin
• Inv token and its use
• TerraJet, a tool for utilizing the Terraform community's work in Crossplane
• Creating a Linode provider using TerraJet and Terraform
• TerraJet's design and functionality as a code generator and controller
• The history of Marcus's involvement with Terraform and Linode
• The current state of providers generated with TerraJet, including AWS, Azure, GCP, and others.
• ProviderJet AWS has 765 custom resource definitions (CRDs), which is too many for the Kubernetes community
• Another provider was added in the last week, which generated a ProviderJet Linode with 12 commits to Crossplane Contrib
• The previous Linode provider in Crossplane had not been maintained and may not work with the latest versions of Crossplane
• A single resource (LKE cluster) is currently available for provisioning in TerraJet, but additional resources are needed
• Future plans include announcements about stabilized providers (AWS, Azure, GCP), versioned resources, and conversion webhooks
• Implementing a cross-plane provider using TerraJet
• Ease of use with TerraJet compared to other implementations
• Example of a community-written provider (Exoscale) in 6 hours
• Adding an instance resource to JetLinit provider as simple as 10-15 lines of code
• Step-by-step process for creating a Crossplane Linode provider
• Installing Crossplane and the Linode provider using Helm
• Discussion of crossplane RBAC manager and pods
• Using Canines as a CLI for quick tasks
• Creating new clusters with Linode jet crossplane IO V1 alpha 1 group
• Provisioning new clusters using crossplane LKE
• Overview of how crossplane continuously reconciles requests
• Creation of a new LKE instance and cluster in Linode and Kubernetes
• Obtaining kubeconfig for the newly created cluster
• Discussion of using Crossplane to target a Kubernetes cluster without exposing the kubeconfig
• Exploring self-automated system where Crossplane provisions resources and updates application
• Demonstration of deleting a cluster and observing the controller's behavior in reconciling the absence of the cluster
• Explanation of how the controller will try to create a new cluster if it detects that one is missing, with a wait period of up to 1 minute
• Discussion of a custom resource that triggers a Kubernetes event
• Cluster creation and reconciliation process
• Issue with Linode node pool being deleted when cluster was deleted from UI
• Introduction to composite resources and their benefits in managing multiple resources as one
• Explanation of how composite clusters can recreate nodes, installations, and other dependencies automatically
• Example scenario where accidental deletion of a cross-plane cluster led to discussion on the importance of automated recreation of dependent resources
• Idea of improving current functionality by installing base components and using two compositions with XRDs to define APIs for multiple resources.
• Clusterscoped does not have any namespaces
• Creating a composition with base system components for a cluster
• Using a central production cluster with its own claim, similar to PVC, and referencing it from other namespaces via XRD
• Publishing a new API instead of manually configuring cloud-specific fields
• Moving Crossplane from being hosted on the current cluster to a seed cluster on a cloud like AWS or GCP