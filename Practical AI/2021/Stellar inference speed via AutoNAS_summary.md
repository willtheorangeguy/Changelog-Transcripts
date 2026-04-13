• Model design approach for optimal data and hardware performance
• Importance of optimizing models for inference hardware
• Benefits of customizing models for specific hardware vs using pre-existing models
• Discussion on inference workload and its impact on organization resources
• Overview of Jonathan Geifman's company, DESI, and its focus on productionizing models
• Hardware considerations for cloud deployment vs. edge inference
• Proportions of GPU usage in cloud-based data science teams
• Challenges of deploying models from training to production
• Trade-offs between model accuracy and deployment complexity
• Importance of considering edge constraints (latency, memory) during development
• Costs of running inference workloads in the cloud
• Use of GPUs vs. CPUs for inference tasks (task-dependent)
• Edge hardware diversity and challenges of deployment to Edge devices
• Understanding the software stack suitable for specific hardware
• Considering limitations of target hardware, such as memory constraints and performance
• Need to measure model performance on target hardware early in development stage
• Importance of holistic approach to balance accuracy, latency, and model size
• Inference stack concept with hardware at bottom, followed by drivers, graph compilers, open source methods (pruning and quantization), and specialized model design approaches
• Optimizing models for specific hardware types through tailored model design
• Collaboration with Intel on performance booster for image classification models
• Neural architecture search using Ultronac algorithm
• Improving model accuracy and reducing latency through modifications to ResNet50 architecture
• Understanding the importance of different layers in neural networks
• Observing changes made by Ultronac algorithm to identify design insights for better architecture design
• Automatic neural architecture search on hardware-specific models
• Input requirements for automatic neural architecture search (model serialized version, dataset)
• Relationship between latency and accuracy in model optimization
• Measuring latency without training data on hardware
• Importance of accuracy constraint to avoid suboptimal models
• Accounting for variability in deployment environments during training
• Drones and automotive applications are areas where custom environments and hardware considerations are crucial.
• Proxies for device performance, such as floating point operations, can be inaccurate or misleading.
• Measuring actual device metrics like latency and throughput is essential for understanding real-world performance.
• Neural architecture search has limitations in comparison to other compression techniques like pruning.
• Maintaining a search space that includes new layers and operators as they emerge is a challenge.
• Growing the search space requires balancing inclusion of new developments with the need for efficient and accurate evaluation.
• The current state of deep learning models suggests that focusing on the composition of operators rather than "fancy tricks" is crucial for achieving good results.
• It's not easy to beat a well-optimized ResNet model with quantization and graph compilation techniques.
• Different domains, such as NLP and computer vision, have varying levels of optimization difficulty.
• Semantic segmentation networks are more complex than classification networks but can still be optimized using the right principles.
• The three main components of most networks are the stem, backbone, and prediction block.
• The majority of computation happens in the backbone component.
• Optimizing the backbone can improve performance across various tasks such as classification, semantic segmentation, and object detection.
• DESI has an end-to-end platform for development to production, including tools Inferi and RTIC.
• The platform provides a SaaS offering with model repository and standardized API for deployment.
• Companies can deploy models using their existing infrastructure or use DESI's deployment tools.
• DESI supports various frameworks such as TensorFlow, PyTorch, and Keras.
• DESI nets for achieving performance in various tasks
• Using pre-optimized models for each hardware type
• Plotting an efficient frontier chart to show the trade-off between accuracy and latency
• Providing pre-optimized results from AutoNAC for immediate use
• Exploring the efficiency landscape of neural architecture search
• Feedback loop of using AutoNAC and learning to start with better initial models
• Automatic neural architecture search and its application in hardware-optimized models
• DESINETS: pre-optimized models for specific hardware, allowing for faster and more accurate results
• Comparison with off-the-shelf models (e.g. EfficientNets) and their limitations on certain hardware
• Potential to build upon optimized backbones with additional prediction heads or tasks
• Future aspirations for the DESI platform, including advancements in model optimization and performance.
• Expanding model optimization to the entire development lifecycle
• Controlling training, optimization, and deployment of deep learning models on a platform
• A "triangle" of optimization: balancing model, data, and hardware
• Providing tools to solve this triangle, currently focusing on model side but future plans include data and hardware
• Future goals: data enrichment, augmentation, self-supervised learning, hardware recommendation systems, FPGA capabilities
• The host recommends subscribing to the master feed of Changelog Podcasts, which includes Practical AI and Ship It.
• The benefits of subscribing include having multiple podcasts in one place and access to a changelog of all episodes.
• Users can search for the master feed on their podcast app or visit changelog.com/master to subscribe.
• Practical AI is hosted by Daniel Whitenack and Chris Benson, with music provided by Breakmaster Cylinder.
• The podcast is sponsored by Fastly, Vaughn Starkly, and Linode.