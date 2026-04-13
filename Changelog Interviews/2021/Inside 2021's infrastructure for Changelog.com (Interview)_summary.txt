• The podcast is called "Ten Times Better"
• The current setup is an order of magnitude better than the previous one
• The previous episode was a big change, with Kubernetes and a three-tier web app setup
• Gerhard argues that this is not overkill, but rather a complex system with many components that need to be managed
• The current setup has a control plane that manages all the components and automates tasks
• Migrating from the 2021 setup to the 2022 setup took only 27 minutes
• Gerhard had some prior knowledge of Kubernetes, but had to learn more to implement it
• The main topic is the improvements made to the Changelog infrastructure
• The law of diffusion of innovation was discussed, with Gerhard Lazu explaining that Kubernetes is currently in the late majority stage of adoption.
• Gerhard Lazu shared his experience with adopting Kubernetes, stating that they waited for a managed Kubernetes service from their hosting provider, Linode, before implementing it.
• The conversation turned to the challenges of adopting PostgreSQL with Kubernetes, specifically issues with replication and data loss.
• Gerhard Lazu discussed the importance of having good backups in place to mitigate the impact of data loss.
• The discussion highlighted the immaturity of some aspects of Kubernetes, including the complexity of documentation and the difficulty of resolving issues.
• PostgreSQL issues in Kubernetes
• Network latency and its impact on system performance
• Linkerd as a potential solution for latency issues
• The complexity of Kubernetes and its tooling
• The value of simplicity in system design
• The use of S3 for backups and disaster recovery
• Experiences with Linode Kubernetes engine and early adoption challenges
• Proper CDA integration with Fastly increased the website's speed to 15 times faster
• Integration with Grafana Cloud for monitoring and synthetic monitoring
• Caching was not properly set up before, resulting in average latency of 818 milliseconds
• After setting up caching behind the CDN, average latency decreased to 66 milliseconds
• The team had previously relied on a centralized, single point of presence for serving responses, which led to slower speeds for users in other regions
• The team is now using worldwide monitoring with Grafana Cloud to understand the full-rounded picture of the problem
• Observability provided data to understand the problems and improve the website's performance
• Kubernetes is not required to use Grafana, but it is often seen as a simplified plane for teams to understand cloud-native concepts
• Kubernetes and its standardized API for teams to understand and manage
• Average latency of 880 ms, with highest latency of 200 ms in Dallas and 400 ms in London
• Grafana probes can be overloaded, leading to high latency and errors, but not necessarily issues with the website itself
• CDN caching and micro-caching to serve cached content while asynchronously requesting updates
• Overloaded probes can cause issues, such as the one in Frankfurt with frequent spikes in latency
• NGINX logs show response times, traffic served, and the ability to visualize the same metrics after CDN cache
• High latency in NGINX to app response time, especially in short time intervals, indicating a problem that was previously unknown
• Large host with 32 CPUs, 64/128 gigs of RAM, and SSDs, yet high latency between Ingress NGINX and app suggests an issue in the queue proxy or overlay network.
• The hosts are grappling with the complexities of their infrastructure and considering whether to invest in Kubernetes or a platform-as-a-service
• They discuss the issue of bandwidth and the need for a high amount of terabytes of bandwidth
• The hosts explore the concept of "zooming in" and the law of diminishing returns, where further optimization may not be worth the resources invested
• They consider using tracing to help identify the source of issues, but note that it may not be the solution
• The hosts discuss their desire to share their experiences and knowledge with others through a new show, Ship It
• They aim to have a consistent and regular format for sharing stories and experiences, and to invite other teams and experts to share their own stories
• The hosts acknowledge the complexity and ever-changing nature of infrastructure and technology, and the need for ongoing learning and exploration
• Elon Musk as a guest on Ship It to discuss shipping Kubernetes to Mars
• Ship It's approach to improving infrastructure and speed
• The importance of knowledge and understanding in improving systems
• Potential community involvement in the show, with topics and guests suggested by listeners
• Gerhard's goal of sharing interesting topics and solving specific problems that others would find helpful and interesting
• The possibility of a Ship It community, with enthusiasts sharing ideas and approaches on how to improve systems
• Creation of a community channel (Ship It) for discussion and idea sharing
• Comments enabled on episodes, with potential for improvement in design and user experience
• Discussion of community engagement and feedback mechanisms (e.g. Changelog.com/request)
• Importance of building systems for easy and straightforward shipping
• Introduction of Gerhard Lazu as a weekly podcast host for Ship It