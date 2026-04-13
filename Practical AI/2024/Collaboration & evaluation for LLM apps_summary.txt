• The guest Dr. Reza Habib discusses his work at Humanloop and the challenges of using Large Language Models (LLMs) in industry
• LLMs bring new capabilities but introduce challenges such as prompt engineering, usability, and performance measurement
• Historically, AI systems were built by machine learning experts, but with LLMs, non-technical people are involved in customization
• Prompts need to be versioned, managed, and treated like code; collaboration between technical and non-technical people is necessary
• Measuring performance of generative AI models is subjective and difficult due to the lack of a clear "correct answer"
• Humanloop solves problems related to finding and managing prompts for large language models (LLMs), as well as evaluating model performance.
• Companies often start using LLMs with enthusiasm but struggle with collaboration, versioning, and evaluation as they move from prototype to production.
• Many companies try to manage these issues by building in-house tools or using existing solutions, but this can lead to cumbersome processes and quality control issues.
• Humanloop provides an interactive environment for prompt management, allowing for collaboration, history tracking, and variable connection.
• The development of LLM applications requires coordination among domain experts, data scientists, AI/ML engineers, product managers, and software engineers, creating a complex landscape of interactions.
• Product managers can be directly involved in developing AI applications
• Software engineers are still necessary to implement the bulk of the application
• Domain experts, such as linguists, play a key role in developing prompts for models
• Human loop and non-technical stakeholders' involvement is essential in developing Gen AI applications
• Collaboration between technical teams and domain experts leads to innovation and new possibilities
• A new era of the internet can be built with people in charge, rather than large corporations.
• HumanLoop is a platform that enables workflows for evaluating and improving language models
• It helps with prompt iteration, versioning, and management, as well as evaluation and monitoring
• The platform includes an interactive environment where users can try out different prompts, compare them, and save versions for deployment to production or other environments
• HumanLoop supports human evaluation in addition to model-based scoring methods
• The platform allows for capturing end-user feedback, both explicit and implicit, which becomes a valuable resource for debugging and fine-tuning the model
• Fine-tuning is often misunderstood as simply injecting data into prompts, but it typically means doing extra training on a base model with specific example pairs of inputs and outputs
• In reality, teams are more likely to fine-tune their workflows, language model chains, or retrieval/data instead of the models themselves
• People start with prompt engineering due to its ease and high impact
• Fine tuning is useful for improving latency, cost, tone of voice, or output constraints
• Fine tuning is like compilation, optimizing a model's performance
• Fewer people are doing fine tunes initially due to the power of prompt engineering
• Hybrid systems like RAG (retrieval augmented generation) have become popular alternatives to fine tuning
• Fine tuning has its limitations and requires significant data and time investment
• Humanloop supports both closed proprietary models and open models, allowing users to integrate multiple models
• High performance models are now economically competitive for hosting one's own model, but data privacy is still a concern
• Companies using open source models due to data privacy concerns or for real-time/low latency requirements
• Vana.ai: Python RAG framework for accurate text-to-SQL generation, allowing users to chat with relational databases
• Human Loop System: enables collaboration between domain experts and engineers in building question-answering systems
• Roles involved:
	+ Domain experts: figure out system requirements, determine what "good" looks like
	+ Engineers: build retrieval part, orchestrate model calls, integrate human loop APIs, set up evaluation
• Workflow:
	+ Domain experts try out models in playground environment, engineers connect database to human loop
	+ Iteration involves trying different prompts, reviewing outputs, making changes and re-evaluating
	+ Rigorous evaluation involves generating test cases, setting up evaluation criteria, running evaluation, deploying to production, gathering user feedback
• Evaluation phases: prototyping, testing prompts, and iteration
• Components of LLM applications: base model, prompt template, data collection strategy, tools, and APIs
• Importance of evaluation in preventing regressions and handling model upgrades
• Three stages of evaluation: interactive development, regression testing, and monitoring in production
• Use cases for interactive testing: early prototyping, adversarial testing, and ensuring system security (e.g. age appropriateness)
• Benefits of using a combination of fixed test sets and interactive testing
• Considerations for evaluating model upgrades and changes to prompt formats or behaviors
• Collaboration challenges and benefits from using code collaboration systems
• Examples of surprising use cases, such as publicly listed companies improving their workflows with HumanLoop
• Complexity of apps being built with LLMs, including simple agents and assistants that can use existing software
• Importance of tooling for achieving complex use cases, with examples of companies building their own tools (e.g. Ironclad's Rivet)
• Error prone processes without good tooling, including duplicate annotation jobs and inability to scale to more complex agentic use cases
• Future developments in AI, including multimodal models, generative models, and increased reasoning capabilities
• Excitement about agent use cases, but acknowledgment that there are still few successful applications in production
• The current state of applications on HumanLoop are mostly simple LLM or retrieval augmented applications.
• Excitement for seeing agents in production and multimodal models in production.
• Goal to move from a passive to proactive platform where the system suggests improvements to applications based on evaluation data.
• Potential feature: automated prompt suggestion, cost reduction, and user acceptance of changes.