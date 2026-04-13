• The goal of technology is to support humans, not replace them
• AI can help automate and de-bias human decision-making, but should not replace human judgment
• Challenges in scaling human judgment in critical decisions
• Overview of the podcast "Me, Myself, and AI" which explores the intersection of AI and business
• Discussion of why only 10% of companies succeed with artificial intelligence
• Jaron Singer's background as CEO of Robust Intelligence and his expertise in mitigating AI model failures
• Introduction to AI model failure modes, including data-related issues and behaviors
• Example of Microsoft chatbot failing due to racist training data
• AI models can fail in various ways, including through manipulation or being led astray by malicious actors
• Distributional drift occurs when AI models are trained on outdated data and applied to a changed environment
• Failure of AI models has significant implications, including reputational damage and risk to people's safety
• There is an increasing trend towards applying AI models in more complex business use cases
• Algorithmic decision making based on AI is being adopted at an exponential pace across various industries, including insurance, lending, and predictive policing
• Intentional and unintentional factors can contribute to AI model failures, but the approach to addressing these issues may be similar regardless of intent
• Abstracting root cause of model failure to focus on solution
• Approach to model protection is agnostic to cause of failure (adversarial input, data drift, etc.)
• Importance of understanding and addressing both distributional drift and adversarial inputs
• Risk perception varies by company and team, with some prioritizing one over the other
• Human oversight is necessary in AI decision-making processes, especially for high-risk applications
• Industry trend towards automation, but still requires human monitoring and intervention
• AI is moving towards automation, where most retraining tasks will be done automatically without human intervention in the next few years.
• The industry has come a long way from requiring PhDs to code SVMs just 5-7 years ago, with significant advancements in tools and automation.
• As AI moves towards full automation, it's essential to understand and mitigate risks associated with both human-heavy and automated processes.
• There is an inevitable trade-off between automating tasks and preserving human judgment and decision-making capabilities.
• The goal of technology should be to support humans, not replace them, especially in critical decision-making scenarios.
• PhD student at Berkeley and professor of computer science and applied math at Harvard
• Worked on machine learning models, algorithmic decision-making, and the vulnerabilities of ML models
• Found that there is a lack of theoretical understanding in algorithmic decision-making with ML input
• Proved mathematical impossibility theorems for certain cases
• Developed algorithms for noise robustness, focusing on what can be done rather than just proving impossibilities
• Introduced decoupling as a concept to separate model building from model security/safety
• Found that retraining models to make them more robust to adversarial input is often ineffective and reduces accuracy
• Addressing the main problem while considering ancillary issues like security
• Mathematical vs product/ engineering considerations in building robust models
• Decoupling AI model development from deployment and protection to prevent errors
• Building an AI firewall to protect against mistakes made by the model
• Identifying risky data and using a process of stress testing to train the AI firewall
• Understanding how different inputs affect the model's predictions to catch potential errors
• Discussion of an approach to preventing mistakes in models by replacing predictions with the mode of the distribution
• Integration of the product into existing MLOps pipelines with minimal disruption
• Principle of "no integration" and using prediction logs for continuous testing
• Approaches to integrating with Kubernetes, AI firewalls, and on-premise data storage
• Continuous testing as a method for identifying biases in models
• Importance of testing for bias, particularly in sensitive categories such as age, race, and personal details
• Use of automated tests within the product to detect biases in predictions, UCs, false positives, and false negatives across different categories
• Predictions for the future of robust intelligence and AI adoption in various industries
• Mandatory third-party stress testing for organizations using AI that can affect people
• Widespread use of AI firewalls to protect models within a few years
• Future evaluation of predictions made on this podcast, with potential revisit in 3 years