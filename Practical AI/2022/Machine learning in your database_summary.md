• Disconnect between flashy AI advancements and practical business applications
• Machine learning in a business context often involves predicting a single column from relational data with joins
• Many tasks can be accomplished without deep learning, such as using linear regression, scikit-learn algorithms, or XGBoost
• Introduction to Postgres ML and its founders Montana and Lev
• Backstory of how Montana and Lev connected machine learning to a popular database, starting at Instacart
• Chaos and rapid growth during early days at Instacart
• Publishing work on Lore, an open source platform
• Changing technology landscape with new platforms emerging daily
• Growing pains with Elasticsearch data infrastructure
• Challenges of real-time business operations
• Complexity of handling multiple store inventory and product variations
• Scaling Elasticsearch cluster to meet growing demands
• Join problem in Elasticsearch
• Attempting to move join operations to Postgres read time
• Exploring sharding options (Postgres, TimescaleDB, Citus data)
• Investigating full-text search capabilities in Postgres
• Reviewing machine learning functionality in Elastic
• Finding most things happen at application layer for joins between microsystem data stores
• Shadow testing Postgres prototype against Elasticsearch
• Identifying data ingestion bugs and implementing changes
• Implementing second system rewrite due to pandemic-related growth
• Flipping load from Elasticsearch to Postgres cluster during incident
• Optimizing long tail queries in Postgres cluster
• Elasticsearch was the backup system after a new system was implemented
• The new system experienced incidents with increased data usage and was vastly underscaled compared to Elasticsearch
• Feature stores, model stores, and other systems were not horizontally scalable
• A solution was to transfer data from underperforming databases to a new horizontally scalable Postgres cluster
• Instacart's growth led to rapid scaling issues and a focus on simplifying the system architecture
• The project involved iterating and adding features, including unlocking new machine learning capabilities for search
• Constraints with Madlib, an Apache Foundation library, prevented integration of deep learning models into the database
• A monolithic Postgres system replaced microservices, simplifying complexity and reducing organizational resources required.
• The speaker's company had issues with RDS (Amazon Relational Database Service) due to high latency and IO limitations.
• They switched to SSDs (NVMe) which greatly improved performance and allowed them to scale their workloads.
• Postgres became the primary database management system for the company.
• The speaker discusses how machine learning models were not effectively integrated into Postgres due to limitations in deep learning capabilities.
• He notes that most business-related machine learning applications involve simple tasks such as linear regression, XGBoost, and join operations on relational data.
• The conversation touches on the idea that deep learning is often overhyped and that simpler methods can achieve similar results.
• Discussing latency issues with traditional ML system architecture
• Exploring the idea of keeping data processing within the database layer
• Development of Postgres ML, a new approach to integrating machine learning into PostgreSQL
• Sharding and load balancing capabilities for large-scale databases
• Influence of previous projects (Instacart) on the creation of Postgres ML
• Current status and limitations of Postgres ML as a public alpha release
• Concerns about adding load on the primary data store
• Benefits of using a single data store with expertise and muscle built around it
• Integration of Postgres ML and PGCat for machine learning capabilities
• Plans to combine two pieces in an online service offering as a new venture
• Overview of Postgres ML experience, including training and deployment workflows
• Explanation of the "black box" approach to machine learning and hyperparameter search feature
• Role of data curation and manipulation in data science work
• Simple workflow example using SQL for data manipulation and Postgres functions.
• Overview of Postgres ML and its functionality
• Creating training data as a table or view in Postgres
• Feature engineering and using views for reuse
• Handling application databases with updating rows
• Training models and storing them in the Postgres ML models table
• Making predictions using the PGML predict function
• Comparison of different algorithms and selecting the best one
• Initial release features, including a dashboard and algorithm selection
• Supervised learning tasks: classification and regression
• Embeddings and vector operations in PostgresML
• Importance of data transformation and cleaning for machine learning models
• Limitations of current SQL-based solutions for complex transformations
• Value of having vector operations available in a database management system like Postgres
• Call for feedback from users to improve the functionality of PostgresML
• Future potential of PostgresML to simplify workflows and enable non-technical users to work with machine learning models.
• ML deployment checklist requires a team of people and can be simplified
• Complexity of Python code and mathematical concepts is a barrier to entry for some machine learning engineers
• Simplifying the process would allow smaller teams to deploy models at high quality without dropping essential tasks
• The goal of Postgres ML is to provide simplicity and ergonomics, making it easy to run queries and deploy models immediately
• The impact on machine learning engineers' productivity and enjoyment is expected to be significant