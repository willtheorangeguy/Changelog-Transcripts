[0.00 --> 14.42]  What up nerds? I'm Jared and this is changelog news for the week of Monday, April 15th, 2024.
[15.02 --> 22.02]  For a limited time only, I'm trading changelog sticker packs for thoughtful five-star reviews
[22.02 --> 28.68]  on Apple podcasts and Spotify. Send evidence of a new review on any of our pods to jared
[28.68 --> 35.96]  at changelog.com. That's J-E-R-O-D at changelog.com with a mailing address and I'll hook you up with
[35.96 --> 44.18]  the goods. Let's do this. Okay, let's get into the news. Devin's Upwork side hustle exposed.
[45.00 --> 52.60]  YouTuber Internet of Bugs posted a lengthy breakdown exposing Devin's creators, Cognition Labs,
[52.60 --> 59.18]  for falsifying claims about their world's first AI software engineer. Devin was pitched as a fully
[59.18 --> 65.26]  autonomous software developer and one of the more impressive demos showed it completing and getting
[65.26 --> 72.76]  paid for freelance jobs on Upwork. Sound too good to be true? It did to Internet of Bugs who says,
[73.14 --> 79.22]  quote, I broke down the Devin Upwork video frame by frame and here I show what Devin was supposed to do,
[79.22 --> 85.80]  what it actually managed to do instead, and how bad a job of that it did. On the whole, that's not
[85.80 --> 90.88]  surprising given the current state of generative AI and I wouldn't be bothering to debunk it except,
[91.36 --> 97.28]  one, the company lied about what Devin could do in the video description and, two, a lot of people
[97.28 --> 102.96]  uncritically parroted the lie all over the internet and, three, that caused a lot of non-technical people
[102.96 --> 108.66]  to believe that AI might replace programmers soon. End quote. Devin really did garner a lot of
[108.66 --> 114.08]  attention, also known as money, because of that demo. We talked about it on our shows with a healthy
[114.08 --> 119.44]  amount of skepticism, I think, but I'm thankful their claims have been debunked and I hope we all give
[119.44 --> 125.78]  Cognition Labs the side eye from here on out. Exaggerating your development capabilities? Maybe Devin
[125.78 --> 134.52]  really is human, after all. Redis re-implemented with SQLite. Redka is Anton Ziyanov's attempt to
[134.52 --> 140.94]  re-implement in Go the good parts of Redis with SQLite while remaining compatible with the Redis
[140.94 --> 148.64]  API. The goal is to support five core Redis data types. Strings, lists, sets, hashes, and sorted sets.
[149.02 --> 154.00]  This is cool because so many devs, and tools for devs, already know and love Redis' API,
[154.00 --> 159.48]  but the project's legal woes and administration needs, which aren't that complex, but one more
[159.48 --> 165.68]  moving part, are not ideal. SQLite, on the other hand, is entirely open source and the most deployed
[165.68 --> 171.86]  in-process database in the world. Redka is slower than Redis, two to six times by early benchmarks,
[172.34 --> 176.96]  but that's no big surprise considering the relational backend, and it can still do 22,000
[176.96 --> 181.60]  writes per second and 57,000 reads per second, which is nothing to shake a stick at.
[181.60 --> 188.90]  Open Tofu responds to HashiCorp's cease and desist. Last week's big story was HashiCorp's
[188.90 --> 195.56]  Nastygram sent to Open Tofu and the question of whether or not they forked up by copying copyrighted
[195.56 --> 201.08]  Terraform code in an attempt to maintain future parity. The Open Tofu team has now issued their
[201.08 --> 206.64]  response, which includes a lengthy source code origination document and a three-page letter
[206.64 --> 210.24]  written by their lawyer with this sentence in bold text. Quote,
[210.24 --> 217.08]  To my client's knowledge, none of the Terraform code subject to the BUSL has been improperly copied,
[217.42 --> 222.26]  incorrectly sourced, or used for any purpose. End quote. Your move, Hashi.
[222.68 --> 225.54]  It's now time for sponsored news.
[225.54 --> 232.72]  Save the date. On April 30th, our friends at Tailscale are doing a webinar covering how to connect
[232.72 --> 240.04]  to your AWS resources easily and securely, which lets you simplify AWS connectivity by using Tailscale
[240.04 --> 245.46]  to reduce the complexity of managing secure remote access to the Amazon resources that power your
[245.46 --> 253.16]  organization. Increase security for AWS access by enabling secure remote access from AWS VPC to EC2
[253.16 --> 258.44]  instances, IP-based connectivity via subnet routing, exposing services in your EKS clusters,
[258.68 --> 264.54]  and control plane to your tail net. Achieve high availability failover, seamlessly connect across
[264.54 --> 269.56]  availability zones, and deliver persistent resource monitoring and session recording to support
[269.56 --> 274.96]  compliance goals. Reserve your spot today by following the link in your chapter data and in
[274.96 --> 280.04]  the newsletter. Thanks to Tailscale for supporting our work by sponsoring Changelog News.
[280.04 --> 284.74]  Introducing Enhance Wasm. Brian LaRue says, quote,
[284.94 --> 291.40]  Web components are the browser-native way to extend HTML, but as a primarily browser-based technology,
[291.82 --> 296.68]  they are defined with JavaScript, which limits them to either rendering solely client-side,
[296.88 --> 302.18]  which has janky performance, poor SEO, and is not optimally accessible, or within a server-side
[302.18 --> 307.36]  JavaScript runtime, which isn't always an option for shops that use other backend runtimes.
[307.36 --> 312.94]  Enhance Wasm unlocks server-side rendering web components for any backend runtime.
[313.34 --> 319.04]  End quote. Pretty cool. You write standard web components and then deploy them with any backend,
[319.22 --> 324.04]  like Rails, Django, Node, WordPress, etc. Enhance Wasm is an open source initiative,
[324.38 --> 329.60]  and they're looking for collaborators to join them on this mission. Oh, and Brian has agreed to join me
[329.60 --> 336.34]  on an upcoming JS Party episode to discuss this effort. In-depth. Pumpkin OS is a re-implementation
[336.34 --> 343.38]  of Palm OS. This is not your average Palm OS emulator. There's no Palm OS ROMs required.
[343.82 --> 349.78]  It is a full-on re-implementation of Palm OS that runs on modern architectures like x86,
[350.14 --> 357.28]  ARM, etc., and can run M68K Palm OS apps. It currently runs as a normal application on a host operating system,
[357.28 --> 362.08]  but efforts to strip down the underlying things is underway. As far as I can tell,
[362.28 --> 366.98]  this project is purely for the joy of it. That being said, it's written in C, so honestly,
[367.16 --> 372.30]  how much joy could there possibly be? Just kidding. Regardless, if you have Palm OS nostalgia
[372.30 --> 376.74]  and or the desire to hack on some low-level code, check out Pumpkin OS.
[377.44 --> 382.72]  That's the news for now, but this is episode number 90, so that means it's time once again
[382.72 --> 390.24]  for some Changelog++ shoutouts. Shoutout to our newest members, Nathan N, Luke P, Addison G,
[390.60 --> 398.58]  Sunny B, Dominic S, Stephen B, Richard W, Eric N, and Christian B. We appreciate you for supporting
[398.58 --> 405.50]  our work with your hard-earned cash. If Changelog++ is new to you, that's our membership program you can
[405.50 --> 411.62]  join to ditch the ads, get closer to the metal with bonus content, receive a free sticker pack in the mail,
[411.62 --> 416.88]  and get shoutouts like the ones you just heard. Have a great week. Don't forget that five-star review
[416.88 --> 420.30]  if you want some free stickers, and I'll talk to you again real soon.
