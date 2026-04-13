• Shopify's monolithic application and its limitations
• Decision to split the Storefront domain into a separate application
• Details of the monolith and its components (Storefront, admin, payment processing, etc.)
• The Storefront's rewritten application and its goals (simplified Ruby app, separated from admin)
• Success criteria for the rewrite (same features and behavior as the older application)
• Use of a verifier mechanism to ensure equivalent output for the same input
• Goals for the project: improve performance, scalability, and resilience
• Considered alternative languages and runtimes, but decided to stick with Ruby due to existing infrastructure and knowledge
• Focused on Storefront due to its high traffic volume and performance requirements
• Extracting Storefront from monolith to optimize for performance and scalability
• Planning to leverage TruffleRuby for performance improvements
• Prioritizing Storefront due to its impact on user experience and business goals
• Shopfroont's rewrite from Rails to pure Ruby for performance improvements
• Hybrid approach combining Ruby and Rails components
• Use of self-destructive style method calls to optimize memory consumption
• Comparison of Active Record and simple SQL for memory usage
• Goal of feature parity between old and new implementations
• Importance of verifying equivalent responses between old and new backends
• Team's success criteria: feature parity, improving performance, and improving resilience and capacity
• Guide rails for measuring progress and identifying issues during the rewrite
• Verifier mechanism to compare new service with monolith reference baseline
• Diffs and discrepancies found in verification process
• Most issues due to missing modules, bugs, or differences in output
• Verifier mechanism implemented in NGINX routing module using Lua
• Traffic patterns and sampling used to identify areas of focus for improvement
• Diffs can range from extreme (e.g. blank page) to minor (e.g. missing newline)
• Patterns and normalization used to filter out non-problematic issues
• Parity tracking and logging system used to triage and prioritize issues
• System not a traditional error tracker, but a custom solution for parity tracking
• Approaches to addressing the issue of supporting multiple merchants, including breadth-first and depth-first methods
• Use of dashboards and logging pipelines to track and prioritize issues
• Team approach, dividing tasks between depth and breadth teams
• Gamification and tracking progress towards 100% support
• Challenges of a moving target, with changes to the monolith storefront requiring catch-up efforts
• Impact of merchant behavior on progress, with features being used before support is added
• Implementing a new application while maintaining parity with the existing monolith
• Drawing a line to determine which features are handled by the new application and which by the existing monolith
• Addressing bugs and sub-optimal aspects of the monolith in the new application for parity
• Implementing a verifier to ensure traffic is rendered correctly in the new application
• Gradually rolling out the new application to a small number of shops and eventually increasing the number
• Maintaining reverse parity by keeping the same features in both codebases for a certain period
• Eventually removing the old code from the monolith and making the new application the canonical source of truth.
• Rewrite of Shopify's storefront implementation
• Trade-offs involved in rewriting, including temporary overlap with old implementation
• Communication and awareness among development team and stakeholders
• Performance improvements, including 3x-5x faster storefront response times on cache misses
• Steps to doing a rewrite right, including shortest feedback loop possible and frequent verification of implementation
• Starting small to validate approach and scope
• Making it easy and enjoyable to work on the new thing, reducing friction and adoption barriers
• Importance of documentation and public support for new application
• Setting tripwires or failure thresholds to measure progress and make informed decisions
• Showcasing progress and results to stakeholders, such as the Shopify town hall meeting
• Achieving parity with the existing application, currently at +90% with a goal of 100%
• Progress toward 100% traffic being served by new implementation
• Fixing last few differences and finding ways to speed up process
• Team effort to resolve issues
• Parity diff fixing and external communications with merchants
• Shopify-wide initiative
• Successful outcome and sense of accomplishment