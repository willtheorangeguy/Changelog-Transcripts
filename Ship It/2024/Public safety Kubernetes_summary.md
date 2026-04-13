• Kubernetes in public sector
• Identity system for first responders
• Grant funding from DHS/FEMA
• Active Directory integration issues
• LDAP virtual directory solution
• Government procurement process
• Tremolo Security's involvement with the project
• Open source vs Microsoft-focused approach
• Early days of the company's infrastructure and deployment
• Move to physical appliances and custom-built interface
• Challenges with networking and certificates (expiring certs, etc.)
• Migration from Windows to Linux, .NET to Java, AD to Azure
• Implementation of ADFS and getting rid of virtual directory components
• Takeover of monitoring and building out a Prometheus infrastructure
• The importance of real-time monitoring and feedback loops for software development
• Manual fallbacks in high-stakes industries like public safety where technology failure can be life-threatening
• Automating alert systems with tools like RSS feeds and "if this, then that" alerts
• Integrating multiple systems across jurisdictions with different security protocols (e.g. Azure AD vs Entra)
• The tension between compliance and security standards in industries subject to federal regulations
• Challenges in whitelisting Microsoft URLs due to dynamic IP generation
• Compliance vs security trade-offs in identity management
• Legacy virtual directory technology being replaced by Entra
• Migration to Kubernetes and Azure for increased flexibility and automation
• Automation of infrastructure using Azure DevOps and GitOps
• Transition from .NET to Java backend
• Moving from a push-based pipeline to a pull-based GitOps controller
• Need for a secondary instance of the environment in another region
• Using GitOps to manage configuration manifests and ensure redundancy
• Azure DevOps backend being a custom tool, not an open source one
• Impacts of Azure security vulnerabilities on the team's operations
• Marc Boorshtein expresses his positive experience with Java and Kubernetes
• He discusses the challenges of using Azure due to frequent changes and deprecations
• He compares Azure's interface to AWS, suggesting that failed AWS designers may have worked on Azure's interface
• He gives props to Azure for a successful migration from an old MySQL offering to a new one
• He describes the applications his company manages, including identity management and other tools like Mattermost and wiki.js
• The conversation turns to Marc Boorshtein running his own email server in 2024, despite having access to Office 365
• Marc Boorshtein reveals that his company provides SSO for a regional SharePoint system
• Moving SharePoint system online and integrating with Azure identity management
• Issues with SSO (Single Sign-On) and Azure's B2B/B2C concepts
• Technical issues with U.S. federal government authentication and commercial tenant limitations
• Identity aggregation system for external accounts, contractors, and NGOs
• Email forwarding service to authenticate users and bypass email blocking by public clouds
• Discussion on the flaws of using email addresses as identities due to name changes and other reasons
• Discussion of Azure and GitOps
• Plans for future improvements to Open Unison, including converting configuration from XML to CRDs
• Current and future projects, including interface revamp with Material UI and externalizing secrets management
• Use of Argo instead of Flux in a GitOps setup
• Challenges of running infrastructure as code and the importance of expertise in this area