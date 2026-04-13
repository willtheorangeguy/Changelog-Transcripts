• Introduction to the show and its hosts
• Recording location: Waikiki Beach, Hawaii
• Guest introduction: Mike Param, a Rubyist and open source enthusiast
• Discussion of Mike's past projects: MemCash Client, Dolly, and Sidekick
• Mike's history with open source: 18-year-old first project, a Windows NT35 application launcher
• Evolution of open source communities: SourceForge, GitHub, and democratization of code sharing
• Critique of SourceForge as a "punching bag" and its impact on the community
• The conversation discusses the evolution of a specific platform, including its decline and rebirth, and its shift away from prioritizing ads and towards supporting its community through membership.
• The platform's relaunch included removing ads and implementing other changes, and it is now supported by its members.
• The conversation also discusses GitHub's impact on the open-source community and its focus on helping developers and making code more shareable and liberable.
• The main topic of the conversation shifts to Sidekick, a background processing framework, and its key features and differences from other similar frameworks.
• Sidekick is a multi-threaded framework that allows for concurrent job processing, which is its main speed advantage.
• The conversation also discusses the concept of message processing and how it allows for asynchronous processing, and the importance of retry mechanisms in such processing.
• Exponential backoff and retry system for sidekick
• Potential speed boost and gotchas with sidekick
• After commit issues with sidekick and database transactions
• Delayed job and retry system
• History of sidekick and why it was created (multi-threading, performance, and features)
• The speaker started working on the open-source project "Sidekick" during a two-week downtime period after leaving their previous employer, Carbon 5.
• The idea for Sidekick came from working with a client of Carbon 5.
• The speaker initially released Sidekick under an LGPL license and offered a commercial license for $50, but this brought in minimal revenue and didn't justify the time spent on the project.
• The speaker decided to create a premium product, "Sidekick Pro," which extends the functionality of the free, open-source version.
• Sidekick Pro includes features like batch processing and reliability, which address issues with the base Sidekick version, such as knowing when jobs are complete and dealing with Ruby VM crashes.
• The speaker's goal is to make open-source projects valuable to both new and experienced developers, and to provide a way for creators to be compensated for their work.
• Alternative queuing system to prevent job loss in case of a crash
• Comparison of base sidekick and sidekick pro features
• Value of sidekick pro as a cost-effective solution for experienced developers
• Pricing and cost-benefit analysis of sidekick pro
• Concerns about forking sidekick to recreate pro features
• Discussion of the ethics of forking sidekick to create a competing product
• Success of sidekick pro sales and customer adoption
• Exploring the possibility of sidekick as a service
• Challenges of providing an execution environment for user code and sandboxing
• Discussion of heroku's similar challenges with sandboxing
• Ruby way vs Rails way
• Design decision to make perform method an instance method in Sidekick
• Multi-threading and thread safety in Sidekick
• Influence of Rescue on Sidekick's design
• Rumors of Rescue 2.0 development
• Comparison of Sidekick, Rescue, and Delayed Job
• Choosing between Sidekick, Rescue, and Delayed Job
• Evaluating software decisions for message processing
• Graduating from simple to more complex solutions as a developer learns
• Tribal knowledge in developer communities
• The speaker recommends using Sidekick for background jobs due to its efficiency and trend in the industry.
• The speaker discusses the overhead of using Redis with Sidekick, but concludes it's simple and reliable.
• Sidekick is compared to other projects, including Lunchy and Dolly, and is seen as more popular and useful due to its ability to solve a larger problem.
• The speaker explains that Sidekick was designed to make applications asynchronous and highly performant.
• Girl Friday is mentioned as a separate project that solves the same problem as Sidekick, but runs inside the Rails process and uses threads.
• Mention of past mistakes with girl friday and shift to new project sidekick
• Discussion of tone and aggression in responses to pull requests
• Personal struggle with self-evaluation and adjusting to criticism
• Acknowledgement of being better at code than community interaction
• Concerns about suppressing contributions to open source community due to fear of criticism
• Sharing of personal experiences and struggles with criticism and community interaction
• The speaker is proud that someone they had a negative interaction with went on to do great things
• The importance of being positive and kind in the digital world, and not jumping to conclusions about others' intentions
• The speaker's project, Sidekick, and how it encourages people to contribute and build on top of it
• The benefits of using Sidekick, including its ability to process a high volume of jobs
• A discussion about a blog post on the Changelog that mentioned Sidekick's speed and retry mechanism
• The speaker's own use of Sidekick and their belief that its retry mechanism is awesome and effective
• Retries in Sidekick: manual vs exponential backoff
• Programmer heroes: Tony Arcieri (Celluloid) and Jeremy Kemper (Ruby on Rails)
• Multi-threading in Celluloid: no need for mutexes
• Sidekick's dependency on Celluloid and its impact on application development
• Host's background: Ruby developer and motorcycle racer