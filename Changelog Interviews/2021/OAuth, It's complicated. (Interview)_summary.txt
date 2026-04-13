• Aaron Parecki's long-term tracking of his location and activities, starting in 2008
• His use of logbooks and notebooks to track his daily activities as a child, before GPS
• His current use of Foursquare and other location-tracking apps
• His fascination with data collection and personal data tracking
• His struggles with tracking certain types of data, such as mood, due to inconsistencies and self-awareness bias
• His approach to tracking his location, aiming for passive collection and avoiding self-awareness bias
• Normalizing and organizing GPS tracking data
• Using a custom database and storage format for location data
• Integration with IndieWeb principles and practices
• Demonstrating the potential of self-tracking and publicizing location data
• The concept of IndieWeb and its community
• Accessibility and onboarding for those interested in IndieWeb
• Implementations and resources for IndieWeb enthusiasts
• IndieWeb community aims to have people control their own online presence through their own website.
• Various levels of involvement and customization are possible, from a simple one-page site to a full log of online and offline activities.
• Importance of owning one's own domain and publishing content on one's own website.
• Using social networks for their intended purposes and promoting one's own content on those platforms.
• OAuth 2 and its evolution, including the introduction of extensions like PKCE.
• The natural, slow evolution of the space, with documentation and security features being added over time.
• OAuth 2.1 is a simplification and distillation of the best practices from OAuth 2.0
• OAuth 2.1 aims to consolidate and standardize the various specifications and flows of OAuth 2.0
• The main flow in OAuth 2.1 is the authorization code flow with PKCE (Proof Key for Code Exchange)
• PKCE is a security feature that should be used in all OAuth flows to prevent attacks
• The authorization code flow is the most secure and recommended flow for most use cases
• The client credentials flow is used for service accounts and administrative tasks
• The device flow is used for devices that don't have a browser or keyboard, such as smart TVs or streaming devices
• OAuth 2.1 aims to simplify and standardize the OAuth ecosystem, making it easier for developers to implement and use
• OAuth limitations for devices without browsers
• OAuth device flow
• Transactional authorization (GNAP) as a new protocol
• GNAP's focus on individual instance authentication
• OAuth 2.1's goal of cleaning up existing issues
• Challenges of working within the OAuth framework's assumptions
• OAuth is not impossible to secure, but it's not the easy way and is harder to describe.
• GNAP is starting over and has potential to be a better fit for future developments, but OAuth 2.1 is still important for stabilizing the current system.
• OAuth 2.1 aims to simplify the definition of OAuth and provide a more incremental approach to updates, rather than a complete overhaul.
• The implicit flow is considered insecure and should be replaced with a more secure flow, such as the authorization code flow.
• PKCE is a recommended addition to OAuth applications to prevent phishing attacks, but is not a breaking change and can be added incrementally.
• The legacy of OAuth and the need for backward compatibility can make it difficult to make changes to the system.
• OAuth front channel and back channel concepts
• Problems with implicit flow: insecure access token delivery
• Limitations of implicit flow: lack of trust in front channel
• Alternative solution: authorization code flow with PKCE
• Authorization code flow: secure delivery of access token in back channel
• PKCE (Proof Key for Code Exchange) solves the problem of not knowing who is requesting an authorization code in an OAuth flow
• PKCE uses a hash mechanism to verify the requester is the same as the one who receives the authorization code
• The hash is created and sent in the front channel, and verified in the back channel when the authorization code is exchanged
• PKCE is not a replacement for client authentication, but a way to ensure the requester is the same as the one who receives the code
• PKCE is typically transparent to the user, and is only used internally by the app or service to authenticate the request.
• The importance of making authentication easy and seamless for users
• Explanation of the PKCE protocol and its benefits
• Resources for learning OAuth 2, including a book and video course
• Upcoming Okta Developer Day event, including hands-on labs and talks
• Aaron Parecki's OAuth Happy Hour YouTube show
• OAuth specification and its complexities, and the efforts to simplify it