• Introduction to Ecosyste.ms and its relation to Andrew's previous projects
• Andrew's background in open source metadata and sustainability
• The development of Libraries.io and its focus on package manager metadata
• The challenges of maintaining Libraries.io as a side project and the decision to sell to Tidelift
• The issues with Tidelift's culture and the outcome of the sale to Sonar
• The history and context of Ecosyste.ms and its goals
• Development of Ecosyste.ms as a rewritten version of Libraries.io
• Lessons learned from Libraries.io, including its scalability and performance issues
• Ecosyste.ms as a modular, scalable platform for collecting and combining open source metadata
• Reuse of code from Libraries.io, including the dependency parser and package manager mappings
• Usage of Ecosyste.ms in research, including studying package manager behaviors and security issues
• Potential for Ecosyste.ms to track how CLIs install themselves and their dependencies
• Indexing of public Docker images and running SBOM scanners on them
• The Debian popularity contest is a good proxy for download stats, but it's opt-in and not comprehensive.
• 0.01% of packages make up 80% of usage in package ecosystems, with 10,000-15,000 packages being the most used.
• 15,000 people are maintaining the critical level of open source usage, with 1 maintainer per package on average.
• 25-50% of top critical packages have some way of receiving automated donations or funding.
• Some packages use GitHub Sponsors or Open Collective as a way to sell digital goods or services, rather than donations.
• There is a significant difference in the number of individual vs. company sponsors on GitHub Sponsors, with individuals sponsoring other individuals at a much higher rate.
• Open Collective is used more for large company sponsorships of projects, rather than individual donations.
• The speaker discusses the difficulty of supporting open-source projects financially
• The impact of global economic changes, particularly the COVID-19 pandemic, on open-source funding
• The use of Open Collective for transparent financial tracking
• The scale of the project, with 12 million packages, 287 million repositories, and 24.5 billion dependencies
• The technical infrastructure, including Postgres databases, dedicated machines, and Dokku as an open-source alternative to Heroku
• The data management and caching system, including Cloudflare and aggressive caching
• The team and contributors involved in the project, including part-time staff and volunteer contributors
• The vision for the project, including automating analysis and publishing of open-source data to facilitate research
• Ecosyste.ms project funding and sustainability
• Grant from Schmidt Sciences to support initial work
• Support from Open Collective and customers for data access and analysis
• Recent grant from Alpha Omega to make Ecosyste.ms long-term sustainable
• Plans to implement new features and improve onboarding for customers
• Revenue share model with maintainers of command line tools
• Potential income sources, including relicensing of data and customer fees
• Balance between sharing data and paying for its maintenance
• Efforts to standardize package metadata and support different ecosystems
• Use of SBOMs and integration with GitHub Actions
• Discussion of package manager ecosystems and their quirks
• Notably hard-to-work-with ecosystems, including R, Maven, and npm
• Legacy issues with package metadata and versioning
• R package manager's unusual behavior and lack of API
• The challenge of maintaining and funding open-source software
• The potential for connecting papers and citations to software usage
• The "unsolved social problem" of open-source contribution and maintenance
• Software Heritage Project: a massive index of open-source files to help solve dependency management issues
• Importance of lock files in package managers for reproducibility and maintainability
• Using AI to scrape APIs and extract data from large datasets
• Challenges with MCP adapters and security implications of prompt injection
• Rate limits and polling in API usage, and strategies for managing enthusiastic users
• Potential solutions for large-scale data queries, including a read-only column store database
• The time requirements for research can be flexible, with some users accepting data that is a day or a week old.
• Andrew Nesbitt's primary user is himself, allowing him to understand the needs of others.
• The platform's APIs are open and useable, with each one having its own open API YAML spec.
• Users are building tools on top of the platform, such as Parlay, which enriches SBOMs using Ecosyste.ms.
• SBOM enrichment involves taking raw data and adding additional information to it.
• The platform is being used to support multi-ecosystem use cases, where a single tool is needed to manage different types of software dependencies.
• The substrate of the platform is being used to build various applications, including the Funds app and the Dashboards app.
• Future development priorities include building a search engine and tools to help maintainers understand who is using their software.
• The platform's user base includes a mix of humans and automated systems, such as Docker pulls and CI builds.
• Building a CI that tests changes against popular downstream users to ensure compatibility
• Providing maintainers with data-driven insights to be proactive about changes and collaborate with users
• Using Dependabot data to track PRs and understand user behavior
• Empowering maintainers to improve their process and make better open source software
• Exposing data to maintainers through a user interface, such as showing top dependents and version usage
• Using AI to help with large amounts of users and automate tasks, such as upgrading users to the latest version
• Tracking users through natural usage patterns, rather than invasive telemetry
• Using project-level data, rather than individual user data, to avoid complexity and maintain volunteer-driven projects
• Avoiding automated pull requests and instead using data to inform proactive decisions
• Information black holes for features and tracking in open source
• Challenges of collecting and processing large amounts of data, including structured and unstructured text
• Use of Large Language Models (LLMs) and their potential for open source discovery
• Ad-supported tools like AMPCode for accessing LLM functionality
• Open source taxonomy and categorization of projects based on facets like technology, user role, and domain
• Alignment and standardization in open source discovery and community development
• Creating a taxonomy for open-source software in research space
• Challenges in discovering and navigating open-source projects
• Importance of categorization and structure in open-source projects
• Exploring new ecosystems and languages through the help of LLMs
• Identifying gaps in specific spaces and opportunities for improvement
• Collaboration and input from experts needed to expand and improve the taxonomy
• Using data to have a positive impact on the open-source world