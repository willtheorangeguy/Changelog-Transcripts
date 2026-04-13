• Introduction of JS Party and its community
• Announcing a new episode on core web vitals with guests Annie Sullivan and Rick Viscomi
• Introducing Annie Sullivan, tech lead for core web vitals at Google Chrome team
• Describing the role of Annie's team in developing core web vital metrics and performance APIs
• Introducing Rick Viscomi, developer relations engineer for web performance at Google Chrome team
• Discussing Rick's role in helping developers understand how to make their websites faster and succeed with core web vitals
• Talking about the challenges of convincing developers to prioritize website speed and performance
• Mentioning the use of data and A/B testing to demonstrate the benefits of optimizing website performance
• Main thread: where all JavaScript code runs, responsible for DOM updates and user interface
• Event loops: process that browser uses to accomplish work on main thread, turning like a wheel with phases of tasks execution
• Long animation frames: an animation frame taking too long (beyond 16.6ms), impacting performance and user experience
• Core web vitals: upcoming official metrics for measuring web page performance, including LCP, FID, CLS, and Largest Contentful Paint (LCP)
• Long animation frames are considered too long if they exceed 100 milliseconds
• Responsiveness in the context of user interactions refers to how quickly a browser responds to user input, aiming for under 100 milliseconds
• Interactions are defined as discrete events such as taps, clicks, or key presses, not including continuous interactions like scrolling
• Core web vitals are health metrics for the web that measure loading performance, interaction responsiveness, and layout stability
• The core web vitals include:
	+ Largest contentful paint (LCP)
	+ Interaction to next paint (or first input delay)
	+ Cumulative layout shift (CLS)
• Correlation between web performance metrics (e.g., Largest Contentful Paint, First Paint) 
• Importance of field data in measuring user experience
• Confusion around Lighthouse scoring system and its limitations
• Need for considering multiple scenarios, devices, and factors when testing performance
• Changes to core metrics over time, including the introduction of Interactive and Cumulative Layout Shift (CLS)
• Value of consistency and gradual changes in web performance measurement
• Importance of hydration for performance and the need for measurable metrics
• Live experiments on Chrome traffic to measure impact of changes
• Small, subtle improvements that matter for developers, even if they only affect a small percentage of traffic
• Case of misleading content or poor app performance despite good overall numbers
• Balance between multiple metrics (e.g. largest contentful paint, cumulative layout shift) to prevent gaming the system
• Connection between core web vitals and SEO, with a business incentive for improving performance
• Intrinsic value of optimizing web performance beyond just its impact on search engine rankings
• Improving conversion rates through web performance
• Core Web Vitals as a baseline for measuring user experience
• Applying Core Web Vitals in different types of websites (e.g., e-commerce, games)
• Monitoring additional metrics for long-lived apps and customizing measurements
• Integrating Powersync with an application's stack for offline-first architecture
• Powersync allows for local-first web apps with instant reactive UX, syncing data in real-time
• Inp (Interaction to Next Paint) is a new core web vital measuring responsiveness of pages to user input
• A good inp score is 200 milliseconds or below, but threshold can be adjusted depending on device capabilities
• Inp measures the time between user interaction and the next page update or animation frame
• Interaction with long processing times (e.g. file uploads) should still show user feedback and keep main thread free
• Replacing First Input Delay (FID) metric with Interaction to Next Paint (INP)
• FID measures only the first interaction and is limited to the main thread
• INP captures a broader range of interactions, including those that occur after page load
• INP is not affected by animations or compositor usage if done correctly
• Common pitfalls for slow INP include slow event handlers and blocked main threads
• Potholes on a road (poor quality) can slow down an experience
• Huge DOMs and complex JavaScript queries can cause performance issues
• Too much JavaScript on a page can lead to slow loading times
• Prioritizing tasks is key, with critical tasks happening first
• Using the Performance Panel in Chrome Dev Tools for objective measures
• The Scheduler API allows developers to set priorities for tasks
• A polyfill for the Scheduler API is available for download
• Availability of full API for Chrome browsers
• Origin trial and availability of Yield API in 2024
• Scheduling and prioritization in frameworks like React
• Imps (Interactions per minute) on a page, including aggregate scoring and outlier removal
• Largest Contentful Paint (LCP) metric, including its user-centric design and implications for loading performance
• The importance of LCP (Largest Contentful Paint) in web performance and its role as one of three core web vitals metrics.
• Why prioritizing elements below the fold is necessary, even if they're not immediately visible.
• How analytics data can help identify common causes of LCP issues and inform optimization decisions.
• The concept of a "deep link" and how it affects the loading priority of a webpage.
• The role of URL strategy and query parameters in communicating with servers and optimizing performance.
• The need for a comprehensive approach to web performance, including hiring experts and making space for formal study within organizations.
• Cumulative Layout Shift (CLS) metric and its impact on page loading
• Unexpected shifts in content causing poor user experience
• Algorithm change to use windowing approach, cutting off at 5-second window
• Skeletal loaders (gray boxes) improving user experience by showing expected content shape
• Potential "gaming" of CLS metric through optimized page loading and skeleton design
• Importance of tracking core web vitals in daily development workflow
• Importance of web performance hygiene
• Using web.dev documentation for guidance on web vitals and optimization
• Chrome User Experience Report as a tool to monitor website performance
• Page Speed Insights and Search Console as additional tools for monitoring core web vitals
• Local testing and debugging using tools like Web Vitals extension
• Constant maintenance of web performance is necessary, with no single "magic bullet" solution
• Team effort required across the web ecosystem to improve performance
• Limitations of public data and importance of private, first-party data
• Core Web Vitals (LCP) and event timing API implementation in Chrome, Firefox, and other browsers
• Open web standards and collaboration among browser vendors
• Criticism of Google's influence on the web and potential bias in promoting its own interests
• Importance of community feedback and criticism in shaping web development decisions
• Importance of accountability and checks and balances in performance optimization
• Why web performance is crucial for all stakeholders in the ecosystem
• Benefits of faster websites, including increased conversions and user engagement
• Micro-level focus on providing best possible experiences for every user
• Measuring and sharing best practices to drive collective improvement
• Need for a community-driven approach to web performance optimization
• Fly.io partnership promotion
• Breakmaster Cylinder mystery referenced
• Sentry.io promotional code (changlog) and discount offer for team plan
• Announcement of return next week to "party" with them