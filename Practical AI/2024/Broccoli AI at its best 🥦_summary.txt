• Introduction to Practical AI podcast
• Intel Innovation 2024 conference announcement
• Upcoming episode with data scientist Bing-Sing Chua
• Discussion on doing data science in the energy sector
• Challenges and limitations of working with traditional infrastructure
• Importance of active learning and NLP in the context of the energy sector
• Bringing cloud native technologies to a traditional on-prem server setup
• Unstructured data is often collected and stored, but not analyzed at scale
• Traditional industries have large amounts of unstructured data from sources such as comments, observations, and safety reports
• The speaker conducted a proof-of-concept to analyze unstructured data using machine learning and found significant insights in the data
• The insights were previously locked up in the unstructured data, but not being used due to lack of analysis capabilities
• Examples of unstructured data include text files, Microsoft documents, and comments alongside structured data in table form
• Difficulty in working with unstructured data
• Challenges of bootstrapping labeling process without labeled data
• Issues with deploying models to production environments (specifically Windows servers)
• Need for infrastructure to manage and store models (e.g., MLflow)
• Orchestration of model deployment using services like cron jobs or dedicated orchestrators
• Importance of contextual understanding in working with nuanced, company-specific data
• Challenges of code-switching in multilingual datasets
• Users were involved in the foundational development of an app
• Users labeled data for the classification model, with some contention over labels
• A voting system was used to resolve label disputes
• Arjila was used as a platform to manage user labeling and collect feedback
• Initial bootstrapping of labels required 1,800-2,000 labels to be established before training the first model
• Training a simple AI model using Hugging Face's sentence transformers
• Deploying the model for text classification with moderate performance (60-70% F1 score)
• Implementing active learning to improve model performance and gather user feedback
• Creating a pipeline to collect new data, make predictions, and send emails to users
• Using Argyla as a Python API to create a loop for data collection and prediction
• Collecting around 4,000 labeled datasets through user feedback
• Discussing the need to periodically retrain the model and address concerns about Gen AI security, trust, compliance, and cost risks
• Mentioning Motific as an AI innovation that addresses these challenges and supports the entire Gen AI journey
• Update cycle for new model
• Judging when to update the model based on relevant testing and metrics
• Current approach: periodically updating every couple months, monitoring data drift but not implementing advanced observability yet
• Limited resources and prioritizing simplicity
• Model deployment through a model repository and potential future use of Docker containers
• Using Docker containers for data management
• Experience with SharePoint and difficulties in wrangling and data handling
• Introduction of DuckDB as a middle layer for data processing and analytics
• Embedded SQL service for data cleansing and preparation
• Comparison to big data problems and the need for different query solutions
• Future plans and excitement about embedded databases, LLM, and Gen AI applications
• Interest in scaling down AI capabilities for more accessible devices and applications
• Discussion about a trademarked term
• Hype cycle mentioned, possibly related to the previous topic
• Conclusion of the podcast and thanks to listeners and partners
• Call to action to subscribe to the podcast and join the community Slack team
• Final goodbyes and appreciation from the hosts