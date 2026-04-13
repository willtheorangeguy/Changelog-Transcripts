• Ragas is an open source library for evaluating LLM applications
• The founders' background in ML and experience with natural language processing
• Challenges with manually evaluating LLM applications, including time-consuming and tedious process
• Development of Ragas to provide evaluation metrics and tools for AI engineers building LLM apps
• Initial MVP release in mid-2023 and ongoing iteration and organic growth
• Differences between LLM evaluation and application-level evaluation
• Spectrum of responsibility for model building and evaluation, from researcher to application builder
• Challenges of evaluating an LLM's performance without specific use case knowledge
• Goal of making LLM evaluation intuitive and time-efficient for non-ML experts
• Comparison of benchmarks and metrics for models versus evaluating applications
• Differences in testing approach between unit tests/integration tests and LLM integration
• New considerations for software engineers integrating LLM functionality into their software
• The application of AI in software development creates new challenges in testing due to its continuous output space and non-deterministic nature.
• Traditional software testing focuses on discrete outputs, whereas AI applications require evaluation in a continuous space with varying degrees of correctness.
• Software engineers need to adapt their thinking from traditional binary results to a more nuanced understanding of correct outputs within a range.
• The concept of metrics-driven development is introduced as an extension of test-driven development, aimed at educating developers about using metrics to evaluate performance and understand changes in the system.
• Metrics-driven development involves quantifying the performance of the system before and after changes, enabling analysis and identification of areas for improvement.
• Metrics-driven development for debugging and testing applications
• Assembly AI's speech AI models for various tasks such as speech-to-text, streaming speech-to-text, and speech understanding
• Converting voice data into accurate text, extracting information and metadata, summarizing audio data, and detecting speaker identities
• Assembly AI's simple API for developers to build applications using voice data, with features like entity extraction and PII masking
• Opportunity for developers to leverage trapped value in voice data, such as podcasts, videos, and phone calls
• Industry-leading speech AI models for various apps and workflows, including summarization, speaker diarization, and speech understanding capabilities
• Assembly AI's scalable API constantly updated with new features and models
• Metrics calculation and documentation
• Value props: load off developers, intuitive understanding of metric calculations
• Expanding restore metrics to use cases and identity workflows
• Differentiating between LLM based and non-LLM based metrics
• Abstracting complex decisions for developers
• Providing related features and data for adopted metrics
• Metric alignment across different domains and expectations
• Using feedback to align larger language models with specific measurements
• Data burden and path towards getting data in place for LLM applications
• Sample size for offline evaluation (typically 100-500)
• Importance of test data diversity to represent production distributions
• Reference-free metrics vs reference-based metrics with error estimation
• Challenges of creating accurate test data sets from production data due to messiness and uncontrolled environments
• Synthetic creation of test data sets grounded in production data and internal documents
• Upcoming feature: seeding from production data for more realistic behavior imitation in test data sets
• Improving efficiency in generating and validating synthetic data
• Manual review of synthesized data to ensure quality
• Limitations of current LLM applications (e.g. RAG, HND Code tool use cases)
• Tool binding and its potential for improving performance on tool use cases
• Enterprise adoption of AI applications and their benefits (time and resource savings)
• Development of frameworks and libraries around AI applications
• Clarity on building AI applications and combo systems
• Research and advancements in data processing, pre-processing, and model quality
• Synthetic data can improve AI models
• Model output can be used to improve the model itself
• Evaluation of AI models is a pain point for enterprises due to lack of standardization
• Open-source standard for evaluating LLM applications is being developed
• Long-term goal is to establish an agreed-upon way of evaluating LLMs