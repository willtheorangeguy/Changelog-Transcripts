• The complexity of optimizing models for different hardware targets
• Machine learning-based optimizations to learn about hardware behavior
• Compiling models on specific hardware, searching for optimal ways to optimize and tune the model
• Resource constraints and optimization challenges in different deployment scenarios (edge devices, cloud, on-prem)
• Joint all-domain operations (JADO) as a concept related to AI in the defense industry
• Luis Cezé is interviewed as co-founder and CEO of OctoML and professor at University of Washington
• Discussion about weather in Seattle and its contrast with other parts of the country
• Luis shares his background, from growing up in Brazil to working at IBM Research on the Blue Gene Project
• He talks about his work on hardware software co-design, high-performance linear algebra, and speculative parallelization
• He discusses his transition to research on machine learning, energy efficiency, and performance optimization for AI
• Growing set of machine learning models and hardware targets six years ago
• Fragmentation in ecosystem with TensorFlow and PyTorch
• Need for common intermediate representation for high-level model optimization and specialized code generation
• Genesis of the TVM project through research on machine learning model optimization and compilation
• Importance of linear algebra in machine learning and role of approximate computing
• Machine learning compilers and intermediate representations explained
• Machine learning compilers aim to squeeze more performance out of hardware
• They treat the process of translating a model into executable code as a compiler problem, enabling optimizations
• Optimizations can include fusing layers, generating new code, and quantization
• Performance is ambiguous and can refer to either speed or accuracy; machine learning compilers generally do not change accuracy
• Apache TVM uses machine learning-based optimizations to automate the process of compiling models for deployment
• The process of getting a model ready for deployment can be laborious and take weeks/months of software engineering work, which Apache TVM aims to automate
• Snowplow Analytics: behavioral data management platform
• Apache TVM: compilation process for models
• Model serialization and deployment: discussing formats (Onyx, PyTorch, TensorFlow) and interfaces with TVM
• Workflow of compiling a model in Apache TVM: ingesting serialized models or calling TVM directly from code
• Optimization and inference: CVM's high-level and low-level optimization magic and machine learning for machine learning engine
• Output after compilation: executable code for the model, including model and runtime
• Limits on target architecture: discussion of low capability or low power targets (e.g. Raspberry Pi)
• Hardware targets and model optimization for inference
• Custom binary packaging with CVM for models
• API calls for model inference and shared libraries (DLLs)
• Edge device limitations, including memory and compute constraints
• Model compression techniques: sparsity, quantization, and pruning
• OctoML platform for hardware-agnostic model deployment and optimization
• Inference with Apache TVM is as simple as two lines of code
• The Octomizer offers a high-level service for model optimization compilation
• It provides an API call to embed the optimization process into any workflow
• OctoML was formed to invest in and grow the Apache TVM ecosystem
• The company aims to make machine learning model optimization accessible to a broad set of users through open-source collaboration
• Discussion of how machine learning moves quickly and models change frequently
• Introduction to OctoML as a SaaS offering for packaging and optimizing machine learning models
• Explanation of Apache TVM as an open-source project for compiler and auto-tuning capabilities
• Overview of the Optimizer, a full SaaS offering for automating model optimization
• Comparison of using the Optimizer versus working with the open-source Apache TVM project
• Discussion of Onyx, a model serialization format used by OctoML and other frameworks
• Mention of Changelog++ as a way to support practical AI and access exclusive content
• Momentum around Onyx for model description languages
• Benefits of having a widely adopted format for storing models
• Rapid evolution of the field with new frameworks and architectures emerging
• Importance of strong community and collaboration to keep up with changes
• Role of Apache TVM in automating hardware-specific tasks for hardware vendors
• Benefits of open-source contributions from industry players due to professional governance
• The importance of open source communities in dealing with growing diversity
• Recruiting early users and truly listening to their feedback
• Clear differentiation from existing tools and communicating unique value
• Building relationships with hardware vendors, such as ARM and NVIDIA
• Leveraging community support for popular hardware, like Raspberry Pi
• Benefits and challenges of using QDNN vs TVM native code
• Importance of a clean code generation interface for new hardware vendors
• Advantages of using Apache TVM, including community support and ease of use
• Emerging hardware vendors' need to choose between building internal compilers or using TVM
• Exciting developments in AI industry, including harder aware network architecture search and automation in data management
• Reconfigurable architectures on the horizon, such as CPUs, GPUs, and accelerators
• FPGAs (Field-Programmable Gate Arrays) and their increasing relevance in machine learning
• Excitement around FPGAs being tuned for machine learning applications, with companies like Xilinx and Altera leading the way
• Machine learning's potential to enable large-scale genomics studies and complex data analysis
• Using machine learning to design systems, such as molecular systems and aircraft
• Reverse engineering and reverse design techniques enabled by machine learning
• Opportunities in using machine learning for machine learning improvements
• Potential for using machine learning to optimize chip design and training systems
• Machine learning's tolerance to noisy execution and its implications for future technologies
• Return from break announced multiple times
• "Game on" statement at end of session