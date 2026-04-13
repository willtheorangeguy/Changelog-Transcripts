• Hosts Chris and Daniel discuss the AI community and machine learning
• Chris shares his experience building an AI workstation from scratch
• Discussion of NVIDIA's 30 series GPUs and their scarcity
• Shared story of a person trying to purchase one, including attempts at virtual shopping together on Best Buy
• Announcement of partnerships with Leno cloud servers and other sponsors
• GPUs in AI workstations
• Accelerating training and inference with NVIDIA GPUs
• Challenges with limited availability of GPUs
• Using a workstation with two GPUs for model training
• Intel-based edge devices and testing models on them
• SSH connections to remote computers and workflow implications
• Port forwarding and network setup issues with Comcast Xfinity router
• Alternative solution: connecting machines to IT closet network
• The speaker hasn't used their primary workstation for its intended purpose, but rather uses it as a remote SSH server to do work on their laptop.
• The workstation is not optimized for resource-intensive tasks like training workloads, which can consume a lot of memory and GPU resources.
• The speaker's motivation for building the workstation was not just practical, but also nostalgic - they enjoyed building computers in college and wanted to experience that again.
• They also appreciated having an opportunity to learn about new computer hardware and technology.
• Break-even point for using GPUs in the cloud vs building a workstation
• Affordability of solutions for using GPUs in the cloud (e.g. PaperSpace, Google CoLab)
• Comparison of costs between cloud-based GPU usage and self-built workstations
• Factors influencing decision to build a deep learning workstation, including team needs and cost savings
• Research into prebuilt deep learning workstations from companies like Lambda Labs and System 76
• The speaker is looking for a lower-cost alternative to prebuilt deep learning computers
• They came across blog posts by Jeff Chen and Curtis Northcutt with suggestions on building their own custom workstations at a lower cost
• Two GPU configuration was chosen, aiming for expandability in the future
• Single-GPU training runs were prioritized due to the time-consuming setup required for multi-GPU training
• The two-GPU setup allows for concurrent training runs by multiple team members
• Future plans include exploring multi-GPU capabilities and utilizing NV link technology
• The speaker mentions future workloads as a factor in choosing hardware
• The need for a motherboard that can support two GPUs with expandability
• A blog post by Jeff Chen on building a workstation is referenced and found to be relevant despite some outdated information
• The importance of considering tradeoffs, including expandability and ventilation, when building a system
• The speaker's choice of Gigabyte Motherboard and Aorus brand for their system
• The consideration of ventilation capabilities with GPU placement and the two main types of cards (blower style and non-blower style)
• The potential for increased performance by choosing blower-style GPUs
• The importance of proper airflow and fan placement to manage heat with multiple GPUs
• PCIe lanes and their importance for supporting multiple GPUs
• Motherboard and CPU compatibility for sufficient PCIe lanes
• Storage and RAM considerations when building a machine
• Power supply requirements for powering GPUs
• Case design and airflow (or lack thereof) impacting performance
• Cooling options, specifically air coolers vs. liquid cooling systems
• The speaker has a workstation with an AMD GPU and is experiencing issues with power cables sticking out of the side of the case.
• They are considering upgrading to an Intel-based system for better performance in certain tasks, particularly multi-threaded applications.
• The speaker notes the trade-off between single-core speed and multi-core processing power between Intel and AMD processors.
• They discuss their workflow, which involves using both TensorFlow and PyTorch frameworks, Amazon S3 or Digital Ocean Spaces for storing training data, and pre-processing that data on an Intel-based system before running it through models.
• The speaker reflects on the importance of considering other aspects of a workflow, such as model optimization and pre-processing, in addition to hardware choices.
• Discussing the benefits of local workstation setup for model training
• Using Docker to isolate environments and manage dependencies
• Managing GPU utilization and potential future upgrades
• Automating workflows for tasks such as spoken language identification
• Exploring options for pipeline automation (Packaderm, Allegro AI)
• Monitoring and logging (Tensorboard, Weights and Biases)
• Cost-benefit analysis of the workstation setup vs. cloud computing
• Filling up storage space with speech or video data can be easier than expected
• Using cold storage for large amounts of data is a good idea
• Personal experience with storing 1 terabyte of data and its benefits (e.g., reduced heating costs)
• Invitation to join the community Slack channel and share knowledge about AI
• Sponsors and closing remarks