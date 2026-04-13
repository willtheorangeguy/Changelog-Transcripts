• History of SSL
• Let's Encrypt project
• Importance of encrypting the web
• Challenges of implementing HTTPS
• Let's Encrypt's impact on securing the web
• Certbot project
• Jacob Hoffman-Andrews' role with EFF and Let's Encrypt
• Cost of implementing HTTPS
• Mixed content and third-party content issues
• Cost of CPU usage for encryption
• Network cost or connection cost for HTTPS handshake
• Cost of purchasing a certificate from a certificate authority
• Human time cost of HTTPS and TLS configuration
• The challenges of implementing HTTPS at Twitter, including forgetting to renew certificates and consuming time from skilled engineers.
• The launch of Let's Encrypt in 2015 as a non-profit certificate authority to provide free HTTPS certificates, and its rapid growth to 30 million active certificates.
• The analysis of certificate data showing that over 90% of Let's Encrypt certificates are for newly encrypted sites.
• The process of setting up a certificate authority, including generating keys and certificates in a Hardware Security Module (HSM) and undergoing audits and cross-signing to gain trust.
• The potential for political and technical barriers to starting a new certificate authority, including the need for cross-signing and the potential for resistance from established vendors.
• Let's Encrypt's business model and differences from larger commercial CAs
• Domain validation vs. extended validation certificates
• Incentives for site owners to use extended validation certificates
• Limitations of extended validation certificates in automated and free certificate issuance
• User research on security indicators and usability of security features
• HTTP BAD initiative and marking HTTP as unsafe
• ACME protocol for automated certificate management and interoperability
• ACME protocol and its use in automated certificate issuance
• Boulder: server-side certificate authority software implementing ACME
• /wellknown: standardized path for protocol-specific files
• Certbot: client software for requesting certificates using ACME
• Challenge methods: HTTP, DNS, and TLS SNI
• OCSP: Online Certificate Status Protocol for checking certificate revocation
• Certbot features: automated certificate issuance, renewal, and installation
• Certbot limitations and outdated tutorials
• 90-day certificate renewal and its benefits
• Automation of certificate renewal with ACME protocol
• History of HTTPS adoption and the delay in widespread implementation
• Integration of Let's Encrypt with web servers such as NGINX and Apache
• Future of web security and the goal of making HTTPS a standard
• The US government's restrictions on cryptography in the 90s, known as the "First Crypto Wars", led to the classification of cryptography as a munition under ITAR regulations.
• This led to uncertainty and doubt in the software community about the legality of implementing crypto algorithms, and created a market impact.
• The Electronic Frontier Foundation (EFF) fought a court case (Daniel J. Bernstein vs. the US government) to challenge these restrictions and won the right to export strong cryptography.
• The current crypto wars are rumblings in the government to restrict cryptography and limit access to secure internet and secure transmissions of messages.
• The goal of encrypting the entire web is ambitious, with about 50% of sites currently using HTTPS.
• The EFF is working to encourage website owners to switch to HTTPS, and is tracking progress through metrics such as the percentage of pageloads happening over HTTPS.
• Let's Encrypt's role in increasing HTTPS adoption
• Let's Encrypt's funding model as an independent non-profit
• Benefits of HTTPS for users and website owners
• Certbot and ACME protocol for easy HTTPS implementation
• Certificate Transparency (CT) and its potential to prevent malicious certificate issuance
• Certificate transparency and its implementation
• Merkle trees and blockchain-like technology used in certificate logging
• Requirements for CAs to use CT logs, especially for Chrome EV certificates
• Let's Encrypt's adoption of CT logs and plans for future development
• Blockchain vs. Merkle tree technology used in CT logs
• Opportunities for developers to contribute to Let's Encrypt
• Importance of advocacy and user action in promoting HTTPS adoption