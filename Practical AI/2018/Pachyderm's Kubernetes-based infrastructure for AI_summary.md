• Sponsored by Fastly, Rollbar, Linode, and DigitalOcean
• Introduction to Practical AI podcast
• Guest introduction: Joe Doliner (JD), CEO and founder of Packeter, discusses his background and current projects
• Discussion of data science infrastructure and tools
• Overview of Packy Durham, a tool for high-level production data infrastructure in the cloud
• Pachyderm file system: version controls large datasets, stores data, and provides discrete commits like Git
• Provenance: links different versions of training data to their outputs, allowing for tracing back to original inputs and code
• Open-source platform: accessible through a web interface, allows users to upload code and train models
• Enterprise system: includes additional features, but everything discussed so far is open-source
• Versioning: enables tracking changes to datasets over time
• Containerization: uses containers like Docker to ship around code for processing in Pachyderm
• Docker containers as a solution for incompatible code environments
• Pachyderm's use of Docker containers to unify processing steps across different languages and tools
• Provenance tracking in Pachyderm, allowing data lineage to be tracked across multiple languages and steps
• Using Pachyderm with Jupyter notebooks, including packaging a notebook into a Docker container for deployment
• Steps required to move a Jupyter notebook from local development to production on Pachyderm
• Extracting code from Jupiter and exporting it as a Python script
• Creating a Python container with dependencies for pre-processing, model training, and post-processing
• Deploying the system on the cloud to automate pipeline execution
• Optimizing each step of the pipeline individually for better performance
• Teasing apart steps in the pipeline for parallel processing
• Scaling up infrastructure based on need using Kubernetes
• Introducing Kubeflow as a tool for making training happen in parallel
• Kubernetes handles deployment of distributed applications by managing multiple programs on different machines.
• Packeterm uses Kubernetes to deploy containers and manages data processing with object storage for persistence.
• Data is stored in containers temporarily until processed, then written back out to object storage.
• Packeterm provides a language-agnostic interface for code to interact with data, using normal file system calls.
• Trade-offs exist between performance and data locality, as downloading and writing data can incur penalties.
• Challenges of maintaining object storage for admins due to its simplicity
• Trade-offs between performance and infrastructure complexity
• Use of S3 as a cache layer in Hadoop and Spark environments
• Importance of understanding infrastructure and keeping it simple
• Skills gap between data scientists and engineers, particularly with containerization and Kubernetes
• Need for education and training on DevOps topics, such as permissioning and cluster management
• Issues with S3 network connectivity and bucket rejection during deployment
• Goal of Packeterm: simplify data infrastructure management for companies without large teams
• Current challenges in making Packeterm easy to use, including DevOps complexities and infrastructure leap requirements
• Integrations with existing technologies such as Hadoop, Spark, Hive, and Cassandra
• Challenges in fitting into existing data infrastructure and potential solutions through container-based integrations
• Focus on building from scratch and long-term vision for supporting users who commit to Packeterm from the start
• Recent funding round and increased resources to pursue Packeterm's data science vision
• Discussing the benefits of committing to Packeterm as infrastructure with a focus on stability and company longevity
• Introducing the enterprise product, which includes features such as permissioning systems and provenance tracking
• Describing the differences between open-source and enterprise products, including the need for enterprise-level security and data management
• Mentioning the importance of support and customer engagement in an open-source model
• Discussing the challenges of funding and adoption with an open-source product
• Introducing the idea of a hosted version of the software to change the value proposition
• Outlining resources available for learning and getting started with Pachyderm, including tutorials, quick start guides, and user support
• Pachyderm progress and updates
• Slack channel as a resource for discussion
• Show notes with links to tutorials, docs, and more
• Upcoming episode topics on JS Party podcast (JavaScript and web development)
• Promotions for sponsors: Fastly, Rollbar, and Linode