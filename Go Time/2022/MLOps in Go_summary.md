• Introduction to a podcast discussing feature stores with Mike Eastham
• Explanation of what Tecton is and its role in building systems for production machine learning applications
• Background on Mike Eastham's experience working at Google on indexing and serving infrastructure for web search and his current role as tech lead at Tecton
• Definition and explanation of a "feature store" and its purpose in managing feature definitions and data within an organization
• Discussion on what constitutes a feature, including engineered inputs that go into machine learning models
• Explanation of the objective of using feature stores, including making features reusable parts of the workflow for building multiple models
• Features are inputs used for training and prediction in machine learning models
• Features can be generic or specific to certain products and user combinations
• Feature stores support various techniques for building features and provide a clean seam between data scientists and operators
• Performance requirements differ between model training and prediction contexts, with latency being more important in online contexts
• Feature stores address the need for faster everything, including fast search results and predictions
• Both data scientists and operators use feature store systems
• Feature store to manage features and ensure consistency between training and serving systems
• MLOps vs AIOps: terms referring to the same concept of managing machine learning pipelines
• MLOps pipeline complexity: longer process with multiple stakeholders and roles involved
• Differences between MLOps and traditional DevOps: loopback from deployed model to retraining, more complex skills and roles required
• Terminology debate: MLOps vs AIOps, one-word or two-word formatting, capitalization conventions
• Use of Go in MLOPs: application in online surveying interface for low-latency feature value requests
• Hybrid approach to data processing with some prematerialized data and final aggregations at serving time
• Importance of low latency in data processing and consistency of tail latency
• Use of Go for performance tuning and troubleshooting due to built-in tracing and profiling tools
• Embedding Python interpreter within Go server for on-demand transformations
• Consideration of compiling Python to LVM bytecode for linking into Go binary
• Supporting internal users' familiarity with Python as a primary tool
• Discussion of Go's suitability for Machine Learning Operations (MLOps) due to latency sensitivity and availability of tools for troubleshooting
• The speaker Mike Eastham discusses his work with Google and the use of Go programming language in various projects.
• He mentions that a metric pipeline was written in Go to process logs from thousands of experiments at once.
• Feast is an open-source project that has some Go mixed in, but is more Python-focused.
• Natalie Pistunovich mentions contributing code to the Feast repository for those interested.
• Mike Eastham shares his unpopular opinion: he doesn't like maple syrup on pancakes or waffles.
• The conversation then devolves into a humorous discussion about maple syrup and Canadians.