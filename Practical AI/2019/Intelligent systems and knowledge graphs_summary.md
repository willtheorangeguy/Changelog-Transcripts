• Sponsors: Fastly, Rollbar, Linode, DigitalOcean
• Introduction to the Practical AI podcast and its hosts Chris Benson and Daniel Whitenack
• Discussion of messy data issues and NVIDIA's GTC conference
• Upcoming session at GTC led by Chris Benson with a fireside chat on intelligent systems and knowledge graphs
• Guest introduction: James Fletcher, principal scientist at Graken Labs, discussing machine intelligence and cognition
• Introduction to machine learning capabilities
• Transition from research to commercialization
• IP and licensing of algorithms
• Commercialization challenges and lessons learned
• Shift in focus from AI to hardware and robotics
• Application to veterinary science and human health
• Importance of finding a specific vertical or problem to solve
• Connection between animal welfare and technology
• Starting a new endeavor in an area with connection or passion can lead to success
• Passion and motivation are key drivers for learning and sticking with something long-term
• The speaker's transition from robotics and microscopy to knowledge graphs was driven by desire for impact and challenge
• Graken is a database that specializes in knowledge graphs, which store large amounts of knowledge as interconnected data points
• Knowledge graph is synonymous with knowledge base, but the term "knowledge graph" is used due to its sexier connotations and ability to convey the graph-like structure of the data
• Graph databases vs relational databases
• Advantages of graph databases for network data
• Knowledge graphs and their benefits
• Natural representation of complex relationships in data
• Simplification of querying and referencing data with a graph structure
• Graken schema allows entities, relations, and attributes to be created
• Entities can be abstract concepts or concrete objects like people or companies
• Relations are the glue between entities, providing flexibility in modeling relationships
• Hyper edges allow multiple relationships to be represented with a single relation
• The schema enables complex domain representation and data validation
• Labeling elements in the graph provides context for search and querying
• User-friendly interaction with data is key, allowing users to use their own domain terminology
• Entity-attribute relation principles in knowledge graph design
• Meeting of philosophy and technology in knowledge engineering and representation
• Role of ontologists in knowledge graph design
• Importance of true-to-domain modeling in knowledge graphs
• Defining schema elements as classes in object-oriented programming analogy
• Schema as a map for data, defining what exists in the knowledge graph and how they're connected
• Importance of disallowing invalid relationships in schema to prevent incorrect data
• Misconception about knowledge graphs: they don't just collect existing internet information automatically.
• Developing a schema for knowledge graphs requires effort and careful consideration of the types of knowledge being represented.
• Entity recognition and automated processes can be used, but focus on building from ground up with proprietary data.
• Artificial intelligence is related to knowledge graphs as they are central to creating intelligent systems.
• Knowledge graphs can provide data for AI models or serve as a source for training them.
• Automated reasoning and logical programming (e.g. Prolog) can infer new information based on existing data and rules.
• Tie-in between automated reasoning and current technologies like generative adversarial networks and natural language processing is possible, but not directly equivalent.
• Developing rules to definitively determine the truth of new facts based on existing knowledge
• Complementing machine learning approaches with logical reasoning in AI systems
• Integrating logic, intuition, and machine learning for intelligent decision-making
• Building learners on top of a logical reasoner and knowledge graph
• Iterative process between fact learning and reasoning
• Knowledge graph applications:
  • Question-answering tasks
  • Graph completion (predicting new links)
  • Enriching graphs with background knowledge
• Applying background knowledge to NLP systems and computer vision systems
• Improving customer service platforms with integrated knowledge graphs
• Discussing whether a customer's complaint about a broken connection can be directly understood based on their product usage.
• Machine vision and the challenges of identifying objects within images.
• Knowledge graphs and augmenting AI with contextual information to improve accuracy.
• The distinction between graph-based data for computation vs. graph-structured data in knowledge representation.
• Approaches to processing graph-structured data in machine learning pipelines, including transforming square inputs into more suitable formats.
• Investigating methods for moving from traditional vector or matrix representations to graph-based inputs for AI systems.
• Discussing random walk approaches for analyzing graphs
• Introducing GraphSage approach to analyze neighbors and their neighbors
• Critique of current methods as too generic, missing specific connections between entities
• Need to learn graph structure data in a neural network for more accurate predictions
• Comparison with natural language processing (NLP) where context is crucial for understanding
• Importance of moving beyond curve fitting to true understanding in machine learning
• Discussing the importance of identifying specific features or structures in a knowledge graph related to one's interests
• Introduction to the GraphNets library and its ability to learn over graphs
• Using TensorFlow with GraphNets for graph-based tasks
• Graken: a system for building, querying, and maintaining knowledge graphs
• KGLib: a library for machine learning on top of knowledge graphs
• Building a knowledge graph with Graken: components involved and steps required
• GRPC (Google's remote procedural call) has replaced REST services
• Clients use native language to access database through Grakel query language
• Grakel allows users to make function calls that interact with knowledge graph
• Bulk upload techniques exist for importing data into Grackle
• Users can migrate from SQL or CSV data using ETL pipelines
• Automatically building knowledge graphs is possible, but requires human understanding and iterative process
• Links to documentation and resources on Grackle's website
• Availability of examples repository on GitHub
• Introduction to KGLib repo for machine learning applications
• Recommendation to check out Grackle's blog for more information and motivation
• Discussion of bandwidth providers (Fastly) and error tracking tool (Rollbar)
• Information about hosting platform (Linode) and show sponsors