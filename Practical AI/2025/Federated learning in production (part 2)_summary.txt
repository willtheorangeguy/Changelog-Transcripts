• Introduction to Practical AI podcast and its companion show The Change Log
• Brief overview of last week's episode on federated learning with Patrick from Intel
• Chong Shen introduces himself as a research engineer at Flower Labs, discussing his background in computational physics and transition into industry
• Federated learning and distributed computing concepts discussed as key aspects of Chong's work
• Chong explains how he discovered the importance of federated learning through client projects and connections to Flower framework
• Two broad categories of data: sensitive/siloed and massive/complex
• Federated learning as a solution for moving machine learning models to where the data is generated
• Federated learning process: local training, model weight aggregation, and globally aggregated model
• Typical user motivations for adopting federated learning: inability to move data due to privacy concerns and difficulty in coordinating multiple databases
• Challenges of implementing federated learning across different security levels and enclaves
• Solution to harmonize data standards before implementation to simplify the process
• Federated learning adoption has grown 100x since 2021, driven by ability to train large language and foundational models
• Previous limitations on model size (hundreds of millions of parameters) have been surpassed with newer developments
• The Flower framework's architecture has been updated to support larger model weights and streaming capabilities
• New version of the framework is expected to be released soon with improved features for users
• The appeal of federated learning has increased due to its ability to train large models, making it a more versatile tool
• NordLayer is advertised as a network security solution for businesses, comparing itself to having a senior DevOps engineer on staff
• Flower framework is an open-source code built on the Apache 2.0 license that allows users to build federated learning solutions
• The framework provides a basic Python distribution and apps to construct federated learning architecture
• It emphasizes user experience and prioritizes supporting users through various channels, including Slack and discourse channels
• Federated learning using Python is a natural fit due to its widespread use in machine learning and deep learning.
• The Flower framework has improved significantly over the past 10 releases, focusing on user experience and reducing cognitive load.
• A new feature called CLIs (Command Line Interfaces) simplifies tasks such as creating templates for federated learning projects and monitoring runs.
• Previously, setting up a federation required starting three Python scripts, but with the new CLI, it's more intuitive and scalable.
• A production-ready federated learning system using Flower can involve multiple components, including aggregation servers, client apps, and data sources.
• Considerations for moving from a prototype to full-scale production include scalability, security, and monitoring of the entire workflow.
• Testing implementation of basic architecture in simulation runtime using Hugging Face datasets or artificially created data
• Execution modes: simulation runtime and deployment runtime
• Requirements for deploying production system: Blurb (bandwidth, latency, efficiency, reliability, and privacy)
• Infrastructure layer in flower framework: application layer and infrastructure layer; superlink and supernodes
• Reliability and connection handling through long-running services
• Bandwidth and latency optimization between superlink and supernodes
• Centralized setup process for connecting super nodes or clients
• Roles in setting up federation: administrator role (deploying, registering users, monitoring usage) and user/data practitioner role (writing apps, running experiments)
• Deployment of super nodes using templates (Kubernetes, Docker, Helm charts) and hosting superlink by trusted third party server or flower labs.
• Authentication and authorization requirements for using the flower framework
• Knowledge and skills required for users to effectively use flower, including networking and communication protocols
• Infrastructure and DevOps familiarity for deploying super nodes and working with infrastructure
• Impact of generative AI on flower's roadmap and future development
• Federated learning as a key technology driving the framework's development
• Combining multiple models together to achieve tasks and how this affects using federated learning
• Development of models for agentic workflows requires optimization for specific structures and evaluation metrics.
• Integration of federated learning with agentic workflows holds promise, but requires proper evaluation and understanding of limitations.
• The potential for distributed learning to improve model performance is a key area of interest.
• Chong's team is working on a foundation language model trained using federated learning, which aims to be both privacy-preserving and state-of-the-art.
• Collaboration with Vana in the US is exploring data dials and contributing to this effort.