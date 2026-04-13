• Building an open source company
• Challenges of creating an open source database
• Changes in the landscape for building an open source company since 2015
• Shift to cloud-based consumption models and their impact on open source
• Evolution from traditional software procurement to as-a-service models
• Future of open source in a world where everything is consumed as a service
• Preserving the best aspects of open source while adapting to changing market trends
• Amazon's business practices impact Cockroach Labs' ability to improve and innovate
• The GIMP's origin story and how it evolved from an undergraduate project to a widely-used open-source software
• Spencer Kimball's early experience with open source, including co-creating the GIMP
• How the name "GIMP" was chosen after the character in Pulp Fiction
• Kimball's career path after leaving Berkeley, including working at Accenture and a boutique investment bank
• The speaker's experience with the dotcom bust and starting a company after it
• Importance of having co-founders who have been through similar experiences
• Value of working for a successful startup before founding your own
• Need to be selective about business partners and prioritize those with whom you've shared "trench" experiences
• Benefits of learning from failures and gaining experience in the trenches before starting your own company
• Sharding problems with MySQL led to high application complexity and scalability challenges
• Resilience challenges were also encountered, particularly with traditional primary-secondary database replication
• Asynchronous replication streams can lead to data loss during failover, resulting in "regressing" to an earlier version of the state
• Google developed Bigtable, Megastore, and Spanner to address these issues, with Spanner being a key inspiration for Cockroach
• Consensus-based replication (e.g. Paxos, Raft) provides guaranteed consistency and operational continuity
• Sharding is like RAID for hard drives, providing redundancy and fault tolerance
• The popularization of NoSQL databases and cloud-native scalability was driven by various factors, including:
	+ Advancements in technology and infrastructure
	+ Changes in scale and complexity (e.g. from enterprise to web scale)
	+ Increased demand for operational continuity and consistency
• Creating software that meets current needs rather than hypothetical future ones
• The importance of using the right tools for one's specific problem, rather than relying on existing solutions from larger companies
• The origin and development of CockroachDB, including its creation as a response to limitations in open-source databases and infrastructure at the time
• The challenges of building reliable databases that can survive data center outages and maintain business continuity
• The role of Spencer Kimball's work at Square in further developing and refining CockroachDB
• The importance of being in a "flow state" while programming and how it can be meditative.
• The history of Cockroach Labs, including its founding by Spencer Kimball after leaving Square and deciding to start another open-source project.
• The company's early success with funding rounds and adoption by major companies, but the challenges that come with growth and scaling a business.
• The transition from selling CockroachDB as a self-hosted solution to offering it as a database-as-a-service (DBaaS) competitor to AWS, Google Cloud, and Microsoft.
• Strategies for competing with big cloud vendors, including innovating and out-innovating the competition, being multi-cloud or cloud-agnostic, and reducing friction in delivering databases as a service.
• Ambitious goal to make relational databases serverless and truly global
• Perpetually free tier for developers with generous storage limits
• Tiered pricing model: free for small-scale use, paid for overages
• Dedicated clusters for high-scale production use cases
• Multitenancy cluster sharing to increase efficiency and reduce costs
• Partnerships with cloud providers and other tech companies to define the next-gen stack
• Emergence of a technology stack that enables companies to build scalable services like Google
• Impact of 5G on latency improvements in communication networks
• Threshold for human-perceptible latency: under 100 milliseconds
• Potential applications and use cases enabled by low-latency networks (real-time experiences, gaming, AR/VR, self-driving)
• Challenges of providing low-latency experiences across global locations due to limitations of data transmission speed
• Importance of expanding data architecture to accommodate global use cases and comply with data sovereignty regulations