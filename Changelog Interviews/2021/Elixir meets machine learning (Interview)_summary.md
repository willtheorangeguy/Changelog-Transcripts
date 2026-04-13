• José Valim introduces Nx, a library for numerical computing, machine learning, and data science in Elixir
• Nx includes multi-dimensional tensors and numerical definitions for efficient GPU computation
• José Valim discusses the inspirations for Nx, including Jax and Google XLA
• Nx has bindings for EXLA (Google XLA) and is working on bindings for PyTorch (LibTorch)
• Other libraries released by Nx include Axon (high-level neural network library) and LiveBook (interactive and collaborative code notebooks)
• José Valim explains the motivation for developing Nx, driven by the desire to expand the capabilities of Elixir and make it a more diverse and powerful language
• Expanding Elixir's capabilities to include data processing and machine learning
• Bringing machine learning to Elixir to provide a more comprehensive toolset
• José Valim's interest in broadening Elixir's domains and areas of use
• Collaboration with Sean Moriarity on developing Elixir-based machine learning capabilities
• Comparison with existing Python libraries and tooling for machine learning and data science
• Goal of making Elixir a more viable option for developers working in machine learning and data science
• Discussion of the potential for Elixir to replace Python in certain areas of AI and machine learning development
• The speaker and Sean discovered the Jax library and its functional programming style, which led to the development of Nx, a numerical computation library for Elixir.
• Jax's computation graph approach is discussed, where the library builds a graph of operations and then compiles it to run on the GPU.
• The speaker notes that immutability in Elixir is a key feature that allows Nx to avoid some pitfalls present in Jax, such as the tape pattern.
• Axon, a neural network library built on top of Nx, is introduced, which allows users to build and train neural networks using a high-level API.
• The speaker expresses a desire for a GPU to run some examples in Axon, but is currently hindered by supply chain issues and NVIDIA's recent changes to their GPU lineup.
• Introduction to Axon, a high-level API for building machine learning models in Elixir
• API design and usability, including interoperability with other frameworks (e.g. PyTorch, TensorFlow)
• Serialization of models to multiple formats, including ONNX
• Potential use cases for Axon in edge computing and embedded systems
• Collaboration and community involvement in Axon development
• History and development timeline of Axon and related projects (Nx, XLA)
• Productivity and efficiency in building machine learning libraries, comparing Axon's approach to others in the field
• Axon's API is designed to be familiar and build upon existing knowledge
• Inspiration from other projects, such as Think AI in Python and PyLightning
• Diversity of AI models and frameworks, with consistent architecture patterns
• Axon's design goal of being easy to understand for developers outside of the Elixir community
• Development of LiveBook, an interactive and collaborative notebook for Elixir
• LiveBook's features and goals, including real-time collaboration and interactive data inspection
• Plans to expand LiveBook's capabilities to include interactive data analysis and neural network training
• Problems with Jupyter notebooks, including formatting, version control, and dependencies
• LiveBook, a new approach to collaborative notebooks with features like explicit dependencies and reproducibility
• Inspiration from other tools, including LiveMarkdown, Jupyter Notebooks, Pluto.jl, and Deepnote
• LiveBook's use of LiveView and Monaco editor for autocompletion and collaborative features
• Distributed notebooks and ability to run on multiple machines
• Plans for future development, including graphs and data frames
• Challenges of supporting notebooks in production environments
• Erlang Ecosystem Foundation Machine Learning Working Group
• LiveBook features and limitations, including sequential evaluation and collaboration
• Integration with tools like TensorBoard and potential for unified monitoring of training runs
• Collaboration features, including GitHub integration and pluggable file systems
• Nx and its role in bringing machine learning tools to Erlang and Elixir
• Community and involvement opportunities, including Discourse forum, Slack, and monthly meetings
• José Valim's work on building a neural network in Erlang using Axon and Nx
• Possibility of cross-over from the Python world to Erlang for AI development
• Plans for Daniel Whitenack to try out and share José's work with the Practical AI community
• Links to José's LiveBook demo and the Erlang Ecosystem Foundation in the show notes