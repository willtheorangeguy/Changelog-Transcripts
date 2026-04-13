• Maikel's background as a long-time listener of Changelog who joined the Slack community
• Maikel's inspiration from Solomon Hykes' Docker talk in 2013 to go into web development full-time
• Docker and Kubernetes usage by Maikel in his career and current projects
• Cloud engineer role definition, including enabling developers and UX designers to deliver software efficiently
• Comparison of cloud engineers and platform engineers, including self-service models and integration with development teams
• Day-to-day interactions between Maikel (cloud engineer) and other roles (developers, admins, etc.) during a migration from on-premise to cloud
• Current technology stack used by Maikel's team, including Terraform, Kubernetes, VPCs, Azure DevOps, GitLab CI
• GitLab is used as a CI/CD system and for provisioning infrastructure with Terraform
• Infrastructure is Kubernetes-based, with separate database management
• Argo CD is installed via Terraform script and manages updates to the cluster without downtime
• Argo CD can update itself in place without restarting the service
• Self-hosted GitLab instance on Kubernetes is updated automatically using a CI job that creates a merge request for the upgrade
• The system handles upgrades with minimal or no downtime, but requires careful configuration and management
• Idempotency issue with upgrades
• GitLab vs GitHub comparison and features
• Self-hosting GitLab for flexibility and control
• Upgrades and migration issues in self-hosted environment
• Azure DevOps integration with GitLab and Argo CD
• Argo CD deployment model (infrastructure as code)
• GitOps push model vs Argo CD
• Difficulty of reconciling multiple systems for infrastructure management
• Documentation for understanding the setup of different endpoints
• Kubernetes workshop planning to educate team members
• Use of Kubectl and its alternatives (Kube CTL)
• Centralizing logs and potential use of Loki as a logging system
• Cluster organization (per environment, per application) and potential splitting of Argo CD into separate clusters
• Managed services vs self-hosted solutions for logging and monitoring systems
• Data privacy regulations in Europe and implications for managed services
• User experience design principles applied to infrastructure
• Challenges of aligning configuration across different IDEs (e.g. IntelliJ, VS Code, Vim)
• Centralized repository management (monorepo vs multiple repositories)
• Credential management and single sign-on systems
• Storing secrets with tools like Vault, LastPass, or 1Password
• Securely distributing secrets with tools like Sealed Secrets operator
• Connections to source of truth for secrets
• Using DevSpace to synchronize files in a remote Kubernetes development environment
• Comparison to GitHub Codespaces and Gitpod
• Options for development environments: local native, local Kubernetes, remote Kubernetes, and all remote
• Use case: developing on an iPad with remote Kubernetes
• Inconsistent PostgreSQL versions caused issues due to differences in index building and versioning.
• Node.js version inconsistencies are common and can affect compatibility.
• The importance of aligning team setup with a consistent CI system, formatting, and Git usage is emphasized.
• Maikel recommends avoiding prolonged discussions over Slack or comments, instead opting for quick calls or meetings to resolve issues.
• Discussion on upgrading tools like GitLab and Argo CD without downtime, as well as using remote Kubernetes setups closer to production.