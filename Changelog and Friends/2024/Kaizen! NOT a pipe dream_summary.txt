• Kaizen 15: Gerhard's return to Changelog & Friends
• Discussion of bidets
• Gerhard mentions a significant event on June 21st, 2022, related to Ship It show
• Explanation of Kaizen and its purpose: continuous improvement and change for the better
• Adam shares his research on the meaning of Kaizen and its application in business
• The hosts discuss the collaborative nature of Kaizen and its adoption by all three of them.
• Discussion of Omphaloskepsis and navel gazing
• Introducing Kaizen as a reframe of navel gazing
• Turning navel gazing into a product or service
• Continuous improvement vs. continuous change
• The importance of effectiveness over productivity
• Gerhard Lazu's introduction to the next part of the episode
• Sharing stories and celebrating wins from the open source community
• Redesign of the Changelog News page to better serve both the podcast and newsletter
• Background story of the Changelog News podcast and newsletter, and the decision to streamline them
• Technical details of the redesign, including the creation of a separate page for the podcast and newsletter
• Shout-outs to team members and contributors who worked on the redesign
• Discussion of the new design and its features, including a "27 more reasons to subscribe" list
• A humorous exchange about the list, including the addition of two new reasons
• Discussion about a pyramid scheme in a list of reasons to subscribe
• Gerhard Lazu submits a pull request to improve the list, which is accepted by Jerod Santo
• The feature is discussed as part of the newsletter redesign
• Gerhard Lazu showcases a new feature of connecting to Neon from the local environment
• The team discusses their favorite aspects of the newsletter redesign, including the pyramidical structure of reasons to subscribe and the improved landing page
• Discussion about the future goal of acquiring changelog.news for a more streamlined URL
• Redesign of the newsletter to have a dual design, with a dark mode that represents the content and a light mode that shows the latest issue
• Discussion of the podcast/newsletter hybrid format and its unique design challenges
• Improvements to the podcast player, including making it more noticeable and user-friendly
• Demonstration of a development workflow using Neon, including resetting to a parent branch and synchronizing with production data
• Discussion of the value and benefits of using a development workflow, including the ability to recover from mistakes and minimize downtime
• Neon's dev branch database features and benefits
• Discussion of database design and security
• Gerhard Lazu's system for preventing key deletion
• Adam Stacoviak's conversation with Bryan Clark about Neon's future features
• Gerhard Lazu's "Pipe Dream" feature and future plans
• Discussion of sponsored content and newsletter design
• Gerhard Lazu's suggestions for improving newsletter formatting
• Sponsored sections blending with other content in the newsletter
• Desire for visual cues to distinguish sponsored content
• Proposal to use the money bag emoji as a consistent visual cue
• Discussion of balancing tastefulness with clear sponsorship labels
• Gerhard's preference for an option to quickly skip over sponsored content if desired
• Discussion of proposed changes to the show's format and style
• Shoutout to Brandon Smith for a one-character pull request that fixed an issue with GitHub interpreting hash signs as pull requests
• Upcoming feature: allowing Plus Plus members to create custom feeds
• Progress on integrating custom feeds, including building a feature to create custom feeds and syncing membership information from Supercast and Stripe
• Plans to roll out the custom feed feature to Plus Plus members
• WebHook system updates: subscription management and instant login
• Custom feeds development: creating and managing feeds for Plus Plus subscribers
• Stripe integration: halfway to closing the loop and becoming a full SaaS
• Podcast as a Service (PaaS) model: transitioning from SuperCast and creating a more autonomous experience
• Custom feeds rollout: allowing users to create feeds for specific shows and podcasts
• Pull request 516: integrating GitHub Actions workflows with Honeycomb for better debugging and performance analysis
• Honeycomb UI demo: exploring workflows, pipeline runs, and details on performance issues
• World Page Speed Test tool introduced by Chris McCord
• Tool connects to multiple Fly data centers to load websites in a Chrome headless browser from different locations
• Changelog.com tested with tool, showing varying load times in different locations
• Comparison with News Y Combinator and Google.com shows Changelog.com to be relatively fast
• Discussion of caching and Fastly cache
• Tool used to test loading times from Fly nodes in different locations, including Sydney, where Google.com was slow
• Discussion of HTTPS vs HTTP and potential redirect issues
• Idea to integrate tool with Honeycomb for tracking and visualization of page speed issues
• Google page load times vary greatly depending on location
• Discussion of a CDN and its potential issues
• Introduction of a new tool/service called Pipedream
• Review of a previous demo on building a CDN
• Demo of using Fly to scale Pipedream globally
• Use of the httpstat tool to analyze HTTP request breakdowns
• Approving a project and moving forward with implementation
• Discussing the cost of the project and its infrastructure
• Conducting a latency test on the Pipe Dream website
• Comparing the performance of Pipe Dream to Changelog.com
• Reviewing the Varnish configuration and code
• Deciding to deploy the Pipe Dream project
• Implementing a custom CDN using Varnish on top of Fly.io
• Discussion of bandwidth costs and potential exceeding of Fly.io sponsorship limits
• Challenges with static content serving, backend health, and log management
• Weighing the pros and cons of building and maintaining a custom CDN versus using a third-party service
• Potential for a partnership with Fly.io to sponsor the custom CDN
• Estimating the maintenance burden and the time required to complete the project
• Implementing Varnish configuration for dynamic pages with purging
• Discussing middle layer to manage Varnish caches, potentially an orchestrator
• Evaluating CDN options, with analogies comparing Fastly and Pipe Dream
• Proposing an endpoint for the current discussion, potentially concluding the saga