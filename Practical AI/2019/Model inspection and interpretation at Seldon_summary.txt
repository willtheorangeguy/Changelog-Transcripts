• Sponsor acknowledgments (Fastly, Rollbar, Linode, DigitalOcean)
• Introduction to Practical AI podcast and hosts
• Background of guest Janice Klaes, a data scientist at Selden
• Transition from academic mathematical modeling background to industrial data science work
• Discussion of the role of machine learning in Selden's work
• The speaker had not read the Foundation series by Isaac Asimov before joining Selden, but later asked about it and was reminded to re-read it
• The series is about a psychohistorian named Harry Seldon who uses mathematics to predict societal collapse and create two foundations to preserve knowledge
• The name "Selden" is fitting because it's related to prediction and the company works on machine learning deployment
• Selden focuses on deploying machine learning models after they've been trained, making them accessible for business use
• Selden has an open-core business model with a primary product called Selden Core, a platform that runs on top of Kubernetes for wrapping up and deploying ML models
• Customers are businesses looking to make their data science models more accessible and user-friendly in production environments
• Selden Core is an open source deployment platform
• Enterprise layer is being built on top of Selden Core for easier and more accessible use
• Features include centralized monitoring, team collaboration, and authentication
• Friction exists between engineering teams and data science/AI teams due to differences in tooling and expertise
• Selden sees interest from both sides (DevOps and AI) in its platform
• In larger enterprises, silos exist between teams leading to a "chuck it over the wall" approach
• Smaller companies often have people doing multiple roles at once
• Selden's motivation for model inspection and interpretability is driven by capabilities of its open source deployment platform
• Model interpretability and inspection of routing logic for model selection
• Monitoring machine learning models from a data science perspective, including:
  • Model explanations
  • Outlier detection and concept drift to identify evolving data distributions
• Tooling landscape for monitoring ML models, including custom logic and Alibi as an open-source library for model explanation
• Integration of Alibi with Selden core and Selden deploy to produce model explanations in production environments
• Motivation for choosing Jupyter Notebooks as core interface
• Alibi's API and its use in providing interpretable email methods
• Explanation algorithms within Alibi and their structure
• Comparison of Alibi's API to scikit-learn's model or estimator
• Model agnosticism and compatibility with various frameworks (TensorFlow, PyTorch)
• Black box explanation methods in Alibi and their portability
• Anchor explanation method and its application
• Global vs. local explainability and the importance of asking human-interpretable questions
• The anchor technique is used to create interpretable questions that can help design explanation methods
• Anchors are a method that returns a subset of features and their values that result in the same model prediction 95% of the time
• Anchors are useful for identifying pertinent features for individual predictions, such as marital status and work category
• Lime is a related method that fits a linear surrogate model to approximate non-linear decision boundaries
• Alibi has an ambitious roadmap to become a go-to platform for model explanation methods, with plans to integrate various techniques
• The team's goal is to make Alibi the scikit-learn of model explanations, providing a unified API for people to use.
• Alibi's ambition is to have a standardized API for explainability methods
• Selden is demoing its enterprise product with anchor explanations at COGX event in London
• Alibi and Selden resources can be found on docs.selden.io for documentation and getting started
• Christoph Molnau's book on interpretable machine learning is recommended for learning about the topic
• Practical AI community channels (Slack, LinkedIn) are available for questions and discussion about Alibi, Selden, and related topics
• Introduction/Conclusion of an interview
• Appreciation and gratitude expressed to the guest
• Upcoming conference possibility
• Encouragement to rate and share the podcast on various platforms
• Sponsorship acknowledgments (Fastly, Rollbar, Linode)
• Hosts introduced (Daniel Whitenack and Chris Benson)