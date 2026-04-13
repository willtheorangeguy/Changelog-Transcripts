• Kate Soule discusses her background and how she transitioned to IBM Research from a business background
• Granite is IBM's large family of large language models produced by IBM Research
• The large language model landscape has shifted since November 2022, with increasing interest in business applications
• IBM is positioning large language models as building blocks that can be reused across various use cases and products
• Centralized development within IBM Research allows for efficient creation and distribution of these models across multiple products and downstream applications
• Discussing the benefits of developing Granite within research without a P&L
• The use of open source license for Granite, specifically Apache 2
• IBM's decision to choose an open source license and its reasoning behind it
• The unique characteristics of AI models and their treatment under licensing
• The choice of Apache 2 as the license for Granite and its implications for ecosystem growth
• IBM's legacy in open source and how it influenced the decision to go with open source for Granite
• IBM's leadership supported open ecosystem for generative AI
• Architecture decisions are driven by making educated bets based on constraints and strategy
• Early focus was on replicating existing architectures with innovation in data
• As the field evolved, focus shifted to efficiency and economical models
• Mixture of experts is an approach to using smaller models for inference, rather than entire large model.
• The need to reduce the number of parameters in large language models to improve inference time efficiency
• Mixture of Experts (MOE) models as a solution to select specific parameters at inference time
• Developing smaller MOE models for local applications, such as running on CPUs or edge devices
• Designing model sizes based on intended environments and compute resources available
• Segmenting models into different tranches for various use cases, including IoT, local, and cloud-based applications
• Experimental chain of thought reasoning capabilities in the Granite 3.2 model release
• Large language models have the capability to "think" and generate logical thought processes before responding
• A new inference time compute area of innovation has been developed in Granite 8B 3.2, allowing for selective reasoning
• The model can be turned on or off depending on the complexity of the question, with longer questions triggering more detailed responses
• The "thinking" feature is currently experimental and may become a standard part of future models
• Selective reasoning is becoming a trend in AI development, with Claude 3.7 being an example of this approach
• Smaller models are increasingly able to match the performance of larger ones, making them more efficient and cost-effective
• The shift towards smaller models may be driven by the capabilities of selective reasoning, which can make large models less necessary
• Discussing the evolution of language models and technology advancements
• Focus on smaller-sized models for more efficient performance
• Targeting 80-20 rule: 80% of use cases handled by models with 8 billion parameters or less
• Introducing Granite model family, including language models (1B-8B params) and vision models for image understanding tasks
• Prioritizing document and chart Q&A data in training sets
• Exploring RAG workflow integration with vision models to improve question answering capabilities
• Companion models, such as Granite Guardian, designed to work alongside language or vision models
• Models detecting adversarial prompts, harmful inputs/outputs, hallucinations, and model responses
• Embedding models assisting in broader generative AI workflows
• Conversion of text data into embeddings for search and retrieval
• Multimodal capabilities in Granite models, including vision and time series
• Efficiency of Granite models compared to other generative AI models
• Performance of time series forecasting models, including top marks on the GIFT leaderboard
• Introduction of Granite Guardian for guardrails and security features
• Importance of trust and safety in AI development
• Fine-tuning of Granite to create a specialized version for detecting and monitoring inputs and outputs.
• Agents and responsible AI workflows
• Injecting observability into AI systems to prevent errors and hallucinations
• IBM's work on agent framework and model co-design for safety and security
• Protecting sensitive information through model design and demarcation
• Agent applications in various industries, including consulting and edge environments
• Evolution of Granite towards smaller, hyper-efficient models for edge deployment
• Building with models for smaller sizes and optimizing performance
• Dividing tasks into smaller pieces for efficient processing by small models
• Leveraging model and hardware co-design to improve speed and efficiency
• Focusing on the efficient frontier of model performance, not just benchmark scores
• Enabling flexible use of models based on task difficulty and desired performance level
• Promotion of Changelog newsletter
• Reasons to subscribe to the newsletter (29 in total)
• Example reason: starting to look forward to Mondays
• Thanks and credits: Fly.io, Breakmaster Cylinder, and listeners