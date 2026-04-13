• Discussing accessibility and its importance
• Introducing Tryggvi Gylfason, a frontend engineer at Spotify who works on web accessibility
• Topic for today's episode: Ten accessibility mistakes to avoid in 2021
• Specific discussion point 1: Avoid using too much animation, and using the "prefers-reduced-motion" media query to accommodate users with reduced motion preferences
• Resources mentioned:
	+ CSS Remedy GitHub repository
	+ Jen Simmons' snippet for turning off animations or making them shorter when user prefers reduced motion
• Failing to address transitions and animations for users with disabilities
• Not displaying related information at all stages of a process (e.g. checkout or form)
• Ignoring user experience principles, which often overlap with accessibility issues
• Designing forms that don't account for common UX pitfalls (e.g. system amnesia, autocomplete interactions)
• Failing to add input types properly on different devices (e.g. telephone, password)
• Not updating state correctly in web applications (e.g. Spotify's Play button example)
• Update ARIA labels when button states change
• Provide clear and descriptive text for multiple buttons (e.g. "Play Water Under the Bridge by Foo Fighters")
• Ensure color contrast between background and foreground colors is sufficient (at least AA compliant)
• Consider situational disabilities (temporary or situational impairments) in accessibility design
• Importance of semantic HTML and landmark regions for accessibility
• How screen readers use the Virtual DOM and hotkeys/quick keys to navigate web pages
• Benefits and importance of light mode vs dark mode in applications
• Trade-offs between customizing application settings (e.g. light mode) vs relying on operating system features
• Pitfalls of using display: none for visually hiding elements and its impact on accessibility
• Alternatives to display: none, such as setting visibility to none or using utility classes
• Using display: none to hide elements from screen readers
• Adding alt tags to images, especially those containing text
• Avoiding redundant ARIA attributes in HTML
• Using semantic HTML elements instead of adding roles (e.g. role=presentation)
• Choosing the right router library for single-page applications that works with screen readers
• Changes to the screen that are not announced to the screen reader
• Effective announcement of autocomplete search results and loading
• Focus and keyboard traps, including incorrect focus order and removal of visual feedback for keyboard navigation
• Managing complex UIs with CSS Grid and its impact on tab order
• Rescuing focus when elements are removed from the DOM or become inaccessible
• Live updates for visually-impaired and blind users
• Using aria-live regions to alert users of time-sensitive information
• Importance of being mindful of user experience when using assertive live notifications
• Common mistakes in accessibility, such as forms and repeatable information
• Dynamically updating tab index and focus management
• Temporary disabilities and the importance of universal accessibility
• Limitations of live updates on unmounted components