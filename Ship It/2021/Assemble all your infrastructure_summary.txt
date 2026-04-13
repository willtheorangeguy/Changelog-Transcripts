• Marques is still involved with Crossplane, but not part of the current podcast
• The version of Crossplane in November 2019 was 0.5.0, and now it's on 1.3.0
• There have been over 1,800 commits since 0.5.0 from 24 contributors
• The user experience of Crossplane has changed significantly, with more flexibility and power in defining compositions and abstractions
• Compositions are a way to combine resources to satisfy abstract types, and can be combined within each other
• Configuration packages declare dependencies on providers and other configurations, allowing for the creation of complex platforms
• Defining abstractions in Crossplane and enabling flexibility for users to define their own
• Discovering and sharing abstractions through registries and repositories
• Packaging and sharing of abstractions using OCI-compliant registries
• Building a registry with rich discoverability features by Upbound
• Creating a directed acyclic graph (DAG) to resolve dependencies and conflicts between configuration packages
• Importance of Crossplane in providing a unified API for infrastructure management
• Evolution of the story behind Crossplane, from storage orchestration to dynamic provisioning of various infrastructure resources
• Business value of using Crossplane in shared services infrastructure platform teams and application teams
• Challenges of managing infrastructure across different cloud services and providers
• Overview of Crossplane's value proposition for building customized infrastructure platforms
• Importance of discoverability and ease of use in onboarding with Crossplane
• Role of Upbound Cloud in providing additional features and functionality beyond the open-source version
• Reference platforms and documentation available to help users get started and learn more about Crossplane
• Crossplane abstractions for defining entire infrastructure setup
• Linode provider exists and can be used with Crossplane
• Integrating CDN (Fastly) with Crossplane as a resource
• Helm and Kubernetes providers available in Crossplane
• Template or configuration package for deploying Phoenix web app possible through Crossplane registry
• Relationship between Crossplane and Argo CD, including using GitOps to provision infrastructure and applications
• Two options for managing control plane: running Crossplane on premises or using Upbound Cloud's hosted instance
• Issues with Kubernetes are not relevant as long as Crossplane is always available and healthy.
• The value proposition of Crossplane lies in its decoupling from infrastructure management, allowing users to focus on other tasks.
• A hosted control plane is important for provisioning infrastructure and ensuring infrastructure health.
• Automating infrastructure management through managed services can free up teams to work on more complex and interesting problems.
• Crossplane's goal is to automate tedious tasks, not eliminate jobs, but rather enable teams to focus on higher-level tasks.
• Open sourcing and community development for Crossplane
• Extending Crossplane through APIs and providers for multi-cloud support
• Comparison with Terraform, including differences in active reconciliation and permissioning at abstraction level
• Crossplane's composition model and its benefits for infrastructure management and isolation
• Hack week results, including new provider developments and tooling enhancements
• Development of tools for integrating designers into the app development process
• Hack week project: k8s container registry, allowing direct image pushing into Kubernetes without an external registry
• WebAssembly and browser-based OCI image building
• Community growth and contribution to Crossplane.io
• Future vision of infrastructure management with higher-level abstractions and control planes