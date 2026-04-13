• Curl's 23rd anniversary
• Daniel Stenberg's role as maintainer and creator of Curl
• History of Curl and its development
• Changes in the internet and API needs since Curl's inception in 1998
• Daniel's initial use case for Curl (downloading currency rates for an IRC bot)
• Curl's evolution from a small tool to a widely used piece of software
• Daniel's current use of Curl (mostly for simple cases, not as a regular user)
• Daniel's transition from Mozilla to full-time work on Curl
• Daniel Stenberg works full-time for wolfSSL, selling commercial support for the open-source project Curl, which he created in the late 1990s.
• He discusses the challenges of transitioning from a hobby project to a full-time job, including the pressure to deliver and the need to balance work and personal life.
• Daniel mentions that he still spends nights and weekends working on Curl, but has a established routine that allows him to balance work and personal life.
• The conversation turns to Daniel's motivation for continuing to work on Curl, with him attributing it to the happiness of his users and the desire to keep the project working and powerful.
• Daniel discusses his change of heart regarding the programming language used for Curl, from C to considering Rust, citing the sharp edges and corners of C as a reason for this change.
• Daniel Stenberg discusses the future of Curl, an HTTP client library, and how it may coexist with other languages like Rust.
• Curl's C foundation is likely to remain, but it can be extended with libraries written in other languages, such as Rust.
• Hyper, a Rust library, is being integrated into Curl as an optional HTTP backend.
• Curl's wide availability and use in various platforms, including embedded systems and potentially even space, is noted.
• The conversation turns to the safety of C and the potential for replacing it with Rust or other thread-safe languages.
• Daniel Stenberg agrees with Josh Aas' concerns about C's safety but notes that Rust still has a way to go before it's a viable alternative.
• The state of new HTTP protocols, including QUIC, is discussed, with Daniel Stenberg highlighting his efforts to keep Curl up-to-date with the latest developments.
• HTTP/3 is a protocol built on top of QUIC, a TCP and TLS replacement, and is almost finalized
• The main goal of HTTP/3 is to improve performance and lower latency, especially for the big players and infrastructure providers
• However, the benefits may not be noticeable for individual users, but will trickle down to them through better performance from large services
• QUIC and HTTP/3 are part of a larger effort to improve network latency, especially with the advent of 5G and IoT devices
• The development of QUIC and HTTP/3 is just the beginning, and there will be further improvements and development in the future
• Curl's future with evolving network technologies, including HTTP/3 and 100ms latency
• Daniel Stenberg's views on supporting various network protocols and devices
• The experimental support of HTTP/3 in Curl
• The "Spotify and Instagram hacking ring" story, where a user mistakenly accused Daniel Stenberg of hacking their accounts
• The humorous exchange between Daniel Stenberg and the interviewers about the situation
• Problems with users who are frustrated and confused about Curl's usage in various projects
• Discussion of a specific user who emailed Daniel Stenberg, threatening and blaming him for a hacking incident that led to the loss of his business and personal life
• The challenges of dealing with threatening and confusing emails on the internet
• The fact that Curl is used in many projects and can be involved in shady activities, but that's not something Daniel Stenberg can control
• Handling security exploits and vulnerabilities, including the use of a bug bounty and rewarding security researchers
• Bug bounty program and handling security issues
• Using Open Collective for bug bounty funding and rewards
• Staying focused on a small community of users and stakeholders
• Estimating and tracking Curl usage and installations (10+ billion)
• Balancing individual user needs with the needs of a large user base
• Prioritizing and focusing on the needs of the current community
• The challenges of determining the "right direction" for a project and the difficulty of balancing the needs of power users and casual users.
• Daniel Stenberg's experience of using Curl only for simple tasks and not being aware of its more advanced features.
• The variety of user types, including those who only use Curl for simple tasks, those who ask for help in forums or Stack Overflow, and those who are involved in the development process.
• Daniel Stenberg's approach to managing the direction of the project, including learning from other open-source projects and seeking feedback from the community.
• The importance of listening to the community and seeking feedback through various channels, including the mailing list, Twitter, and experimental features.
• The use of experimental features to try out new ideas and gather feedback before making them permanent.
• Opt-in process for experimental features in Curl, such as HTTP/3 support
• Why opt-in is done at build time rather than runtime
• Balance between making features accessible and maintaining control over their development
• Importance of user feedback and surveying users for input
• Curl master's tips and tricks, including:
  • Using --libcurl to generate C code for Curl commands
  • --write-out option for extracting metadata from transfers
  • Importance of using Curl's command line options effectively
• Curl does not interpret or handle data, it only transfers it to the next command.
• Curl has options for outputting data to a file without redirecting or piping.
• The --remote-name-all option can automatically save files to the local file system.
• The --next option allows for chaining commands in a single Curl command, reusing connections and improving performance.
• Curl has options for handling cookies, including storing them in a file or using a cookie jar.
• Using the -next option in curl requires enabling cookies specifically
• The Everything Curl Book (everything.curl.dev) aims to provide a comprehensive resource for learning curl, including tutorials and examples
• The book is a living document that is constantly evolving and incomplete, but provides a thorough introduction to curl
• Daniel Stenberg has recently acquired the curl.se and curl.dev domains, with curl.se being his preferred choice
• There have been no major copyright or patent issues related to curl, although there was a lawsuit involving technology used by curl in the US that never went forward
• The Curl Inc company, which owns the curl.com domain, has not taken any action against curl, and it seems they have learned to coexist
• Daniel Stenberg has an Open Collective fund to handle security bugs and other issues, and has mentioned working with a law firm to handle potential issues.
• Discussion of Daniel Stenberg's work on Curl and its evolution from a hobby to a full-time project
• Changes between H/3 and H/2 versions of Curl
• Appreciation for Daniel's contributions to open source and his writing on the topic
• Encouragement for Daniel to continue writing and sharing his experiences and insights