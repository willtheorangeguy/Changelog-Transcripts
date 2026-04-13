• Trend of home network speeds increasing to 2.5 gig and beyond, with 10 gig being the next logical step
• Growing concern for power efficiency and cost of energy, leading to a shift away from high-power enterprise servers and towards low-power devices
• Adoption of Intel NUCs and similar low-power devices for homelab use
• Increase in storage capacity, with 14-20 terabyte drives becoming common
• Desire for solid state storage, but current prices for SSDs with the capacity of spinning drives are not yet viable
• Solid state drives (SSDs) are not as power-efficient as spinning drives, especially NVMe drives
• Storage is exploding in demand, with people wanting to keep large collections of data at home due to rising cloud costs
• CPUs with Quick Sync are becoming a viable option for transcoding and encoding videos, making GPUs less necessary
• People are opting for consumer-grade desktop CPUs with Quick Sync instead of Xeon processors and separate GPUs
• Efficient storage solutions, such as ZFS, are being used to store and manage large collections of data
• Discussion of over-choosing CPU for a project
• Definition and explanation of "homelab"
• Importance of homelab as a playground for experimentation and innovation
• Adam Stacoviak's personal experience with homelabbing and how it helped him develop skills and confidence
• Application of homelab skills to work projects
• Using homelab as a sandbox for testing and learning new technologies
• The importance of home labs for learning and experimentation
• How home labs provide a safe introduction to Linux
• The role of networks in home labs, including wireless and network performance
• How a desire to improve network performance can be a gateway to homelabbing
• The use of Raspberry Pi and virtual machines as alternatives to physical hardware
• The challenges and considerations for setting up a home lab, including network setup and management
• The benefits of homelabbing, including learning, experimentation, and cost-effectiveness
• The use of tools like Plex and uptime monitoring software to facilitate homelabbing
• The conversation starts with the hosts discussing how curiosity and watching YouTube tutorials can lead to upgrading home networks.
• The hosts mention their favorite YouTubers, including Chris and Tom Lawrence, for their knowledge and expertise in networking.
• Adam Stacoviak discusses his preference for UniFi, but acknowledges that others may prefer different brands, including Jeff Geerling who is against UniFi.
• The hosts discuss the trade-offs of using UniFi, including its proprietary OS and cost, vs. using open-source options like pfSense.
• Techno Tim shares his personal experience with networking, including his preference for a single pane of glass and his use of pfSense for an open-source network firewall.
• Comparison of OpenSense and pfSense as open-source alternatives to Ubiquiti's UDM Pro
• Discussion of the pros and cons of using Ubiquiti's UniFi switches in a home network
• Advantages of using a separate firewall and switch, such as avoiding single-pane-of-glass solutions
• Potential drawbacks of using Ubiquiti's network controller, including double administration and limited visibility
• Comparison of RAID configurations and their impact on performance
• Personal experiences with Ubiquiti's RMA process and customer support
• Discussion of home network setup and camera installation
• Discussion of homelabbing and the importance of network speed
• Comparison of SSDs, NVMe, and hard drives for storage
• Challenges of saturating 10-gigabit network speeds with storage
• Use of ZFS and caching for optimal performance
• Debate over whether to upgrade to faster storage options or optimize existing hardware
• Mirrored pairs vs RAID Z2 for homelab storage
• Probability of drive failure and business continuity
• Performance benefits of mirrored pairs
• Ease of expansion with mirrored pairs vs RAID Z2
• Trade-offs between mirrored pairs and RAID Z2 (cost, complexity, etc.)
• Expansion features and limitations of RAID Z2
• Homelab setup using ZFS and TrueNAS
• Comparison of ZFS with other file systems (Btrfs, unRAID, Synology)
• Discussion of RAID configurations and access patterns
• Techno Tim's personal experience with ZFS, including its benefits (snapshots, integrity checks, scrubbing)
• Mention of Proxmox using ZFS and its influence on Techno Tim's choice of file system
• Discussion of RAM usage and storage in file systems, with the goal of minimizing disk access.
• Backup strategies and methods, including the use of ZFS and ZFS send/receive
• Continuity of data and the importance of backups
• Options for object storage, including B2, R2, and S3
• Business continuity and disaster recovery
• Homelab connectivity and accessing homelab resources externally
• Self-hosting and self-cloud concepts
• Reverse proxy and port forwarding techniques using Cloudflare and Traefik
• Use of Let's Encrypt for automatic certificate generation
• Setting up public-facing services in a VLAN with a load balancer and Let's Encrypt certificates
• Discussion of Tailscale as a solution for secure tunnels
• Techno Tim's self-hosted homelab setup and colocation project
• Home automation and IoT devices, including use of Home Assistant and HomeKit
• Managing and automating various smart devices and systems
• Discussion of privacy and data collection concerns
• Home automation setup using UniFi cameras and Home Assistant
• Running Home Assistant in a Kubernetes cluster within a Proxmox virtual machine
• Debate on whether to use Kubernetes for homelab management
• Kubernetes limitations and caveats for homelab use
• Discussion on the need for highly available services in homelab, but not necessarily fault-tolerant ones
• Caution against migrating all services to Kubernetes, but instead using it as a testing ground for specific use cases.
• Kubernetes is a valuable skill to learn, even if it's not directly related to work.
• Docker containers can be run on a single host, scaling vertically until resource constraints are reached.
• Divide containers into different hosts based on network requirements, such as public-facing workloads.
• Consolidating containers onto a single host reduces points of failure and administrative overhead.
• Use separate hosts for workloads that require external storage or specific hardware, such as video cards.
• TrueNAS is mentioned as a platform for hosting Plex and other workloads, with benefits including reduced latency and points of failure.
• The speaker's home lab setup includes multiple servers, including an HL15 and an AV15, both from 45Drives.
• OCuLink and its potential for expanding PCIe lanes
• Local AI processing and its computational requirements
• CPU limitations, specifically the 20-lane limit on Intel processors
• Motherboard design and the trade-off between slots and lanes
• Homelab trends, including downsizing and the use of small form factor systems
• Storage, particularly the high cost of large SSDs (4TB+)
• Techno Tim and Adam Stacoviak discuss the challenges of buying computer parts in odd quantities, such as one of a particular item.
• Techno Tim explains his habit of buying computer components in pairs or multiples due to homelab requirements.
• The conversation touches on the importance of homelab and the joy of discussing it with others.
• Adam Stacoviak thanks Techno Tim for participating and for the opportunity to geek out over homelab topics.
• Techno Tim expresses his appreciation for being able to share his knowledge with others and for the chance to connect with like-minded individuals.
• The hosts bid farewell to their audience.