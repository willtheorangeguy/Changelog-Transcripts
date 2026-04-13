• Kaizen discussion and changelog compilation
• GitOps implementation challenges
• Using Honeycomb for question asking
• Jared's work on moving static files to S3-like object store
• Christmas gifts and upcoming episode themes
• Importance of GitHub Codespaces integration
• Backstage 20 release and Changelog 459 relation
• Partnership announcements (Fastly, LaunchDarkly, Linode)
• Fly platform promotion for global app deployment
• The conversation revolves around an incident that occurred and how it has been addressed
• The incident is related to a GitOps approach where unhealthy pods were put back into service using the "latest" tag
• The speaker explains that the latest tag refers to the most recent version, which can be problematic if the latest version is broken or outdated
• A tradeoff was made in the past by allowing corners to be cut for efficiency, but it failed once and now needs to be revisited
• The conversation turns to a need to revisit the GitOps approach and consider using fixed versions instead of "latest" to avoid similar incidents
• The speaker reflects on how they learned about the incident through investigation and analysis of the manifest
• They discuss the importance of capturing specific version numbers for apps and containers to avoid infinite loops or failures.
• Difficulty in handling unfinished TV shows and similar content
• Discussion of GitOps and its implementation
• Current lack of proper GitOps configuration in the system
• Need to use GitOps properly with tools like Argo CD
• Reviewing resources for learning about GitOps, including GitOps.org and WeWorks' website
• Understanding of push-based and pull-based deployment models
• Importance of following a standardized flow for deployments to prevent issues like using "latest" when it's broken
• Capturing production for recovery from disaster
• Importance of specific SHA (version) tagging in container images
• Incident where a "disaster" occurred due to a broken "latest" tag and continuity not being in place
• The role of caching and CDN in minimizing the impact of the incident
• Integration with Honeycomb for enhanced visibility into app behavior and interactions
• Resolving an issue related to slow MP3 requests using pull request/issue 383.
• Integration with Honeycomb provides detailed insights into CDN performance
• Observability features allow for slicing and dicing of data by various criteria, including top URLs, browser, user agent, country, and city
• Cache status and hit/miss rates can be viewed in detail, as well as audio request breakdowns
• Derived queries enable exploration of specific issues and root causes
• Slow requests and their impact on website performance are identified, with an example of a GIF taking 1.4 minutes to load due to its large size and need for travel to the data center
• Discussion of a large GIF file being served from Newark to Hong Kong and taking a long time to load
• Use of lazy loading to improve user experience by allowing content to be accessed while the image is still loading
• Issues with cache misses on Fastly CDN, including expired content not being cached indefinitely
• Limitations of current caching setup, including headers asking for content to be kept in CDN for a few weeks but it may expire when requested again
• Discussion of paying for caching service to keep all content cached globally
• Assessment of total assets and weight of content to determine feasibility of caching everything
• Discussion of latency and tail latency issues
• Idea to serve static content from CDN instead of own infrastructure
• Law of diminishing returns and slow clients consuming resources
• Need for optimization in serving non-cached content from CDN
• Requesting Fastly to cache content indefinitely
• Imposter syndrome due to feeling like not using CDN correctly
• The speaker is frustrated with the performance of their CDN, specifically Fastly
• They discuss how long-term content is not being cached as expected
• They mention that they are a media company with static content that doesn't change often
• They express confusion about why the CDN is not working as intended despite following best practices
• They suggest that there may be issues within the CDN itself or its configuration that need to be addressed
• They propose reaching out to Fastly for further assistance and collaboration.
• Discussion of a high number of misses in MP3 file delivery
• Importance of data visibility and the impact of having "hard facts" with Honeycomb integration
• Conversation about Fastly's functionality and how it handles misses
• Reference to LaGuardia and Hong Kong locations, possibly related to edge caching or CDN configuration
• Explanation of Incident.io and its role in incident management within Slack
• Promotion of Raygun for performance monitoring and user insights
• Personal anecdote about setting up new M1 Macs
• Discussing challenges with setting up M1 Mac for changel.com development environment
• Considering alternatives to Docker and GitHub Code Spaces
• Wanting to run own infrastructure on Equinix Metal or Linode
• Concerns about cost and simplicity of GitHub Code Spaces
• Understanding GitHub's infrastructure and lack of agnosticism in dev environments
• Suggesting alternative cloud spaces options, such as Gitpod
• The speaker wants to discuss using GitHub Code Spaces for development environments.
• They mention wanting to partner with GitHub and have them sponsor Changelog's use of Code Spaces.
• The speaker prefers using a pre-built, automated dev environment over setting up their own local machine.
• They express frustration with managing upgrades on their local machine and the potential for conflicts between personal projects and work-related development environments.
• The speaker considers an electric vehicle analogy to describe their desire for a "prescribed dev space" that is easy to use and doesn't require them to manage upgrades or configurations.
• They discuss the importance of identity and access control in such a dev environment.
• A short-term solution suggested is using Code Spaces as it currently exists, with the hope of future improvements.
• Discussion of using GitHub Code Spaces as a solution for the Changelog app
• Comparison with Gitpod and Equinix Metal
• Planning for a future episode on GitHub Code Spaces in December
• Short-term solution: brew install Elixir, brew install Postgres, clone the repo (rejected)
• Alternative short-term solution: use Code Spaces wrapped in a bow (GitHub-provided infrastructure)
• Shipping delays for new MacBooks
• Using old machines as a temporary solution
• Uploading to cloud storage (specifically S3)
• Prioritizing tasks due to limited time and GitHub issues
• Bug fix: newsletter links proxy encodes special URLs with HTML instead of percent based
• Apostrophe in URL causing encoding issue
• The speaker is investigating an issue with a web framework, specifically Elixir Phoenix, where an apostrophe in a URL is causing HTML encoding instead of URL encoding.
• They consider it a dependency issue and seek advice on how to proceed from Gerhard.
• Gerhard suggests checking for issues in the repository, looking at code changes around the problem area, and opening an issue if necessary.
• The speaker questions whether this is actually a bug or just expected behavior.
• They decide to upgrade all dependencies, including Phoenix, rather than addressing the specific issue directly.
• The upgrade process reveals breaking changes in the new version of Phoenix that were not anticipated by the speaker.
• Upgrading from Phoenix 1.5 to 1.6 caused issues with API changes
• Two specific keys in the "assigns" data bag were removed: view module and view template
• The removal caused metadata issues on the entire site, including Twitter embeds and third-party integrations
• The developer had to refactor the meta module and fix several hours of work
• A yak was shaved (in a humorous analogy)
• Upgrading or replacing Ingress Nginx with Traffic
• External DNS management
• Honeycomb Agent and other agents' setup
• The yak shaving problem: getting stuck in a cycle of small tasks leading to more work
• State of flow and perseverance in completing tasks
• Overconsumption of time on non-priority tasks during a state of flow
• Mention of multiple gifts and projects
• Discussion of using cross-plane to manage infrastructure
• Benefits of integrating various tools, including Dagger and Honeycomb
• Importance of giving feedback to improve products
• Storytelling approach in the podcast and its benefits
• Connection between the creators and users of certain projects (e.g. Solomon Hikes)
• Reflection on the "circle of life" and serendipity in collaborations
• Discussing feedback and suggestions for various tools, including Honeycomb, Dagger, Crossplane, and Grafana Cloud
• Importance of observability in the CDN and its benefits
• Concept of "an and proposition" rather than "either or" when choosing tools with different strengths and weaknesses
• Understanding trade-offs between different tools and not looking for a single "perfect" tool
• Upcoming episodes and topics, including contributions from Echoes initiative
• Discussion of user experience and the importance of a patient and knowledgeable approach
• Introduction to Kaizen and its application in improving processes
• Expression of gratitude to team members, listeners, and partners
• Announcement of future plans for the podcast and community
• Promotion of the changelog.com website and community
• Closing remarks and preview of upcoming episodes
• The show's previous recording was cut due to a humorous and uncontrollable break caused by Gerhard's reaction to Jared's yak shave story.
• Gerhard spent three weeks resolving his home network setup issues with multiple routers, internet connections, and physical installations.
• He now has two fiber connections, two ISPs, and additional holes in his walls.
• The conversation focuses on the absurdity and dedication required for such an extreme case of yak shaving.
• Discussion of WAN connections and network setup
• Mention of budgeting and new equipment purchases
• Use of specific software tools, including Gitpod and Codefaces
• Reference to movie "Contact" and the phrase "you can never have too many"
• Humorous exchange about wanting multiple copies of a person (Gerhard's wife)