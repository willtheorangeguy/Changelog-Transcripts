• Nabeel Sulieman built KCert, an open-source certificate manager for Kubernetes
• He created KCert as a solution to issues with cert-manager and NGINX in his cluster
• The problems he faced included DNS issues causing cert-manager to fail, leading him to manually create certificates using certbot
• After documenting the manual process on GitHub, he transitioned to building KCert from scratch in .NET Core
• He wanted to automate the certificate management process after experiencing the pain of doing it manually
• KCert is designed to simplify and streamline certificate issuance for Kubernetes clusters
• KCert is a tool for managing certificates in Kubernetes clusters
• It was created as a side project and has since been open-sourced
• KCert works by creating temporary ingresses to route ACME challenges
• It automates certificate renewal and can avoid issues with DNS propagation
• KCert does not solve the problem of decoupling compute from control, but rather suggests having an external secret store like a vault as a better solution
• The conversation also touches on decoupling compute from control and storing secrets in an external source of truth
• Certificates from Let's Encrypt can't be directly managed by Fastly due to DNS verification limitations
• Managing certificates through cert-manager is more flexible but requires manual upload to Fastly
• Using KCert for issuing certificates has limitations, including HTTP validation only and no support for wildcard certificates
• Proposed solution involves decoupling certificate management into three steps: issuance, syncing with source of truth, and deployment to other places
• Feature request was suggested to add external storage interface to KCert (now proposed as AnyCert) to support storing certificates in various vaults or platforms.
• Nabeel Sulieman is working on an experimental reverse proxy project called KCert
• Gerhard Lazu expresses interest in exploring KCert and collaborating with Nabeel
• Nabeel shares that KCert is still in development and he's hesitant to share it publicly
• Discussion around the trade-offs of keeping projects private vs. sharing them with a community
• Nabeel mentions his experience with another open-source project, which also keeps its scope narrow
• Gerhard asks about the potential for KCert to be used in production by others besides Nabeel
• KCert limitations: not designed for multiple instances, certificate management
• Comparison with Caddy and Traefik: combining reverse proxy and certificate management
• Interface contract between router and certificate manager (KCert)
• Need for clear interface or protocol between components
• Erlang ecosystem's capabilities in serving traffic without NGINX Ingress Controller
• Alternative to NGINX Ingress Controller using a load balancer with the Erlang application
• YARP library usage and scalability
• Private experiment's performance and scalability concerns
• KCert's usage and future development
• Separating KCert from the router for easier maintenance
• Building a reverse proxy tool to replace NGINX Controller
• Open sourcing vs private development and potential challenges
• The importance of feedback and community involvement in open source projects
• Lessons learned from Nabeel's experience with open sourcing: taking time, keeping scope narrow, and being prepared for maintenance