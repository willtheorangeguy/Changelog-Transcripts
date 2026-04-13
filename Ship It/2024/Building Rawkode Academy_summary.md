• David Flanagan's background and experience
• Rawkode Academy and its transition from a YouTube channel to a self-built platform
• Reasons for leaving Pulumi and the decision to build a self-controlled platform
• Criticism of using platforms like YouTube, citing lack of control and data insights
• Architecture and technologies used in building the Rawkode Academy platform
• Microservices approach and use of GraphQL
• Complex data refactoring and migration challenges
• Database schema management in microservices architecture
• Comparison of NoSQL databases vs traditional RDBMS with schema
• Use of GrafBase to manage meta-data and joins across multiple services
• Advantages of using GraphQL for API design and querying
• Benefits of WebAssembly serverless deployment and caching mechanisms
• Using Postgres and its plugins for data management
• Challenges with RBAC model and need for custom SQL functions
• Exploring alternative databases such as SQLite and LibSQL
• Benefits of using SQLite, including flexibility and reduced infrastructure costs
• Avoiding managed services and wanting platform agnosticism
• Reasons for not choosing NoSQL databases like Cassandra
• Using SQLite as a cost-effective alternative for simple applications
• Big data storage in managed services (e.g. S3, Redshift, Snowflake) and their potential drawbacks
• The importance of simplicity and avoiding over-engineering in software development
• License changes affecting popular technologies like Redis and Elasticsearch
• WebAssembly's potential to simplify microservices by reducing operational overhead
• WebAssembly performance compared to traditional JavaScript execution
• Benefits of using compiled binaries over containers or virtual machines for local development
• Comparison between Rust and Go as compilation targets for WebAssembly
• Discussion on the importance of developer experience and memory safety in programming languages
• The advantages of Cargo, Rust's package manager, compared to other dependency management systems like npm, pip, etc.
• DevRel industry challenges: companies prioritizing marketing over authentic developer advocacy, and the difficulty of scaling meaningful relationships with developers.
• Authenticity vs. Marketing: importance of genuine messaging and credible storytelling in DevRel, as opposed to relying on scripted or misleading content.
• The impact of free marketing platforms (e.g. Linux Foundation, Cloud Native Foundation) on project adoption and contributor expectations.
• Critique of overloading marketing arms with too many voices, diluting messaging and authenticity.
• Need for authentic, hands-on experience in DevRel roles, rather than just selling products or technologies.
• The potential for a shift towards more meaningful, community-driven developer advocacy.
• Building a custom streaming pipeline using Equinix Metal and Kubernetes
• Custom video encoding and processing
• Using open-source tools for tasks like OCR and AI, such as Ollama, Gemini, and OpenAI
• Creating a local-first StreamYard-like platform with WebRTC
• Analyzing YouTube's limitations and building custom analytics
• Utilizing anonymized data to understand audience behavior and improve content creation
• Sharing knowledge and open-source code on GitHub and making it accessible to others
• Justin Garrison prepares to take a quiz on Kubernetes from David Flanagan
• David explains that the questions will range from easy to "Rawkode" difficulty level
• Justin expresses concern about his lack of experience with certain Kubernetes topics
• The quiz begins with an easy question about which Kubernetes object ensures a specified number of pods are running at any given time
• Justin correctly answers the first question, showing he understands the hierarchy of Kubernetes controllers
• David asks follow-up questions about liveness and readiness probes in Kubernetes workloads
• Justin struggles to recall specific details about liveness probes but eventually gets it correct with David's help
• The quiz continues with more questions, including one about which Kubernetes API object is used to expose a service to external traffic using layer four TCP or UDP
• Justin provides thoughtful answers, showing he has a good understanding of certain Kubernetes concepts, but also highlights the limitations and potential inaccuracies of AI-generated content
• The limitations of Layer 4 support in Kubernetes
• Types of admission control in Kubernetes (static vs dynamic)
• Difference between validating and mutating webhooks/admission controllers
• Deprecation of Pod Security Policies (PSPs) and introduction of Pod Security Admission
• Kubernetes quiz questions and answers