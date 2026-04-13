• eBPF (Extended Berkeley Packet Filter) is a technology that allows running programs within the kernel of the operating system
• eBPF enables dynamic loading of programs into the kernel to change kernel behavior, observe kernel activity, and build security tooling and network functionality
• The technology has been evolving since the 1990s, but has only recently gained widespread interest due to advancements in recent kernel versions
• eBPF can be used for tasks such as dynamically mitigating kernel security vulnerabilities, such as the "Packet of Death" vulnerability
• The technology is powerful because it can be used by anyone, regardless of their Linux distribution, and does not require kernel upgrades or reboots
• Old kernel versions are still used in some environments due to stability and security concerns
• The principle of "cattle, not pets" suggests that servers should be easily replaceable and disposable
• Many organizations are still running legacy deployments and have not fully transitioned to modern cloud-native infrastructure
• eBPF (Extended Berkeley Packet Filter) is a feature that allows for kernel updates without downtime, but raises security concerns
• eBPF programs are checked by a verifier to ensure they are safe to run, but still require careful handling due to potential security risks
• Running eBPF programs and the power and responsibility that comes with it
• eBPF is a kernel feature that allows for low-level program execution, but most people interact with it through higher-level tools and projects
• Examples of tools and projects that use eBPF, including Cilium, Parca, and Pixie, for observability, performance tracing, and networking
• Performance implications of eBPF, including the potential for significant improvements in latency and the importance of writing efficient code
• eBPF Maps as a data structure for storing and retrieving data in the kernel, allowing for efficient collection and analysis of event data
• The trade-off between sampling and collecting all events, with sampling allowing for more efficient collection of data but potentially missing some events.
• eBPF performance benefits allow for more frequent or detailed monitoring without impacting system performance
• Security checks can be made in the kernel, allowing for more precise control over file system access
• Evolution of eBPF capabilities, including the Linux Security Module Interface and Tetragon, enable more powerful filtering and security checks
• Getting started with eBPF programming involves writing kernel and userspace code, typically in C or Rust
• Cross-platform issues, including kernel version and instruction set changes, can make eBPF tool distribution challenging
• Recent innovations, such as "compile once, run everywhere", have improved the ease of distributing eBPF-based tools
• Pain points include older kernel versions and specific instruction set limitations, such as the Max 4096 limit
• eBPF performance improvements, including more efficient hooks and better testing and code coverage tools
• The eBPF verifier as a challenge to work with, but with potential for future improvements
• Who is eBPF, with a personal story of Liz Rice's introduction to eBPF through the Cilium project
• The relationship between Cilium and Isovalent, including how Cilium is donated to the CNCF and Isovalent provides an enterprise distribution
• The benefits of open source infrastructure software, including collaboration and competition at the application layer
• The trend of infrastructure software moving into the kernel, with eBPF and other kernel-based offerings enabling more innovation and collaboration.
• eBPF (extended Berkeley Packet Filter) and its flexibility
• Comparison of eBPF to browser tech (JavaScript) and kernel tech
• eBPF applications: networking, security, profiling and observability
• Examples of eBPF usage: Cilium, Katran (Facebook/Meta), Cloudflare, Brendan Gregg's work (Netflix), Pixie, Parka, Hubble, Falco, Tracy, Tetragon
• Future of eBPF: implementation on Windows kernel, eBPF Summit (community conferences)
• eBPF Summit plans, including speaker lineup and session proposals
• Virtual event access from anywhere with an internet connection
• Past eBPF Summit events and activities, including interactive sessions and "capture the flag" challenges
• Liz Rice's excitement and enthusiasm for eBPF and its potential
• Future of eBPF and potential new developments and innovations
• Plans for Liz Rice to return as a guest in a year to discuss further developments and progress.