• Let's Encrypt has issued over 1 billion certificates since its inception in 2013, with over 200 million sites now using its service.
• The organization's goal is to make it easy for people to obtain SSL certificates, making the internet more secure by default.
• However, this has led to a "catch-22" situation where people take Let's Encrypt for granted, but the organization still needs to fund its operations through donations and support.
• Let's Encrypt uses a variety of methods to communicate its mission and needs to the public, including social media, blogging, and outreach to companies and open-source projects.
• The organization has had to mitigate some issues with its software, including stability and compliance problems, but has a good track record for security and reliability.
• When issues do arise, Let's Encrypt prioritizes transparency and quick fixes, often resolving problems within a few hours and providing detailed public reports.
• Let's Encrypt's goal is to simplify the process of obtaining HTTPS certificates, making it free and easy to use.
• The biggest obstacle to widespread HTTPS adoption is the complexity and cost of obtaining certificates.
• Let's Encrypt uses an API and client software to automate the process, eliminating the need for manual configuration and payment.
• The protocol used by Let's Encrypt is called ACME, which has been standardized by the IETF.
• The Let's Encrypt community has developed hundreds of client software packages that work with the ACME protocol.
• The EFF's Certbot client was instrumental in making Let's Encrypt accessible to a wide range of users.
• The founders of Let's Encrypt, including Josh Aas, were motivated by the frustration of trying to get websites to use HTTPS due to the complexity of obtaining certificates.
• Discussion around requiring HTTPS for the H2 protocol
• Criticism that requiring TLS would make H2 deployment difficult and expensive for some
• Idea of creating a new, publicly-beneficial certificate authority to address the cost issue
• Creation and launch of a new certificate authority
• Progress made in encryption rates over 5 years, with a focus on accessibility and participation on the web
• Overview of the process of building and running a certificate authority, including getting authorization and trust from major browser makers
• Details on the Baseline Requirements document and CA/Browser Forum
• Discussion of the importance of browser trust and root programs in certifying a CA.
• The process of getting a root of trust from CA (Certificate Authority) root programs can take 3 months to 3 years to get accepted
• Once accepted, it can take another 3-7 years for all devices to trust the CA, due to varying update cycles and compatibility issues
• The cost of getting a CA up and running can be millions of dollars and requires a 6-10 year commitment to compliance and auditing
• There is a shortcut method, used by Let's Encrypt, called cross-signing, which involves partnering with an existing trusted CA to temporarily gain trust
• Let's Encrypt is transitioning from cross-signing to its own root of trust, which will be widely trusted but may not be compatible with older devices
• The cost of running a CA is primarily personnel costs, with other expenses including startup costs, hardware, and data storage
• Let's Encrypt is a publicly-trusted CA that operates independently of cloud providers
• The organization has its own hardware in secure, special rooms in data centers
• Let's Encrypt offers a basic option for certificate issuance, with limited customization and human support
• The organization prioritizes efficiency and best practices over offering a wide range of certificate options
• Other CAs exist to offer specialized services and features that Let's Encrypt does not provide
• The process of becoming a trusted CA is complex and time-consuming, requiring significant investment and resources
• Most people do not start a CA from scratch, but instead acquire an existing CA or participate in cross-signing
• Extended validation certificates and other specialized certificate types have limited practical value and are not widely used.
• Discussion of Extended Validation (EV) certificates and their perceived value
• Critique of EV certificates as being redundant and not useful for security
• Issues with EV certificate validation and the potential for arbitrariness
• Impact of browser vendors removing EV certificates from UI
• Let's Encrypt's success in promoting HTTPS adoption and its role in changing the web's security landscape
• Discussion of whether Let's Encrypt is pushing for HTTPS adoption or riding a wave of existing demand
• Importance of encrypting all traffic, not just sensitive information
• Risks of unencrypted traffic, including modification and exploitation
• Celebration of a billion HTTPS certificates issued in a short time
• Transition to HTTPS as a standard, facilitated by Let's Encrypt and community efforts
• Comparison to other internet technologies, such as IPv6, and their transition times
• Discussion of "cog mentality" and the importance of individual contributions to a larger system
• Recognition of various organizations and individuals who have supported Let's Encrypt's efforts
• Let's Encrypt's mission and goals
• Platinum sponsors and financial supporters
• Efficiency and budget management
• Automating processes and reducing data storage
• Global HTTPS adoption trends and remaining challenges
• Continuing to issue certificates and maintain trust
• Long-term plans and future goals for Let's Encrypt
• Upcoming challenges in internet security, including potential BGP protocol exploits and massive outages
• Need for improved BGP security, requiring collaboration from major internet companies
• Concerns about memory safety and the risks of using languages like C and C++ in software development
• Goal of removing code written in memory-unsafe languages from critical infrastructure
• Importance of rewriting existing software in safer languages like Rust
• Ambition needed to tackle large-scale security challenges in software development
• Cross-signature concept and its importance
• Encouraging developers to prioritize long-term security considerations
• Importance of secure software in the long-term
• Praise for Let's Encrypt and its mission