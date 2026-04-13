• Definition of observability and its origins in mechanical engineering
• Observability as a way to understand internal system state without prior knowledge
• Instrumenting code to gather context and information about system behavior
• Importance of gathering high cardinality dimensions such as user IDs and request data
• Distinguishing between metrics-based monitoring tools for infrastructure and observability for understanding code behavior
• Shift from monolithic architecture to microservices and serverless, requiring more robust observability methods
• Applying observability principles to monolithic systems and focusing on end-user experience and journey through the app
• Development teams spend more time with code than end users
• CI/CD pipelines are essential for observability and reducing bug fixes
• Observability helps engineers have a tight feedback loop by quickly seeing changes in production
• Time is key: shipping to production as soon as possible (ideally < 15 minutes) reduces bugs and pathologies
• Shipping into production is crucial, and testing in production is inevitable; the goal is to do it well with guardrails
• "Dead code" isn't valuable unless it's in production
• The number of engineers required to maintain codebase scales with time spent on maintenance, with 2x as many engineers needed for each doubling of time
• Importance of minimizing wait times in engineering, especially when trying to solve new problems or ship changes quickly
• Goal of achieving a 15-minute deployment cycle for most companies, with some variation depending on stack and complexity
• Relationship between testing and shipping speed, with tests ideally running within the same short timeframe
• Concept of "shipping" as not just deploying code, but also learning from it and getting answers to questions quickly
• Example of Changelog.com's monolithic application and how to make it more observable using Honeycomb OpenTelemetry instrumentation
• Visualization of data in Honeycomb, including features like BubbleUp for diagnosing problems and identifying differences
• Overview of the backend infrastructure for storing events, including Kafka, retriever nodes, S3, Lambda jobs, and API interactions
• Use of Kafka as a storage engine
• Comparison with Kinesis and outsourcing vs running in-house
• Managing and updating Kafka clusters
• Performance characteristics of storing data on SSDs and S3
• Monitoring and testing Honeycomb using internal "dogfood" cluster
• Automated deployment process to kibble, dogfood, and production environments
• Importance of acknowledging human fallibility and optimizing for learning
• Importance of building systems that make it easy for engineers to write code quickly
• Characteristics of a high-performing team, including ability to ship often and focus on new problems
• Benefits of joining a high-performing team vs trying to improve an existing one
• Role of engineering managers in creating healthy teams and pushing back against short-sighted approaches
• Unhealthy power dynamics between product people and engineers, and importance of triad-based relationships
• Healthy relationship between money flow and priorities, including considering long-term investment and employee well-being
• Importance of uninterrupted focus for engineers
• Measuring happiness and health of engineering teams through surveys and open communication
• Human element in software development, treating engineers as people not machines
• Observability and CI/CD pipelines for improving team performance
• Book "Observability Engineering" and its free early release