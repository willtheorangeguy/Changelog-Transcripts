• Daniel Stenberg was awarded a gold medal from the Swedish king in 2017 for his contributions to curl
• Stenberg celebrated his 20-year anniversary with curl, reflecting on the project's impact on his life
• He discussed the benefits of maintaining open source, including a fulfilling career and friendships worldwide
• Stenberg addressed the question of retirement and passing on the torch, stating that he has thought about it but doesn't plan to step down soon
• The project's ownership structure was discussed, with Stenberg owning most copyrights but not all
• The conversation touched on the challenges of passing on a project, particularly one that is deeply personal and has been a significant part of Stenberg's life.
• Challenges of delegating responsibilities to others in the project
• Difficulty in attracting contributors due to the complexity and depth of the project
• The impact of curl on a large scale, including its influence on billions of devices
• Strategies for making the project more appealing and fun for contributors, including celebrations and community events
• Challenges in communicating changes and new features to users, and the need to highlight and showcase them
• Ideas for creating resources and documentation, such as a cookbook or pamphlet, to help users discover and utilize the full potential of curl
• Development of the "Everything Curl" book
• Description of the book's purpose and scope
• Ongoing updates to the book due to curl's changing nature
• Discussion of alternative documentation formats for curl
• Feature of "Copy as curl" in various browser dev tools
• UI improvements to curl, including bold headers
• Explanation of the complexity of implementing bold headers
• Mention of the book's length and format (250 pages, online publication)
• Progress on TLS 1.3 and QUIC
• HTTP/2 adoption and usage statistics
• Challenges in updating TCP protocol
• Development of QUIC as a new transport protocol
• Comparison of TCP and UDP protocols
• QUIC's evolution from Google's experimental protocol to a standardized transport protocol
• The current state of the QUIC protocol, which is still being developed and is expected to be finalized by November 2018.
• The transition of QUIC from a transport protocol to a new HTTP version, "HTTP over QUIC".
• The challenges of changing the TCP protocol, including the need to ensure compatibility with middleboxes and routers.
• The use of encryption to solve the problem of ossification, where middleboxes block changes to the protocol.
• The limitations of TCP in handling packet loss, which can lead to slower performance in lossy networks.
• The advantages of QUIC in handling packet loss, which allows for continued transmission of streams even if some packets are lost.
• The use of UDP as a transport protocol for QUIC, which provides a way to bypass the ossification of TCP.
• QUIC's mission is to reduce roundtrips and work transparently with HTTP/2, while being secure by default.
• QUIC is designed to be encrypted by default, with no unencrypted version.
• There are plans for future versions of QUIC to support additional features, such as DNS and Multipath TCP.
• The current adoption rate of QUIC is around 7%, primarily among Google Chrome and Google services.
• Google's QUIC implementation is separate from the IETF version, which is being implemented by other players.
• The IETF version of QUIC is still a draft, with a target formalization date in November 2018.
• Implementing QUIC support in curl is expected to start soon, possibly in a month or so.
• The "post-TCP world" refers to the idea of transitioning to protocols that don't rely on TCP, with QUIC being a key part of this vision.
• Challenges of moving away from TCP in QUIC
• HTTP/2 and QUIC coexistence and bootstrapping
• Post-TCP world implications and the ossification problem
• QUIC's benefits in allowing protocol development and innovation
• Importance of patience and timing in adopting new technologies like QUIC
• Advice for developers to get familiar with QUIC for low-latency applications
• Daniel Stenberg's general advice on open source and software development: find what's fun, be patient