• Kurt Mackey discusses the challenges of building a cloud platform and the complexities of scaling to meet customer demand.
• He explains that Fly's proxy has been a point of failure in unexpected ways, affecting a large number of users.
• Adam Stacoviak mentions that the conversation will be sponsored by Fly, and that they want to talk to other platform providers, including Railway and Render.
• Kurt Mackey suggests a podcast format where multiple platform providers can have a non-one-sided conversation and discuss their differences and approaches.
• The conversation touches on the idea of inviting DHH (David Heinemeier Hansson) on the podcast to discuss his opinions on cloud platforms.
• Kurt Mackey shares his thoughts on DHH's Twitter comments about Fly's issues, and Adam Stacoviak confirms that DHH does listen to the podcast.
• The discussion covers the differences between cloud providers, including AWS, and other companies like Vulture, Hetzner, and OVH.
• Discussion of DHH's "merchants of complexity" comment and its application to Fly's infrastructure
• Complexity and scalability of Fly's global proxy and its impact on app performance
• Critique of overselling of infrastructure complexity for financial gain (e.g. Hortonworks)
• Comparison of Fly's infrastructure to AWS and the differing expectations for availability and cost
• Market pressure to offer very low-cost or free options for insignificant projects and mostly free for significant projects
• Fly's efforts to make its platform more accessible and affordable for developers
• Companies like Neon and Supabase are competing in the managed PostgreSQL market.
• Neon's value proposition is providing scalable, serverless PostgreSQL for a low cost.
• Supabase's goal is to get developers to use their product, which runs on PostgreSQL, as a platform for building applications.
• Neon's architecture is more focused on providing a "zero-cost" PostgreSQL solution, while Supabase is more interested in providing a platform for building applications.
• Kurt Mackey suggests that Supabase would use Neon's service if it were easier to work with, but currently, Supabase has its own PostgreSQL implementation.
• The concept of the "Rebel Alliance" refers to a strategy where multiple companies work together to provide complementary services, rather than competing directly.
• EC2 startups and infrastructure services
• S3 and Tigris object storage
• Supabase for Postgres
• The concept of a "Rebel Alliance" cloud, where companies build and share specialized infrastructure
• The potential drawbacks of a Rebel Alliance cloud, including UX and compliance issues
• Fly's shift in approach, from partnering with other companies to building out its own infrastructure
• Building managed Postgres on Fly's infrastructure
• Kurt Mackey's approach to competition: focusing on doing well for existing users rather than competing with other platforms
• The benefits of Fly's globally distributed infrastructure and compute capabilities
• The company's reliance on their own hardware and networking, and the benefits of controlling costs and supply chains
• The potential risks of building on a single platform, such as Fly, and the importance of having a strong relationship with the platform provider
• Kurt Mackey's philosophy of prioritizing doing well for existing users and avoiding the need to "pitch" or convince users to switch to Fly
• Tigris benefits from Fly's global compute and load balancer capabilities, allowing them to scale without building their own infrastructure.
• Tigris pays close to market price for hardware and bandwidth, with minimal profit for Fly.
• The companies are exploring a Venn diagram of overlap, where Fly's capabilities complement Tigris's needs.
• Tigris plans to add cold storage capabilities, which are not currently offered by Fly.
• Object storage is a critical piece of many applications, and Fly's integration with S3 has been streamlined.
• Tigris benefits from Fly's large developer base and streamlined signup process.
• Upstash and Tigris are seen as successful examples of companies that have leveraged Fly's capabilities and ecosystem.
• Alliance as a future outcome that is not being relied upon
• Postgres as a missed opportunity, where Fly could have been five times bigger if managed Postgres was shipped in 2020
• Challenges in working with Postgres providers, including some being "leeches" that only wanted to sell to Fly rather than be a partner
• Difficulty in storing data on the platform without a database, making it easy for customers to leave if they have issues
• Decision to work with Percona and offer a managed Postgres service instead of pursuing an alliance
• Recognizing the value of a managed database and the difficulty of doing it, but choosing to punt on the alliance
• Kurt Mackey's approach to building a managed database service, focusing on solving real problems rather than trying to be novel
• Percona's tooling and Kubernetes support being used to simplify database management
• The decision to "buy" from Percona rather than building everything from scratch
• The importance of reliability and meeting user needs rather than trying to be "world-beating"
• Comparison of Fly's approach to more exotic database services like PlanetScale and Neon
• Discussion of the limitations and potential for building on top of Fly's service
• Adam Stacoviak discusses the difficulties his company has faced with their CDN provider, Fastly, citing issues with the VCL (Varnish Configuration Language) not being versioned, making it hard to collaborate on code, and APIs changing without notification.
• He mentions that his team is currently building a simpler CDN on top of Fly, using Varnish, and exploring the possibility of making it usable by others.
• Kurt Mackey, founder of Fly, is interested in this project and suggests that his company's existing infrastructure could support a CDN without the need for complex setup.
• The conversation touches on the history of CDNs, with Mackey sharing his experience of launching Fastly, which gained popularity due to its instant purge feature.
• Adam Stacoviak mentions that his team is not using Tigris, but Mackey suggests they consider using it instead of Varnish.
• The speaker discusses the limitations of proprietary CDN solutions and the potential benefits of using cloud providers like Fly
• The speaker's company had previously built a proprietary CDN solution but decided to pivot to a cloud-based solution
• The speaker mentions the challenges faced by companies like Cloudflare and Fastly, which were successful but locked into proprietary solutions
• The speaker discusses the concept of "Pipe Dream", a single-purpose multi-tenant CDN for a specific company (Changelog) that runs Varnish cache and is open source
• The speaker and Adam Stacoviak discuss the potential for a simple CDN solution, and the possibility of building a open source CDN like Pipe Dream
• Kurt Mackey mentions his previous blog post "The five-hour CDN" and its potential influence on the Pipe Dream idea
• The conversation touches on the idea of building a custom CDN solution versus partnering with a existing CDN provider
• Kurt Mackey mentions his experience with building small demo projects as a way to cope with burnout, and suggests that building a custom CDN solution like Pipe Dream may be his next project
• The benefits and limitations of using a CDN as a separate service vs. having it built into an app
• Kurt Mackey's personal experiences and lessons learned from building Fly, including its impact on his mental health and relationships
• The challenges of building a company and maintaining a work-life balance, including the potential for self-medication and depression
• Kurt's journey of self-discovery and therapy, including his divorce and his newfound understanding of the importance of emotional energy from multiple areas of his life
• The nuances of marriage and its effects on children, including the idea that a bad marriage can be better for children than a toxic one
• Kurt Mackey discusses his experience of going through a divorce and finding relief on the other side
• He talks about learning to be content with himself and finding ways to enjoy solo activities, such as building Lego sets while watching TV
• Adam Stacoviak recommends a Lego cooking YouTube series and discusses its production quality
• Kurt Mackey shares his favorite TV shows and movies, including Ted Lasso and Fallout
• He discusses his preference for reading physical books over listening to audiobooks, unless he's already read the book
• Adam Stacoviak recommends an audiobook narrator, Ray Porter, and suggests the Bobiverse book series
• Kurt Mackey recommends the book Children of Time by Adrian Tchaikovsky, comparing it to the Bobiverse series in terms of its speculative fiction elements.
• The speaker discusses their thoughts on time and its perception in the context of traveling at high speeds.
• The speaker praises the narrator of an audiobook for their ability to immerse listeners in the world of the story.
• The future of Fly, a company, is discussed, with the speaker expressing a desire for the company to be enduring and have an impact.
• The speaker acknowledges the risks and challenges facing Fly, including competition with monopolies and the need to grow significantly to be sustainable.
• The company's current financial situation is described as healthy, but the speaker is cautious about the future, citing the potential for outages and a shift in the perception of the company's value.