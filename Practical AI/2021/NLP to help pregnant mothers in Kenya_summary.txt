• Improving maternal healthcare in Africa
• Using data to route mothers effectively to care in a timely manner
• Leveraging conversational history and triggers to predict future danger signs
• Development of a model using initial work done
• Introduction to Jacaranda Health and its digital health tools
• Role of AI, NLP, and data science in improving maternal healthcare
• Mothers enroll in a service through public health facilities and receive SMS messages about their health and baby's health
• The service also allows mothers to ask questions via SMS at no charge, which was initially unexpected but became a significant aspect of the service
• As the number of users grew, it became clear that a way to triage incoming questions was needed due to the varying levels of urgency and importance
• Machine learning techniques were explored as a solution to categorize messages and prioritize responses
• The team had some initial experience with tools like Dialogflow, but it wasn't immediately clear if machine learning/ AI could provide a solution
• Discarding the automated chatbot idea due to language complexity and user dissatisfaction with cookie-cutter responses
• Approaching the problem by testing various NLP solutions, including Google's NLP, with a dataset of labeled questions from previous years
• Identifying Google's NLP as most useful for the specific use case
• Training the model using a larger dataset with translated output and intent classification
• Defining a list of intents (33 in length) and determining that fine-grained labeling was optimal
• The labor-intensive process of data labeling, involving manual assignment of labels by team members
• Challenges and subjectivity involved in labeling, requiring additional training and rigor to establish consistency
• Signal Wire is a real-time video tech platform for creating interactive experiences
• It offers broadcast-quality, ultra-low latency video with APIs and SDKs for popular programming languages
• A company used Signal Wire to scale their model and improve question classification accuracy
• The team had to retrain the model on 100,000 questions and outsource labeling due to complexity
• The company's culture changed from focusing solely on machine learning to incorporating human expertise
• The team successfully brought along employees by framing benefits for them and sharing results with the help desk
• Prioritization and classification of questions in the early rollout period
• Challenges with the initial NLP model and integration with help desk team
• Improving precision and recall through iterative development
• Integrating SMS messaging platform with ticketing software and NLP model
• Unique aspects of Jacaranda's workflow and innovation in integrating AI with existing systems
• Importance of understanding the "glue" that holds the system together, rather than just focusing on machine learning or NLP itself
• Linguistic diversity in Kenya, where English and Swahili are major languages, but local dialects and informal language (Sheng) can cause issues with text-based communication.
• NLP model struggles with mixed languages and Sheng, leading to garbled translations, but has achieved 87% accuracy for general questions and danger sign questions.
• Data set includes various question categories, such as danger signs, which make up about 30% of incoming questions, including actual danger signs (around 3-5%) that need immediate attention.
• Automated responses are being explored to improve efficiency and reduce the workload on human help desk agents.
• A two-step approach is being tested: automated response with follow-up question to confirm if the answer resolved the issue.
• Designing a system where AI models are updated based on feedback from agents, eliminating the need for manual labeling of hundreds of thousands of questions
• Ensuring data security and confidentiality in handling sensitive health information, including implementing industry best practices and using major cloud providers' security tools
• Collecting minimal personal identifiable information (PII) while still tailoring message campaigns to individual users
• Balancing data collection with user consent and transparency, particularly in regions where knowledge about machine learning and data usage is limited
• Improving model accuracy through partnerships with machine learning experts and incorporating context and understanding into question processing
• Scaling the system to increase capacity without increasing costs, while also exploring predictive analytics capabilities for faster and more effective maternal care
• Data layers within the healthcare system can be used to route mothers more effectively to care in a timely manner
• Conversational history and triggers can predict future danger signs, potentially developing a model for early intervention
• Supporting mothers with information, such as vaccination schedules and dietary guidance, is a key goal of the project
• Digital tools, like voice assistants and home records, can provide convenient access to medical information and support case histories