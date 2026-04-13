• Introduction to the Practical AI Podcast and its goals
• Guest introduction: Chris Aquino's background as a web developer and his recent hiring at Mozilla to work on Thunderbird projects
• Overview of Mozilla and Thunderbird, including their history and current status within the organization
• Explanation of how Chris Aquino was recruited by Mozilla after being laid off from SurveyMonkey
• Thunderbird's history and transition to a separate entity
• Changes in email usage over the years and how people interact with their email
• The focus on user control and privacy, allowing users to manage multiple accounts and avoid ads/intrusive AI
• Challenges of managing information overload in modern email use
• Integration of AI features in email clients and potential trade-offs
• Automatic summarization and autocomplete features in email clients
• Concerns about data privacy and the potential for AI to read personal information
• Loss of tone and dehumanization of email due to AI processing
• Trade-offs between time-saving benefits and loss of human touch
• Importance of data ownership and control in email management
• Intersection of Thunderbird's ethos with AI features and integration
• Experimental AI assistant for Thunderbird not built into the app
• Two options considered: adding model inference to Thunderbird or running it separately in a cloud service
• Concerns about user data security and battery drain with local model processing
• Exploring remote APIs with varying levels of data protection and privacy considerations (e.g. homomorphic encryption, end-to-end encryption)
• The importance of considering data storage at rest and model openness when working with AI models
• The distinction between hosting models oneself or having a third-party host them
• The discussion of remote inference and its implications for email processing
• Comparison of the story to the Lord of the Rings trilogy (The Hobbit, The Fellowship of the Ring, etc.)
• The development of an experiment as a Thunderbird add-on using APIs from Firefox
• Challenges with data storage and confidentiality, leading to a search for cloud-based providers with end-to-end encryption guarantees
• Collaboration with Flower Labs to implement end-to-end encryption and access to their private LLM via API
• Flower's SDK and end-to-end encryption for email summarization and reply generation
• Collaboration between Thunderbird and Flower, facilitated by Mozilla's investment in Flower
• Hosting a private model within the Flower system for inference and post-training
• Technical partnership with Flower to conduct experiments on email summarization and reply generation
• Development of "Thunderbird Assist", a personal executive assistant using LLMs to summarize emails
• Experimentation with various models, including Meta's LLAMA, to improve performance
• Overprompting issues encountered while developing the daily brief feature
• The speaker had issues with a language model's ability to extract important messages and highlights from emails
• They learned that it was better to split tasks into multiple requests rather than asking for everything at once
• The formatting task never worked well due to the LLM's limitations as a statistical model
• The team switched to using a local Bayesian classifier to reduce load on the cloud provider's infrastructure
• The speaker noted the importance of being specific and constrained in what is asked from the model
• They explored optimizing requests for subsequent tasks, including parallelization and task delegation to different models
• A new approach was considered for the daily brief feature, using multiple small models dedicated to specific tasks and coordinating them deterministically
• Users of Thunderbird assist are homogeneous and mostly comprised of Thunderbird employees
• The application has three main features: individual email summarization, email reply generation, and daily brief
• Different types of users require different approaches, including those who need thread summarization and others who need help with overwhelming emails
• Future development will focus on semantic search, task management, calendar integration, and RSS feed analysis to better serve diverse user needs
• The conversation highlights the importance of segmenting models or applications to effectively cater to specific use cases
• Remote inference encryption
• Confidential enclave for decryption
• HTTPS as a baseline encryption method
• Three-part process for data protection: API authentication, public key exchange, and model server separation
• Double protection with HTTPS and public key encryption
• Future directions in remote confidential inference and federated learning
• Discussing offline LLMs and pre-generated embeddings
• Concerns about server access to user data and end-to-end encryption
• Expanding context for LLMs, including calendar, to-do lists, RSS feeds, and notes applications
• Ideas for personal knowledge management and communication tools using LLMs
• Desirability of deterministic LLMs and small, task-specific models
• Need for discreet inputs and outputs and reusable workflows for information processing
• Acknowledging team contributions and work
• Expressing gratitude to the guest for sharing insights
• Appreciation for taking time to participate
• Recap of upcoming plans and website information
• Mention of social media connections and latest AI developments
• Thanks to sponsors and supporters, including Prediction Guard and Break Master Cylinder