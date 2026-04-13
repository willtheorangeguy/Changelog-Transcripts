• Introduction to the podcast and sponsors
• Overview of O'Reilly's online learning platform
• Announcement of a special episode on Numerical Elixir (nx) from the Changelog podcast
• Interview with Jose Valim, creator of Elixir, about nx and its features
• Discussion of nx as a library for machine learning, data science, and numerical computing in Elixir
• Explanation of multi-dimensional tensors and their importance in representing images and other complex data
• Description of numerical definitions, a subset of Elixir that can compile and guarantee immutability.
• Building on numerical computing and neural networks capabilities
• Releasing bindings for TensorFlow (XLA) and PyTorch (LibTorch)
• Introducing new libraries: Axon for high-level neural network building, Live Book Two for interactive coding notebooks
• Elixir's ecosystem growth, expanding to various domains beyond web development
• Motivation for incorporating AI/ML capabilities into Elixir, driven by community demand and interest in broader applicability
• Historical context of Elixir's origins from the Erlang Virtual Machine, its use cases in concurrent systems, and expansion into new areas
• Discussion of using a platform for machine learning tasks
• Bringing numerical computing capabilities to the Elixir programming language
• Avoiding the need to switch between languages (e.g. Python) for tasks like inference
• Comparison of Python's dominance in AI/ML and its potential drawbacks
• Acquiring knowledge and taste for new domains (e.g. numerical computing in Elixir)
• Collaboration on a project involving Sean, Jackal, and others to develop Elixir-based tools for deep learning
• JAX, a Python library from Google, potentially replacing TensorFlow as a next big library
• JAX designed to be used with functional programming style, but has immutable arrays unlike NumPy
• Functional programming concept allows for building computation graphs and emitting specialized code
• Speaker discovered the idea of functional programming through reading JAX documentation and a book on genetic algorithms in Elixir
• Immutability was initially seen as a negative aspect, but turned out to be a feature in Elixir implementation
• Pitfalls in JAX include inability to record certain operations, such as setting properties or passing objects to conditionals
• Elixir's immutability and use of macros allow for rewriting code to run on GPU without pitfalls present in JAX
• Speaker developed tools using Elixir and JAX, finding advantages in Elixir's immutable data structures
• New tool, Axon, built on top of NX (Nerves X), is a neural network library based on NX
• Sean built a neural network framework in Elixir called Axon
• It's a high-level API with building blocks for functions, including initialization, optimizers, layers, and activations
• Axon is designed for ease of use, similar to Keras or PyTorch
• The framework includes examples for classical machine learning datasets (e.g. MNIST, Fashion MNIST) and algorithms (e.g. ResNet)
• Interoperability between different frameworks is a key consideration in the design of Axon
• Sean's work on Axon has inspired a discussion about the importance of interoperability in AI development
• The speaker discusses the use of interoperability between Elixir and other frameworks, specifically for running machine learning models.
• Elixir is capable of running on embedded devices with Nerves framework, and has potential in edge AI applications.
• The necessity of serialization and model deployment from a central location to an embedded device is discussed.
• The Onyx library, which provides serialization functionality, is mentioned as being worked on by the Elixir community.
• A discussion ensues about the development process and approach taken for building the Axon library, focusing on its ability to support multiple layers and operations with ease.
• The speaker attributes this success to the high-level abstraction of functions built on top of each other, allowing for rapid composition and implementation of new features.
• The speaker thinks that the Axon API is trying to be familiar with other existing projects in the AI world
• Inspiration for Axon's design comes from various sources, including ThinkAI, Spacey, and PyTorch/Lightning
• The use of Elixir as a programming language and its potential benefits for building AI applications are discussed
• The need for an equivalent to data frames and plotting libraries in the Axon ecosystem is mentioned
• The speaker explains the concept of LiveView, a framework for building interactive real-time applications with Phoenix, and how it can be used to build collaborative notebooks like Livebook
• A humorous anecdote about someone setting up a GitHub request without asking is shared
• Replacing jQuery with JavaScript in Livebook
• Collaborative and interactive applications in Elixir
• Features of Livebook, including reproducibility and explicit dependencies
• Addressing issues with notebooks, such as managing state and execution flow
• Inspiration from other projects, including DrupTer Notebooks, Pluto.jl, and Deep Note
• Jonathan's live view application was built in three months while studying and working part-time
• Live Book has features like auto completion, collaborative coding, and distributed capabilities
• The notebook approach is different from others (e.g. nx and exon) and leverages Elixir's strengths
• Out-of-the-box functionality allows notebooks to work distributed without external dependencies
• Future plans include shipping Docker images and a command-line executable with configuration flags
• Production notebooks are becoming more prevalent, and the speaker hopes to explore graphing, data frames, and other related topics
• Integration with TensorBoard for visualizing training data
• LiveBook as a marketing and collaboration tool
• Sequential evaluation limitations in notebooks
• Branching and forking in notebooks for multiple tasks
• Pluggable file systems, including GitHub integration
• Collaboration features, such as hosting notebooks on GitHub
• Community involvement and contribution opportunities
• Machine learning working group and discussion forums
• Discussing the Erlang ecosystem and its openness to new ideas
• Bringing machine learning tools to Erlang, specifically through the use of Elixir's Nif interface (Nif)
• Exon, a library for building neural networks in Erlang with no performance cost
• Potential crossover from the Python world into Erlang due to increasing openness to alternative ecosystems