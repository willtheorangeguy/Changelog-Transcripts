• Todd Gamblin's job role at Lawrence Livermore National Laboratory
• Overview of Lawrence Livermore's missions and responsibilities
• Todd's specific work on Spack, DevOps, and machine learning for parallel performance
• The lab's history with open source, including the development of Linux for HPC machines and popular open-source projects like ZFS and Slurm
• Collaboration across the DOE, universities, and other laboratories
• Slurm is used on Linux clusters at Lawrence Livermore Lab, including a 1.5 million core IBM Blue Gene machine
• ZFS file system is used in industry and has been ported by Lawrence Livermore Lab for use with Lustre parallel file system
• Spack package manager was open sourced by Todd Gamblin as part of his work at Lawrence Livermore Lab, but it's not the first project he open sourced
• CRAM tool splits jobs into smaller ones to manage large-scale computing tasks on the lab's clusters
• The lab has a policy document from 2004 requiring software developed under Advanced Simulation Computing Initiative to be open source unless there are reasons not to
• Todd Gamblin notes that while some projects may generate royalties, others like Spack are more suitable for open sourcing and sharing resources among computing sites
• The lab's IP organization reviews software releases, including a tedious process involving burning CDs and filling out paper forms
• Spack is a package manager for high-performance computing (HPC) environments, specifically designed to build and manage software on large machines.
• The project was created by Todd Gamblin at Lawrence Livermore National Laboratory to address specific challenges in the HPC software ecosystem, such as complex dependency management and reliance on vendor libraries.
• Spack is a "functional" package manager that builds software from source and assigns a unique hash to each dependency graph, allowing for reproducibility and versioning.
• The project's primary audience is not the general public but rather a smaller community of HPC researchers and developers who require high-performance computing capabilities.
• Contributing to Spack requires specialized knowledge of HPC environments and software development, limiting its contributor base.
• Growing the contributor base could involve expanding outreach to industry partners and other stakeholders in the HPC community.
• Structure of HPC communities with multiple roles (users, developers, center staff)
• Spack deployment model vs cloud-based models
• HPC centers' varying approaches to open source software and community building
• Influence of industry on government's open source practices and adoption of GitHub
• Challenges in implementing open source practices within government labs
• NumFOCUS affiliation for the Spack project
• Democratizing package management in HPC through Spack
• Cultural differences between cluster maintainers and casual users
• Spack's design choices (Python, Homebrew-based format) to make it easy for users to contribute
• Comparison with other HPC package managers (EasyBuild)
• Funding models for Spack (programmatic funding, grants from the Office of Science, LDRD)
• Challenges in navigating funding opportunities and the gap between research funding and production funding
• Importance of socializing projects to obtain programmatic funding
• Challenges with maintaining software projects due to lack of funding stability
• Importance of exit plans for research projects, including programmatic funding options
• Differences in how government organizations and private companies approach software maintenance costs
• Benefits and limitations of using grants versus programmatic funding for research projects
• Strategies for sustaining software products through community building and contributor engagement
• Impact of academic cycles on contribution rates to software projects
• Success stories, such as Exascale, where focus is placed on developing software rather than just writing papers or getting funding
• Development of software stack for large-scale scientific applications
• Coordinating releases of multiple applications within the stack
• Balance between open-source and proprietary components in the stack
• Involving industry contributors and expanding HPC adoption to smaller companies
• Addressing support needs for industry users and potential solutions (e.g. support contracts, small companies)
• Lessons learned from open-sourcing Spack and importance of thinking beyond one's own use case