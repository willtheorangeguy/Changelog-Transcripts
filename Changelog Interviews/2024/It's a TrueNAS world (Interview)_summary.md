• Kris Moore's background and experience with iXsystems and TrueNAS
• Early days of ZFS and its integration with FreeBSD and PC-BSD
• ZFS file system features and benefits
• TrueNAS setup and configuration, including boot device redundancy and data backup
• Config backup options and automation with TrueCommand and the API
• Discussion of backup strategies and the importance of off-site backups
• Introduction to TrueNAS, including its history and development
• Explanation of the difference between TrueNAS Core and TrueNAS Scale
• Discussion of the evolution of TrueNAS from FreeNAS and iXsystems' involvement
• Explanation of the decision to unify the TrueNAS and FreeNAS brands and create TrueNAS Core and TrueNAS Scale
• Description of the features and benefits of TrueNAS Core and TrueNAS Scale
• Discussion of the future of TrueNAS Core and the focus on TrueNAS Scale
• Explanation of the reasons behind the move to Linux and the benefits of TrueNAS Scale
• TrueNAS is in a conservative "maintenance mode" with a focus on stability and rock-solid performance, rather than introducing new features.
• The core and scale editions of TrueNAS have different approaches to achieving stability, with core being more minimalist and scale being more feature-rich and user-friendly.
• FreeBSD is a complete Unix-like operating system, unlike Linux which is a kernel that can be combined with other components to form a distro.
• Kris Moore recommends starting with the Scale edition for new users, especially homelabbers, due to its more user-friendly UI and built-in replication features.
• TrueNAS provides a more straightforward and reliable way to manage backups and replication, compared to manually scripting solutions.
• The TrueNAS team aims to take care of the complex work of ensuring backups and replication work correctly, allowing users to focus on other aspects of their work.
• Alerting and data integrity for monitoring and backup
• TrueNAS' automated features vs manual CLI configuration with ZFS
• TrueNAS Scale's ability to run applications and manage Kubernetes
• Tailscale integration issues with TrueNAS Scale
• The importance of understanding what TrueNAS is doing under the hood and having access to the shell for debugging purposes
• Troubleshooting TrueNAS error messages and logs
• Understanding Kubernetes and TrueNAS deployment behavior
• Importance of checking container logs for deployment issues
• TrueNAS forums and community resources
• Setting up bonded interfaces and link aggregation in TrueNAS
• Potential issues with TrueNAS UI and configuration
• Reporting bugs and submitting debug files for troubleshooting
• Issues with network configuration and aggregation
• Limitations on multiple interfaces on the same subnet
• Troubleshooting and UI improvements for adding new link aggregates
• Evolution of TrueNAS UI from Django to Angular and improvements in recent years
• Consolidation of features and pages in the Scale UI
• Upcoming features in the fall release, including customizable dashboard widgets and GPU feedback
• TrueNAS UI development and feedback process
• Managing ZFS compatibility and future-proofing across different Linux versions and TrueNAS releases
• Intentional design of ZFS to prevent rolling back to older versions with lost features
• Ability to try before upgrading to a newer ZFS version in TrueNAS
• Pool interoperability and replication considerations when upgrading to a newer ZFS version
• TrueNAS upgrade process, including "try before you buy" feature and potential issues with older pool formats
• Replication and interoperability between Core and Scale systems
• Maintenance mode and keeping pools interoperable across different TrueNAS versions
• iXsystems business model and revenue streams
• Competition and market positioning of TrueNAS and iXsystems
• Enterprise features and support offered by iXsystems, including proactive support and appliance offerings
• Importance of uptime and stability in enterprise environments
• Benefits of TrueNAS' open-source model, including community feedback and collaboration
• TrueNAS Enterprise products and features, such as dual controllers and high-availability storage
• Target markets and use cases for TrueNAS, including media and entertainment, hospitals, universities, finance, and virtualization
• Advantage of unified platform and environment, including control over hardware and firmware
• In-house hardware design and development, including a dedicated R&D lab and prototype testing
• TrueNAS business model is based on hardware sales, with enterprise customers accounting for most revenue
• Hardware business supports development and maintenance of TrueNAS software, which is offered for free
• Enterprise customers receive priority support and have direct access to developers and engineers
• iXys has a large team of engineers and developers working on various aspects of the product, including software, hardware, and documentation
• The company's goal is to create a high-quality product that is both functional and enjoyable for users, with a focus on community involvement and user experience
• Kris Moore emphasizes the importance of a passionate and enthusiastic team, with engineers who are also enthusiasts of the product.
• Discussion of the author's experience with TrueNAS and his job as a partner
• Trade-offs between GUI and CLI management in TrueNAS
• Flexibility and customization options in TrueNAS, including scripting and open-source development
• Homelab market and hardware options for TrueNAS, including mini units and rack-mountable systems
• Possibility of iXsystems supporting custom-built TrueNAS systems for homelabbers
• Market demand for a middle ground between enterprise and DIY homelab hardware solutions
• Discussion of product viability and financial considerations
• Importance of trust in storage components and hardware configuration
• TrueNAS Scale product release cycle and upcoming features
• Dragonfish release (24.04) and its features, including ZFS ARC functionality, SMB performance enhancements, and auditing
• Upcoming beta and RC releases and the importance of testing and feedback
• The current issue with networking on the TrueNAS system
• Upgrading from train Bluefin to Cobia to resolve the issue
• ZFS stability and data integrity, with Kris Moore emphasizing the importance of stability
• New features in Cobia, including a redesigned app page, improved storage pool creation, and support for up to 1,200+ drives on a single system
• Dragonfish beta, with Kris Moore recommending it as an alternative to Cobia
• Upgrading process from Bluefin to Cobia, including recommendations for backing up the config file and understanding the upgrade process
• Changes to the Adaptive Replacement Cache (ARC) in the Dragonfish beta
• Discussion of the release schedule for Dragonfish, with Kris Moore stating that it will be available in April
• Kris Moore advising Adam Stacoviak to start with the Cobia release and then move to Dragonfish
• Plans for rolling back to a previous version if needed, as beta is considered too scary
• Discussion of the current beta testing phase, with around 1,500 people participating
• Kris Moore's experience working with TrueNAS and ZFS, and his appreciation for the community and culture surrounding it