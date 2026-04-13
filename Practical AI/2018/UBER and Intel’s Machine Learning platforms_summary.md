• Movidius is an Intel subsidiary that specializes in visual processing units (VPUs) for edge AI
• The company focuses on machine learning and computer vision at the edge
• Customers use Movidius' VPUs for applications such as digital security, smart cities, drones, robotics, and camera devices
• There are challenges in porting neural networks to embedded silicon, including a tradeoff between portability and performance
• Researchers often optimize models on large datasets like ImageNet, but these may not be suitable for edge devices with limited resources
• Discussing classification problems and how they differ from large-scale tasks like ImageNet
• Domain transfer: applying models to smaller-scale problems with reduced complexity
• Techniques for reducing model size and improving efficiency: pruning, sparsification, quantization
• Tools and resources available for model optimization: Distiller (Intel's open-source project), PyTorch, TensorFlow contrib
• State of the art in specialized hardware support: FPGAs, GPUs, VPUs
• Quantizing networks for edge devices
• Techniques for improving model performance on different silicon
• AutoML and learning models for specific silicon capabilities
• Movidius' Neural Compute Stick and its applications
• Edge AI use cases: water filter, shark detection, medical imaging
• Future prospects: advancements in inference silicon and metrics
• Compute sticks with low power and price points
• Future of compute capabilities and potential market developments
• Introduction to Michelangelo, a machine learning platform developed at Uber
• Challenges faced by data scientists in productionizing machine learning models
• Need for an unified ML platform like Michelangelo to simplify the process of building and deploying models
• Goals of Michelangelo to bring data science best practices to the platform and make it easier for data scientists to build reproducible, scalable, and maintainable models.
• The platform supports various machine learning use cases across the company, including fraud detection and Uber Eats ranking
• There are over 100 ML use cases on the system, but it's difficult to determine how many are fully productionized
• The feature store is a key part of the platform that has gotten disproportionate adoption and allows for collaboration, visibility, and feature sharing
• Data scientists previously didn't have insight into feature pipelines built by others, but now can reuse existing features and collaborate more easily
• Building an ML platform requires both software engineering expertise and machine learning knowledge
• The company's leadership was willing to invest in the development of an ML platform earlier than usual, allowing them to learn from mistakes
• Balance between data scientists' need for flexibility and productionized systems' need for stability
• Design philosophy of allowing data scientists to work within a system using relevant tools
• Providing APIs to ease transition from prototyping to production
• Monitoring models in production, including data science metrics and model drift detection