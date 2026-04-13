• The Linux Foundation's Open Source Summit North America 2023 in Vancouver, Canada, is discussed
• Open source AI is the common denominator of conversations, featuring Byung Liu, Danny Lee, and Stella Biederman
• Byung Liu's team at Sourcegraph is working on Cody, a completely open source model agnostic coding assistant
• Databricks has released Dolly 2.0, the first open source instruction following LLM fine-tuned on human-generated instruction data
• Stella Biederman gave a keynote address on generative AI and model training, and AI ethics
• DevCycle's CTO and co-founder Jonathan Norris discusses the company's uptime reliability and feature flagging tool
• Cody is a significant interest and a big deal, following Sourcegraph's relaunch as the intelligence platform
• Sourcegraph's 10-year history and its mission to enable everyone to code
• The company's early vision and how it has evolved over time
• The role of large language models in changing the way developers find information and create code
• The trade-offs between search engines like Google and large language models like ChatGPT
• The limitations of ChatGPT, such as its reliance on outdated data and its lack of context in search results
• Discussion of the capabilities of language models, specifically ChatGPT, with plugins enabled
• Combination of large language models with code search engines
• Benefits of this combination, including highly context-aware answers and code generation
• History of the development of large language models, including the release of GPT-3
• The author's background in computer science and machine learning
• The development of Cody, a tool combining large language models and code search engines
• Potential impact of this technology on software development and engineering
• Discussion of how humans learn and leverage technology
• Chat interfaces as a simple, yet effective way to access powerful tools
• The author's background as a programmer and his enthusiasm for textual input
• Comparison of textual input and graphical input (e.g. mouse, 4K screens)
• Importance of human agency in programming computers
• Evolution of tools like Kodi to become rich REPLs (Read-Eval-Print Loops)
• Future of Sourcegraph as a tool that integrates various sources of information
• Discussion of the company's past decade of building advanced code understanding tools
• The on-ramp to using powerful tools has historically been difficult due to the need for education and steep learning curves.
• Language models have made it easier to provide powerful tools without requiring extensive education.
• Sourcegraph is rethinking the user interaction experience to take advantage of language models.
• Cody is the first iteration of this new user interaction, a conversational AI editor assistant.
• Cody is an open-source extension available for download in the VS Code marketplace, with other editors to follow.
• The extension provides features such as inline completions and chat functionality, using the language model's knowledge and the user's code base context.
• Cody fetches context from local code and Sourcegraph
• Cody gets intelligence from local codebase as an extension
• Cody uses a language model to understand the codebase
• Cody reads relevant pieces of documentation and source code from the codebase
• Cody answers questions in real-time, typically within 1-2 seconds
• Sourcegraph is fast and has no latency due to its classical CPU-based code
• Privacy is extremely important to the company, including individual developers and enterprise customers
• The company has zero retention policies with language model providers, ensuring data is never used as training data
• The language model providers forget user data as soon as the request is complete
• Sourcegraph has always taken user and code privacy seriously to serve enterprise customers.
• Language models have increased value and sensitivity of user data
• Users should have control and ownership over their data
• Large language models can "memorize" user data and potentially be used for malicious purposes
• Transparency and clear communication about data usage and privacy policies are essential
• A clear terms of use agreement is presented to users, but its clarity and length are discussed
• The company aims to be transparent and not hide important information from users
• The possibility of language models being used for nefarious purposes is acknowledged, but also their potential benefits are highlighted
• The company is planning to create specialized language models for various domains, including law and software creation.
• Comparison of Cody and GitHub Copilot
• Zero sum game vs non-competitive market
• Features of Cody that set it apart from Copilot
• Context window and model size of Copilot and Cody
• Open source and model agnostic approach of Cody
• Enterprise friendly and proxy friendly features of Cody
• Legal concerns and lawsuits related to Copilot and Cody
• Integration of models in Cody for different use cases
• Cody is a code search engine that can also detect copied code and flag it for users
• Cody is open-sourced to allow for integrations with various platforms and systems to pull in context
• Cody is expanding to include more context and integrating with AI tools for code generation
• The model layer of Cody is being explored for deeper capabilities, including chat-based completions
• Cody can currently generate code based on natural language instructions, but limitations emerge when adding custom features
• Future plans include allowing users to self-host Cody for large corporations with strict data retention policies
• Developing an app without writing code using natural language
• The challenges of coding with AI and the "whack-a-mole" problem
• Adding new features to the app using AI
• Predicting the future of AI and its potential impact on programming and society
• The spectrum of AI capabilities, from glorified autocomplete to AGI
• The potential for AI to empower more people to create software and change the way we think about programming
• The future of coding will be more accessible and "flat", like reading and writing on Twitter, with many different forms of coding
• The access to coding and AI will be democratized, allowing people to learn and level up quickly, regardless of background or experience
• Code and AI will become like a "patient sidecar" that can have conversations and assist humans in creative and problem-solving tasks
• This democratization of coding and AI will be a "fantastic thing" and will have a significant impact on society
• The author compares language models to a "race car" or "rocket ship" that can greatly increase an individual's productivity and leverage
• The growth of Cody has been "magical" and has addressed some of the challenges the company faced in getting programmers to adopt their product
• The author attributes the success of Cody to its accessibility and ease of use, which has bridged the gap between programmers and non-programmers
• The speaker discusses how Cody, a natural language interface, can explain complex code to non-technical stakeholders.
• The speaker mentions a pitch meeting with a Fortune 500 company where Cody was used to explain open-source libraries, impressing even a 30-year-out-of-touch programmer.
• The speaker predicts that in a few years, almost every human will be empowered to create software in some way.
• The speaker discusses the potential for language models to become the primary interface for coding, reducing the need for traditional coding skills.
• The speaker contrasts the strengths and weaknesses of language models, citing examples of their limitations.
• The speaker proposes a future where systems combine the strengths of language models and traditional coding, creating hybrid systems that are more powerful than either on their own.
• Acquisition of Code Cove by Sentry
• Role of Code Cove in developer lifecycle (before deploy time)
• Role of Sentry in developer lifecycle (after deploy time)
• Integration of Code Cove and Sentry
• Benefits of integrating Code Cove and Sentry (de-risking code changes and software)
• Onboarding process for teams to use Code Cove with Sentry
• Code Cove's analysis and reporting of code coverage
• CodeCov's ability to ensure code coverage across an entire team
• Promotion of Sentry.io with a free team plan for three months using code "changelog"
• Mention of CodeCov.io for code coverage
• Databricks discussion, specifically Dolly 2
• Author Denny Lee's presentation preparation habits and procrastination/efficiency debate
• The speaker and a colleague from Denmark gave a presentation together, but they had to put together their slides just 30 minutes before the session.
• The speaker has been able to get away with this approach so far, but acknowledges it may eventually "bite" them.
• The topic of the presentation is Dolly, a model that allows for fine-tuning an older model with good data to get good results, saving millions of dollars in training costs.
• Dolly 1.0 was successful in achieving good results with a minimal amount of data, leading the team to generate their own data.
• The team generated their own data by having employees contribute to a Q&A format, which was used to train the model.
• The data generated was used to train Dolly, and the team was able to share the weights and model with others, but not the data itself due to its proprietary nature.
• The conversation discusses the Dolly 2.0 model, a chatbot that can answer questions
• Dolly 2.0 is a clone of Dolly, the first sheep to be cloned
• The model is used to generate 15,000 Q&A pairs, which are then used to train the model
• The model is trained using a old model from two years ago and costs $100 to train
• The model is compared to ChatGBT4.0, which is found to be more verbose but equally correct
• The conversation discusses the use of the model, including how to download and run it using Databricks or Hugging Face
• The conversation also touches on the limitations of the model, including its tendency to provide long answers and the need for users to be able to control its verbosity.
• Optimizing a model for M1 Mac performance
• Bug in model causing garbage answers
• Fixing the bug
• Collecting and formatting data for Dolly to understand
• Asking specific, detailed questions for Dolly to provide accurate answers
• Example of asking questions to gather information about making great espresso
• Addressing bias in the data and answers provided by Dolly
• Importance of verbosity in providing context and proof for training models
• Limitations of training large models with vast amounts of data
• Dolly1.0's surprising performance with minimal training data
• Business benefits of using open-source models to maintain data ownership and privacy
• Fine-tuning large language models for specific use cases
• Availability of various open-source models from companies like Hugging Face
• Cost-effectiveness of using open-source models with smaller training data sets
• Concerns about data ownership and privacy when using third-party services
• Positive mention of Microsoft and OpenAI's contributions to the field
• Discussion about paying more for data and its perceived value
• Mention of the "no moat" concept and how it relates to the overemphasis on collecting large amounts of data
• Criticism of the idea that companies must collect massive amounts of data to train models
• Suggestion that foundational models can be fine-tuned with a smaller amount of data and be effective
• Idea that companies trying to build a moat around themselves are actually giving away their competitive advantage
• Discussion of the benefits of building one's own model and not relying on third-party services
• Mention of using ChatDB and other services for convenience and value
• Discussion of the future of AI and data processing with Databricks' angle being the importance of ETL and data processing.
• Databricks' purpose is to make it easy for users to process and access large amounts of data, regardless of the technology used.
• The company believes in open-source systems and services, and users should own their data.
• Data should be a competitive advantage, and services like OpenAI can be useful, but users should know what they're doing.
• Databricks provides a platform that makes it easy to use services like OpenAI within a database platform.
• The company suggests that users should understand when to use a service and when to build their own model.
• The use of Dolly 2.0, an open model, can be leveraged for personal betterment, such as generating blogs based on transcripts.
• Databricks makes it easy for users to build, maintain, train, and infer against their own models.
• The company's goal is to simplify the process of synthesizing key points from conversations.
• Reviewing and validating AI model output
• The potential of open-source models like Dolly to simplify processes
• Using AI models to generate content based on user style and transcripts
• The importance of choosing the right foundational model for specific tasks
• Nat Friedman and the Nat.dev playground for testing and comparing different models
• The value of experimentation and testing to determine the best model for a particular use case
• The CentOS project was pivoted due to business agenda and commercial needs, causing a significant pain point in the industry.
• The Rocky Linux and RESF (Rocky Enterprise Software Foundation) were created to ensure that similar issues do not happen again.
• The RESF is a community-run organization that governs the management of Rocky Linux and other projects.
• Eleuther AI, a non-profit organization, has trained several large open-source language models, including Pythia.
• Eleuther AI is seeking help from the open-source community to address issues related to maintainability, licensing, regulation, and sustainability in the AI ecosystem.
• The organization is promoting foundation models and large language models, and encouraging people to get involved and contribute to the open-source work needed to build a robust and enduring ecosystem.
• Donations from companies such as Google, Stability AI, and Hugging Face
• Applying for grants from the U.S. government
• Computing resources for training large language models
• Cost of training large language models, with examples of specific models and costs
• The TensorFlow Research Cloud and its role in providing free computing resources
• The development and deployment of open-source language models, including GTP NeoX and Pythia
• The political will and sponsorship required to train large language models
• Open source AI research in general
• Large-scale AI, language models, and protein interactions (AlphaFold)
• Creating an open source infrastructure for training large language models
• Developing the Pile dataset and evaluation suite for language models
• Training large language models (up to 20 billion parameters)
• Investigating model interpretability, ethics, and alignment
• Designing a model suite for scientific research (DALI-2)
• Focusing on tracing the behavior of language models back to their training data
• Intermediary checkpoints for model performance evaluation
• Understanding memorization in language models
• Investigating the effect of training data on model behavior
• Reverse engineering the interaction between models and data
• Improving model interpretability by studying model development
• Forecasting memorization and designing transparent models
• Addressing the reproducibility issue in model training
• Enabling model designability and predictability
• Understanding how AI models change over the course of training
• Importance of being prepared for future paradigm shifts in AI
• Safety concerns and the potential for future dangers
• Efforts to improve AI interpretability and understanding of model behavior
• Research on developing language models for non-English languages
• Using a public Discord server as a platform for discussion, collaboration, and research participation
• Involvement of volunteers and researchers from various organizations in AI research
• Discussion of the difficulty in creating effective safeguards against AI systems that are not very successful
• Mention of the speaker's own work in AI and open-source research
• Thanks and closing remarks from the speaker and the host
• Promotion of a premium subscription to the show's content
• Announcement of the show's conclusion and the host's promise to return on Friday