[0.00 --> 9.72]  Welcome back, friends.
[9.72 --> 14.22]  This week on the change law, we're taking you to the hallway track of the Linux Foundation's
[14.22 --> 18.06]  Open Source Summit North America 2023 in Vancouver, Canada.
[18.50 --> 24.02]  This episode is part of our Maintainer Month celebration, along with GitHub and many others.
[24.38 --> 27.44]  Check it out at maintainermonth.github.com.
[27.44 --> 32.90]  Today's Anthology episode features Byung Liu, co-founder and CTO at Sourcegraph,
[32.90 --> 41.44]  Danny Lee, developer advocate at Databricks, and Stella Biederman, executive director and head of research at Eleuther AI.
[41.92 --> 46.08]  The common denominator of these conversations is open source AI.
[46.72 --> 51.76]  Byung Liu and his team at Sourcegraph are focused on enabling more developers to understand code,
[51.76 --> 59.34]  and their approach to a completely open source model agnostic coding assistant called Cody has significant interest from us.
[59.76 --> 63.54]  Danny Lee and the team at Databricks recently released Dolly 2.0.
[63.92 --> 71.56]  This is the first open source instruction following LLM that has been fine-tuned on a human-generated instruction data set
[71.56 --> 74.94]  and is licensed for research and commercial use.
[75.52 --> 82.82]  And Stella Biederman gave the keynote address on generative AI and works at the base layer doing open source research,
[83.26 --> 84.92]  model training, and AI ethics.
[85.34 --> 91.00]  She trained the Eleuther AI Pythia model family that Databricks used to create Dolly 2.0.
[91.46 --> 98.22]  A massive thank you to our friends at GitHub for sponsoring us to attend this conference as part of Maintainer Month.
[98.22 --> 115.86]  Okay, before the show kicks off, I'm here with one of our sponsors at DevCycle, CTO and co-founder Jonathan Norris.
[116.30 --> 121.50]  So Jonathan, my main question, I guess, if I'm handing off my feature flags to you all,
[121.74 --> 125.02]  is my uptime dependent on your uptime?
[125.12 --> 127.66]  Like, if you're down, am I down?
[127.66 --> 131.46]  We've designed into all the SDKs and all the APIs.
[131.66 --> 132.56]  APIs fail, right?
[132.64 --> 134.42]  That's a cardinal rule of the internet.
[135.22 --> 140.84]  So all the SDKs have been designed with kind of defaults and caching mechanisms and all that stuff in place
[140.84 --> 146.94]  so that, yeah, if our CDN is down or our APIs are down, it'll sort of fall back to those defaults
[146.94 --> 149.32]  or those cache values in those SDKs.
[149.34 --> 151.62]  So that handles for those blips pretty easily.
[151.70 --> 156.78]  And then we rely on Cloudflare as our sort of main high-load edge provider.
[156.78 --> 161.90]  So all of our edge APIs are through Cloudflare and they're also operating as our CDN for assets.
[162.24 --> 166.78]  So obviously relying on a large provider like that that runs such a large percentage of the internet
[166.78 --> 171.66]  means that, yeah, you're not relying on our ability to keep AWS instances running properly.
[172.00 --> 176.06]  You're relying on sort of Cloudflare and ability to sort of make sure the internet still works
[176.06 --> 178.48]  as they control such a large percentage of it.
[178.48 --> 183.94]  So yeah, we've architected it in a way that it doesn't sort of rely on our APIs to be up all the time
[183.94 --> 187.82]  and our databases to be up all the time to have that good reliability.
[188.46 --> 189.14]  Well, that's good news.
[189.38 --> 191.52]  Okay, so how do you accomplish that?
[191.88 --> 196.40]  One of the core sort of architectural decisions we made with our platform when we designed it
[196.40 --> 203.00]  was trying to move the decisioning logic of your feature flags as close to the end user and end device as possible.
[203.00 --> 209.18]  So we did that with those local bucketing server SDKs that are using sort of a shared WebAssembly core.
[209.56 --> 216.14]  And then we have edge-based APIs that are also powered by WebAssembly to serve sort of those client SDK usages.
[216.28 --> 218.30]  So things like web and mobile apps.
[218.50 --> 224.40]  So that's one of our core principles is to try to get that decisioning logic as close to the end device as possible.
[224.56 --> 227.78]  And this is probably one of the only use cases where performance really matters
[227.78 --> 232.38]  because you want your feature flags to load really, really quickly so you can render your website
[232.38 --> 234.66]  or you can render your mobile app really quickly.
[234.88 --> 238.62]  And so, yeah, we definitely understand that your feature flagging tool needs to be fast
[238.62 --> 240.70]  and needs to be really, really performant.
[241.22 --> 244.28]  So if you want a fast feature flagging tool that's performant
[244.28 --> 246.88]  and is not going to impact your uptime,
[247.26 --> 248.78]  check out our friends at DevCycle.
[249.44 --> 252.74]  That's devcycle.com slash changelopod.
[252.74 --> 256.98]  And for those curious, they have a free forever tier that you can try out
[256.98 --> 260.48]  and prove to yourself and your team that this is going to work for you.
[260.80 --> 264.94]  So check it out, devcycle.com slash changelopod.
[265.40 --> 266.30]  And tell me I sent you.
[282.74 --> 285.64]  So, Cody.
[286.30 --> 287.10]  Yeah, Cody.
[287.20 --> 287.48]  Cody.
[287.80 --> 288.36]  This is a big deal.
[289.36 --> 290.16]  We think it is.
[290.20 --> 290.70]  Seems like it.
[290.70 --> 290.82]  Yeah.
[291.70 --> 297.42]  Wasn't it Sourcegraph 4.0 last year was relaunched as the intelligence platform?
[297.60 --> 297.80]  Yep.
[297.88 --> 298.30]  Is that right?
[298.52 --> 302.08]  Because before, not just, but just code search, which was cool,
[302.20 --> 305.08]  but hard to really map out the ecosystem.
[305.30 --> 309.24]  And you want all the space in there, but there was a limit to code search.
[309.24 --> 312.14]  And you had to expand the insights and the intelligence.
[312.38 --> 315.14]  And now, obviously, Cody is just like one more layer on top of insights.
[315.36 --> 315.84]  Yeah, totally.
[316.08 --> 321.12]  So, as you know, Sourcegraph historically has been focused on the problem of code understanding.
[321.38 --> 321.52]  Right.
[321.64 --> 326.76]  So heavily inspired by tools like CodeSearch inside Google or TPGS inside Facebook.
[326.88 --> 327.08]  Right.
[327.20 --> 330.16]  These kind of systems that indexed your company-wide code base
[330.16 --> 334.42]  as well as your open source dependencies and made that easy to search and navigate.
[335.92 --> 339.02]  And that's what's been powering the business for the past 10 years.
[339.02 --> 343.22]  This is actually, you know, the 10th year of building Sourcegraph.
[343.42 --> 344.58]  I was just wondering about that.
[344.58 --> 344.74]  Wow.
[344.74 --> 347.86]  Because when we first met you, it had to be about a decade ago.
[348.16 --> 348.30]  Yeah.
[348.42 --> 352.84]  I think Sourcegraph just either didn't exist or just had existed.
[353.24 --> 354.42]  Sourcegraph existed when we met.
[354.66 --> 355.48]  This was like GopherCon.
[355.48 --> 356.58]  I think it was like 2014.
[357.28 --> 358.04]  The first or second GopherCon.
[358.04 --> 358.48]  GopherCon.
[358.66 --> 358.94]  Yeah.
[359.70 --> 362.64]  And you had this vision of, you know, Sourcegraph.
[362.76 --> 366.18]  And I'm wondering 10 years later, like, have you achieved that vision?
[366.26 --> 367.78]  Has the vision changed, et cetera?
[367.78 --> 372.06]  You know, our mission was always to enable everyone to code.
[372.58 --> 379.28]  And we actually took a look at our seed deck recently.
[380.32 --> 381.54]  You know, it kind of tripped down memory.
[382.20 --> 383.10]  It was very quaint.
[383.26 --> 385.48]  We were very bad at PowerPoint.
[385.72 --> 386.88]  You're probably a lot better at it now.
[387.58 --> 388.50]  Not really.
[388.74 --> 388.76]  No?
[388.76 --> 388.86]  Okay.
[389.72 --> 390.78]  Better at the pitch maybe.
[391.14 --> 391.66]  Maybe.
[391.72 --> 392.60]  You refine it just slightly.
[392.60 --> 397.12]  But largely, like, I could deliver that pitch today off that deck.
[397.16 --> 397.34]  Do it.
[397.34 --> 398.48]  It's basically the same.
[398.48 --> 398.98]  Do it right now.
[399.28 --> 403.46]  I mean, it's just the pitch of Sourcegraph, which is like there's never been more code in the world.
[404.14 --> 410.58]  Most of your job as an engineer or software creator is understanding all the code that already exists in your organization.
[410.82 --> 410.98]  Yeah.
[410.98 --> 414.12]  Because that is all upstream of figuring out what code you want to write.
[414.26 --> 414.32]  Right.
[414.32 --> 417.56]  And then once we actually figure out what you need to build, like, that's almost the easy part.
[417.62 --> 418.60]  It's also the fun part, right?
[418.64 --> 418.72]  Right.
[418.72 --> 420.34]  Because you're building new things and shipping stuff.
[420.54 --> 426.72]  But we help you get to that point of, you know, creation and enjoyment by helping you pick up all that context.
[427.10 --> 427.24]  Right.
[427.24 --> 427.32]  Right.
[427.62 --> 429.28]  Traditionally, that's been, like, search, right?
[429.32 --> 430.76]  Just like Google's been web search.
[431.20 --> 434.60]  But then these large language models have now come on the scene.
[434.72 --> 434.90]  Yeah.
[435.38 --> 438.14]  And in some ways, they're disruptive to kind of, like, search engines.
[438.30 --> 439.82]  But in other ways, they're highly complementary.
[440.24 --> 442.68]  So, you know, anyone who's used ChatTBT.
[442.68 --> 443.20]  I'm still Googling.
[443.52 --> 444.34]  I just less.
[444.56 --> 445.18]  It's just less.
[445.44 --> 445.64]  Right.
[445.70 --> 448.50]  It's more like the last thing you do when you can't get the answer elsewhere.
[448.86 --> 449.14]  Right.
[449.30 --> 451.22]  You're like, I guess I'll go Google it.
[451.66 --> 451.94]  Yeah.
[452.06 --> 452.72]  Although technically.
[452.72 --> 456.92]  Google is a weird thing because I will search a product and they think I want to buy it.
[456.92 --> 457.82]  Not research it.
[458.46 --> 458.66]  Right.
[458.66 --> 462.74]  It's like, I want to learn about the thing and those who are teaching about the thing.
[462.90 --> 463.10]  Yep.
[463.16 --> 464.44]  And how it integrates other things.
[464.78 --> 466.48]  Not where can I buy it and for how much.
[466.58 --> 466.74]  Yeah.
[466.90 --> 468.34]  So there's, like, zero context there.
[468.40 --> 473.24]  Like, they're incentivized, it seems, to point you to places that you can purchase it.
[473.46 --> 473.60]  Yeah.
[473.60 --> 475.52]  Not learn how to use it.
[475.56 --> 475.98]  Yeah, yeah.
[476.06 --> 477.36]  I mean, I think there's an interesting discussion.
[477.36 --> 478.76]  Which is the opposite of ChatGPT.
[479.78 --> 480.14]  Yeah.
[480.14 --> 483.72]  So there's kind of, like, pluses and minuses to both, right?
[483.72 --> 489.30]  Like, with Google, you get results to actual web pages and you can kind of judge them based
[489.30 --> 489.92]  on the domain.
[490.16 --> 492.86]  And it's kind of like more primary source material, which is useful.
[493.02 --> 493.80]  It's also live.
[494.32 --> 497.52]  You know, you get results from 2023 rather than 2021.
[497.86 --> 498.04]  Sure.
[498.30 --> 499.26]  Whereas ChatGPT.
[499.52 --> 499.84]  That'll change.
[500.98 --> 502.10]  That's a temporary thing, right?
[502.18 --> 504.04]  I mean, the delay will be temporary.
[504.24 --> 505.36]  Eventually, it'll catch up.
[505.94 --> 508.96]  Well, I mean, GPT-4 is still, it came out recently.
[508.96 --> 509.78]  2021, right?
[509.78 --> 510.36]  It's still 2021.
[510.36 --> 514.52]  Right, but isn't the plugins and all that stuff where it's like, okay, the model is old,
[514.66 --> 515.82]  but it has access to new data.
[516.02 --> 519.60]  So the plugins is actually where it gets interesting because that's where things get really powerful,
[519.70 --> 520.14]  in my opinion.
[520.28 --> 520.38]  Yeah.
[520.38 --> 524.12]  Because if you ask ChatGPT with the plugins enabled, it can go and browse the web on your
[524.12 --> 524.56]  behalf.
[525.48 --> 532.70]  So it's not just the base model, you know, trying to answer your question from memory anymore.
[532.86 --> 536.26]  It's actually going stuff and essentially Googling for things, right?
[536.26 --> 538.44]  Yeah, it's like it has access to what you would do.
[538.44 --> 539.26]  Behind the scenes.
[539.42 --> 539.66]  Exactly.
[539.66 --> 540.14]  Yeah.
[540.46 --> 540.86]  Exactly.
[541.06 --> 542.24]  So it's the best of both worlds.
[542.42 --> 546.88]  And essentially, we're doing that with Kodi, but in your editor for developers.
[547.22 --> 555.20]  So basically combining large language models like GPT-4 or AnthropX Claude model and then
[555.20 --> 559.16]  combine that with power with the most advanced code search engine in the world.
[559.62 --> 561.06]  So it's the best of all worlds.
[561.56 --> 565.82]  It gives you highly context aware and specific answers about your code.
[565.82 --> 569.82]  And it can also generate code that's kind of tuned to the specific patterns in your code
[569.82 --> 574.26]  base, not just the kind of like median stack overflow or open source code.
[574.70 --> 575.54]  How did you get there?
[575.60 --> 576.70]  How did you think, wow?
[576.78 --> 578.88]  I mean, obviously, LLMs are a big deal.
[579.18 --> 579.36]  Yep.
[579.36 --> 579.88]  Right.
[579.88 --> 579.92]  Right.
[580.02 --> 583.44]  This new wave of intelligence that we have access to.
[584.24 --> 586.62]  How far back is this in the making?
[586.74 --> 587.90]  Has this been years?
[588.16 --> 590.72]  Or has it been like, wow, Chet GPT is crazy.
[590.88 --> 591.18]  November.
[591.38 --> 593.56]  Chet GPT-3 is in November.
[593.56 --> 594.04]  Okay.
[594.20 --> 594.88]  We got to move.
[594.88 --> 596.38]  How far back does this go?
[596.54 --> 596.70]  Yeah.
[596.80 --> 597.22]  Good question.
[597.36 --> 597.50]  Yeah.
[597.54 --> 600.64]  So for me personally, it's kind of a bit of a homecoming.
[600.84 --> 605.24]  So like my first interest in computer science actually was machine learning and artificial
[605.24 --> 605.72]  intelligence.
[605.72 --> 607.96]  That's what I did a lot of my undergrad doing.
[607.96 --> 612.74]  It was actually part of the Stanford AI lab doing vision research in those days under
[612.74 --> 614.12]  Professor Daphne Kohler.
[614.22 --> 614.92]  She's my advisor.
[615.70 --> 617.12]  And so I did a lot of work there.
[617.22 --> 618.14]  It was super interesting.
[618.56 --> 620.20]  And I felt really passionate about it.
[620.26 --> 623.18]  There's just a lot of elegant math that goes into things.
[623.18 --> 626.58]  And it feels like you're kind of like poking at some of the hidden truths of the universe
[626.58 --> 627.44]  a little bit.
[628.40 --> 632.86]  But the technology at that point was just, it was nowhere near commercializable.
[633.58 --> 637.88]  And so I decided to pursue my other passion, which is developing productivity and dev tools
[637.88 --> 642.40]  and kind of like stayed on top of the research as it was coming along.
[642.58 --> 647.88]  And I think one of the inflection points for us was the release of GPT-3 because that was
[647.88 --> 651.38]  kind of a step function increase in the quality of the language models.
[651.38 --> 656.38]  And we started to see some potential applications to developer tools and code.
[657.06 --> 662.50]  And we really started in earnest maybe a little over a year ago, maybe 12 to 18 months ago,
[662.80 --> 667.76]  experimenting with the kind of like internal representations of language models as a way
[667.76 --> 668.98]  to enhance code search.
[668.98 --> 676.72]  So we actually put out an experiment called code search.ai that uses embeddings to enhance
[676.72 --> 680.54]  the quality of code search results that you get.
[680.74 --> 682.66]  And that was pretty successful as an experiment.
[683.14 --> 687.28]  I think we released that probably middle of last year, so about a year ago.
[687.82 --> 689.56]  And that kind of started us down the road.
[689.56 --> 694.48]  And then, of course, when ChatGPT came out, that was also another big inflection point.
[694.98 --> 700.52]  And that's when we started to think very seriously about kind of like a chat-based interaction
[700.52 --> 705.72]  that could happen in your editor, have all the advantages of ChatGPT, but know about the
[705.72 --> 706.96]  specific context of your code.
[707.24 --> 713.18]  And so for Cody specifically, I think first commit was December 1 or something like that.
[713.18 --> 718.14]  By February, we basically had a version that we're having users and customers try.
[718.40 --> 721.30]  And then March was when we rolled out to our first enterprise customer.
[721.52 --> 724.18]  So it's just been like this whirlwind of development activity.
[725.56 --> 731.82]  And I don't know, I cannot remember a time where I've been more excited and just eager
[731.82 --> 735.54]  to build stuff because we're living through interesting times right now.
[735.64 --> 735.90]  It is.
[736.02 --> 736.12]  Yeah.
[736.20 --> 740.96]  This is the eureka moment that we've all been waiting for, basically, right?
[740.96 --> 745.84]  I mean, this is the invention of the internet all over again, potentially the iPhone level
[745.84 --> 746.82]  invention.
[746.98 --> 752.02]  I think it's a dramatic paradigm shift in how we think as engineers and software developers.
[752.30 --> 753.70]  Like, how do we learn?
[753.98 --> 754.98]  How do we leverage?
[755.22 --> 756.00]  How do we augment?
[756.36 --> 756.44]  Yeah.
[756.74 --> 762.26]  You know, it's just insane what is available to somebody who doesn't have an understanding
[762.26 --> 766.92]  to quickly get understanding and then be, you know, performant in a certain task or whatever
[766.92 --> 770.02]  because of the LLMs that are available and how it works.
[770.02 --> 770.64]  It's so crazy.
[770.64 --> 774.12]  The chat interface is pretty simple though, right?
[774.22 --> 776.50]  Like the simplicity of a chat interface.
[777.06 --> 781.24]  Did you expect this eureka moment to be simply chat?
[781.80 --> 783.12]  Like as you've been, you know what I mean?
[783.40 --> 785.18]  Like it's a web app.
[785.42 --> 785.56]  Yeah.
[785.68 --> 787.16]  It's not something else.
[787.22 --> 788.30]  It's a web interface.
[788.42 --> 789.42]  It's a chat interface.
[789.84 --> 793.62]  I think, so, you know, I'm a programmer by background.
[793.62 --> 798.34]  So I've been like pushing, I've been trying to spread the gospel of textual based input
[798.34 --> 800.68]  for, you know, as long as I can remember.
[800.86 --> 804.78]  Obviously, it's mostly fallen on deaf ears because, you know, the non-programming world
[804.78 --> 806.92]  is like, you know, command line.
[807.04 --> 808.22]  That's what are we in?
[808.30 --> 809.56]  Like the 1980s.
[809.56 --> 809.84]  Right.
[811.04 --> 817.66]  But I actually think philosophically, like textual input, the reason I like it is because
[817.66 --> 822.28]  if you think about just like the IO, like bit rate of human computer interaction, it's
[822.28 --> 829.72]  like we live in a time where like we have 4K screens running at, you know, 60 or 120
[829.72 --> 830.10]  hertz.
[830.28 --> 835.98]  Like the sheer amount of like data that computers can feed into us through our eyeballs is huge.
[836.10 --> 840.00]  Whereas in kind of like the point and click, you know, mouse world, it's like how many bits
[840.00 --> 843.40]  per second can you really feed into the computer as a human?
[843.62 --> 843.94]  Right.
[843.94 --> 848.20]  And now textual input, you know, it doesn't get us all the way there to, you know, 4K times,
[848.34 --> 849.62]  you know, 60 hertz.
[849.62 --> 857.06]  But it does, it basically like 10Xs or more like the input bit rate of what we can do to
[857.06 --> 857.74]  instruct machines.
[857.86 --> 860.54]  I think it's a great win for kind of like human agency.
[860.84 --> 863.70]  Like we want to be programming the computer is not the other way around.
[863.70 --> 864.02]  Right.
[864.08 --> 868.16]  And I think a lot of the technology that has emerged over the past, you know, 10, 15 years
[868.16 --> 872.78]  has been kind of computers programming us as humans a little bit in terms of like all the
[872.78 --> 873.66]  stuff that we consume.
[874.06 --> 877.88]  And so, yeah, I'm super excited for textual based inputs.
[877.88 --> 881.12]  It's, I think chat is kind of like a subset of that.
[881.48 --> 885.60]  The way we think about Kodi evolving is really it's going to evolve in the direction of just
[885.60 --> 887.12]  like this rich REPL.
[887.28 --> 892.94]  So it's not, it's not necessarily going to be like, oh, it's a human-like thing that you
[892.94 --> 894.34]  talk with conversationally.
[894.48 --> 897.10]  It's more like if you want to do a search, you type something that looks like a search
[897.10 --> 897.34]  query.
[897.48 --> 898.78]  It knows that you want to do a search.
[899.28 --> 900.32]  Shows you search results.
[900.32 --> 903.88]  If you ask a high-level question, it knows you're asking a high-level question.
[903.88 --> 907.24]  It gives you an answer that integrates the context of your code base.
[907.40 --> 912.46]  If you want to ask a question about your production logs or maybe something about something someone
[912.46 --> 917.88]  said in chat or like an issue or a code review, you should pull context from those sources
[917.88 --> 923.88]  and integrate that and both synthesize an answer to your specific question, but also like refer
[923.88 --> 927.96]  you back to the primary sources so that you can go and like dig deeper and understand more
[927.96 --> 929.08]  fully how it got to its answer.
[929.08 --> 931.64]  So we think chat is just the starting point.
[931.78 --> 935.12]  It's really just like this rich REPL that's going to integrate like all sorts of context,
[935.30 --> 940.52]  like whatever, you know, piece of information is relevant to you creating software.
[941.02 --> 943.88]  This is kind of like the thing that focuses that and pulls it all in.
[944.12 --> 948.46]  It really seems like that, at least as an interface, you're seeing that as the future
[948.46 --> 949.82]  of what Sourcegraph is, isn't it?
[949.86 --> 952.52]  Or is there more to Sourcegraph than that in the future?
[952.88 --> 957.18]  So the way we think about it is like we spent the past 10 years building the world's most
[957.18 --> 958.42]  advanced code understanding tool.
[958.42 --> 959.72]  So we have the best code search.
[959.84 --> 961.42]  We have the best code graph.
[961.58 --> 965.68]  So the global reference graph across, you know, all the different languages in the world.
[966.14 --> 972.34]  We have a large scale code modification refactoring system and a system to track high level insights.
[972.46 --> 976.06]  So there's all these like backend capabilities that are really, really powerful.
[976.74 --> 982.56]  And what language models have done is given us a really, really nice beginner friendly interface
[982.56 --> 983.86]  to all that power.
[984.10 --> 986.92]  And I think you're going to see this across all kinds of software.
[986.92 --> 991.22]  It's like historically building power user tools has been difficult because the on-ramp
[991.22 --> 997.16]  to getting full, full, taking full advantage of those tools has been a little steep.
[997.52 --> 998.04]  Requires education.
[998.22 --> 998.30]  Yeah.
[998.36 --> 998.52]  Yeah.
[998.62 --> 1002.72]  And so like if you're worried about the on-ramp, maybe you end up constraining your product a
[1002.72 --> 1006.78]  little bit just to make it simpler, dumb it down for the beginning user.
[1006.78 --> 1007.90]  But you lose out on the power.
[1007.90 --> 1012.64]  I think that tradeoff is no longer going to be as severe now with language models.
[1012.84 --> 1019.96]  And so at Sourcegraph, we're basically thinking, rethinking the user interaction of the entire
[1019.96 --> 1020.54]  experience.
[1020.74 --> 1024.64]  Like the underlying capabilities and underlying tech is not changing.
[1024.80 --> 1028.02]  That's still, if anything, that's gotten more valuable now because you can feed it into
[1028.02 --> 1029.84]  the language model and instantly get value out of it.
[1029.84 --> 1033.84]  But the entire user interaction layer, I think, needs to be rethought.
[1034.28 --> 1040.74]  And Cody, as your AI editor assistant, is kind of like the first iteration of that thought
[1040.74 --> 1041.14]  process.
[1041.44 --> 1043.86]  How did you iterate to the interface you're at now?
[1043.90 --> 1045.82]  And is it a constant evolution?
[1046.50 --> 1046.80]  Yeah.
[1046.90 --> 1049.74]  I mean, it's pretty much like, hmm, I think that would be a good idea.
[1049.80 --> 1051.64]  Let me go hack it together and see how it plays.
[1051.66 --> 1052.68]  And you play around with it.
[1052.74 --> 1054.32]  And then you kind of experience it yourself.
[1054.42 --> 1055.98]  And you build conviction in your own mind.
[1055.98 --> 1060.38]  And then you maybe share it with one or two other teammates and see if they have the same
[1060.38 --> 1060.92]  wow moment.
[1061.14 --> 1064.38]  And if they do, that's usually a pretty good sign that you're onto something.
[1064.84 --> 1068.98]  And there might be more details to hammer out to make it more accessible to everyone.
[1069.24 --> 1074.38]  But if you can convince yourself and at least two or three other smart people out there that
[1074.38 --> 1078.88]  there's something worth investigating, I think that's typically a pretty good sign that you're
[1078.88 --> 1079.34]  onto something.
[1079.50 --> 1080.80]  How do you get access to Cody?
[1080.84 --> 1084.16]  Not so much get access, but how do you use it in the Sourcecraft world?
[1084.16 --> 1085.60]  Like, how does it appear?
[1085.98 --> 1086.86]  How do you conjure it?
[1087.32 --> 1087.50]  Yeah.
[1087.56 --> 1088.80]  So it's just an editor extension.
[1089.16 --> 1091.08]  You can download it from the VS Code marketplace.
[1091.54 --> 1092.84]  It's available now.
[1093.02 --> 1094.12]  And it's free to use.
[1095.52 --> 1098.26]  And we have other editors on the way.
[1098.42 --> 1100.04]  IntelliJ is a very high priority for us.
[1100.08 --> 1100.84]  Also NeoVim.
[1101.04 --> 1102.68]  And of course, my editor of choice, Emacs.
[1103.34 --> 1103.70]  Of course.
[1106.60 --> 1110.08]  And we're developing it completely in the open as well.
[1110.08 --> 1113.26]  So Cody itself is completely open source and Apache licensed.
[1114.16 --> 1119.08]  And to get access to it, to start using it, you just install the extension into your editor
[1119.08 --> 1120.80]  and start using it.
[1120.86 --> 1122.04]  It opens up in a sidebar.
[1122.18 --> 1122.92]  You can chat with it.
[1122.98 --> 1124.58]  We also do inline completions.
[1124.90 --> 1127.26]  So as you're typing, we can complete code.
[1127.70 --> 1132.44]  Again, taking advantage of the kind of like baked in knowledge of the language model plus
[1132.44 --> 1135.00]  the context of your specific code base.
[1135.00 --> 1138.32]  So generating like very high quality completions.
[1139.38 --> 1145.38]  And yeah, it's generally just as simple as installing the extension and then you're off
[1145.38 --> 1145.82]  to the races.
[1146.18 --> 1147.44]  Probably a Sourcegraph account first.
[1148.04 --> 1148.28]  Right?
[1148.54 --> 1148.78]  Yeah.
[1148.84 --> 1153.44]  So you do have to off through Sourcegraph because that's how we, I mean, we wouldn't be able
[1153.44 --> 1157.14]  to provide it for free if you didn't off through Sourcegraph because on the back end, we're
[1157.14 --> 1158.86]  calling out to different language model providers.
[1159.30 --> 1161.92]  And we're also running a couple of our own.
[1162.66 --> 1162.98]  Okay.
[1163.30 --> 1164.60]  So accessible then.
[1164.68 --> 1169.32]  Not having to install Sourcegraph, have it scan my repository.
[1169.32 --> 1173.92]  Like the traditional way you provide intelligence, which is to leverage literally Sourcegraph
[1173.92 --> 1174.78]  on my repo.
[1174.98 --> 1181.40]  I can just simply off through Sourcegraph, have an extension in my VS Coder in the future
[1181.40 --> 1181.96]  Emacs.
[1182.10 --> 1182.54]  Exactly.
[1182.90 --> 1183.58]  Them potentially.
[1183.88 --> 1185.14]  They're kind of loosely coupled.
[1185.36 --> 1189.08]  Like we don't, we don't, we don't believe in strong coupling just for the sake of, you
[1189.08 --> 1190.72]  know, selling you more software.
[1190.78 --> 1194.90]  And I think with Cody, the design philosophy was like, look, if you connected to Sourcegraph,
[1195.50 --> 1196.54]  it does get a lot better.
[1196.62 --> 1199.94]  It's like if you gave a really smart person access to Google, they're going to be a lot smarter
[1199.94 --> 1201.78]  about answering your questions.
[1202.14 --> 1202.20]  Yeah.
[1202.20 --> 1205.14]  But if you don't give them Google, they're still a smart person.
[1205.38 --> 1210.64]  And so Cody will still fetch context from kind of like your local code using non-Sourcegraph
[1210.64 --> 1213.10]  mechanisms if you're just running it standalone.
[1213.52 --> 1213.62]  Yeah.
[1213.82 --> 1216.38]  How does it get this intelligence as an extension?
[1216.52 --> 1218.30]  Like how does that, explain how that works.
[1218.34 --> 1220.28]  Like I've got it on my local repo.
[1220.40 --> 1220.90]  It's an extension.
[1221.06 --> 1222.58]  How does it get the intelligence from my code base?
[1223.06 --> 1223.30]  Yeah.
[1223.42 --> 1229.94]  So it's basically, I mean, think of the way that you would like understand or build a mental
[1229.94 --> 1232.22]  model of what's going on in a code base as a human.
[1232.94 --> 1235.44]  You might, you know, search for some pieces of functionality.
[1235.84 --> 1238.98]  You might read through the readme, click on a couple search results.
[1239.00 --> 1239.64]  It does all that.
[1239.72 --> 1240.84]  It's reading my readme right away?
[1241.28 --> 1242.22]  Yeah, basically.
[1242.22 --> 1249.10]  So when you ask a question, Cody will ping Sourcegraph for, hey, what are the most relevant pieces
[1249.10 --> 1252.02]  of documentation or source code in your code base?
[1252.14 --> 1255.68]  And then essentially, you know, quote unquote, read them as a language model and use that
[1255.68 --> 1256.98]  as context for answering a question.
[1257.38 --> 1260.26]  So if you ask like a general purpose question, it'll typically read the readme.
[1260.26 --> 1263.16]  If you ask a more targeted question, like, oh, how do you do this?
[1263.24 --> 1266.02]  This, you know, one specific thing, like, you know, read a PDF or whatever.
[1266.48 --> 1272.64]  It'll go find the places in source code where you're, you know, it processes PDFs and read
[1272.64 --> 1276.64]  that in and then interpret that through the lens of answering your question.
[1277.08 --> 1277.66]  In real time.
[1277.76 --> 1277.90]  Yeah.
[1278.12 --> 1278.24]  Yeah.
[1278.38 --> 1281.98]  Is there a latency to the question to the gathering?
[1282.28 --> 1283.48]  And like, what's the speed?
[1283.48 --> 1289.74]  If I said that example, how does my application, you know, compile a PDF from a Markdown file,
[1289.78 --> 1290.14]  for example?
[1290.38 --> 1290.54]  Yeah.
[1290.62 --> 1293.28]  So it typically gets back to you within like one or two seconds.
[1293.56 --> 1296.12]  And most of the latency is actually just the language model latency.
[1296.26 --> 1298.98]  So it depends on what language model you're choosing to use underneath the hood.
[1299.30 --> 1303.34]  All the source graph stuff is super fast because that's just, I mean, there's no like, yeah,
[1303.50 --> 1304.82]  it's source graph is fast.
[1304.90 --> 1306.88]  We've spent the past 10 years making it very fast.
[1306.88 --> 1312.80]  And there's no like, you know, billions of linear algebra operations happening with source
[1312.80 --> 1313.02]  graph.
[1313.10 --> 1319.24]  Source graph is just, you know, classical, you know, CPU based, you know, code and text.
[1319.48 --> 1319.90]  What about privacy?
[1319.90 --> 1320.18]  Yeah.
[1321.14 --> 1321.32]  Yeah.
[1321.40 --> 1325.92]  So privacy is extremely important to us, both in terms of, you know, individual developers
[1325.92 --> 1327.38]  and our enterprise customers.
[1327.38 --> 1331.68]  Like the last thing they want to do is have their private code be used as training data
[1331.68 --> 1335.38]  into, you know, some general purpose model that's going to leak their sensitive IP to
[1335.38 --> 1336.08]  the rest of the world.
[1336.08 --> 1343.08]  So we basically negotiated zero retention policies with all our proprietary language model providers,
[1343.28 --> 1347.68]  which means that your data is never going to get used as training data for a model.
[1347.88 --> 1354.26]  And not only that, the language model providers will forget your data as soon as the request
[1354.26 --> 1354.82]  is complete.
[1354.82 --> 1360.42]  So like there, there is no persistence in terms of like, you know, remembering the code that
[1360.42 --> 1364.80]  you sent over to complete a request that just gets forgotten as soon as the language model
[1364.80 --> 1366.60]  generates a request for Cody.
[1366.60 --> 1372.66]  And then for the rest of it, I mean, Sourcegraph has always taken user privacy and code privacy
[1372.66 --> 1373.32]  very seriously.
[1373.66 --> 1377.56]  It's why we've been able to serve the sorts of enterprise customers that we do.
[1377.76 --> 1377.98]  For sure.
[1377.98 --> 1381.54]  I know why that's important, but why, spell it out, why is that important?
[1381.82 --> 1385.56]  What your, this zero attention policy, what's the real breakdown of that privacy?
[1385.66 --> 1387.70]  Why is it important to the main users?
[1388.58 --> 1393.48]  So from, from a company's point of view, it's important because you don't want to leak portions
[1393.48 --> 1397.18]  of your code base or have them persist in the logs of some third party data provider.
[1397.78 --> 1402.16]  As an individual developer, I think it's, it's just important to give you control over,
[1402.34 --> 1403.24]  over your own data.
[1403.24 --> 1407.96]  Um, and I think that's going to be an especially important thing, uh, in, in this new world
[1407.96 --> 1413.98]  that we're living in where, um, you know, before private data was, was valuable.
[1413.98 --> 1415.52]  Um, you know, it carries value.
[1415.52 --> 1420.92]  It tells you things about a certain person or the way they work and that can be used for,
[1420.92 --> 1422.80]  you know, purposes, both good and bad.
[1423.02 --> 1423.74]  Search history.
[1424.36 --> 1425.50]  It's like search history, right?
[1425.50 --> 1425.90]  Exactly.
[1426.16 --> 1428.66]  You can tell a lot about a person by their search history, their watch history, their
[1428.66 --> 1429.28]  like history.
[1429.36 --> 1429.64]  Totally.
[1429.68 --> 1431.28]  But now it's used for a whole nother reason, right?
[1431.28 --> 1431.50]  Yeah.
[1431.50 --> 1436.64]  And, and I think it's important to grant our users and customers, uh, control, uh, and
[1436.64 --> 1438.90]  ownership over that data because it is your data.
[1438.90 --> 1443.96]  And I think with language models, like language models, just, uh, they like 10 X the value
[1443.96 --> 1445.62]  and the sensitivity of that data.
[1446.22 --> 1452.30]  Uh, because now instead of, you know, just like feeding into like a gen one, uh, AI model
[1452.30 --> 1456.06]  or exposing it to some other human, you can feed it into one of these large language models
[1456.06 --> 1460.60]  that can, you know, kind of like memorize everything about you as a person or a programmer.
[1460.60 --> 1464.36]  Um, and you know, in some ways maybe that's good.
[1464.36 --> 1467.78]  Like if you're open to that, if, if you're willing to share your data, we could potentially
[1467.78 --> 1471.86]  train language models that, you know, emulate some of the best and brightest programmers
[1471.86 --> 1472.40]  in existence.
[1472.40 --> 1475.90]  But we ultimately, we think that should be, you know, your personal decision.
[1476.02 --> 1476.14]  Yeah.
[1476.14 --> 1476.34]  Right.
[1476.54 --> 1476.86]  Exactly.
[1476.86 --> 1482.70]  How explicit is that in this, in the signup or the acceptance of the Cody license or the,
[1482.70 --> 1487.86]  you know, this GA to now, you know, widespread usage, how do you, how explicit are you with
[1487.86 --> 1489.78]  a new signup that says, I want to use Cody?
[1490.38 --> 1493.62]  Do you say privacy and all these things you just said basically, how clear is that?
[1494.38 --> 1498.28]  Uh, so when you first install it, there's kind of like a terms of use that pops up and
[1498.28 --> 1502.20]  you cannot use Cody unless you accept it, you read through and accept it.
[1502.20 --> 1504.44]  How many words is in that, that, uh, TOS?
[1504.60 --> 1508.56]  Uh, it fits, uh, on like basically one page without scrolling.
[1508.62 --> 1508.86]  Okay.
[1508.92 --> 1511.32]  So a thousand words, maybe, uh, 500.
[1511.92 --> 1512.28]  Yeah.
[1512.42 --> 1512.78]  250.
[1513.90 --> 1514.84]  Maybe not 250.
[1514.96 --> 1516.46]  I think it's probably 250 to 500.
[1516.90 --> 1521.14]  Uh, I had to go back and check specifically, but like digestible in a, in a minute.
[1521.56 --> 1521.92]  Yeah.
[1522.00 --> 1524.96]  We're, we're not trying to be one of those companies that tries to hide stuff.
[1524.96 --> 1528.74]  What I mean by that is less trying to say, are you hiding it, but more how clear are you
[1528.74 --> 1528.98]  being?
[1528.98 --> 1531.18]  Cause it seems like you care to be clear.
[1531.36 --> 1531.54]  Yeah.
[1531.54 --> 1536.30]  So is that like a paramount thing for you all to be so clear that you say, Hey, privacy
[1536.30 --> 1536.86]  matters.
[1537.02 --> 1537.24]  Yes.
[1537.28 --> 1539.04]  We don't collect zero retention.
[1539.04 --> 1540.12]  It's spelled out really clear.
[1540.20 --> 1543.22]  It's a bullet list saying, basically saying exactly what you said.
[1543.46 --> 1544.18]  Privacy matters.
[1544.30 --> 1545.12]  We don't collect data.
[1545.26 --> 1545.84]  And I wrote it for you.
[1545.90 --> 1546.28]  Using.
[1546.74 --> 1546.94]  Yeah.
[1547.14 --> 1547.54]  Basically.
[1547.82 --> 1549.90]  Well, Tammy, our, our wonderful legal counsel.
[1550.16 --> 1551.32]  I didn't write it.
[1551.40 --> 1551.84]  I'm just kidding.
[1552.04 --> 1552.82]  We all know chat.
[1552.84 --> 1553.52]  GBT wrote it.
[1553.52 --> 1553.82]  Okay.
[1553.82 --> 1556.24]  Let's be serious here.
[1556.98 --> 1559.44]  Actually, you know, that, that's a great use case for, for chat.
[1559.44 --> 1563.80]  GBT, if, if you're asked to accept one of these like lengthy, uh, and use it in there,
[1563.88 --> 1565.58]  summarize it, paste it in there, summarize it.
[1565.64 --> 1566.80]  Telling it if there's anything fishy.
[1567.32 --> 1568.46]  Uh, yes.
[1568.66 --> 1569.68]  That'd be cool for sure.
[1569.86 --> 1570.02]  Yeah.
[1570.10 --> 1570.70]  That's the best.
[1570.80 --> 1572.54]  I cannot wait, honestly, for that to come out.
[1572.70 --> 1574.80]  What are the loopholes in this contract?
[1575.32 --> 1575.50]  Woo.
[1575.50 --> 1577.78]  I have nefarious action on the other side.
[1577.94 --> 1579.34]  What are my loopholes to get out?
[1579.56 --> 1579.70]  Right.
[1579.78 --> 1580.22]  You know what I mean?
[1580.44 --> 1580.66]  Yep.
[1580.82 --> 1580.94]  Yep.
[1580.94 --> 1581.50]  For bad or good.
[1581.58 --> 1583.86]  I guess you could use that in the bad side or the good side, but like.
[1584.04 --> 1586.12]  GBT for X, where X is literally everything.
[1586.34 --> 1586.58]  Right.
[1586.86 --> 1586.98]  Yeah.
[1587.00 --> 1587.74]  It's going to be there.
[1587.88 --> 1591.80]  Like there's going to be one specifically trained for lawyer, lawyering.
[1592.12 --> 1592.34]  Yeah.
[1592.42 --> 1592.62]  Yeah.
[1592.74 --> 1597.74]  I think, um, you know, language models will be a huge democratizing force in many domains.
[1597.84 --> 1603.16]  You know, it's democratizing understanding of, of legal concepts, democratizing access to
[1603.16 --> 1603.92]  software creation.
[1604.44 --> 1609.52]  I think it's going to be, it's, there's going to be a huge expansion of the, uh, percentage
[1609.52 --> 1612.46]  of people that's going to be able to access those knowledge domains.
[1612.72 --> 1613.14]  Right.
[1613.90 --> 1617.32]  So let's say I'm a happy GitHub copilot user.
[1617.54 --> 1617.82]  Mm-hmm.
[1617.96 --> 1618.32]  Oh yeah.
[1618.78 --> 1621.38]  Would I install Cody alongside this and be happier?
[1621.56 --> 1622.42]  Would I be less happy?
[1622.54 --> 1625.50]  Are these competitive, like, is this a zero sum game?
[1625.64 --> 1627.54]  Do I need to go all in on Cody?
[1627.64 --> 1628.58]  What are your thoughts on that?
[1628.66 --> 1630.90]  I think it's the exact opposite of a zero sum game.
[1630.90 --> 1631.10]  Okay.
[1631.10 --> 1635.48]  I think there's like so much left to build that, uh, you know, the, the market is, is
[1635.48 --> 1637.08]  huge and, and vastly growing.
[1637.88 --> 1642.00]  Um, we do have, uh, features that copilot doesn't have.
[1642.00 --> 1647.28]  So, you know, currently they don't have, uh, kind of like a chat based, uh, you know, textual
[1647.28 --> 1650.28]  input to ask high level questions about the, the code.
[1650.98 --> 1654.16]  Um, I think that's coming in copilot X to some extent, but
[1654.16 --> 1655.40]  Yeah, I think they announced that, but it's not out yet.
[1655.46 --> 1655.76]  I don't think.
[1655.76 --> 1656.38]  It's not out yet.
[1656.38 --> 1659.26]  And if you, if you look at the video, the, the kind of context fetching they're doing,
[1659.26 --> 1661.18]  it's basically like, you know, you're currently open file.
[1661.26 --> 1662.00]  Explain that.
[1662.00 --> 1664.30]  And, and Cody is already doing much, much more than that.
[1664.30 --> 1668.14]  It's, it's reading, uh, even if you ask it a question about the current file, it'll actually
[1668.14 --> 1671.98]  go and read other files in your code base that it thinks are related and use that to inform
[1671.98 --> 1672.46]  your answer.
[1672.46 --> 1676.48]  So, so we think, you know, the power of source graph gives us a bit of a competitive edge
[1676.48 --> 1682.24]  there with the kind of high level questions and onboarding and kind of like rubber ducking
[1682.24 --> 1683.14]  a use case.
[1683.32 --> 1686.92]  And then for completions, you know, I think copilot is, is great.
[1687.10 --> 1690.08]  Um, but for, for completions, we're essentially doing the same thing.
[1690.08 --> 1694.92]  So like the completions that Cody generates, it takes, uh, into account that same context
[1694.92 --> 1696.42]  when it's, it's completing code.
[1696.42 --> 1703.60]  So that means it's, it's better able to kind of mimic or, or emulate the patterns and best
[1703.60 --> 1706.42]  practices in your specific code base.
[1706.42 --> 1711.88]  And again, because we're kind of open source and model agnostic, we are just integrating
[1711.88 --> 1715.10]  all the best language models as, as they come online.
[1715.10 --> 1718.94]  So I think, you know, Anthropic, I don't know when this episode's going out, but Anthropic
[1718.94 --> 1720.36]  today just, okay, pretty quick.
[1720.36 --> 1721.36]  The 24th.
[1721.36 --> 1722.36]  Yeah.
[1722.36 --> 1725.16]  So Anthropic just announced today that they have a new version of Claude that has a,
[1725.16 --> 1728.24]  a, an incredible, like a hundred thousand token context window.
[1728.24 --> 1733.60]  It's just like, uh, uh, I think like orders of magnitude more than, than, uh,
[1733.60 --> 1735.28]  what was previously available.
[1735.28 --> 1739.82]  And, uh, that should be, I mean, by the time this episode goes online, that should, it should
[1739.82 --> 1740.88]  be available on Cody.
[1740.88 --> 1741.88]  Yeah.
[1741.88 --> 1745.82]  Whereas, you know, Copilot, I think they're like, uh, maybe someone from GitHub can correct
[1745.82 --> 1748.94]  me if I'm wrong, but I think they're still using the codex model, which was released in
[1748.94 --> 1750.10]  like 2021 or something.
[1750.10 --> 1756.54]  Um, and so it's a, it's a much smaller model, um, that only has around like 2000 tokens of,
[1756.54 --> 1760.38]  of context window and much more basic context fetching.
[1760.38 --> 1763.46]  It's already incredibly useful, but I think we're, we're kind of taking it, taking it to
[1763.46 --> 1764.46]  the next level a little bit.
[1764.46 --> 1765.46]  Right.
[1765.46 --> 1767.46]  So open source and model agnostic.
[1767.46 --> 1769.62]  Open source, model agnostic.
[1769.62 --> 1773.14]  We're not locking you in to like a vertical proprietary platform.
[1773.14 --> 1774.14]  Proxy friendly.
[1774.14 --> 1775.14]  Proxy friendly.
[1775.14 --> 1778.38]  Uh, also enterprise friendly, you know, source graph.
[1778.38 --> 1783.92]  We, we, we, we've made ourselves easy to use in both cloud and on premises environments.
[1783.92 --> 1788.18]  So we're just trying to do the best thing for our customers and for developers at large.
[1788.18 --> 1793.66]  So because you're model agnostic, does that mean that you're not, you're not doing any
[1793.66 --> 1796.68]  of the training of the base layer models?
[1796.68 --> 1798.42]  So do you also sidestep legal concerns?
[1798.42 --> 1803.78]  Cause I know like with, with codex and copilot, there's been, there's at least one high profile
[1803.78 --> 1804.94]  lawsuit that's pending.
[1804.94 --> 1808.08]  Like there's, there's legal things happening.
[1808.36 --> 1809.54]  There's going to be things litigated.
[1809.82 --> 1813.32]  I'm wondering if you're in the target for that now with Cody or if you're just not because
[1813.32 --> 1814.58]  there's other people's models.
[1814.58 --> 1819.44]  No, we're, we're very mindful of that and, um, we actually integrate models in a couple
[1819.44 --> 1820.00]  of different ways.
[1820.00 --> 1822.56]  So we do it for kind of like the chat based autocomplete.
[1822.56 --> 1826.46]  There's a separate model we use for code completions and, and there's another model that we use
[1826.46 --> 1829.94]  for like embeddings based, uh, code search and information retrieval.
[1829.94 --> 1832.40]  Um, and it's kind of like a mix and match.
[1832.40 --> 1835.64]  Like sometimes we'll use like a proprietary off the shelf model.
[1835.64 --> 1837.90]  Other times we'll, we'll use the model that we fine tuned.
[1837.90 --> 1842.82]  Um, but for the ones that, uh, the models that we do rely on external service providers
[1842.82 --> 1849.62]  for, um, we're very mindful of the kind of like evolving legal and IP landscape.
[1849.62 --> 1852.94]  And so one of the things that we're, we're currently building is, is basically like copyright
[1852.94 --> 1855.76]  code, uh, or, or copied code detection.
[1855.76 --> 1859.78]  And if you think about it, like source graph as a code search engine is, is kind of like
[1859.78 --> 1862.50]  in, in a great position to, to build this feature.
[1862.50 --> 1867.30]  It's like, if you emit a line of code or you write a line of code, uh, that is, you
[1867.30 --> 1874.04]  know, verbatim copied from, uh, uh, somewhere else, uh, in open source or, or even in your
[1874.04 --> 1877.14]  own proprietary code base, you know, you might be worried about just like code duplication.
[1877.14 --> 1880.74]  We can, we can flag that for you because we've built, we've been building code search for
[1880.74 --> 1881.74]  the past 10 years.
[1881.74 --> 1882.74]  Yeah.
[1882.74 --> 1883.74]  Cool stuff, man.
[1883.74 --> 1887.74]  So moving fast, what comes next?
[1887.74 --> 1892.00]  When are you going to drop Cody two?
[1892.00 --> 1893.76]  It's probably like a week from now, right?
[1893.76 --> 1894.76]  Yeah.
[1894.76 --> 1895.76]  That's a great question.
[1895.76 --> 1899.72]  I mean, we are just kind of like firing all on all cylinders here.
[1899.72 --> 1903.74]  We have a lot of interesting directions to explore, like one, one direction or one dimension
[1903.74 --> 1906.68]  that we're expanding in is just integrating more pieces of context.
[1906.68 --> 1911.68]  So one of the reasons why we wanted to open source Cody, um, is because we just want to
[1911.68 --> 1916.24]  be able to integrate like context from wherever it is and not be limited by, you know, a single,
[1916.24 --> 1917.86]  you know, code host or a single platform.
[1917.86 --> 1922.66]  Like there's so much institutional knowledge, uh, that's in many different systems might
[1922.66 --> 1923.66]  be in Slack.
[1923.66 --> 1925.58]  It might be in, uh, you know, GitHub issues.
[1925.58 --> 1927.58]  It might be in your code review tool.
[1927.58 --> 1929.34]  Uh, it might be in your production logs.
[1929.34 --> 1934.42]  And so we want to build integrations into Cody that just pull in all this context.
[1934.42 --> 1937.58]  And I think the best way to do that is just to make this, this kind of like platform,
[1937.58 --> 1942.54]  uh, this orchestrator of sorts like open source and accessible to everyone.
[1942.54 --> 1947.46]  Um, the other dimension that, that is very exciting to us is, is going deeper into the
[1947.46 --> 1948.00]  model layer.
[1948.00 --> 1951.88]  So we've already started to do this for the embeddings based, uh, like code retrieval.
[1951.88 --> 1956.50]  Um, but I think we're, we're exploring some, uh, models that are related to code generation
[1956.50 --> 1959.38]  and potentially even like the chat based completions at some point.
[1959.38 --> 1964.46]  Um, and that's going to be interesting cause it's, it's going to allow us to incorporate pieces
[1964.46 --> 1966.42]  of source graph into the actual like training process.
[1966.42 --> 1970.30]  And there's been some research there that shows that, uh, incorporating like search
[1970.30 --> 1975.34]  engines into training, uh, language models actually, uh, you know, yields very nice, uh,
[1975.34 --> 1978.22]  properties in terms of like lower latency, but, uh, higher quality.
[1978.72 --> 1981.84]  Um, and it's also important to a lot of our customers because a lot of them are, you know,
[1981.84 --> 1987.96]  large corporations, they deploy on premises and, uh, even the zero retention policy where,
[1987.96 --> 1992.16]  you know, the, the code is forgotten as soon as it's, uh, you know, sent back over, uh,
[1992.16 --> 1994.02]  is not good enough for, for some of our customers.
[1994.02 --> 1998.14]  So they want to completely be able to self host this and, uh, you know, we plan to serve
[1998.14 --> 1998.64]  them as well.
[1999.16 --> 2004.92]  How high up the stack, like the conceptual stack, do you think Cody can get or maybe
[2004.92 --> 2010.42]  any AI tooling with code gen with regards to like how I instructed as a developer?
[2010.66 --> 2011.06]  Yeah.
[2011.18 --> 2013.92]  You know, cause right now we're very much like, okay, it's autocomplete.
[2014.18 --> 2015.60]  There's a function here, right?
[2015.64 --> 2020.28]  I can tell it, write me a thing that connects to an API and parses the JSON or whatever.
[2020.28 --> 2023.94]  And I can do, you can spit that out, but like how high up the stack can I get?
[2024.00 --> 2030.08]  Can I say, you know, write me a Facebook, Facebook for dogs, you know, and be done for
[2030.08 --> 2033.12]  instance, or like user stories, kind of write some user stories and go from there.
[2033.30 --> 2033.64]  What do you think?
[2033.74 --> 2034.28]  That's a great question.
[2034.38 --> 2038.54]  I mean, we've all seen, uh, the Twitter demos by now where, you know, someone is like,
[2038.56 --> 2042.40]  you know, GPT four, like build me an app and you know, it creates a working app and
[2042.40 --> 2043.34]  whole website.
[2043.34 --> 2047.94]  I think if you actually gone through and tried that in practice yourself, you soon realize
[2047.94 --> 2053.28]  like, Hey, you can get to like a working app pretty quickly just through like instructing
[2053.28 --> 2055.38]  it using English or natural language.
[2055.38 --> 2058.96]  But then you get a little bit further down that path and you're like, Oh, I wanted to
[2058.96 --> 2059.40]  do this.
[2059.48 --> 2060.28]  I wanted to do that.
[2060.36 --> 2061.30]  Can you add this bell and whistle?
[2061.48 --> 2065.82]  There's kind of this like commentatorial complexity that emerges as you add like different features
[2065.82 --> 2068.42]  and you're kind of diverging from like the common path.
[2068.42 --> 2070.62]  And then, and then it falls apart.
[2070.70 --> 2071.74]  Like I actually tried this myself.
[2071.74 --> 2076.68]  Like I tried to write a complete app, uh, is actually a prototype for, for the next
[2076.68 --> 2077.24]  version of Cody.
[2077.42 --> 2077.68]  Okay.
[2077.84 --> 2082.52]  Um, I tried to do it by not writing a single line of code just by writing English.
[2082.52 --> 2086.30]  And I got like 80% of the way there in like 30 minutes.
[2086.30 --> 2087.50]  And I was like, this is amazing.
[2087.70 --> 2088.70]  Like this is the future.
[2088.70 --> 2090.10]  Like I'm never going to code again.
[2090.20 --> 2095.42]  And then the remaining 20% literally took like four hours and I was banging my head against
[2095.42 --> 2099.14]  the wall because I asked it to do one thing and then it did, did it.
[2099.20 --> 2102.78]  But then it kind of like screwed up this other thing and it became kind of like this like
[2102.78 --> 2103.52]  whack-a-mole problem.
[2103.58 --> 2105.10]  So we're not all the way there yet.
[2105.20 --> 2109.32]  But I think, I think the way we think about it is like Cody right now is at the point where
[2109.32 --> 2112.50]  if you ask it, uh, this is another thing I tried the other day.
[2112.50 --> 2114.16]  Like I wanted to add a new feature to Cody.
[2114.58 --> 2118.60]  Uh, Cody has these things called recipes, which are kind of like templated interactions with,
[2118.60 --> 2119.62]  uh, Cody.
[2119.74 --> 2123.94]  So like write a unit test or generate a doc string or, you know, smell my code, you know, give
[2123.94 --> 2124.56]  me some feedback.
[2124.56 --> 2128.84]  Like I wanted to add a new recipe and I basically asked Cody, Hey, I want to add a new recipe
[2128.84 --> 2129.40]  to Cody.
[2129.94 --> 2131.72]  Uh, what parts of the coach I modify?
[2131.86 --> 2134.66]  And it basically showed me all the parts of the code that were relevant.
[2134.76 --> 2139.46]  And then it generated the code for the new recipe using the existing recipes as like a
[2139.46 --> 2140.04]  reference point.
[2140.52 --> 2143.92]  Uh, and I basically got it done like five minutes and it was amazing.
[2143.92 --> 2145.82]  So like, I was still obviously in the hot seat there.
[2145.82 --> 2150.60]  I was still calling the shots, but it turned something that probably would have been, uh, at
[2150.60 --> 2154.12]  least 30 minutes, maybe an hour, you know, if I got frustrated or, or, or distracted
[2154.12 --> 2155.74]  into something that was like five minutes.
[2156.02 --> 2159.92]  And that was actually, that was actually the interview question we were using for interviewing
[2159.92 --> 2161.00]  on the AI team.
[2161.08 --> 2163.26]  So after that we had to go back and like revamp that.
[2163.34 --> 2164.28]  It's like, this is too easy.
[2164.40 --> 2165.02]  Too easy now.
[2165.76 --> 2166.90]  Everything just got easier.
[2167.12 --> 2167.34]  Yeah.
[2167.34 --> 2172.46]  Do you think this is like a, a step change in what we can do?
[2172.46 --> 2176.68]  And then we're going to plateau right here for a while and like refine and, you know,
[2176.68 --> 2180.14]  do more stuff, but kind of like stay at this level of quote unquote intelligence.
[2180.40 --> 2183.56]  Or do you think it's like, just the sky's the limit from here on out?
[2183.56 --> 2186.72]  Like, which I mean, obviously just conjecture at this point.
[2186.96 --> 2187.42]  Challenging to predict.
[2187.56 --> 2189.40]  I mean, it's, it's very challenging to predict.
[2189.72 --> 2194.00]  Uh, you know, I might be eating my words, um, in, in another six months, but like, uh, you
[2194.00 --> 2199.16]  know, on the spectrum of, you know, oh, it's just like glorified autocomplete and it doesn't
[2199.16 --> 2202.70]  really know anything to all, all the way to like, you know, AGI doomer, you know, let's,
[2202.70 --> 2204.62]  let's nuke the GPU data centers.
[2204.80 --> 2205.08]  Right.
[2205.24 --> 2205.70]  Oh my gosh.
[2205.86 --> 2208.68]  Um, I just, where do you fall?
[2208.84 --> 2209.12]  Yeah.
[2209.28 --> 2210.56]  Don't give him ideas.
[2212.84 --> 2213.78]  Cancel, cancel, cancel.
[2213.78 --> 2217.42]  Honestly, I think a lot of the discourse, uh, on that end of the spectrum has just gotten
[2217.42 --> 2218.32]  kind of crazy.
[2218.64 --> 2221.90]  Um, like the way, the way I view it is this is a really powerful tool.
[2222.00 --> 2223.14]  It's an amazing new technology.
[2223.14 --> 2227.84]  And, you know, it can be used for, for evil certainly as, as any technology can, but,
[2227.84 --> 2232.56]  uh, I'm a techno optimist and I think this will largely be like positively impactful,
[2232.56 --> 2234.18]  uh, for the world.
[2234.30 --> 2237.84]  Um, and I don't really see it, you know, replacing, uh, programmers.
[2237.94 --> 2241.68]  It might change the way we think about programming or, you know, software creation.
[2242.04 --> 2245.84]  Uh, there's certainly going to be a lot more people that are going to be empowered to create
[2245.84 --> 2246.54]  software now.
[2247.20 --> 2251.62]  Um, and I think there, there'll be kind of a spectrum of people, um, from, you know, those
[2251.62 --> 2256.66]  who, who write software, uh, just by describing it in, in natural language, uh, all the way
[2256.66 --> 2262.00]  to the people who are kind of like building the, the core kernels, uh, of, of kind of
[2262.00 --> 2266.22]  like the operating systems of the future that form like the solid foundation that, you know,
[2266.22 --> 2270.06]  pack in the really important, you know, data structures and algorithms, algorithms and,
[2270.06 --> 2275.20]  and, and core architecture around which everyone else can, uh, you know, throw their, you know,
[2275.26 --> 2276.84]  ideas and, and, and stuff.
[2276.94 --> 2278.48]  So there'll be like a huge spectrum.
[2278.48 --> 2282.80]  I think, you know, we'll almost think of it in terms of like the way we think of like
[2282.80 --> 2286.22]  reading and writing now where like, you know, you have many different forms of reading and
[2286.22 --> 2286.46]  writing.
[2286.46 --> 2290.60]  Like there's people just like reading, writing stuff on Twitter, you know, that's, that's
[2290.60 --> 2291.16]  one form of writing.
[2291.18 --> 2295.94]  And then there's other people who write, you know, long books that span, you know, uh, many
[2295.94 --> 2297.40]  years of intense research.
[2297.40 --> 2300.34]  And I think the future of code looks something like that.
[2300.42 --> 2301.96]  It's the ultimate flattener.
[2302.68 --> 2304.46]  You guys, you see that book, the world is flat.
[2304.66 --> 2304.92]  Yeah.
[2305.08 --> 2305.28]  Yeah.
[2305.46 --> 2306.06]  It's like that.
[2306.12 --> 2310.38]  Like for a while there it was outsourcing and now it's sort of like just accessibility
[2310.38 --> 2311.22]  to everybody.
[2311.22 --> 2316.28]  Now, you know, people who don't know much about code can learn about code and level up pretty
[2316.28 --> 2316.64]  quickly.
[2317.26 --> 2324.86]  And so the access, the catered access to have, uh, a patient, whether person or not, like I have
[2324.86 --> 2329.60]  conversations with chat GPT and I swear, I'm like, I tell my wife, I'm like, I'm literally
[2329.60 --> 2336.74]  talking to a machine and I get it, but we 30, 40 rounds back and forth through whatever
[2336.74 --> 2337.38]  it might be.
[2337.38 --> 2341.60]  And it's very much like a conversation I have with Jared, if you would give me the time
[2341.60 --> 2343.76]  and patience and if you wouldn't get frustrated, you know what I mean?
[2344.26 --> 2347.08]  And so it's a very patient.
[2347.22 --> 2347.32]  Yeah.
[2347.56 --> 2353.32]  Well, not necessarily, but you know, the world now has access to a patient, uh, sidecar
[2353.32 --> 2357.92]  that's quite intelligent that will get even more intelligent, whether you call it artificial
[2357.92 --> 2358.96]  intelligence or not.
[2359.04 --> 2359.24]  Yeah.
[2359.40 --> 2364.40]  You know, it has intelligence behind it, some knowledge and it's accessible right now.
[2364.80 --> 2365.56]  I agree.
[2366.02 --> 2367.48]  Humans are still necessary.
[2367.48 --> 2369.06]  Thank the Lord.
[2369.62 --> 2375.40]  Um, but wow, it's super flat now and a lot more people have access to what could be and
[2375.40 --> 2376.64]  what might be because of this.
[2376.96 --> 2378.08]  And that's a fantastic thing.
[2378.14 --> 2381.70]  I think of, you know, there's that Steve Jobs quote where he said computers are amazing
[2381.70 --> 2384.48]  because they're, they're like a bicycle for the human mind.
[2384.48 --> 2384.78]  Yeah.
[2384.78 --> 2388.98]  They allow a much more, I think it was drawing comparisons to like, you know, how different
[2388.98 --> 2393.82]  animals get around and like a human walking is like very inefficient, but a human on a bicycle
[2393.82 --> 2397.78]  is like more efficient than like the, the, the fastest cheetah or whatever.
[2397.98 --> 2398.26]  Right.
[2398.34 --> 2403.76]  I think like what, what language models, um, are, are capable of doing is instead of like
[2403.76 --> 2407.20]  a bicycle, now we each have like a race car or, or a rocket ship.
[2407.34 --> 2408.74]  Now we're still in the driver's seat, right?
[2408.74 --> 2411.86]  Like we're still steering it and telling you where to go, but it's just, it's way more
[2411.86 --> 2415.12]  leverage, uh, for any given, uh, individual.
[2415.48 --> 2416.96]  So great thing.
[2416.98 --> 2422.28]  If you know, you love being creative, you love dreaming up, you know, new ideas, um, and,
[2422.46 --> 2423.80]  and ways to, to solve problems.
[2424.02 --> 2426.00]  One more question on the business side of things.
[2426.14 --> 2428.56]  How has growth been because of Cody?
[2429.42 --> 2430.54]  That's a great question.
[2430.78 --> 2438.72]  Um, Cody is, I, you almost would not believe it if, uh, I described it to you, but
[2438.72 --> 2444.44]  um, Cody is literally like the most magical thing to happen to the source graph, go to
[2444.44 --> 2450.08]  market, uh, or, or sales, uh, motion since basically when we started the company ever,
[2450.18 --> 2450.56]  basically.
[2450.78 --> 2451.92]  Uh, I've been paying attention for a while.
[2451.96 --> 2452.66]  That's why I asked that question.
[2452.66 --> 2456.68]  Cause like you've had trouble getting growth cause you got to install a server or go cloud
[2456.68 --> 2458.30]  and then you got to examine the code base.
[2458.36 --> 2461.64]  Then you got to learn how to search the code, which is all like friction points.
[2461.64 --> 2465.16]  So, so one of the, like transparently, one of the challenges that we had as a business
[2465.16 --> 2472.38]  is, you know, we, we had a couple of sub, uh, subsets of the programmer population that
[2472.38 --> 2476.02]  were, were very eager to adopt source graph is basically, if you use a tool like source
[2476.02 --> 2477.72]  graph before you want to use it again.
[2477.72 --> 2483.34]  So if you're an ex Googler, ex Facebooker, ex Dropboxer, or, you know, ex Microsoft or
[2483.34 --> 2486.56]  at, you know, in, in, in a couple of teams, you kind of got it immediately.
[2486.56 --> 2491.16]  Uh, and then everyone else is like, Oh, is it like grep or is it like control F?
[2491.16 --> 2494.68]  Uh, and we, we would lose a lot of people along the way.
[2494.80 --> 2499.88]  I think with Cody, it's, it's at the point where not only does any programmer get it right
[2499.88 --> 2500.12]  away.
[2500.12 --> 2501.24]  They're like, Oh, holy shit.
[2501.24 --> 2506.62]  Like, uh, you know, you just asked to explain this like very complex code and in English and
[2506.62 --> 2508.10]  gave me like really good explanation.
[2508.70 --> 2510.92]  Um, even like non-technical stakeholders.
[2510.92 --> 2515.88]  So like as we sell to larger and larger companies, a lot of times, you know, in the room is, is someone
[2515.88 --> 2523.96]  with like, uh, uh, I don't know, uh, CEO or like board of directors or, uh, you know, non-technical
[2523.96 --> 2527.82]  someone who's pretty distant from, from the code, uh, traditionally speaking.
[2528.36 --> 2530.72]  And, uh, they get it too.
[2530.72 --> 2535.76]  Cause yeah, you know, we were in a pitch meeting the, the other week where it was like a large
[2535.76 --> 2537.28]  kind of fortune 500 energy company.
[2537.62 --> 2539.34]  And there was not a program in the room.
[2539.34 --> 2543.66]  It was just kind of like, you know, high level business owners, um, who are all very
[2543.66 --> 2546.02]  skeptical until we got to Cody.
[2546.02 --> 2550.04]  We opened up, you know, one of their open source libraries and asked Cody to explain what
[2550.04 --> 2550.70]  was going.
[2550.88 --> 2555.60]  And one person leaned in and they were like, you know, I'm, I haven't coded in like 30
[2555.60 --> 2558.00]  years and even I would get value out of this.
[2558.20 --> 2560.52]  So yeah, it's, it's just absolutely incredible.
[2560.86 --> 2562.98]  Your total adjustable market got a lot bigger.
[2563.22 --> 2563.46]  Yeah.
[2563.88 --> 2564.06]  Yeah.
[2564.06 --> 2564.28]  Right.
[2564.28 --> 2564.68]  Yeah.
[2564.70 --> 2566.36]  Cause like what is an engineer now?
[2566.62 --> 2572.44]  Um, I think it's like in, in a couple of years, uh, almost every human in the world
[2572.44 --> 2575.70]  will be empowered to create software and in some, some fashion.
[2575.92 --> 2581.62]  You said before that Cody leverages all that source graph is today, the intelligence.
[2581.78 --> 2581.96]  Yep.
[2582.14 --> 2583.18]  Will that always be true?
[2583.18 --> 2586.64]  I guess is maybe the more basic way to answer that or ask that question.
[2586.64 --> 2592.38]  Because at some point, if this is the, you know, the, the largest arc in your hockey stick
[2592.38 --> 2598.12]  growth and all the up from here is, you know, not so much Cody related, but Cody driven really.
[2598.40 --> 2598.50]  Yeah.
[2599.12 --> 2603.78]  Does what source graph do at large now eventually become less and less important?
[2603.90 --> 2609.72]  And the primary interface really is this natural language Cody interface that explains
[2609.72 --> 2610.20]  my code.
[2610.64 --> 2611.34]  That's a great question.
[2611.42 --> 2615.78]  It's like, you know, does, does AI just like swallow all of programming at some point?
[2615.78 --> 2621.30]  Like at some point do we cease to write, uh, kind of like old traditional, like systems
[2621.30 --> 2624.60]  oriented, uh, software in the von Neumann tradition.
[2624.60 --> 2625.46]  You hand wrote that code?
[2626.36 --> 2626.76]  What?
[2627.88 --> 2632.64]  You wrote a for loop instead of just like asking it nicely to repeat something?
[2632.88 --> 2633.02]  Nicely.
[2633.10 --> 2633.88]  Forget code search.
[2633.98 --> 2634.92]  I don't even read code.
[2635.22 --> 2636.72]  Like, why are you reading code?
[2637.64 --> 2638.42]  Let alone searching.
[2638.50 --> 2638.76]  Right.
[2638.90 --> 2639.16]  Yeah.
[2639.38 --> 2642.92]  I, you know, this is still very early days.
[2642.92 --> 2647.88]  So, uh, it's very difficult to predict, but the way I think about it, it, I think about
[2647.88 --> 2654.04]  it in, in terms of like, maybe we have, there are different types of computers that can exist
[2654.04 --> 2654.88]  in the world.
[2654.88 --> 2658.14]  Like a traditional, you know, like PC, that's one type of computer.
[2658.56 --> 2661.24]  You can maybe say like the human brain is another type of computer.
[2661.76 --> 2666.64]  Um, and then these language models, I think they're, they're a new type of computer and they
[2666.64 --> 2671.98]  do some things a lot better than, you know, the PC type of computer did.
[2671.98 --> 2674.16]  Uh, and then something's much worse.
[2674.16 --> 2675.78]  Like they're far less precise.
[2676.48 --> 2680.64]  Um, I think I saw a tweet the other day where someone repeatedly asked, you know, GPT-4,
[2680.76 --> 2682.68]  whether, you know, four was greater than one.
[2682.80 --> 2688.04]  And then at some point GPT-4 got unsure of itself and said, oh no, actually I was mistaken.
[2688.20 --> 2689.22]  You know, one is greater than four.
[2689.42 --> 2690.00]  I apologize.
[2690.68 --> 2691.68]  Yeah, exactly.
[2691.80 --> 2692.12]  Exactly.
[2692.76 --> 2692.90]  Yeah.
[2693.18 --> 2693.94]  So I apologize.
[2694.28 --> 2697.72]  So I think these two types of computers are actually very complimentary.
[2697.72 --> 2703.52]  And so like the most powerful systems are going to be the ones that combine both and
[2703.52 --> 2708.34]  feed the inputs of one and the outputs of the other, uh, and, and synthesize them in
[2708.34 --> 2709.22]  a way that's truly powerful.
[2709.22 --> 2711.78]  And, and we're already seeing early examples of this.
[2711.78 --> 2716.82]  Like Cody is one, you know, we use kind of like the, the Chomsky style, like code understanding
[2716.82 --> 2720.76]  tech with the more Norvig style, you know, language models.
[2720.76 --> 2725.94]  Um, Bing search is another, you know, where, uh, they're using chat GPT, uh, for, for
[2725.94 --> 2729.32]  the AI part of it, but they're still relying on kind of traditional Bing web search.
[2729.32 --> 2733.08]  And so I think we'll see a lot of hybrid systems emerge that combine the best of both worlds.
[2733.40 --> 2733.54]  Yeah.
[2735.02 --> 2735.70]  Exciting times.
[2735.78 --> 2736.56]  Thanks for talking to us.
[2736.68 --> 2736.84]  Yeah.
[2736.88 --> 2737.78]  Thanks for having me on.
[2738.04 --> 2738.68]  Good seeing you again.
[2738.72 --> 2739.14]  Good talking.
[2739.46 --> 2740.26]  Pleasure chatting with you.
[2741.04 --> 2741.40]  Yeah.
[2741.40 --> 2741.94]  That was fun.
[2742.02 --> 2742.36]  That's exciting.
[2742.36 --> 2743.08]  You guys are good at this.
[2743.08 --> 2743.84]  I'm excited for you.
[2743.84 --> 2743.94]  Yeah.
[2743.94 --> 2744.12]  Yeah.
[2744.12 --> 2744.34]  Yeah.
[2744.34 --> 2744.40]  Yeah.
[2744.40 --> 2744.94]  Yeah.
[2744.94 --> 2745.00]  Yeah.
[2745.00 --> 2745.50]  Yeah.
[2745.50 --> 2746.00]  Yeah.
[2746.00 --> 2746.38]  Yeah.
[2746.38 --> 2746.50]  Yeah.
[2746.50 --> 2747.00]  Yeah.
[2747.00 --> 2747.06]  Yeah.
[2750.76 --> 2765.04]  So in the sponsor of Minnesota here in the breaks, I'm here with Tom who dev advocate
[2765.04 --> 2767.18]  at Sentry on the code cove team.
[2767.18 --> 2770.48]  So Tom, tell me about Sentry's acquisition of code cove.
[2770.76 --> 2774.12]  And in particular, how is this improving the Sentry platform?
[2774.62 --> 2779.12]  When I think about the acquisition, when I think about how does Sentry use code cove or
[2779.12 --> 2781.28]  conversely, how does code cove use Sentry?
[2781.52 --> 2784.62]  Like I think of code cove and I think of the time of deploy.
[2784.92 --> 2787.82]  When you're a software developer, you have your listicle, you write your code, you test
[2787.82 --> 2791.58]  your code, you deploy, and then your code goes into production and then you sort of fix
[2791.58 --> 2792.04]  the bugs.
[2792.32 --> 2795.70]  And I sort of think of that split in time as like when you actually do that deploy.
[2796.38 --> 2799.46]  Now, where code cove is really useful is before deploy time.
[2799.76 --> 2801.34]  It's when you are developing your code.
[2801.50 --> 2804.00]  It's when you're saying, hey, like, I want to make sure this is going to work.
[2804.00 --> 2806.28]  I want to make sure that I have as few bugs as possible.
[2806.28 --> 2810.02]  I want to make sure that I've thought of all the errors and all the edge cases and whatnot.
[2810.64 --> 2812.62]  And Sentry is the flip side of that.
[2812.90 --> 2815.58]  It says, hey, what happens when you hit production, right?
[2815.62 --> 2819.24]  When you have a bug and you need to understand what's happening in that bug, you need to understand
[2819.24 --> 2820.18]  the context around it.
[2820.24 --> 2823.44]  You need to understand where it's happening, what the stack trace looks like, what other
[2823.44 --> 2828.70]  local variables exist at that time so that you can debug that and hopefully you don't
[2828.70 --> 2829.88]  see that error case again.
[2830.14 --> 2834.22]  When I think of like, oh, what can Sentry do with code cove or what can code cove do with
[2834.22 --> 2834.56]  Sentry?
[2835.00 --> 2839.14]  It's sort of taking that entire spectrum of the developer lifecycle of, hey, what can
[2839.14 --> 2843.64]  we do to make sure that you ship the least buggy code that you can?
[2844.04 --> 2848.56]  And when you do come to a bug that is unexpected, you can fix it as quickly as possible, right?
[2848.76 --> 2851.62]  Because, you know, as developers, we want to write good code.
[2851.74 --> 2854.74]  We want to make sure that people can use the code that we've written.
[2855.04 --> 2856.96]  We want to make sure that they're happy with the product.
[2857.06 --> 2857.90]  They're happy with the software.
[2857.90 --> 2859.56]  And it works the way that we expect it to.
[2859.56 --> 2864.50]  If we can build a product, you know, the Sentry plus code cove thing to make sure that you
[2864.50 --> 2871.10]  are de-risking your code changes and de-risking your software, then, you know, we've hopefully
[2871.10 --> 2873.56]  done the developer community as service.
[2874.14 --> 2877.06]  So Tom, you say bring your tests and you'll handle the rest.
[2877.16 --> 2877.80]  Break it down for me.
[2877.86 --> 2881.30]  How does a team get started with code cove?
[2881.74 --> 2885.98]  You know, what you bring to the table is like testing and you bring your coverage reports.
[2885.98 --> 2890.26]  And what code cove does is we say, hey, give us your coverage reports, give us access to
[2890.26 --> 2894.78]  your code base so that we can, you know, overlay code coverage on top of it and give us access
[2894.78 --> 2895.56]  to your CICD.
[2895.96 --> 2901.62]  And so with those things, what we do and what code cove is really powerful at is that it's
[2901.62 --> 2903.68]  not just, hey, like this is your code coverage number.
[2903.90 --> 2905.72]  It's, hey, here's a code coverage number.
[2906.00 --> 2910.58]  And your viewer also knows and other parts of your organization know as well.
[2910.70 --> 2914.10]  So it's not just you dealing with code coverage and saying, I don't really know what to do
[2914.10 --> 2914.56]  with this.
[2914.56 --> 2919.48]  Because we take your code coverage, we analyze it and we throw it back to you into your developer
[2919.48 --> 2920.02]  workflow.
[2920.58 --> 2923.54]  And by developer workflow, I mean your pull request, your merge request.
[2923.90 --> 2927.98]  And we give it to you as a comment so that you can see, oh, great, this was my code coverage
[2927.98 --> 2928.34]  change.
[2928.72 --> 2932.96]  But not only do you see this sort of information, but your viewer also sees it and they can tell,
[2933.12 --> 2935.38]  oh, great, you've tested your code or you haven't tested your code.
[2935.84 --> 2940.22]  And we also give you a status check, which says, hey, like you've met whatever your team's
[2940.22 --> 2944.06]  decision on what your code coverage should be, or you haven't met that goal, whatever it
[2944.06 --> 2944.66]  happens to be.
[2944.92 --> 2949.36]  And so CodeCov is particularly powerful in making sure that code coverage is not just
[2949.36 --> 2953.66]  a thing that you're doing on your own island as a developer, but that your entire team can
[2953.66 --> 2955.66]  get involved with and can make decisions.
[2955.66 --> 2956.48]  Very cool.
[2956.54 --> 2957.04]  Thank you, Tom.
[2957.18 --> 2964.14]  So, hey, listeners, head to Sentry and check them out, Sentry.io and use our code changelog.
[2964.38 --> 2970.20]  So the cool thing is, is our listeners, you get the team plan for free for three months,
[2970.48 --> 2973.78]  not one month, not two months, three months.
[2974.22 --> 2974.48]  Yes.
[2974.78 --> 2976.48]  The team plan for free for three months.
[2976.48 --> 2977.76]  Use the code changelog.
[2977.86 --> 2980.60]  Again, Sentry.io.
[2980.86 --> 2984.36]  That's S-E-N-T-R-Y.io.
[2984.68 --> 2986.14]  And use the code changelog.
[2986.24 --> 2989.08]  Also check out our friends over at CodeCov.
[2989.20 --> 2991.36]  That's CodeCov.io.
[2991.72 --> 2994.34]  Like code coverage, but just shortened to CodeCov.
[2994.78 --> 2995.98]  CodeCov.io.
[2996.54 --> 2996.94]  Enjoy.
[2996.94 --> 2997.12]  Enjoy.
[2997.12 --> 2997.22]  Enjoy.
[2997.22 --> 2997.72]  Enjoy.
[2997.72 --> 2997.94]  Enjoy.
[2997.94 --> 2998.94]  Enjoy.
[2998.94 --> 2999.22]  Enjoy.
[2999.22 --> 2999.94]  Enjoy.
[2999.94 --> 3000.94]  Enjoy.
[3000.94 --> 3001.72]  Enjoy.
[3001.72 --> 3002.22]  Enjoy.
[3002.22 --> 3002.72]  Enjoy.
[3002.72 --> 3003.22]  Enjoy.
[3003.22 --> 3003.72]  Enjoy.
[3003.72 --> 3004.72]  Enjoy.
[3004.72 --> 3005.72]  Enjoy.
[3005.72 --> 3021.02]  So now we're fine-tuned here.
[3021.06 --> 3021.54]  We're ready to go.
[3021.54 --> 3021.70]  I think so.
[3021.90 --> 3022.06]  Okay.
[3022.46 --> 3023.76]  I see what you did there.
[3025.08 --> 3026.90]  Swine-tuned, I think, is what you were trying to say.
[3027.34 --> 3029.22]  Well, no, I think it was a Dolly reference, fine-tuned.
[3029.52 --> 3030.20]  So, yeah.
[3030.32 --> 3030.76]  It was a pun.
[3031.06 --> 3031.52]  It was a pun.
[3032.56 --> 3033.42]  Work with us, Jared.
[3033.50 --> 3035.10]  I mean, Adam and I are already on the same page.
[3035.14 --> 3035.62]  What the heck, man?
[3035.62 --> 3038.10]  Adam's puns are on point always.
[3038.62 --> 3039.60]  He never misses with a pun.
[3039.80 --> 3040.34]  All right.
[3040.44 --> 3040.86]  Thank you.
[3041.32 --> 3041.68]  All right.
[3041.68 --> 3045.94]  So we have Denny Lee from Databricks or Databricks.
[3046.24 --> 3046.56]  Databricks.
[3046.94 --> 3047.22]  Databricks.
[3047.22 --> 3047.42]  Yes.
[3047.46 --> 3048.22]  Is that the official stance?
[3048.24 --> 3049.30]  It's not a Canadian or American thing.
[3049.36 --> 3050.00]  It's just Databricks.
[3050.02 --> 3050.62]  It's just Databricks.
[3050.62 --> 3050.74]  Yeah, yeah.
[3051.46 --> 3058.48]  Here to talk about Dolly 2, but first, I hear you're a just-in-time conference presenter.
[3058.98 --> 3060.10]  Tell us what this means.
[3060.10 --> 3065.12]  Well, I think the context was that you were asking me, hey, what's your presentation?
[3065.22 --> 3066.14]  That's what you asked me first.
[3066.28 --> 3066.38]  I did.
[3066.38 --> 3071.48]  And I was actually responding, I don't remember the name, nor do I remember- I do remember the
[3071.48 --> 3071.98]  concepts.
[3072.22 --> 3073.20]  At least I do have that part.
[3073.42 --> 3074.60]  But I don't remember the name.
[3074.70 --> 3075.00]  Nor.
[3075.00 --> 3076.98]  Nor are the slides done yet.
[3077.06 --> 3078.60]  And this is-
[3078.60 --> 3078.88]  Normal.
[3078.96 --> 3079.94]  And it starts in 30 minutes.
[3080.14 --> 3080.16]  No.
[3080.18 --> 3080.88]  No, no, no, no, no, no.
[3080.90 --> 3081.18]  Tomorrow.
[3081.38 --> 3081.64]  No, no.
[3081.66 --> 3082.04]  Tomorrow.
[3082.14 --> 3082.50]  Tomorrow.
[3082.84 --> 3083.08]  Okay.
[3083.28 --> 3089.52]  I'm just simply saying that it is common for me to go ahead and not do a thing until 30 minutes
[3089.52 --> 3091.72]  before the actual presentation to create the slides.
[3091.76 --> 3092.92]  So you're a procrastinator.
[3093.28 --> 3093.68]  Yes.
[3093.90 --> 3094.86]  I'm a very good one.
[3095.12 --> 3096.50]  That's not procrastination.
[3096.64 --> 3096.72]  No.
[3096.88 --> 3097.12]  Efficiency.
[3097.12 --> 3097.62]  That's optimization.
[3098.06 --> 3098.36]  Efficiency.
[3098.68 --> 3099.18]  Pure efficiency.
[3099.32 --> 3101.22]  Why sweat over the details until you have to?
[3101.30 --> 3101.70]  Exactly.
[3101.98 --> 3102.20]  Exactly.
[3102.20 --> 3108.30]  Because what if you start 30 minutes before, but you realize the details required 45 minutes?
[3108.52 --> 3112.34]  So I had this one time where actually a buddy of mine, Thomas Kaiser, he and I went ahead
[3112.34 --> 3114.80]  and did a presentation where he- so he's from Denmark.
[3115.14 --> 3115.86]  I'm from Seattle.
[3116.12 --> 3120.14]  We're both in, I don't know where, some other city to do the presentation.
[3120.36 --> 3120.88]  Somewhere in the world.
[3121.02 --> 3121.68]  Somewhere in the world.
[3122.04 --> 3126.16]  So we actually got together, but we realized we actually hadn't done squat on the slides
[3126.16 --> 3128.60]  until 30 minutes before the actual session.
[3128.94 --> 3129.46]  And guess what?
[3129.46 --> 3132.80]  So 30 minutes before, put together the slides, bam, we're good to go.
[3133.84 --> 3134.82]  Has it ever bit you?
[3136.14 --> 3137.16]  I'm sure-
[3137.16 --> 3137.48]  Tomorrow.
[3138.14 --> 3140.72]  I'm sure at some point it will bite me.
[3141.50 --> 3145.02]  I guess the context is I've gotten away with it so far.
[3145.64 --> 3146.38]  So I'm going to go with it.
[3146.40 --> 3148.20]  And enough times that you have full confidence.
[3148.44 --> 3148.78]  Yes.
[3149.32 --> 3149.80]  Fair enough.
[3150.06 --> 3150.32]  Yes.
[3150.46 --> 3151.64]  Or at least I know how to fake it.
[3152.04 --> 3154.00]  So what would you like to know about Dolly?
[3154.14 --> 3156.38]  About Dolly 1, how he came about with Dolly 1.0?
[3156.38 --> 3156.58]  Why?
[3156.78 --> 3157.50]  Let's start with why.
[3157.50 --> 3157.72]  All right.
[3157.78 --> 3158.26]  Let's start with why.
[3158.36 --> 3158.76]  And then how?
[3158.76 --> 3159.28]  All right.
[3159.34 --> 3160.72]  So let's go backwards a little bit.
[3160.90 --> 3161.16]  That's when.
[3161.34 --> 3162.00]  No, you're talking when.
[3162.02 --> 3163.48]  All the way back three weeks ago.
[3163.76 --> 3163.90]  Okay?
[3164.10 --> 3164.28]  Okay.
[3164.64 --> 3164.96]  Roughly.
[3165.36 --> 3166.48]  In the days of yore.
[3166.54 --> 3166.72]  Yeah.
[3166.76 --> 3168.12]  In the days of yore four weeks ago.
[3168.22 --> 3168.48]  All right?
[3168.98 --> 3172.62]  So one of the things that, and I want to give credit where credit's you.
[3172.70 --> 3174.44]  Mike Conover is the guy who actually figured it out.
[3174.54 --> 3174.74]  Okay.
[3174.74 --> 3174.82]  Okay.
[3175.46 --> 3179.98]  Now, we were using a much older particular model.
[3180.62 --> 3183.38]  And we're going like, eh, would this work?
[3183.58 --> 3183.72]  Right?
[3184.12 --> 3188.08]  And what it boiled down to is that there's a supposition that could you take an older model,
[3188.50 --> 3192.78]  fine tune it with good data, and still actually end up getting good results?
[3192.78 --> 3198.46]  With the key point being that, hey, we're only going to pay $30 to actually train the data
[3198.46 --> 3202.42]  as opposed to, oh, the tens of millions of dollars that you'd have to do.
[3203.14 --> 3203.96]  And could you do it?
[3203.96 --> 3204.04]  Okay.
[3204.26 --> 3206.38]  That was the supposition for Dolly 1.0.
[3206.62 --> 3208.50]  And sure enough, we were right.
[3209.30 --> 3215.82]  Basically, it was about $30 worth of training time on what is not considered public data.
[3216.04 --> 3217.20]  So that's why it's Dolly 1.0.
[3217.40 --> 3217.58]  Okay.
[3217.60 --> 3218.42]  So we could give you the weights.
[3218.50 --> 3219.08]  We could give you the model.
[3219.16 --> 3222.78]  But we couldn't give you the data because the data itself was actually not public.
[3222.88 --> 3223.52]  But you owned it.
[3223.94 --> 3224.24]  No, no.
[3224.38 --> 3227.92]  That was the, in fact, I believe it was the same data that ChatGPT was using.
[3228.12 --> 3229.30]  So we could give you the weights.
[3229.30 --> 3230.30]  Again, that's open source.
[3230.40 --> 3230.50]  Right.
[3230.50 --> 3232.46]  But we can't do the data because the data is actually ChatGPT.
[3232.54 --> 3232.74]  Gotcha.
[3232.74 --> 3232.82]  Okay.
[3232.82 --> 3233.42]  All right.
[3233.50 --> 3238.86]  So then we're going, wait, we actually used only a tiny amount of data and it still came
[3238.86 --> 3240.64]  out with some pretty decent results.
[3240.84 --> 3241.04]  Okay.
[3241.18 --> 3244.56]  Let's go ahead and say, why don't we generate our own data?
[3245.32 --> 3247.76]  So again, take credit where credit is due.
[3247.98 --> 3251.94]  Our founders went ahead and said, hey, why don't we just get, we have about 5,000 employees
[3251.94 --> 3252.74]  at Databricks now.
[3252.90 --> 3253.56]  This is my favorite part.
[3253.68 --> 3253.82]  Yeah.
[3254.00 --> 3256.22]  Let's just go ahead and generate our own data.
[3256.34 --> 3258.48]  So for two weeks, that's literally all we did.
[3258.48 --> 3263.88]  We had basically a bunch of employees dumping in data in a Q&A style format.
[3264.02 --> 3265.12]  We had seven different categories.
[3265.30 --> 3266.10]  It's all listed out there.
[3266.14 --> 3267.88]  So I don't remember all those details anymore.
[3268.68 --> 3269.84]  I worked on the t-shirts.
[3269.98 --> 3271.30]  So at least I was helpful on that part.
[3271.36 --> 3271.90]  Love the t-shirt.
[3272.04 --> 3272.16]  Yeah.
[3272.16 --> 3272.66]  That's a good one.
[3272.74 --> 3274.42]  No one's seeing this right now, but it is a...
[3274.42 --> 3274.72]  Well, yeah.
[3274.72 --> 3275.44]  It is a podcast.
[3275.86 --> 3276.30]  That's right.
[3276.42 --> 3277.08]  That tends to...
[3277.08 --> 3278.50]  Draw a word picture, Adam.
[3278.50 --> 3279.30]  Dude, a sheep.
[3279.52 --> 3280.34]  Come on, man.
[3280.42 --> 3280.90]  It's Dolly.
[3281.18 --> 3281.32]  It's a sheep.
[3281.32 --> 3281.58]  Dolly.
[3281.68 --> 3282.00]  Dolly.
[3282.00 --> 3282.04]  Dolly.
[3282.04 --> 3282.28]  Sheep.
[3282.28 --> 3282.78]  Oh, my gosh.
[3283.02 --> 3283.74]  Oh, my goodness.
[3283.74 --> 3284.88]  See, I already thought he was on point.
[3285.08 --> 3285.36]  Oh.
[3286.20 --> 3286.56]  Okay.
[3286.84 --> 3289.04]  So Dolly, the sheep, a clone, right?
[3289.12 --> 3289.94]  It's a clone, right?
[3290.02 --> 3290.88]  So that's the whole context.
[3291.06 --> 3291.08]  It's a clone.
[3291.34 --> 3291.58]  Yes.
[3291.80 --> 3293.50]  So we go ahead and actually get that up and running.
[3293.82 --> 3300.88]  And then we're like, hey, now we've got 15,000 plus so set of Q&A style new information,
[3301.02 --> 3304.24]  all brand new, and we're publicly giving it away, right?
[3304.24 --> 3310.42]  So the actual data set, if you go to Hugging Face or Databricks Labs slash Dolly or whatever
[3310.42 --> 3314.72]  the GitHub site is, basically all that data is there, okay?
[3314.84 --> 3316.02]  All 15,000 lines.
[3316.46 --> 3317.56]  Sorry, lines.
[3317.80 --> 3319.10]  15,000 Q&As.
[3319.34 --> 3319.58]  Okay.
[3320.04 --> 3325.72]  And then we train that data set again using the same old model from two years ago, okay?
[3326.10 --> 3326.38]  Okay.
[3326.46 --> 3330.94]  And we ran that, and then basically what was really cool about this is that it cost us
[3330.94 --> 3334.02]  about $100 worth of training, but it's pretty good.
[3334.02 --> 3338.22]  And if you ask some pointed questions on this stuff, it actually responds really, really
[3338.22 --> 3338.50]  well.
[3338.68 --> 3343.32]  For example, I've got some examples where I'm actually asking coffee questions, and the coffee
[3343.32 --> 3348.40]  questions answers are, okay, I'll give ChatGBT4.0 a lot of credit.
[3348.56 --> 3348.72]  Yeah.
[3348.80 --> 3352.10]  It is much more verbose than what Dolly 2.0 can provide.
[3352.44 --> 3354.72]  But in terms of correctness, it is correct.
[3354.84 --> 3359.34]  They both are the same level of correctness between Dolly 2.0 and ChatGBT4.0.
[3359.34 --> 3363.54]  I actually have it on my own, like, it's on my own GitHub somewhere, like a review where
[3363.54 --> 3364.40]  I actually explain all that.
[3364.76 --> 3368.42]  Mainly because I was actually running it on an M1 Mac, too, because I was goofing off and
[3368.42 --> 3369.18]  decided to do it.
[3369.18 --> 3369.20]  Which is fine.
[3369.34 --> 3370.30]  That's amazing right there.
[3370.46 --> 3370.56]  Yeah.
[3370.62 --> 3376.50]  Let me first just say, as a daily user of ChatGBT, sometimes verbose is not desirable.
[3376.50 --> 3376.90]  Yes.
[3376.90 --> 3381.06]  And I'm like, dude, I actually will tell it to be brief or in one sentence.
[3381.16 --> 3381.64]  Very specific.
[3381.64 --> 3384.76]  Because I'm so sick of the word salad that spits out.
[3384.82 --> 3385.78]  I'm like, I just want the answer.
[3385.98 --> 3386.08]  Right.
[3386.08 --> 3387.36]  The answers are, you know, useful.
[3387.64 --> 3387.82]  Yes.
[3387.84 --> 3390.66]  But sometimes you're like waiting for it to tell me the whole history of the thing.
[3390.76 --> 3391.08]  You're like, no.
[3391.38 --> 3393.96]  Well, don't you want to know, like, the retrospective while you're at it?
[3394.40 --> 3396.00]  I'm being very sarcastic about it.
[3396.08 --> 3396.22]  Yes.
[3396.48 --> 3399.74]  People can't tell it's a podcast, but we're all eye-rolling each other on that one.
[3399.92 --> 3400.02]  We are.
[3400.12 --> 3401.24]  That was major eye-rolls.
[3401.24 --> 3409.74]  So using it, let's say I've never used anything but ChatGBT's web UI.
[3409.86 --> 3410.02]  Sure.
[3410.04 --> 3410.62]  But I'm a developer.
[3410.84 --> 3411.02]  Sure.
[3411.18 --> 3412.34]  And I want my own.
[3412.56 --> 3414.68]  I want Dolly to answer my questions.
[3414.88 --> 3415.06]  Yes.
[3415.22 --> 3416.70]  What does that process look like for folks?
[3416.82 --> 3416.98]  Okay.
[3417.06 --> 3418.36]  So you've got two choices.
[3419.06 --> 3419.60]  No, no.
[3419.62 --> 3420.24]  I should rephrase it slightly.
[3420.28 --> 3421.34]  You've got many choices, in fact.
[3421.34 --> 3426.64]  But the most common choices are we have a Databricks notebook that's in the Dolly GitHub
[3426.64 --> 3429.42]  that you can just download for free, run it.
[3429.42 --> 3433.40]  Now, then you're going to tell me, but Denny, I don't want to use Databricks.
[3433.82 --> 3434.34]  That's fair.
[3434.44 --> 3436.44]  I would prefer you to, but I understand if you don't.
[3436.70 --> 3437.06]  That's fine.
[3437.16 --> 3438.06]  Go to Hugging Face.
[3438.72 --> 3441.96]  The instructions are all right there on how to use it.
[3442.04 --> 3445.68]  In fact, like I was saying, I was actually playing with it so that way I could optimize
[3445.68 --> 3448.66]  for an M1 Mac and so that the answers could come back faster.
[3448.82 --> 3448.92]  Right.
[3449.24 --> 3453.50]  My only problem was that when I started testing it, there was an obvious bug and pie torch.
[3454.18 --> 3454.54]  Okay.
[3454.54 --> 3459.88]  Because basically when we told it to go ahead and use the M1, it was giving us back garbage
[3459.88 --> 3460.30]  answers.
[3460.54 --> 3462.02]  Like it wasn't even like actual answers.
[3462.02 --> 3466.24]  It was literally like nonsensical characters.
[3466.42 --> 3466.64]  Okay.
[3466.90 --> 3469.66]  And when we used CPU mode, it worked perfectly fine.
[3469.94 --> 3474.62]  But then just as I was about to create a new issue on pie torch, they fixed it.
[3474.90 --> 3475.66]  No, that's a good thing.
[3475.72 --> 3476.12]  That's a good thing.
[3476.32 --> 3476.46]  I know.
[3476.52 --> 3478.06]  But I also had the fix.
[3478.42 --> 3479.34]  Oh, you had the fix.
[3479.34 --> 3479.78]  Okay.
[3480.34 --> 3480.68]  That's it.
[3480.80 --> 3481.24]  I get you.
[3481.62 --> 3482.80]  You're about to have a contrived.
[3482.94 --> 3483.68]  I was going to waste my time.
[3483.70 --> 3484.72]  You wasted my time.
[3484.72 --> 3485.24]  Damn it.
[3485.36 --> 3485.72]  But no, no.
[3485.90 --> 3486.88]  But it's fun.
[3486.98 --> 3490.36]  But basically the idea is that obviously, okay, I shouldn't say obviously.
[3490.50 --> 3490.84]  Can I share a question about that?
[3490.84 --> 3493.72]  You probably don't want to train with an M1, but you can definitely do inference with
[3493.72 --> 3493.92]  M1.
[3494.12 --> 3494.20]  Sorry.
[3494.40 --> 3494.98]  The Q&A.
[3495.06 --> 3495.78]  So you got your data.
[3496.02 --> 3501.68]  So how do you collect that data and how do you format it so that Dolly can understand
[3501.68 --> 3501.84]  it?
[3501.84 --> 3502.18]  No joke.
[3502.30 --> 3504.62]  I'm assuming you're saying, so don't use Databricks data.
[3504.92 --> 3506.50]  You could do the same thing like you did with the Q&A.
[3506.50 --> 3506.58]  Yes, absolutely.
[3506.78 --> 3507.02]  Literally.
[3507.24 --> 3507.78]  It's not at work.
[3507.78 --> 3509.54]  When we asked people to fill out, it was a Google form.
[3509.76 --> 3510.00]  Okay.
[3510.36 --> 3511.18]  That's literally it.
[3511.50 --> 3512.38]  And what were the questions?
[3512.88 --> 3513.24]  Oh, no, no.
[3513.36 --> 3516.36]  They could produce the questions and then the answers.
[3516.58 --> 3519.28]  They would ask a question and then it would spit out.
[3519.28 --> 3520.76]  Provide a detailed answer for it.
[3520.80 --> 3521.12]  I see.
[3521.22 --> 3523.26]  So how do you make an espresso?
[3523.42 --> 3523.94]  How do you make?
[3524.14 --> 3524.76]  To choose coffee.
[3525.02 --> 3526.64]  It wouldn't even be how do you make an espresso.
[3526.78 --> 3527.84]  For example, let's be very specific.
[3528.02 --> 3528.12]  Okay.
[3528.60 --> 3535.92]  It would say, what are the particular features of great espresso?
[3536.36 --> 3536.66]  Okay.
[3536.66 --> 3536.74]  Okay.
[3537.02 --> 3541.02]  And then we would talk about, okay, you're required to have a fine grind.
[3541.26 --> 3544.62]  You're required to, using a conical burr grinder.
[3544.90 --> 3547.40]  There's a religious war between flat burr grinders and conical burr grinders.
[3547.74 --> 3548.78]  I put in conical burr grinders.
[3548.90 --> 3552.52]  So, yeah, I'm sure the flat burr grinders are pissed off that that's not the answer that
[3552.52 --> 3553.12]  they're going to get from Dolly.
[3553.24 --> 3553.58]  That's bias.
[3553.72 --> 3554.70]  You're putting bias into them.
[3554.72 --> 3555.24]  Yes, absolutely.
[3555.30 --> 3556.82]  There's absolutely 100% bias.
[3556.94 --> 3557.82]  Let's not pretend there isn't.
[3557.90 --> 3558.02]  Okay?
[3558.08 --> 3558.30]  Okay.
[3558.30 --> 3562.90]  So, it also requires you to actually have coffee beans roasted in a particular way.
[3563.24 --> 3567.24]  It also requires you to have the espresso water boiled at a particular temperature.
[3567.76 --> 3568.02]  Okay.
[3568.02 --> 3570.50]  So, you put all of those details down.
[3571.28 --> 3572.12]  That's the idea.
[3572.30 --> 3575.16]  Like, so, in other words, it's not just like, okay, hi, how are you doing?
[3575.16 --> 3576.08]  Like, what's great espresso?
[3576.68 --> 3578.70]  You buy from Espresso Vivace in Seattle.
[3578.84 --> 3582.66]  I mean, while that's true, and I'm basically, I don't own any stock in them, by the way, but
[3582.66 --> 3584.20]  they are easily the best coffee.
[3584.30 --> 3585.12]  Who's the brand against you?
[3585.36 --> 3586.80]  Espresso Vivace in Seattle.
[3586.92 --> 3587.30]  Espresso Vivace.
[3587.30 --> 3590.82]  Yeah, David Shomer is a magician when it comes to espresso.
[3591.12 --> 3591.32]  Okay.
[3592.22 --> 3595.48]  But the context is like, well, as much as I want to just provide an answer like that,
[3595.62 --> 3596.38]  the reality is no.
[3596.62 --> 3597.78]  Obviously, we can't train that bad.
[3597.88 --> 3603.20]  We actually need verbosity to provide context, provide proof, if you want to put it that way.
[3603.78 --> 3607.34]  Because there's going to be other people putting other answers, too.
[3607.86 --> 3608.08]  Oh.
[3608.30 --> 3611.60]  So, for example, in this case, I'm just going to call a buddy of mine, Rob Reed.
[3611.60 --> 3612.66]  He's a fellow cyclist.
[3612.82 --> 3614.30]  He's also a fellow coffee addict.
[3614.30 --> 3618.02]  I know he also put some coffee answers inside there as well.
[3618.42 --> 3623.20]  So, between everybody that put coffee answers in there, that's actually literally, you're
[3623.20 --> 3627.26]  getting data from myself, from Rob, and a few other folks from, well, Databricks.
[3627.60 --> 3627.84]  Right.
[3628.06 --> 3631.66]  And how many instructions are in there that you guys put in?
[3631.72 --> 3632.56]  The 5,000 employees?
[3633.00 --> 3634.70]  Oh, 5,000 employees put 15,000.
[3634.82 --> 3635.56]  15,000.
[3635.86 --> 3636.76]  So, it's remarkable.
[3636.88 --> 3638.94]  If you think about it, that's remarkably small.
[3639.30 --> 3639.46]  Yeah.
[3639.46 --> 3643.30]  We were always under the impression when we started this process that we would require hundreds
[3643.30 --> 3645.88]  of thousands or millions of answers.
[3645.88 --> 3646.70]  I was going to say, how does it know?
[3646.76 --> 3647.96]  You gave it coffee instructions.
[3648.16 --> 3648.30]  Yeah, yeah, yeah.
[3648.30 --> 3648.42]  Yeah.
[3648.56 --> 3648.70]  No.
[3648.86 --> 3650.04]  How does it know something totally different?
[3650.06 --> 3652.38]  Like I said, Dolly1.0 shocked us.
[3652.62 --> 3656.34]  It really shocked us because we thought we would need to put in a lot more data.
[3656.58 --> 3658.44]  We thought we would need to do a lot more training.
[3658.72 --> 3662.00]  And then we were like, wow, this is not bad.
[3662.08 --> 3664.62]  I mean, it's not perfect, but it's not bad, actually.
[3664.62 --> 3669.06]  And so, from a business perspective, what ends up happening is if you have your own business,
[3669.60 --> 3673.20]  now your data, you don't need a million things.
[3673.32 --> 3675.42]  You've got 15,000 pieces of information.
[3676.04 --> 3678.44]  Now, the great thing, and I'm not telling you to use Dolly, by the way.
[3678.50 --> 3680.02]  I mean, obviously, go use it if you want to.
[3680.08 --> 3682.90]  But I'm saying, use any open source model.
[3683.18 --> 3684.22]  I don't care which one.
[3684.64 --> 3688.60]  That way, you get to go ahead and keep it and have your data as your IP.
[3689.12 --> 3693.84]  So, you as a business end up using the data actually in a good way.
[3693.86 --> 3694.14]  Right.
[3694.28 --> 3699.54]  Where you actually make it advantageous for you, yet also keeping the privacy for the users that make up that data.
[3699.74 --> 3700.44]  At the exact same time.
[3700.50 --> 3704.12]  So, the move is you have these, I don't know if this is technically what a foundational model is,
[3704.18 --> 3707.20]  or you have these models that are large enough language models.
[3707.36 --> 3707.66]  Right.
[3707.80 --> 3708.08]  Right?
[3708.24 --> 3713.84]  And then each company or each org or each use case says, okay, now we're going to fine-tune it.
[3714.06 --> 3714.32]  Right.
[3714.32 --> 3715.40]  I don't know if that's the right language or not.
[3715.54 --> 3715.86]  It is.
[3715.86 --> 3718.30]  And apply it to us.
[3718.56 --> 3718.76]  Right.
[3718.92 --> 3720.34]  And there are going to be all sorts of, exactly.
[3720.56 --> 3721.98]  There's all sorts of models out there.
[3722.12 --> 3728.50]  There are already, like, a lot of people were asking me originally, like, hey, okay, well, then, you need to use Dolly.
[3728.58 --> 3729.40]  I'm like, no, no, no, no.
[3729.94 --> 3732.80]  Dolly was just us proving that it can be done.
[3733.26 --> 3734.18]  That's all it was.
[3734.58 --> 3741.42]  So, there are a lot of really good companies, whether it's Hugging Face or anybody else, that produces solid, open source, large language models.
[3741.50 --> 3741.62]  Yeah.
[3741.94 --> 3742.86]  Use those, too.
[3742.86 --> 3749.86]  Because the whole point is that you can use it yourself, run it with smaller amounts of data, have really good answers, and you're paying $100.
[3750.62 --> 3751.96]  At least, in our case, we did.
[3752.14 --> 3753.06]  $100 to train it.
[3753.22 --> 3753.38]  Right.
[3753.62 --> 3756.16]  So, we're like, okay, that's actually worth your business.
[3756.38 --> 3758.00]  You're protecting the privacy of your users.
[3758.46 --> 3761.40]  You're going ahead and actually having relatively solid answers.
[3761.40 --> 3765.44]  And you're not basically giving your data away to another service.
[3765.60 --> 3767.70]  Because that's the key thing about when you use a service.
[3768.04 --> 3768.24]  Right.
[3768.40 --> 3772.74]  That you're basically giving away your data so they can go train against the two.
[3772.94 --> 3773.20]  Right.
[3773.32 --> 3773.50]  Right?
[3773.58 --> 3777.90]  Now, I know Microsoft and OpenAI, for example, you're calling those two out in a positive way, not a negative.
[3778.26 --> 3780.68]  Usually, I'm a former Microsoft employee, so I'm allowed to be negative if I want to.
[3780.74 --> 3781.84]  But this is actually me being positive.
[3781.84 --> 3791.90]  They actually have introduced concepts saying you can pay more to train and that they'll never actually use your data.
[3792.38 --> 3795.80]  But I don't remember the cost, but it is definitely paying more.
[3796.18 --> 3796.38]  Yeah.
[3796.60 --> 3796.76]  Yeah.
[3797.68 --> 3800.64]  Well, it's not as valuable to them, so it makes sense as a transaction.
[3800.78 --> 3801.02]  Exactly.
[3801.20 --> 3802.78]  So, that becomes more of a transaction that way.
[3802.84 --> 3803.04]  Exactly.
[3803.82 --> 3806.86]  So, have you seen the Googler's leaked memo about we have no moat?
[3807.34 --> 3807.56]  Yes.
[3807.56 --> 3808.06]  Because isn't this like…
[3808.06 --> 3809.82]  Everybody talks about that memo.
[3809.82 --> 3812.90]  And what's interesting about that whole concept is that…
[3812.90 --> 3816.50]  I know it sounds sideways, but I was about to actually give you another context.
[3816.70 --> 3817.92]  And this is actually, again, my con over.
[3818.04 --> 3818.60]  I want to give credit.
[3818.78 --> 3820.22]  Attributions of the guy who actually said it.
[3821.12 --> 3824.76]  What's really interesting about this whole thing, when they talk about moat, they talk about everything else,
[3824.80 --> 3829.46]  is that more fundamentally, we could have done this two years ago.
[3830.46 --> 3837.74]  We could have taken this concept of basically saying small amount of data, foundational model, fine-tune it,
[3837.74 --> 3839.66]  and actually have good results.
[3839.82 --> 3843.88]  So, all of us were focusing on, I need a bigger model.
[3844.12 --> 3845.26]  I need to dump more data.
[3845.58 --> 3850.34]  I need to scrape the entire freaking internet and chuck it all into the gigantic model.
[3850.60 --> 3857.00]  Spend tens of millions of dollars, warp every single GPU until Azure basically melts in order to go ahead and train this thing.
[3857.10 --> 3858.06]  Until the heat death of the universe.
[3858.08 --> 3858.58]  Right, exactly.
[3859.02 --> 3865.50]  And then meanwhile, it's like, or we literally could have taken a foundational model that was okay to good,
[3867.10 --> 3870.06]  $100, and bam, we get something good.
[3870.14 --> 3870.28]  Yeah.
[3870.28 --> 3870.32]  Yeah.
[3870.66 --> 3874.70]  So, when they talk about, like, there's no moat and all this other stuff between open source and not,
[3875.18 --> 3878.34]  literally my attitude toward this whole thing is like, no, just step backwards for a second.
[3878.74 --> 3878.94]  Okay?
[3879.34 --> 3881.00]  The reality is we could have done this.
[3881.26 --> 3887.40]  We all got attracted to the idea, the shiny thing of, ooh, bigger, more, bigger, more, larger, more.
[3887.40 --> 3888.70]  That's all we got attracted to.
[3889.36 --> 3892.34]  And so, in the end, I'm going, I don't care.
[3893.60 --> 3898.68]  Like, these companies, the ones that, quote unquote, are trying to build a moat around themselves,
[3899.22 --> 3905.38]  what they're doing, they're trying to make sure that they have a service in which you will give them your data,
[3905.78 --> 3909.46]  and then by definition, you will give away your competitive advantage.
[3909.58 --> 3909.76]  Right.
[3910.00 --> 3910.52]  Simple as that.
[3910.52 --> 3917.56]  For the folks that don't want to do that, which I think is the vast majority, then my attitude is, like, quite simple.
[3917.74 --> 3920.02]  Then don't do that and build your own model.
[3920.16 --> 3922.28]  Now, how about if I'm the general consumer?
[3922.48 --> 3926.98]  I just want to pump out a good blog template for me to work with.
[3927.52 --> 3927.76]  Yeah.
[3928.36 --> 3928.76]  Absolutely.
[3929.68 --> 3930.22]  Why not?
[3930.38 --> 3930.48]  Yeah.
[3930.80 --> 3933.60]  Seriously, I'm not trying to say these services aren't worthwhile.
[3933.86 --> 3934.46]  Quite the opposite.
[3935.00 --> 3935.60]  ChatDB is fine.
[3935.62 --> 3936.10]  Very valuable.
[3936.10 --> 3936.46]  Oh, yeah.
[3936.54 --> 3937.62]  It's extremely valuable.
[3937.62 --> 3941.90]  In fact, I've already had it pumping out code for me just for shits and giggles.
[3942.18 --> 3942.28]  Yeah.
[3942.64 --> 3943.68]  So my Rust is-
[3943.68 --> 3945.54]  It's going to pump out some slides for you here soon for tomorrow.
[3945.56 --> 3946.20]  That's a good idea.
[3946.20 --> 3947.20]  I should test out that.
[3947.44 --> 3947.72]  Yeah, yeah.
[3948.02 --> 3948.96]  Take that 30 minutes.
[3949.04 --> 3949.76]  Turn it into 12.
[3949.82 --> 3950.16]  Oh, yeah.
[3950.16 --> 3950.80]  That'd be perfect.
[3950.88 --> 3951.08]  Yeah, yeah.
[3951.18 --> 3952.02]  But see, you get my drift.
[3952.38 --> 3952.94]  Yeah, totally.
[3953.14 --> 3953.26]  Yeah.
[3953.32 --> 3955.10]  So my Rust code is Rusty.
[3956.22 --> 3960.86]  And so basically, I was using ChatGBD to basically pump out a bunch of Rust code for me.
[3960.88 --> 3962.68]  I'm like, hey, this is a great boilerplate.
[3963.06 --> 3965.44]  Now I've got something to work with, and boom, now I can start writing again.
[3965.54 --> 3965.74]  Right.
[3966.04 --> 3966.14]  Yeah.
[3966.14 --> 3969.14]  So what is Databricks' play in this chess game?
[3969.26 --> 3970.34]  Like, what's your guys' angle?
[3970.58 --> 3971.56]  Our angle's quite simple.
[3971.96 --> 3974.48]  You've got a ton of data.
[3974.90 --> 3977.54]  You need to ETL and process it in the first place.
[3977.96 --> 3985.78]  Then you need to have a platform to run machine learning or data science or AI or whatever freaking wording you want to use.
[3985.78 --> 3986.14]  Okay?
[3986.38 --> 3996.76]  Whether it's LLMs today, deep learning yesterday or tomorrow, image optical resolutions, object recognition.
[3996.94 --> 3997.66]  I don't care.
[3997.90 --> 3998.06]  Okay?
[3998.20 --> 4000.30]  The point is that you have a ton of data.
[4001.04 --> 4002.58]  You need to be able to process it.
[4002.76 --> 4007.18]  You need to be able to access every single open source system or service.
[4008.68 --> 4009.82]  Databricks' play is quite simple.
[4009.82 --> 4011.40]  We just make it easy for you to do any of it.
[4011.74 --> 4011.92]  Yeah.
[4012.06 --> 4012.44]  That's it.
[4012.66 --> 4013.84]  That's our only play.
[4013.96 --> 4014.72]  Let's make it easy.
[4015.16 --> 4015.28]  Yeah.
[4015.42 --> 4015.56]  Yeah.
[4016.24 --> 4019.86]  Are you for, I guess, then, people owning their own data?
[4020.40 --> 4020.64]  Oh, no.
[4020.64 --> 4021.92]  It seems that that's your...
[4021.92 --> 4023.14]  So, here's the thing.
[4023.50 --> 4028.44]  I'm absolutely for both from a Databricks perspective but also from an open source perspective.
[4028.68 --> 4028.76]  Right?
[4028.94 --> 4029.10]  Yeah.
[4029.10 --> 4030.48]  So, I'm an open source contributor.
[4030.58 --> 4032.90]  I contributed to Apache Spark and MLflow.
[4033.22 --> 4035.24]  And I'm also a maintainer for Delta Lake.
[4035.58 --> 4035.74]  Okay?
[4036.10 --> 4037.28]  And so, yeah.
[4037.96 --> 4043.00]  By definition, I'm always going to lean toward open source, which means you should own your data.
[4043.12 --> 4044.30]  Data should be a competitive advantage.
[4044.84 --> 4047.74]  Everything else should be open source, basically, for all intents and purposes.
[4047.74 --> 4053.48]  I'm even for things like differential privacy and privacy-preserving histograms to basically protect your data.
[4053.66 --> 4056.86]  And I can go on a diatribe on that, so let's not do that.
[4057.28 --> 4064.82]  But the context is, I'm not saying, though, these services like OpenAI or Bing or whatever else aren't worthwhile.
[4065.44 --> 4065.92]  They are.
[4066.30 --> 4067.06]  They're cheap.
[4067.34 --> 4067.90]  They're helpful.
[4068.20 --> 4072.14]  In fact, training other systems isn't necessarily a bad thing either.
[4072.84 --> 4074.88]  For me, it's not about don't do it.
[4075.24 --> 4077.36]  It's about knowing what you're doing.
[4077.36 --> 4077.68]  Right.
[4077.86 --> 4078.20]  That's it.
[4078.30 --> 4078.38]  Yeah.
[4079.16 --> 4079.64]  Transparency.
[4079.72 --> 4079.92]  Exactly.
[4080.02 --> 4080.26]  That's it.
[4080.36 --> 4081.32]  That's my con.
[4081.90 --> 4086.32]  If you want to use OpenAI within a database platform, we make it easy.
[4086.52 --> 4091.24]  We have a, for crying out loud, we add a SQL syntax directly so you can literally write Spark SQL,
[4091.70 --> 4095.62]  which basically is, at this point, is basically anti-SQL compliant.
[4095.64 --> 4095.86]  Right.
[4095.86 --> 4102.52]  You literally write SQL to go ahead and access your OpenAI to run an LL model directly against your data.
[4102.86 --> 4104.92]  So, literally, party hardy.
[4105.12 --> 4105.46]  Have fun.
[4105.46 --> 4109.78]  So, it's not, our attitude isn't so much like don't use one versus the other.
[4109.78 --> 4112.70]  Our attitude is very much, no, no, just know what you're doing.
[4113.28 --> 4116.06]  Understand when you're using something like a service.
[4116.46 --> 4118.94]  Understand when it makes sense for you to build your own model.
[4118.94 --> 4124.32]  And we also make it easy for you to build, maintain, train, infer against that model.
[4124.60 --> 4124.94]  That's it.
[4125.60 --> 4127.94]  So, I mentioned we have our transcripts as open source, right?
[4128.02 --> 4128.42]  Yeah.
[4128.42 --> 4131.80]  Everything we're saying here, when it hits the podcast, it's going to be transcribed into words.
[4131.80 --> 4131.82]  Exactly.
[4132.42 --> 4138.40]  How are ways we can use Dolly 2.0, this open model that you're talking about, this direction,
[4138.94 --> 4143.60]  how can we leverage these transcripts for our personal betterment as a podcast company?
[4143.62 --> 4148.78]  For example, as a podcast company, one of the first things, in fact, I'm actually already doing this technically for Delta Lake, okay?
[4149.14 --> 4151.24]  Is that we also have podcasts ourselves, okay?
[4151.58 --> 4152.68]  So, what are we doing, though?
[4153.14 --> 4158.14]  I'm spending time and effort to generate blogs based off of the podcast.
[4158.56 --> 4158.88]  Why?
[4159.02 --> 4161.10]  Because it's better for Google SEO search, right?
[4161.76 --> 4164.32]  It's not like I'm trying to just repeat the same thing.
[4164.36 --> 4168.74]  I'm just trying to summarize because, you know, we talked about barbecue in the beginning, right?
[4168.74 --> 4169.52]  We talked about coffee.
[4169.52 --> 4174.74]  We probably don't need all of those details inside the transcript of the podcast of our blog.
[4175.14 --> 4178.54]  You want people to go ahead and actually understand what they're talking about when it comes to Dolly,
[4178.54 --> 4183.10]  cool, we generate a blog based off of this conversation.
[4183.36 --> 4185.64]  It can summarize it, get to the key points.
[4186.02 --> 4187.02]  Boom, there you go.
[4187.48 --> 4192.72]  It simplifies the whole process so that way you're not spending exorbitant hours trying to figure out
[4192.72 --> 4199.44]  how to basically synthesize the key points out of our conversation right now, right?
[4199.74 --> 4204.76]  So, it's still time for you to review and look to make sure the model isn't giving you garbage.
[4204.76 --> 4211.76]  It's still time for a producer or for any other person who is knowledgeable in this field to validate the statements.
[4211.86 --> 4214.06]  Maybe I'm full of, you know, BS of all I know, right?
[4214.30 --> 4216.10]  And then so you get next to it and he's like, oh, yeah, yeah.
[4216.36 --> 4216.82]  I don't know.
[4216.92 --> 4217.74]  Denny's full of it.
[4217.86 --> 4218.26]  Forget it.
[4218.50 --> 4221.46]  It'd most likely be the Conical versus Flatbird Grinder.
[4221.58 --> 4223.42]  But, again, you know, that's a whole other story.
[4223.48 --> 4224.42]  The whole summary will just be added.
[4224.42 --> 4226.32]  I'm on your team Conical is me.
[4227.16 --> 4227.82]  I'm Conical.
[4227.94 --> 4228.40]  Team Conical.
[4228.64 --> 4229.00]  There you go.
[4229.06 --> 4229.30]  Perfect.
[4229.42 --> 4229.50]  See?
[4229.86 --> 4234.12]  But the context is that we can go ahead and actually use these systems to simplify.
[4234.46 --> 4237.96]  Would it be cheaper and easier if we just went ahead and did like ChatGB to do it?
[4238.14 --> 4238.38]  Yeah.
[4238.90 --> 4239.40]  Go for it.
[4239.96 --> 4243.38]  Would it be worthwhile to do it in your own Dolly model?
[4243.52 --> 4243.86]  Absolutely.
[4244.02 --> 4247.50]  Because you have your own style, right?
[4247.70 --> 4247.84]  Yeah.
[4247.84 --> 4256.84]  So if you have your own style, if it's building, if Dolly or any other open source model, again, I want to be very clear here, is going ahead and be trained against your transcripts.
[4257.62 --> 4262.84]  It will then be able to start writing blogs based off of your style, right?
[4263.46 --> 4264.64]  That's the cool thing about it.
[4264.78 --> 4270.38]  Is it cool to actually chain like that or is it better to go to a foundational model and then just our stuff?
[4270.50 --> 4276.56]  Or it'd be cooler to be like, well, start with Dolly because it has instructions and then add our style and then maybe add something else.
[4276.56 --> 4278.70]  I'm telling you my answer is all of the above because we don't know.
[4278.70 --> 4279.36]  Just whatever you want.
[4279.40 --> 4279.54]  No, no.
[4279.54 --> 4279.86]  We don't know.
[4280.08 --> 4281.46]  We don't know because that's the whole point.
[4281.96 --> 4286.42]  Different foundational models will be better at different things.
[4286.92 --> 4287.54]  As simple as that.
[4287.84 --> 4290.16]  Some models will be better at, for example, conversations.
[4290.56 --> 4292.50]  Some models will be better for writing purposes.
[4296.90 --> 4297.78]  Nat.dev.
[4298.06 --> 4299.30]  I'm forgetting the guy's name.
[4299.46 --> 4299.88]  Nat Friedman.
[4300.04 --> 4300.42]  Nat Friedman.
[4300.42 --> 4300.48]  Thank you.
[4300.56 --> 4301.08]  Oh, my God.
[4301.12 --> 4302.74]  I don't believe I spaced out on that.
[4302.76 --> 4303.94]  He's a nobody.
[4304.34 --> 4304.50]  Yeah.
[4304.50 --> 4304.96]  We got you back.
[4304.98 --> 4305.90]  He's a small guy.
[4305.90 --> 4306.34]  Okay.
[4306.52 --> 4308.90]  So Nat Friedman, former CEO of GitHub.
[4309.06 --> 4309.12]  Okay.
[4309.44 --> 4310.42]  So slightly important guy.
[4311.16 --> 4316.82]  Nat.dev is an awesome playground, for example, where you can test out a lot of different models already.
[4317.18 --> 4320.20]  And you're literally just chucking like, hey, let me try with ChatGBT3.
[4320.34 --> 4321.38]  Let me try with Vacuna.
[4321.60 --> 4322.38]  Whatever else.
[4322.94 --> 4331.14]  And literally you will see with the same question, especially if we do the compare playground section, different answers from the different models.
[4331.30 --> 4331.42]  Yeah.
[4331.42 --> 4332.30]  So, yeah.
[4332.44 --> 4335.76]  Like, literally, you got to play a little bit to figure out which model makes sense for you.
[4335.84 --> 4335.98]  Yeah.
[4336.86 --> 4337.10]  So, yeah.
[4338.30 --> 4338.82]  Love it.
[4339.56 --> 4340.92]  Well, thanks for talking with us, Denny.
[4341.36 --> 4341.88]  Glad to.
[4341.92 --> 4342.16]  Always.
[4342.36 --> 4346.82]  Aside from your opinions on coffee and whatnot, you're pretty good.
[4346.84 --> 4347.36]  Pretty solid dude.
[4347.64 --> 4347.76]  Yeah.
[4349.22 --> 4350.36]  You know, those are fighting words.
[4350.36 --> 4351.08]  I just want to say that.
[4351.18 --> 4351.30]  Okay?
[4351.40 --> 4352.20]  Those are fighting words.
[4352.36 --> 4352.58]  Oh.
[4353.10 --> 4353.86]  Oh, that's good.
[4354.54 --> 4355.16]  All right.
[4355.50 --> 4356.60]  Gentlemen, thank you very much.
[4356.82 --> 4357.44]  Yes, thank you.
[4357.44 --> 4357.88]  All right.
[4357.88 --> 4358.42]  Let's go.
[4358.42 --> 4358.78]  Cool.
[4359.78 --> 4371.26]  Hey, friends.
[4371.38 --> 4379.94]  This episode is brought to you by CIQ, the founding sponsor and partner of Rocky Linux, Enterprise Linux, the open source community way.
[4379.94 --> 4387.10]  And I'm here with Gregory Kertzer, the founder and CEO of CIQ and the creator of Rocky Linux.
[4387.54 --> 4400.84]  So, Greg, I know that a lot of people are still sort of catching up to some degree with what went down with CentOS, the Red Hat acquisition, and just the massive shift that required everyone using CentOS to do.
[4400.92 --> 4404.26]  Give me a glimpse into what happened there.
[4404.26 --> 4411.06]  We've seen a number of cases in the open source community where projects were pivoted due to business agenda or commercial needs.
[4411.32 --> 4412.70]  We saw that happen with CentOS.
[4413.10 --> 4418.58]  CentOS was one of the primary, one of the biggest enterprise operating systems ever.
[4418.98 --> 4421.22]  People were using it all over the place.
[4421.42 --> 4426.72]  Enterprise organizations and professional IT teams were all leveraging CentOS.
[4426.72 --> 4437.06]  For CentOS to be stripped away from the community and removed as a suitable option to meet their needs created a massive pain point and a gap within the industry.
[4437.56 --> 4444.48]  As one of the founders of CentOS, I really took this to heart, and I wanted to ensure that this does not happen again.
[4444.86 --> 4449.20]  And that is what we created with Rocky Linux and the RESF.
[4449.34 --> 4449.84]  Okay.
[4449.90 --> 4451.64]  You mentioned the RESF.
[4451.74 --> 4455.32]  What is that, and what is its relationship to Rocky Linux?
[4455.32 --> 4470.08]  The RESF is the Rocky Enterprise Software Foundation, and it is an organization that we created to hold ourselves responsible to what it is that we've promised that we're going to do with the community.
[4470.08 --> 4471.60]  It is community-run.
[4471.92 --> 4472.96]  It is community-led.
[4472.96 --> 4482.32]  We have a board of directors, which is comprised of a number of people that have a huge amount of experience, both with Linux as well as open source and community.
[4482.32 --> 4493.04]  And from this organization, we solidify the governance of how we are to manage Rocky Linux and any other projects that come and join in this vision.
[4493.58 --> 4494.02]  Sounds good, Greg.
[4494.06 --> 4494.52]  I love it.
[4494.64 --> 4502.32]  So Enterprise Linux, the open source way, the community way, has a home at Rocky Linux and the RESF.
[4503.12 --> 4506.76]  Check it out and learn more at RockyLinux.org slash changelog.
[4506.76 --> 4510.74]  Again, RockyLinux.org slash changelog.
[4529.34 --> 4530.90]  All right, Stella Biederman.
[4531.44 --> 4531.72]  Yeah.
[4531.72 --> 4534.58]  And you're with, I'm going to also butcher the name of the org.
[4534.82 --> 4535.14]  Eleuther.
[4535.26 --> 4536.38]  Eleuther.
[4536.96 --> 4537.32]  Eleuther.
[4537.44 --> 4537.64]  Eleuther.
[4538.04 --> 4538.36]  Yes.
[4538.50 --> 4538.82]  Okay.
[4538.92 --> 4539.56]  What is this?
[4539.70 --> 4540.24]  What is Eleuther.
[4540.38 --> 4540.46]  Eleuther.
[4540.46 --> 4543.70]  Y'all were just talking with Databricks about Dolly.
[4543.88 --> 4544.42]  This is right.
[4544.62 --> 4545.04]  Yes, correct.
[4545.48 --> 4550.28]  So that was built on top of a open source language model.
[4550.50 --> 4550.78]  Okay.
[4550.88 --> 4551.16]  Yes.
[4551.60 --> 4552.16]  I trained that.
[4553.18 --> 4553.52]  Okay.
[4553.58 --> 4555.40]  So you're underneath Dolly.
[4555.70 --> 4555.98]  Yes.
[4556.22 --> 4556.54]  Okay.
[4556.84 --> 4558.22]  So you personally trained it.
[4558.32 --> 4558.54]  Yes.
[4558.98 --> 4559.30]  Okay.
[4559.80 --> 4560.68]  What's the model?
[4560.68 --> 4562.06]  It's called Pythia.
[4562.52 --> 4562.88]  Pythia.
[4563.20 --> 4568.62]  It's a suite of language models, actually, that we put out a couple of months ago.
[4568.84 --> 4569.04]  Okay.
[4569.34 --> 4573.56]  But in general, Eleuther.i has trained several of the largest open source language models
[4573.56 --> 4575.12]  in the world in the past three years.
[4575.72 --> 4576.12]  Okay.
[4576.68 --> 4577.56]  Very nice.
[4578.04 --> 4579.20]  So what do you want to tell the world then?
[4579.52 --> 4580.76]  What do I want to tell the world?
[4582.10 --> 4583.70]  Honestly, didn't think that far in advance.
[4583.90 --> 4584.22]  Okay.
[4585.74 --> 4586.38]  All right.
[4586.64 --> 4588.00]  Well, what should the world know?
[4588.36 --> 4589.38]  What should the world know?
[4589.38 --> 4593.38]  About what you do in terms of training models that Databricks uses, that's open source, etc.?
[4593.90 --> 4599.46]  Honestly, especially like the open source world, should really know that the AI world really
[4599.46 --> 4601.78]  needs help from the open source community writ large.
[4602.32 --> 4606.66]  That's actually, broadly speaking, why I'm here at the Linux Open Source Summit.
[4607.22 --> 4607.48]  Okay.
[4607.48 --> 4614.28]  You know, we're struggling with a lot of issues about maintainability, issues about licensing,
[4614.68 --> 4621.48]  issues about regulation, issues about building sustainable ecosystems that the open source
[4621.48 --> 4625.52]  community writ large has been working on for years, if not decades.
[4625.76 --> 4626.00]  Yeah.
[4626.00 --> 4631.08]  And a lot of people in the AI world are a little too proud to ask for help from non-AI people,
[4631.96 --> 4635.26]  which is definitely a real systemic problem.
[4635.26 --> 4642.80]  But there's, I think, a lot of, if people are excited about foundation models, large language models,
[4642.90 --> 4647.42]  whatever you want to call them, and want to get involved and don't know, or want to help
[4647.42 --> 4653.88]  and don't know that much about AI, there's a ton of open source work that needs to be done
[4653.88 --> 4659.32]  that we need help with to build a robust and enduring ecosystem.
[4660.10 --> 4661.56]  Where is the money coming from?
[4661.56 --> 4663.06]  Where is the money coming from?
[4663.14 --> 4663.82]  Great question.
[4664.14 --> 4668.46]  So, at Eleuther AI, we recently formed a non-profit.
[4670.18 --> 4678.82]  And we have donations from a number of companies, most prominently Google, Stability AI, and Hugging Face.
[4679.10 --> 4679.34]  Okay.
[4679.88 --> 4682.70]  And CoreWeave are among our biggest sponsors.
[4682.70 --> 4692.16]  We have also been applying for grants from mostly the U.S. government to pay for our, I guess, forthcoming research and work.
[4692.62 --> 4699.18]  In terms of, like, computing resources, it's actually, like, training these really large language models is not that expensive.
[4700.00 --> 4701.28]  Which is, like...
[4701.28 --> 4701.96]  Is that a secret?
[4702.78 --> 4706.66]  I don't know if it's a secret or what.
[4706.66 --> 4715.90]  But, like, I think that the CS world kind of got used to the idea that anything can be done on, like, a personal laptop.
[4716.44 --> 4722.16]  And that that's kind of what constitutes a reasonable amount of money to spend on a paper.
[4722.50 --> 4723.78]  And, like, that's great.
[4724.12 --> 4726.00]  There's a huge accessibility boon for doing that.
[4726.00 --> 4726.18]  Yeah.
[4726.18 --> 4728.66]  But training these large language models, it is pricey.
[4729.62 --> 4732.76]  You know, it's not something that anyone can do on their own.
[4733.32 --> 4735.36]  But it's not ruinously expensive.
[4735.72 --> 4741.08]  There are thousands of companies around the world that can afford to do this.
[4741.14 --> 4744.02]  There are dozens of universities that can afford to do this.
[4744.08 --> 4745.54]  And by and large, they just haven't been.
[4746.10 --> 4746.36]  Okay.
[4747.36 --> 4749.22]  So there's Pythia model that you trained.
[4749.62 --> 4749.82]  Yeah.
[4749.88 --> 4750.84]  How much did that cost?
[4750.84 --> 4753.32]  Uh, so we trained...
[4753.32 --> 4758.34]  So it's part of a suite of models that had, like, 28 in it total.
[4758.84 --> 4761.50]  But altogether, that was, like, less than $800,000.
[4762.02 --> 4767.12]  The largest model one training run would probably be, like, $200,000.
[4767.88 --> 4768.56]  Not bad.
[4768.66 --> 4769.10]  Which...
[4769.10 --> 4769.92]  That's more than a laptop.
[4770.08 --> 4771.06]  Which is more than a laptop.
[4771.20 --> 4771.72]  But it's less than...
[4771.72 --> 4774.36]  It's not, like, a mind-boggling amount of money.
[4774.62 --> 4775.78]  It's less than a Super Bowl commercial.
[4776.06 --> 4776.44]  It's true.
[4776.76 --> 4776.98]  Yeah.
[4776.98 --> 4777.02]  Yeah.
[4777.42 --> 4781.98]  So right now, the largest open source...
[4782.76 --> 4783.26]  Well, okay.
[4783.34 --> 4787.74]  The second largest open source English language model in the world is called GTP NeoX.
[4788.00 --> 4788.70]  We train that.
[4788.78 --> 4789.24]  I train that.
[4789.58 --> 4790.36]  My organization.
[4791.04 --> 4795.72]  And that cost us about $350,000.
[4796.02 --> 4798.30]  Or what if we weren't given the compute for free?
[4798.58 --> 4802.94]  But, like, $350,000 for the second largest open source language model in the world.
[4803.02 --> 4804.72]  And at the time we released it, it was the largest.
[4804.72 --> 4809.60]  Later, someone else trained a bigger model with sponsorship from the Russian government.
[4810.56 --> 4812.92]  But it's for...
[4812.92 --> 4816.16]  So, GTP3 came out in 2020.
[4816.86 --> 4822.98]  And for about two years, almost nobody was training in open sourcing language models.
[4822.98 --> 4829.50]  Google was doing it with similar models, but not, like, the same kinds of models that GTP3 is.
[4830.12 --> 4831.02]  And we were doing it.
[4831.46 --> 4833.22]  It was really not that expensive.
[4833.82 --> 4842.30]  We got into it on compute that we got for free through a Google research computing program called the TensorFlow Research Cloud.
[4842.30 --> 4851.72]  And, you know, with that, we trained a 6 billion perimeter language model, the one that underpins the first version of DALI that he was talking about.
[4851.98 --> 4859.06]  That's been extremely widely used, deployed in a whole bunch of different industry and research contexts, and been hugely successful.
[4859.52 --> 4862.00]  And it was literally just like Google gave us for free.
[4862.44 --> 4862.52]  Yeah.
[4862.52 --> 4865.18]  It ran preemptively on their research...
[4865.18 --> 4870.96]  Basically, the idea of TRC is that they have a research cluster that they don't always use all of.
[4871.52 --> 4882.64]  And so other researchers, independent researchers, academics, nonprofits, can apply to be able to run preemptible jobs on their research cluster and just use the compute that they're not using at the time.
[4882.64 --> 4887.18]  And using that, we trained this model in, like, two and a half months.
[4887.52 --> 4887.92]  Wow.
[4888.16 --> 4890.46]  And it was a really big deal when it came out.
[4890.50 --> 4895.14]  It was the largest model of its type in the world by a sizable margin.
[4895.22 --> 4897.44]  It was about three times the size of the four.
[4897.92 --> 4901.76]  Four times the size of the largest open source model of its type in the world.
[4902.44 --> 4902.84]  Yeah.
[4902.84 --> 4915.48]  And the Pythia models, we trained on, like, 120 A100 GPUs for a couple weeks, which is certainly a lot of computing resources, but it's not, like, mind-boggling amounts of compute.
[4915.60 --> 4919.02]  There are lots and lots and lots of companies that have that that could...
[4919.02 --> 4926.28]  You know, it's less about it actually being too expensive and more about kind of having the political will to actually go do it.
[4926.62 --> 4926.82]  Yeah.
[4927.04 --> 4929.68]  Are you focused on training open source models?
[4929.80 --> 4930.38]  Is that your focus?
[4930.38 --> 4934.68]  So our focus is on open source AI research in general.
[4935.16 --> 4945.66]  Our kind of area of expertise is large-scale AI, and most of what we do is language models, but we've also worked on training and releasing other kinds of large-scale AI models.
[4945.78 --> 4947.74]  So we are part of the OpenFold project.
[4948.90 --> 4956.18]  So DeepMind created an algorithm for modeling protein interactions called AlphaFold.
[4956.24 --> 4957.34]  That was a really big deal.
[4957.34 --> 4964.30]  And we helped some academics scale up their research and get that and replicate that and release it open source.
[4965.00 --> 4974.08]  We've done some stuff in the text-to-image space, both on our own, and some of our staff have kind of gone on and worked at Stability AI on some of their language...
[4974.08 --> 4975.22]  Sorry, image models.
[4975.22 --> 4979.48]  ...and we are a big proponent of open source research in general.
[4979.48 --> 4993.82]  So our kind of...the reason we decided to start training these large language models was back in the summer of, like, 2020, we thought, you know, this G2B3 thing is going to be a major player in the future of AI.
[4993.82 --> 5003.94]  And it's going to be really essential if you want to be...if you want to be doing something meaningful in AI, you probably want to know how these things work.
[5004.00 --> 5006.12]  You want to be able to experiment with them and want to have access to them.
[5006.40 --> 5009.54]  And back then, you couldn't even pay OpenAI to let you use the model.
[5009.92 --> 5010.00]  Yeah.
[5010.10 --> 5011.56]  They announced that they had it, and that was it.
[5011.56 --> 5015.22]  And so we said, well, what the...let's try to train a model like that.
[5015.30 --> 5016.78]  We'll learn something along the way.
[5017.18 --> 5021.98]  And so we started building, like, an open source infrastructure for training large language models.
[5022.20 --> 5028.14]  We created a data set called the Pile, which is now kind of the de facto standard for training large language models.
[5028.50 --> 5040.34]  We created a evaluation suite for consistently evaluating language models, because everyone runs their evaluations a little differently, and there's huge reproducibility issues.
[5040.34 --> 5050.02]  So we built a framework that we could release open source and run on our own models, run on other people's models, and actually have kind of meaningful apples-to-apples comparisons.
[5050.68 --> 5052.28]  And we started training large language models.
[5052.38 --> 5058.72]  We trained a 2.7 billion parameter model, which was, like, a little bit bigger than G2B2 was at the time.
[5059.02 --> 5060.62]  And then we started training larger models.
[5060.74 --> 5066.06]  6 billion parameters was the largest open source G2B3 style language model in the world.
[5066.06 --> 5072.84]  20 billion parameters was the largest language model of any sort to be released open source in the world.
[5073.54 --> 5079.52]  You know, since then, there's been a lot more investment and willingness to train and release models.
[5079.66 --> 5081.40]  There's several companies that are now doing it.
[5081.96 --> 5087.36]  So Mosaic is a company that released a 9, I want to say, something.
[5087.70 --> 5088.60]  A large language model.
[5088.60 --> 5092.38]  That seems really excellent, like last week.
[5093.04 --> 5097.40]  There is Meta, which has been training and releasing sort of models.
[5097.92 --> 5102.54]  They'll tell you that they're open source releasing models, but that's just not actually correct.
[5103.36 --> 5108.76]  They're under non-commercial licenses, and they're not open source, despite their rhetoric to the contrary.
[5109.48 --> 5111.20]  But there's a whole bunch of companies.
[5111.44 --> 5113.42]  Stability AI is training large language models.
[5113.54 --> 5117.30]  So now there's a lot more people in this space and doing it and releasing it.
[5117.30 --> 5122.24]  And honestly, from my point of view, we got into training large language models mostly because we wanted to study them.
[5122.32 --> 5127.44]  We wanted to enable people to do essential research on interpretability, ethics, alignment,
[5127.60 --> 5130.66]  understanding how these models work, why these models work, and what they're doing,
[5131.02 --> 5137.92]  so that we can design better models and so that we can know what appropriate and inappropriate deployment contexts for them are.
[5138.68 --> 5143.42]  And so now that there's a lot more people working in kind of this open source training space,
[5143.42 --> 5148.66]  we're moving more towards doing that kind of scientific research that we've always wanted to do.
[5149.26 --> 5155.06]  So in the past six months, we've been doing a lot of work in interpreting language models
[5155.06 --> 5158.28]  and kind of understanding why they behave the way they do.
[5158.68 --> 5164.90]  My personal kind of area of focus is tracing the behavior of language models back to their actual training data.
[5164.90 --> 5170.62]  So the models that the DALI-2 is trained on, the Pythia suite, what kind of makes that special
[5170.62 --> 5175.94]  is that most language model suites are very ad hoc constructed.
[5176.60 --> 5180.20]  I'm calling them suites because you have several models that are similar of different sizes.
[5180.70 --> 5180.82]  Right.
[5180.98 --> 5188.24]  So like the OPT suite by Meta, for example, ranges from 125 million parameters to 175 billion parameters.
[5188.76 --> 5191.92]  But they're not actually very consistent between them.
[5191.92 --> 5194.50]  Some of them even have different architectures.
[5194.62 --> 5195.56]  They have different data order.
[5196.10 --> 5200.58]  There's a lot of stuff that kind of limits your ability to understand,
[5201.24 --> 5203.12]  to do controlled experiments on these models.
[5203.30 --> 5208.40]  And so we sat down and we said, if we wanted to design from the ground up a suite of large language models
[5208.40 --> 5211.62]  that was designed to enable scientific research, what would it look like?
[5211.92 --> 5213.62]  What kinds of properties would it have?
[5213.82 --> 5217.14]  What kinds of experiments do we think people are going to want to do that we're going to need to enable?
[5217.14 --> 5222.92]  And we built this list of requirements and then created a model suite that satisfies that.
[5223.28 --> 5225.46]  So it was trained on entirely publicly available data.
[5226.10 --> 5228.18]  All of the training, it was trained on the same data.
[5228.38 --> 5230.64]  Every model in the suite was trained on the same data in the same order.
[5231.26 --> 5233.64]  And we have a whole lot of intermediate checkpoints that are safe.
[5233.70 --> 5239.54]  So if you want to know, you know, after 10 billion tokens, how each model in the suite is performing,
[5239.68 --> 5242.36]  you can go and grab those checkpoints after 10 billion tokens.
[5242.36 --> 5247.08]  And then you can say, okay, what's the next data point it saw during training after 10 billion tokens?
[5247.16 --> 5248.84]  What was the 10 billion first token?
[5248.94 --> 5254.40]  And you can actually use some stuff we've uploaded to the internet to actually load that data
[5254.40 --> 5256.02]  in the same order it's seen by the models.
[5256.10 --> 5260.68]  You can study kind of how being exposed to particular training data influences model behavior.
[5261.14 --> 5264.76]  So we've been using this right now primarily to study memorization,
[5265.06 --> 5270.44]  understanding because language models have a pre-pensity for reproducing long exact sequences
[5270.44 --> 5271.82]  from their training corpus.
[5272.36 --> 5275.72]  And we're interested in understanding what causes memorization,
[5276.28 --> 5279.00]  why certain strings get memorized and others don't.
[5279.20 --> 5282.20]  Right now I'm wrapping up our kind of first paper on that.
[5282.26 --> 5285.16]  We have some more research in the works, trying to understand, you know,
[5285.46 --> 5288.40]  looking at the actual models throughout the course of training
[5288.40 --> 5290.58]  and looking at kind of the training data points that they see
[5290.58 --> 5295.98]  and trying to reverse engineer what that actual interaction between the model and the data is.
[5296.74 --> 5299.06]  And yeah, this is something I'm personally really high on.
[5299.06 --> 5306.20]  Most interpretability research right now is kind of focused on final trained models as like pre-existing artifacts.
[5306.20 --> 5310.40]  So you have this trained model and you want to understand what behaviors it has.
[5310.40 --> 5317.72]  But, you know, my perspective as someone who trains these models is much more focused on kind of where they come from.
[5318.04 --> 5321.58]  And what especially like my overarching goal is to kind of, you know,
[5321.68 --> 5327.06]  if I as a person who trains a large language model have a particular desire for a property the model has,
[5327.12 --> 5328.42]  a property the model doesn't have,
[5328.42 --> 5333.50]  what decisions can I make to actually influence that and to make the model have the properties I want it to have.
[5333.54 --> 5335.10]  So if there's data, I don't want it to memorize.
[5335.56 --> 5338.56]  Is there a way that I can know ahead of time what's going to be memorized?
[5338.64 --> 5345.46]  That's the paper that we have that we actually just released on archive about forecasting what is going to be memorized before you actually train the model.
[5345.88 --> 5349.42]  Is that to make it less black box, more like you deploy it and you don't know what it can do?
[5349.42 --> 5358.02]  So that you can sort of understand, okay, here's the data, here's how it's trained to sort of have a more clarity of what the box actually contains versus this black box.
[5358.18 --> 5359.12]  Is that why that's important?
[5359.22 --> 5361.42]  That is what the field of interpretability is about in general.
[5361.58 --> 5372.10]  And I would say kind of building on that, that what my research is about in particular is not just opening up that black box and looking inside and understanding what the model is actually doing,
[5372.42 --> 5378.18]  but understanding where it came from and how we can build boxes that are more transparent from the ground up.
[5378.50 --> 5379.36]  Predictable maybe even?
[5379.56 --> 5379.70]  Yeah.
[5380.02 --> 5380.24]  Yeah?
[5380.66 --> 5385.10]  Because, I mean, that's one of the fears is, you know, especially with like Bing.
[5385.54 --> 5385.76]  Yeah.
[5385.76 --> 5388.42]  When they put that out there, I think what, it threatened the person?
[5388.54 --> 5391.56]  Like there was some sort of like threat on humanity essentially.
[5391.84 --> 5396.72]  And it's like you deploy this thing out into the world and you don't understand what they can actually do.
[5396.82 --> 5400.50]  Is that to be more predictable, more controlled to some degree?
[5400.50 --> 5400.58]  Absolutely.
[5401.58 --> 5401.74]  Sorry?
[5402.10 --> 5403.26]  And even designable.
[5403.46 --> 5405.58]  Like say, well, forget these things, remember these things.
[5405.76 --> 5405.96]  Yeah.
[5407.40 --> 5409.08]  Designability is a really big component.
[5409.08 --> 5411.14]  I think that's going to become huge in the future.
[5411.50 --> 5411.58]  Right.
[5411.58 --> 5414.90]  And really it hasn't been studied primarily because people haven't had the tools.
[5415.58 --> 5418.46]  Very few model suites have intermediate checkpoints at all.
[5419.26 --> 5423.38]  A lot of publicly released models weren't trained on publicly released data sets.
[5423.38 --> 5428.52]  Or if they were trained on publicly released data sets, they didn't tell you what order it was trained on.
[5428.90 --> 5430.32]  And it turns out that matters a lot.
[5431.12 --> 5433.04]  What it saw early in training, what it saw late in training.
[5433.46 --> 5445.74]  And so there's really a huge reproducibility issue in terms of under, like if you want to dig in and really understand how data by data, data point by data point, the model is learning to behave.
[5445.74 --> 5448.26]  You need to be able to basically fully reproduce the training.
[5448.50 --> 5451.74]  Not actually, because you're not going to spend a couple hundred thousand dollars.
[5452.24 --> 5457.50]  But at least in principle, you need to be able to inspect individual data points, know when it's going to get loaded, understand kind of how it works.
[5457.50 --> 5464.02]  And this is something that we've put a huge amount of resources into, both on the training side as well as kind of on the engineering side.
[5464.12 --> 5469.32]  It was not easy, but you can actually reproduce our model training exactly.
[5469.60 --> 5482.88]  So if you take the code base that we used to train these Pythia models and you pick a checkpoint and you load that checkpoint and you resume training from that checkpoint, you will end up with the same fully trained model that we did.
[5483.22 --> 5483.62]  Exactly.
[5484.16 --> 5484.80]  That's important.
[5485.10 --> 5485.82]  That is really important.
[5485.82 --> 5492.08]  It's important because if you want to understand how to design models, you need to understand how they're changing over the course of training.
[5492.60 --> 5499.62]  And that is really persnickety and really sensitive to a lot of implementation specific details that tend to not get released.
[5500.26 --> 5508.72]  How far in the future do you think, since you're at the training level, you're like the ground level of if this is the eureka moment for humanity.
[5509.00 --> 5509.18]  Yeah.
[5509.26 --> 5509.44]  Right.
[5509.74 --> 5514.70]  How far in the future do you think and do you have fear, trepidation, hope?
[5514.70 --> 5516.94]  Like where will this take us as humanity?
[5517.40 --> 5518.36]  I really don't know.
[5519.06 --> 5529.78]  My kind of attitude is that the recent, like there was a really big paradigm shift in 2020 with the release of G2B3 and the aggressive focus on scaling.
[5529.78 --> 5537.00]  And people really changed their attitudes towards like how to design language models and kind of how they can be used and what they can be used for.
[5537.28 --> 5539.78]  In a sense, we got really lucky because it wasn't that dangerous.
[5540.18 --> 5543.48]  You know, there were a lot of fears about what G2B3 could do.
[5543.48 --> 5547.16]  And by and large, it turned out to be pretty safe.
[5547.60 --> 5551.66]  There wasn't all that much harm done and a lot of the fears turned out to be not come to fruition.
[5552.40 --> 5559.38]  And, you know, kind of looking forward, I think the really important thing to think about is we obviously can't predict the next paradigm shift.
[5559.38 --> 5569.44]  But building tools that allow us to hopefully more readily adopt and adapt and respond to future paradigm shifts in large scale AI.
[5570.06 --> 5574.48]  So that, you know, one day there probably will be something that gets developed that is dangerous.
[5574.66 --> 5577.16]  And we want to be able to be, I guess, ready for that.
[5577.56 --> 5577.64]  Yeah.
[5577.96 --> 5578.12]  Yeah.
[5578.68 --> 5578.94]  Cool.
[5579.02 --> 5580.24]  Well, what are some touch points?
[5580.46 --> 5586.02]  People who are interested in what you're up to, want to help out, want to give money, want to read more?
[5586.20 --> 5587.20]  Where can people connect with you?
[5587.20 --> 5590.36]  So the best place to connect with us is our Discord server.
[5590.88 --> 5596.60]  We are a research institute, but we actually operate basically entirely in the public view.
[5597.06 --> 5602.70]  We're distributed all over the world and we do our research in a public Discord.
[5602.92 --> 5608.44]  And anyone can join, anyone can drop in, read about what we're getting up to, hang out with us, chat with us about AI.
[5608.84 --> 5612.54]  So our Discord server is discord.gg slash EleutherAI.
[5613.10 --> 5616.08]  There's also a link on our website, which is Eleuther.AI.
[5616.08 --> 5616.48]  Nice.
[5616.48 --> 5616.88]  Shockingly.
[5618.06 --> 5619.60]  We'll link it up to the show notes for sure.
[5619.98 --> 5620.12]  Yeah.
[5620.90 --> 5624.10]  And yeah, we're always happy to take on more volunteers.
[5624.86 --> 5628.82]  We have a small professional staff and a large number of volunteers that help out as well.
[5628.94 --> 5629.70]  How small is small?
[5631.42 --> 5632.68]  Like 10 full-time employees.
[5632.88 --> 5633.06]  Okay.
[5633.06 --> 5635.94]  And if they go to the Discord server, what can they do there?
[5636.00 --> 5637.42]  What can they expect from the Discord server?
[5637.62 --> 5639.18]  Like you're there, others are there.
[5639.54 --> 5639.76]  Yeah.
[5639.84 --> 5641.86]  So you can chat about AI.
[5642.10 --> 5646.84]  We have a bunch of discussion channels where people talk about kind of cutting edge trends in artificial intelligence.
[5646.84 --> 5655.12]  Honestly, like I don't really follow AI publication news anymore because I just follow my Discord server and everything that's important shows up for me.
[5655.14 --> 5655.46]  There you go.
[5655.72 --> 5657.32]  Which is a really nice place to be.
[5657.66 --> 5658.64]  But you can talk with us.
[5658.66 --> 5659.60]  You can talk with other researchers.
[5659.76 --> 5663.18]  We have a large amount of researchers at the cutting edge of AI.
[5663.18 --> 5667.08]  I can't count the number of times that someone's posted a paper and been like, hey, this is really cool.
[5667.58 --> 5669.02]  Like, does anyone know anything about this?
[5669.04 --> 5671.00]  And someone just like tags the guy who wrote the paper.
[5671.28 --> 5672.12]  That happens all the time.
[5672.22 --> 5684.98]  We have people from OpenAI, Anthropic, Meta, like all the major labs who come, DeepMind, come in and chat about language models, give advice, give perspectives on research and talk about kind of how things are going.
[5685.62 --> 5689.16]  You can also get involved with ongoing research projects.
[5689.16 --> 5698.78]  So we have a dozen-ish ongoing research projects ranging from learning to train, figuring out how to train better language models to training language models in other languages.
[5699.34 --> 5704.80]  So if you look at like the list of the hundred largest language models in the world, basically all of them are English or Chinese.
[5705.46 --> 5705.54]  Yeah.
[5706.24 --> 5718.34]  And, you know, so if you want to spread the benefits of this technology and the ability to kind of use and understand this technology to the world writ large, like not everyone speaks English and Chinese.
[5718.34 --> 5721.80]  And even the people who do often also speak other languages that they care about.
[5722.42 --> 5726.94]  So we're training, we've trained and released several Korean language models.
[5727.56 --> 5735.62]  We're currently training with the plan of releasing some Indic language models as well as some Romance language models.
[5736.10 --> 5739.32]  So, yeah, on the developing new model side, we do research like that.
[5739.32 --> 5749.52]  On the interpretability side, we do a lot of different stuff, understanding training dynamics, understanding how to evaluate language models, understanding how to kind of extract the best information from them.
[5750.04 --> 5761.52]  We recently started up some work on kind of red teaming them and trying to understand, you know, there's a lot of stuff out there right now about prompt hacking, about how people are trying to put filters on language models and they're kind of not really very successful.
[5761.52 --> 5770.60]  And trying to understand, like, what the dynamics of that is like, whether you can build meaningful safeguards around these things or whether it's always going to be subverted.
[5770.86 --> 5772.26]  We do a lot of work like that as well.
[5772.94 --> 5773.32]  Very cool.
[5773.96 --> 5775.40]  Well, thanks for coming on the show, Stella.
[5775.62 --> 5776.68]  Yeah, it's a pleasure.
[5777.12 --> 5778.98]  It was awesome having this deep dive with you.
[5779.00 --> 5779.42]  I love that.
[5779.52 --> 5779.90]  Thank you.
[5780.18 --> 5780.84]  Great to meet you guys.
[5780.84 --> 5808.42]  Yeah, so if you'd have told me a few years ago that I'd be going to an open source summit and talking about AI in open source at this level from Cody, a coding assistant to Databricks and training models on small data sets to Stella's work and the Luther AI's work on open AI research and all these things.
[5808.42 --> 5816.74]  That it'd be real, that it'd be touchable, that it'd be usable today to transform my work, to transform your work, to transform the world around me.
[5817.12 --> 5819.64]  I would not have believed it, but it's true.
[5819.94 --> 5821.88]  We're here and this show was awesome.
[5822.02 --> 5823.14]  So hope you enjoyed it.
[5823.44 --> 5831.66]  Once again, a big thank you to our friends at GitHub for sponsoring us to go to this conference as part of Maintainer Month.
[5832.22 --> 5836.32]  There is a small bonus for our plus plus subscribers.
[5836.78 --> 5838.24]  So stick around for that.
[5838.24 --> 5840.60]  If you're not a plus plus subscriber, it's too easy.
[5841.10 --> 5843.34]  Changelog.com slash plus plus.
[5843.54 --> 5844.74]  We drop the ads.
[5844.92 --> 5847.00]  We obviously give you bonus content.
[5847.34 --> 5849.38]  We bring you a little closer to the metal.
[5849.56 --> 5852.10]  And the best part, you directly support us.
[5852.50 --> 5854.74]  Ten bucks a month, a hundred bucks a year.
[5855.26 --> 5857.50]  Changelog.com slash plus plus.
[5858.14 --> 5858.62]  That's it.
[5858.68 --> 5859.32]  This show's done.
[5859.54 --> 5860.42]  Thanks for tuning in.
[5860.42 --> 5862.48]  We will see you on Friday.
[5868.24 --> 5898.22]  We'll see you on Friday.
