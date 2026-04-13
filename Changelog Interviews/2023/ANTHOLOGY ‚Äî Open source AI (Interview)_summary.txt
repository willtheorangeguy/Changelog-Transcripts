• Sourcegraph's evolution from code search to intelligence platform
• The company's 10-year history and its original mission to enable everyone to code
• The impact of large language models on search and the potential for combining LLMs with code search
• The development of plugins to enable large language models to browse the web on behalf of users
• The integration of large language models with Sourcegraph's code search engine to provide context-aware and specific answers about code
• The timeline of the development of large language models and how Sourcegraph began experimenting with them around 12-18 months ago
• Cody's development began about a year ago as an experiment, with a significant inflection point when ChatGPT was released.
• The chat interface is seen as a simple yet powerful way to interact with software development tools.
• The technology behind Cody is based on language models, which provide a beginner-friendly interface to advanced code understanding and modification capabilities.
• Sourcegraph is rethinking its user interaction layer, with Cody as the first iteration of this thought process.
• Cody is an AI editor assistant available as a free extension for VS Code, with plans to support other editors like IntelliJ and Neovim.
• The technology is open source and Apache-licensed, with development happening in the open.
• Sourcegraph provides backend services and language model providers
• Cody uses Sourcegraph for better intelligence, but still functions standalone
• Cody fetches context from local code, and uses non-Sourcegraph mechanisms if standalone
• Cody reads documentation and source code to answer questions
• Question answering is done in real time, with typically one or two seconds latency
• Sourcegraph's design philosophy is to avoid strong coupling and selling more software
• Privacy is extremely important to Sourcegraph, and zero retention policies are in place
• Data is not used as training data for language models, and is forgotten after request completion
• Users have control over their data, and can opt-in to usage
• Terms of Use and license are explicit and clear about data usage and retention
• ChatGPT used to summarize lengthy legal documents
• Cody's chat-based input and ability to read related files in a codebase give it a competitive edge over Copilot
• Sourcegraph's open source and model-agnostic approach allows for better context switching and access to a growing market
• Anthropic's new version of Claude has a large context window, which will be integrated into Cody
• Cody's focus on high-level questions, onboarding, and rubber-ducking use cases sets it apart from Copilot
• Sourcegraph's approach to model integration and copyright code detection may sidestep legal concerns related to proprietary models
• Future plans for Cody include integrating more context and expanding into the model layer for code generation.
• Cody's capabilities in code generation and interaction
• The potential for Cody to incorporate search engines into its training process
• The limitations of current AI tooling, including "Whack a Mole" problems and combinatorial complexity
• The future of coding, with a potential spectrum of people from basic description to core kernel development
• The accessibility of code creation and the flattening of the tech landscape
• The role of humans in coding and the necessity for collaboration with AI tools
• The efficiency of language models, with a bicycle being a more efficient mode of transportation than a cheetah, is used as an analogy for the power of language models
• Cody, a language model, is a game-changer for Sourcegraph's go-to-market and sales motion, making it easier for non-technical stakeholders to understand complex code
• The growth of Sourcegraph's total addressable market has increased due to Cody's ability to explain code in English
• The future of coding may involve more human-AI collaboration, with language models and traditional coding being complementary rather than competitive
• Hybrid systems that combine the strengths of language models and traditional coding may emerge, and will be more powerful than either one alone
• Denny Lee's procrastination methods, or rather his "efficiency" approach to creating presentation slides just before the actual presentation
• The development of Dolly, a conversational AI, and its evolution from Dolly 1.0 to Dolly 2.0
• The initial idea behind Dolly 1.0, which was to fine-tune an older model with good data and achieve good results at a low cost ($30)
• The limitations of Dolly 1.0, which relied on non-public data, and how the team generated their own data using employee contributions (Dolly 2.0)
• The cost-effectiveness of Dolly 2.0, which achieved good results at a cost of $100 in training
• The comparison between Dolly 2.0 and ChatGPT 4.0, with Dolly 2.0 providing concise and correct answers
• Using ChatGPT's web UI vs. developing a custom interface
• Dolly's data collection process using Google forms
• Formatting data for Dolly to understand, including specific questions and answers
• Using M1 Macs for inference with Dolly
• Databricks notebook for running Dolly vs. Hugging Face instructions
• Optimizing Dolly for M1 Macs and dealing with bugs in PyTorch
• Bias in data collection and the importance of verbosity in providing context
• Number of instructions and data points used in Dolly's training
• Surprising effectiveness of Dolly's training with a relatively small dataset
• Discussion of using open source models and fine-tuning them for specific use cases
• Benefits of keeping data as intellectual property and maintaining user privacy
• Microsoft and Open AI's introduction of concepts allowing data owners to pay for training and not give away their data
• The idea that companies can build their own models and avoid giving away data to other services
• ChatGPT's value as a tool for general consumers and professionals
• Databricks' role as a platform to simplify data processing and access to various open source systems and services
• Databricks' stance on data ownership and the importance of keeping data as a competitive advantage
• Use of language models, such as OpenAI and Dolly, for tasks like generating blogs and summarizing conversations
• Importance of transparency and understanding when to use pre-trained models versus building own models
• Discussion of Dolly's ability to learn and adapt to a company's style and tone
• Comparison of different language models, including ChatGPT and Vicuna, and their strengths and weaknesses
• Use of Nat.dev as a playground for testing and comparing different models
• Personal experiences and anecdotes about using language models and AI tools
• Open source AI community's need for help from non-AI experts
• Funding for AI research and model training
• Cost of training large language models
• Open source model training and release
• Importance of open source research and infrastructure
• OpenFold project and collaboration with DeepMind
• Large language model training and evaluation
• Companies are developing and releasing large language models, including Mosaic, Meta, and Stability AI.
• The speaker's company created a model suite, Pythia, designed to enable scientific research on language models, with consistent properties and intermediate checkpoints.
• The Pythia suite is trained on publicly available data, with the same data used for all models, and allows for the study of memorization and understanding of model behavior.
• The speaker's research focuses on understanding where language models come from and how to design them, with goals of predictability, control, and designability.
• The field of interpretability is important for understanding and designing language models, with a need for transparency, reproducibility, and ability to inspect individual data points.
• The speaker's company made a significant effort to reproduce their model training exactly, allowing for a deeper understanding of model behavior and design.
• Recent paradigm shift in AI with GPT-3's release and focus on scaling
• Importance of being prepared for future paradigm shifts and potential dangers of AI
• Discussion of the EleutherAI research institute and its work on language models and AI
• Invitation to join the EleutherAI Discord server for public research and collaboration
• Overview of ongoing research projects and areas of focus, including language model interpretability and red-teaming
• Call for volunteers and involvement with the research institute