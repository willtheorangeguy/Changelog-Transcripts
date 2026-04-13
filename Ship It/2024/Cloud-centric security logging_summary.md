• Discussion of listeners speeding up the podcast and sounding like chipmunks
• Interview with Steven from Scanner about collecting logs at scale, specifically for security teams
• Importance of planning and choosing the right database and data store for logging and other applications
• Dangers of using NoSQL databases without considering performance and scalability implications
• Critique of Snowflake's use case and flexibility vs. being used for the wrong purposes
• Discussion of adapting to changing requirements and scaling needs in application development
• The guest, Steven Wu, is the CTO of a startup called Scanner that offers a petabyte-scale log search and storage solution.
• The company's architecture is cloud-native, with each component (storage, indexing, querying) farmed out to the cloud service best suited for it.
• Wu discusses the benefits of this approach, including separating compute from storage, which he believes is becoming more widely accepted as companies move to the cloud.
• He also addresses concerns about cloud costs, noting that Scanner's pricing is significantly lower than competitors like Splunk Cloud.
• The company's product is marketed as a SIEM (Security Information Event Management system) and is designed for large enterprises with significant security teams.
• Product differentiation from Athena: indexing and query speed
• Use case: freeform text search with aggregations on log data
• Schema requirements: flexible schema, no pre-defined columns or tables
• Architecture limitations: no support for multiple tables, joins, etc.
• Target market: smaller teams without database expertise or resources
• Cost savings with serverless computing
• Database management costs and challenges
• Scalability and query performance with Lambda functions
• Multi-tenancy and security considerations in cloud storage
• Trade-offs between serverless and traditional compute options
• Query use cases and volume for security analysis teams
• Cost optimization strategies for AWS services
• Cost considerations for cloud services vs. self-managed solutions
• Lambda usage costs and benefits in relation to system architecture
• OpenSearch as an alternative to Athena and its hosted service features
• Comparison of costs between various solutions (Athena, ELK stack, etc.)
• Impact of user behavior on costs and scalability
• Thresholds for free query capacity and paid usage
• Cost-effectiveness and trade-offs in system design
• Cloud providers offering similar services to the company
• Potential for cloud providers to make their services cheaper
• Trade-offs made in product development for specific use cases
• Caching mechanisms used to reduce query costs
• Operations side of companies and celebrating "ops wins"
• Company's opinionated cloud architecture and gamble on making right trade-offs
• Pipelining and aggregation features in Scanner's query language
• Query language is similar to Splunk but with some differences, requiring users to learn new properties
• Discussion of organizational problems leading to outages, such as layoffs and lack of institutional knowledge
• Azure outage on July 30th, 2024 due to DDoS attack on Azure Front Door
• Importance of maintenance and testing for software reliability
• Discussion of a recent Azure outage caused by a DDoS attack and a mistake in the CDN's load shedding setting
• The CDN was intended to mitigate DDoS attacks but instead amplified their impact due to an automated system change
• The outage lasted 10 hours and affected global access to Azure services
• The importance of human oversight in automation, especially in critical systems
• Examples of previous outages caused by automation mistakes, including Justin Garrison's own experience with taking down Disney animation for a day and breaking the internet for Google
• Discussion of another outage on July 18th that affected 24 backend services in the US Central region due to a storage problem
• Azure storage outage affecting multiple services
• CrowdStrike incident impacting servers
• Centralization of systems leading to broader impact
• Business decisions influencing availability and reliability
• Partnerships with providers require careful consideration
• Importance of renegotiating or reevaluating business decisions as circumstances change