[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.02 → 36.08] Learn more at fly.io.
[42.44 → 46.26] Welcome to another episode of Practical AI.
[46.64 → 48.26] This is Daniel Whiten ack.
[48.40 → 51.68] I'm a data scientist and founder of Prediction Guard.
[51.68 → 57.72] And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[57.72 → 57.98] Martin.
[58.16 → 58.88] How are you doing, Chris?
[59.50 → 60.80] Doing well today, Daniel.
[61.02 → 66.10] It just continues to be super interested in this space, in the world of AI.
[66.40 → 67.46] So much change.
[68.02 → 69.46] This has been a year.
[69.94 → 75.36] I think it's a year that's for the history books in terms of the advances and the fact
[75.36 → 81.86] that AI is really making deep impact into the general population, people who normally might
[81.86 → 84.66] not be listening to our podcast as hard as it is to believe that.
[85.18 → 90.24] Yeah, I was just going to say people like in companies like my wife's company, which is
[90.24 → 95.68] not a large company, it's not a tech company, but they're having conversations about how do
[95.68 → 103.14] we as a company leverage AI or leverage large language models in our content generation or
[103.14 → 104.48] what have you?
[104.84 → 108.62] And it's really permeated all industries at this point, I think.
[108.68 → 114.58] And people are wrestling with the idea of what do we do, not just, you know, if we do something
[114.58 → 116.06] in relation to AI.
[116.74 → 117.02] Agreed.
[117.12 → 119.44] I think that's a huge issue right now.
[119.44 → 128.06] It is potentially more confusing about how to handle everything that's coming at companies
[128.06 → 133.26] these days from a large language model and generative AI than it ever has been.
[133.62 → 135.66] And the problem is getting harder.
[136.34 → 139.88] And so we want to talk a little bit about that today.
[140.04 → 143.26] And I want to acknowledge a couple of things with our audience.
[143.62 → 146.36] Many of you have been with us for quite a long time.
[146.36 → 150.14] We've been doing this show for about five years on a weekly basis.
[150.32 → 151.40] I know it's been forever.
[152.02 → 154.04] And it's just getting more and more interesting.
[154.62 → 158.82] Over that course of time, something I wanted to share with our audience is I've gotten to
[158.82 → 159.88] know Daniel pretty well.
[159.98 → 162.24] And we didn't know each other super well beforehand.
[162.50 → 167.70] We had met in the Go software development community as kind of the two people looking at
[167.70 → 168.46] data concerns.
[169.02 → 176.06] But Daniel over time has demonstrated not only the fact that he is repeatedly an incredibly
[176.06 → 181.82] smart man with a lot of capability, but he's also an incredibly good human being.
[182.16 → 186.12] And for anyone who's followed the show for a long time, they know that the idea of just
[186.12 → 191.40] being a good person and AI for good and such things are a huge repeating topic in the show.
[191.52 → 198.02] And I've also learned to trust where he's going and to understand that if Daniel is doing or
[198.02 → 201.00] interested in something, it's something that I want to know about.
[201.00 → 207.50] And so today we want to hit this large language model kind of in the world and how you manage
[207.50 → 207.90] that.
[208.22 → 212.38] But I also want to acknowledge that we're going to have bits of the show that could be considered
[212.38 → 213.40] conflict of interest.
[213.74 → 217.18] And the reason I say that is we're going to talk about some work Daniel has been doing.
[217.70 → 221.94] And so if that bothers anybody, this is the point where you might want to shut off this
[221.94 → 222.86] particular episode.
[223.26 → 227.80] But I'm hoping that most of you trust us and have been with us for long enough to know that
[227.80 → 230.06] I'm not going to take you down a path that you wouldn't want to go.
[230.48 → 237.18] And I've asked Daniel to talk not only about the space of large language models being brought
[237.18 → 241.04] into production and trying to juggle all the things coming out, but talk about the work
[241.04 → 241.64] he's doing.
[242.24 → 244.70] And so we are unabashedly going to go that direction.
[244.84 → 250.94] And if anyone has hate mail to send, please send it to me because I have demanded that Daniel
[250.94 → 251.96] talk about this.
[252.78 → 255.88] And, so thank you for bearing with us on that.
[255.88 → 260.86] And so Daniel, if you're kind of both the co-host today and the guest, if you will.
[261.42 → 268.26] And if you might lay out a little bit of the landscape for us about what this looks like
[268.26 → 273.00] as an insider or someone who spends all your time focusing on this problem, that might be
[273.00 → 273.76] a good way to start.
[274.24 → 275.08] Yeah, thanks, Chris.
[275.12 → 276.88] And thanks for the kind words.
[277.32 → 283.24] I've over time learned so much from doing this show, and it's shaped a lot of what I think
[283.24 → 283.56] about.
[283.56 → 289.50] And certainly the things that I've been thinking about really since, well, this whole year,
[289.62 → 295.54] since kind of Christmastime, have been focused around these ideas of controlling large language
[295.54 → 300.30] models, guiding them, guarding them, making compliant AI systems.
[300.30 → 305.52] And a lot of that's led into the thing that I'm building right now, which is called prediction
[305.52 → 305.86] guard.
[305.94 → 308.46] So that's what you're referring to in terms of what I'm building.
[308.46 → 314.02] So I'm coming at it from that perspective and been thinking about this a lot, been talking
[314.02 → 319.38] about this a lot publicly and excited to do things like, you know, upcoming.
[319.64 → 325.50] There's an LLMs in production event put on by our friends at the ML Ops community.
[325.72 → 326.60] That's really cool.
[326.68 → 330.00] I'm giving a talk there and controlled and compliant AI applications.
[330.00 → 333.64] So that's part of what I'll share here today as well.
[333.64 → 339.90] One question maybe that I have for you as we start out here, Chris, is what have you experienced
[339.90 → 345.72] in terms of the people that you're talking to with regard to the pressure that they're
[345.72 → 351.56] feeling either internal to their own company or from like market pressures, like jump into
[351.56 → 357.18] the AI waters, like implement something, make AI part of our stack.
[357.30 → 358.42] Like what are you seeing there?
[358.42 → 362.76] So I don't think you'll be surprised when I say this, and we've alluded to this on some
[362.76 → 368.56] previous episodes, but it is a difficult business concern to navigate.
[369.26 → 375.26] I know all of us who straddle into the AI technical realm are incredibly excited.
[375.40 → 378.86] We're trying to figure out how to do the models and put them out there and everything like that.
[379.02 → 384.86] But if you are not in our shoes, if you're walking on a slightly different path, and let's say
[384.86 → 392.30] you work for a legal department or a compliance department or other business concerns, and
[392.30 → 400.10] suddenly these technologies are coming at you hard and fast week by week in 2023, and you're
[400.10 → 405.68] trying to navigate that and look at things like licensing on how the data that goes into
[405.68 → 406.62] models is used.
[407.04 → 409.06] And you're looking at compliance concerns.
[409.06 → 413.92] And you're looking at protecting your intellectual property.
[414.46 → 420.52] There's a whole host of challenging business problems with essentially no guidance.
[420.72 → 424.76] This is a brave new world that has to be pioneered through.
[425.04 → 431.68] And so I have talked to a lot of business people in various roles, including attorneys, and this
[431.68 → 433.64] stuff is scary stuff.
[433.76 → 435.18] It is problematic stuff.
[435.18 → 437.12] It is challenging to navigate.
[437.96 → 444.14] And I definitely want to take you down the path today of talking about the space and prediction
[444.14 → 451.76] guard relative to how you actually get these models out there productively in a business
[451.76 → 456.82] environment so that people can take advantage of the technology and understand what the pitfalls
[456.82 → 457.70] are and such.
[457.96 → 460.64] So that's the big thing that I've been hearing.
[460.74 → 462.12] I've been getting an earful of it lately.
[462.12 → 463.28] Like, Chris, settle down.
[463.48 → 465.88] Stop taking us down this AI thing.
[465.96 → 467.40] We've got to figure some things out first.
[467.48 → 469.26] So I'm coming to you for answers, man.
[469.92 → 476.42] Yeah, it's so tempting, actually, to have really easy-to-use systems.
[476.60 → 478.84] Like, let's say, the OpenAI API, right?
[479.48 → 486.24] I can go to the playground, or I can go to ChatGPT, or I can go wherever, put in my prompt,
[486.36 → 489.00] and get some magical output, right?
[489.00 → 496.26] It's magical, and immediately it triggers in your mind, I can solve real business problems,
[496.26 → 501.12] and I can create, like, actual solutions with this type of technology.
[501.32 → 503.16] Like, it's so quick to make that connection.
[503.76 → 509.64] But what I've seen, both in sort of advising and consulting and conversations that I've been
[509.64 → 518.82] having is on maybe, like, a less stringent case, like, people are struggling to make that
[518.82 → 523.70] connection to how they can build robust systems out of these technologies.
[523.70 → 528.06] So it's one thing to get text output and look at it with your eyes as a human, right?
[528.42 → 534.00] And say, like, extract this piece of data, or give me a summary of this, or something like
[534.00 → 540.26] that, but as soon as you make that programmatic, right, and automated, then how do you know
[540.26 → 541.80] you're getting the right output?
[542.06 → 547.10] And if you actually want to do something with that, like you're outputting a number, you know,
[547.16 → 553.42] a vomit of text blob out of a large language model doesn't really actually do you that much
[553.42 → 558.22] good if you're trying to implement, like, a robust system that's making actual business
[558.22 → 560.98] decisions on top of the output of large language models.
[561.24 → 568.76] On the harder side of this, I'm getting feedback from people that either I know or I'm advising
[568.76 → 576.12] or other things that companies are actually telling them, no, there's a full stop on using,
[576.12 → 582.44] quote, GPT models in this organization because of one of a few different reasons.
[582.44 → 587.72] Maybe that's a risk thing around, hey, we're going to hallucinate some name.
[588.22 → 593.70] Out of this or something that this person doesn't exist, and that's going to get us in trouble.
[594.04 → 596.88] People are going to start trusting our product and that sort of thing.
[596.96 → 600.36] So there's the hallucination or consistency of output sort of thing.
[601.08 → 607.34] There's also, as you mentioned, the IP or PII type of leakage scenario.
[607.34 → 612.30] So it is actually a problem for people to sit in a company.
[612.60 → 617.48] I'm sure this would be true whether you're at, you know, your company or a variety of other
[617.48 → 621.20] companies that I've talked to where I'm sitting there, and I'm like, oh, I could solve this
[621.20 → 622.82] problem with ChatGPT.
[623.04 → 630.00] Let me copy and paste this user data into ChatGPT and like have it summarize something or
[630.00 → 632.12] extract something or whatever it might be.
[632.72 → 639.02] It's sort of unclear and murky waters like how that data is actually going to be used by
[639.02 → 648.14] OpenAI, and you're kind of leaking IP or company information, PII to external systems, right?
[648.24 → 650.16] Which is a big, big no-no.
[650.56 → 656.34] Regardless of how that's used in the end, this data, it seems like is going to exist
[656.34 → 658.18] outside your own systems.
[658.86 → 664.92] And so on the harder side of this problem, people are being told like, no, you have a full stop.
[665.08 → 666.16] Can't use GPT.
[666.32 → 667.66] Can't use large language models.
[667.66 → 673.18] So to summarize how I would kind of think about this problem space, people are feeling
[673.18 → 678.64] the pressure that they need to or really want to implement these systems either because
[678.64 → 682.90] they feel like they're getting left behind or there's an actual market pressure for them
[682.90 → 683.72] to do something.
[684.42 → 688.66] But in practice, they don't know how to deal with the outputs of large language models.
[688.98 → 694.56] And they might not even be able to connect to the kind of most common large language models
[694.56 → 699.32] because of this privacy, security, leaked IP type of issues.
[699.98 → 701.76] I think that's really, really widespread.
[702.56 → 707.16] It's funny, you've kind of enumerated a whole set of risks associated with that.
[707.40 → 713.22] Yesterday, just as a thing, you know, I have a particular employer and thinking about public
[713.22 → 718.40] information, you know, well-known public information about the lines of business that we have that
[718.40 → 721.56] is publicly acknowledged in multiple sources out there.
[721.72 → 723.46] I went to ChatGPT.
[723.72 → 726.40] I should have done the 4.0 model, but I forgot.
[726.66 → 728.64] And I just let it default to the 3.5.
[729.02 → 733.98] And I simply asked for our 19 lines of business, which is incredibly public knowledge.
[734.08 → 735.08] And it got it wrong.
[735.36 → 736.62] It got it wrong the first time.
[736.62 → 739.98] And so I tried to steer it a little bit, and it got it wrong the second time.
[740.60 → 748.40] And had I not known better about the intellectual property concerns with licensing, had I tried
[748.40 → 751.04] to put something in that might have been out there in the public.
[751.12 → 755.14] So I run into what you just said all the time.
[755.14 → 756.20] And there are so many risks.
[756.38 → 761.90] And yet, there's so much value to extract from the space.
[761.90 → 768.76] And so I think putting your finger on the fact that if you can find a way to mitigate these
[768.76 → 776.40] risks in various ways, that will unlock a huge amount of value for a lot of organizations
[776.40 → 778.04] and users to do that.
[778.16 → 782.14] But it certainly, from my standpoint, feels like the Wild West right now.
[782.70 → 785.14] Yeah, I would say that that's true.
[785.14 → 791.42] And yet, there are these concerns, like the money that people are able to save operating
[791.42 → 794.12] costs with AI in your business are significant.
[794.54 → 803.44] So I saw the study from Accenture estimating insurance companies saving $1.5 million per
[803.44 → 805.26] 100 full-time employees.
[805.50 → 813.14] So if your insurance company A, and you're not trying to implement AI systems in your business,
[813.14 → 818.30] then you're actually introducing a liability, right?
[818.36 → 821.94] Because insurance company B might be doing that.
[822.16 → 827.48] And they're going to slash their prices and undercut you and put you out of business, right?
[827.48 → 836.46] So even regardless of new features that might be implemented in people's products and that
[836.46 → 843.06] sort of thing, there's this real liability around not considering AI solutions as part of
[843.06 → 844.14] your business strategy.
[844.68 → 845.92] I think that's a huge point.
[846.00 → 849.06] And that's the other side of the coin that I was just talking about.
[849.16 → 854.02] There was the risk of using, and there is the potentially larger risk of not using at
[854.02 → 854.34] all.
[854.72 → 864.88] So we're seeing that in all markets in terms of the need to stay on top of what is gradually
[864.88 → 869.82] evolving over these past months and to be able to use that to promote your business.
[869.82 → 872.56] And if you don't do that, the risk is substantial.
[872.56 → 879.82] So the idea of navigating the licensing and the compliance concerns and being able to productively
[879.82 → 885.84] use these outputs is really crucial to being successful in almost any industry going forward.
[885.98 → 890.48] So definitely looking forward to finding out how we might do that.
[890.48 → 898.96] I'm Jared, and this is a changelog news break.
[899.30 → 906.60] In what appears to be a particular security unaware move, Google has added eight new top
[906.60 → 912.26] level domains, two of which are quite concerning, .zip and .mov.
[912.86 → 913.28] Yikes.
[914.48 → 916.20] Ars Technica writes, quote,
[916.20 → 922.40] While Google marketers say the aim is to designate tying things together or moving really fast
[922.40 → 929.60] and moving pictures and whatever moves you, these suffixes are already widely used to designate
[929.60 → 930.82] something altogether different.
[931.32 → 935.98] Specifically, .zip is an extension used in archive files that use a compression format
[935.98 → 936.76] known as zip.
[937.14 → 942.12] The format .mov, meanwhile, appears at the end of video files, usually when they were created
[942.12 → 943.30] in Apple's QuickTime format.
[943.72 → 944.10] End quote.
[944.10 → 947.02] Fissures and scammers rejoice.
[947.54 → 953.34] The rest of us, beware and be ready to help protect your family and friends from this otherwise
[953.34 → 955.92] completely avoidable new threat vector.
[956.78 → 962.52] The linked Ars Technica article demonstrates a few URLs scammers could now craft, and they're
[962.52 → 968.00] darn near indistinguishable from the legit URL, even to someone like myself with trained eyes.
[968.00 → 976.32] One such URL in the example is a Kubernetes release, which, yes, is distributed as a zip file.
[976.32 → 981.84] You just heard one of our five top stories from Monday's Changelog News.
[982.24 → 987.06] Subscribe to the podcast to get all the week's top stories and pop your email address in
[987.06 → 993.12] at changelog.com slash news to also receive our free companion email with even more developer
[993.12 → 994.62] news worth your attention.
[995.06 → 998.50] Once again, that's changelog.com slash news.
[998.50 → 1010.32] If I could summarize some of what's been said, we kind of talked about these two large categories
[1010.32 → 1011.40] of problems.
[1011.40 → 1020.94] One was the structuring, consistency and validation of the output of these models to make them
[1020.94 → 1023.10] useful in actual business use cases.
[1023.60 → 1030.32] And the second was maybe compliance concerns, privacy security concerns, which really have
[1030.32 → 1036.18] to do with like how a model is hosted or how you access that model.
[1036.18 → 1040.84] So on the one side, it's how do you process the output of a model?
[1040.84 → 1044.66] And then on the other side, how do you access or host a model?
[1044.88 → 1052.26] Both of those things can be pretty big blockers to kind of dive into the latter of those, the
[1052.26 → 1054.42] hosting privacy security thing.
[1054.60 → 1061.12] I actually am quite encouraged by where things are headed recently because we've seen this
[1061.12 → 1067.22] kind of proliferation and explosion of open access models that continue to be released day
[1067.22 → 1067.84] after day.
[1067.84 → 1074.18] The most recent one at the time of recording this, I might be missing one.
[1074.26 → 1075.38] They seem to come out every week.
[1075.50 → 1081.98] But one, for example, that came out recently is the MPT family of models from Mosaic ML,
[1082.18 → 1083.62] which is just really extraordinary.
[1084.38 → 1089.74] I think that they have up to like context links or like you can think about that as kind of your
[1089.74 → 1093.04] prompt size for the model of like 60,000 tokens.
[1093.04 → 1097.04] And they do quite well in various scenarios.
[1097.78 → 1102.68] So there are these increasing number of open access models.
[1103.02 → 1107.80] But I would say there are two problems with using these as a business.
[1107.80 → 1110.88] Let's say I wanted to host one of these and use it internally.
[1111.38 → 1112.66] Well, maybe three problems.
[1112.96 → 1114.56] It's always good to have three points, right?
[1114.98 → 1116.00] Three problems.
[1116.00 → 1121.72] One is like you still have to figure out like the weird GPU hosting and like scaling of that
[1121.72 → 1123.26] model, which is a challenge, right?
[1123.92 → 1129.88] The second is in reality, these open access models, at least according to most people,
[1129.88 → 1136.02] I think it's generally accepted that these aren't quite up to the standards of the larger
[1136.02 → 1141.70] commercial systems that like OpenAI and others are putting out there, Cohere and Anthropic
[1141.70 → 1142.36] and others.
[1142.78 → 1142.92] Sure.
[1142.92 → 1145.06] So there's like a performance concern.
[1145.26 → 1146.84] There's the hosting concern.
[1147.08 → 1151.92] And then the third, which is the same as our other major topic here, is you still have to
[1151.92 → 1153.52] figure out how to use the output of them.
[1153.60 → 1156.78] They're still just going to vomit up text on you, and you have to figure out how to deal
[1156.78 → 1157.24] with that.
[1157.74 → 1165.42] This has led some people to strike up this kind of expensive deals to host open AI models
[1165.42 → 1167.32] in Azure infrastructure.
[1167.80 → 1170.02] That's becoming easier over time.
[1170.10 → 1172.18] I hope that becomes increasingly easier.
[1172.18 → 1178.64] It's still a little bit like limited to Azure mainly in my understanding.
[1178.64 → 1181.26] And it's definitely not cheap.
[1181.26 → 1186.06] I would say if you kind of compare all the costs and add in the engineering time to do
[1186.06 → 1187.62] that and all that.
[1187.62 → 1196.04] So some people are solving this model hosting issue by either hosting an open access model,
[1196.22 → 1203.36] maybe with a hidden performance or implementing a really expensive kind of private version of
[1203.36 → 1205.48] open AI, something like that.
[1205.54 → 1210.24] And if you don't have that budget or if you don't know about GPUs or how to host models,
[1210.24 → 1212.74] you're kind of out of luck in a lot of ways.
[1212.74 → 1218.60] Not only I agree with you, but I think that that's going to proliferate in terms of the challenges across there.
[1218.78 → 1224.66] I know speaking for myself and another friend that I talked to a lot about this stuff a lot,
[1225.08 → 1229.60] we are experiencing the fact that as model updates come out, new models come out,
[1229.88 → 1231.44] they have different strengths and weaknesses.
[1231.44 → 1235.98] There are some things that I might, for instance, go to GPT-4 on.
[1236.08 → 1238.78] There are other things I might go to BARD on now.
[1239.70 → 1241.34] And, you know, those are just two.
[1241.48 → 1244.42] There's a bunch of open source ones that we were starting to talk about that.
[1244.94 → 1247.94] And with the acknowledgement of, for instance,
[1248.08 → 1253.74] OpenAI has kind of acknowledged that there is a practical limit in terms of how much data you can feed a model
[1253.74 → 1256.98] and that we need to start looking at other dimensions on that.
[1256.98 → 1263.40] So with practical limits in sight, the commercial advantage, for instance, may hit that ceiling
[1263.40 → 1265.72] and open source ones will gradually catch up.
[1265.82 → 1274.68] And so you're seeing the relationships of utility for a user between different models changing on a regular basis
[1274.68 → 1277.82] and us users having to make adjustments to that.
[1278.10 → 1280.86] How does that play into the landscape?
[1280.86 → 1285.60] Because if you're an organization, and you're trying to make investments,
[1286.16 → 1288.34] like do we bet on OpenAI and Microsoft?
[1288.62 → 1289.42] Do we bet on Google?
[1289.54 → 1291.18] Do we bet on open source options?
[1291.78 → 1292.90] What are the options there?
[1293.04 → 1297.12] What are the different capabilities that might be available to us for doing that?
[1297.26 → 1299.62] And acknowledging up front Prediction Guard, maybe one of those.
[1300.04 → 1301.86] What does the rest of the landscape look like?
[1301.88 → 1303.44] And how does Prediction Guard fit into that?
[1304.04 → 1306.16] And what are some of the pros and cons that you see?
[1306.44 → 1309.94] I'll decouple a couple of these things and talk about the general landscape
[1309.94 → 1311.26] and then Prediction Guard.
[1312.02 → 1318.78] So in terms of this problem of the hosting, compliance, privacy, IP leakage, that sort of thing,
[1319.24 → 1327.50] I think if you're a company of a certain size, and you can afford kind of a private open AI setup in Azure,
[1328.06 → 1330.24] it's probably a pretty reasonable solution.
[1330.66 → 1334.70] It will definitely work very well, but it's going to be very, very costly.
[1334.70 → 1342.16] And again, it's not going to solve this like structuring and usage of the output of language models problem.
[1342.50 → 1350.62] So you're going to have to put additional engineering effort into helping build layers on top of that,
[1350.70 → 1352.48] that work for your business use cases.
[1352.48 → 1359.42] You could bet on certain open access models right now, but like you said, things are advancing so quickly.
[1359.42 → 1366.22] It's hard to say like, I'm going to put all of this effort into one and hosting of the one and build a system around it.
[1366.22 → 1375.52] I do think that there are advantages if you're going that route to centre your infrastructure around kind of model agnostic workflows,
[1375.52 → 1381.18] like those in Lang chain or others, where you actually abstract away the model interface
[1381.18 → 1387.80] and can connect to multiple large language models with a lower switching cost
[1387.80 → 1391.88] than if you kind of have a one-off solution centred around a certain model.
[1391.98 → 1395.52] So I think there are some things that people could be encouraged about there.
[1395.52 → 1404.32] In terms of that, though, if you think about, okay, now I'm going to go all in on these open access models.
[1404.32 → 1407.02] Like you say, these models have different characters.
[1407.02 → 1412.58] So I'm going to want to host maybe multiple of them and generate these model agnostic workflows
[1412.58 → 1414.90] on top of Lang chain and other things.
[1415.38 → 1420.32] You start to really add up the engineering effort to make this happen.
[1420.32 → 1430.02] A parallel might be I could create a data visualization solution for my company by assembling a database and hosting that,
[1430.24 → 1436.84] making the connection into like a layer that would run like Plot plots or something like that,
[1436.84 → 1440.58] and then maybe some UI for my users that those are embedded in.
[1440.58 → 1449.12] And all of a sudden, I'm now talking about an absolute fortune in engineering costs and support costs over time,
[1449.12 → 1455.96] which is why products like Tableau or other, you know, I remember a long time ago,
[1455.98 → 1458.02] I don't know how much people are still using it.
[1458.14 → 1460.38] One of the companies I was at was using Demo.
[1460.62 → 1465.08] This is one of these solutions where you quickly suck in data and visualize it and all of that.
[1465.08 → 1468.00] There's a reason why those products exist.
[1468.54 → 1473.88] So Prediction Guard, you could kind of think of as taking the best of open source models
[1473.88 → 1479.04] and the best of this kind of control and structuring of output, which we haven't talked about yet
[1479.04 → 1485.86] and we can get into here in a second, and assembling those together in an easy to access and cost-efficient manner
[1485.86 → 1491.74] so people can get quality output out of the latest large language models
[1491.74 → 1495.28] that's structured and ready to be used in business use cases.
[1495.84 → 1504.08] And also with a guarantee if you want it around using only specific models that are hosted in a compliant way,
[1504.28 → 1507.84] even compliant in a certain way, like a HIPAA-compliant way,
[1508.00 → 1514.32] or in a data private sort of way where your data isn't leaked if you're putting data into models.
[1514.32 → 1518.48] So that's kind of how the landscape works and how Prediction Guard works
[1518.48 → 1524.06] as this kind of system that assembles the best of large language models
[1524.06 → 1529.50] with structured and typed output that can be deployed compliant
[1529.50 → 1535.12] without this whole huge engineering effort to build your, you know, roll your own system.
[1535.62 → 1540.42] You mentioned structured and typed output, and can you go ahead and kind of talk a little bit about that?
[1540.42 → 1543.34] Because I think, you know, for many of us that are listening,
[1543.58 → 1548.54] we're used to using the models that are out there kind of in the default interfaces on the web,
[1548.62 → 1552.68] you know, using ChatGPT, using BARD, and we're not really dealing with that.
[1552.78 → 1558.96] You know, we get an output, but we're not at the level of sophistication where we're doing APIs and such as that.
[1559.00 → 1562.48] Can you talk a little bit about what structured output looks like
[1562.48 → 1565.84] when you're dealing with it from an API standpoint and how you unify that landscape?
[1565.84 → 1571.96] There are a lot of use cases where this may come up, but let's take one for example.
[1572.10 → 1574.12] Let's say that you're doing data extraction.
[1574.56 → 1580.40] You have a database with a column in it, which is basically,
[1580.58 → 1583.24] so this scenario has happened at every company that I've been with,
[1583.30 → 1584.62] so I know that it's very common.
[1585.12 → 1587.50] There's some database with a table in it,
[1587.62 → 1591.08] and there's a column that's like a comments column or something.
[1591.08 → 1597.86] And it's just like text blobs in there that are like notes from people or technician messages
[1597.86 → 1601.18] or user messages or like whatever it is.
[1601.20 → 1602.10] It's not structured.
[1602.24 → 1606.76] And you want to run a large language model over that to extract,
[1606.92 → 1612.18] you know, maybe it's phone numbers or prices
[1612.18 → 1617.66] or certain classes of information out of this column.
[1617.66 → 1621.56] Well, you could run your large language model and set up a prompt that says,
[1621.66 → 1628.46] you know, give me the sentiment of each of these pieces of text in my database.
[1628.70 → 1632.42] Well, that prompt, each time you run it through a large language model,
[1632.88 → 1638.72] maybe once it generates an output that says space positive sentiment,
[1638.90 → 1642.18] and the next time it creates an output that says positive,
[1642.44 → 1646.50] and the next time it creates an output that says this is positive sentiment.
[1646.50 → 1649.68] And you can start to see there's a consistency problem here.
[1649.78 → 1653.44] Like, how do I parse all of these strange outputs from my large language model?
[1653.96 → 1656.84] You can do a little bit of prompt engineering to get around that,
[1656.96 → 1661.10] but ultimately it doesn't solve the problem that you could have all sorts of weird output
[1661.10 → 1662.54] out of your large language model.
[1662.94 → 1666.60] So ultimately what you would want in that scenario is a system
[1666.60 → 1671.34] that lets you constrain and control what types of output
[1671.34 → 1673.50] you're going to get out of your large language model.
[1673.50 → 1677.88] So in the case of sentiment, maybe I want to restrict my output to only
[1677.88 → 1681.92] POS, NEG, and NEW, tags for sentiment.
[1682.06 → 1683.04] There's only three choices.
[1683.28 → 1685.34] I always want one of those three, right?
[1685.42 → 1689.06] I don't want it to say this is positive sentiment, right?
[1689.42 → 1693.74] So I want to actually structure or control the output of my large language model
[1693.74 → 1695.84] to produce one of these outputs.
[1696.42 → 1701.14] Another example that's maybe a little bit more complicated would be to say,
[1701.14 → 1706.46] I actually want to output a valid JSON blob out of my large language model
[1706.46 → 1709.70] or valid Python code out of my large language model.
[1709.86 → 1713.78] And these are structures that are very well-defined,
[1713.78 → 1717.48] but you could have all sorts of variability coming out of your large language model.
[1717.62 → 1721.42] And if you want a specific type coming out of your large language model,
[1721.56 → 1726.78] maybe it's a float that you can do like greater than or add it to another number.
[1726.78 → 1731.90] Like you need that as a typed output, or you need very specific structured output
[1731.90 → 1735.26] to actually make automated decisions in your business.
[1735.42 → 1740.26] And so with Prediction Guard, what we're doing is we're kind of assembling the best
[1740.26 → 1744.52] of the recent advances in this kind of control and structuring of output
[1744.52 → 1750.36] and layering it on top of these open source large language models to allow you to say,
[1750.36 → 1757.80] here's my prompt, I'm going to send it to these five open source or open and or closed.
[1757.80 → 1759.26] We support OpenAI as well.
[1759.64 → 1761.24] So open and or closed models.
[1761.78 → 1765.18] And for each output, I want you to give me a float number.
[1766.04 → 1771.48] And that's the sort of rich output that you can get from large language models very quickly
[1771.48 → 1777.06] with Prediction Guard kind of prompt because you can control the models that you're using,
[1777.06 → 1782.88] either ones that are more privacy conserving or the closed source options and provide constraints
[1782.88 → 1786.56] around the output that allow you to actually make business decisions on that.
[1786.92 → 1792.02] Now, there are additional checks that could go along with that, like factuality checks and toxicity
[1792.02 → 1793.98] checks, which we also implement.
[1794.58 → 1797.54] But I've vomited up a lot of information.
[1797.54 → 1798.50] So I'll pause here.
[1799.44 → 1800.96] No, no, that sounds fascinating.
[1801.18 → 1806.06] It's the way I'm interpreting what you're saying is sort of like you have this kind of software filters
[1806.06 → 1812.08] that are creating boundaries, if you will, on how you structure input and what that output
[1812.08 → 1816.88] can be so it's usable, which kind of goes back to one of the points that we're often talking
[1816.88 → 1822.08] about on the show is that the AI is to some degree inseparable from the software that you're
[1822.08 → 1822.72] using it within.
[1822.90 → 1828.44] And so you have the best of breed software product that's kind of shaping and constraining what
[1828.44 → 1831.78] that can be so that it's actually usable on that.
[1831.78 → 1838.84] Um, so as we look forward at kind of where things are going and you, what, what are some
[1838.84 → 1843.76] of the problems that you see going in the space that we have?
[1843.76 → 1847.74] And like, what are some of the things that you would like to see prediction guard starting
[1847.74 → 1849.78] to address, uh, in the time ahead?
[1849.84 → 1853.78] And I don't mean so much as the far distance, but kind of like you're, you're busy putting
[1853.78 → 1858.02] this solution together now, uh, works pretty darn well.
[1858.02 → 1859.28] Oh, what you already have.
[1859.40 → 1863.00] What are some of the challenges when you're in this kind of fast moving space?
[1863.00 → 1867.04] Because you're, you're having the world change out from under you on a week by week basis
[1867.04 → 1867.52] right now.
[1868.12 → 1868.36] Yeah.
[1868.36 → 1873.68] I think maybe one of the things that we're thinking about is really at the forefront of
[1873.68 → 1880.64] our mind is ease of use and accessibility to both data scientists and developers.
[1880.64 → 1887.58] So the reality is that I think we had Kirsten Sum on the podcast talking about this, like
[1887.58 → 1892.52] the majority of data scientists out there are supers constrained in the time that they
[1892.52 → 1894.58] have to put into one of these solutions.
[1894.58 → 1895.06] Right.
[1895.28 → 1903.38] So it's really, really important that there is an ease of use to this sort of controlled
[1903.38 → 1907.88] compliant LLM output and generative AI output.
[1907.88 → 1913.16] Now what we're seeing, and I want to acknowledge this as well as there are an increasing number
[1913.16 → 1919.28] of open source projects that are doing an amazing job at digging into this problem of
[1919.28 → 1921.26] controlled and guarded LLM output.
[1921.40 → 1929.38] So these are things like guardrails and guidance from Microsoft and, uh, Matt Rickard's, REALM or
[1929.38 → 1930.74] regex LLM.
[1930.74 → 1938.04] These projects are doing amazing things at really flexible ways for you to control the
[1938.04 → 1939.96] output of large language models.
[1940.14 → 1944.28] But I see this as kind of like a double-edged sword a bit.
[1944.46 → 1951.70] The more flexible you become, it's also possible to become less easy to use.
[1952.02 → 1953.74] And there's more engineering involved in it.
[1953.74 → 1954.38] Yeah.
[1954.58 → 1961.78] So I saw Matt Rickard, uh, tweet about this related to his regex LLM project, which is
[1961.78 → 1966.24] that sort of famous quote about regex, which is I have a problem.
[1966.34 → 1970.18] And so I decided to use regex, and now I have two problems.
[1970.34 → 1970.66] Yeah.
[1971.08 → 1972.02] That's an old one.
[1972.08 → 1973.60] That's been around for a long time, actually.
[1973.68 → 1974.16] Yeah.
[1974.52 → 1976.20] It's actually so true.
[1976.20 → 1976.56] Right.
[1976.56 → 1982.68] And, uh, these, some of these solutions are coming up with their own query languages to
[1982.68 → 1986.78] kind of deal with this structured output, which I think is great.
[1986.78 → 1991.88] And it's really important, but there's a need for this abstraction layer on top where
[1991.88 → 1995.70] I know kind of what I want my output to look like.
[1996.08 → 2002.52] So I should be able to plug that into something and have it constrain the output of my large
[2002.52 → 2004.26] language model appropriately.
[2004.26 → 2010.96] So with prediction guard, what we've started with is the kind of presets of structuring
[2010.96 → 2011.52] your output.
[2011.68 → 2016.88] So I want integer and float and JSON and Python or YAML.
[2017.12 → 2018.76] I want categorical output.
[2018.92 → 2020.60] These are things that we support now.
[2020.96 → 2026.90] Also, uh, supporting kind of these hosted models and access in a guarded kind of controlled
[2026.90 → 2027.96] way to these models.
[2028.16 → 2033.26] But let's say that I have a really specialized format that I want to work with.
[2033.26 → 2037.10] I would rather set up a solution with prediction guard.
[2037.18 → 2042.06] And this is actually what we're actively working on where they could give examples of the structure
[2042.06 → 2042.94] that they want.
[2043.16 → 2049.40] And we actually generate the right constraints for them on the large language model output,
[2049.40 → 2050.86] which I think is very possible.
[2051.04 → 2055.92] And our initial work on this, which is kind of in a beta form is perfect.
[2055.92 → 2062.46] So let's say that I want a specific JSON with these specific fields or a specific CSV output
[2062.46 → 2064.60] with these specific columns, right?
[2065.02 → 2070.68] I should be able to give a few examples of that and generate the right underlying constraints
[2070.68 → 2075.48] for my large language model without the user having to think about special languages or
[2075.48 → 2080.80] regex or context-free grammar or these things that are a little bit harder to grasp.
[2080.80 → 2086.22] We'll handle that bit for you and you just get the right structured output from your models.
[2086.40 → 2093.40] So that's part of where I see us headed is leveraging these rich systems under the hood
[2093.40 → 2099.38] that are being produced around using context-free grammars, special query languages, regex,
[2099.46 → 2105.10] all of these things to structure output and combining those in a more automated way for users
[2105.10 → 2110.40] where they can just say, here's my examples, here's my query, and they just start getting
[2110.40 → 2113.52] the right formatted output from their language model.
[2113.64 → 2118.48] So that's kind of thing one is this automation of some of the problem and the constraints.
[2118.48 → 2125.74] I think the thing two would really be around the validation and checking of output in addition
[2125.74 → 2126.84] to the structuring.
[2127.30 → 2133.40] So right now we support factuality and toxicity checks on the output of large language models.
[2133.40 → 2136.10] Could you talk a little bit about what each of those are?
[2136.66 → 2137.24] Yeah, yeah.
[2137.38 → 2143.54] So let's say that I take a big piece of text and I generate a summary, or I do a question-answer
[2143.54 → 2145.46] prompt and get an answer, right?
[2145.72 → 2148.84] That doesn't mean the answer is factual, right?
[2148.96 → 2153.52] And we all know about the hallucination problems of these models.
[2153.74 → 2158.72] So the things that we have implemented in Prediction Guard are two things with respect to that.
[2158.72 → 2165.32] The first is a factuality checking score, which is built on these trained models under the
[2165.32 → 2172.78] hood that look at a reference piece of text and your text output to determine a likelihood
[2172.78 → 2174.50] of the answer being factual.
[2175.00 → 2178.18] So this is an estimate on the factuality of your output.
[2178.42 → 2183.80] The other thing that we're doing around hallucinations and factuality is making it really easy for people
[2183.80 → 2185.34] to do consistency checks.
[2185.34 → 2190.42] I kind of alluded to this earlier, but we have all of these different language models
[2190.42 → 2192.04] accessible under the hood.
[2192.18 → 2200.40] So you could combine the outputs of CAMEL 5 billion, MPT 7 billion, DALI, and OpenAI,
[2201.18 → 2207.74] restrict the output to say, give me the answer, but only if all of these agree on what the output is.
[2207.74 → 2212.74] If all of them don't agree, then I'm going to flag that as not a reliable output.
[2213.16 → 2218.18] And so you can actually gain a lot by not just leveraging one model, but resembling these
[2218.18 → 2219.78] models together to do a check.
[2219.92 → 2224.34] The toxicity thing is something that's been studied for a while, and there are models out
[2224.34 → 2231.08] there, state-of-the-art models for detecting whether an output is toxic or not, or includes
[2231.08 → 2232.96] hate speech or not, that sort of thing.
[2233.28 → 2236.28] So this is another layer of check that you can have on the output.
[2236.28 → 2242.10] And so if you put the whole pipeline together of prediction guard, you've got models on
[2242.10 → 2247.98] the output, which can be deployed compliant with HIPAA or just data privacy.
[2248.26 → 2252.80] Those structured or typed output that you can define very easily.
[2252.80 → 2258.74] And then you can run additional checks on that output for factuality, toxicity, consistency
[2258.74 → 2265.88] as a final sort of layer in the pipeline towards the output that's used in a business application.
[2266.28 → 2267.54] I appreciate the explanation.
[2267.72 → 2271.24] It's a very robust sounding pipeline that you have on that.
[2271.70 → 2277.06] Let me ask you this, and this could be whether it's prediction guard or whether it's the larger
[2277.06 → 2277.88] field.
[2278.42 → 2282.86] You know, one of the challenges is certainly something I've been playing with, but I don't
[2282.86 → 2284.98] have a good rhyme or reason to it yet.
[2284.98 → 2290.74] But with the proliferation of these models coming out and evermore coming, you know, we know
[2290.74 → 2292.40] this space is going to get larger and larger.
[2292.40 → 2298.48] How does a user, or how would a system like prediction guard be able to determine which
[2298.48 → 2303.38] is the right way to go in terms of which model you want to choose, or which group of models?
[2303.50 → 2305.62] And you talked about the comparisons a moment ago.
[2305.62 → 2314.16] Like, how do you structure the input and know that you're going to get what you need from
[2314.16 → 2318.90] an output by putting the right model or collection of models together and then knowing how to
[2318.90 → 2320.06] evaluate them against each other?
[2320.14 → 2320.78] Does that make sense?
[2321.32 → 2321.74] Yeah, yeah.
[2321.76 → 2322.50] That makes sense.
[2322.90 → 2328.48] Actually, early on when we were building the prediction guard back in, this was actually
[2328.48 → 2332.60] front of my mind and has since kind of evolved a little bit.
[2332.60 → 2336.98] The fact that there's all of these models and I want to choose the right one for my
[2336.98 → 2339.98] use case, you can very much automate that process.
[2340.14 → 2344.82] And we actually it's actually still implemented in the prediction guard back end where you can
[2344.82 → 2349.06] give some examples and evaluate a bunch of models on the back end.
[2349.62 → 2355.70] I think where this is headed, though, and where the prediction guard system is headed is making
[2355.70 → 2362.34] it is easier for people to get output from multiple models in a typed way.
[2362.60 → 2364.78] Because they know how to do the evaluation.
[2365.12 → 2369.62] They're familiar with this sort of thing, whether you're a developer doing sort of integration
[2369.62 → 2375.20] tests or unit tests, and you're checking, and you're asserting certain values, or you're a
[2375.20 → 2378.90] data scientist that's running a larger scale test against the test set.
[2379.42 → 2382.78] People kind of know what they want to do with that sort of thing.
[2382.78 → 2387.72] What they need is an easy way to get that typed output from multiple models.
[2387.72 → 2394.88] So like if I have a test set, and I'm comparing two scores on the output, like float numbers,
[2395.04 → 2400.28] I need to get float numbers out of a bunch of different large language models to
[2400.28 → 2404.08] compare them to my baseline or to my test set.
[2404.24 → 2410.68] Right now, that's very difficult because all of these different kind of structuring guidance
[2410.68 → 2417.58] control systems work not for all models, and they don't work in the same way for all models
[2417.58 → 2420.04] and you have to implement it for all the models.
[2420.54 → 2425.40] And so it becomes this compounding problem to figure out how to do that.
[2425.40 → 2430.48] And so how we're approaching that with the prediction guard system is there's a standardized
[2430.48 → 2436.52] API to all of these different models along with the typed and structure control on the output.
[2436.52 → 2445.22] So I can do a query that says, give me the float output for these hundred prompts using
[2445.22 → 2447.26] these five models.
[2447.68 → 2451.26] And then I'll just compare all the float outputs and figure out which is the best.
[2451.50 → 2454.08] That's not the hard problem.
[2454.26 → 2460.26] It's the getting that structured output from the variety of models in a robust and consistent
[2460.26 → 2463.24] way that's actually a more difficult problem.
[2464.10 → 2464.20] Gotcha.
[2464.20 → 2470.42] Is it fair, you know, as we're talking about this, it sounds a lot like you're also solving
[2470.42 → 2475.06] one of the bigger challenges we've talked about over time, which is that there's so much
[2475.06 → 2479.32] domain expertise in the AI space in terms of being able to manage models.
[2479.90 → 2486.18] But if I'm understanding you correctly, it sounds like with minimally, with some basic software
[2486.18 → 2492.66] skills, knowing how to use APIs and stuff, you can probably without deep expertise and deep
[2492.66 → 2498.80] learning manage to get some fairly productive output through production guard by implementing
[2498.80 → 2499.20] it that way.
[2499.28 → 2501.86] In other words, it becomes just another part of your software workflow.
[2502.04 → 2503.92] Is that a fair characterization?
[2504.24 → 2504.64] What I'm saying?
[2505.36 → 2512.86] I would say it is in the sense that there's still some sort of like integration testing and
[2512.86 → 2515.86] integration that will have to happen regardless.
[2515.86 → 2516.34] Right.
[2516.34 → 2516.42] Right.
[2517.00 → 2523.76] But going back to my example before of like the data visualization stack, it's a lot
[2523.76 → 2530.98] harder to implement the database and the visualization layer and the front end than it is to like log in and
[2530.98 → 2535.88] do the there's still configuration that's needed in like a Demo type solution or Tableau.
[2535.88 → 2537.56] It's just a lot more accessible.
[2537.56 → 2538.00] Right.
[2538.34 → 2542.38] So here we have the language models hosted on the back end.
[2542.52 → 2548.96] We have the structured guarded way to query those models via something that all developers
[2548.96 → 2552.12] know how to use a REST API or a Python client.
[2552.72 → 2558.70] Maybe there'll be other clients over time and have the ability to configure that in the way
[2558.70 → 2559.28] that you want.
[2559.38 → 2561.34] So I want output from these five models.
[2561.44 → 2565.00] I want to ensemble them together, or I want this structured output.
[2565.00 → 2566.80] And so there's still configuration.
[2567.04 → 2570.12] And I think developers and data scientists, they want that.
[2570.90 → 2574.10] It's just that it's really hard to get all the other pieces in place.
[2574.24 → 2576.66] And we're hopefully making that a lot easier.
[2577.64 → 2579.04] So and let me ask one final.
[2579.16 → 2582.20] I think this is an aspirational question, but I'm kind of curious.
[2582.82 → 2587.68] One of the things that we've seen with large language models is the ability for people who
[2587.68 → 2588.70] aren't even developers.
[2589.00 → 2594.20] You know, I was saying like developers who aren't even deep learning experts, but to have a certain
[2594.20 → 2601.58] amount of capability producing code, you know, that's the kind of avenue into a no code world
[2601.58 → 2603.52] has at least been started on this.
[2603.58 → 2605.28] It has a lot of maturing to do, obviously.
[2605.78 → 2611.84] Do you envision a point where someone with very limited skills can also use prediction
[2611.84 → 2618.06] guard in this way and be able to kind of generate apps using large language models that
[2618.06 → 2622.04] then kind of feed into a more mature workflow like what you've described?
[2622.04 → 2625.86] Do you think that that's attainable at some point in the not so distant future?
[2626.64 → 2631.12] It's hard to say how far this kind of automation will go.
[2631.30 → 2637.94] I think a lot of the agents that we've seen produce good demos, right?
[2638.00 → 2643.50] But they have an additional layer of this sort of additional problems around automating these
[2643.50 → 2645.52] various steps of the process.
[2645.52 → 2652.28] I think that in terms of what we're looking at, this sort of automated structuring of output
[2652.28 → 2658.20] is a step in the right direction in terms of I don't have to define a special query language
[2658.20 → 2664.22] or a special specification, but I can say what sort of structure I want output and that
[2664.22 → 2664.92] gets output.
[2665.06 → 2671.18] I think then if you layer that on top of the agent sort of infrastructure that's in Lang
[2671.18 → 2676.44] chain and the data augmentation, we just had the episode with Jerry from Llama Index, which
[2676.44 → 2677.46] is super fascinating.
[2677.74 → 2685.50] So if you layer the kind of structured guarded output with the chaining and agent and automation
[2685.50 → 2691.82] of Lang chain and maybe the data augmentation of Llama Index, I think a lot of things become
[2691.82 → 2692.30] possible.
[2692.72 → 2696.02] I hope that that becomes some of the things that you mentioned become possible.
[2696.02 → 2703.18] It's yet to be seen, but I am really encouraged that adding in this sort of type safety for
[2703.18 → 2708.84] outputs and structuring of outputs gives a lot more confidence maybe in some of the checks
[2708.84 → 2712.30] that you could do on AI agents over time.
[2712.76 → 2719.24] And that increases our confidence in sort of releasing AI agents on various parts of the
[2719.24 → 2721.22] workflows that we'd like them to work on, right?
[2721.82 → 2724.30] So you've sort of already covered some of the territory.
[2724.30 → 2730.46] But for our listeners, Daniel and I often when we're talking to a guest, we'll kind of
[2730.46 → 2735.96] finish with what we roughly call the future question, you know, kind of wax poetic about
[2735.96 → 2737.02] where things are going.
[2737.78 → 2742.80] And so Daniel, since you're knowing that there's, I've kind of hit some of that already, but
[2742.80 → 2745.38] what would you be asking yourself?
[2745.82 → 2750.68] You know, so you've kind of had me throwing these questions at you from a point of somewhat
[2750.68 → 2754.28] ignorance compared to where you're coming from as the expert on it.
[2754.70 → 2759.64] What right now would you ask yourself that you haven't covered that you think is worthy
[2759.64 → 2761.78] of getting in before the episode is over?
[2762.00 → 2763.22] I'm putting you on the spot.
[2764.34 → 2769.18] Yeah, I've mentioned open access models quite a bit.
[2769.34 → 2774.58] And I think hopefully a lot of us are encouraged by the direction that that's going, that these
[2774.58 → 2776.10] models are getting better and better.
[2776.10 → 2783.74] But one thing that maybe I would ask myself or that I think is important to highlight and
[2783.74 → 2790.88] encourage people with is these open access models might not quite be at the level of open
[2790.88 → 2793.80] AI, Anthropic, et cetera, yet.
[2793.80 → 2801.20] But I think not only will they get there, but already like in the space where we're at now
[2801.20 → 2806.28] with some of these kind of structured control elements around open access models, you can
[2806.28 → 2812.50] actually boost the performance of open access models to be more in line with, you know, open
[2812.50 → 2818.36] AI level output, because what you can do is say, well, I'm going to force my output to this.
[2818.52 → 2823.72] If I'm not able to produce it, you know, I can re-ask the question, or I can try a variant
[2823.72 → 2830.24] of my prompt and this kind of wrapping layers around open access models actually provide a way
[2830.24 → 2838.68] for you to operate in a data private compliant way with open access models that boost their
[2838.68 → 2845.46] performance closer to what this kind of closed and maybe more suspect in terms of IP leakage
[2845.46 → 2847.90] and that sort of thing systems are doing.
[2848.16 → 2852.16] So I think that's an encouragement that I've found recently.
[2852.16 → 2857.86] And I hope that's encouraging to others is we are really seeing a proliferation of these
[2857.86 → 2861.34] models, and they're all going to have a little bit of different character.
[2861.74 → 2868.12] But the ways that we wrap them and the way that we present them is a lot of provides the
[2868.12 → 2870.32] majority of the value of those models.
[2870.48 → 2876.12] And I think we'll see not only Prediction Guard, but other systems as well coming out that wrap
[2876.12 → 2881.82] these models and use them in really intelligent manners that boost their performance in a way that
[2881.82 → 2884.86] isn't reliant on sort of centralized API.
[2885.58 → 2886.92] I appreciate that.
[2887.02 → 2887.98] I think you're right.
[2888.60 → 2893.92] And I am deeply appreciative of you not only telling us about Prediction Guard, but actually
[2893.92 → 2895.50] kind of laying out the space.
[2895.96 → 2902.96] Even if someone is not champing at the bit the way I am to use Prediction Guard, they hopefully
[2902.96 → 2907.20] kind of understand what some of the problems are that need to be addressed, whether by you
[2907.20 → 2908.30] are others out there.
[2908.86 → 2914.22] So thank you for allowing me to twist your arm and do this episode today.
[2915.12 → 2918.14] I appreciate you letting me go there.
[2918.26 → 2924.94] So anyway, thank you very much to my good co-host and my guest today for coming on Practical
[2924.94 → 2925.16] AI.
[2925.52 → 2926.46] Thanks so much, Chris.
[2926.46 → 2956.44] Thank you.
[2956.46 → 2961.46] Thanks once again to our partners Vastly, Fly, and Type Sense for helping us bring you
[2961.46 → 2963.40] awesome pods each and every week.
[2963.82 → 2968.02] And to Break master Cylinder for producing all the beats on all Changelog podcasts.
[2968.76 → 2969.84] That's all for now.
[2970.14 → 2971.88] We'll talk to you again next week.
