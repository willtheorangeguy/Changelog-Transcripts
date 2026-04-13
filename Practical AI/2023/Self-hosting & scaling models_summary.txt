• Introduction to Practical AI podcast
• Update on Base 10, a company focused on machine learning and AI
• Discussion of the shift from data scientists being primary users of ML/AI to others (e.g. developers)
• Emergence of open source models and Hugging Face as a community hub
• Changes in the landscape of deploying machine learning and AI systems
• Hugging Face's dominance in AI is compared to GitHub's dominance in software development
• Concerns about the quality and reliability of models on Hugging Face due to clones and random versions
• Emergence of open-source models and their impact on solving complex problems, such as transcription and OCR
• Chat GPT moment for AI, with its influence on consumer and developer expectations for machine learning capabilities
• Infrastructure opportunity for supporting large-scale model deployment and end-user experiences
• Shift from data scientists to engineers needing to grapple with machine learning
• Transition from small, memory-based models to larger models that require more infrastructure support
• Evolution of product development to incorporate machine learning and AI
• Infrastructure challenges in running larger models, including model hosting and workflow management
• Product concerns around using large language models, such as prompt filtering and data privacy
• Analogy between autonomous drones and large language models: initial excitement followed by complexity and difficulty in use
• Comparison of closed APIs to open models like llama or mistrawl, highlighting the difficulties of integrating them into production environments
• Deploying models from platforms like Hugging Face
• Containerization and infrastructure setup for production-ready models
• Scaling and variable traffic management
• Security concerns with serving layers
• Workflow layer and version management
• Observability, logging, and API integration
• Kubernetes experience required for efficient organizations
• Abstracting away complexities to provide a seamless user experience
• The types of people using Base 10 are increasingly engineers and product engineers with ML exposure, rather than traditional data scientists.
• Open-source APIs like Base 10 appeal to users due to cost savings, as open AI costs tend to stack up over time.
• Data privacy and security concerns drive companies to host their own models, especially for B2B use cases and enterprises.
• Fine-tuning open AI models is challenging, but hosting one's own models provides more control and flexibility.
• Companies have data ownership and can deploy Base 10 within their own VPC, keeping data within their boundaries.
• The architecture of Base 10 aims to make it easy for application developers to host and manage their own models with some structure and control.
• Writing a Python class with load and predict functions is required for using base10's features
• The load function tells base10 what the model is trying to accomplish, while the predict function runs the actual inference
• Within these functions, developers can compile code, perform preprocessing and post-processing, and manage data
• Base10 abstracts out some of the work involved in deploying and managing models, but still gives control at the product/application level
• The platform is open-source and allows for deployment on base10's hosted infrastructure or on-premises
• Using base10 versus running a model on EC2 or ECS means less boilerplate code and more streamlined workflow, making it easier to manage production-grade inference
• Saving time and effort in production with Base 10
• Replicating and deploying AI-native products quickly
• Ease of use and speed to production for customers
• Auto-scaling and SRE work for model deployments
• Managed solutions vs building from scratch
• Market demand for fast, talent-constrained industry
• Opportunities in machine learning infrastructure
• Emerging stack: fine-tuning, training, observability, logging
• Trends in AI model deployment, including hosting models on edge devices and optimizing them for various environments.
• Challenges in deploying large language models in resource-constrained environments.
• Opportunities for companies to leverage expertise in cloud-based AI to develop more efficient edge-based solutions.
• Generalization of device-specific challenges and the need for OS-level standardization.
• Coexistence of different approaches, including API-based connections and more complex model optimization.
• Infrastructure concern of model hosting and separating it from expertise
• Edge devices and running multiple models
• Kubernetes and hybrid deployment options
• Future of infrastructure for model hosting, including frameworks and containers
• Multi-cluster support and bringing own compute to base 10
• Enterprise use cases and self-hosted solutions
• Fine tuning as an art, rather than a solved problem
• Need for more control over data, models, and fine tuning scripts
• Collecting data sets around models and caching inputs/outputs
• Multi-cloud adoption in enterprises
• Base 10 capabilities and its potential to provide a unified hosting and control plane
• Opportunities in the GPU-contained world with base 10
• Fine-tuning models using base 10 and data sets
• Tooling layer for AI and ML development
• Potential for innovation and growth in the field