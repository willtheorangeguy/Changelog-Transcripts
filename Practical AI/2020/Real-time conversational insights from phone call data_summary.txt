• Introduction to the Practical AI podcast
• Sponsors: Fastly, Rollbar, and Linode
• Background of guest Mike McCourt: transition from astrophysics research to data science
• Mike McCourt's journey into AI and data science, including his initial goal to be a college professor
• Postdoc experience and transition to industry
• Collaboration between physics and AI/data science
• Similarities in research process between physics and AI
• Importance of explaining results and framing ideas in data science
• Career path and joining Invoca for call analytics in marketing
• Unique aspects of working with phone call data sets in AI research
• Invoca is an AI-powered call tracking and analytics platform
• Call analytics provide data on customer interactions with businesses via phone calls
• Campaign attribution links phone transactions to marketing campaigns for optimization
• Marketers typically have limited information about customers who make purchases over the phone
• Invoca closes this gap by enabling marketers to analyze and attribute phone transactions to online marketing efforts
• The platform uses unique phone numbers for each ad, allowing for tracking of which ads drive calls
• This approach is made possible by advances in telecom technology that enable rapid provisioning and deprovisioning of phone numbers.
• Programmatic phone numbers and their context in business operations
• Challenges in reusing phone numbers and optimizing number usage
• Complexity of problems in programmatic phone operations
• Transition to AI-related topics at Invoca, specifically Signal AI product
• Motivation behind Signal AI: attributing revenue to marketing campaigns
• Classification of calls using supervised machine learning models (Signal AI)
• Limitations of classification on phone calls due to variable lengths and language variations
• Challenges of analyzing phone calls for classification due to varied language and accent
• Importance of sensitivity in classifier algorithms to pull patterns out of speech
• Impact of dialect and regional differences on classification accuracy
• Variability of audio quality in phone calls and its effect on transcription
• Use of text-based methods for classification after transcripts are available
• Multiple models vs. single master model approach in workflow
• Accounting for variability within different speakers, including accents
• Signal AI has one model per customer, trained only on each customer's data
• Data limitations: sometimes only a few hundred phone calls to train models for regional variations
• Hold messages and advertisements can confuse models; stripping them out helps improve accuracy
• Models are made parsimonious by including words and phrases with solid statistical evidence
• Customer interaction: uploading data, training own model, fine-tuning through human-in-the-loop feedback
• Model updating: retraining based on customer corrections (thumbs up/down) and new data uploads
• Emotional contagion as a better subtitle for mirror neurons
• Research on pain and recognizing suffering in others
• Empathy as a construct and understanding key brain structures involved
• Customer self-service process and automated model training
• Unsupervised topic modeling to ease labeling burden and suggest topics
• Development of an unsupervised model that analyzes calls without human labels
• Unsolved problem of understanding clusters or topics in unsupervised methods
• Difficulty of human interpretation of model outputs
• Importance of imposing constraints on the model for interpretability
• Discussion of Zip's Law, a statistical property of language that describes the distribution of word frequencies
• The relationship between common and rare words in language, with implications for modeling and understanding human communication.
• Describing a hierarchical model to analyze phone calls
• Topic modeling to identify common themes in phone call data
• Use of probability distributions (power law) to represent word usage
• Splitting dictionary into layers of abstraction and specialization
• Deriving probabilities for words based on their frequency and rarity
• Identifying distinct statistical relationships between sets of calls
• Developing unsupervised method to separate out distinct topics or themes
• Consistent patterns in data set
• Dictionary vs. rich, idiosyncratic information in dataset
• Successive layers of specialization to meet ends of dictionary and messy data
• Interpretable results from tuned math and FIPS law
• Future of unsupervised language methods and AI
• Semi-supervised models using labeled data to inform topic model
• Designing a semi-supervised predictive model for conversation topics
• Potential applications in speech and conversational data analysis