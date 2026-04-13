• Iterative process for machine learning and model refinement
• ML Ops as a solution for iterative processes in machine learning
• Importance of automation in accelerating the process
• Rapid changes in software industry, including AI and machine learning
• Introduction to Practical AI podcast and its focus on AI, machine learning, and data science
• Revisit with ClearML (formerly Allegro AI) on ML Ops and its applications
• Benefits of comprehensive MLOps approach now recognized by most companies
• Transition from manual to automated processes in industries like agriculture
• Case study: GreenEye's transformation using Docker and Kubernetes for MLOps
• Overview of AI in agriculture, including tools for farmers and autonomous decision-making systems
• Merger of high-tech advancements (deep learning, ML ops) with traditional farming industry
• A speaker describes a large sprayer machine with cameras and a boom that can cover up to 5,000 acres.
• The Green Eye technology aims to reduce chemical use by spraying only where needed, rather than assuming the entire field is weeds.
• This approach saves money and reduces chemical use, making it a "win-win situation".
• A company representative discusses evaluating opportunities in industry for applying ML Ops technology.
• They look for iterative processes that involve refining and rebuilding models, which can be accelerated with automation.
• Discussing the concept of getting ideas into the world and seeing what happens
• Interview with charity majors from Honeycomb about their experiences with code, ops, infrastructure, and team collaboration
• Importance of assuming you're wrong rather than right and testing your ideas through experimentation
• Practical application of MLOps (Machine Learning Operations) in automating model deployment and retraining on a real-world example involving a massive machine with sensors or cameras for spraying fields
• Challenges of implementing MLOps, including data control and training models for specific applications
• Use of automation tools such as Kubernetes and TensorRT to streamline the model deployment process
• Running Kubernetes on embedded devices, specifically on tractors, for real-time operations and management
• Discussion of Special Ops and its dedicated team for research
• Comparison of ML Ops to Special Ops
• Introduction of FinOps as a new addition to the teams
• Use of clear mail and Allegro in past workflows
• Shift from Kubeflow Pipeline to clear mail for training runs
• Kubernetes deployment on tractors, including use of K3S
• Benefits of running Kubernetes in all places, including edge environments
• Challenges with ARM 64-bit compatibility in edge environments
• Potential impact of NVIDIA's acquisition of ARM on edge computing and Kubernetes adoption
• The ease of using Kubernetes for sharing and forwarding between edge and cloud environments
• Automation in ML environment allowing thousands of models to be run per year
• Challenges of updating vision models due to changing real-world conditions (weather, geography, etc.)
• Importance of testing on devices rather than just cloud metrics
• Limitations of relying on a single model to solve complex problems
• Need for reproducibility and logging in ML Ops, including data versioning and system setup
• Using ClearML for logging and dashboarding in ML Ops
• ClearML for accelerating compute tasks
• Goal to optimize and streamline model training and inference processes
• Use of retraining models for improved performance and adaptability
• Importance of logging and tracking in model development and deployment
• Collaboration with Moses team on large-scale ClearML implementation
• Development of features driven by community feedback and open-source approach
• Introducing ClearMail orchestrator as a dynamic Docker file for easier job management
• Limiting container usage and promoting resource sharing to avoid thousands of unused containers
• Developing "Kubernetes glue" to convert jobs into Kubernetes-compatible format for better visibility and control
• Implementing priority queue for scheduling jobs and resources, adding order and priority to the process
• Addressing access limitations by allowing data scientists to use the platform without direct access to Kubernetes cluster
• Discussion on running Kubernetes on edge devices and using ClearML as a platform agnostic tool
• Microservices architecture and its management with Kubernetes, and how ClearML approaches MLOps differently
• Data flows from tractors into various processing jobs, including model training
• Model training jobs often fail and can be run using Kubernetes or ClearML
• Models are tied to data and get shipped out for use in edge environments
• There are two paths for starting training: researcher-initiated or data-driven
• Training is done on Moses servers and continuously reports to the main server via ClearML
• Metrics are collected and used to decide whether to deploy a new model version or stop tracking it
• Inference is run on Kubernetes cluster as a service or on K3S as a REST service
• Alon's goals for ClearMetal in the context of GreenEye
• ClearML's new serving solution, replacing KF Serving
• Development of a flexible and scalable serving service
• Plans to release the new serving solution by the end of next month
• Research on solving data access issues in ClearMetal
• Creating a holistic ML Ops approach for better visibility and data utilization
• Promotion of the Practical AI podcast
• Subscription and sharing of the show with friends
• Acknowledgment of sponsors (Fastly) and sound design (Breakmaster Cylinder)
• End of episode, thanking listeners
• Final farewell and sign-off