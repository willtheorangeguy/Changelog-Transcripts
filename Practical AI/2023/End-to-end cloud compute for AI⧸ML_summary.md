• Introduction to Practical AI and its host Daniel Whitenack
• Guest introduction: Eric Bernardson with modal, a cloud compute platform
• Brief discussion of a previous blog post by Eric on building data teams
• Eric describes modal as an end-to-end stack for cloud compute
• Background on Eric's experience working with data and founding modal
• Discussion of the problems that modal addresses in cloud computing
• Modelo's focus on online inference and machine learning
• The concept of running code locally vs. in the cloud
• The challenge of slow iteration speed for data teams due to deployment cycles
• Building a custom container runtime and infrastructure to address this issue
• Creating a serverless, developer-friendly workflow with rapid iteration capabilities
• AWS Lambda limitations: iteration speed, no support for GPU, long running jobs
• Problem with Kubernetes and AWS: inefficient iteration speed due to containerization
• Docker inefficiencies: layering, lack of deduplication of information
• Custom-built file system: deduplicates content by computing checksums
• Comparison with other existing solutions (Kubernetes, Lambda, Docker)
• Decision to use lower-level primitives instead of relying on established frameworks
• Benefits and challenges of using custom-built workflows for machine learning/AI applications
• The speaker discusses the benefits of using a quick cycle workflow for data-related tasks
• Online inference is a key area of focus, particularly with GPU support being limited among vendors
• Serverless options are gaining popularity due to cost savings and ease of use
• Modal is mentioned as an example vendor providing serverless solutions for GPU compute
• Modal's user experience is praised, but limitations exist in areas such as data pipelines and scheduling
• The speaker has a significant number of modal apps deployed and uses it extensively in their work
• The speaker discusses modal's concept of infrastructure and app code being combined in the same code
• Modal provisions itself, allowing developers to define infrastructure needs in code without configuration files or local setup
• Developers can create functions with specific container requirements (e.g. GPU, CPUs, RAM) that are provisioned on demand
• The speaker highlights modal's ability to provide a fast feedback loop for development and testing, eliminating the need for local environments and minimizing environment conflicts
• Modal allows developers to import dependencies without needing to install them locally, using cloud-based containers instead
• Modal was initially intended for batch workhorse tasks but saw traction in online inference and model deployments
• Improving startup performance is now a focus due to the need for quick container spin-up and model loading when doing online inference
• Users are leveraging modal's functionality to set up web hooks, allowing them to build full-blown web apps on mobile with graphical UIs
• Some users are replacing traditional job queues with modal functions, which can enqueue work without worrying about scaling or deployment
• A typical AI ML workflow in modal involves decorating an existing Python function with a special decorator and annotating it for model usage.
• Using Modal to create and deploy Python functions
• Defining an image in code using modal syntax
• Creating a Docker file with packages (transformers, accelerate, diffusers)
• Annotating the function to use the defined image
• Deploying and running the function with Modal (modal deploy or modal run)
• Optimizing for fast feedback loops in software engineering
• Front end engineers' iteration cycles (writing code, hot releasing it)
• The importance of fast and snappy feedback in software development
• Modal's hot reloading feature for web serving and cloud deployment
• Complexity of implementing hot reloading under the hood
• Challenges of migrating large companies to modal from existing infrastructure
• Strategies for companies with legacy infrastructure to adopt modal
• Importance of security and compliance considerations for big companies
• Key differences between selling to early-stage companies vs. larger enterprises
• Finding niche use cases that are low risk and don't rely on critical business paths
• Starting with research projects or greenfield initiatives to deploy models and pipelines
• Needing to support multiple types of jobs and apps in Modal, which could make it a general-purpose tool or fill a specific niche
• Path forward involves fine-tuning and training features, pre-processing, scheduling, retraining, and hosting stateful applications
• Long-term vision is for consolidation or defragmentation of the data landscape through fewer vendors doing more
• Infrastructure built in Rust will be language-agnostic and can support multiple languages like Python, TypeScript, R, Go, and others
• The speaker loves Rust and considers it their favorite language.
• Go and Rust are used for back-end development.
• Discussion about edge computing, its limitations, and how model is not well-suited for latency-sensitive applications.
• Model focuses on serverless architecture with traditional Linux distributions in containers or VMs, which has non-trivial overhead.
• The speaker is happy to let other vendors handle edge-based workloads that require low latency (e.g., IoT, high-performance CDNs).
• Current focus on improving the user experience of the SDK for distributed cloud applications and making it feel intuitive.
• Work needed to improve the user experience when running modal in notebooks and scaling up the backend infrastructure.
• Challenges with running architecture, including GPU support and security
• Work being done on containers, isolation, and VMs for secure multi-tenant environments
• Plans for expanding modal use cases beyond online inference to training and parallelization
• Focus on building enterprise-ready solutions with security compliance work
• Future plans for increased traction and customer adoption