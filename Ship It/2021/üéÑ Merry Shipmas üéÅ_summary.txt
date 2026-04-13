• Introduction to a CI/CD LEGO set used by Changelog.com for production
• New pipeline improves coding-to-prod time to at least twice as fast as before
• Use of Dagger and CUE language in the pipeline
• Discussion of the team's experience working on the project, including challenges and learning opportunities
• Explanation of the new pipeline workflow, including parallel dependency builds and caching mechanisms
• Plans for improving developer experience with BuildKit and CUE
• Demonstration of the new pipeline and its features, including actions and parallel dependency builds.
• BuildKit and Docker build features
• Steps as container-based actions with inputs and outputs
• Pipeline running in parallel with caching and speed improvements
• Dagger integration with GitHub Actions and local machines
• Open tracing feature for visualizing pipeline performance
• Fine-grained step relationships enabling parallel execution
• CI setup and environment variables configuration
• Secrets management using SOPS encryption
• Discussion of a pipeline's configuration and how it interacts with Docker and CUE (Configure, Unify, Execute)
• Explanation of CUE as a configuration language that aims to be better than JSON and YAML
• Benefits of using CUE for schema definition, data validation, and type-checking
• Example use case: deploying serverless functions on AWS using CUE
• Mention of future improvements with Europa, including improved DX (Developer Experience) and potential removal of hoops to jump through in the pipeline configuration
• Discussion of the value of profiling Kubernetes workloads
• Explanation of sampling profiling and its benefits over traditional profiling methods
• Introduction to Parka, a tool for recording and analyzing CPU profiles
• Demo of Parka's functionality, including visualizing CPU samples and Flame Graphs
• Discussion of how Parka can be used to optimize code and reduce CPU usage
• Discussion of performance spikes in Parka's profiling data
• Symbolization and ingestion of profiling data as potential causes for performance issues
• Optimizations to reduce performance impact, including buffer reuse and storage optimizations
• Displaying Flame Graphs in Parka, with the ability to view different profiles and machine-compiled binaries
• Explaining memory addresses in Flame Graphs due to stripped debug information in Postgres binary
• Introduction of Debuginfod project for on-demand debug symbol retrieval
• Discussion of Erlang VM's just-in-time compiler and perf.maps implementation
• Comparison view feature in Parka, with interpretation of results regarding CPU cycles and observations of stack traces.
• Discussion of color scheme for visual representation
• Attempt to diagnose an issue with Parka Agent symbolization, specifically a memory address that doesn't match any executable code
• Investigation into procfs and process maps to understand memory-mapping behavior
• Theoretical explanation of potential issues with stack trace snapshots in eBPF
• Decision to seek further expertise from Lukas Larsson on Erlang runtime behavior
• Discussion of using Crossplane to provision a Linode Kubernetes cluster for Changelog.com setup
• Discussion about an upcoming Easter Egg in a project
• Review of control plane and Kubernetes cluster versions (K 1.3.1 and patch updates to 1.3.3)
• Terrajet setup and requirements for Crossplane version (version 1.3 sufficient)
• Pairing session on setting up a new repository using the Provider Jet template
• Troubleshooting issues with Terraform provider source and Terraform download name in the Docker file
• Discussing a GitHub issue with a Linode Terraform provider
• Resolving an issue with the provider's version and import path
• Understanding how to set up credentials for the Linode provider in a Terraform configuration
• Introduction to Terrajet, a code generator that creates Crossplane providers from Terraform providers
• Explanation of how Terrajet was used to create a Linode provider for Crossplane
• Discussion of the number of providers generated with Terrajet and where they can be found
• List of new providers added to Crossplane, including Equinix, Exoscale, and Jet Linode
• Discussion on TerraJet's ability to handle large numbers of CRDs (custom resource definitions) with APIs
• Introduction of a new provider for AWS that has 765 CRDs
• Explanation of how a Crossplane provider was added in just 12 commits
• Announcement of upcoming changes for Terrajet, including stabilized API groups and commercial WebHooks
• Demonstration of how easy it is to create a new Crossplane provider using TerraJet
• Installation of Crossplane and the Linode provider in production
• Explanation of how small images can be used to pull larger images with metadata
• Crossplane used to provision a new Linode Kubernetes Engine (LKE) cluster
• The CRD (Custom Resource Definition) in Linode Jet Crossplane IO v1 Alpha 1 group is used for provisioning clusters
• Terrajet uses Terraform's tfstate and exports it as a secret, which is then decoded by Crossplane to generate the kubeconfig
• The goal is to create a self-updating, self-provisioning system where Crossplane can provision resources within the cluster without needing external kubeconfig
• If a resource (in this case, the cluster) is deleted, Crossplane will reconcile and try to recreate it after a 1-minute wait period
• Crossplane recreates a cluster and its nodes after it is accidentally deleted
• Composite resources allow for the creation of multiple resources in one composition
• The "batteries included" concept allows for installing base system components with a single composition
• Compositions can be used to define custom APIs and manage applications across multiple clusters
• Future plans include moving Crossplane from being hosted on a cluster to being hosted on Upbound cloud, allowing for centralized management of multiple clusters and other resources.