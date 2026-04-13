• Kubernetes usage
• PostgreSQL storage options
• Supply chain security challenges
• KubeCon EU conference attendance
• Adolfo's upcoming talks and demo preparation for the conference
• SBOM (Software Bill of Materials) tools development
• Splitting SBOM into micro SBOMs for easier storage and management
• Tooling to pool together separate SBOMs for a central view of all information
• Kubernetes signing and demo on signature structure and information obtainable from them
• Provenance attestations published with Kubernetes releases
• Tools for creating and managing SBOMs, including BOM tool (Bill of Materials)
• Using GitHub Actions for release process and pooling tools together
• Support for various artifacts in BOM tool, including container images, source code directories, files, image archives, and operating system packages
• Challenges implementing support for container images due to their complexity and nesting
• Details obtainable from SBOMs, such as package names, licensing information, and maintainer details
• SBOMs (Software Bill of Materials) help organizations manage dependencies and identify vulnerabilities
• Current focus on producing and consuming SBOMs, with debate around their true nature
• Cosign from Sigstore helps sign container images using ephemeral keys, storing public keys in a transparency log
• Sigstore transparency log is a public service that stores information about signatures and can be queried for verification
• Infrastructure behind Sigstore runs on Kubernetes, with Trillian as the backend project and Rekor serving the transparency log
• Fulcio acts as the certificate authority for the project, handing out certificates for signing and verifying artifacts
• Sigstore vs Letsencrypt: differences in issuing certificates
• OIDC identities used to sign software with Cosign
• Infrastructre for verifying certificates handled by public service (Sigstore)
• Plans for General Availability (GA) of Sigstore infrastructure
• Discussion on releasing Kubernetes less often and making it more secure
• Current release cycle for Kubernetes: 3 releases per year, switching from 4
• Trade-offs in slowing down release pace to ensure stability and security
• Upgrading to Kubernetes 1.24 deprecates Dockershim
• Support windows for previous Kubernetes versions: 3 branches supported (currently 1.23 and 1.22)
• Deprecation and removal process for deprecated features
• Maintenance mode after a branch is end-of-life
• Cherry-picking bug fixes and security updates to older branches
• Workload on release team, including SIG Release technical lead role
• Contributing to Kubernetes as a volunteer or part-time job
• Importance of supply chain security in Kubernetes release process
• Discussion of challenges with implementing digital signatures in Kubernetes
• Explanation of the multi-stage release process and how to ensure integrity and signatures are carried over between stages
• Overview of the Kubernetes release process, including the role of release managers and the release team
• Details on the technical side of releasing Kubernetes, including building, staging, and verifying artifacts
• Story behind Adolfo García Veytia's nickname "Puerco" and its use across various online platforms
• Discussion of the importance of community input and collaboration in open-source projects like Kubernetes
• Emphasis on supply chain security in software and the need for collective effort to address complex problems
• Importance of secure software supply chain and awareness of risks
• Need for signed artifacts, SBOMs, and verification in open source projects
• Complexity and urgency of addressing the problem beyond just software
• Encouragement to take small steps towards improvement
• Call to action to prioritize supply chain security and be aware of vulnerabilities flowing upstream