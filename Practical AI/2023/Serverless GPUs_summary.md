• Introduction to the podcast and its focus on AI-related technologies
• Welcome to Eric Dunderman, founder of Banana (serverless GPUs)
• Explanation of serverless computing: dynamic allocation of servers based on usage needs
• Discussion of serverless GPUs and the concept of making Google-level infrastructure accessible without high effort
• Background on the challenges of implementing serverless GPUs and the timeline for its development
• Focus on inference side of machine learning, where serverless GPUs are most valuable
• Inference and serverless computing
• Challenges with cold boot times, particularly for GPUs
• Importance of not occupying GPU RAM to avoid waste and cost
• Caching models on local storage or CPU to reduce cold boot time
• Pre-caching models on CPU before inferences occur
• Serverless workflow considerations for adapting existing workflows
• Cold starts in models and their impact on performance
• Tolerance for cold boots among clients
• Strategies for mitigating cold start times, including serverless platforms and fine-tuning autoscalers
• User preferences regarding idle time vs. cold boot frequency
• Trade-offs between cost and latency sensitivity among users
• Impact of faster cold starts on user experience and inference performance
• Language choices: Python and Go are used, with a focus on simplicity and ease of maintenance
• Infrastructure framework: Boilerplate code in Python is provided for a server setup
• Pipeline infrastructure: Mostly done in Go (95%)
• Runtime: C++ and CUDA used for deep work, but only by a small subset of the team
• Banana workflow: Users can start with one-click templates for popular models, then customize and iterate on their own code using a local dev environment
• Integration: API creation and customization possible through modifying functions within an HTTP framework
• CI/CD pipeline for deploying models to Banana
• Recommended workflow for shipping new fine-tuned versions
• Necessary skills for users to productively use Banana (Python, Hugging Face, Docker)
• Integrating Banana with Python apps through REST endpoints or official SDKs
• Serverless workflow and custom deployment of unique APIs
• Insights into how people are using Banana's serverless workflow (custom repos, fine-tuning, etc.)
• Customization of models in Banana for fine-tuning and running multiple models side by side
• State-of-the-art models changing rapidly, making customization necessary for users to stay ahead
• Serverless GPU infrastructure limitations, such as cold boots and slow inference with steady traffic
• Training on serverless platforms, including issues with observability and tracing settings
• Batch processing jobs being more suitable for traditional infrastructure rather than serverless
• Adoption of forward-leaning languages, such as Rust and Go, by users of Banana's serverless GPUs
• Targeting early adopters and developers using modern frameworks and languages in their applications
• The importance of choosing the right cloud provider for running GPUs
• Differences in pricing and scalability between traditional hyperscalers and newer clouds
• Using "skate ahead of the puck" analogy to describe auto scaling in Kubernetes
• Recommendations for auto scaling Kubernetes pods and nodes
• The future of AI, including the potential for fine tuning models at the user level
• The importance of serverless computing for user-level fine tunes
• End of conversation wrap-up
• Gratitude to Eric for chatting with the audience
• Call to action: subscribe and share Practical AI with others
• Acknowledgment of sponsors (Fastly, Fly)
• Credits and appreciation for Breakmaster Cylinder's music