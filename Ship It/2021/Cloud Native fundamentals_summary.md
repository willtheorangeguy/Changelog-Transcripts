• The hosts Gerhard Lazu and Katie Gamanji discuss how they met at an End User Partner Summit
• Katie Gamanji shares her experience with cloud-native tools, starting with Kubernetes setup difficulties and progress in documentation improvements
• Katie introduces the Cloud-Native Fundamentals course, aiming to provide a practical approach to understanding the landscape and using specific tools
• Gerhard praises the diversity of approaches and choices in the cloud-native landscape, which can be overwhelming for beginners
• Katie explains her curation process for the course, focusing on breaking down complex topics into fundamental principles and easy-to-follow steps
• CI/CD pipeline separation
• Use of GitHub Actions for CI and Argo CD for CD
• Importance of clear distinction between continuous integration and delivery
• Interoperability and diversity of tooling in cloud-native environment
• Separation of CI and CD allows for independent changes and flexibility
• Unix philosophy applied to cloud-native with small utilities combined in infinite ways
• Cloud-native approach benefits from being pluggable and interoperable
• Kubernetes can be replaced with other scheduling platforms like Nomad or serverless options
• Serverless computing has its advantages, but may not be suitable for every organization
• Modernization of infrastructure is required to take full advantage of cloud services
• A PaaS (Platform as a Service) may be a viable alternative to container orchestration tools
• Monolithic architecture can be an acceptable starting point for development, but should be broken down into microservices once the team grows and becomes more complex.
• The importance of segregating applications into microservices for fault tolerance and independent management
• The need to reiterate and adjust the segregation of services as the application evolves
• Merging microservices to optimize management and improve performance
• Stale or unused microservices should be retired from the application
• Understanding the organization's requirements and context is crucial in determining whether microservices are necessary
• Kubernetes is a suitable option for managing microservices, but not always the best choice, especially for small teams or startups with limited resources
• Cloud providers can offer free tiers and be a more accessible option for smaller teams or organizations
• Kubernetes as a tool for managing complex applications, providing automated scaling, declarative representation, and control managers to ensure desired state.
• Custom resource definitions (CRDs) and Ingress for managing reachability and granular control over HTTP endpoints.
• Kubernetes' unified API and scalability across various platforms.
• Pipeline and continuous integration and delivery (CI/CD) processes for automating updates and deployments to production environments.
• Stages of CI/CD including testing, packaging, storing, and distributing artifacts, and propagating changes through dev, QA, staging, and production environments.
• GitOps strategy and its importance in cloud-native development
• Argo CD vs FluxCD, with Argo CD being preferred due to its visual interface and community support
• Choice of CI tool, with GitHub Actions being recommended for simplicity
• Importance of monitoring, telemetry, logs, traces, and events in application development, including readiness and liveness probes
• Observability in cloud-native development, including Grafana and Prometheus for metrics collection and visualization
• Instrumenting code for monitoring and debugging purposes
• Cloud-native development requires a DevOps culture
• DevOps is not just a tool or technology, but a collaboration between application developers and infrastructure engineers to leverage tools for transparency and efficiency
• A course on cloud-native fundamentals is being developed and will be free, with the first four courses (Cloud-native Fundamentals, Message Passing, Observability, and Security) making up a nano-degree that will be available as a standalone paid option
• The course aims to make cloud-native ubiquitous and accessible to everyone, with the author hoping to reach the next generation of cloud-native practitioners