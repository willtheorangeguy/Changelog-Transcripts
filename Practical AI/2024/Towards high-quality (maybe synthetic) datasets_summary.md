• Introduction to Fly.io, a platform for building and deploying AI-related tech
• Annie Sexton discusses the benefits of using Fly.io, including flexibility and ease of use
• Tigress object storage is introduced as an example of a partner service that integrates seamlessly with Fly.io
• Ben Bertenshaw from Argila joins the conversation to discuss data collaboration and management
• The concept of "broccoli AI" is mentioned as a type of healthy AI for organizations
• Collaboration between domain experts and data scientists/ai engineers in AI development
• Importance of understanding the problem and modeling it before building a model
• Common mistakes when curating data for AI models, such as lacking a clear task or not considering how to properly curate data
• The need to establish a baseline or benchmark before fine-tuning a model with domain-specific data
• How to approach data curation in a way that is relevant to specific AI workflows and tasks
• Setting up a baseline for retrieval and annotation tools
• Iterating on the pipeline by adding re-ranking, fine-tuning models, or switching to different models (e.g., LAMA)
• Creating a workflow for testing and iterating on the system
• Writing down expected questions and associating them with documents
• Testing model performance using simple benchmarks (e.g., ChatTBT, Hugging Chat)
• Scaling up retrieval and introducing proper retrieval
• Using RAG setup to optimize different components (retrieval, generative model, prompt)
• Starting with simplest levers such as rule-based retrieval and semantic search
• Introducing hybrid search and exact match for word queries
• Enterprise features and their benefits for SMBs
• WorkOS' free offerings and competitive pricing compared to Auth0 and other platforms
• Targeting companies at different stages of growth with varying technology needs
• Supporting companies from small startups to large enterprises with complex technology stacks
• The potential for mixing rule-based systems, machine learning, and larger Gen AI models in enterprise applications
• Balance between traditional data science models and newer workflows like RAG
• Using classification and generation pipelines to improve output quality
• Importance of fine-tuning smaller models over large language models
• Cost efficiency, privacy, and ease of fine-tuning with smaller models
• Retrieval augmented generation (RAG) pipelines and query classification
• Arjila's approach to data annotation and collaboration between AI engineers and domain experts
• The UI is lightweight and can be deployed in Docker or Hugging Face spaces
• The SDK uses Python classes to construct dataset settings, including fields and questions
• The UI allows annotators to see all questions with nice descriptions, tweak, and change as needed
• The system enables distributing tasks between teams and requires some questions to be answered while skipping others
• Keyboard shortcuts in the UI make it easy for users to navigate and move through tasks efficiently
• The UI is scalable and can handle complex tasks such as multi-page documents or detailed images with chat conversations
• Roles using the tool include developers, AI experts, and non-technical domain experts
• AI experts can add features like semantic search to data sets, enabling more efficient labeling
• Using synthetic data within JLA and integrating AI feedback is a new area of exploration
• Non-technical domain experts finding Argeala intimidating due to technical aspects
• User experience for non-technical subject matter experts in Argeala
• Overview of Argeala's development from past experiences with collecting feedback from domain experts
• Features of Argeala's interface, including single record view and labeling process
• Collaboration between domain experts and AI engineers using Argeala
• Smart sleep device that uses AI algorithms for temperature control and tracking biometrics
• Device can cool or warm the bed to a specific temperature, with separate controls for each side
• AI-powered system learns sleep patterns over time and adjusts temperature accordingly
• Mobile app provides access to sleep analytics, trends, and daily sleep fitness score
• Discussion of AI feedback and synthetic data in the context of machine learning and data labeling
• Use of LLMs (Large Language Models) to generate documents, provide qualitative feedback, and filter data sets
• Ability to use AI systems to label or annotate data, rather than relying on manual annotators
• Developing a classification dataset by applying topics to documents
• Using generative models to generate questions or queries from documents
• Creating a Q&A or retrieval data set with generated search queries
• Addressing hallucination when generating data sets, including self-evaluation and using larger models
• Introducing Distalable as a tool for synthetic data generation and AI feedback
• Discussing the importance of avoiding flaws in datasets, particularly in sensitive industries such as healthcare and security
• Using pipeline structures to organize tasks and LLM executions, with features like asynchronous execution and caching intermediary results
• Discussion of the still label and its usage in data sets
• Adoption of the still label for generating millions of rows of synthetic data
• LMI's use of the still label to rewrite and resynthesize emails in production
• Future plans to expand modalities beyond text, including image, audio, and video
• Tightening the loop between applications to deal with feedback from domain experts
• Conversation ends and is repeated multiple times
• Duration of conversation: approximately 7 minutes
• No substantive topics discussed or mentioned