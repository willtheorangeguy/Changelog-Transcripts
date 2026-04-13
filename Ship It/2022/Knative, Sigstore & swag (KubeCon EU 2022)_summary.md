• Chainguard's swag business is pivoting
• Availability of swag at KubeCon EU in Valencia
• Matt Moore's excitement for Knative's presence in the CNCF and reconnecting with the open-source community in person
• Food and activities to look forward to in Valencia, particularly Spanish cuisine
• Chainguard talks scheduled for KubeCon EU, including SBOMs and their evolving use cases
• The hosts discuss the KubeCon talks and recommend watching the one that interests you most after skimming all five options.
• Matt Moore explains why a high revision count of 4-6 on Knative services is significant due to resource quotas in their GKE cluster.
• Moore clarifies that each update increments a generation number, representing how many times a service has been updated with a new image or configuration.
• He highlights the benefits of using Knative for building production-ready services by automating tasks such as auto-scaling, TLS termination, and smart rollouts.
• The conversation focuses on the nuances of Kubernetes life cycles, particularly around readiness probes, draining traffic, and accepting traffic.
• Implementing a pre-stop hook in Knative to ensure proper signaling and draining of traffic
• Ensuring consistent networking behavior across different revisions and Ingress providers
• Managing scale-up and scale-down scenarios to avoid 500 errors
• Discussion about Chainguard's purpose and focus on supply chain security
• Introduction to Matt Moore's dog, Charlie, a Cavalier King Charles Spaniel
• The importance of package managers in bootstrapping new languages
• The need to secure supply chains beyond just securing individual codebases
• The Sigstore projects (Fulcio, Rekor, Cosign) and their goal to make keyless signing accessible to developers
• Keyless signing as a process that uses an identity challenge to verify the signer's identity without requiring them to manage keys
• The use of OAuth flows for identity challenges and the generation of certificates that include the signer's identity
• The ability to verify keyless signatures using tools like Cosign and Fulcio
• The concept of federation, which allows services to exchange tokens for first-party tokens through security token services (STS)
• Google and Amazon don't need identity information from OIDC-compliant identity providers
• Workload-based signing is built around OIDC federation
• GitHub now supports identity tokens in GitHub Actions
• Keyless signing can be done with a single command
• Signing is the foundation for more advanced features like attestations and policy enforcement
• Nforce complements signing by enabling policies around trusted identities and context-dependent authentication