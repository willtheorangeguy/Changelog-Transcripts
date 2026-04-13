• Discussion about the focus of the show and introduction of guests
• Introduction of the concept of "suspicion machines" in the context of welfare systems in Europe
• Explanation of predictive risk assessments used in European welfare systems to flag individuals for investigation
• Case study of a machine learning model that wrongly flagged 30,000 families in the Netherlands, leading to a scandal
• Discussion of the challenges and methods used by journalists to investigate these systems
• Overview of existing literature on AI fairness and its relevance to predictive risk assessments
• Setting thresholds for predictive modeling in welfare systems
• Initial discovery and research into the use of predictive analytics in Europe
• Freedom of information laws used to gather information about model deployment
• Tiered approach to requesting documents, starting with non-sensitive materials
• Trends in machine learning deployment by government entities across Europe
• Bifurcation between industry-driven adoption and internal capacity building
• Limitations and failures of big data analytics in welfare systems
• Evidence of predictive analytics use in assessing risk and welfare
• Justification for using advanced technology to combat welfare fraud
• Challenges in distinguishing between deliberate fraud and unintentional error
• Role of consultancies in promoting predictive analytics
• Welfare fraud estimates are often exaggerated by consultancies
• National audits have estimated welfare fraud rates to be around 0.2-1%
• Predictive models for detecting welfare fraud may not accurately identify actual fraudsters
• Unintentional mistakes can be misclassified as fraud
• Machine learning models may introduce biases and inaccuracies in detection
• Researchers encountered difficulties in obtaining data from governments, but were eventually able to access a predictive model used by the Dutch city of Rotterdam
• The model ingests 314 variables and outputs a score, but it was unclear what this meant for individuals flagged as potential fraudsters
• Realistic testing data was challenging to obtain, but was eventually accessed through a histogram provided by the government
• Limitation in training data: no access to labels (fraud or not)
• Gradient boosting machine model used
• Features included in dataset, such as demographic info, language skills, and behavioral assessments by caseworkers
• Problematic variables, like subjective caseworker judgments and biased features
• Labeling issue: fraud/no fraud label doesn't distinguish between intentional and unintentional mistakes
• Training data construction issues: non-random subset of past investigations and potential bias in labeling
• Impact of being flagged for investigation by AI-powered systems
• High-risk individuals targeted, including single mothers from minority backgrounds
• Punitively invasive investigations, including unannounced raids and financial scrutiny
• Questioning the validity and consistency of labels used in investigations
• Consequences of being wrongly accused, even if ultimately cleared
• ChatGPT custom prompts leaked via prompt injection, revealing Gen Z slang and lingo
• Concerns about model performance despite data flaws and potential biases
• Rotterdam's AI model deployment, including contract with consultancy Accenture
• The model being discussed has a hit rate of 30% in identifying fraud, but its ROC curve is poor
• The model's performance is influenced by the selection process used to gather data, which may introduce biases
• An example is given where men in the training data are more likely to be selected through investigations with low likelihood of finding fraud, while women are selected through anonymous tips or random sampling
• This can lead to disparate outcomes and patterns in the model that do not reflect real-world situations
• The story was an educational piece on machine learning and its impact, aiming to take readers through the full life cycle of a model
• Non-technical audiences found the discriminatory aspects of the model's performance and decision trees interesting, but were also fixated by the non-linear interactions in the decision trees
• One city (Rotterdam) responded graciously to the results, calling them informative and educational, and decided not to use the model due to ethical risks
• Algorithmic fairness as a holistic concept, encompassing various aspects such as training data, input features, model type, and outcome fairness.
• Importance of examining the quality and representativeness of training data in machine learning systems.
• Need for transparency and open discussion around how these systems operate and make decisions.
• Discussion about whether transparency would allow people to "game" the system, potentially improving it.
• Evaluation of current AI systems as often being poorly constructed and having disparate impacts on various groups.
• Possibility of creating better AI systems through careful feature selection, training data construction, and model evaluation for bias.
• Future conversation topics include assessing the effectiveness of AI decision-making in removing human biases and promoting equal treatment.
• False positive rates and their impact on different groups
• Difficulty of discussing ethics and fairness in AI systems
• Need for a broader societal perspective beyond just math problems
• Importance of considering the consequences of AI deployment, such as underutilization of welfare benefits
• Encouragement to rethink the premise of deploying certain models and consider alternative approaches