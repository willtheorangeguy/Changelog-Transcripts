• GitHub's security approach and goals
• Securing developer profiles and accounts
• Social engineering and supply chain attacks
• Insider threat programs and broader supply chain security
• Attestations and SLSA compliance for secure builds
• Balancing verification and accessibility in open source communities
• Change of ownership of GitHub repositories and potential security risks
• Attestations for builds in GitHub Actions to verify origin and integrity
• Importance of transparency and machine-readable transparency in open-source software
• Deterrent effect of attestation on malicious actors
• Responsibility of organizations using critical software to ensure security and accountability
• Need for elevated expectations of security tooling and code scanning in open-source software
• Role of GitHub and other platforms in promoting security and transparency in open-source software
• Challenges of securing software due to the vast number of lines of code and potential vulnerabilities
• Importance of adopting secure by design principles and implementing industry-wide best practices
• Need for industry-wide commitment to secure code and product development
• Examples of secure by design principles in action, such as GitHub's Push Protection for Secrets
• Discussion of the trade-off between convenience and security in software development
• Analysis of the impact of mandatory 2FA and secure scanning processes on user behavior and security
• High-level overview of the architecture and cost of implementing secure scanning processes
• GitHub's advanced security features include static analysis, dependency scanning, and secret scanning
• These features are based on CodeQL and are available for free to public repos on GitHub
• GitHub also offers a more comprehensive security suite for enterprise customers, including security overview, trending, and charts
• Dependabot has improved in detecting used code vs. latent code, but still struggles with false positives
• Attestations are a new capability allowing code to be digitally signed and verified by users
• Attestations can be added to a GitHub workflow using a specific GitHub Action
• Receiving end users can verify the attestation using the GitHub command line tool
• The attestation process allows tracking of binary origin, even if downloaded from a local or public artifact store
• The process involves cryptographic hashes and attestation lookup, with a focus on GitHub-specific implementation
• The SigStore approach is used, which is a scaled version of the Sigstore released with npm last year
• Attestations can be used to create a paper trail of software development, including build instructions and commit history
• Software Bill of Materials (SBOMs) and attestation are related concepts, with attestation providing additional information on the source of ingredients
• Industry-wide adoption of attestation and paper trail is expected, with the next step being standardization of these practices in build workflows
• Training, tutorials, and conference talks are being used to promote adoption of these practices and tools
• GitHub code scanning and other AI-powered tools are being explored to make adoption easier for the developer ecosystem
• CodeQL and AI-powered autofix capabilities for detecting and fixing vulnerabilities in code
• Integration of Copilot AI for suggesting fixes and reducing friction for developers
• Proactive versus reactive security measures, including proactive scanning and attestation
• Use of variant analysis and modeling in CodeQL to identify patterns and insecure code
• Advances in editor Copilots for proactive security checks and recommendations
• Importance of low-friction and low-pain security practices for developers to focus on value-add work
• Potential for AI to prevent typosquatting and other security issues through proactive measures
• Discussion of AI-powered tools and their potential to augment human capabilities, particularly in areas where tasks are repetitive or time-consuming
• Examples of AI's potential to improve productivity and efficiency in tasks such as software development and security testing
• GitHub's focus on accelerating human progress through software development and enabling open source, and how AI fits into this mission
• The potential for AI to assist in tasks such as code review, documentation, and security incident response
• The role of AI in reducing the time and effort required for tasks, allowing humans to focus on higher-value work
• Discussion of the intersection of AI and security, including the potential for AI-powered security tools to help organizations protect themselves against threats
• Secure product development and community
• Mitigating abuse of free compute resources
• Balancing security with user experience
• Use of AI in security and abuse
• Incident response and communication during security incidents
• Securing the open source supply chain
• Need for clear, paved paths for secure open source development practices
• GitHub's role in taking responsibility for open source security
• Importance of making security easier for developers
• Need for corporations to invest in open source security
• Ways for organizations to partner with GitHub on security
• Steps for maintainers to bolster their GitHub profile and secure their repositories
• Idea for consensus-based maintenance and attestation for new maintainers
• Maintainer files and community-driven pull request approach for open source maintainership
• GitHub's internal access system uses pull requests for entitlements and approval
• Attestation vs. authorization in open source projects and chains of authority
• Integration of AI into security capabilities for developers
• Securing GitHub and developer ecosystem, including partnership between security and engineering teams