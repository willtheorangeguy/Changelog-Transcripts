[0.00 → 4.88] Mixed reality or virtual reality or augmented reality is perfect examples of applied AI.
[5.12 → 9.92] So when you're doing hand tracking, for example, that we do in HoloLens, you can imagine that it's
[9.92 → 13.64] literally looking at your hands and saying, okay, this finger is pointing one particular way,
[13.72 → 18.16] it's pointing that way, or I'm grasping my hand here. And to even create a data set, of course,
[18.18 → 23.06] you can capture a lot of hand angles, but you can also create different 3D orientations of a hand
[23.06 → 28.30] and have the label data set. So you can train your hand detection models and so forth. And even
[28.30 → 32.88] all these devices in HoloLens, you can speak to it. So there's a lot of onboard speech recognition
[32.88 → 38.20] and so forth. So there is, one is, of course, it's a very good example of applied AI for us.
[38.34 → 42.88] But the second one is for our customers and our developers. It is actually the simplifying and
[42.88 → 46.32] accelerating the development experience and really at the end of the day, helping customers realize
[46.32 → 47.62] more value out of these technologies.
[49.76 → 54.52] BAM with 4Change Log is provided by Vastly. Learn more at Fastly.com.
[54.52 → 59.10] Our feature flags are powered by Launch Darkly. Check them out at LaunchDarkly.com.
[59.36 → 64.58] And we're hosted on Linde cloud servers. Get $100 in hosting credit at Linode.com slash
[64.58 → 65.12] Changelog.
[65.76 → 70.94] What up, friends? You might not be aware, but we've been partnering with Linde since 2016.
[71.26 → 76.12] That's a long time ago. Way back when we first launched our open source platform that you now
[76.12 → 83.42] see at Changelog.com. Linde was there to help us and we are so grateful. Fast-forward several years
[83.42 → 88.92] now and Linde is still in our corner behind the scenes helping us to ensure we're running
[88.92 → 94.40] on the very best cloud infrastructure out there. We trust Linde. They keep it fast and they
[94.40 → 101.30] keep it simple. Get $100 in free credit at Linode.com slash Changelog. Again, $100 in free credit
[101.30 → 104.60] at Linode.com slash Changelog.
[104.60 → 125.92] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[125.92 → 130.48] and accessible to everyone. This is where conversations around AI, machine learning,
[130.48 → 134.84] and data science happen. Join the community and Slack with us around various topics of
[134.84 → 139.76] the show at Changelog.com slash community and follow us on Twitter. We're at Practical AI FM.
[146.32 → 152.16] Welcome to another edition of the Practical AI podcast. My name is Chris Benson. I'm a principal
[152.16 → 156.96] emerging tech strategist at Lockheed Martin. And with me as always is Daniel Whiten ack, a data
[156.96 → 161.90] scientist with SIL International. How's it going today, Daniel? It's going great. I think we
[161.90 → 169.30] discussed when we recorded last week, which was pre-US Thanksgiving, our plans for Tour for
[169.30 → 175.36] Thanksgiving, which I had. I'm not sure if you partook as well. Furthermore, I did. So anyone who listens to
[175.36 → 179.68] us regularly hears Daniel and I talk about our plant-based meals, and I'll take a two-second
[179.68 → 185.44] divergence. I had an interesting entry into Thanksgiving dinner that has nothing to do with AI ML whatsoever.
[185.44 → 191.64] We were just about five, 10 minutes from sitting down, and I got a call from a neighbour saying,
[191.86 → 197.10] I have a large black snake in my house. Can you come help me? And so anyone that's listened to us
[197.10 → 202.14] knows I'm the animal fan. Yeah. And you're on call for that sort of thing, I think. I am. So I like
[202.14 → 206.94] totally separate from all this, what we're talking about today. I do a bunch of animal stuff and I
[206.94 → 211.64] actually run a snake hotline. How weird is that? Do you know anyone else that runs a snake hotline?
[211.64 → 218.28] So I get the call. I go, and I have a neighbour with a large black king snake in their basement
[218.28 → 224.44] and they were very upset because they were not very snake savvy people. And so I calmed them down.
[224.52 → 230.46] We got the screams to stop, and I picked the king snake up and carried it delicately outside,
[230.58 → 234.88] released it, educated them along the way as the screaming stopped.
[234.88 → 237.62] You made an unexpected house visit on Thanksgiving.
[238.14 → 243.50] It was. It was. And then I dashed home just in time to sit down for Thanksgiving dinner. So it was
[243.50 → 245.64] a memorable Thanksgiving dinner in that way.
[245.66 → 246.30] Yeah, that's great.
[246.30 → 249.08] A little odd story that goes with it.
[249.24 → 255.60] Yeah, that's awesome. Yeah. Well, we have some interesting things to discuss today and including,
[255.84 → 262.02] you know if you were to have taken a picture of that experience, you might've wanted to come up
[262.02 → 266.72] with a caption for it and that might've been somewhat difficult. That's one of the tasks
[266.72 → 268.10] that we're going to discuss today.
[268.72 → 269.02] Indeed.
[269.42 → 276.28] Yeah. And we're really excited to have with us Bharat Sadhu, who is the director of Azure AI
[276.28 → 279.32] and Mixed Reality at Microsoft. Welcome, Bharat.
[279.74 → 281.30] Thank you. Thank you for having me.
[281.64 → 286.86] Yeah. If you could just give us a little bit of an idea about your background and how you got
[286.86 → 288.70] into AI and what you're doing now.
[288.70 → 297.42] Yeah, sure. By the way, just for Thanksgiving, even we had a plant-based Thanksgiving this last
[297.42 → 299.32] week. So we joined. We joined.
[299.46 → 300.06] Ah, good.
[300.10 → 300.76] No snakes though.
[300.94 → 305.10] You have any, any recommendations on that front for our listeners? We always try to
[305.10 → 307.36] throw in an occasional recommendation.
[307.72 → 312.94] You know, I, we just tried like, so we tried to reduce the amount of meat we eat, my wife and I.
[313.02 → 318.54] So we tried it this Thanksgiving, and we just cooked up some new recipes. The green beans recipe was,
[319.26 → 325.28] it turned out extremely well. It was spicy. And, you know, it was just normally a different kind
[325.28 → 329.58] of Thanksgiving food, a little bit of spice in it. But yeah, I don't know that we just copied some
[329.58 → 336.10] recipe off on the web. So I can, I can share that with you. And yeah, it's good. I don't know that
[336.10 → 341.74] mine ever look quite as tasty as the picture on the recipe, but sometimes, you know, just finding
[341.74 → 344.08] those recipes online that it works out pretty good.
[344.76 → 349.36] You know, before long, because this is not a new topic. We have had other folks on the
[349.36 → 353.78] show talking about this on the side before we got in the main topic. Pretty soon, we're
[353.78 → 359.20] going to need our own conference. It'll be like the plant-based AI, ML and data science
[359.20 → 361.64] practitioner conference. Yeah.
[361.64 → 362.56] Just saying.
[363.44 → 367.54] Yeah. It'll describe to you what you cooked and what you could have cooked. And actually,
[367.62 → 370.66] cooking is kind of like machine learning, right? It's like not just the ingredients,
[370.74 → 373.82] it's how you shape them and all the work that goes in it.
[373.82 → 377.78] I'm glad you bring that up. Actually, it's one of my favourite examples that I give when
[377.78 → 384.94] I'm teaching workshops is a lot of industrial AI applications are really more like, you know,
[385.00 → 390.94] using a recipe and bringing your ingredients to it rather than sort of designing the recipe
[390.94 → 396.86] itself. Right. And, you know, maybe that gets into some of how people use Azure AI and other
[396.86 → 401.96] things which we can talk about. But yeah, before we get into that, I'd love to hear a little
[401.96 → 405.64] bit about your background and how you ended up where you're at right now.
[406.02 → 410.52] Yeah. So, you know, I've been at Microsoft for a bit over 10 years, close to 11 years now. But,
[410.88 → 415.26] you know, I'm a computer engineer by training. My first job was a computer engineer writing code.
[416.02 → 419.14] And, you know, as before we got on the call, we were talking with, you know, Chris was Lockheed
[419.14 → 424.70] Martin. So my first job was this company of National Instruments. And, you know, I started as an
[424.70 → 430.00] engineer, but then I moved out to work with customers in our field engineering and sales division back
[430.00 → 434.92] then. Are they the ones that make Lakeview? Is that the... Yes, that's right. Lakeview. Okay.
[435.10 → 439.76] Yeah. That's my experience with National Instruments. For those that don't know, Lakeview is like
[439.76 → 445.80] software that helps you interface with all sorts of different instruments and circuits and design
[445.80 → 450.10] various things. And yeah. Anyway. Yeah. And some of the work, you know, like, so if you're an
[450.10 → 455.24] engineer by training, you know, and you start working with customers like Sikorsky making the Blackhawks
[455.24 → 460.30] helicopter, United Technology, the Fuel Cell and Pratt & Whitney making the, you know, the engines
[460.30 → 467.38] for, I think, a lot of fighters, including the F-35 now. Correct. It was quite fascinating because
[467.38 → 470.82] back in the day, not that many companies were collecting a lot of data, but these companies were
[470.82 → 475.64] collecting a ton of data and kind of building, you know, hardware in the loop testing and those
[475.64 → 480.16] kind of things. So it was a fascinating time. And, you know, so that was my kind of like early
[480.16 → 486.54] career learnings working with folks building literally jet engines and working with tons
[486.54 → 490.02] and tons of data and trying to make sense of them. We actually focus a lot on hardware
[490.02 → 494.26] in the loop testing, which is before you should build something, and you want to, you know,
[494.30 → 498.92] instrument it all up, you want to maybe do some simulation. So, you know, Math Lab and Simulink
[498.92 → 503.78] were common players we worked with, competed with also back in the day. And, you know,
[503.84 → 508.06] nevertheless, I did that and got my MBA. Then I joined Microsoft and in Microsoft, my career
[508.06 → 513.76] has mostly been commercializing incubation businesses. So first was Unified Communications,
[513.96 → 518.92] which is funny, we're talking about over Zoom right now. But 11 years ago, you know, at
[518.92 → 523.94] least for Microsoft, it was a newer entry back then. And then, you know, I joined our IoT,
[524.38 → 529.54] Azure IoT team. We were launching our Azure IoT offering and then the big data space. In the
[529.54 → 534.54] last three years, really the AI space and very recently the mixed reality. And the common trend
[534.54 → 540.44] has been commercializing these very emerging new technologies and, you know, making it a viable
[540.44 → 545.98] business value proposition for companies, for our partners and for our customers, making it easy for
[545.98 → 551.36] them to actually benefit from these technologies. You know, it's pretty interesting. I think a lot
[551.36 → 558.28] of companies that are getting into AI, like whatever AI-based system they're creating might be one of
[558.28 → 563.96] those things that they're incubating within their own organization. So do you have any insights from your
[563.96 → 569.82] experience kind of productizing these different, you know, incubated ideas into actual offerings?
[569.86 → 575.44] Do you have any insights for those out there that are maybe their AI-based system? Is their internal
[575.44 → 582.46] incubation project any suggestions for them or advice? Yeah, you know, a comment, like first,
[582.66 → 589.06] you know, technologies come and go, you know, deep neural networks, a fancy today will be quite passé
[589.06 → 593.70] in a few years time, right? So like, just like in reinforcement learning is kind of coming into
[593.70 → 597.88] some areas, but these are just technology. So never please get fascinated by technology.
[598.54 → 603.42] And at least for those of us who work in technology companies, have to be very careful of that,
[603.68 → 607.20] because we get super excited about new techniques. It really is actually at the end of the day,
[607.48 → 611.68] business has not changed. You know, we have customers, and we have to serve them better.
[611.68 → 618.26] And we have competition, and we have to provide better offerings at the competition. So being
[618.26 → 623.48] super grounded, whether a project is going to help dramatically reduce cost, improve operations,
[623.56 → 628.56] or increase revenue is the most fundamental starting point. And, you know, I have seen, you know,
[628.66 → 634.48] I think we've all have a lot of organizations have incubation or innovation offices, which is great.
[634.84 → 639.42] But, you know, you know, as we work with customers, it's always like, okay, what is the core business
[639.42 → 647.92] need? And more importantly, have the key stakeholders bought into it upfront. And then they've signed up
[647.92 → 653.50] for maybe a year-long project, or maybe sometimes longer, to prove out whether this kind of venture,
[653.62 → 658.44] in this case, AI, for this particular application, is actually going to provide value for the business
[658.44 → 665.50] or not. So just setting up the project in a very methodical way, with key stakeholders bought in
[665.50 → 671.10] all the way up front, and then having regular meetings and making sure we have the KPIs identified
[671.10 → 676.36] or improving them as we go through it is super important. You know, so that'll be the one thing
[676.36 → 680.46] we'll say, like at Microsoft, we kind of make sure we stay true to that at the same time, you know,
[680.48 → 685.14] for us, we have the luxury, like with some other companies like Google and Apple and Amazon,
[685.76 → 689.78] to do a lot of just pure research. But a lot of companies in the world do not have the
[689.78 → 696.16] you know, the luxury sometimes. So especially if the core competency is not technology or AI,
[696.22 → 701.12] machine learning. So for these companies, it's our, I think, duty to help them kind of walk through
[701.12 → 704.46] how they can evaluate projects, not just technologies.
[705.02 → 705.14] Gotcha.
[705.30 → 707.52] So I'll just go back to kind of going back to business basics.
[707.80 → 711.88] When I was introducing you, and I was mentioning your title is one, one thing I was wanting to follow
[711.88 → 717.68] up on is, is, as part of your title is mixed reality. And we hear about all sorts of different
[717.68 → 723.76] types of, you know, something reality, virtual reality, augmented reality, and, but what is
[723.76 → 726.80] mixed reality, or at least how does, how does Microsoft define that?
[727.20 → 732.00] Yeah, sure. So mixed reality for us, you know, and I think X reality is a new term that's also
[732.00 → 736.94] started kicking around. But basically, like, if you look at our, the way we interface with our
[736.94 → 741.86] phones or laptops, it's a 2D screen. And then you have things like Oculus Rift or Windows virtual
[741.86 → 747.38] reality headsets. And I got an Oculus a few weeks back. I love it. And Quest, sorry, Oculus.
[747.38 → 751.78] So it's a virtual reality. So there you're in a virtual reality environment, but you're
[751.78 → 756.22] in a separate environment. You're totally removed from the physical space. And then you've augmented
[756.22 → 760.18] reality, which HoloLens is an example. Magic Leap is another example where you can actually
[760.18 → 765.06] see through, and you can see holograms. So you can have presence of the world around you,
[765.06 → 772.58] as well as virtual elements in it. Now, mixed reality is, you know, it's a term that spans
[772.58 → 776.98] augmented and virtual reality. Because what you'll see happening more and more, and even with
[776.98 → 781.38] Quest, I was quite impressed to see, you can actually see through and see the augmented
[781.38 → 786.82] reality. So from a development platform perspective, you should not have two separate set of tools
[786.82 → 791.78] and development environments and, you know, Unity for this and Unreal for that. You really
[791.78 → 797.38] want to have a consistent development platform, a consistent ecosystem. And really for customers,
[797.38 → 802.10] you use these technologies. Some like, well, of course, have a better experience in virtual reality,
[802.10 → 806.26] like gaming. But for a lot of like industrial commercial use cases, augmented reality is much
[806.26 → 810.10] more effective. But they also have a seamless experience through these different devices. So
[810.10 → 816.10] mixed reality, as a term really is meant to span the world of virtual reality and augmented reality.
[816.50 → 820.58] And really say it's a common development platform and a common user experience. It's really more of a
[820.58 → 824.50] a term at this point, but it is meant to bridge the two different worlds right now.
[824.50 → 829.54] It sounds like kind of that that element of common has a lot to do with it in terms of spanning. So
[829.54 → 834.90] Yes, would it be fair to almost say it's kind of taking augmented reality and applying tooling,
[835.38 → 842.58] common tooling across so that your productivity is improved without some of the natural distinctions on
[842.58 → 847.38] the two sides of it? Absolutely, yes. So if you're a developer, you don't have to learn two separate
[847.38 → 854.50] types of development stacks, and so forth, right? Some there, of course, be some nuances, right?
[855.06 → 860.98] But more and more, as much as we can make it easier for customers to go from an iOS or a phone-based
[860.98 → 866.90] augmented reality system to really like holographic, like all a HoloLens kind of experience to
[866.90 → 871.62] even a virtual reality experience, and the developers don't have to learn a different stack every single
[871.62 → 876.18] time, different set of tools every single time. I think that's added a value to the ecosystem.
[876.18 → 880.34] So that's one thing. As an end customer also, we're not there yet, but we have a consistent
[880.34 → 885.14] experience, and they have a consistent experience through the different devices and so forth.
[885.78 → 890.90] But yeah, mixed reality is basically trying to say is a bridging of this virtual reality and
[890.90 → 895.70] augmented reality worlds. And is that where the kind of common thread with the other things you're
[895.70 → 901.94] involved with in terms of the Azure AI platform? I know there's, you know, just from my own experience,
[901.94 → 909.94] so vastly different number of environments that people use for developing AI. Are part of the
[909.94 → 915.94] goals with the Azure AI platform similar in the sense of bridging some of those and creating a unified
[915.94 → 916.90] development experience?
[916.90 → 923.22] Yeah, also like AI is, I would say, a much more mature place than mixed reality or AR so far. But
[923.22 → 927.06] yes, I think there's a common, like, you know, basically just simplifying the developer experience
[927.06 → 932.58] is a common thread, for sure. The other thing is also, by the way, mixed reality or virtual reality
[932.58 → 937.78] or augmented reality is perfect examples of applied AI. So when you're doing hand tracking,
[937.78 → 942.90] for example, that we do in HoloLens, like you can imagine that it's literally looking at your hands and
[942.90 → 947.70] saying, okay, this finger is pointing one particular way, it's pointing that way, or I'm grasping my
[947.70 → 953.54] hand here. And to even create a data set, you know, of course, you can capture a lot of hand angles,
[953.54 → 959.06] but you can also in a 3D studio like Maya or something, create different 3D orientations of a hand
[959.06 → 965.06] and have the label data set. So you can train your hand detection models and so forth. And even all these
[965.06 → 970.18] devices and HoloLens, you can speak to it. So there's a lot of onboard speech recognition and so forth.
[970.18 → 975.86] So there is, one is, of course, it's a very good example of applied AI for us. But the second one
[975.86 → 980.02] is for our customers and our developers. It is actually the simplifying and accelerating the
[980.02 → 984.34] developer development experience. And really, at the end of the day, helping customers realize more
[984.34 → 990.66] value out of these technologies. So as you describe it that way, and would it be fair to say if you take
[991.22 → 996.74] applied AI, you know, meaning deep learning, reinforcement learning, things like that, and enabling
[996.74 → 1002.50] the mixed reality environment or experience with these technologies. And that becomes kind of the
[1002.50 → 1007.46] use case, if you will, for the applied AI as an enablement technology. Is that a fair way of
[1007.46 → 1011.62] talking about the relationship between them? Yeah, yeah, absolutely. And of course, not every
[1011.62 → 1017.86] single application needs to have the customer or the partner build an AI element to it too. But like,
[1017.86 → 1023.38] you know, we had this example in, I believe it was Disney, where they actually had a depth sensor,
[1024.10 → 1029.06] sensing people walk up to a screen. And I think they were doing the stranger things. Yes, they were
[1029.06 → 1032.66] doing the stranger thing enactment. And then the monster of the stranger thing will come out and say,
[1032.66 → 1038.02] who are you? You'll say your name, it will recognize, they will use speech to text or speech on
[1038.02 → 1043.62] recognition to know, to understand your name, but then do modulation of the speech and speak to text your
[1043.62 → 1048.02] speech to speak back to you and to ani scare you and so forth. So there you actually have blending of AR
[1048.02 → 1053.06] and AI from a customer perspective too. So, you know, right now, these are two distinct businesses
[1053.06 → 1058.10] for us. You know, some places they overlap when it comes to customer use cases, but a lot of the way
[1058.10 → 1062.98] we take these technologies to market has a lot of commonalities of kind of going from super early
[1062.98 → 1073.46] incubation into commercial businesses for us. So there's a business connectivity tissue also.
[1073.62 → 1084.90] So, you know, change log plus is the best way for you to directly support practical AI.
[1084.90 → 1089.62] Join today and unlock access to a private feed that makes the ads disappear,
[1089.94 → 1095.62] gets you closer to the metal and help sustain our production of practical AI into the future.
[1096.50 → 1102.66] Simply follow the change log plus link in your show notes or point your favourite web browser to
[1102.66 → 1108.82] change log dot com slash plus. Once again, that's change log dot com slash plus.
[1108.82 → 1112.66] Change log plus is better.
[1112.66 → 1142.50] So, Bart, I'm kind of interested, you know, while we're talking about the Azure AI platform to dig in a bit to what developing AI in the cloud looks like now.
[1143.14 → 1155.94] So in its very sort of raw form, I imagine people might think, oh, I could spin up a cloud instance or a virtual machine, maybe attach a GPU to that and do some AI things.
[1155.94 → 1163.54] But of course, each cloud provider has developed a whole suite of different things that, you know, aid AI development.
[1163.54 → 1166.50] What does that picture look like in Azure AI right now?
[1166.50 → 1169.70] Yeah. So, you know, our AI stack.
[1169.70 → 1172.90] Do you mind if I just explain what our how we take the market?
[1172.90 → 1173.70] Yeah, please do.
[1173.70 → 1174.10] What Azure is?
[1174.10 → 1174.50] Absolutely.
[1174.50 → 1174.90] Yeah.
[1174.90 → 1181.06] So first, you know, like, you know, there's a ton of innovation in AI in the open source world, which is awesomeness.
[1181.06 → 1186.26] So, you know, we our goal is to make sure we can provide that to our customers in a more packaged fashion.
[1186.26 → 1190.50] We also have a ton of research centres around the world. We have eight research centres.
[1190.50 → 1203.86] And the work they do is really fine-tuning and developing algorithms, you know, and their charter has really been to kind of like say, OK, let's go and build the best text to speech or speech to text or image captioning that we cover later on techniques.
[1203.86 → 1210.26] Now, these are researchers and PhDs in machine learning. You know, we have more of those now than we used to have maybe many years back.
[1210.26 → 1215.22] But, you know, they specialize in really deep like machine learning space.
[1215.22 → 1218.90] We take all the work they do, and then we bring it to Azure AI.
[1218.90 → 1231.22] And our goal in Azure AI is to use all the open source technologies available, all the work we're doing in that space too, and taking all the research milestones and baking them on a platform that we can give to developers and data scientists.
[1231.22 → 1239.22] So then they can use it from a simple, no cost free API call to kind of doing highly high scale reinforcement learning techniques.
[1239.22 → 1253.62] We also, by the way, test this stuff in our own products, and we have the I think, we're just lucky to have many different types of endpoints from teams, which if you were to join a team session now, you can do transcription of all the calls.
[1253.62 → 1257.62] They can do recording and transcription and translation, right?
[1257.62 → 1259.62] So all that's powered by Azure AI.
[1259.62 → 1270.34] Within PowerPoint, if you've used it recently, there's something called PowerPoint designer that looks at your PowerPoint bullet points and says, okay, hey, maybe you want to actually have a better representation of the slide.
[1270.34 → 1275.86] And it's really using Azure machine learning under the covers to do all the inferencing and give you those recommendations.
[1275.86 → 1279.94] And even Xbox, you know, the holiday season's here.
[1279.94 → 1284.34] But if you have an Xbox, if you log in, you're given a personalized screen.
[1284.34 → 1287.06] So if you log in to any other creates, you'll get a different dashboard.
[1287.06 → 1295.54] And that's powered by Azure AI and a service called Personalized that uses reinforcement learning on behind the scenes to do very personalized recommendations for folks.
[1295.54 → 1297.78] And the same technology is available to developers.
[1297.78 → 1304.26] So our approach to bringing AI to developers and data scientists is we take things in the open source world.
[1304.26 → 1307.62] We, of course, do our own research, and then we package it.
[1307.62 → 1313.22] And the real goal is to make it usable for customers, whether they're very professional data scientists.
[1313.22 → 1323.70] So give them access to, you know, the best collaborated notebook environments we can with highly scalable compute so they can do the really highest end training work they need to do.
[1323.70 → 1332.58] All the way to simple APIs that any developer can call using multiple, any other language of the choice and add AI to the application in a very simple fashion.
[1332.58 → 1341.06] And then what we have also done recently is we started creating what we call scenario specific app services, and we can get into that.
[1341.06 → 1359.94] A good example would be a metrics advisor where we have anomaly detection models running behind the scenes, but they also have a bunch of other logic around them to ingest data from multiple time series sources of data, to do root cause analysis, and to have composable UX elements that a developer can embed in the application.
[1359.94 → 1371.30] So if they want to do more of metrics monitoring, we don't just give them a model, but we give them a higher level, still a past service that does a lot of the other work and the other business logic for that thing.
[1371.30 → 1373.30] So that really becomes a platform.
[1373.30 → 1377.70] So at the base, we have Azure Machine Learning, which is used to train machine learning models.
[1377.70 → 1380.50] On top of that, we have customizable AI models.
[1380.50 → 1382.42] We call them cognitive services.
[1382.42 → 1385.62] Those are the speech, vision, language, and so forth.
[1385.62 → 1393.78] And then on top of that, we have a set of services that are really tuned for separate kind of scenarios like form recognition to metrics, monitoring, and so forth.
[1393.78 → 1396.42] And that's really a stack for Azure AI.
[1396.42 → 1401.46] We do go one step beyond that, and we have a platform called Power Platform.
[1401.46 → 1403.62] I'm not sure if you are aware of that.
[1403.62 → 1406.26] It is basically a platform for business users.
[1406.26 → 1408.98] It's a no code, low code environment.
[1408.98 → 1413.70] And really allow citizen developers really to go ahead and design applications.
[1413.70 → 1425.86] So all the Azure AI tech that I described is provided in a low code, no code way in this environment for anybody with a citizen developer to build AI into their applications without having to write code.
[1425.86 → 1426.66] That's fantastic.
[1426.66 → 1435.58] So first, I want to say regarding my next question, you've actually answered it in a fantastic format in kind of going through a lot of the benefits.
[1435.58 → 1440.98] But I also want to kind of distill it a little bit because so much of our audience is our practitioners.
[1441.22 → 1441.78] That's right.
[1441.78 → 1442.88] That are engaged in AI.
[1443.34 → 1453.44] And it is very, very typical for them to be in an environment where they're going to engage in a project, and they may have access not only to Microsoft, but competitors as well.
[1453.44 → 1455.82] And they're trying to justify that.
[1456.08 → 1462.92] If a practitioner has just listened to this episode, and we have more to go, obviously, but they're like, I want to do Microsoft AI on Azure.
[1463.38 → 1473.48] How would you differentiate it or how would you recommend they differentiate it for their manager or whoever they are having to report back to say, I definitely don't want to go with the other guys.
[1473.52 → 1474.36] I want to go with this one.
[1474.48 → 1475.46] How do you position that?
[1475.82 → 1482.48] Yeah, first, I must just say it's better for the AI field if the customers go with anybody, and they do an amazing AI project, right?
[1482.48 → 1482.92] Understood.
[1483.70 → 1488.36] I just want to acknowledge that, like, look, they have great competition, and that's great for the industry.
[1488.82 → 1491.36] And we're excited to play a role in this thing.
[1491.64 → 1500.50] But what guides us is our core three main investments, which, you know, we've had the fortune of working with multiple enterprises over many, many decades as a company.
[1500.78 → 1503.82] So we really hone into kind of making things enterprise-grade.
[1503.90 → 1505.32] So it really breaks down into three main things.
[1505.32 → 1516.40] First, it's making sure we can give the tools to developers and bring all the heritage of IDE tools and so forth on their terms, which means they can use the tools and frameworks of the choice.
[1516.40 → 1520.26] Whether they're professional data scientists, they love Jupyter notebooks, right?
[1520.46 → 1523.28] And then they want to use TensorFlow or PyTorch, great.
[1523.52 → 1540.36] But then have it optimized for the high-scale training, the kind of work we do with OpenAI, for example, and give them really fleets of very high, powerful, you know, infrastructure, computer infrastructure, which is just not GPUs, but also the networking layer for them to be able to do training very cost-effectively at the end of the day and highly reliably, right?
[1540.36 → 1551.10] But that's for what I would call the most more professional practitioners, right, who are really looking for tooling to do ML in a scalable, reproducible fashion.
[1551.66 → 1561.98] And that's really the Azure machine learning layer where our investments on making that really robust machine learning platform on the cloud, the play layer, you know, is really resonating with the customers.
[1562.30 → 1566.66] But the second one would be for customers who are not deep machine learning experts.
[1566.66 → 1573.88] And for them, like, it's easy to say, hey, you can have an API call, and you can have an AI model in your application.
[1574.34 → 1576.24] But the AI model has to be perfect.
[1576.90 → 1580.24] Otherwise, it will not, you know, it will work, but it will work in a bad way.
[1580.66 → 1589.68] So our commitment to quality, whether it's speech-to-text or text-to-speech, or you're getting our Turing models, which are very large-scale models, right, but available through an API call.
[1590.32 → 1593.98] So your language or text analytics is very high fidelity.
[1593.98 → 1596.34] And then also the high-end services.
[1596.46 → 1604.92] So it's just not having models, but ability to kind of, like, get to market faster for form recognition and other scenarios like video indexing and so forth.
[1605.56 → 1611.24] You know, we just have the services that, you know, a lot of times our competitors sometimes don't have it at this level we do.
[1611.24 → 1621.02] And be able to kind of provide this level of different various, various levels of access points for developers to work on, but work on one environment together.
[1621.46 → 1622.20] So that's one thing.
[1622.30 → 1632.74] Other two things I would just say, which I think we sometimes take for granted, but it's super valuable for our customers is really baking them and making them enterprise-grade.
[1632.74 → 1647.00] Like, it might sound boring, but things like Net and, you know, having ability to run these in, like, you know, environments that are highly regulated and having the certifications, having all the services and models be certified, you know, and so forth.
[1647.10 → 1648.08] This goes a long way.
[1648.08 → 1660.08] And last one, which, you know, has surprised us too, is our commitment to responsible AI is proving us to kind of, like, allow customers to take AI and use it in their applications much more effectively.
[1660.42 → 1668.52] So we have long, not just principles, but even, like, tooling that we provide to our customers and guidance that we provide to apply AI responsibly.
[1668.98 → 1670.84] So really, those are the three things.
[1670.84 → 1680.98] One is, like, allowing customers to kind of get access to AI on their terms, whether the professional data scientists or just developers who don't have machine learning expertise at all, but want to get access to AI.
[1681.56 → 1685.20] Second, giving them an enterprise-grade fashion so they can deploy with confidence.
[1685.68 → 1691.90] And third one, also giving them responsible AI, not just guidance, but also tools and capabilities to do it.
[1692.20 → 1698.96] And having it all built into our products, not just you can go to this doc here, you can go to this GitHub repo there.
[1698.96 → 1701.44] It's all available as part of our platform.
[1701.58 → 1703.24] That was a great explanation.
[1703.50 → 1713.10] You mentioned along the way OpenAI, and I know that Microsoft has an exclusive relationship on GPT-3, which obviously the whole industry is excited about with OpenAI.
[1713.64 → 1718.38] I'm assuming that at some point that becomes pretty normally accessible via Azure.
[1718.78 → 1722.60] Anything you can share on that, along where that's going to go or what we should expect?
[1723.00 → 1725.80] Yeah, you know, we're still working with them on a lot of these things right now.
[1725.80 → 1734.12] Like right now, what we want to make sure is we can enable OpenAI to really break through AI research and to give them amazing cloud resources.
[1734.26 → 1742.14] The things we spoke about, I think we have now the fifth-largest supercomputer, maybe probably the first one in the cloud that they access to build these models.
[1742.84 → 1747.66] You know, these are about 300,000 CPU cores, 10,000 GPUs, and the networking layer that goes with it.
[1748.00 → 1751.64] You know, and then also it allows us to kind of develop our optimization.
[1751.64 → 1759.44] So you might have heard of something of Onyx Runtime, which is really used to be for high-speed inferencing, but we've also tuned it to do high-speed training.
[1759.78 → 1765.32] But all those optimizations kind of came in also with the work that we've been doing with OpenAI and even internally and all that stuff.
[1765.78 → 1768.60] So, you know, more to come on where some of this work shows up.
[1768.60 → 1779.04] But, you know, we also, I think, you know, our goal is to allow OpenAI to do amazing work like GPT-3 and give them the ability to do it from tooling and all that.
[1779.10 → 1785.70] And all that also shows up for our customers, even if they don't get, let's say, access to a GPT-3 model today, right, which they can get from OpenAI.
[1785.70 → 1791.46] But all the work that went into enabling OpenAI to do the work is available to our customers also.
[1791.74 → 1792.34] Yeah.
[1792.54 → 1800.66] Just before we leave the subject of the Azure AI platform, where are some good resources for people to dig in and get started?
[1800.82 → 1811.14] Maybe specifically for data scientists or software engineers who are wanting to get their hands dirty, you know, working a little bit with the Azure AI platform.
[1811.14 → 1816.32] Where can they get started? Any recommendations for them as their sort of onboarding?
[1817.02 → 1821.96] Yeah. You know, so I'll say they're like, depending on where they are, three main ways I'll recommend them.
[1822.04 → 1828.90] If they're already using, they already know machine learning, you know, the machine learning practitioners, you know, just jump into Azure machine learning.
[1829.36 → 1833.96] So, you know, the documentation, we have a bunch of courses on our Microsoft Learn.
[1834.08 → 1836.68] We have them on Udacity too now and other courses. You can take courses.
[1836.68 → 1840.10] But if you know machine learning, the best way is to kind of just dive into the product.
[1840.10 → 1843.84] And again, the product's really designed for ML as a team sport.
[1844.32 → 1851.74] So, especially for folks that have AI teams or data science teams, data engineers, data scientists, and they want to work in a collaborative environment,
[1851.88 → 1857.04] they'll really benefit from ML and having to do it with really modular ML pipelines.
[1857.40 → 1863.10] So, it'd be great to jump into the product and learn about, you know, what an ML platform in the cloud provides like Azure Machine Learning.
[1863.10 → 1866.60] So, just go to Azure Machine Learning or ml.azure.com.
[1867.56 → 1870.18] And if you don't have Azure subscription, you'll be able to go sign it up.
[1870.28 → 1872.06] It's free, and you'll get access to it.
[1872.96 → 1874.40] And that's a great place you can learn.
[1874.84 → 1877.90] Documentation is always a perfect place and easy place for people to access.
[1878.46 → 1885.14] If folks who are wanting to learn, and same with the rest of the portfolio, you can also go to www.azure.com.ai.
[1885.14 → 1888.86] That will take you to all the different offerings we have.
[1889.58 → 1897.06] But if folks who are interested in learning machine learning, who might not be experts, you know, we recently partnered with Udacity to launch a couple of courses.
[1897.06 → 1901.90] And they're perfect in-depth courses that have been developed by us in partnership with them.
[1902.08 → 1904.12] So, that would be the other second place I'll recommend them.
[1904.32 → 1906.64] We also have great training on our Microsoft Learning website.
[1907.32 → 1909.60] And there it can go deep in different areas.
[1909.76 → 1911.10] So, those are the three main areas.
[1911.10 → 1916.04] The product itself, you know, and please give us feedback on what you don't like so we can improve it.
[1916.46 → 1918.72] And the learning courses that we just mentioned.
[1918.72 → 1948.46] So, Bart, in our conversations prior to the show, we had talked a little bit about some of the work that Microsoft is doing research-wise.
[1948.46 → 1956.80] And productizing research to enable computer vision to be used to help people who are blind or have low vision.
[1957.32 → 1961.92] And we talked a little bit about the Seeing AI app and other things.
[1962.10 → 1968.66] But I was wondering if you could kind of just give us a little bit of a briefing on Microsoft's work in this area.
[1968.66 → 1973.58] And I know that they had a pretty interesting milestone in terms of image capturing.
[1973.82 → 1975.14] So, maybe you can go into that a little bit.
[1975.48 → 1975.58] Yeah.
[1975.88 → 1981.36] You know, as I mentioned earlier, like, big focus is kind of doing good research but then putting into products.
[1981.82 → 1988.64] And things we've done in the responsible AI work for model interpretability, fairness detection, and all that, which is available in Azure Machine Learning.
[1988.64 → 1995.94] We did the same thing very recently for the Cognitive Services family of products, which is the customizable AI models.
[1996.54 → 1999.08] In particular, we did the image captioning milestone.
[1999.26 → 2003.10] So, you might know there's a basically novel image captioning benchmark.
[2003.72 → 2011.26] And basically, you know, if you look at image captioning, it is a technique where you show the computer an image, and it says it's an image of blah.
[2011.26 → 2018.28] Normally, the way these things have been trained is by actually giving them, you know, images and complete sentences of what these images are.
[2018.62 → 2020.86] So, what the research team did was something different.
[2021.18 → 2025.70] So, they actually kind of went about how children will learn vocabulary.
[2026.42 → 2029.34] So, when we're learning, we basically say, hey, there's an apple.
[2029.78 → 2032.32] And there's a picture of an apple and this is an apple.
[2032.48 → 2033.28] There's a picture of an orange.
[2033.50 → 2034.50] This is an orange.
[2034.88 → 2036.80] We never said this is an apple sitting on a table.
[2036.80 → 2046.96] So, that's kind of like the first process the team went through, which is building a visual vocabulary by really training object and what the object was.
[2047.28 → 2049.74] Then, that was how they did the pre-training of the model.
[2050.26 → 2055.90] Then, for the fine-tuning, they actually then started giving full sentences to the image, to the model.
[2056.42 → 2060.72] And so, during the inference time, what it first does is it does a visual vocabulary.
[2060.92 → 2061.86] So, it's an image.
[2061.98 → 2063.46] It contains A, B, C.
[2063.46 → 2069.74] Then, based on this fine-tuning step, it is able to put together sentences.
[2070.20 → 2071.78] So, we've had image captions for a while.
[2072.32 → 2074.54] But, you know, we really dramatically improved it.
[2074.56 → 2081.00] So, some couple of examples was, it was a picture of, and I'm happy to share these before and after.
[2081.32 → 2084.08] It's easier to see it than explain it.
[2084.26 → 2086.64] But imagine a picture of a doctor with a stethoscope.
[2087.32 → 2089.66] Before, it said a woman looking at a camera.
[2090.38 → 2092.86] Now, it says a woman wearing a stethoscope around her neck.
[2093.46 → 2095.60] So, very much more accurate.
[2096.30 → 2100.56] Before, this picture of a satellite looking up in the sky, it said a yellow sunset.
[2100.92 → 2101.98] Because, yeah, there was a sunset.
[2102.62 → 2104.96] But now, it says a satellite dish on a dirt road.
[2105.58 → 2108.82] So, basically, it was because of the ability to kind of the way they trained the model.
[2109.24 → 2113.08] And really, it was actually also done, there was a benchmark that they were able to beat.
[2113.08 → 2116.14] And really achieve human parity.
[2116.14 → 2121.30] Which really means, you know, the computer is describing images in the same way that you, or I would describe images.
[2121.42 → 2122.18] Or sometimes even better.
[2122.38 → 2124.08] So, that was kind of the research milestone.
[2124.28 → 2126.50] But, you know, these research milestones are very fascinating.
[2127.26 → 2129.08] Organizations have them around the world all the time.
[2129.76 → 2132.40] What we want to do was bring them to our developers.
[2132.40 → 2135.20] So, in record time, we brought them to Cognitive Services.
[2135.74 → 2140.50] It's a feature of Computer Vision API that's available as part of Cognitive Services.
[2140.82 → 2141.36] There's a free tier.
[2141.40 → 2142.12] People can try it.
[2142.40 → 2145.04] We've also, by the way, embedded it into our applications.
[2145.66 → 2151.32] So, in PowerPoint and Word, when you insert an image, you can do alt text to describe the image.
[2152.10 → 2154.08] And, you know, that's model that's there now.
[2154.34 → 2160.12] Seeing AI is the application that was developed to really help people with blindness to see the world around them.
[2160.12 → 2165.58] And you can only imagine the kind of impact this kind of technology can have in their world.
[2165.80 → 2169.46] So, that's a quick, super quick overview of the research that went in.
[2169.80 → 2173.26] And then really how we bring it to developers and customers.
[2173.54 → 2175.08] I think this is amazing.
[2175.36 → 2190.10] You know, oftentimes on the show, we talk about various things that, you know, like object recognition or computer vision or other things that are either seen by a lot of people as, you know, competitions to be a part of it.
[2190.12 → 2192.98] Or, you know, benchmarks to break.
[2193.38 → 2200.28] But really seeing how that can actually connect to benefit people in a really positive way.
[2200.64 → 2207.52] So, impacting people in terms of the Seeing AI app or, you know, helping accessibility in other ways.
[2207.52 → 2211.68] That's a really amazing place where AI can have a contribution.
[2211.86 → 2214.66] So, I really appreciate you, you know, sharing that.
[2214.66 → 2219.00] And Microsoft for really emphasizing that because it is really amazing work.
[2219.28 → 2222.22] How long has a Seeing AI app been around?
[2222.42 → 2228.38] And have there been impressions of the app from the blind or low vision community?
[2228.92 → 2230.88] Yeah, it's been there for many years.
[2230.96 → 2232.64] I'd love to go see, like, how many exact years.
[2232.76 → 2235.38] But at least the last five years, I believe, it's been out there.
[2235.46 → 2236.08] Five, four years.
[2236.08 → 2242.58] I believe it runs some award, too, about from the industry, you know, for disabilities.
[2243.32 → 2245.16] But, you know, like, those things are great.
[2245.28 → 2250.38] But really, like, at the end of the day, I think it's really our ability to provide something to the world and improves people's lives.
[2250.44 → 2255.84] It really goes to our mission of empowering people, all kinds of people to do more with what they have.
[2256.10 → 2257.96] So, it's been there for a while.
[2258.12 → 2259.36] It has good adoption.
[2259.86 → 2262.44] Sharia, who created it, is blind himself.
[2263.20 → 2263.98] He works at Microsoft.
[2264.28 → 2270.76] He's, you know, and we're just super honoured to have this as one example of us kind of helping customers do more.
[2271.24 → 2280.06] The other example you might not know is something we have called Immersive Reader, which is also, by the way, available as a cognitive service that, you know, developers can put in their applications.
[2280.38 → 2287.32] But you can just, if you download Edge browser, you know, you can right-click on the and it can say, read aloud or immersive reading.
[2287.80 → 2289.64] So, it does a lot of different things.
[2289.64 → 2293.58] It allows you to blow up the text, allow you to focus on separate parts of the text.
[2294.18 → 2296.58] Of course, read the text to you and so forth.
[2297.02 → 2304.14] But that's another, like, you know, thing we've been doing to use AI to help people with disabilities just do their job really well.
[2304.64 → 2305.24] Love hearing that.
[2305.60 → 2308.88] We talk about this kind of use cases pretty regularly on the show.
[2308.88 → 2314.70] You know, the general classification of AI for good in different ways and making the world a better place.
[2314.78 → 2316.12] So, those are pretty fantastic.
[2316.46 → 2319.42] As you were going through that a moment ago, it made me wonder.
[2319.56 → 2321.04] You were talking about research and stuff.
[2321.04 → 2331.64] And within Microsoft, as new research is coming out either internally or external to the organization and everyone's consuming it and trying to understand the latest advancements that are going on.
[2331.94 → 2342.62] How do you get from that point where you read a scientific paper and at some point somebody realizes that there is a service in Azure that you can, you know, utilize that.
[2342.62 → 2348.14] And it becomes something that people like us will then use through Azure Cloud.
[2348.32 → 2356.40] What does that process at a high level kind of look like to get from cool new thing that we're reading about to something that you're now offering the public?
[2356.82 → 2356.94] Yeah.
[2357.20 → 2360.14] Look, some of this work is what I call loosely coupled.
[2360.42 → 2363.86] Because if you try to, like, orchestrate it too finely, then things break down.
[2364.12 → 2365.92] Because a lot of research is exploratory.
[2366.36 → 2371.60] And it is kind of, like, should not be tied to commercial goals directly, right?
[2371.60 → 2374.82] And the area of just pure research and pure learning.
[2375.20 → 2377.38] So we have a dedicated research arm there.
[2377.50 → 2381.02] But it's totally connected to our product side.
[2381.80 → 2383.74] So an AI is a great example.
[2383.88 → 2385.30] And quantum computing is another example.
[2385.40 → 2398.54] There are some spaces where really, like, cutting edge research has a direct line into our engineering teams where we actually are always looking to see, you know, especially when we look at vision, speech, language, and what we call decision category,
[2398.54 → 2406.04] which is where the computer is making a decision or AI algorithms making a decision where something is not just classifying it, but actually making a decision.
[2406.70 → 2411.48] And, you know, recommended something on behalf automatically, not just classifying it again.
[2411.70 → 2415.38] These are kind of four listed domains of research also that we really invest in.
[2415.38 → 2422.16] So our research teams stay super plugged in with our engineering teams, or rather our engineering teams stay super plugged in with their research teams.
[2422.42 → 2433.84] And as these things happen, you know, we're able to kind of, we have established mechanism to take kind of literally raw research and have pipelines built to kind of put them into production and processes to do that.
[2433.84 → 2438.80] And one of the things we've done a lot is had a responsible AI thread throughout this area.
[2439.26 → 2443.32] Because, you know, it's easy to say we have principles of responsible AI, and we, of course, do.
[2443.78 → 2446.46] It's also like, hey, was the data collected with consent?
[2446.74 → 2449.28] Was the data was collected for this kind of research breakthrough?
[2449.46 → 2456.70] Or before we productize it, what other ways do we need to augment the data set to make sure it's not biased or does it have inherent biases and all that stuff?
[2456.70 → 2469.14] And there's a pretty, very big ethics committee that works through the from research into kind of releasing it as a product to the world, where we augment anything that might have been missed in the research phase.
[2469.26 → 2471.94] Because that's really not the focus there oftentimes, as you can imagine.
[2472.92 → 2474.52] It's loosely coupled, but it's connected.
[2474.74 → 2481.24] And then we have a set of processes that walk us through, enables us to kind of bring these things to market really quickly, but do it responsibly too.
[2481.24 → 2490.92] I think it's pretty interesting that you've had the chance to work for many years on these incubated projects within Microsoft.
[2491.42 → 2503.04] And it strikes me that this might give you a unique perspective in terms of the future trajectory of some AI-related technologies and maybe things on the horizon.
[2503.04 → 2515.32] So I'm curious to know a little bit about what excites you about the future of practical AI or AI platform or the mixed reality space and some crossover there.
[2515.44 → 2524.70] What are some of the things like when you're falling to sleep at night, what are those things that are kind of running through your mind that you're dreaming about?
[2524.88 → 2529.94] This is my favourite question when we ask people this, because we get some really cool answers coming back.
[2530.08 → 2530.96] So no pressure.
[2530.96 → 2537.40] Yeah, we've never had anyone pull out their dream journal and read something off.
[2537.74 → 2538.98] As you said, I didn't pull it out.
[2541.06 → 2545.74] Look, with AI, it's a fascinating space because I think it's not just an appeal incubation space now.
[2545.82 → 2548.16] It's getting more and more mainstream than many other technologies.
[2548.36 → 2553.16] And even when it compared other technologies, it's gaining mainstream adoption faster.
[2553.54 → 2560.52] And it's really happening, I just believe, because they're what we call digital native companies, especially, that have been built on the foundation.
[2560.52 → 2565.02] They've been built in the cloud, and they've used AI and ML as a way to really separate themselves.
[2565.30 → 2579.00] So the things that can be exciting, to be more precise, is we've seen companies that you would not imagine using machine learning and doing it not just for descriptive analysis, but actually running ML pipelines, building thousands of models.
[2579.00 → 2583.72] We have a company called AJ and Australia.
[2584.10 → 2584.88] They make windmills.
[2585.52 → 2589.16] And now they're building a machine learning model to windmill, right?
[2589.26 → 2592.20] Not just one generic machine learning model.
[2593.86 → 2596.08] Nestle is another very commonly known name, right?
[2596.08 → 2600.82] But it's not known as a born-in-the-cloud company.
[2600.90 → 2606.60] It's a very old company that has really adopted technology to really help them out-innovate their competition.
[2607.40 → 2615.12] And they're also, by the way, using Azure machine learning in this case to do the email phishing attacks to detect them because they have a huge employee base.
[2615.12 → 2629.98] And they're using very sophisticated ML pipelines to not only train the model once, but to actually look at all the emails that come in and to kind of then stack rank them in the risk factor and then to run more sophisticated machine learning models to really reduce the amount of things that are happening.
[2630.26 → 2631.78] Candid, even aliens is another one.
[2632.36 → 2636.08] You know, they use machine learning to do fraud detection activities.
[2636.08 → 2644.54] And when they want to say, hey, Daniel, Chris, you're a loyalty member, but you did something bad, they need to be very sure before they ask you that question.
[2645.02 → 2650.58] And they're using, you know, again, machine learning and responsible machine learning capabilities to make sure the models are built.
[2650.86 → 2652.34] You know, I have super high confidence.
[2652.46 → 2654.26] They're using model interpretability and all that thing.
[2654.60 → 2664.96] So what really gets me excited is, A, we have many more mainstream companies using AI, not just in the lab, but literally doing thousands of models in production.
[2664.96 → 2673.96] And, you know, really revolutionizing the businesses now, you know, so it's really not in the hands of, let's say, Google, Microsoft, Apple only.
[2674.68 → 2681.34] It's really, you know, what I would call, you know, I'm sure Locke Martin, you know, also does a bunch of machine learning, although I don't work with them anymore.
[2681.80 → 2682.74] A little bit, right?
[2683.20 → 2685.80] But this mainstream company is benefiting from this a lot.
[2685.90 → 2687.40] That gets me excited every single day.
[2687.42 → 2691.88] The second thing is the space is innovating at a superfast pace, right?
[2691.88 → 2694.40] So we have all these new techniques coming in.
[2694.96 → 2701.18] And it almost seems like what was cool two years ago is quite passé now, you know?
[2701.58 → 2706.24] Like whoever, like we all use sidekick learn, but like nobody really talks about it that much in the sense, right?
[2706.28 → 2710.24] Now we're all about putting deep learning models in production at high scale.
[2710.50 → 2715.32] And the space of getting new AI research into the world is just super fascinating.
[2715.32 → 2722.42] And what keeps me excited is like, you know, like I think everybody in this field is AI should never be in the hands of a few.
[2723.04 → 2724.24] And increasingly, it's not.
[2724.74 → 2730.10] Now, as it does get to reach more people, you know, you have to do it in a very responsible fashion.
[2730.10 → 2734.56] And that word cannot be used loosely in the sense that, yeah, anybody can build a model using automated machine learning.
[2734.56 → 2741.50] But unless you give them the ability to kind of look under the hood to understand, you know, did the data have any issues?
[2741.64 → 2743.42] Were there any biases built into the data?
[2743.56 → 2745.08] Would they have high cardinality issues?
[2745.54 → 2754.50] You know, just because the model is 99% accurate, if it has a, you know, if it's classifying the wrong thing, and it's missing nine of the 10 cancer detection.
[2754.50 → 2755.64] It's a pretty damn bad model.
[2756.16 → 2762.64] But being able to now, bringing the sophistication of being a data scientist to people who are no data scientist, it's not easy.
[2763.24 → 2768.80] And we should never trivialize, you know, using API or automated machine learning, you have a model and you're lucky.
[2769.18 → 2771.92] I don't know, you're happy and go and deploy it around the world.
[2772.48 → 2776.70] Now the fun part is, okay, now that we simplified some aspects of machine learning,
[2776.96 → 2782.22] how do we make sure it's applied in a way where people who are applying it fully understand the implications?
[2782.22 → 2787.34] And that's a super exciting space for me and what the industry is doing, what Microsoft is doing.
[2787.82 → 2790.98] Not just simplifying it, but putting it, making it practical at the end of the day.
[2791.22 → 2792.98] So more people get benefit from it.
[2793.28 → 2795.56] And, you know, it's a never ending cycle.
[2795.80 → 2801.06] New research comes in, taking it to market and doing it in a way that most people can benefit from it.
[2801.52 → 2807.42] Controlling the hype around this topic, but really driving the, you know, benefits for our customers.
[2807.42 → 2814.00] So it's a long-winded answer, but it is kind of making sure AI is applicable to a large set of customers,
[2814.26 → 2820.02] but in a practical fashion, not in a buzzword-y fashion, not just saying one click and boom, you have a model.
[2820.38 → 2827.00] And the second one is just the pace of innovation and new techniques coming in and the opportunity it offers to customers,
[2827.20 → 2830.20] even who don't have data, to do machine learning.
[2830.70 → 2834.98] Like things like reinforcement learning techniques when applied correctly can solve some of these kind of issues.
[2834.98 → 2845.80] So it's really making this not a special topic, but a really, really widely useful topic is what excites me and keeps me up.
[2846.32 → 2846.38] Awesome.
[2846.60 → 2848.90] Well, I don't know about you, Chris, but I'm inspired.
[2849.32 → 2851.28] I'm psyched right now, if you can't say.
[2852.02 → 2855.46] We're at a really great way to end our conversation here.
[2855.60 → 2858.24] I think our listeners will be equally inspired.
[2858.46 → 2861.78] I hope that they get out and try some of these things in Azure Cloud.
[2861.78 → 2867.04] We'll make sure and include links in our show notes to all of those things that we discuss.
[2867.22 → 2870.56] So make sure you get out there and try some things, get hands on.
[2871.26 → 2873.54] And yeah, thank you so much for joining us, Bharat.
[2873.70 → 2874.64] Thank you for having me.
[2874.86 → 2876.86] And thanks for having a great podcast.
[2877.24 → 2877.72] Thank you.
[2877.72 → 2886.52] Come hang out with Daniel, Chris, and hundreds of other AI practitioners in our community Slack.
[2886.68 → 2887.86] It's a cool place to be.
[2887.94 → 2890.04] Not a lot of noise, some great signal.
[2890.18 → 2891.84] And best of all, it's totally free.
[2892.24 → 2894.60] Check it out at changelog.com slash community.
[2894.98 → 2900.40] And don't forget to follow the show on Twitter for AI news and links, highlights from past episodes and more.
[2900.40 → 2902.54] We are at Practical AI FM.
[2902.74 → 2903.92] We'd love to have you following along.
[2903.92 → 2908.10] Thanks to Daniel and Chris for hosting Practical AI week in and week out.
[2908.20 → 2912.56] To the mysterious Break master Cylinder for the excellent beats you hear on all changelog podcasts.
[2912.88 → 2916.98] To our sponsors who have our back, Vastly, Linde, and Launch Darkly.
[2917.20 → 2918.12] And to you for listening.
[2918.42 → 2920.02] We appreciate your time and attention.
[2920.66 → 2921.78] That's all for now.
[2921.88 → 2928.64] On the next episode of Practical AI, we are running Daniel's panel at the R conference talking AI for good.
[2928.64 → 2930.02] So stay tuned for that one.
[2930.08 → 2931.90] Hit in your feed next week.
[2933.92 → 2935.80] We'll see you next week.
[2935.82 → 2935.92] Bye.
[2935.92 → 2936.42] Bye.
[2936.42 → 2936.92] Bye.
[2936.92 → 2937.92] Bye.
[2937.92 → 2938.92] Bye.
[2938.92 → 2939.92] Bye.
[2939.92 → 2940.92] Bye.
[2940.92 → 2941.92] Bye.
[2941.92 → 2942.92] Bye.
[2942.92 → 2943.92] Bye.
