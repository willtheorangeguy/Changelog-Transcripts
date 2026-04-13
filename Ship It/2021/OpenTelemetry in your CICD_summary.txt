• Presentation on Jenkins CI agents and monitoring with OpenTelemetry
• Importance of observability in distributed systems like Jenkins
• Akihiro Kiuchi's project on OpenTelemetry for Jenkins agents as part of Google Summer of Code
• Use of OpenTelemetry to provide visibility into job execution, agent allocation, and communication
• CI/CD system architecture and the blurring of lines between CI and CD
• Importance of using open standards like OpenTelemetry for monitoring and observability in cloud-native deployment
• Benefits of using OpenTelemetry for distributed tracing, audit, supply chain security, and cost accounting
• Discussion on the importance of a unified view of CI/CD processes and systems
• Dimensions in pipeline data collection and abstraction for unified vision
• Ideal pipeline flow with OpenTelemetry integration
• Challenges in instrumenting pipelines, such as capturing correct spans and attributes
• Role of OpenTelemetry in helping CI/CD administrators troubleshoot complex issues
• Importance of observability in identifying problems impacting multiple teams or organizations
• Administrator challenges in understanding and debugging complex CI/CD pipelines
• Caching issues in CI/CD systems and difficulties in identifying dependencies
• Flaky tests in distributed systems and need for observability to improve confidence in changes
• OpenTelemetry's role in providing visibility into CI/CD pipeline events, dependencies, and performance
• Integrating OpenTelemetry with existing tools such as Jenkins and Concourse CI
• Using Otel CLI as a wrapper for Maven builds or makefiles to gain more granularity in pipeline execution
• Deploying Jenkins in production using Kubernetes and Helm charts or Operators
• Configuring pipelines and agents as code, storing them in the same repository as the project code
• Importance of testing locally on development cycle and having fragments that can be tested locally
• Jenkins pipeline can be defined in Groovy DSL or Yaml format
• Declarative syntax vs scripted pipelines, pros and cons of each
• Configuring Jenkins using Kubernetes API or targeting the master node directly
• Separating CI from CD concerns, benefits and implementation details
• Using separate tools for CI (e.g. GitHub Actions) and CD (e.g. Argo CD)
• GitOps approach connecting CI and CD processes
• Decoupling deployment from integration concerns using tooling like Keelsh
• Developing CI/CD pipelines locally with minimal code and business logic
• Creating pipeline libraries to reuse common steps and reduce complexity
• Standardization of CI/CD processes
• Supply chain security in CI/CD space
• Importance of capturing right information in bill of materials
• OpenTelemetry instrumentation for observability and audit trails
• Captain Obvious project for quality gate management and compliance
• Oleg Nenashev's move to Switzerland and his work with CloudBees
• OpenTelemetry helps improve developer velocity, reduce costs, and shorten delivery cycles by providing essential data.
• The same view can be achieved across different systems as long as they emit OpenTelemetry events.
• Standardization of events is needed for efficient collaboration between systems.
• Oleg Nenashev wants to lay foundations for working groups to standardize OpenTelemetry events.
• Continuous Delivery Foundation is already working on standardizing CD events.
• Adoption of OpenTelemetry has been massive, and it's likely to become incubating soon in CNCF.
• Cyrille Le Clerc shares updates on donated OpenTelemetry Maven integration and Ansible integration.
• Oleg Nenashev announces his job change but promises continued involvement in open source and observability.