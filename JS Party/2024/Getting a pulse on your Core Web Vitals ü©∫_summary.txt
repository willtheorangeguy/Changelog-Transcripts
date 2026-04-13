• Introduction and welcome
• Guests' backgrounds: Annie Sullivan (tech lead for Core Web Vitals) and Rick Viscomi (developer relations engineer working on web performance)
• Discussion of Core Web Vitals, INP (Interaction to Next Paint), and long animation frames
• The role of the guests in helping developers improve website performance and making a case for removing unnecessary JavaScript
• Metaphor comparing the guests' work to agents trying to curb an addiction to JavaScript
• Main thread: the central location where code runs in JavaScript, affecting user interface responsiveness
• Event loops: the process that manages tasks on the main thread, ensuring timely execution and visual updates
• Long animation frames: animation frames that take longer than expected (e.g., 100 milliseconds) to render
• Responsiveness: the time it takes for the browser to respond to user input (ideally under 200 milliseconds)
• Interactions: discrete user actions like taps, clicks, or key presses, not continuous interactions like scrolling
• Definition of Core Web Vitals as health metrics for web performance
• Importance of measuring user experience in real-world scenarios vs. lab testing
• Evolution of web performance measurement from onload event to field data and percentiles
• Role of Lighthouse and other tools in measuring performance and providing actionable feedback
• Confusion around Lighthouse score and its limitations in identifying performance issues
• Changes to Core Web Vitals over time, including the introduction of Interaction to Next Paint (INP) and the deprecation of First Input Delay (FID)
• Importance of keeping metrics consistent and stable to help developers focus on important issues
• Impact of small changes in metrics on website performance
• Counterintuitive cases where metrics look good but user experience is poor
• Gameable aspects of metrics and the importance of focusing on individual site performance rather than comparison to others
• Business value of optimizing web performance, including improved conversion rates and revenue
• Alignment between Chrome and search recommendations for user experience metrics
• Core Web Vitals are designed for web content, but may not be suitable for long-lived apps with complex interactions
• Interaction to Next Paint (INP) is a new metric that measures responsiveness and user experience
• INP looks at all interactions throughout the page lifetime and takes the slowest one into account, with built-in tolerances for applications with many interactions
• A good score for INP is 200 milliseconds or less, but this threshold can be adjusted based on specific use cases
• INP measures how quickly a page handles user input, with an emphasis on providing feedback to users in under 100 milliseconds
• The metric is independent of the actual action being performed and focuses on providing immediate response and user feedback
• INP is intended to replace First Input Delay (FID) as it provides more comprehensive information about user experience and interactivity.
• Introduction of Core Web Vitals and improvements made to desktop performance
• Explanation of INP (Interaction to Next Paint) metric and its differences from FID
• Discussion on common pitfalls for INP, including slow interactions, DOM size, and excessive JavaScript
• Importance of prioritizing critical tasks on the main thread
• Use of Chrome DevTools tracing to objectively measure page performance
• The Scheduler API and its use for declarative scheduling
• Polyfills and wrappers for the Scheduler API, such as the Chrome Labs polyfill
• Scheduling APIs in popular frameworks like React
• User-centric performance metrics like Largest Contentful Paint (LCP) and how it measures content load times
• Edge cases and corner cases in LCP measurement, including user interactions and lazy-loading of images
• Core Web Vitals metrics and their importance in measuring web performance
• LCP ( Largest Contentful Paint) metric and its relationship to above-the-fold content
• Prioritizing images below the fold based on analytics data and deep linking scenarios
• Cumulative Layout Shift (CLS) metric, including its definition and algorithm
• CLS scoring and windowing mechanism for measuring page layout shifts
• Strategies for mitigating CLS issues through animations and loading techniques
• Benefits of skeleton pages for user experience and performance
• Psychology behind skeleton pages (providing a loading state that users can expect)
• Importance of web vitals metrics (Core Web Vitals) for measuring website performance
• Tooling and measurement options for tracking Core Web Vitals (e.g. Chrome User Experience Report, PageSpeed Insights, Search Console)
• Best practices for incorporating performance testing into daily workflows (local testing, A/B testing, etc.)
• The role of documentation in web performance space (web.dev as a resource)
• Discussion on measuring web page performance using Chrome's LCP (Largest Contentful Paint) metric
• Limitations of public data in providing detailed insights into specific webpage performance
• Importance of first-party tools and private data for in-depth analysis
• Comparison of Chrome's Web Vitals with other browsers, including Firefox and WebKit
• Criticism of Google's influence on web standards and performance metrics
• Response from Google representatives on criticism, emphasizing the importance of community input and criticism
• Discussion on why web performance is important for users and businesses
• Role of stakeholders in promoting web performance best practices
• The importance of performance and accessibility in web development
• Measuring user experiences to improve website speed and performance
• Sharing best practices and case studies for optimizing website performance
• The need for a collective community effort to improve website performance
• Contact information for speakers Annie Sullivan (@anniesulli) and Rick Viscomi (@Rick\_viscomi)