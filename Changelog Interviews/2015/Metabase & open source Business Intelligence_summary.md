• Metabase and its goal of providing business intelligence and analytics to everyone in a company
• SQL and its role in Metabase
• Technology behind Metabase, including Clojure and JavaScript
• Metabase's connection to Samir Al-Sakran and Tom Robinson's previous work at 280 North
• Objective-J, a language extension to JavaScript developed by Tom Robinson and 280 North
• History of 280 North and its notable projects, including Cappuccino and Objective-J
• The company 280 North was acquired by Motorola in 2010 and is no longer active.
• Samir, the CEO of Metabase, has a background in machine learning and data engineering, but has moved towards data presentation and visualization.
• Most companies struggle with data, particularly small businesses, which often have no handle on their data and lack insights.
• Metabase is a tool that allows normal human beings to interact with data without writing SQL, making it easier to present and visualize data.
• The primary purpose of Metabase is to take a table or database and render it in a real way, allowing users to interact with and gain insights from the data.
• Purpose of Metabase and how it's intended to be used
• Clarifying the concept of "questions" in Metabase
• Metabase as a layer on top of databases, allowing exploration and visualization of data
• Impedance mismatch between the concept of "questions" and the actual process of exploring and building queries
• Simplifying the cognitive space for constructing queries and making it accessible to non-technical users
• Metabase's approach to letting users work in their own mental model, rather than the schema of their data
• Exploratory features, such as double-clicking on cells and following connections, to emerge from the data rather than requiring precise question formulation
• Open-source nature of Metabase
• Metabase is a company that emerged from a custom analytics system built for Expo, a startup studio in San Francisco.
• The system was designed to be highly customizable and was used by multiple companies, but the creators wanted to make it open-source and available to a wider audience.
• The company plans to offer the core Metabase software for free, open-source, and production-grade, while charging for additional features and support for large-scale commercial use.
• The decision to make Metabase open-source was driven by a sense that it's a basic component of modern data infrastructure, and that open-source is the best way to ensure a high-quality product.
• The company is exploring additional features and support for commercial use, such as compliance, data governance, and auditing, which will be available as paid add-ons.
• Metabase offers one-on-one mentoring with a TopTal senior developer for a year
• Metabase is a tool that provides a graphical way of expressing queries, making it more accessible to those without programming knowledge
• SQL was a revolutionary tool when it was first introduced, but has since become limited in its accessibility
• There have been waves of accessibility in data analysis, with each new tool (e.g. spreadsheets, Tableau) widening the pool of people able to analyze data
• Metabase is seen as a tool that can remove the barrier to entry for non-programmers to analyze data
• Having multiple tools and approaches to data analysis is beneficial, as it allows people to approach problems from different directions and perspectives
• Data analysis can be a team effort, but having too many interruptions can be distracting and inefficient.
• Metabase is a tool that allows users to ask questions and formulate queries without needing to write SQL.
• The user experience involves selecting a database, choosing filters, aggregations, and sorting options, and aggregating results.
• Metabase provides a graphical editor for expressing queries and tries to limit choices to make sense and provide special interfaces for different data types.
• The tool is read-only, and users should set up a replica database for testing queries.
• Metabase also allows users to access a basic SQL editor with auto-completion for writing SQL queries.
• The SQL editor is meant to allow users with SQL expertise to create queries that cannot be expressed through the graphical editor.
• Saved questions can be added to a dashboard and reused by others.
• Auto-detection of database connections is an ongoing process
• Supported databases: MySQL, Postgres, Mongo, SQL Server, Redshift
• Adding new database drivers involves creating a new interface or driver
• Support for RethinkDB and other databases is possible through community contributions
• Determination of which databases to support is based on community requests and GitHub issues
• Current work includes writing drivers for SQL Server and Redshift
• Future work includes supporting Elasticsearch, BigQuery, Spark, Presto, and Impala
• Plans for Slack integrations, specifically a feature called "pulses"
• Discussing new features for MetaBase, including the ability to send saved questions to various channels (Slack and email)
• The idea of "Siri-fication" of querying, where users can type free-form questions and get results without needing to structure a query
• The importance of making money as a company, and the current funding and runway situation
• Plans for MetaBase Conf (MetaConf) and the idea of a microbrewery (Meta Brewery/Meta Beer)
• Discussion of a beer named after GopherCon
• Technology discussion, specifically a project's evolution and technical choices
• Project's initial development as a Python application with jQuery charts
• Switch from Python to Scala and then to Clojure
• Current implementation, where the Clojure app compiles to a JAR file running on the JVM
• Mac app's purpose, which is to bundle the JRE with the JAR file and provide a user-friendly installation experience
• "Brain damage" associated with the team's effort to rewrite the project in various languages
• JVM's advantages in terms of ease of installation and deployment
• Scala's strong typing makes it difficult to construct a type system for dynamic queries
• The team experimented with a query language that is composable and easy to manipulate
• The query language is similar to an abstract syntax tree (AST) and allows for tree manipulations
• The team transitioned from an Angular front end to a React front end, with React now being the primary front end technology
• The team is still using RESTful JSON APIs for data transport, but is considering moving to GraphQL or similar technologies
• Exploring application of interesting ideas to Metabase
• Discussion of React and state management (Flux, Relay, Redux)
• Introduction of Redux and its unidirectional data flow framework
• Mention of Dan Abramov and his potential contribution to the project
• Database discussion (Postgres, MySQL, Redshift, H2, SQLite)
• Review of Metabase's technology stack and potential future developments
• Discussion of data fingerprinting and semantic model inference
• Types of open source projects and the desired direction for Metabase
• Initial focus on Metabase employees working on the project in the open
• Designing a user-friendly interface for Metabase
• Limitations of open-source community in creating end-user interfaces
• Identifying specific areas for open-source contributions
• Documentation and APIs for extending Metabase
• Getting started with Metabase deployment on various platforms
• Setting up Metabase on Elastic Beanstalk, Heroku, or as a jar file
• Support and resources for users (Twitter, Metabase forum, issues tracker)
• Future of Metabase: building a standard open source BI platform
• Slack integration and future capabilities
• Graph traversal and natural language question answering
• Eliminating job titles through automation, freeing up time for more complex analysis
• Importance of human labor and expertise in data analysis
• Computers writing programs for humans
• WordPress as an inspiration for user experience
• Instant gratification in database setup
• Discussion of programming heroes, specifically Jeff Dean and TensorFlow
• Announcement of the launch of season 2 of Beyond Code
• Discussion of TensorFlow and its significance
• Mention of Jeff Dean and his career at Google
• Reference to John Carmack and his reputation as a programming hero
• Discussion of open-source machine learning and client-server communication
• Mention of specific projects such as Falcor and Ohm next
• Question about the open source radar and hypothetical choice of projects to play with
• Simplification of adding new features to the frontend
• Potential implementation of Closure Script on the frontend
• Comparison of JSX with Closure Script and its accessibility
• Designers' ability to work with React and JSX
• Interest in exploring speech recognition and NLP libraries
• Discussion of proof of concept for integrating voice commands with Metabase
• Wrap-up and thank yous