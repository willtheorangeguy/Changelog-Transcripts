• Mike Parham's new project, Inspector, is a monitoring tool for application infrastructure
• Inspector is a reimagined version of monitoring, with a focus on guiding users to build reliable applications
• It doesn't monitor initd services, instead promoting the use of modern init systems like upstart or systemd
• Inspector aims to provide a more user-friendly and efficient monitoring experience than existing tools like Monit
• It makes some design choices that might not be liked by everyone, such as not supporting legacy initd services.
• The host and guest discuss the guest's transition to creating a commercial product on top of an open-source product, specifically with sidekick and inspector.
• The guest shares their decision to create a business model that includes both an open-source product and a commercial product.
• The guest explains that he initially only had an open-source product, but found that it didn't generate enough revenue to justify his time.
• The guest describes how he created a commercial product on top of sidekick and started selling it, which led to a good income and the ability to provide for his family.
• The guest mentions other business models, such as services and consulting, and notes that he prefers to keep his business small and focused on creating smaller, useful tools.
• The guest shares his experience with sidekick and inspector, and notes that creating a commercial product on top of an open-source product can be a successful business model.
• Open-source vs. commercial versions of Sidekick
• Concerns about people taking Sidekick features and adding them to the open-source version
• Distinguishing between paying for features and paying for long-term support and maintenance
• Customer behavior: companies want stability and support for their business, but developers may use open-source versions for personal projects
• Sales numbers for Sidekick Pro: $7,500 in 2012, $85,000 in 2013, and expected to top $175,000 this year
• Recurring income and diversification: the decision to launch a new product with a similar model to Sidekick Pro
• Diversifying investments and products to reach a wider customer base
• Inspector as a generic product useful to anyone using Linux, not just Ruby
• Diversification of products to mitigate risk of a single product's failure
• Inspiration from Mana and existing open-source tools that are cumbersome to use
• Criticism of existing open-source monitoring tools as being unfriendly and overly complex
• Goal of creating a simple, easy-to-use product (Inspector) with minimal configuration
• Steps to create a successful open-source/commercial product, including:
  • Finding a non-trivial and important tool for your current system or workflow
  • Identifying a market gap in an existing product with too many features or complexity
  • Creating a simpler, more user-friendly product that solves a specific problem
• Streamlining a word processor by simplifying and adding useful functionality
• Building a business model by offering free and paid features
• Drawing a line between free and paid functionality
• Evolving from an open-source project to a commercial product
• Monetizing a product through recurring income and pricing strategy
• Identifying pain points in software development, such as html to pdf conversion
• Using the "30 by 500" formula to calculate potential revenue
• Breaking down the process into achievable steps
• Building a business on spare time and with minimal investment.
• Salary vs sidekick pro income and when the author started considering going full-time
• Drawing a line between pro features and open source features in the inspector project
• The author's approach to distinguishing enterprise features from team features
• Balancing open source contributions with pro features and revenue generation
• Managing third-party contributions and avoiding conflicts of interest
• Lessons from Twitter's API management and road mapping approach
• Discussion of Twitter's free and paid model and the trade-offs involved
• App.net's paid model and its potential success
• The importance of network size and user engagement in social media platforms
• Paid vs free models in social media and their impact on user engagement
• The concept of a sponsored podcast and a job search platform (Hired.com)
• Contributions and user engagement on the Sidekick platform
• The use of the Go programming language in the Inspector tool and its potential impact on user engagement
• Comparison of Inspector and Sidekick as open-source projects
• Design decisions made for the Inspector tool, including removing unnecessary features and adding modern functionality
• The importance of integrating application components with the operating system's init system for reliability and maintenance
• The developer's experience with integrating components with an init system
• Removal of features from the inspector, including monitoring file permissions and directory permissions
• Simplification of the configuration process for the inspector
• Installation story for the inspector, including distribution through package cloud and package repositories
• Comparison of the open-source and pro versions of the inspector
• The developer's experience learning the Go programming language and rewriting the inspector code multiple times
• Challenges and frustrations with learning Go and idiomatic coding practices
• The speaker discusses the choice of Go as a programming language for their project, Inspector, and how it offers simplicity and a strong standard library.
• The speaker compares Go to Ruby, noting that Ruby is better suited for large-scale applications and prototyping, while Go excels at building small, focused projects.
• Inspector, a monitoring tool, is discussed, and its features, including daemon-specific metrics, host metrics, and integration with popular collaboration tools, are mentioned.
• The speaker notes that the open-source version of Inspector is still in its early days, but it will monitor any service integrated with the init system, and users can contribute their own daemon-specific metrics.
• The speaker discusses the advantages of using Go, including its simplicity, strong standard library, and low runtime dependencies.
• Inspector provides real-time monitoring and alerting for metrics, with a console-based interface
• Commercial version (Pro) supports monitoring init d, legacy systems, and has additional features
• Pro version includes features such as chat room integration for alerts, ownership management, and customizable alerting
• New features being considered for the open-source version, including monitoring cron jobs and a web interface for metric overview
• Roadmap and engagement opportunities for users to contribute to the project's development and launch
• Agenda is not an issue and the speaker is open to help and improvement
• The speaker has a list of features but wants to add more and gather ideas
• Specific feature to add more application components to the inspector
• PRs (pull requests) are encouraged to add more features
• Show notes will include links to the code and company site
• Sponsors mentioned: Code Ship, hired.com, and Digital Ocean
• The speaker thanks the audience and says goodbye