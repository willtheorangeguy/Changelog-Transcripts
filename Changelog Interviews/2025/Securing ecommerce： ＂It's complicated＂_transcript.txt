[0.00 --> 11.72]  Welcome to the ChangeLog, where each and every week we sit down with the hackers, the leaders,
[12.18 --> 17.80]  and the innovators of the software world to pick their brain, to learn from their mistakes,
[18.10 --> 22.84]  to get inspired by their accomplishments, and to have a lot of fun along the way.
[22.84 --> 29.50]  On this episode, I'm joined by Ilya Gregorik, distinguished engineer and technical advisor
[29.50 --> 36.24]  to the CEO at Shopify. Ilya has been hard at work securing e-commerce checkouts from sophisticated
[36.24 --> 42.48]  new attacks, such as digital skimming, and he's here to share all the technical intricacies and
[42.48 --> 48.84]  far-reaching implications of this work. But first, a mention of our partners at Fly.io,
[48.84 --> 55.42]  the public cloud built for developers who ship. You know we love Fly, and you might too. Check
[55.42 --> 61.66]  them out at Fly.io. Okay, Ilya Gregorik on the ChangeLog. Here we go.
[67.60 --> 74.44]  Well, friends, I'm here with a good friend of mine, David Hsu, the founder and CEO of Retool.
[74.44 --> 80.06]  So David, I know so many developers who use Retool to solve problems, but I'm curious. Help me to
[80.06 --> 87.70]  understand the specific user, the particular developer who is just loving Retool. Who's your
[87.70 --> 96.84]  ideal user? Yeah, so for us, the ideal user of Retool is someone whose goal, first and foremost,
[96.84 --> 102.50]  is to either deliver value to the business or to be effective. Where we candidly have a little bit
[102.50 --> 107.00]  less success is with people that are extremely opinionated about their tools. If, for example,
[107.00 --> 110.88]  when you're like, hey, I need to go use WebAssembly, and if I'm not using WebAssembly,
[111.00 --> 115.08]  I'm quitting my job, you're probably not the best Retool user, honestly. However, if you're like,
[115.08 --> 119.02]  hey, I see problems in the business, and I want to have an impact, and I want to solve those problems,
[119.34 --> 123.76]  Retool is right up your alley. And the reason for that is Retool allows you to have an impact
[123.76 --> 128.00]  so quickly. You could go from an idea, you could go from a meeting, like, hey, you know what,
[128.04 --> 132.84]  this is an app that we need, to literally having the app built in 30 minutes, which is super,
[132.84 --> 136.98]  super impactful on the business. So I think that's the kind of partnership, or that's the
[136.98 --> 140.68]  kind of impact that we'd like to see with our customers. You know, from my perspective,
[140.94 --> 147.36]  my thought is that, well, Retool is well known. Retool is somewhat even saturated. I know a lot
[147.36 --> 150.86]  of people who know Retool, but you've said this before. What makes you think that Retool is not
[150.86 --> 157.56]  that well known? Retool today is really quite well known amongst a certain crowd. Like, I think if you
[157.56 --> 162.82]  had a poll, like, engineers in San Francisco, or engineers in Silicon Valley, even, I think it'd probably get,
[162.82 --> 169.26]  like, a 50, 60, 70% recognition of Retool. I think where you're less likely to have heard of Retool is
[169.26 --> 175.16]  if you're a random developer at a random company in a random location, like the Midwest, for example,
[175.44 --> 180.24]  or like a developer in Argentina, for example, you're probably less likely. And the reason is,
[180.30 --> 184.32]  I think we have a lot of really strong word of mouth from a lot of Silicon Valley companies,
[184.32 --> 188.60]  like the Brex's, Coinbase's, DoorDash's, Stripes, et cetera, of the world. There's a lot of chat,
[188.68 --> 192.34]  Airbnb is another customer, NVIDIA is another customer, so there's a lot of chatter about Retool
[192.34 --> 197.44]  in the Valley. But I think outside of the Valley, I think we're not as well known. And that's one
[197.44 --> 203.34]  goal of ours, to go change that. Well, friends, now you know what Retool is, you know who they are,
[203.52 --> 207.26]  you're aware that Retool exists. And if you're trying to solve problems for your company,
[207.64 --> 213.58]  you're in a meeting, as David mentioned, and someone mentions something where a problem exists,
[213.58 --> 221.22]  and you can easily go and solve that problem in 30 minutes, an hour, or some margin of time,
[221.22 --> 226.24]  that is basically a nominal amount of time. And you go and use Retool to solve that problem.
[226.46 --> 233.54]  That's amazing. Go to retool.com and get started for free or book a demo. It is too easy to use
[233.54 --> 238.54]  Retool. And now you know, so go and try it. Once again, retool.com.
[252.96 --> 261.26]  So I'm here with Ilya Gregorik from Shopify, back on the show after years and years. You've been on the
[261.26 --> 265.30]  show, I think four or five times, Ilya. Welcome back. Thank you. I'm glad to be back.
[266.32 --> 269.62]  What have you been up to, man? I think it was 2021. Last time you were on the show,
[269.66 --> 273.22]  we were talking to Hydrogen. You're still at Shopify. So you've been there a very long time.
[273.32 --> 277.34]  What have you been up to? So I think, yeah, last time we talked about custom storefronts and
[277.34 --> 283.20]  a big mission we had at Shopify to enable developers to build customized storefronts using their own
[283.20 --> 288.68]  application stack. Since then, I've spent a lot of time diving into our APIs and infrastructure.
[288.68 --> 293.30]  And then also kind of in a roundabout way, ended up spending a lot of time in checkout,
[293.50 --> 298.34]  which at the end of the day is kind of the engine of the entire e-commerce operation, right? Like
[298.34 --> 303.26]  an analogy, perhaps an apt analogy is kind of like air traffic controller within your commerce operation,
[303.26 --> 308.28]  because everything, all the planes have to land there. You can think in different pieces in
[308.28 --> 313.70]  isolation. You have taxes, you have shipping, you have fulfillment concerns, you have inventory,
[313.70 --> 318.12]  inventory. But all of that has to come together during checkout, where you have all the different
[318.12 --> 325.80]  policies, all the different negotiations, all the UI that needs to be in place. And that has been a
[325.80 --> 331.92]  really interesting and complex domain to kind of wrap your head around and navigate through. And of
[331.92 --> 335.94]  course, I think today we're going to dive into one particular aspect of it, which is the compliance
[335.94 --> 341.56]  aspect, which I admit is not something that I thought I'd be working on, but it turned out to be at a
[341.56 --> 344.96]  really interesting technical challenge. So you've been at Shopify for how long now?
[345.40 --> 350.60]  In dog years, it feels like forever. In chronological time, I think it's been for four years,
[350.60 --> 353.54]  but it's been a pressure cooker.
[354.70 --> 359.46]  Yeah. And you before that, I think, was it GitHub and Google or you're at PostRank?
[359.82 --> 362.84]  You started PostRank. Can you tell us just briefly your travels?
[363.32 --> 369.04]  Sure. Let's see how far do we want to rewind. I started my professional career as a founder of a
[369.04 --> 377.24]  startup. This was back in the 2011 era. And our insight at the time was on the heels of
[377.24 --> 384.14]  Web2 and all of the social things that are happening, blogs at their heyday and all the rest.
[385.22 --> 390.96]  We figured that we could create a better search algorithm. So if you think of PageRank as the
[390.96 --> 397.02]  original PageRank of treating links to perform the ranking, effectively, that's a thumbs up,
[397.02 --> 401.78]  right? Except that when we approached this problem, and actually it was not, it wasn't 2011,
[401.88 --> 407.28]  it was 2008. We observed that there was a lot of extra signals available. Like there was literal
[407.28 --> 412.34]  thumbs up from different social platforms. You could leave comments, you can share them on
[412.34 --> 415.94]  different surfaces. So if we could aggregate all of those signals, we could build a better kind of
[415.94 --> 421.84]  human-driven algorithm for identifying what are the interesting topics. So that was the kind of the
[421.84 --> 426.46]  technical underpinning. And then we went on to build a number of products around it, which were
[426.46 --> 432.06]  analytics for publishers to help them understand where their audience is, where the content is being
[432.06 --> 437.74]  discussed, where people are engaging. There was a product for marketing agencies, which kind of worked
[437.74 --> 442.70]  in reverse, which is, hey, if I have a thing that I'd like to seed, who are the folks that I should be
[442.70 --> 448.48]  engaging? What are the communities and all the rest? And through that work, that led us to Google,
[448.48 --> 453.82]  which acquired the company. And I ended up working on Google Analytics at the time, integrating a lot
[453.82 --> 459.28]  of this kind of social analytics know-how that we acquired into the product, and later took a hard
[459.28 --> 465.60]  pivot into infrastructure, technical infrastructure within Google, where we did a lot of fun things,
[465.84 --> 469.84]  like building radio towers to figure out if we could build a faster and better radio network,
[470.10 --> 477.14]  and then learning that that's a hard problem. But then later that actually became Google Fi,
[477.14 --> 483.84]  which is an overlay network. And in the process, I picked up the kind of ambiguous problem of,
[484.52 --> 488.10]  hey, we keep talking about performance and measuring performance, like we want to make it better,
[488.20 --> 492.40]  but how do you objectively quantify it? It's one of those things where you kind of know it when you
[492.40 --> 496.72]  see it. It's like that felt slow. But if I just asked you to put a technical metric on it,
[497.06 --> 503.96]  how do you actually measure that? So we spent a lot of time with browser developers in a W3C. I was a
[503.96 --> 508.02]  co-chair of the W3C, War Performance Working Group, just wrestling with that problem of,
[508.34 --> 514.72]  like, how do you measure fast? Like, is it the unload time? No, not really. Okay, if it's like,
[514.80 --> 519.02]  when did pixels paint on the screen? But how do you measure that? And which pixels are most important?
[519.78 --> 525.38]  So this leads you down to this kind of interesting cascade of questions. So that took a while.
[525.92 --> 531.22]  That was a good, you know, five or six years of my life of working on standards and working with
[531.22 --> 537.18]  browser developers, which was a lot of fun. And later I decided to join Shopify because commerce was
[537.18 --> 545.46]  clearly an interesting area and a deep domain area. And that's been the last four years of my life here,
[545.46 --> 551.12]  where I got to work on building custom storefronts, which I think we covered in our last show.
[551.58 --> 552.02]  Yep.
[552.22 --> 560.06]  Like, what is the Shopify opinionated toolkit for building custom experiences? So today, this is
[560.06 --> 566.88]  actually Hydrogen. That has evolved quite a bit since we last talked. It is a remix-based stack
[566.88 --> 573.02]  for, with a lot of built-ins for building, like, beautiful customized experiences powered by Shopify
[573.02 --> 579.84]  APIs. From there, that work also led me into API infrastructure. So looking at our GraphQL APIs
[579.84 --> 585.56]  and trying to understand, first of all, do we expose the right capabilities there? But second,
[585.56 --> 590.46]  also, once again, performance capabilities and all the rest, we have buyers all around the world.
[590.78 --> 597.22]  We want to deliver great user experience to all the buyers. So like, how do you deploy a global cart?
[597.70 --> 604.56]  And how do you deliver the right experience reliably? And then finally, that led me into the
[604.56 --> 608.96]  guts of like technical infrastructure. Like how do we actually stand up app servers in our, like,
[609.04 --> 613.74]  Ruby stack? Shopify is a Ruby primarily company, right? So rebooting our application stack,
[613.74 --> 618.54]  and also working on checkouts, which kind of brings us back to the earlier part of the conversation.
[619.14 --> 623.22]  Yeah, full circle. So we're definitely going to talk checkouts. Since you somewhat moved on from
[623.22 --> 630.58]  your, at least web performance years, I'm curious to get your take on recent work, specifically Core Web
[630.58 --> 635.82]  Vitals. Is that something you've been tracking? And do you have a hot take? Do you like that? Do you
[635.82 --> 638.94]  think it's hits the mark, misses the mark? What are your thoughts on that as a metric?
[639.56 --> 641.96]  Core Vitals was one of my key projects when I worked at Google.
[641.96 --> 646.60]  So it's, it's, it's, it's, at least to me, this is definitely, yeah, well, it wasn't purely me,
[646.68 --> 652.02]  but it was one of the key things that we incubated. And part of it was, it's actually the same
[652.02 --> 656.68]  question. Like it, what is the definition of a vital, right? Like a vital is like a vital,
[656.80 --> 661.24]  then the incentive behind the vital was like a vital signal, just like you have a heartbeat in a human
[661.24 --> 666.28]  body. Like what are those things that you measure about a website that tells you that it's a good
[666.28 --> 672.98]  experience. And the key problem that we wanted to solve was first come up with some shared agreement
[672.98 --> 679.54]  across browsers of how we can measure that reliably and not just in a lab environment, because the
[679.54 --> 685.50]  thing that we keep learning time and time again is that the outside world is just so unpredictable
[685.50 --> 692.60]  that you have to measure what happens in the real world. Like you can, you can bake in all kinds of
[692.60 --> 697.52]  assumptions into your model. And then you get consistently surprised when you release your
[697.52 --> 702.12]  application or website into the public and you're like, wow, you know, I never expected this amount
[702.12 --> 707.34]  of traffic to come from this particular region, which happens to have this routing topology and my CDN
[707.34 --> 712.30]  just doesn't account for it. Or like my API is located in North America, but I have this tidal wave of
[712.30 --> 718.12]  users coming from, I don't know, Europe or somewhere else. And for them, the experience is just that much
[718.12 --> 724.08]  worse. So ROM or real user measurement metrics are critical. And Web Vitals was our attempt to,
[724.22 --> 730.04]  first of all, define what those are, like what does that subset? And second, what are the recommended
[730.04 --> 735.78]  thresholds? Right? Because everyone has a different definition, like is fast 100 milliseconds, is fast
[735.78 --> 744.08]  one second? We try to align on that. So I'm really glad to see that the Web Vitals has continued to evolve.
[744.08 --> 750.56]  Like the initial set, when we first published, I believe it was back in 2020 or so, it focused on
[750.56 --> 756.02]  loading metrics. But we knew even when we were walking into that announcement that we really need
[756.02 --> 763.12]  to also talk about interactivity. Like it's not just that the pixels rendered fast, right? It's also,
[763.48 --> 771.14]  hey, is it responsive? Is the page locking up when I'm trying to interact with it? How about scrolling?
[771.14 --> 777.68]  Like how smooth is that? So Web Vitals continues to evolve and add those metrics. And I think that's great.
[777.74 --> 781.76]  And it's really important for us as an industry to have that shared definition of what good looks like.
[782.26 --> 786.74]  Shows how fast the internet moves. Because I thought core Web Vitals was still relatively new.
[786.96 --> 791.64]  And it turns out it's like, you know, five years ago and you're the one working on it. So crazy.
[792.18 --> 797.38]  I think it highlights the complexity of the problem. It takes a long time to propagate
[797.38 --> 804.04]  kind of those practices and metrics. But yes, it's been a long journey and it was a great capstone
[804.04 --> 809.36]  of like all the work that I did at Google and web performance. What shipping with Vitals felt like a
[809.36 --> 815.08]  good milestone and that allowed me to kind of give myself permission to shift attention to other things.
[815.08 --> 823.54]  Right. Well, let's do that. Let's shift attention to checkouts, compliance, security, PCI, some of these
[823.54 --> 830.00]  things that honestly scare away or maybe lull to sleep. Many of us, we start talking about compliance
[830.00 --> 837.52]  matters. PCI version four is burgeoning or maybe it's out now. I don't know. Tell us the skinny. What is
[837.52 --> 842.46]  PCI? Why does it matter? And then what's, we'll get to what's new in the latest versions.
[842.46 --> 849.56]  Sounds good. So first, let's unpack the acronyms because those are always not helpful. PCI stands
[849.56 --> 856.28]  for payment card industry and it provides us, it defines a set of security requirements that you
[856.28 --> 864.38]  have to comply with as someone who processes sensitive credentials. So an example would be your
[864.38 --> 870.22]  personal access number or your credit card number plus the CVV and all the other data, right? There's a
[870.22 --> 875.02]  set of protections put in place around that for if you're handling that data, then how you should be
[875.02 --> 881.26]  treated, what kind of security precautions those services must comply by and all the rest. And it is
[881.26 --> 886.98]  a fairly burdensome set of requirements to comply with. Then you have to get periodically audited and
[886.98 --> 892.60]  show that you're in good standing and all the rest. So as a consumer, this is great because
[892.60 --> 899.50]  fraud on the internet is definitely a big thing isn't still very much an unsolved problem, right? Like
[899.50 --> 907.06]  it is entirely entering a credit card number into a web or random web form is not a secure
[907.06 --> 914.42]  undertaking, right? But we've managed to build a relatively reliable experience for consumers,
[914.42 --> 922.34]  thankfully. Now what's different about PCI v4? In PCI v3, a key requirement was that
[922.34 --> 929.70]  you had to protect the service or the surface area where you're entering your credentials. So
[929.70 --> 934.68]  technically how we've solved that as an industry is we said, okay, well, if I want to accept payments
[934.68 --> 940.44]  on the web, I'm not going to do the obvious thing, which is going to put a random form on my page and
[940.44 --> 946.44]  start accepting credit cards because then I'm accepting that data. Like my service will get a
[946.44 --> 953.12]  post request and I'm going to have the unencrypted payment credentials. And now I'm liable for all of
[953.12 --> 958.96]  the compliance. Instead, why don't we outsource this problem? And hey, we actually have a great tool
[958.96 --> 964.88]  in the web platform. It's called iFrames. iFrames can provide us to, can give us an ability to embed
[964.88 --> 970.38]  an external service that can basically do this. And we can skin it in a way that it looks seamless.
[970.44 --> 975.88]  Right. Most pages that you visit on the internet, the payment form, if you actually open up your
[975.88 --> 982.04]  dev tools, you'll see that it's iFramed for the specific reason, but it doesn't look janky. It
[982.04 --> 987.00]  looks integrated into the website. And the nice property of the solution is you can then just
[987.00 --> 994.96]  basically all of the inputs, all of the, and like mouse events are obfuscated from the parent page.
[994.96 --> 1002.66]  So that means you can wholly like delegate the responsibility for PCI v3, at least to your
[1002.66 --> 1007.16]  provider. A common example of that would be someone like Stripe. If you want to accept payments on your
[1007.16 --> 1013.66]  website, they provide a like Stripe elements. You import a web component, pass out a few props and
[1013.66 --> 1019.86]  boom, you have a checkout form under the hood. It'll inject a knife frame and do all the things on your
[1019.86 --> 1024.66]  behalf. So that's great. And that's been effectively where we've settled. You know, I think PCI v3 came
[1024.66 --> 1032.62]  into existence around 23 or sorry, 2013 or 2014. So the last, let's say 10 years or so, that's how we've
[1032.62 --> 1042.06]  solved that problem as an industry. Now that is really good, but it's not sufficient. So in the interim,
[1042.06 --> 1049.42]  what we've observed is, Hey, sure, you've isolated this particular input into a secure sandbox.
[1050.20 --> 1054.74]  But what happens if your top level page gets compromised? Let's say you have a supply chain
[1054.74 --> 1060.26]  attack or you have an XSS hole in your checkout page and someone injects a malicious script.
[1060.54 --> 1068.04]  What could they do with that? Well, what stops them from removing your secure input form and replacing
[1068.04 --> 1073.40]  with a fake one or maybe providing an overlay and then tricking the user effectively into entering
[1073.40 --> 1080.64]  information into an insecure form that then exfiltrates the data and then swaps in the original,
[1081.16 --> 1088.10]  right? This class of attack is called like skimming attacks, also known as mage card attacks,
[1088.50 --> 1093.88]  which is a nod to Magento, not to cast shade on Magento, but I think one of the first like published
[1093.88 --> 1100.04]  large scale instances of this attack was against Magento, which had some flaw. Magento is an
[1100.04 --> 1105.94]  e-commerce platform, open source. And for better or for worse, that like mage card attack name has stuck.
[1106.34 --> 1112.74]  Now, to be clear that this is a problem that spans all platforms regardless, right? As long as you have
[1112.74 --> 1119.78]  some sort of vector for attack. So PCI before tries to solve for this particular problem. Like it tries to
[1119.78 --> 1126.34]  tighten the perimeter to say, it's no longer sufficient to protect the payment page. You also
[1126.34 --> 1132.00]  have to protect or provide some guarantees around the parent page, the thing that is embedding this
[1132.00 --> 1139.92]  payment form. Okay. And specifically, there's a set of set of provisions. I think that in the spec
[1139.92 --> 1144.42]  itself, which is very long, like we'll zoom in on one particular aspect of this whole conversation,
[1144.42 --> 1149.98]  which is like section 643. It's one of these random numbers that you just remember once you've
[1149.98 --> 1159.22]  been long enough in the PCI game. Yep. 643 defines in high level terms, three requirements. It says,
[1159.38 --> 1164.56]  hey, for the parent page, you have to maintain an inventory of all scripts that are being executed
[1164.56 --> 1169.62]  on the page. And also please document why they're necessary and how they're being used.
[1170.62 --> 1177.32]  Right. So just like, give me an inventory one. Two, once you have that inventory, have some mechanism
[1177.32 --> 1182.26]  to ensure that only those scripts, the authorized scripts are being loaded. And then finally,
[1182.80 --> 1188.72]  have some way to guarantee or check the integrity of each loaded script, right? Because you could say,
[1188.84 --> 1193.34]  hey, this is my inventory. These are the scripts I've authorized, but what if that thing got compromised
[1193.34 --> 1198.30]  as an example, right? Somebody replaced it with a malicious script because of supply chain attack
[1198.30 --> 1204.36]  or otherwise. So those three things combined give you strong assurances about what's executing a
[1204.36 --> 1209.50]  top level page, which is great. Now, the practical reality of how you go about implementing that,
[1209.74 --> 1213.22]  as you can imagine, is complicated. Sounds like a lot of work.
[1213.74 --> 1217.88]  Yeah, it's good. Exactly. And it's complicated for two reasons. Like first, we should partition this
[1217.88 --> 1222.48]  problem into like if the two of us had had a checkout page and we were to sit down and try to
[1222.48 --> 1228.58]  think through like, okay, we need to meet these compliance requirements. I would partition the
[1228.58 --> 1233.06]  problem into first party and third party scripts, first of all, right? Like, okay, for the first party
[1233.06 --> 1240.42]  content, yes, like we can define a process for we audit which scripts we include, we audit their
[1240.42 --> 1246.28]  dependency, we have some security review, we have release process, we have CI checks. Sure, I can give you
[1246.28 --> 1252.24]  inventory of those scripts, right? Also, because they're first party, I can put a content security
[1252.24 --> 1258.00]  policy and maybe even put a sub resource integrity, which are hashes that effectively fingerprint the
[1258.00 --> 1265.74]  specific version of that page. So maybe during my build, I can just enforce a CSP, snapshot the hashes,
[1265.92 --> 1272.10]  put those on the thing and like, great. Now I have strong assurances that the scripts that are being
[1272.10 --> 1280.32]  executed on the page are mine and tied to a specific version. So far, so good. Now, what about the third
[1280.32 --> 1287.76]  parties? One of the challenges with checkout is they're one of the most important pages for the
[1287.76 --> 1294.66]  entire e-commerce operation. Like this is where instrumentation is critical, right? You want to know
[1294.66 --> 1299.60]  performance telemetry. You want to know which elements user is interacting with because that
[1299.60 --> 1306.96]  affects conversion. You are likely running A-B tests. So you have either first party or a set of third
[1306.96 --> 1312.24]  party vendors doing that. Of course, you have all of the conversion pixels that need to be executed
[1312.24 --> 1316.48]  because all the ad campaigns and all of the analytics that you need to drive that entire up
[1316.48 --> 1323.14]  funnel, down funnel loop. And what about all of the other marketing pixels that you may need?
[1324.42 --> 1330.34]  It's not uncommon. If you just, if you take an average checkout page and you open up the network tab,
[1330.34 --> 1337.30]  you'll probably find hundreds of scripts on many of them, right? And oftentimes it'll be,
[1337.94 --> 1344.94]  hey, we load a tag manager that then allows our marketing and other teams to inject whatever they
[1344.94 --> 1353.92]  need to drive the whole process. But now we're staring at that problem and we're saying, so how exactly do I
[1353.92 --> 1359.80]  apply an inventory and all these things? Because first of all, like my partner asked me to put a tag
[1359.80 --> 1365.52]  manager so they can load things. Well, I need to unwind that decision, right? Because now I need to
[1365.52 --> 1370.12]  know exactly what everything that's being executed and I need to have kind of a full transit of chain
[1370.12 --> 1377.90]  of all dependencies. I need to be able to account for that. Second, you need to provide, how do I know
[1377.90 --> 1384.34]  what CSP policy should I define? Can I just say only load from partner.com or is the partner also
[1384.34 --> 1389.98]  loading from some other CDNs? Well, you know, that's, I need to go ask the partner for what those
[1389.98 --> 1396.32]  assurances are. And then lastly, if I want to ensure integrity, that's not my content. How do I obtain
[1396.32 --> 1401.26]  the hash of the thing? And then if that partner wants to rev the version of their script, how do I
[1401.26 --> 1407.06]  get the hash so I can put the thing inside? And then also I'm not the one injecting the content
[1407.06 --> 1412.00]  into the page. So it becomes this like a really complicated rigmarole of like, actually, I just cannot do this.
[1412.00 --> 1418.80]  Yeah. Sounds not possible. Precisely. Which is one of those things where the standard was written
[1418.80 --> 1423.36]  with good intent, right? And they in passing mentioned, Hey, you have these tools, you have
[1423.36 --> 1428.84]  content security policy, you have sub research integrity in principle, in theory, you have the
[1428.84 --> 1435.08]  right things to do this job. In practice, if you unpack your average checkout page on the web, it's like,
[1435.38 --> 1439.52]  I don't know how I would achieve this. I could guarantee maybe a slice of it for first party,
[1439.52 --> 1446.00]  but how do I solve this for third parties? Right. So turns out, it's complicated, right?
[1446.64 --> 1449.62]  So I thought you might say that.
[1469.52 --> 1481.46]  Well, friends, I'm here with Scott Dietzen, CEO of Augment Code. Augment is the first AI coding
[1481.46 --> 1486.86]  assistant that is built for professional software engineers and large code bases. That means context
[1486.86 --> 1492.66]  aware, not novice, but senior level engineering abilities. Scott Flex for me, who are you working
[1492.66 --> 1495.04]  with? Who's getting real value from using Augment Code?
[1495.04 --> 1501.22]  So we've had the opportunity to go into hundreds of customers over the course of the past year,
[1501.36 --> 1506.84]  and show them how much more AI could do for them. Companies like Lemonade, companies like
[1506.84 --> 1512.96]  Kodem, companies like Lineage and Webflow. All of these companies have complex code bases. If I take
[1512.96 --> 1518.24]  Kodem, for example, they help their customers modernize their e-commerce infrastructure. They're
[1518.24 --> 1523.18]  showing up and having to digest code they've never seen before in order to go through and make these
[1523.18 --> 1528.36]  essential changes to it. We cut their migration time in half because they're able to much more
[1528.36 --> 1534.04]  rapidly ramp, find the areas of the code base, the customer code base that they need to perfect and
[1534.04 --> 1538.88]  update in order to take advantage of their new features. And that work gets done dramatically more
[1538.88 --> 1540.82]  quickly and predictably as a result.
[1541.48 --> 1546.44]  Okay, that sounds like not novice, right? Sounds like senior level engineering abilities.
[1547.14 --> 1552.14]  Sounds like serious coding ability required from this type of AI to be that effective.
[1552.14 --> 1557.68]  100%. You know, these large code bases, when you've got tens of millions of lines in a code base,
[1557.74 --> 1562.88]  you're not going to pass that along as context to a model, right? That would be so horrifically
[1562.88 --> 1568.78]  inefficient. Being able to mine the correct subsets of that code base in order to deliver AI insight
[1568.78 --> 1576.18]  to help tackle the problems at hand. How much better can we make software? How much wealth can we release
[1576.18 --> 1582.50]  and productivity can we improve if we can deliver on the promise of all these feature gaps and tech debt?
[1582.74 --> 1588.04]  AIs love to add code into existing software. You know, our dream is an AI that wants to delete code,
[1588.18 --> 1592.80]  make the software more reliable rather than bigger. I think we can improve software quality,
[1593.30 --> 1599.06]  liberate ourselves from tech debt and security gaps and software being hacked and software being fragile
[1599.06 --> 1604.62]  and brittle. But there's a huge opportunity to make software dramatically better. But it's going to take an AI
[1604.62 --> 1608.44]  that understands your software, not one that's a novice.
[1609.02 --> 1613.88]  Well, friends, Augment taps into your team's collective knowledge, your code base, your documentation,
[1614.12 --> 1619.24]  dependencies, the full context. You don't have to prompt it with context. It just knows.
[1619.70 --> 1622.80]  Ask it the unknown unknowns and be surprised.
[1622.80 --> 1629.18]  It is the most context aware developer AI that you can even tap into today. So you won't just write code
[1629.18 --> 1635.04]  faster. You'll build smarter. It is truly an ask me anything for your code. It's your deep thinking buddy.
[1635.52 --> 1645.98]  It is your stay in flow antidote. And the first step is to go to augmentcode.com. That's A-U-G-M-E-N-T-C-O-D-E.com.
[1646.32 --> 1651.52]  Create your account today. Start your free 30 day trial. No credit card required.
[1651.52 --> 1654.22]  Once again, augmentcode.com.
[1658.06 --> 1662.76]  So how do we approach this at Shopify? I think there's, let me take first a branch into Shopify
[1662.76 --> 1668.00]  and then we can talk about kind of the broader, broader landscape. We've been on a mission to
[1668.00 --> 1674.74]  provide stronger control and behavior over checkout, not just because of compliance, but because we want
[1674.74 --> 1680.86]  upgrade safety, reliability, performance and security in checkout. And our observation is
[1680.86 --> 1686.54]  first of all, for those not familiar, Shopify provides a hosted checkout experience where
[1686.54 --> 1695.42]  you don't get access to the underlying HTML, right? We provide the base UI and we allow you to
[1695.42 --> 1699.38]  configure it. And it's a very flexible system. You can customize the branding. You can custom,
[1699.48 --> 1703.32]  you can introduce custom components. You can install apps that introduce components.
[1703.32 --> 1709.32]  You can do a lot of customizations to make it feel like your own. But a key principle that we've
[1709.32 --> 1714.94]  been operating on is that we want a set of predefined, first of all, we're going to define the UI
[1714.94 --> 1721.84]  elements because we want to preserve consistency and experience. And we want to optimize for performance,
[1722.10 --> 1729.70]  security and all the rest. What that allows us to do is to say, actually, we're not going to allow
[1729.70 --> 1737.12]  any third-party scripts in our top-level page. And that is a very consequential and big decision.
[1737.28 --> 1744.04]  This has been work that we've been on an arc for about three years, if not more, to achieve. And
[1744.04 --> 1749.14]  we're finally there. And now we're reaping the benefits of that. So then the question is,
[1749.70 --> 1753.34]  wait a second. So you excluded all third-party scripts, but what about all those shiny things that
[1753.34 --> 1757.40]  you just mentioned earlier, right? The analytics, the customizations, the everything else.
[1757.40 --> 1764.24]  And this is where sandboxing comes in. So our decision was to say, only effectively, the moment
[1764.24 --> 1769.50]  you introduce a third-party script into top-level page, you have untrusted content and you've
[1769.50 --> 1775.00]  compromised all integrity of the top-level page. We cannot provide any assurances on integrity of
[1775.00 --> 1782.72]  the top-level page, right? Because in the past, when we did allow folks or merchants to bring their
[1782.72 --> 1789.34]  own JavaScript into top-level page, they just end up doing things that break compatibility.
[1789.34 --> 1793.98]  Like they'll hook in a specific selector, right, to inject an element,
[1794.56 --> 1799.62]  knowing full well that we've never defined a contract for it. And then if we change that,
[1799.70 --> 1804.56]  we will break them. And then security is compromised as well, because they're introducing
[1804.56 --> 1806.42]  their own scripts and we can't provide any assurance.
[1806.42 --> 1811.74]  So we took away that capability and said, instead, we're going to give you a sandbox.
[1812.20 --> 1818.06]  So we're going to spin up a set of web workers and give you a bridge. So for example, we've built a
[1818.06 --> 1824.96]  library and open source called Remote Dumb, which allows you to construct an element tree in an
[1824.96 --> 1832.42]  isolated worker that operates off the main thread. And then that UI is reflected back for you in the
[1832.42 --> 1839.64]  parent page. So it feels like ergonomically, DX-wise, it feels still very straightforward
[1839.64 --> 1844.82]  because you're just manipulating elements. And we provide a predefined set of UI elements that
[1844.82 --> 1851.94]  fit into the checkout UI and work with all the branding primitives. But we do that work on your
[1851.94 --> 1856.30]  behalf. And the critical part is because we control the bridge between the web worker and the top-level
[1856.30 --> 1862.04]  page, we have tight control over what kind of mutations can be pushed between the parent,
[1862.04 --> 1868.82]  and the isolator worker. So you can't just arbitrarily inject JavaScript or perform unsafe operations
[1868.82 --> 1876.18]  on the parent page. So in that way, we can take any third-party script, put it into a sandbox and say,
[1876.26 --> 1881.58]  you know what, you can do whatever the heck you want in that environment, because you can load
[1881.58 --> 1888.12]  a transit of chain of other dependencies. We don't particularly care because all we know that
[1888.12 --> 1894.96]  the operations that you can pass back to the parent page are safe and approved set that we will allow.
[1895.72 --> 1901.76]  And we also control what data is exposed to you. So for example, if you have an extension that wants
[1901.76 --> 1911.00]  access to some sensitive buyer data, first that application and then the worker itself needs to have the right
[1911.00 --> 1918.10]  consent. So a worker that has not been granted the right consent by the merchant or the buyer will just not have
[1918.10 --> 1924.68]  access to that data. So that is our solution for extensibility and allows us to partition the
[1924.68 --> 1930.66]  problem of first-party and third-party content. It's based on remote DOM. And then we use the same
[1930.66 --> 1937.04]  technology for our pixels or analytics as well, where we define an event bus, we emit all the events,
[1937.38 --> 1941.80]  analytics providers are executed in the sandbox as well.
[1942.42 --> 1947.30]  Is that a compromise in terms of functionality? Do you get 100% of what you could do before in terms of
[1947.30 --> 1953.00]  what you all are providing or is it like a, are you constraining people through and losing features
[1953.00 --> 1953.54]  along the way?
[1954.04 --> 1958.98]  Yeah, you asked exactly the right question. So the answer is we've had to rebuild a lot of stuff
[1958.98 --> 1964.46]  because a web worker, if you're familiar, is not the same thing as working in the top level page,
[1964.52 --> 1967.94]  right? Like it doesn't, it doesn't give you access to the DOM. It doesn't expose all the same events.
[1967.94 --> 1974.48]  So the reason it took us as long as it did to layer all of this infrastructure is because we had to work
[1974.48 --> 1979.52]  with partners and replicate. So what do you actually need, right? Instead of raw access to the DOM tree,
[1979.70 --> 1983.98]  like what are you looking for? For example, if you were building a heat map solution as an example,
[1984.18 --> 1989.58]  right? Like some of our merchants are really keen on having very visual, clear understanding of how users
[1989.58 --> 1995.62]  are behaving on their checkout page. Like you need a lot of different access to a lot of different events
[1995.62 --> 2000.06]  elements. Okay. Well, let's, let's work through that and figure out what is the right subset that
[2000.06 --> 2006.52]  we can expose via this bridge. So over time, we've built up a collection of these APIs and primitives,
[2006.66 --> 2012.88]  some of which effectively replicate what is available on the parent page. One of the challenges
[2012.88 --> 2017.74]  here, by the way, is like, if you ever work with web workers is they use asynchronous communication,
[2018.00 --> 2022.70]  right? So you have to post message between a web worker and the top level page. Whereas a lot of the
[2022.70 --> 2028.02]  DOM APIs are synchronous APIs. So if you're just naively writing code, expecting to be executed
[2028.02 --> 2034.44]  on top level page, you would use synchronous APIs. So we've had to shim some of that. And like in places
[2034.44 --> 2039.84]  we try to keep it as close as we can to what you would expect as a developer, because we don't want to
[2039.84 --> 2044.96]  impose additional friction. But in certain places we had to provide replacement APIs where we said,
[2044.96 --> 2049.88]  look, you're building for Shopify. It will operate across scale of millions of merchants.
[2049.88 --> 2054.44]  If you're building an application, it is worth for you to do this extra step because then you have
[2054.44 --> 2060.76]  all of these insurances in place. So a lot of handholding with partners and getting the developers
[2060.76 --> 2067.62]  to adopt all of those APIs. But the benefit of all of that work today is I'm not going to say we're done
[2067.62 --> 2072.18]  because there's still more things to build, but we're in a really good place because now all of our
[2072.18 --> 2080.38]  merchants are running on the sandboxed primitive that I've described. And what we can provide is,
[2080.62 --> 2084.30]  first of all, upgrade safety. We can safely roll forward our capabilities in checkout,
[2084.84 --> 2092.62]  knowing that customizations that you've deployed will not break as you move forward, right? Because
[2092.62 --> 2097.20]  we control the bridge, we control the API interface. So if we change the underlying API on our site,
[2097.20 --> 2103.82]  we can still provide guarantees about that. We have reliability. We know that. So for example,
[2103.90 --> 2109.34]  we saw examples where merchants would inject scripts where a partner would just time out.
[2109.62 --> 2113.52]  So they would have some logic and for some reason their service goes down and then the checkout's
[2113.52 --> 2118.30]  broken because, well, it's just waiting to render, right? Like Shopify, you've broken the checkout.
[2118.46 --> 2122.98]  It's like, actually, it's your part. It's your script that you injected of a partner that failed
[2122.98 --> 2129.78]  to scale to your flash sale, right? So now we have assurances about that. And then finally,
[2129.88 --> 2136.24]  performance and security. Another benefit of putting work into the sandbox is it moves all
[2136.24 --> 2143.16]  the work off the main thread. So you can't have code that monopolizes the main thread and renders the UI
[2143.16 --> 2147.44]  unresponsive, which gets back to our web vitals conversation, right? Like we can make better
[2147.44 --> 2151.92]  performance guarantees about how the page is loaded, how responsive it is, and the rest. And finally,
[2151.92 --> 2157.20]  there's a security bit, which is, we know that you can't inject arbitrary content in top level page
[2157.20 --> 2162.58]  and exfiltrate data. And then finally you have PCI compliance because now we have a clean partition
[2162.58 --> 2169.98]  where we say, as Shopify as a platform, we will provide all of the inventory authorization and
[2169.98 --> 2175.20]  integrity checks for the first party scripts that are executed in top level page. And, oh, by the way,
[2175.32 --> 2179.96]  you can totally bring third party content, but we will execute it in this isolated context
[2179.96 --> 2186.74]  that allows us to punt that problem and not have to worry about all of the integrity
[2186.74 --> 2190.52]  problems that happen when you just include it in a top level page.
[2190.52 --> 2196.18]  So did I hear you right that you said all your merchants are already using this? You're able
[2196.18 --> 2199.84]  to deploy that without, or did you not say all?
[2199.84 --> 2199.94]  Yeah.
[2200.40 --> 2200.70]  Yes.
[2200.78 --> 2200.92]  Yeah.
[2201.24 --> 2207.24]  Yes. All. Yeah. So this has been a long journey to move all of our merchants onto this new platform.
[2207.24 --> 2213.34]  But as of earlier this year, like 99.9% of our merchants are on this platform. There may be like
[2213.34 --> 2218.66]  one or two exceptions, but effectively any Shopify checkout that you, Shopify power checkout that you
[2218.66 --> 2221.16]  visit today as a consumer is running on this infrastructure.
[2221.70 --> 2227.72]  Hmm. And that was something that they had to opt into or that you just did on it. Like,
[2227.76 --> 2231.20]  how did you all roll that out? You said it took a long time, but what was, what did it look like?
[2231.20 --> 2235.76]  Well, it took a long time because of the right question that you asked, which is,
[2236.10 --> 2242.04]  Hey, did you, what did you have to take away? Right. And the answer is we had to rebuild a lot
[2242.04 --> 2246.06]  of the capabilities because we've created this isolated environment. We've had to recreate a lot
[2246.06 --> 2252.80]  of APIs. So a lot of our work was working with other developers, partners who provide capabilities
[2252.80 --> 2259.72]  that merchants want in checkout to make sure that they can bring the same capabilities into this new
[2259.72 --> 2265.60]  world of sandbox execution. That's, that was the long haul. And then for some merchants that
[2265.60 --> 2272.62]  had ability to manipulate content in the top level page, you know, it was a combination of
[2272.62 --> 2279.42]  documentation, handholding, consulting, and just getting them to move to the new world so they can
[2279.42 --> 2285.76]  benefit from all of these capabilities. But we're, we're there and the time is right because now you
[2285.76 --> 2288.36]  have PCI v4 compliance effectively taking care for you.
[2289.72 --> 2298.76]  And do you think that PCI v4 compliance means you cannot be skimmed in the way that you could prior,
[2298.76 --> 2302.12]  or do you think it could still happen in new and exciting ways?
[2303.12 --> 2310.30]  Right. Right. So I think this actually is, is another layer that we should add here. What I've
[2310.30 --> 2317.54]  described is runtime compliance or runtime guarantees, right? So the thing that we've built actually
[2317.54 --> 2322.58]  allows us to provide assurance or like extend some guarantees over, we just know that it's not,
[2322.58 --> 2328.06]  it's not possible to inject third party content. So if you have a supply chain attack on that,
[2328.18 --> 2330.62]  like it's isolated into a thing that doesn't matter.
[2330.62 --> 2339.06]  Right. In practice, I think what a lot of other players are and e-commerce providers will end up
[2339.06 --> 2346.88]  using or how they'll provide compliance is retroactive monitoring. So PCI does not enforce a requirement
[2346.88 --> 2352.46]  that you have to have runtime guarantees. What it says is, Hey, you should have a process
[2352.46 --> 2359.10]  that provides an inventory, make sure that scripts are authorized and you have the integrity. It
[2359.10 --> 2363.76]  doesn't specify that it like, it needs to be guaranteed. So practically how, how could you
[2363.76 --> 2369.52]  implement this and how, how do most, like if you go and search for PCI compliance security products,
[2369.52 --> 2374.60]  you will find plenty that will basically say, Hey, I know a great solution for your PCI problem.
[2374.60 --> 2381.56]  You know what it is? Deploy my JavaScript into your page. Right. Because more JavaScript is always a
[2381.56 --> 2387.58]  solution. Right. And I will instrument the page and listen for all the things that are happening.
[2387.96 --> 2393.54]  I will observe all the other scripts. I will build an inventory. I will monitor if it changes.
[2393.90 --> 2399.34]  I will try to provide hashes and effectively I'll like, you can delegate this problem to me.
[2399.34 --> 2405.08]  Now you can see a flaw in that reasoning, right? It's like, how do you know that your script is not
[2405.08 --> 2409.96]  going to get compromised either? Right. Who watches the watchers? Right. Well, there's that. And how do
[2409.96 --> 2415.18]  you know that the malicious thing doesn't come up with a clever way to obfuscate itself from you?
[2415.18 --> 2422.20]  Right. It's the antivirus problem, right? Like virus hiding, exactly. Virus hiding from the antivirus
[2422.20 --> 2429.32]  problem. Um, but that is likely a solution that many will adopt as a retroactive.
[2429.34 --> 2435.68]  So effectively you observe if anything has changed. It's like, oh, well, that's odd. I'm
[2435.68 --> 2441.90]  seeing a set of reports for a script that I did not expect relative to my inventory as I defined.
[2442.54 --> 2447.50]  Does that indicate that I have a problem on my site? Probably. Right. So there's some guardrails
[2447.50 --> 2454.24]  that PCI sets for like how long that period can be and how you need to react to it. But it is strictly
[2454.24 --> 2459.70]  lesser and less secure experience, which gets back to your question. Like if you have these
[2459.70 --> 2466.16]  assurances, it doesn't mean that the class of attacks is eliminated. The answer is it depends
[2466.16 --> 2471.54]  on how you implement it. Right. So in our case as Shopify, I would feel pretty strongly about
[2471.54 --> 2478.70]  extending a promise of like, yeah, unless our content, first party content is compromised,
[2478.70 --> 2486.34]  it would be very hard to, to compromise this page. Now we can control a Shopify is the buyer
[2486.34 --> 2491.02]  has installed a browser extension that injects arbitrary scripts into the page, right? Like
[2491.02 --> 2495.28]  that is outside of our control because that's a, that operates at a higher layer, or maybe
[2495.28 --> 2500.92]  you even have malware on your computer that does things and inject content into the page
[2500.92 --> 2506.84]  or otherwise intercepts like when you're typing. Like those things are still possible. It is not a,
[2507.48 --> 2512.88]  we've completely eliminated this type of attack, but it certainly makes it a heck of a lot harder
[2512.88 --> 2519.00]  because now it means that at least there at a minimum, there's a way the merchants are required
[2519.00 --> 2525.74]  to detect these changes or the, these, um, attacks and remediate so they can't just go unnoticed.
[2525.74 --> 2533.10]  Mm-hmm. So this all sounds like a lot of really good work you all have done at Shopify for Shopify
[2533.10 --> 2543.12]  and Shopify's customers. Thinking bigger, it would be great if your hard work and years of rethinking
[2543.12 --> 2551.20]  this runtime and sandboxing and actually providing the security that PCI v4 wants everybody to have,
[2551.20 --> 2557.20]  whether or not they do or not to be compliant. Can't some of that get into the browser? Like,
[2557.20 --> 2563.08]  couldn't we just build it? Like, could, could, could your work extend beyond Shopify's borders
[2563.08 --> 2564.56]  and help other people too?
[2565.20 --> 2568.96]  Yeah, absolutely. And this is, I think this is key. This is not just about Shopify. It's about
[2568.96 --> 2575.22]  improving the buyer experience on the, on the web holistically. So two things to answer that.
[2575.30 --> 2579.82]  First of all, the remote DOM library that I mentioned, it's an open source project that we've built
[2579.82 --> 2585.74]  in open source. So if you go to github.com slash Shopify slash remote DOM, you'll find that there,
[2585.74 --> 2590.02]  uh, take a look at it, use it. This is, that's the technology that powers Shopify checkout.
[2590.66 --> 2594.68]  Other large companies have already adopted it. I believe Stripe is using it for their apps.
[2595.04 --> 2600.62]  Actually fun story. Uh, when we built the project, I think Stripe beat us to using it in a production
[2600.62 --> 2601.82]  product. Really?
[2601.82 --> 2607.74]  Even though we were the ones developing it for checkout, but like it is, um, it is used
[2607.74 --> 2615.18]  at Shopify and, uh, by other big, big players to provide this form of isolation. And the general
[2615.18 --> 2619.74]  pattern is, Hey, I have a trusted first party surface into which I want to bring in third
[2619.74 --> 2625.66]  party content. And I, I don't want to compromise integrity of my first party top level surface.
[2625.66 --> 2630.94]  Right. Well, remote DOM is one of the like technical solutions for that. So please take a look at that.
[2630.94 --> 2635.90]  That's answer. Number one, second though, and coming back to the browser conversation.
[2636.86 --> 2642.06]  Absolutely. The primitives that we have in browsers today, content security policy and SRI,
[2642.94 --> 2647.74]  we can make better. And, uh, we've actually done a bunch of work on exactly that at Shopify. Um,
[2648.78 --> 2654.22]  we don't want to do work in JavaScript that we could push into the browser because the browser is
[2654.22 --> 2658.14]  just much more efficient and it has capabilities that we otherwise would be very hard for us to
[2658.14 --> 2664.06]  replicate. So first let's like enumerate some trivial examples of gaps, script integrity.
[2664.06 --> 2669.66]  So, uh, sub resource integrity, uh, for those not familiar on your script tag, you can pass in
[2669.66 --> 2674.86]  effectively a hash. So when you inject the tag into your HTML, you can pass in a hash that is a
[2674.86 --> 2680.70]  fingerprint. And when the browser loads the script before it executes that it can compare the hash of
[2680.70 --> 2685.34]  the thing that it fetched versus what you've defined and say, Hey, if those two things match,
[2685.34 --> 2690.86]  great. I will execute the script. Otherwise I'm going to raise a violation and not report this.
[2691.74 --> 2695.34]  That's a, that's a big capability, uh, in that existing browsers today.
[2696.14 --> 2701.98]  Uh, it's not simple to deploy, but it is doable, right? Because you need to figure out how do I get
[2701.98 --> 2706.38]  these hashes and how do I inject them at the right place? But then one of the gaps that existed for a long
[2706.38 --> 2713.10]  time was, um, module imports. So SRI worked for top level scripts, but if you're building a JavaScript
[2713.10 --> 2718.62]  application and you're using an import, uh, you just could not pass in an integrity hash. Why?
[2719.34 --> 2725.26]  Well, because module imports came after sub resource integrity was designed. So it was just never,
[2725.26 --> 2730.30]  it was never a thing. Um, that was a pain point for us because we use module imports at Shopify. So we
[2730.30 --> 2737.34]  worked with Chrome and Safari to upstream, uh, some patches to get that supported for module imports.
[2737.82 --> 2743.74]  So the good news is that's now baked in, I believe as of May of 2024, I think when Safari shipped it
[2743.74 --> 2749.66]  in the, in their, in their release, uh, both Chrome and Safari support, uh, SRI for module imports. Like,
[2749.66 --> 2755.82]  so that's, that's one. Um, another thing that, uh, came up in our, uh, thinking when we were exploring
[2755.82 --> 2763.58]  CSP compliance and how do we make our law, our own life simpler is, uh, this idea of require SRI for.
[2764.46 --> 2771.50]  So what if you could express a content security policy that says, Hey, all scripts must have an SRI
[2771.50 --> 2779.34]  or some, or integrity hash. Gotcha. Right. And why is that useful? Well, then you can make, um,
[2779.98 --> 2785.26]  a strong claim that if you have that policy being enforced by the browser, then if for some reason
[2785.26 --> 2790.70]  you sneak through by accident or malicious act, a script that doesn't have it, they would just be
[2790.70 --> 2796.94]  rejected, right? Which today it would just execute normally, um, without any questions.
[2797.82 --> 2803.98]  And, uh, even though that might be hard to deploy in an enforcement mode, it could totally work and be
[2803.98 --> 2809.42]  really useful in a report only mode. So for those not familiar with content security policy, you have
[2809.42 --> 2814.38]  an enforcement mode and a report report only mode where you can get violations, which is incredibly
[2814.38 --> 2818.94]  useful because you could say, Hey, this is a policy I would like to enforce. What are the violations?
[2819.98 --> 2825.58]  So with the require SRI for you could deploy this in report only mode and say, great. Now I'm going to
[2825.58 --> 2834.14]  get reliable reports from the browser, from the wild for any time a browser detects that a script
[2834.14 --> 2840.86]  is missing an SRI capability, right? Um, this is great because sophisticated attackers
[2840.86 --> 2847.26]  would not emit these scripts on every single page load. They might target specific users or
[2847.26 --> 2851.90]  a class of user, or maybe they target specific browser, or maybe if it's an extension, it'll, it'll
[2851.90 --> 2856.62]  apply some sort of other heuristic, right? It's very hard to, this kind of mirrors our conversation on
[2856.62 --> 2863.58]  why ROM is important, real user measurement, gathering violation reports from real users gives you a much
[2863.58 --> 2871.50]  much better and reliable signal for where the problems are. So, uh, require SRI for is another
[2871.50 --> 2878.70]  capability that we've, uh, shipped into Chrome and that allows you to get violations on missing SRI
[2878.70 --> 2883.42]  attributes, which allows you to build an inventory of like, this is the list for me to burn down and
[2883.42 --> 2889.18]  figure out why. Right. And if anything changed, how do I, how should I react to it? Yeah.
[2889.18 --> 2897.10]  Yeah. Another example is, okay, great. Now we have these reports coming in. Uh, wouldn't it be nice
[2897.10 --> 2902.38]  if we could also get the hash of the content, right? It's today you would just get a report saying,
[2902.38 --> 2912.30]  Hey, I detected script from example.com slash X, Y, Z dot JS. But what was the content of that? Uh,
[2912.30 --> 2917.74]  you don't know, right? Wouldn't it be nice if you could also get a hash in the report such that you could,
[2917.74 --> 2923.58]  um, audited, um, audited and say, Oh, well maybe that's totally okay because the partner revved their
[2923.58 --> 2928.14]  version and it just happens to be the V2. I just put that, I put that into my approved list and
[2928.14 --> 2935.66]  everything's fine versus I have no idea if that was a compromised version or a legitimate version of
[2935.66 --> 2943.26]  the script. Interesting. So pardon my ignorance for a moment, but where does the reporting take place or
[2943.26 --> 2948.86]  post to the browsers doing the reporting? Is it correct? Who gets the report and how is it?
[2948.86 --> 2954.86]  The browser sends it off somewhere or? Yep. So on the wire, um, you would, when you emit a page,
[2954.86 --> 2961.42]  uh, you can define a content security policy or CSP policy in a header and you would define, you know,
[2961.42 --> 2966.70]  for script source list, for example, a list of origins from which you're allowed to fetch,
[2966.70 --> 2974.94]  um, for images and all the rest. You also have a report to target and a separate report to header
[2974.94 --> 2980.94]  that provides a specification for you specify the end point to where you want the report violation
[2980.94 --> 2987.10]  report to be reported. And you know, as good hygiene, that reporting endpoint should ideally be like a
[2987.10 --> 2994.70]  distinct origin, um, in all the rest, but you provide a destination. So you can find services that will do this
[2994.70 --> 2999.90]  for you, right? They'll just say, point your report to, to us, and we will provide a dashboard,
[2999.90 --> 3002.94]  which you can drill down reports. We will aggregate, we'll give you metrics,
[3003.50 --> 3007.74]  and all the rest. That's something that we do in house at Shopify. And I think many other
[3007.74 --> 3013.34]  large providers will do on their own. Uh, but you could outsource that problem, but just having the
[3013.34 --> 3020.70]  ability to even get the report with, Hey, um, a report has been emitted because the script is missing
[3020.70 --> 3027.98]  an integrity hash is by itself a really useful capability because otherwise you'd probably
[3027.98 --> 3032.06]  have to set up some sort of a crawling infrastructure that periodically checks your page and says,
[3032.78 --> 3036.78]  you know, I, I accessed this page from five different points on the globe.
[3036.78 --> 3037.90]  Right.
[3037.90 --> 3043.26]  Every 24 hours. And I observed that nothing has changed. Well, that's good, but we could do much
[3043.26 --> 3048.14]  better by just actually observing what the real users are seeing and getting the actual reports of
[3048.14 --> 3048.62]  violations.
[3048.62 --> 3058.14]  Gotcha. So this new one require SRI for would work in like manner as the CSP violations in terms of
[3058.14 --> 3058.62]  reporting.
[3058.62 --> 3064.62]  Right. So you would, you would, the, the CSP policy is require SRI for scripts, right?
[3064.62 --> 3070.70]  So you're saying all of my script resources must have a hash. And then you can configure that to
[3070.70 --> 3077.58]  be a report only policy such that it would still execute if the script is missing the hash, but you
[3077.58 --> 3083.26]  would get the violation fired in the background. And the browser has its own logic for prioritizing
[3083.26 --> 3087.10]  batching delivery and doing all of that, uh, to, to get you the report.
[3087.10 --> 3089.90]  Mm-hmm. Now do you deploy this one in Shopify?
[3089.90 --> 3091.26]  Yep.
[3091.26 --> 3091.82]  Yep.
[3091.82 --> 3095.34]  And do you use it in report mode or do you let lockdown mode or how do you use it?
[3096.62 --> 3105.26]  So for this one, it would be a report report mode. Uh, but it depends on how, like, it depends on the
[3105.26 --> 3109.58]  shape of your checkout and how much control you have for your first party or third party content.
[3110.22 --> 3115.98]  Just to double back on that for, for Shopify, we, uh, for our checkout, we enforce a CSP policy.
[3115.98 --> 3123.90]  Actually, let, let me run through the whole list. Uh, for our first party content, we have a well-defined
[3123.90 --> 3130.14]  process for vetting all the dependencies and a process for updates, auditing, to make sure that
[3130.14 --> 3135.02]  we provide some guarantees over, you know, if the library that we depend on has been compromised,
[3135.02 --> 3141.02]  how can we detect that? We have change management process for it. So this is the reviews, testing,
[3141.02 --> 3146.54]  CI, all the things that you would expect that allows us to create the inventory. We know from where it's
[3146.54 --> 3151.50]  served, which means that we can define a strict CSP policy that says you should only fetch from these
[3151.50 --> 3152.78]  sub origins that we trust.
[3152.78 --> 3159.42]  In our build step, we can inject the hashes, the SRI hashes for known content.
[3160.54 --> 3167.98]  And we can also emit the require SRI for policy to ensure that if anything else, for some reason,
[3167.98 --> 3173.42]  if we emit a missed some script that we would get a violation on that because we don't want to break
[3173.42 --> 3179.10]  checkout, but we want to be notified immediately. If those things are detected, then we can react to it.
[3179.10 --> 3185.18]  And we have our own reporting endpoint, which we aggregate, we look at the reports. This is a
[3185.18 --> 3188.46]  thing that merchants don't have to worry about because we do this work on their behalf.
[3189.10 --> 3195.90]  Right. And we can provide this guarantee over overall integrity. And then finally, we've protected
[3195.90 --> 3202.94]  the parent page, but the payment credentials page or the payment form itself is also isolated into its
[3202.94 --> 3208.22]  own iframe, just as it was before. So this is a defense in depth, right? We protected the parent,
[3208.22 --> 3213.90]  but we also have our own implementation of the iframe and like the full PCI compliance
[3213.90 --> 3215.18]  behind that particular form.
[3215.18 --> 3221.26]  Well, that's a lot of stuff for PCI compliance, Ilya. What happens with V5? How many years are you
[3221.26 --> 3222.14]  going to put into that one?
[3223.98 --> 3229.74]  I don't know. That's a great question. I'm pretty sure that V4 will keep us busy for a long while.
[3231.18 --> 3235.10]  Yeah. Because this is only section 6.4.3, right? That's all we're talking about right here.
[3235.10 --> 3238.70]  That's right. There's all the others.
[3240.78 --> 3245.34]  Okay. So interesting stuff. It sounds like you've solved some really
[3246.94 --> 3253.18]  difficult technical challenges in order to do this in a way that's not just compliant, but actually
[3253.18 --> 3257.42]  in the spirit of the compliance as well, like trying to actually make it more secure.
[3257.42 --> 3264.14]  What are some takeaways for listeners out there? Maybe they're doing their own checkout. Maybe they
[3265.02 --> 3270.78]  have compliance they need to do. Maybe they just want some more secure websites. What do you think
[3270.78 --> 3277.02]  they could be thinking walking away from this if they're not in the actual situation that Shopify's in
[3277.02 --> 3280.62]  and having to implement this stuff? What could they learn from this conversation?
[3281.74 --> 3289.58]  Yeah. I think the meta pattern and message takeaway here is broadly the integrity and security of
[3289.58 --> 3295.34]  first party versus third party content. We mix first party and third party in most contexts, but
[3295.34 --> 3302.14]  even outside of checkout, there are many surfaces. Let's say you have an admin surface or
[3304.62 --> 3311.42]  a privileged surface that you only want certain users to access and you want some sort of extensibility
[3311.42 --> 3317.50]  in there. So you want to bring in third party content or customization in all the rest. The pattern that
[3317.50 --> 3323.82]  we're describing with isolating third party content is a generic pattern that you can deploy there.
[3323.82 --> 3329.34]  So we use the same sandbox and technology in checkout. We use the same technology in our admin.
[3329.34 --> 3333.42]  So for merchants, we allow customizations and third party developers to bring in their custom
[3334.06 --> 3339.98]  UI and other aspects. As you can imagine, that's a very sensitive surface. Order data is there,
[3339.98 --> 3345.74]  customer data is there. You don't want to just open up a Pandora's box of injector arbitrary
[3345.74 --> 3354.30]  JavaScript because who knows where the data might travel. So the isolation primitive, it may be a
[3354.30 --> 3363.74]  remote DOM, it may be something else, but this way of thinking of isolating into either an iframe or a
[3363.74 --> 3368.14]  worker, I think is a pattern that we should be adopting more widely. And it has these additional
[3368.14 --> 3373.34]  benefits. You have better assurances about security, yes, performance as well, because you're isolating
[3373.34 --> 3380.38]  content and moving it off the main thread. You get to define the API contract. So you have better
[3381.82 --> 3386.62]  upgrade ability if you need to maintain that. And I think that's just something that we need to get
[3386.62 --> 3392.14]  better at on the web. Now, the challenge, I think for all of us and kind of as industry practitioners
[3392.14 --> 3397.18]  is to think through, boy, the worker is kind of this like naked environment.
[3397.18 --> 3402.86]  Mm hmm. We can probably figure out, we should think about how do we figure out some better set
[3402.86 --> 3407.34]  of APIs that where we don't have to reinvent the entire wheel, just as we did with, you know,
[3407.34 --> 3414.54]  at Shopify for great. Now I want to build a heat map thing. What does that mean? How do I mirror the
[3414.54 --> 3422.14]  entire stream of events from top level page into this isolated environment? I think we can do some
[3422.14 --> 3427.82]  thinking and innovation there. Very cool. Anything else that's on your mind that we haven't discussed
[3427.82 --> 3432.06]  in this context or honestly, in any developer context, I always love to hear your opinions
[3432.06 --> 3437.50]  on stuff. Anything else on your mind? I think one really interesting topic coming, coming back to
[3437.50 --> 3443.18]  the world of checkout and commerce is of course, agents and how agents will interact or how they might
[3443.18 --> 3450.54]  affect any of these behaviors. Oh, yes. MCP. Are you done with MCP? That's the newest acronym,
[3450.54 --> 3456.70]  model context protocol. It's burgeoning. Yep. Yep. MCP is definitely top of mind and we're
[3456.70 --> 3461.90]  looking at it intently. We're using it for a number of tools and internal services at Shopify.
[3461.90 --> 3467.34]  We're also considering if and how we should be exposing MCP as a, as a protocol and endpoint,
[3467.98 --> 3473.98]  as a service on behalf of merchants. So, so imagine you could have a merchant storefront as a remote
[3473.98 --> 3480.62]  MCP endpoint. But more broadly, like if you think of, let's imagine you interacting with an agent
[3480.62 --> 3488.30]  asking it, Hey, I'd like to have a pair of white sneakers, size 10, 15 to or 50 to a hundred dollar
[3488.30 --> 3493.74]  range. Please go find me a pair and check out under the hood. The agent might crawl the web,
[3493.74 --> 3498.46]  find the storefront, add to cart, head to checkout. And what does it do then as it's looking at a
[3498.46 --> 3503.50]  payment form? Is it a responsibility of the agent to hold onto your payment credentials? And what are
[3503.50 --> 3509.74]  the implications of that for entering? How does it enter those credentials? Are there any security
[3509.74 --> 3515.66]  and compliance problems or challenges in that? I think that's a wide open question that we as an
[3515.66 --> 3523.74]  industry are yet to figure out an answer. Is the human required in that loop? What if it's an
[3523.74 --> 3527.58]  accelerated checkout where maybe information is vaulted? Right. I think there's a range of
[3528.38 --> 3532.14]  questions and answers that we need to figure out in the space.
[3533.66 --> 3537.98]  What's your personal thought on is the human required in the loop? How do you feel
[3537.98 --> 3540.94]  confidence wise on removing the human from that loop?
[3540.94 --> 3546.30]  I think it's context dependent. I think there's definitely a class of commerce and types and
[3546.30 --> 3552.38]  certain types of transactions where I know exactly what I want. There's very low risk and it's kind of
[3552.38 --> 3559.50]  a predefined flow where I just say, look, I need another carton of milk. You know exactly what
[3559.50 --> 3563.02]  I'm looking for. You know where to shop and please go finish it. And I just want it to my front door.
[3563.98 --> 3569.90]  And then there is other types of experiences where maybe this is your first time engaging with a
[3569.90 --> 3577.18]  merchant. Maybe a merchant has a set of rules where they actually require you or require the agent to
[3577.18 --> 3584.54]  decelerate because, hey, for compliance reasons, I may need to verify your age or I need you to read
[3584.54 --> 3590.54]  this disclaimer on this product before you purchase it. Right. You can't just have the agent blindly
[3590.54 --> 3597.90]  ignore that context or click approve and then proceed with the transaction. So I think we're,
[3597.90 --> 3604.22]  we'll need to define some protocol or a shared mechanism to signal to agents that like, hey,
[3604.22 --> 3612.78]  in this particular case, I need you to pause and ask for human to either confirm or take over control
[3612.78 --> 3617.26]  and complete the transaction. There's so many questions there. I just don't feel like
[3618.14 --> 3623.98]  I even have the brain right now to analyze all the things that have to be considered. I'm glad that
[3623.98 --> 3629.18]  you're, are you going to be working on this for Shopify? Are you going to stay in the NPC island? What,
[3629.18 --> 3633.50]  what's next for you inside? Is this an active thing that you're thinking about for Shopify?
[3633.50 --> 3639.50]  It is definitely, um, definitely an active area of, uh, of exploration for us. That is one of the
[3639.50 --> 3644.06]  things, um, I'm looking with, um, our team and many of our partners who are building these agents.
[3644.06 --> 3649.34]  We're trying to figure out what is, what is the future of checkout where agents drive some meaningful
[3649.34 --> 3654.06]  portion of, of that experience? What does a good experience even look like, um, in that context?
[3654.06 --> 3659.18]  So I think those are all, um, very interesting and pertinent question given where we are today.
[3659.18 --> 3665.82]  Hmm. Well, I have to have you come back in a year or two and let us know what you end up building as
[3665.82 --> 3670.86]  you've, you figured it all out. You seem to have figured it out. At least this, this hairy technical
[3670.86 --> 3674.54]  problem has come to this new PCI stuff. So I'm sure you'll figure out something.
[3674.54 --> 3679.66]  Yeah. We'd love to be back. And at the rate that we're moving in AI world in a year or two for now,
[3679.66 --> 3682.06]  who knows what will be there. So.
[3682.06 --> 3690.70]  Yes. I'm trying to think of the most recent person who said six to nine months and LLM will be writing
[3691.66 --> 3695.50]  a hundred percent of code. So, I mean, who knows, man, maybe we'll be,
[3695.50 --> 3697.98]  you and I will be out on the street corner talking about this stuff.
[3697.98 --> 3701.18]  I doubt that is the case, but well,
[3701.18 --> 3702.38]  who knows?
[3702.38 --> 3708.86]  Yeah, me too. But you know, it's not a week goes by that somebody doesn't declare software
[3708.86 --> 3713.02]  engineering is dead or dying. So I had to squeeze that one in there.
[3713.02 --> 3716.70]  Yes. I think, I think what we're actually saying is the definition of what software engineering is,
[3716.70 --> 3723.18]  is changing, right? I am constantly amazed by what, um, AI is capable of doing in terms of
[3723.18 --> 3729.18]  software development, but I'm also constantly surprised by the silly and stupid mistakes that it makes.
[3729.18 --> 3731.74]  And oftentimes those mistakes are actually due to
[3731.74 --> 3739.02]  misunderstanding or lack of poor definition of the problem that is being solved. It's kind of
[3739.02 --> 3742.70]  putting the mirror back to yourself, right? Because oftentimes I'll find that like, actually,
[3742.70 --> 3746.70]  you know what, you did exactly the right thing, the way I expressed it, but that's not what I meant.
[3746.70 --> 3750.14]  And I didn't even know what I meant when I typed it, because now that I've seen the mistake,
[3750.14 --> 3755.10]  I understand what I was actually trying to get to. So it is this like art of defining the problem
[3755.10 --> 3761.02]  and rubber duck programming. And I think we're heading more and more towards the world where
[3761.02 --> 3766.38]  we're actively collaborating instead of hands on keyboard typing, uh, if statements.
[3766.38 --> 3771.58]  Yeah. The best rubber duck programmers might be the best programmers of the future. It's the
[3771.58 --> 3775.34]  ones who can just talk it out the best, you know, figure it out as you go. All right,
[3775.34 --> 3780.06]  Elia, appreciate you coming on the show and chatting with us and looking forward to having you back soon.
[3780.06 --> 3781.26]  Thank you, Jared.
[3784.78 --> 3790.22]  Okay. So it turns out securing e-commerce checkouts has never been more complicated,
[3790.22 --> 3796.14]  but thankfully brilliant engineers like Elia and his team at Shopify are putting in the work. And
[3796.14 --> 3801.66]  some of that work is making its way back into the web platform. I love when that happens. And when you
[3801.66 --> 3807.58]  think about it, the complicated nature of it all makes sense. The stakes have never been higher. I read the
[3807.58 --> 3815.18]  other day that last year e-commerce sales soared to a record 1.2 trillion dollars. That's a lot of
[3815.18 --> 3821.58]  moolah being transferred. And if you can hack it, well, you can jack it. So yeah, it's complicated for
[3821.58 --> 3828.46]  a good reason. Let's give one more thanks to our sponsors of this episode, Retool, Augment Code,
[3828.46 --> 3834.46]  and of course, Fly.io. Check out their wares to support their work, which supports our work,
[3834.46 --> 3841.10]  which we appreciate. Thanks also to our beatmaster in residence, Breakmaster Cylinder. Did you know
[3841.10 --> 3846.38]  our next full-length album is almost ready? And I'll tell you right now, it's called After Party.
[3846.38 --> 3851.10]  And I'll also tell you right now that I've been bumping it all week. I dig it. Hopefully you will
[3851.10 --> 3857.34]  too. Soon. So soon. All right, that's all from me, but we'll talk to you again on Changelog and Friends
[3857.34 --> 3859.26]  on Friday. Bye, y'all.
[3887.34 --> 3906.70]  Bye, y'all.
