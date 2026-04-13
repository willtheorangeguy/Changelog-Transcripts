• Bandwidth for Changelog is provided by Fastly
• Rollbar helps fix issues at Changelog
• Linode hosts Changelog's servers
• DigitalOcean announces managed databases, including MySQL and Redis
• Practical AI podcast discusses AI research conferences, such as ACL and NeurIPS
• Chris Benson's week includes a conference on the future of AI and STEM, a panel on protecting AI from threats, and an opening keynote on ethics and AI
• Andrew Stanton joins the show as a staff product manager at Etsy, discussing search and other topics
• Machine learning and search experience
• Entity recognition for unstructured data
• Multimodal deep learning in e-commerce search
• Types of search problems (information, e-commerce, question/answering)
• Evolution of search technologies over time
• Introduction of machine learning and AI to search
• Evolution of search technology from rule-based algorithms to machine learning
• Early applications of AI in search, including catalogs and Boolean queries
• Development of TF-IDF and BM25 methods for relevancy ranking
• Introduction of facets and filters in e-commerce search by companies like Indeka
• Advancements in machine learning for search, including learning to rank work and deep neural networks
• Impact of recent advancements in deep learning on search technology, specifically neural IR
• Data sets used in building machine learning models for search, including existing data sets and internal datasets
• Historical data sets for web search are often overfitted to specific information pieces and may not translate well to other domains
• E-commerce search is distinct from traditional web search, requiring tailored methods and bespoke approaches
• Etsy's challenges with search include a vast inventory (over 60 million results), many of which are handmade or one-of-a-kind, and lack of structured data for product categorization
• Ranking and personalization are crucial in navigating the large number of search results on Etsy
• The platform's niche markets and unique products present a significant challenge for search algorithms to surface relevant results
• Neuroevolution is being used by Etsy for search, combining evolutionary algorithms with machine learning techniques to adapt to the platform's complex and ever-changing inventory.
• Neuroevolution combines evolutionary algorithms with neural nets to evolve network structures and weights
• NEAT is an example of neuroevolution, which can be applied to black box problems
• Neuroevolution differs from meta-learning, which focuses on learning to learn or fine-tuning models
• Neuroevolution competes with stochastic gradient descent (SGD) by using a population-based approach
• Neuroevolution is effective in scenarios where computing gradients is difficult, such as reinforcement learning and multi-objective optimization
• Etsy uses neuroevolution for search problems due to diversity in their dataset between queries and products
• The need to balance two conflicting goals in a marketplace: making existing sellers successful while also enabling new sellers to succeed.
• The concept of the Pareto frontier and the challenges of optimizing multiple objectives simultaneously.
• Using neuroevolution to find an optimal balance between different tradeoffs, but facing computational efficiency issues.
• Mitigating these issues through more efficient languages and algorithms, such as evolutionary strategies and second-order approximators.
• Integrating neuroevolution into a search stack at Etsy, specifically using it in the business intelligence layer for refining search results.
• The results of online experiments showing that the approach worked well, but with trade-offs between different metrics.
• Optimizing relevancy at position K, where precision at K was prioritized over accuracy
• Implementing policies and strategies to manage machine learning systems
• Using Rust in productizing machine learning systems for efficiency and safety
• Replacing C and C++ with Rust to address common problems like buffer overflows and null pointer dereferencing
• Integrating Rust with Python using projects like Py03
• Addressing challenges in the search space, including feature engineering and deploying models across different languages (Python, Java)
• Exploring use of Rust or similar language to embed machine learning algorithms in both Python and Java environments
• Constraints around managed memory in languages like Java and Python led to focusing on Rust for feature engineering and neural evolution
• Rust was chosen for its performance capabilities and ability to scale up systems without paying a performance penalty
• Two main systems written in Rust, Buzzsaw and neuroevolution pieces, are used to power hundreds of billions of predictions daily
• Moving from Python to Rust allowed for significant speedup (100x) and reduction in memory footprint in the neural evolution space
• Implementation overhead was not high due to experience with Rust among developers
• The Rust community is still growing and developing, but indicators suggest it has potential to blossom in the AI/ML space
• Adoption of Rust in industry, particularly by companies like Facebook
• Challenges with using Python for machine learning and AI development (cost of running, maintenance)
• Introducing Rust as a more efficient alternative for large-scale machine learning projects
• Overview of the Rust community and its welcoming nature
• Comparison between Rust's development and that of Go, highlighting Mozilla's involvement in building Rust for the community
• Resources available for learning and adopting Rust (books, GitHub repos, online communities)
• Open problems in search space influenced by AI
• Excitement about the current state of search technology due to increased openness in industry and publication of state-of-the-art research
• Integration of machine learning at every level of search platforms, including using GANs and BERT for NLP tasks
• Handling scale and real production problems in information retrieval systems, such as those faced by Chinese e-commerce companies during Singles Day
• Blending of lines between machine learning, distributed systems, and systems engineering in search systems
• Faster incorporation of techniques from conferences into practical search solutions