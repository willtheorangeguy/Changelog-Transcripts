• Progressive bundling technique
• Using Rollup to bundle ES Modules on demand
• Lambda function caching for faster performance
• Sub-second build times for entry files
• Request-time bundling for first requests, followed by cached responses
• Manual code splitting and entry file creation
• Limited support for legacy browsers and non-ES6 modules
• Deferred build step with potential for future optimizations
• Discussion on using Rollup to manage module dependencies without a build step
• Comparison between pre-compiling everything and using caching to reduce the need for frequent rebuilds
• The importance of fingerprinting files to prevent caching issues with proxies and CDNs
• Introduction of Architect, a tool that simplifies infrastructure management on AWS by providing a high-level manifest format that generates CloudFormation code under the hood
• Discussion of a new approach to web architecture using function-as-a-service (FaaS) and serverless computing
• Comparison with Kubernetes, deemed unnecessary for most modern web applications
• Advantages of FaaS, including faster iteration speeds, better security, and reduced maintenance needs
• Introduction to arc.codes and Begin.com as tools for getting started with serverless computing on AWS
• Comparison of AWS with other cloud providers, including Google Cloud and Azure, with a focus on the advantages of Amazon's market leadership
• Discussion of the potential risks of choosing alternative cloud providers that may not be viable in the long term
• Declaring the end of EC2 for website building
• Discussion of data gravity and the challenges of managing multiple data sources
• The limitations of GraphQL as a solution to these problems
• The need for more innovation in data management, including query languages and persistence
• The importance of declarative infrastructure management and the benefits of a terse manifest format (Architect)
• Discussion of Pulumi vs declarative tools
• Comparison to other configuration management tools (Chef, Puppet, Ansible)
• Concerns about introducing imperative code into declarative environments
• Importance of minimizing runtime dependencies and configuration
• Debate on whether declarative or imperative style is better
• Advice for teams to choose the best approach for their needs
• Discussing the possibility of running JVM-based languages in the browser using WebAssembly
• Comparison between Clojure and ClojureScript, and the differences with other languages like TypeScript
• The benefits and drawbacks of type systems, including the impact on programming style and tooling
• The evolution of typed languages from Java to TypeScript and its approachable design
• The value of progressive adoption in language development and the importance of feedback and bug reporting.