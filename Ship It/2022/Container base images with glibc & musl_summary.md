• Bazel build system limitations for distroless project
• Development of Wolfi distribution as alternative to distroless
• Needs of the distroless community (minimal container images)
• Comparison between Alpine's package manager "apk" and Chainguard's tool "apko"
• Use cases for apko (cataloging dependencies, generating SBOMs)
• Melange: a system for building packages using YAML, allowing for structured data and pipeline-oriented approach
• Comparison to APK builds: clean, self-contained, and easy to understand
• Introduction of Ko (formerly developed by Google): generates statically-linked Go application images on top of Chainguard static image
• Relationship between Wolfi OS and Chainguard Images: Chainguard Images are built using apko and are a community-driven project with customer-specific use cases
• Open source nature of Chainguard Images project, accepting contributions from the public
• Use of Wolfi OS inside the Chainguard Images ecosystem for glibc-based images, as a replacement for Alpine for musl-based images in some scenarios
• glibc vs musl: differences in implementation and compatibility
• anecdotal observations from RabbitMQ that glibc is more predictable for memory management
• Ariadne Conill's explanation of musl's conservative approach to undefined behavior
• Wolfi OS allowing users to choose between glibc and musl based on their needs
• discussion of DNS issues with musl, including limitations in handling large responses
• Chainguard sponsoring work on improving musl's TCP support for DNS
• Ariadne Conill's involvement as a contributor to the musl development team
• The Wolfi core OS has a modular design, allowing for different components to be used or not used based on user preferences
• This approach is beneficial in the embedded world, where different customers may have varying needs
• Ariadne Conill discusses Rust, saying it has pros and cons, but is particularly useful for model-driven development and proving correctness
• She criticizes parts of the Rust community for being unhelpful and promoting unnecessary rewriting of code
• Conill believes that standardization in the Rust ecosystem would be beneficial for adoption, but is currently lacking
• The conversation also touches on the potential use of Rust in the Linux kernel and its benefits for model-driven development
• Conill mentions her previous work on Witchery, a project that used Rust for some functionality before being rewritten in Go
• Witchery was abandoned due to customer concerns over Docker dependency
• Melange is a build tool that allows for package building without Docker
• Chainguard and Wolfi are working on a full Kubernetes distribution
• A bug in the repository management service caused security updates not to be published
• Continuous vulnerability scanning is done using tools like Trivy, Grype, and Snyk
• The workflow involves building, scanning, and publishing images with a "generate readme" step for documentation
• The build tool Apko is used to publish images in the same step as building
• Targeting x86 (64-bit only) and ARM architectures for Wolfi
• Current goals focus on a smaller set of supported architectures, representing 99% of container usage
• No plans to support 32-bit x86 architecture
• Discussion of KubeCon attendance cancelled due to COVID concerns and personal moving situation
• Ariadne Conill's reasons for moving to Seattle instead of Europe, citing the war in Ukraine and desiring a US location with a more European mindset
• Plans for future Wolfi developments, including ARM support and additional container images