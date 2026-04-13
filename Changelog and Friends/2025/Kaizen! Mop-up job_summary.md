• Gerhard's life since the last on-stage Kaizen, including a new job at Loophole Labs
• Gerhard's new role at Loophole Labs, focusing on infrastructure primitives and live migration
• The challenge of migrating large amounts of data between physical hosts
• Gerhard's home lab upgrade, including a 100-gigabit network
• The integration of remote GPUs and low-latency networking
• The connection between Gerhard's personal and professional projects
• Time passing quickly and the sense of life moving fast
• Discussion of the Kaizen 21 podcast and its mopping segment
• Launch of Pipely and the audience's reaction
• Mention of a selfie taken during the stage event
• Discussion of the Changelog Podcast's marquee and the emo night event
• Explanation of the difference between Pipely and Pipedream
• Analysis of the fly.io metrics and the sudden spike in CPU utilization
• Discussion of a CDN issue with tiny instances
• Blue-green deployment strategy and its benefits
• Explanation of the blue-green deployment mechanism
• Underprovisioning of Fly VMs and its consequences
• Personal anecdote about a hike with Jerod and a near encounter with a rattlesnake
• Jerod's experience with drone footage and its use in Changelog News
• Analogies between close calls in life and shipping under-provisioned systems into production
• Close call with a rattlesnake while on a trip
• Importance of asking for what you want, illustrated by a tour of a kitchen at Fogo de Chão
• Discussion of a meal at Fogo de Chão, including a type of meat (picanha)
• Reflections on a recent trip to Denver and its memorable experiences
• Discussion of potentially doing another live show next year (2026)
• Planning a repeat of the ChangelogCon event
• Discussing possible locations, including Denver, Austin, and other options
• Considering factors such as accessibility, travel, and scheduling
• Brainstorming ideas for the event, including format, activities, and interviews
• Setting a goal to decide on a date and city by the next Kaizen episode
• Discussing specific details about Austin, such as the best time to visit and local knowledge
• Uploading MP3s was a problem that was fixed
• The team switched to a new CDN instance on October 5th
• The new CDN instance has improved cache hit ratio from 70.5% to 90%
• The team is considering whether to aim for even higher cache hit ratios
• The current cache hit ratio is 89.5%
• Feeds have a cache hit ratio of 99.5%
• Discussion of improving podcast feed caching to maintain a 99.5% hit ratio
• Analysis of homepage caching, which has improved from 18.8% to 98.5%
• Review of mp3 caching, which has improved from 86% to 87.5%
• Examination of news caching, which has improved from 52.6% to 83%
• Proposal to investigate and improve news and mp3 caching further
• Discussion of doubling memory to see if it improves cache hit ratios
• Brief digression about the movie Swordfish and its depiction of data hacking
• Improvements in Pipedream, including a four-time improvement in feed request response time
• Discussion of the P50, P75, P90, and P99 metrics for feed request response times
• Analysis of the homepage's response time, with a significant improvement for 50% of users
• Comparison of old and new response times using a video demonstrating the difference between 0.0003 seconds and 863 seconds
• Explanation of the rationale behind the video, which uses relative time scales to demonstrate the speed improvement
• Discussion of the Varnish Cache (now Vinyl Cache) and its role in serving requests
• Mention of the renaming of Varnish Cache to Vinyl Cache due to legal disputes
• Varnish Cache will be renamed to Vinyl Cache
• Gerhard Lazu's new 100-gigabit homelab setup
• Review and feedback on Gerhard Lazu's homelab video
• Pipedream benchmarking on Gerhard Lazu's 100-gigabit homelab
• NVIDIA Mellanox Connect X5 network cards and DAC cables used in the setup
• Cost and availability of the network cards and DAC cables
• Creating a virtual connection using two cables for a maximum theoretical speed of 128 gigabits
• Running a benchmark on a Pipedream application, achieving 22 gigabits per second and 225,000 requests per second
• Identifying the bottleneck as the CPU, not the network
• Testing the master feed, which is 13 megabytes in size, and observing high CPU usage
• Swapping the client and host, running Pipedream on the slower host and the client on the faster host, achieving 80 gigabits per second
• Discussing the limitations of the current host and the potential for upgrading the host to achieve higher speeds
• Examining the scalability of the setup and its potential for use as a CDN, noting that Fly.io may be throttling the bandwidth due to unexpected usage patterns
• Discussion of the transition from Varnish to Vinyl, and the upcoming changes to Pipely and Pipedream
• Gerhard Lazu's request for a "BAM" (Big-Ass Monitor) to visualize system traffic and metrics
• Issues with out-of-memory crashes and the need to investigate and prevent them
• Discussion of the current logging and metrics pipeline, and the potential to improve it with Clickhaus
• Exploration of using Clickhaus as a single event store, and its potential benefits for analytics and visualization
• Concerns about being tied to another "beast" of a platform with Clickhaus, and the need for careful evaluation
• Gerhard Lazu's experience with Clickhaus and its reliability at large scales
• Discussion of centralizing event storage and the potential to revamp analytics pipelines
• Jerod Santo's experience with Honeycomb and his desire to upgrade or improve analytics tools
• Discussion of R&D budget and improving existing systems
• Tracking and storing video files (mp4) in addition to audio files (mp3)
• YouTube's role in distribution and potential changes to its policies
• Options for decentralized video distribution and storage (e.g. Jellyfin, CDNs)
• Benefits of a one-to-one relationship between creator and viewer
• Open standards for video consumption and potential for a vibrant community of video viewers
• Video podcasts were initially supported by Apple in the early 2000s, but were not widely adopted due to bandwidth and technology limitations.
• Current video podcasting is limited by the need for multiple file formats and versions to accommodate different devices and platforms.
• The process of transcoding and storing multiple video file versions is complex and resource-intensive.
• Major platforms like YouTube and Vimeo have solved the video podcasting problem, but may not be the best fit for all creators.
• The use of AI and proprietary technologies may lead to a shift in how video podcasting is handled.
• A custom app or platform for video podcasting could provide more control and flexibility, but would require significant investment and development.
• The complexity of video podcasting is a major hurdle to widespread adoption.
• Upgrading Dagger and other utilities
• Improving deploy times and optimizing Fly.io
• Upgrading Postgres
• Replacing Overmind with Runit
• Discussing comments and engagement on YouTube videos
• Introducing Make.It.Work.Club, a community for interacting with Make.It.Work.TV
• Inviting Adam and Jerod to join Make.It.Work.Club
• Discussing various topics, including homelabs and Talos, in Make.It.Work.Club
• Discussion of a smart garage door setup and its features
• Setting up a non-networked garage door to be smart
• Exploring the technical aspects of connecting devices to the garage door
• Reviewing a blue UnderArmour hat given to Jerod Santo by Gerhard Lazu
• Mention of the concept of "Kaizen" (continuous improvement)