• The polyfill.io CDN rug pull incident, where a malicious actor hijacked a popular JavaScript package's CDN
• Hot-linking vs. using a CDN: how the former is not recommended due to potential security risks
• Third-party JavaScript security risks, including dynamic changes and lack of control over client-side code
• The polyfill package and its purpose in allowing newer code to work on older browsers
• A Chinese company's takeover of polyfill.io and subsequent malicious activities, including redirecting users to adult content websites and online casinos
• Security concerns around third-party scripts and the potential for more severe attacks if not properly secured
• Third-party scripts can act dynamically despite appearing static
• Polyfill attack: exploiting domain name ownership change for malicious purposes
• CDN hijacking: replacing files without owning the domain
• DNS hijacking attacks: manipulating DNS to point to controlled locations
• Over 300,000 websites still using compromised domains
• Multiple ways to hijack scripts and IP addresses (layer 3-7)
• SSL encryption does not guarantee safety from script hijacking
• Many engineers unaware of layer 3-7 protocols and vulnerabilities
• Third-party script vulnerabilities: Plausible.io, Drift, Facebook, Cloudflare Analytics
• Assessing risk when adding third-party scripts to a website
• Differentiating between reputable tech-focused companies and "script" businesses
• Self-hosting scripts versus relying on third-party vendors
• Verifying script safety instead of blindly trusting it
• Using content security policies (CSP) and other browser features to improve security
• Limitations of browser-based security measures for dynamic scripts
• Alternatives to third-party scripts such as using npm versions or self-hosting
• Importance of checking compliance of third-party scripts added to websites
• Tension between leadership and engineering teams regarding the use of third-party scripts
• Cookie banners and their limitations in addressing privacy issues
• Use of tools like Google Tag Manager and tag managers for managing third-party scripts
• Need for real-time alerting and monitoring to detect new scripts being loaded on a website
• Discussion of how c/side's product detects and blocks malicious third-party scripts
• Explanation of why frequent alerts for minor changes in script code can be "noisy" and ineffective
• Overview of c/side's approach to detection, including the use of abstract syntax trees and other techniques
• Description of how c/side's free tier contributes to improving the product for all users, even those who do not pay
• Discussion of third-party scripts on c/side's website, including proxying through c/side's servers
• Explanation of c/side's solution to handling third-party scripts, involving proxying and rewriting scripts on their servers
• Client-side monitoring for detecting certain types of attacks
• Need for browser companies to improve their specifications and features to alleviate security issues
• Importance of phasing out old APIs and bad behaviors in browsers
• Conflict between advertising-based business models and user privacy
• Role of third-party scripts in tracking and security concerns
• The importance of considering server-side handling to improve security when using third-party scripts
• Using APIs to reduce the need for client-side interactions with potentially insecure scripts
• Governance and awareness around third-party script usage in companies
• Raising awareness through examples of supply chain attacks and their consequences (e.g. polyfill example, npm attacks)
• The role of industry standards (e.g. PCI DSS) in driving security solutions