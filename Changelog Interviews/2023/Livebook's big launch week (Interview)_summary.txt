• José Valim's current focus on Nx and Livebook
• Connection between Numerical Elixir and Livebook
• Pretrained machine learning models in Elixir
• Use of Livebook for running machine learning models
• José Valim's validation of decision to focus on machine learning and Nx
• Elixir's suitability for machine learning and numerical computing
• Implementation of Stable Diffusion and Whisper in Elixir
• Benefits of integrating machine learning into Elixir apps
• Discussion of Jerod Santo's experiences with Elixir and Phoenix
• Distributed Erlang and running machine learning tasks on specific machines with GPU
• Whisper and speaker identification
• Hugging Face as a repository of machine learning models and a platform for deploying and running models
• BumbleBee as an Elixir library for working with Hugging Face models
• Nx as the base library for Numerical Elixir
• Running models on a cluster with multiple nodes and managing model distribution
• Hugging Face's concept of model parameters and weights, and their implementation in the Hugging Face Transformers library
• Hugging Face Spaces for running custom Docker images with GPU
• Inference APIs and services provided by Hugging Face
• Large language models like LLaMA require support for integration
• José Valim explains Elixir's subset that compiles to the GPU
• Axon neural network library and BumbleBee models are built on top of Nx library
• José Valim discusses the abstractions of the infrastructure, allowing for efficient re-use of parts from other models
• Livebook launch week was inspired by Supabase and allowed for focused content release and discussion
• José Valim compares Livebook launch week to having a child, with mixed reactions at different stages
• Livebook is a code notebook platform for Elixir that combines data, machine learning, and coding in a single interface
• Livebook has a desktop app and a browser-based interface, allowing users to write notebooks with a mix of prose, text, documentation, and code
• The platform has a feature called Smart cells, which allows users to execute code with a UI, but with a focus on visibility and transparency
• Smart cells are inspired by the idea of metaprogramming and are meant to bridge the gap between machine learning developers and Elixir developers
• The goal of Livebook is to allow developers to focus on the task at hand, regardless of whether they use a UI or write code by hand
• The platform has a feature called Explorer, which is part of the launch week and allows users to interact with data and code in a more dynamic way
• Livebook's live cells are implemented using a separate library called Kino
• Livebook has a runtime that runs Elixir code, which doesn't know much about the web application
• Smart cells in Livebook are essentially iFrames that can run any JavaScript, with most using Vue.js
• Livebook's architecture is designed to be extensible, allowing users to create their own Smart cells and outputs
• The Explorer tool brings data frames and series to Elixir, using the Polars library in Rust and inspired by the R community's DeployR API
• The Numerical Elixir project involves data massaging and manipulation before feeding it into a machine learning model.
• The Explorer library is a graphical user interface (GUI) for data manipulation, but users struggle to learn and use it.
• The Smart cells feature allows users to create a workflow for data processing and visualization without writing code.
• The goal is to make the Explorer library extensible and easy to use, allowing users to drag and drop files (e.g. CSV, JSON, SQLite) and automatically generate code for data processing.
• The library will eventually support features like chart suggestions and improved plotting.
• Elixir has bindings for image manipulation libraries like OpenCV and VIPS, which can be used for tasks like image resizing and cropping.
• Explanation of how Explorer decides where to run code, CPU or GPU
• Numerical definitions in Elixir and how they allow for compilation to CPU or GPU
• How Explorer uses Google XLA to compile code to CPU or GPU
• Explorer as an Elixir library for one-dimensional and two-dimensional data frames
• Livebook using Explorer to build on top
• Distributed machine learning notebooks with Elixir and Livebook
• Development of Distributed² machine learning models in Elixir
• Technical features of Distributed², including concurrent and distributed software
• The team behind the project, including José Valim and Dashbit
• Revenue and marketing strategies for the project
• José Valim discusses how a certain book changed his life but he never read it
• The conversation shifts to the development of Elixir projects, including Numerical Elixir and Explorer
• José Valim mentions various team members, including Paulo Valente, Chris Grainger, and Philip Sampaio, working on different projects
• He also discusses Livebook, BumbleBee, and Jonatan Kłosko's involvement in these projects
• José Valim shares his past experiences as a musician and band member with Hugo, including their band's music style and instrumentation
• The idea of José and Hugo performing at ElixirConf is discussed
• The conversation turns to the financial side of the open-source projects, with José Valim mentioning Dashbit's service as a source of funding
• He explains the plan to make Livebook Teams a paid service for collaboration and deployment
• José Valim discusses plans for a beta launch of Livebook in the second semester and notes that the team is not in a hurry
• José Valim shares his experience with VC interest in Livebook, attributing it to the product's focus on data and notebooks
• He explains how Livebook's immutable nature by default allows for reproducibility and enables specific tooling, such as smart cells and caching
• José Valim expresses concerns about attracting VC investment, worried that it would create pressure to grow and potentially dilute the product's focus on Elixir
• The discussion turns to the Whisper audio processing tool, with José Valim mentioning plans to work on automatic audio segmentation and Jerod Santo bringing up the topic of speaker identification
• Jerod Santo expresses interest in speaker identification and suggests exploring tools like Pyannote
• Discussion of difficulties in implementing transcript generation for podcasting
• José Valim and Jerod Santo discuss potential solutions using existing tools and services
• José Valim expresses patience and interest in waiting for a suitable solution to arise
• Mention of Hugging Face models and potential integration with Livebook
• Personal anecdotes about podcast listening habits and speed adjustment
• Discussion of Livebook's potential and future applications