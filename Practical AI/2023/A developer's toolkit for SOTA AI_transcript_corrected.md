[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.04] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.02 → 36.08] Learn more at fly.io.
[43.08 → 46.22] Welcome to another edition of the Practical AI podcast.
[46.64 → 47.66] My name is Chris Benson.
[47.80 → 49.06] I'm your co-host today.
[49.18 → 54.30] Normally we would have Daniel Whiten ack joining us, but Daniel has just gotten off a plane.
[54.30 → 58.70] He flew halfway around the world, and we decided to give him a break from today.
[58.92 → 63.58] I would, I would be, he was more lucid than I would be under the same situation.
[64.10 → 66.42] Today I wanted to, to dive right in.
[66.54 → 69.16] We have a super cool topic.
[69.44 → 74.26] It is not dissimilar from some of the other general things we've been talking about, but
[74.26 → 75.38] I have two guests today.
[75.38 → 81.66] I'd like to introduce Varun, who is the CEO and co-founder of Sodium and Annul, who is
[81.66 → 84.00] the lead of their enterprise and partnership.
[85.04 → 86.28] Welcome to the show guys.
[86.80 → 87.44] Thanks for having us.
[87.88 → 88.78] Thanks for having us, Chris.
[89.32 → 90.38] Yeah, you're, you're welcome.
[90.64 → 94.36] I'm really interested in learning more about Sodium.
[94.66 → 97.00] When Daniel lined you guys up, he's like, Chris, you got it.
[97.04 → 98.72] He sent me this thing saying, you got to look at this.
[98.76 → 100.34] This is really cool and everything.
[100.34 → 101.20] And I'm like, get him on the show.
[101.22 → 102.20] He's like, I'm already doing that.
[102.20 → 105.48] So, so really glad to have you guys on.
[105.62 → 109.02] And he's going to be bumming that he missed the conversation because he was pretty excited
[109.02 → 109.46] about it.
[109.64 → 115.50] And so I guess I wanted to, before we even dive into Sodium and the problems it's trying
[115.50 → 120.82] to solve and such, if you guys could each just tell me a little bit about how you found
[120.82 → 126.10] yourself arriving at this moment, kind of little bit about your background, how you
[126.10 → 129.76] got into AI and how, how this became the thing.
[129.76 → 132.14] Varun, if you want to kick off and then Annul afterwards.
[132.20 → 134.58] So maybe I can get started.
[134.58 → 137.64] Um, actually starts in 2017.
[137.64 → 142.82] I started working at this company called Euro that does autonomous goods delivery.
[142.82 → 144.28] So it's an AV company.
[144.28 → 148.18] There I sort of worked on large scale offline deep learning workloads.
[148.36 → 152.50] So as you can imagine, an autonomous vehicle company needs to run large scale simulation.
[152.84 → 157.66] They need to basically be able to test their ML models at scale before they can actually
[157.66 → 158.62] deploy them on a car.
[158.62 → 165.46] And sort of in 2021, I left Euro and started Expunction, which is the company that is building
[165.46 → 166.60] out this product Sodium.
[167.10 → 170.42] And Expunction started out building GPU virtualization software.
[170.68 → 174.00] So you can imagine for these large scale deep learning applications.
[174.00 → 177.16] One big problem is GPUs are scarce.
[177.38 → 179.56] They're expensive and also hard to program.
[180.34 → 186.02] And sort of what Expunction started building was solutions and software to make it so that
[186.02 → 190.30] applications that ran on GPUs were more effectively using the GPU hardware.
[190.30 → 197.04] And we realized that our software with Expunction was the best applicable to generative AI tech and
[197.04 → 198.96] started building out Sodium around a year ago.
[198.96 → 199.86] Very cool.
[200.30 → 205.18] And before I dive in, because I have several questions for you, but I want to give Annul
[205.18 → 206.70] a chance to introduce himself here.
[206.92 → 207.42] Go ahead, Annul.
[207.86 → 209.54] Surprisingly, my story is actually quite similar.
[209.66 → 210.64] I was also working at Euro.
[211.30 → 214.06] So Varun and I used to work together back in the day.
[214.34 → 217.50] I was not actually working on the ML infrastructure side of things.
[217.64 → 219.44] That was something that Varun had hands-on on.
[220.08 → 223.88] But I decided to kind of also join the team at Expunction.
[224.44 → 228.58] And I think, yeah, as Varun mentioned a year ago, I think we noticed there was like,
[228.98 → 233.42] I think three things kinds of happened at the same time that we noticed that led us to Sodium.
[233.88 → 236.62] I think the first one is that we're engineers.
[237.24 → 238.14] All of us here are engineers.
[238.56 → 244.88] And we had all tried the GitHub co-pilots and all these cool AI tools for code in their beta.
[245.14 → 249.06] And we're like, wow, this is absolutely going to be the future of software development.
[249.44 → 252.82] But at the same time, you know, it's like still scratching the surface of potentially
[252.82 → 254.66] everything that we do as engineers.
[255.22 → 257.30] So it was, I think, like number one, I think that we realized.
[257.48 → 261.68] Then number two was, you know, talking to a lot of our friends at, you know,
[261.68 → 263.94] these like bigger companies or anything like that.
[264.40 → 266.38] A lot of them were just saying like, oh, yeah, it's cool.
[266.38 → 269.88] I've tried it for my personal project, but I can't use it at work, right?
[269.96 → 271.28] My work's not allowing me to use that.
[271.62 → 272.84] So it was like the second thing we heard.
[273.26 → 275.38] And the third thing was exactly what Varun alluded to.
[275.38 → 280.00] We were building like ML infrastructure at scale for really large workloads.
[280.24 → 283.22] Like when this entire generative AI wave started coming, we're like, wow,
[283.24 → 286.20] we're actually kind of sitting on the perfect infrastructure for this.
[286.62 → 290.04] So I think all of those three things kind of combined for us to be like,
[290.40 → 290.68] do you know what?
[290.76 → 293.76] Let's build out an application ourselves and build an application that we,
[293.82 → 296.84] as engineers, are customers ourselves, right?
[296.92 → 298.38] And that ended up becoming Sodium.
[298.38 → 304.16] As you were getting into doing GPU software, what was in general some of the challenges
[304.16 → 308.46] that you were seeing, you know, with NVIDIA has their various software supporting things
[308.46 → 308.86] like that.
[309.32 → 312.48] Clearly you saw that there was a need for something beyond that.
[312.56 → 317.28] Can you talk a little bit about just the layout that you saw in the, you know, in the environment
[317.28 → 321.24] before you got to all the generative stuff and the fact that you had infrastructure?
[321.78 → 323.66] What positioned you for that?
[323.70 → 326.22] And what was the thing that you decided that you needed to address?
[326.22 → 331.28] Maybe I can take it a step back of why these GPU workloads are just a little bit annoying
[331.28 → 332.46] compared to CPU workloads.
[332.82 → 332.88] Okay.
[333.10 → 340.10] One of the really sort of unique things about GPUs is that unlike CPUs, it's kind of tricky
[340.10 → 340.88] to virtualize.
[340.98 → 345.70] Like one common thing that we have with CPUs is you can put a bunch of containers on a single
[345.70 → 350.66] VM, and then you can kind of make use of the CPU compute like effectively, right?
[350.66 → 354.18] You can basically dump 10 applications onto a CPU, and it's perfectly fine.
[354.18 → 358.66] For GPU, it's a little bit more messy because the GPU doesn't have a ton of memory.
[359.16 → 361.68] So you can't just load up infinitely many models on there.
[361.90 → 366.12] Like let's imagine you have a GPU with 16 gigs of memory and each of these models takes like
[366.12 → 366.64] 10 gigs.
[366.82 → 369.36] You can't really even put two applications on there.
[369.86 → 371.92] So then that already becomes a big issue.
[372.14 → 376.16] And that's sort of what a lot of these large deep learning workloads were struggling with.
[376.16 → 382.08] So when I was at Euro, one big problem we had was we had around like tens of models,
[382.08 → 386.76] but we had these workloads that needed hundreds of GPUs, some of them even thousands of GPUs.
[386.92 → 392.32] And we struggled to basically make it so that we were even able to use the hardware properly.
[392.50 → 397.10] And then, you know, you could imagine the complexity then stacks with now we're in a state where
[397.10 → 402.14] companies have trouble even getting access to 10 GPUs because of NVIDIA sort of scarcity issues.
[402.14 → 405.34] And then also the cost of a GPU is like not like a CPU.
[405.46 → 406.84] It's like significantly more expensive.
[406.84 → 411.26] Like the cost of a single H100, you know, chip is well over 30 grand.
[411.48 → 413.26] So these aren't like very cheap chips.
[413.72 → 418.12] So there's like a big need at the time to figure out how do we leverage the hardware properly?
[418.30 → 420.54] And sort of that's what we had to build software for.
[421.10 → 425.44] And just to clarify for me, was that why you were still at Euro or was that after you started Expunction?
[426.00 → 426.18] Yeah.
[426.26 → 430.84] So while I was at Euro, we sort of worked through or I sort of led a team that sort of built
[430.84 → 433.48] software that kind of fixed these problems.
[433.90 → 438.74] But Expunction was focused on generically how do we make sure deep learning based applications
[438.74 → 440.78] could best leverage GPUs.
[441.12 → 443.54] That's sort of what we started out building, actually.
[444.02 → 445.86] And then Sodium came out from that, actually.
[446.12 → 446.22] Gotcha.
[446.64 → 450.60] Tell me a little bit about as you have been right in the middle of this progression,
[450.82 → 452.50] just to frame it for a second.
[452.68 → 456.60] If you look at the last, you know, a couple of years in particular,
[456.60 → 459.52] and the pace of change has been so much.
[459.98 → 465.46] And so you were right there starting at Euro and then creating Expunction, seeing some
[465.46 → 466.10] of the challenges.
[466.28 → 472.66] Could you talk a little bit about how the industry was evolving and changing as you were seeing
[472.66 → 477.46] it so that we can get a sense of kind of how you moved toward Sodium, you know, to give
[477.46 → 480.58] a little bit of the history instead of just starting from where that is.
[480.72 → 485.34] Can you talk a little bit about, you know, the itches that you were scratching and why it led
[485.34 → 485.96] that direction?
[486.22 → 489.00] What did this AI industry look like to you?
[489.70 → 489.82] Yeah.
[489.90 → 494.42] So when we started, like, you can just imagine everything was a lot smaller scale, right?
[494.46 → 498.24] The hyperscalers or the cloud providers just didn't have nearly as many GPUs.
[498.24 → 501.66] Like if you ask them, like, what fraction of cloud spend is GPU spend?
[502.04 → 506.86] It's probably like very small single digit percentage points, maybe even less than that at the time.
[506.96 → 511.10] So this is like a very small workload for them when we sort of started, both me and Annul started
[511.10 → 512.24] at Euro in like 2018.
[512.24 → 515.20] But then over time, this grew a ton.
[515.36 → 517.10] Like we could see it from the training workloads.
[517.52 → 519.86] These were no longer like even single node training workloads.
[520.04 → 524.98] Like back in the day, a single GPU node that had maybe like eight V100s or something was
[524.98 → 526.16] like considered a lot of compute.
[526.62 → 530.68] And suddenly now we were able to witness the fact that this was slowly becoming eight A100
[530.68 → 531.08] nodes.
[531.12 → 535.08] And then more than eight of these nodes were necessary then even to train these models.
[535.08 → 540.50] And similarly, to prove out that these models were capable, like in an actual production
[540.50 → 546.22] setting, you needed to run offline testing at massive scales, like on the order of like
[546.22 → 551.36] 5,000 to 10,000 T4s scales, which is like kind of incredible in terms of raw flops.
[551.50 → 554.72] So we were able to see this hockey stick happen in front of us.
[554.82 → 559.10] And then that's sort of what made us want to start Expunction in the first place.
[559.10 → 562.14] We realized that there were going to be large deep learning workloads.
[562.14 → 567.30] One interesting fact is for us, like for just the Expunction GPU virtualization software
[567.30 → 574.02] that we ended up selling to enterprises, we ended up managing over 10,000 GPUs on GCP
[574.02 → 575.68] in a single GCP region.
[575.82 → 577.42] So we ended up managing more than 20%.
[577.42 → 581.34] And we realized that, that, hey, this was only going to keep growing.
[581.50 → 584.48] Like when we talked to the cloud providers, they were only going to keep growing the number
[584.48 → 585.04] of GPUs.
[585.12 → 588.98] And we realized, I guess the interesting thing was in the future, generative AI was going
[588.98 → 591.18] to be potentially the largest GPU workload though.
[591.18 → 597.36] That was the big thing we realized was GPT-3 came out, which was, I guess, in 2021 now.
[597.78 → 597.86] Gotcha.
[598.10 → 600.92] So, but you had already, at that point, were you already in Expunction?
[601.10 → 602.46] Had it already started at that point?
[602.66 → 603.98] Yeah, it had already started.
[604.10 → 608.58] And we were sort of selling GPU virtualization software to large autonomous vehicle and robotics
[608.58 → 609.06] companies.
[609.44 → 609.68] Gotcha.
[610.02 → 617.08] And so basically, if I'm understanding correctly, the whole generative tsunami just kind of landed
[617.08 → 621.64] on you when you were already sitting in that space doing GPU virtualization already.
[621.80 → 626.08] So you just managed to land right in front of the wave, it sounds like.
[626.40 → 626.58] Yeah.
[626.62 → 631.56] So we started working on Sodium like maybe four or five months ago before ChatGPT.
[631.68 → 635.98] It was interesting just because we realized that an application like GitHub Copilot was
[635.98 → 638.36] going to be one of the largest GPU workloads, period.
[638.36 → 641.34] Like, I don't know if you've probably tried the product out.
[641.42 → 644.78] It's like every time you do a key press, you're going out to the cloud and doing trillions
[644.78 → 645.62] of computations.
[645.96 → 646.04] Yeah.
[646.08 → 646.22] Right?
[646.22 → 647.48] So it's like a massive workload.
[647.62 → 651.98] And we had like, as Annul said, the perfect infrastructure to basically run this at enormous
[651.98 → 652.34] scale.
[652.64 → 655.14] Not to mention, we were in love with the product from day one.
[655.22 → 658.48] Like we were early users of the product the moment it came out in 2021.
[659.00 → 659.66] Very cool.
[659.66 → 667.20] So as generative is starting to take off, kind of with ChatGPT hitting the world and really
[667.20 → 671.28] changing things quite rapidly, you know, I think people are still shocked at how fast
[671.28 → 672.32] things have moved.
[672.48 → 674.30] You had started Sodium already.
[674.70 → 679.58] What kind of synergy were you starting to see there in terms of knowing that you have
[679.58 → 685.04] one of presumably many, many GPTs coming and other similar generative models?
[685.28 → 687.12] You had just gotten into Sodium.
[687.12 → 692.50] Can you talk a little bit about what that was, and what were you putting together in your
[692.50 → 695.60] minds to recognize the opportunity that it was?
[696.18 → 696.30] Yeah.
[696.38 → 701.52] So I think like one of the, you know, great things about entire ChatGPT wave is that,
[701.64 → 703.08] you know, everyone was using it.
[703.34 → 706.04] This is a thing where like literally every individual is using AI.
[706.26 → 708.36] And so it helped us in general, right?
[708.38 → 710.76] You know, like a big wave like raises all ships kind of thing.
[711.06 → 712.22] You know, it really helped us.
[712.28 → 717.04] We weren't really going out and telling people like, hey, a tool like Sodium can help productivity.
[717.12 → 720.28] Because that was kind of just now assumed by everybody.
[720.60 → 725.36] Like, oh yeah, if I do any kind of, you know, knowledge work, then there's potential for
[725.36 → 726.04] AI to help.
[726.36 → 726.48] Right.
[726.52 → 730.28] And I think so from that sense, when the star, like, you know, ChatGPT wave really came
[730.28 → 734.64] about, that overall kind of just like helped us in terms of convincing people to even try
[734.64 → 735.08] the product.
[735.62 → 740.52] The other thing that we recognize is that we were positioning ourselves very specifically
[740.52 → 741.20] from the beginning.
[741.20 → 741.48] Right.
[741.48 → 745.26] When it comes to code, code is like actually a very interesting modality.
[745.48 → 745.58] Right.
[745.60 → 751.64] It's not like your standard, you know, ChatGPT where you have a long context that, you know,
[751.68 → 754.40] user puts in, and then it produces context coming out.
[754.60 → 754.96] Right.
[755.02 → 759.16] Code is interested in the sense that, you know, as we mentioned, it's an autocomplete.
[759.26 → 763.16] That's like a passive AI rather than like an AI that you're actually instructing, you
[763.16 → 764.34] know, the model to do something.
[764.46 → 765.88] It's happening every keystroke.
[766.00 → 768.32] So it has to be a relatively smaller model.
[768.32 → 768.52] Right.
[768.56 → 772.34] You can't, you have these like, you know, hundreds of billions of parameter models being
[772.34 → 772.74] used.
[773.04 → 774.36] It has to be relatively low latency.
[774.96 → 776.10] And then code itself is interesting.
[776.22 → 776.34] Right.
[776.36 → 780.44] If you have a cursor in the middle of a code block, the context both before and after your
[780.44 → 781.42] cursor really matters.
[781.82 → 781.90] Right.
[781.92 → 783.04] It's not just what comes before.
[783.18 → 787.48] So like there's all these interesting kind of like situational kind of constraints about
[787.48 → 791.36] code that you put all these things together, and we realize that, okay, you know, all
[791.36 → 795.12] these ChatGPT waves and conversational AIs are happening.
[795.40 → 796.00] That's great.
[796.00 → 799.26] But we're still not going to be like, you know, rolled over by that because we're kind
[799.26 → 805.06] of focusing on a very specific application and modality of LLMs that was pretty unique
[805.06 → 805.70] in many ways.
[805.70 → 831.12] Could you take a moment as we're diving into sodium and generative AI and its unique, you
[831.12 → 836.46] know, capabilities there and just differentiate a little bit about for those, you know, so
[836.46 → 837.80] many people have tried Copilot.
[838.38 → 841.76] And so it's kind of inevitable that you're going to get that comparison to some degree.
[842.26 → 849.36] Can you talk a little bit about what Copilot's not doing for generative AI or how you're approaching
[849.36 → 854.86] it that allows you to show people this as a better way forward from your perspective?
[855.26 → 857.48] I mean, we have tons of respect for the Copilot team.
[857.48 → 858.58] I'm not just going to start with it, right?
[858.64 → 860.82] And as Rune said, we were all early users of it.
[861.02 → 862.76] Definitely not putting you into conflict with them.
[862.86 → 864.54] That just is a starting point for people.
[864.90 → 865.22] Absolutely.
[865.52 → 865.66] Yeah.
[865.70 → 869.70] I think the way we kind of view this and I kind of like alluded to this earlier is that
[869.70 → 872.20] you're writing brand-new code, right?
[872.24 → 877.46] With autocomplete is really just one small task that we do as engineers, right?
[877.46 → 882.80] We refactor code, we ask for help, we write documentation, we do PR reviews.
[883.56 → 887.52] And so kind of our general approach has always been, let's try to build an AI toolkit rather
[887.52 → 888.86] than AI autocomplete tool.
[889.16 → 889.30] Got it.
[889.34 → 892.72] So we can get more into this, into the weeds here, but like autocomplete is just one of
[892.72 → 895.08] our functionalities that we provide, right?
[895.10 → 896.72] We provide like an in-IDE chat.
[896.80 → 901.28] So think like ChatGPT, except integrated with the IDE, natural language search over your
[901.28 → 903.88] code base using like embeddings and vector stores in the background.
[903.88 → 907.82] So like we're really trying to expand, like how can we address like the entire software
[907.82 → 908.56] development lifecycle?
[908.98 → 912.42] So I think that's probably the, you know, the most obvious difference with a tool like
[912.42 → 915.24] Copilot from like an individual developer point of view.
[915.40 → 918.54] But then the other thing, which really kind of builds off of all the infrastructure that
[918.54 → 923.54] Verdun was mentioning earlier is that we were already deploying, you know, ML infrastructure
[923.54 → 926.98] in our previous customers' private clouds.
[927.08 → 932.10] Like we already had all this expertise of how can we take actual ML infra, deploy it for
[932.10 → 935.96] a customer in a way that, you know, they can fully trust the solution because, you know,
[935.98 → 937.24] we're not getting any of their data.
[937.78 → 941.54] And so another huge differentiator for us was like, okay, I think this might actually
[941.54 → 946.66] be a tool that enterprises can use confidently and safely because we have the infrastructure
[946.66 → 950.90] to do the deployment in a manner that they would, they would be open to using.
[951.02 → 955.32] So I think that was like the other differentiator when it came specifically to enterprises, but we
[955.32 → 956.60] can dive more into that later.
[956.76 → 957.42] No, that sounds good.
[957.42 → 963.10] I want you to connect one more thing for me going from being able to deploy the infrastructure
[963.10 → 966.64] and helping your customers in that way to Sodium as a tool.
[966.98 → 970.12] What's the leap there that got you from one to the other?
[970.22 → 973.58] How did you get from infra focused to Sodium focused?
[974.30 → 974.50] Oh yeah.
[974.60 → 978.32] We, I think we had to do like a full like 180 when we started, we were like one from
[978.32 → 982.34] full like infra as a service company to like, let's like to create a product for consumers,
[982.40 → 982.50] right?
[982.50 → 984.18] Like it was a full 180 in terms of product.
[984.36 → 984.66] A pivot.
[984.66 → 988.42] Yeah, full and in some degrees a pivot because we knew that, you know, eventually, okay,
[988.50 → 990.00] we'll deploy to customers VPCs.
[990.02 → 990.58] That sounds great.
[990.92 → 994.98] But like, if we're going to ship something to a customer, we had to be like super confident
[994.98 → 997.36] that it was a product that would work well, right?
[997.36 → 999.58] Because we're getting no feedback from their developers.
[1000.14 → 1003.96] And so we actually first focused for the first like six or so months of Sodium, just
[1003.96 → 1006.46] building out like an individual tier, right?
[1006.54 → 1008.28] Any developer can go try it.
[1008.64 → 1010.76] We can see how they like it, right?
[1010.76 → 1014.22] Try our new capabilities, get feedback from an actual community, do all these like
[1014.22 → 1018.28] community building things that we hadn't really done as like, you know, infra as a service
[1018.28 → 1018.72] company.
[1018.92 → 1021.42] But that was like a really huge focus for us.
[1021.48 → 1026.90] And, you know, we've grown our actual Sodium individual plan to like over 100,000 active
[1026.90 → 1030.78] developers using us for like, you know, many hours a day because you code for that long
[1030.78 → 1031.46] if you're a developer.
[1032.08 → 1034.74] You know, that's like plenty of feedback to us, right?
[1034.82 → 1037.56] Plenty of people actually using the tool telling us like, yeah, this is good.
[1037.64 → 1038.24] This isn't good.
[1038.30 → 1039.60] Like, oh, you tried pushing a new model?
[1039.66 → 1040.08] That's worse.
[1040.08 → 1043.60] It's like all those things we actually learned so that we can get a product that's good.
[1043.64 → 1046.50] So that was like the I guess the intermediate period, right?
[1046.54 → 1050.98] Really learning from actual developers what is a good product and what is not.
[1050.98 → 1054.44] And I think that's like, that's always going to be a key kind of part of our development
[1054.44 → 1054.82] cycle.
[1055.32 → 1059.82] You're coming into this with this rich knowledge and infrastructure for customers.
[1060.44 → 1062.10] That's a huge area of expertise.
[1062.48 → 1067.00] It's an area of expertise that even though you were moving forward into the kind of the Sodium
[1067.00 → 1073.28] era, if you will, in my words, that is a skill set and level of expertise that very few organizations
[1073.28 → 1075.62] have deeply that you would have had there.
[1075.98 → 1082.78] How did that inform you in terms of Sodium and differentiation against whether it be Copilot
[1082.78 → 1087.08] or other tools that are out there or just, you know, developers, you know, throwing things
[1087.08 → 1088.06] into ChatGPT?
[1088.40 → 1093.38] What did that background give you that gave you that differentiation in the marketplace?
[1093.38 → 1093.86] Yeah.
[1094.16 → 1098.24] So I think when we started, the thing we started with is like, no one cares if we have better
[1098.24 → 1099.84] infrastructure once you're a product.
[1100.08 → 1101.70] Like if we have better infrastructure, that's great.
[1101.80 → 1105.10] But if that makes a product that's the same, no one should care.
[1105.24 → 1106.54] They just assume that you should.
[1106.82 → 1106.98] Yeah.
[1107.32 → 1110.80] So what we started with is we set a very high bar for ourselves.
[1111.08 → 1112.80] Sodium is an entirely free product.
[1112.92 → 1117.54] So like for the individual user, it's something that they can install and use immediately for free.
[1117.72 → 1118.64] There are unlimited.
[1118.88 → 1120.24] There's like no limits at all.
[1120.24 → 1123.46] So like when it comes to autocomplete, you can use it as much as you want.
[1123.92 → 1128.66] And this is, by the way, forced us to do things where infrastructure is as efficient as possible.
[1128.84 → 1134.34] Just to give you a sense of the numbers we're talking about here, we process over 10 billion
[1134.34 → 1135.64] tokens of code a day.
[1135.72 → 1137.10] That might sound like a large number.
[1137.18 → 1141.24] That's like over a billion lines of code a day that we process for our own developers.
[1141.42 → 1143.14] We're forced to do this entirely for free.
[1143.32 → 1147.00] And then on top of that, we probably have one of the world's largest chat applications also
[1147.00 → 1148.36] because it's in IDE as well.
[1148.36 → 1154.16] And all of this put together has allowed us to build a very, very scalable piece of infrastructure
[1154.16 → 1157.10] such that we're the largest users of our own product.
[1157.44 → 1159.32] We're the largest user of our own product.
[1159.46 → 1160.80] We learn the most from our users.
[1161.02 → 1166.38] And we can then take those learnings and deploy in a very cost-effective, very efficient and
[1166.38 → 1168.50] optimized way to our own enterprise users.
[1168.88 → 1173.80] It's one of those things where we force ourselves to learn a lot from an individual plan and then
[1173.80 → 1176.42] take all those learnings and actually bring them over to the enterprise.
[1176.42 → 1181.30] And a lot of the learnings we were only able to make because we place like very, I would
[1181.30 → 1184.80] say like annoying infrastructure constraints on ourselves by saying, hey, you guys got to
[1184.80 → 1186.50] do this entirely for free, basically.
[1186.98 → 1190.04] And we're committed to building, Sodium is going to be a free product forever.
[1190.50 → 1192.28] Actually, the individual plan will always be free.
[1192.38 → 1195.74] And it's one of those things where our users are just always like, how are these guys even
[1195.74 → 1196.30] doing it?
[1196.58 → 1198.52] Like, what are they even doing to make this happen?
[1198.64 → 1201.38] And most of our users, by the way, are users that have churned off of Copilot.
[1201.38 → 1204.28] We have spent very little, if not anything on marketing.
[1204.76 → 1208.02] So it's just one of those things where our users are like, how do we make this free?
[1208.14 → 1211.78] We take the approach of, we think some of the best products in the world are free, like
[1211.78 → 1213.02] products at Google, right?
[1213.04 → 1213.82] They're entirely free.
[1214.12 → 1217.02] Google doesn't tell you all the time that they have the best infrastructure, but they
[1217.02 → 1218.04] do have the best infrastructure.
[1218.40 → 1221.28] It just so happens to be the case that that shows itself off in the best product.
[1221.72 → 1225.30] And we could talk a little bit more about how we take our sort of focus on infrastructure
[1225.30 → 1227.32] and make a much better enterprise product as well.
[1227.64 → 1229.42] But like, that's the way we sort of look at it.
[1229.42 → 1232.84] It's like, how do we deliver materially better experiences with our infrastructure?
[1233.26 → 1235.42] And our users shouldn't care that we actually did that.
[1235.76 → 1236.40] You've brought it up.
[1236.44 → 1237.44] You got to go there now, man.
[1237.56 → 1238.76] Go ahead and dive right into it.
[1238.94 → 1243.18] I guess like one of the interesting things, like just going to how we run one of the world's
[1243.18 → 1247.84] the largest LLM applications, what that sort of focus forced us to do is give it a single
[1247.84 → 1248.68] piece of compute.
[1248.68 → 1251.34] Like, let's say a single node or a single box of GPUs.
[1251.42 → 1253.68] We can host the most number of users on there.
[1253.90 → 1255.76] So like, let's say a large company comes to us.
[1255.76 → 1261.12] They can be confident that whether they're on-prem or they're in VPC, we can give them
[1261.12 → 1265.94] a solution where the cost of the hardware is not going to dominate the cost of the software
[1265.94 → 1266.32] itself.
[1266.56 → 1271.76] Because right now there's kind of this misunderstanding that the GPUs are really expensive, which is
[1271.76 → 1271.94] true.
[1272.02 → 1272.34] They are.
[1272.72 → 1274.54] But the trade-off is they have a lot of compute.
[1274.94 → 1281.30] Like modern GPUs like A100s can do 300 teraflops of compute, which is like some ungodly number,
[1281.42 → 1281.54] right?
[1281.54 → 1284.28] Like that's a crazy number compared to what a modern CPU can do.
[1284.56 → 1286.54] And we can leverage that the best.
[1286.90 → 1288.32] And we've sort of been forced to do that.
[1288.40 → 1291.90] Like, you know, if we didn't do that properly, we'd have outages with our service all the
[1291.90 → 1292.16] time.
[1292.60 → 1297.36] Because of that, enterprises trust us to be like the best solution to run in their own
[1297.36 → 1302.40] tenant in an air-gapped way, which is fantastic because that's like the way that we can build
[1302.40 → 1306.26] the most trust and deploy these pieces of technology to them the most effectively because they don't
[1306.26 → 1307.78] want to ship their code outside the company.
[1308.20 → 1311.48] Annul can talk a little bit more about how we leverage things like fine-tuning as well.
[1311.78 → 1315.96] It's like a pure infrastructure problem that's unique to us versus like any other company
[1315.96 → 1316.32] as well.
[1316.46 → 1318.42] Annul, do you want to sort of take that?
[1318.92 → 1319.26] I mean, yes.
[1319.32 → 1322.74] I think, you know, as Siren said, there are a lot of things that we do from like the individual
[1322.74 → 1326.34] infrastructure point of view so that we can do crazy things like make it all free for
[1326.34 → 1327.50] all of our individual users.
[1327.66 → 1332.74] But once we actually self-host, there are actually a lot of things that you can do that, you know,
[1332.74 → 1335.96] just any other tool can't do without being self-hosted.
[1335.96 → 1339.60] And one of the ones that Siren just mentioned is, you know, personalization, right?
[1339.64 → 1345.80] If you're fully hosted in a company's, you know, tenant, you can use all of their knowledge bases to
[1345.80 → 1348.04] create a substantially better product, right?
[1348.06 → 1353.52] I think the way we generally think about it is that you have a generic model that's good.
[1353.60 → 1356.82] It's learned from trillions of tokens of code on the public corpus.
[1356.82 → 1361.70] But if you think about any like individual company, they have themselves hundreds of
[1361.70 → 1364.38] millions of tokens of code that has never seen the light of day.
[1364.86 → 1368.02] And that's actually the code that's the most relevant for them if they want to write any
[1368.02 → 1368.48] new code.
[1368.74 → 1374.00] Think of like all the internal syntax, semantics, utility functions, libraries, DSLs, whatever
[1374.00 → 1374.58] it might be.
[1375.04 → 1379.74] And a model like a Copilot or a Sodium, by the nature of it having to be low latency, can
[1379.74 → 1383.70] only take about 150 or so lines of code as context, right?
[1383.70 → 1387.52] So this is not like one of those like, you know, chat GPTs or GPT-4s where you're like
[1387.52 → 1389.12] putting in files and files of context.
[1389.22 → 1391.44] Like it's tiny where you can put in.
[1391.88 → 1395.84] And so there's really no way for a single inference to have full context of your code
[1395.84 → 1402.44] base without actually fine-tuning the base model that we ship to them on all of their
[1402.44 → 1403.02] local code.
[1403.48 → 1406.78] And so we've actually, you know, done a bunch of studies, and we're like on how this
[1406.78 → 1410.52] actually massively reduces like hallucinations and all these other things that, you know,
[1410.52 → 1412.40] you always hear coming up with LLMs.
[1412.40 → 1416.80] But, you know, things like this, things like providing more in-depth analytics, all these
[1416.80 → 1419.22] things actually come up by being self-hosted.
[1419.36 → 1423.34] And as Rune mentioned, these are all at the core to some degree an infra problem, right?
[1423.36 → 1428.78] How do you actually do fine-tuning locally in, you know, a company's tenant?
[1429.56 → 1432.42] That's actually an infra problem that, you know, we're happy to talk more about.
[1432.52 → 1434.12] But maybe I'll just, I'll pass it back to you, Chris.
[1434.74 → 1438.72] Actually, I'm about to ask a follow-up about that because you've got me really thinking
[1438.72 → 1441.74] about some of the use cases in my own life on that.
[1442.30 → 1447.12] And so with the self-hosting model, and you're able to now, you kind of like, you know, OpenAI,
[1447.34 → 1451.24] I said, you know, with chat GBT4, there's only so far we're going to go because we've kind
[1451.24 → 1455.50] of, we've used the public corpus of knowledge out there on the internet, you know, so there's
[1455.50 → 1459.14] only so much more vertical scaling you can do on the model learning.
[1459.14 → 1466.10] And so, you know, you're touching on the fact that there's so much hidden IP in code, hidden
[1466.10 → 1471.88] information in code that is of huge value, particularly to the company that it's in, because
[1471.88 → 1476.32] it's representing their business model and the way their business has evolved over time.
[1476.78 → 1481.68] And so if I'm understanding you correctly, you're basically saying that your solution can
[1481.68 → 1486.26] take advantage of that on their behalf and really, really hone against it.
[1486.58 → 1488.32] What are some of the limits on privacy?
[1488.32 → 1489.78] Are they able to do that?
[1489.90 → 1491.20] Because that's a big topic.
[1491.34 → 1495.42] We've actually talked about it on the show before about, you know, in this generative AI
[1495.42 → 1500.00] age with IP concerns and privacy concerns and, you know, getting the lawyers involved.
[1500.56 → 1506.12] Are you able to do the training on their site and keep it to the customer entirely?
[1506.52 → 1509.08] Or do they have to let their IP out and stuff?
[1509.12 → 1510.76] How do you approach that, that problem?
[1511.40 → 1511.52] Yeah.
[1511.60 → 1516.50] I mean, so one of just the answer to any question of like, does any IP leave coding for enterprises?
[1516.50 → 1517.42] The answer is always no.
[1517.42 → 1522.90] So in pretty much every part of the system, like our guarantee is to actually be able
[1522.90 → 1525.24] to deploy this whole thing fully air gapped.
[1525.46 → 1529.88] We've even deployed in places like, you know, AWS COV cloud, which is like entirely, you
[1529.88 → 1531.82] know, doesn't even have a connection with the internet kind of scenario.
[1532.00 → 1533.72] So nothing ever leaves there.
[1533.72 → 1537.98] To address some of the points you brought up there, Chris, like, yeah, I mean, we're not
[1537.98 → 1542.14] like the only ones who are like saying like, oh no, the data that a company has privately
[1542.14 → 1543.30] is like super important.
[1543.84 → 1546.36] And it's potentially even more important than the size of the model.
[1546.70 → 1549.54] I think, you know, a good example, this is actually meta.
[1549.98 → 1554.26] Instead of using like a GitHub copilot or any generic system, they decided in, you know,
[1554.26 → 1558.64] I guess classic meta fashion to like to train their own autocomplete model internally using
[1558.64 → 1559.68] all of their code.
[1560.30 → 1563.58] And they actually, you know, published a paper, I think a few weeks back.
[1564.12 → 1569.66] And their model was like, in terms of size, I think 1.3 billion parameters, like small
[1569.66 → 1571.64] in respect to the LLM world.
[1571.84 → 1575.82] And it just massively outperformed GitHub copilot on pretty much every task.
[1576.12 → 1579.28] There's definitely corroborating evidence to, you know, what we're saying about fine-tuning
[1579.28 → 1585.26] that doing this actually does lead to materially better performances for, you know, the user
[1585.26 → 1585.76] in question.
[1585.96 → 1588.30] Now, does that metamodel going to be good for everyone else to code?
[1588.84 → 1589.74] Probably not.
[1590.08 → 1592.08] But that's also not the whole point, right?
[1592.10 → 1596.14] And in terms of like being able to fine tune locally, yeah, we're able to, you know, do
[1596.14 → 1596.98] this completely locally.
[1597.02 → 1600.06] And again, it comes down to like, you know, scale of data.
[1600.36 → 1603.88] Our base model has been trained on trillions of tokens of code, right?
[1603.90 → 1604.52] That's a lot.
[1604.60 → 1608.92] That's what we need this like, you know, multi node GPU setup to do all this training.
[1609.28 → 1612.94] But an actual company, you know, if they have like, say, like even 10 million lines of
[1612.94 → 1615.02] code, that's about 100 million or so tokens.
[1615.50 → 1619.70] There's like a huge order of magnitude difference still between this pre-training and the fine
[1619.70 → 1624.92] tuning, which is why we can do this kind of locally on actually surprisingly, whichever
[1624.92 → 1627.88] hardware they choose to provision for serving their developers.
[1628.54 → 1631.98] So again, this comes to some of our like ML inference background and all the stuff that
[1631.98 → 1632.52] we know how to do.
[1632.74 → 1637.52] We actually can do fine-tuning and inferences on that same piece of hardware.
[1637.52 → 1641.02] So we don't actually ask, you know, companies to provision more hardware.
[1641.26 → 1647.62] And even more like critically, we are able to do fine-tuning during any idle time of that
[1647.62 → 1648.00] GPU.
[1648.46 → 1652.24] So whenever that GPU is not being used to perform an inference, it's actually doing like, you
[1652.24 → 1655.22] know, backdrop steps to like continuously improve the model.
[1655.76 → 1658.90] You know, fine-tuning is just one aspect of like a larger kind of personalization system.
[1658.90 → 1664.40] But, you know, we've instrumented all of this on hardware using our infra routes to actually
[1664.40 → 1667.58] create a system that is relatively easy to manage.
[1667.66 → 1672.30] It's not like crazy amount of overhead for any company to manage or use Sodium, but still
[1672.30 → 1675.76] get like, you know, the maximum possible wins from these AI tools.
[1676.48 → 1676.52] Okay.
[1676.68 → 1678.16] So that is super cool.
[1678.44 → 1683.14] And you mentioned things like Gov Cloud, which I have actually worked in because in my day job
[1683.14 → 1687.84] quite a bit, and I can think of a bunch of other use cases for me personally, which
[1687.84 → 1694.40] begs the question about kind of going back for a moment because we are a practical AI and
[1694.40 → 1698.00] we like to always give some practical routes for people into that.
[1698.20 → 1703.26] So if we're going to go back toward the beginning of the conversation for a moment, and we have
[1703.26 → 1707.56] some folks that are listening to this right now, and they've been using Copilot for a while,
[1707.56 → 1713.30] they're probably putting code into ChatGPT and trying to accelerate there with varying
[1713.30 → 1714.36] degrees of success.
[1714.64 → 1719.34] They've been experimenting with BARD and BARD's gotten better on code lately, obviously.
[1719.34 → 1725.08] And so, so many people that I talk to are still very frustrated with kind of the workflow
[1725.08 → 1730.46] of the whole thing and recognizing that there are these, you've outlined these differentiators,
[1730.64 → 1734.84] you know, from Copilot and other competition out there in a friendly competition kind of way.
[1734.84 → 1741.56] Talk a little bit about some of the specific generative AI use cases that would be good if
[1741.56 → 1745.14] someone was in that position where they're like, yeah, I'm using the stuff, but I'm not
[1745.14 → 1745.72] real.
[1745.78 → 1747.10] I'm a little bit frustrated with it.
[1747.18 → 1748.06] I don't have it down.
[1748.46 → 1754.74] And if they were to give Sodium that chance and dive in on it, can you give me several kinds
[1754.74 → 1759.18] of layout the use cases on what is, what are they going to get when they move in from
[1759.18 → 1764.72] a very practical, like for me now as the coder perspective, what will that look like?
[1764.86 → 1765.78] What are they nonusing?
[1765.90 → 1769.92] And maybe give me a couple of different ones because I'm really, I'm really curious and
[1769.92 → 1773.14] selfishly, I'm probably going to go try each of these that you're telling me.
[1773.46 → 1775.78] So I'm scratching my own itch by asking the question.
[1776.26 → 1780.02] I think you pointed out like, yeah, workflows and the user experience for a lot of AI tools,
[1780.12 → 1781.78] like everyone's still kind of trying to figure it out, right?
[1781.78 → 1784.14] We're still in very early days of these AI applications.
[1784.64 → 1787.32] And this is our learnings of trying to become a product company.
[1787.32 → 1790.22] We're actually taking like the UX quite seriously, right?
[1790.22 → 1792.98] And this is actually what the individual plan is great to get feedback on.
[1793.36 → 1797.46] I think very, you know, concretely, I think a lot of people have that frustration of like
[1797.46 → 1802.40] having to copy a code block over to ChatGPT, write out a full prompt and like, you know,
[1802.66 → 1806.36] remember the exact prompt that they typed in before that gave them a good result and then
[1806.36 → 1809.28] copying the answers back in and then making modifications.
[1809.28 → 1811.66] Like that workflow is clearly kind of broken.
[1811.66 → 1817.08] So when we actually built our chat functionality into the IDE, we're like, okay, what are all
[1817.08 → 1819.58] the parts here that can get totally streamlined, right?
[1819.64 → 1823.12] And so we actually did things like, you know, on top of every function block, there's little
[1823.12 → 1827.14] like code lenses that are just these small buttons that if someone can like click, like
[1827.14 → 1831.78] explain this function, it'll automatically pull in all that relevant context, open it
[1831.78 → 1832.44] up in the window.
[1832.54 → 1833.68] You're not copying anything over.
[1833.80 → 1836.18] And it's like writing, you know, it out in human text.
[1836.44 → 1839.70] Or if you say like refactor a function or add doc strings, right?
[1839.70 → 1843.62] Or write a unit test, these are all just like small little buttons or, you know, preset
[1843.62 → 1845.84] prompts that you can just then click.
[1846.10 → 1847.36] It'll do this generation on the side.
[1847.40 → 1849.96] And then we even have a way of clicking like apply diff.
[1850.06 → 1853.92] And because we know where we pull the context in, we can apply diff right back into the
[1853.92 → 1854.96] context, right?
[1854.98 → 1858.40] And so you're not copying things back and trying to like resolve merge conflicts.
[1858.40 → 1860.84] Like all of these things are done kind of automatically.
[1861.08 → 1864.22] So there are a lot of really cool things you can actually do when you start bringing these
[1864.22 → 1866.32] things into the IDE where developers are.
[1866.32 → 1870.78] Um, and we spent a lot of time really thinking, as you said, from a workflow point of view,
[1871.20 → 1872.72] how do you make this like super smooth?
[1873.44 → 1877.86] Varun, could you talk a little bit about maybe some specific tasks that you're seeing people
[1877.86 → 1882.70] doing when we talk about generative, and it's expanded and, you know, from LLMs, and we're,
[1882.80 → 1886.42] you know, we're doing things in video, we're doing things in a natural language.
[1886.66 → 1892.40] All the different modalities are gradually being addressed with these different models and
[1892.40 → 1894.06] different tools that are being built around it.
[1894.06 → 1899.34] Could you talk a little bit about, you know, what are people trying to code right now?
[1899.90 → 1902.68] What specifically is Sodium helping them?
[1902.82 → 1907.12] Like what, not just about Sodium, but the actual use cases themselves so that they go,
[1907.28 → 1908.90] ah, I can see a path forward.
[1908.98 → 1910.82] I can, I can go do that.
[1910.92 → 1914.70] I know how to generate this or that or the other with generative AI in Sodium.
[1914.78 → 1917.68] Can you talk a little bit about those and something of a specific level?
[1917.68 → 1922.96] So interestingly, just a little bit about multi-modality, I think we're maybe a little
[1922.96 → 1926.96] bit far from leveraging, I guess, other modes beyond text for code.
[1927.20 → 1931.12] I think maybe that that'll happen, but I think there's not enough evidence right now yet.
[1931.24 → 1936.38] For autocomplete, just to be open about the sort of the functionality we have, we have autocomplete,
[1936.38 → 1938.96] we have search, and we have code-based aware chat, right?
[1939.26 → 1944.20] So for, we recognize right now that of the usage, autocomplete accounts for more than
[1944.20 → 1946.28] 90 to 95% of the usage of the product.
[1946.52 → 1950.12] It's because chatting is not something people do like even every day, potentially.
[1950.30 → 1953.82] They might open it up once every couple of days, but autocomplete is something that's
[1953.82 → 1958.34] like always on very passively helpful and people get the most value out of it, which
[1958.34 → 1959.40] is kind of counterintuitive.
[1959.52 → 1963.84] I think people don't recognize that immediately, but when people are doing autocomplete, we've
[1963.84 → 1966.32] recognized there's like two modalities, right?
[1966.38 → 1967.82] Of the way people type code.
[1968.00 → 1972.20] There's a modality of accelerating the developer, which is like, Hey, I kind of know what I'm
[1972.20 → 1974.54] going to type and I just want to tab complete the result.
[1974.66 → 1978.92] And then there is also an exploration phase, which is like, I don't even know what I'm trying
[1978.92 → 1980.02] to do based on that.
[1980.12 → 1980.76] I write a comment.
[1980.98 → 1984.58] This is like a classic thing where like my behaviour writing code is materially changed
[1984.58 → 1988.12] because of tools like Sodium, where I'll write a comment and I kind of just hope and
[1988.12 → 1992.28] pray that it pulls in the right context so that it gives me the best generation possible.
[1992.28 → 1996.88] So in my mind for the acceleration case, Sodium is like very helpful, right?
[1996.92 → 2000.44] It can like autocomplete a bunch of code, but to make the exploration case, that's where
[2000.44 → 2004.66] the true magical moment comes in where I had like no clue at like how I was going to use
[2004.66 → 2005.52] a bunch of these APIs.
[2005.92 → 2010.30] And that's sort of what we're focused on trying to make really better, whether that
[2010.30 → 2012.40] be in chat as well as with autocomplete.
[2012.70 → 2017.52] How do we make it so that we can build the most knowledgeable AI that is maximally helpful
[2017.52 → 2019.88] and also minimally just like annoying.
[2019.88 → 2024.60] The interesting thing about Sodium as a product or these autocomplete products is they get
[2024.60 → 2028.62] a little bit of getting used to, but even despite the fact that they write wrong things,
[2028.92 → 2032.72] it's not very annoying because you can very easily just say, I don't want this completion
[2032.72 → 2037.78] or it didn't like to write an entire file out, and you need to go and correct a bunch of functions.
[2037.92 → 2040.64] It was like a couple of lines or maybe like 10 lines of code.
[2040.72 → 2042.96] You can very easily validate that it's correct, right?
[2043.28 → 2047.46] That comes back to then what Annul was saying, which is how do we make sure we can provide
[2047.46 → 2050.96] always the maximally helpful sort of AI agent?
[2051.40 → 2053.66] The answer is had the best context possible.
[2054.02 → 2058.02] And a couple of nitty-gritty details we do is currently our context, and we'll write a blog
[2058.02 → 2060.18] post about this is double what Copilots is.
[2060.48 → 2064.00] We allow double the amount of context for autocomplete than what they do.
[2064.34 → 2067.68] The second thing is we're able to pull context throughout the code base.
[2067.88 → 2072.22] And this is actually that same piece of technology that is pulling context throughout the code base
[2072.22 → 2077.10] through search and all these other functionalities is getting used as part of chat for code base
[2077.10 → 2080.18] aware chat, which is something that Copilot doesn't even have today yet.
[2080.62 → 2082.92] The third piece is finally for a large enterprise.
[2083.20 → 2087.08] How do we make it so that these models actually semantically understand your code,
[2087.18 → 2088.68] which is where fine-tuning comes in.
[2088.82 → 2093.14] It's like for us, context gets us a lot of the way, but it doesn't get us all the way
[2093.14 → 2097.28] because you can just imagine even with double the context, let's say we can pass in a thousand
[2097.28 → 2100.34] lines of code for a company with 10 million lines of code.
[2100.46 → 2104.06] We're scratching four orders of magnitude less code than the company actually has.
[2104.38 → 2109.48] So this is where our vision is like we want to continually ramp up the amount of knowledge
[2109.48 → 2112.14] these models have and the ways in which they can be helpful.
[2112.38 → 2113.90] I don't know if that answered the question there.
[2113.90 → 2118.52] It did actually your acceleration versus exploration analogy.
[2118.76 → 2123.56] That was for me personally, different people get different things that really clarified for
[2123.56 → 2129.06] me where I might be using Copilot or where I would go and use Sodium on that because I
[2129.06 → 2131.64] do struggle on the exploration side myself.
[2131.94 → 2135.48] It's a lot easier on the acceleration yet into the line and the line, you know, and crank
[2135.48 → 2139.40] through that fast, which I've been able to do with these other tools.
[2139.64 → 2144.10] But I have struggled on the exploration side because I kind of want to do a thing, and I'm
[2144.10 → 2147.34] kind of trying to figure it out, and I'm just going to kind of see where my fingers lead
[2147.34 → 2147.84] on that.
[2148.32 → 2153.54] And having that ability to support that in the way you described, that gave me a very clear
[2153.54 → 2155.38] understanding from my standpoint.
[2156.00 → 2161.96] So I'd like to ask each of you where this is going, both in the large and in your specific
[2161.96 → 2163.76] concern with Sodium.
[2164.20 → 2168.32] You know, things have never moved faster than they're moving right now in terms of how fast
[2168.32 → 2170.72] these technologies are progressing.
[2171.00 → 2172.78] And Daniel and I have a habit.
[2172.92 → 2175.60] We were commenting on our last episode about this.
[2175.60 → 2180.08] We have a habit of saying, yeah, we recently mentioned this thing and that we'd get to it,
[2180.20 → 2182.06] but then we turn around, and we end up talking about that.
[2182.06 → 2185.16] We just got there way faster than we ever anticipated.
[2185.58 → 2190.00] With the speed of generative AI and, you know, you're already creating these amazing tools
[2190.00 → 2194.36] and stuff like that, and you're having to stay out front, where's your brain taking you at
[2194.36 → 2194.58] night?
[2194.68 → 2198.48] You know, when you stop, and you chill out and have a glass of wine or whatever you do
[2198.48 → 2202.20] and you're kind of just pondering, what does the future look like?
[2202.28 → 2207.82] And I'd like to know both from your own specific personal standpoints in terms of your product
[2207.82 → 2210.82] and that, but just the generative AI world in general.
[2211.00 → 2212.30] How do you see it going forward?
[2212.40 → 2213.16] I'd love your insights.
[2213.68 → 2213.78] Yeah.
[2213.88 → 2218.10] I think the classic question and then the grand scheme of things is like, oh my God, is
[2218.10 → 2222.48] like generative AI just going to like totally get rid of my job or completely like invalidate?
[2222.48 → 2227.74] And I think for us, we will be the first people to say that, you know, we do think like AI
[2227.74 → 2232.06] would just be like the next step in a series of, at least in code or a series of tools that
[2232.06 → 2234.68] have had made like developers more productive, right?
[2234.68 → 2240.42] That have led them to be able to focus on more kind of interesting parts of software development
[2240.42 → 2242.58] and, you know, be an assistant, right?
[2242.66 → 2245.44] All these tools are called AI assistant tools, I think, for a reason.
[2245.44 → 2248.34] You know, we're definitely not at a place yet.
[2248.44 → 2252.58] I don't think for a while where there isn't going to be like a human in the loop, like
[2252.58 → 2256.24] in control, you know, guiding the AI and what to do.
[2256.68 → 2261.16] So from that kind of respect, like the doomsday scenario, I don't want to speak for a room,
[2261.20 → 2263.40] but I think we're like pretty far from that mentality.
[2263.52 → 2267.74] But we do think, I think, you know, we wouldn't have gotten into Sodium if we didn't genuinely
[2267.74 → 2272.10] think that there was just so many things that we do as a day-to-day as engineers that are
[2272.10 → 2276.48] just a little frustrating, boring, kind of take us out of the flow state, you know, slow
[2276.48 → 2277.16] us down.
[2277.62 → 2282.12] Those all seem like very prime, ripe things to like try to address with AI, right?
[2282.12 → 2284.06] And I think that's kind of our general goal, right?
[2284.06 → 2286.80] I think there are a lot more capabilities to build, right?
[2286.88 → 2292.02] I don't think search, chat, these are going to be the last, I guess, like building blocks
[2292.02 → 2292.48] that we build.
[2292.64 → 2295.68] We have more capabilities coming up that we're super excited about.
[2295.92 → 2299.06] But yeah, it's also like, you know, going to be a thing where, as you said, this is moving
[2299.06 → 2299.94] super quickly, right?
[2299.94 → 2304.50] Like we have like research, open source, like applications all developing at the same
[2304.50 → 2306.36] time at brick next speed.
[2306.76 → 2310.98] And so I think part of what we're also looking forward to is like, how can we also just like
[2310.98 → 2315.52] educate, like, you know, at least software developers on the best way to use AI tools,
[2315.58 → 2319.58] how to like best make the most use of it so that they are part of the way for it and that
[2319.58 → 2321.44] they also can get a lot of value.
[2322.06 → 2322.38] Well said.
[2322.64 → 2322.96] Varun?
[2323.32 → 2323.64] Yeah.
[2323.70 → 2327.28] Maybe if I was to just say, like, you were asking me what the big worry is.
[2327.28 → 2331.54] For me, the big worry is there's going to be a lot of like exciting new demos that people
[2331.54 → 2332.10] end up building.
[2332.70 → 2336.96] And obviously for us as a company, we need to make strategic bets on like, hey, this is
[2336.96 → 2338.72] a worthwhile thing for us to invest in.
[2339.12 → 2343.00] For instance, I think a couple of months ago, there was an entire craze on agents being able
[2343.00 → 2347.22] to write like entire pieces of code for you and all these other things.
[2347.70 → 2351.20] For us, though, we had lots of enterprise companies that were sort of using the product
[2351.20 → 2354.66] at the time and recognize that the technology just wasn't there yet, right?
[2354.66 → 2358.22] Like take a code base that's like 100 million lines of code or 10 million lines of code.
[2358.40 → 2362.88] It's going to be hard for you to write C++ that's like five files that compiles perfectly
[2362.88 → 2366.88] and then also like uses all the other libraries when you have context that's like, you know,
[2366.88 → 2367.54] five files.
[2367.90 → 2369.22] It's not going to be the easiest problem.
[2369.64 → 2370.90] And I think that's maybe an example.
[2371.16 → 2376.00] But for us, we've currently, I would say, just a pat on the back over the last eight months,
[2376.26 → 2380.16] iterated like significantly faster than every other company in this space, just in terms
[2380.16 → 2380.92] of the functionality.
[2380.92 → 2385.46] But we need to make strategic bets on what the next thing to sort of work on is at any
[2385.46 → 2385.94] given point.
[2386.42 → 2390.40] And we need to be very careful about like, hey, this is like a very exciting area.
[2390.40 → 2393.72] But is it like actually useful to our users, right?
[2393.76 → 2398.02] Like, is it actually useful in that, hey, like maybe we could do something where a great
[2398.02 → 2400.76] example is given a PR, we generate a summary.
[2400.92 → 2403.84] And I think Copilot has tried building something like this.
[2403.94 → 2408.60] And we tried using the product that Copilot had, and it was just wrong a lot of the times.
[2408.60 → 2412.72] And I think that would have been an interesting idea for us to pursue and keep trying to make
[2412.72 → 2413.02] work.
[2413.14 → 2415.14] But then there is a diminishing return.
[2415.34 → 2420.24] And I think Annul and I have seen this very clearly in autonomous vehicles, where we had
[2420.24 → 2422.68] a piece of technology that was kind of just not there yet.
[2422.82 → 2425.92] Like it needs a couple more breakthroughs of machine learning to kind of get there.
[2426.36 → 2430.18] And the idea of building it five years in advance, right, you shouldn't be doing that.
[2430.36 → 2433.98] You just 100% shouldn't be building a tool when the technology just isn't there yet.
[2433.98 → 2438.90] And that is something that keeps me up at night is like, what are the next things we need to build
[2438.90 → 2443.20] while keeping in mind of this is what the technological capability set is like today,
[2443.66 → 2444.66] if that makes sense.
[2445.08 → 2445.46] It does.
[2445.56 → 2448.94] And it's a very practical AI perspective, if you will.
[2449.08 → 2451.94] So very fitting final words for the show today.
[2452.60 → 2456.24] Well, Varun and Annul, thank you very, very much for coming on the show.
[2456.62 → 2457.48] It's fascinating.
[2457.68 → 2462.50] I got a lot of insight, a lot of new things to go explore from what you just taught me.
[2462.50 → 2463.86] And I appreciate your time.
[2463.98 → 2464.68] Thank you for coming on.
[2464.94 → 2465.50] Thanks for having us.
[2465.76 → 2466.34] Thanks a lot, Chris.
[2475.04 → 2477.42] Thank you for listening to Practical AI.
[2478.02 → 2481.76] Your next step is to subscribe now, if you haven't already.
[2482.20 → 2486.88] And if you're a longtime listener of the show, help us reach more people by sharing Practical
[2486.88 → 2488.22] AI with your friends and colleagues.
[2488.22 → 2493.62] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2494.20 → 2497.98] Check out what they're up to at Fastly.com and Fly.io.
[2498.38 → 2502.98] And to our Beat Freakin' Residence, Break master Cylinder, for continuously cranking out the best
[2502.98 → 2503.70] beats in the biz.
[2504.00 → 2504.88] That's all for now.
[2505.18 → 2506.30] We'll talk to you again next time.
[2506.30 → 2522.26] Regime!
