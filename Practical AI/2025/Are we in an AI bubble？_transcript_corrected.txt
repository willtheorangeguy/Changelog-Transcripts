[0.00 → 8.74] Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 → 13.64] of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 → 19.14] Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 → 23.54] Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 → 25.12] buzz, you're in the right place.
[25.12 → 29.84] Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 → 33.02] drops, behind-the-scenes content, and AI insights.
[33.36 → 35.88] You can learn more at practicalai.fm.
[36.20 → 37.50] Now, on to the show.
[39.94 → 44.54] Well, friends, when you're building and shipping AI products at scale, there's one constant.
[45.18 → 45.66] Complexity.
[46.06 → 50.80] Yes, you're wrangling models, data pipelines, deployment infrastructure, and then someone
[50.80 → 53.28] says, let's turn this into a business.
[53.78 → 55.04] Cue the chaos.
[55.24 → 59.82] That's where Shopify steps in, whether you're spinning up a storefront for your AI-powered
[59.82 → 63.00] app or launching a brand around the tools you've built.
[63.36 → 68.72] Shopify is the commerce platform trusted by millions of businesses and 10% of all U.S.
[68.82 → 73.72] e-commerce, from names like Mattel, Gymshark, to founders just like you.
[74.28 → 79.92] With literally hundreds of ready-to-use templates, powerful built-in marketing tools, and AI that
[79.92 → 84.48] writes product descriptions for you, headlines, even polishes your product photography.
[85.04 → 88.52] Shopify doesn't just get you selling, it makes you look good doing it.
[88.52 → 89.66] And we love it.
[89.92 → 91.06] We use it here at Changelog.
[91.26 → 93.68] Check us out, merch.changelog.com.
[93.88 → 95.18] That's our storefront.
[95.58 → 97.50] And it handles the heavy lifting, too.
[97.82 → 102.00] Payments, inventory, returns, shipping, even global logistics.
[102.64 → 106.56] It's like having an ops team built into your stack to help you sell.
[106.56 → 109.72] So, if you're ready to sell, you are ready for Shopify.
[110.34 → 117.02] Sign up now for your $1 per month trial and start selling today at Shopify.com slash practical
[117.02 → 117.44] AI.
[118.12 → 122.66] Again, that is Shopify.com slash practical AI.
[122.66 → 141.40] Welcome to another episode of the Practical AI Podcast.
[141.98 → 147.88] In these fully connected episodes where it's just Chris and me without a guest, we like to
[147.88 → 154.42] explore some topics from trending AI news or things that are being discussed in the community.
[154.66 → 160.72] Hopefully, we learn along the way and our listeners learn along the way, and we help you all level
[160.72 → 162.68] up your AI and machine learning game.
[163.14 → 164.06] I'm Daniel Snack.
[164.20 → 166.32] I am CEO at Prediction Guard.
[166.84 → 172.68] And I am joined, as always, by my co-host, Chris Benson, who is a principal AI research engineer
[172.68 → 173.52] at Lockheed Martin.
[173.86 → 174.52] How are you doing, Chris?
[174.52 → 176.22] Hey, doing good today, Daniel.
[176.44 → 181.04] Just cruising along, chewing some bubble gum, doing my thing.
[182.20 → 188.90] We both needed a sugary but not sugary caffeinated drink.
[189.00 → 190.42] I think you've got a PIB Zero.
[190.60 → 191.72] I've got a Coke Zero.
[192.16 → 192.90] There you go.
[193.00 → 199.32] It's been a long day of work, and now we get to talk about some fun things.
[199.32 → 204.28] Hopefully, we won't pop the AI bubble today.
[204.78 → 205.82] But certainly...
[205.82 → 205.98] It's okay.
[206.10 → 208.64] We'll clean up the situation if we have to.
[209.14 → 209.98] Yeah, exactly.
[210.28 → 211.50] It's interesting, Chris.
[211.96 → 213.14] I was looking around.
[213.26 → 219.12] Of course, we're always seeing things or people are forwarding us various things in the news
[219.12 → 220.08] related to AI.
[220.08 → 226.98] One this week that I saw was maybe an interesting one with a humanoid-looking robot.
[227.20 → 233.86] But I'd rather maybe discuss this other stuff, which I think a couple of these things that
[233.86 → 236.26] I saw connected...
[236.26 → 241.24] And Chris, a little while ago, we did a hot take and debates type episode.
[241.24 → 248.26] I think today, there's certainly on this topic, there are various sides of this topic and strong
[248.26 → 249.22] opinions about it.
[249.34 → 251.34] And we can just talk through some of those.
[251.92 → 254.38] Certainly, there is a debate going on.
[254.98 → 259.64] And this is really the question, are we in an AI bubble?
[259.96 → 262.68] Which seems to be talked about all the time.
[262.82 → 267.26] People see something in the news, and they're like, oh, we're definitely in an AI bubble.
[267.26 → 271.08] Or people are like, oh, this isn't an actual AI bubble.
[271.30 → 274.56] It's different from maybe the dot-com bubble.
[275.10 → 277.38] Chris, you hear similar anecdotes.
[277.70 → 278.72] And maybe what is your...
[279.68 → 282.74] Maybe just the general concept of bubble.
[283.08 → 285.88] We're not talking about bubble gum, but...
[285.88 → 292.44] Yeah, I mean, the general notion of a bubble, you know, is it's really a financial concept
[292.44 → 300.34] where the valuation of an organization exceeds what its actual value is.
[300.38 → 304.90] In other words, what it's putting out in terms of product and services and the returns
[304.90 → 306.70] that are yielded by those.
[306.70 → 313.06] And so, you know, if you are talking, for instance, about the dot-com bubble, and for
[313.06 → 318.48] those of you who may not have, depending on if you're in the younger skew of our audience,
[318.48 → 328.48] around 2000-ish, in that there was all this internet craze and rage and hype, not dissimilar
[328.48 → 331.16] from the hype we've been seeing in recent years over AI.
[331.66 → 337.68] And a lot of companies came about and new startups and stuff, and they got valued very,
[337.68 → 345.52] very high, but they had very little, in some cases, no revenue and thus no profits available.
[345.52 → 353.32] And so, big valuation by the market with absolutely nothing coming out of them of value.
[353.82 → 358.12] And so, there's a point where the market kind of realizes that and corrects.
[358.66 → 366.80] And the giant dot-com, you know, facade came falling down and kind of led into a recessionary
[366.80 → 368.54] period around the globe.
[368.72 → 371.48] And so, it was kind of a big thing over several years.
[371.48 → 379.40] And so, through this entire period of AI buildup, that's been a concern that has come up regularly.
[379.56 → 383.84] This is not the first time, you know, we've been hearing about AI bubbles and stuff.
[384.20 → 388.20] So, I don't think there's a year that's gone by that we've been doing this podcast where
[388.20 → 389.62] it hasn't been raised as an issue.
[389.74 → 390.26] What do you think?
[390.68 → 391.38] Maybe so.
[391.60 → 391.84] Yeah.
[391.84 → 399.68] And I think there is, you know, genuine concern because previous bubbles that have burst have
[399.68 → 402.80] actually caused real harm.
[403.04 → 409.42] As you mentioned, whether that's economic kind of recession, certainly it distorts the way
[409.42 → 416.96] people invest or maybe what they invest into, which kind of has an effect potentially on retirement
[416.96 → 418.68] or 401ks.
[419.68 → 428.76] There's, you know, a reduction in trust in certain types of organizations or financial institutions
[428.76 → 432.08] or technology companies, that sort of thing.
[432.14 → 433.40] And it could be companies.
[433.56 → 434.46] It could be assets.
[434.72 → 441.02] Like, you know, a lot of times people talk about crypto as an asset that, you know, or I remember
[441.02 → 445.26] not too long ago talking to tons of people about NFTs, right?
[445.32 → 449.64] And this really chaotic time with NFTs.
[449.84 → 454.22] And there's a lot of people that lost a lot of money in that.
[454.88 → 457.32] So, it is a valid concern.
[458.04 → 465.36] And I think the question that's on people's mind is, are we in an AI bubble?
[465.36 → 473.54] And one of the interesting articles that I saw this week, Chris, was that Powell, the Federal
[473.54 → 483.36] Reserve Chair, Jerome Powell in the U.S., for those that aren't listening or aren't listening
[483.36 → 492.78] from the U.S., that's the Federal Reserve Chair, Jerome Powell, often can kind of, anything
[492.78 → 499.32] that's said about the economy by whoever's in this position is taken with a lot of weight
[499.32 → 505.70] because, well, Chris, you may have comments on this, but I'm not an economist.
[506.64 → 514.94] But generally, it is a sign of at least an intelligent opinion on things where there's a lot that's
[514.94 → 519.38] gone on or a direction that, you know, the Federal Reserve wants people to think.
[519.38 → 527.96] So, the two-second background without going off on a track is Jerome Powell, in his capacity,
[528.52 → 532.04] is responsible for a particular committee at the Federal Reserve.
[532.44 → 538.08] And they are responsible for monetary policy, which the Federal Reserve sets, as opposed to
[538.08 → 542.62] what the President and Congress together set, which is fiscal policy.
[542.62 → 549.12] And one of the tools, the largest tool that they mainly do that with, is through the setting
[549.12 → 554.30] of interest rates, which trickles through the entire economy in a bunch of different
[554.30 → 554.62] ways.
[554.68 → 560.36] And I don't want to go into any more depth than that, but they thus slow down or speed up
[560.36 → 566.20] the economy to either tackle an underperforming economy or inflation on the opposite side.
[566.20 → 568.12] And they're trying to balance it between the two.
[568.12 → 576.46] And so, yeah, Chairman Powell noted that there was actually revenue associated with AI expenditure,
[576.92 → 579.94] and thus it wasn't bubble-like in his view.
[580.26 → 583.38] And he is certainly an expert in a lot of ways.
[583.52 → 589.02] I think that there are some other considerations in there, but it's definitely a powerful statement
[589.02 → 591.40] coming from, you know, that particular individual.
[591.40 → 592.92] Yeah, yeah.
[593.06 → 598.78] The title of the article in Fortune, which we'll link, is Powell says that unlike the
[598.78 → 601.80] dot-com boom, AI spending isn't a bubble.
[601.94 → 607.18] And the quote is, I won't go into particular names, but they actually have earnings.
[607.34 → 609.62] Now, I guess we could speculate on this podcast.
[609.94 → 612.22] I don't know what names he's talking about.
[612.22 → 619.50] I'm assuming it's some of these larger names that would be whatever, OpenAI, Anthropic,
[619.84 → 625.42] Cohere, you know, whatever the ones are that people would think of.
[625.48 → 628.46] I imagine some of those are, quote, the names.
[628.92 → 632.38] But he says they sort of actually have earnings.
[632.84 → 639.34] The other interesting piece that I saw, Chris, which is maybe on the other side of this argument,
[639.34 → 644.98] and we can talk maybe after this about, you know, the different ways that people argue
[644.98 → 647.08] that we are or aren't in an AI bubble.
[647.48 → 653.10] But this other one was from the New York Times, which is reporting that NVIDIA is now worth
[653.10 → 654.50] $5 trillion.
[656.42 → 662.16] And this is the quote from the article, as it consolidates power in AI boom.
[662.16 → 668.74] So it's the subheading, the AI chipmaker has become a linchpin in the Trump administration's
[668.74 → 670.66] trade negotiations with Asia.
[670.80 → 675.48] So there's, there's, you know, some policy and political angle to this article.
[675.48 → 685.20] But the general idea with the article is that this $5 trillion valuation maybe is, is part
[685.20 → 686.86] of an AI boom.
[687.30 → 689.54] So yeah, that's certainly interesting.
[689.54 → 691.34] It is, it is.
[692.06 → 696.54] And, and I think we're seeing that, you know, going back to those names that were left unsaid,
[696.66 → 699.40] you, you named a few of those names.
[699.40 → 706.72] And, you know, I think any of the large cloud service providers that are offering a collection
[706.72 → 711.28] of AI services probably, you know, round out some of those names.
[711.52 → 718.22] One of the things, one of the distinctions that I think is interesting to, to weigh as we
[718.22 → 726.36] talk about this is the fact that while he noted, meaning Mr. Powell noted that some of these
[726.36 → 733.02] organizations have earnings, and we are seeing, you know, that reflected in AI related stocks
[733.02 → 740.50] that are just dominating S&P 500 returns to the, to the degree of about 75% of those returns,
[740.50 → 745.88] 80% of earnings growth and 90% of capital spending growth.
[745.96 → 748.32] I mean, those are phenomenal numbers.
[748.32 → 753.36] When you think about that in terms of percentages of total markets that are out there, you know,
[753.42 → 756.30] are obvious, at least exchanges that are representing markets.
[756.30 → 758.18] So, I mean, that's really shocking.
[758.18 → 765.86] But I think one of the things that is, that, that he did not say, and speaking as someone
[765.86 → 772.44] who has nowhere near the economic expertise of Mr. Powell, but did, did have some university
[772.44 → 780.32] studies in economics that, you know, those, those numbers are concentrated in a tiny fraction
[780.32 → 782.74] of companies overall.
[783.48 → 790.38] And so my question that I would ask is for, for some of those giant companies that are,
[790.48 → 796.62] that are making huge earnings from many, many, many thousands of customers spending huge amounts
[796.62 → 798.24] of money on AI growth.
[798.40 → 804.72] We have also talked about the fact that there is, there's also in the media quite a bit of
[804.72 → 810.64] questioning of ROI on a lot of those AI investments at various companies.
[810.64 → 817.52] And so, you know, if you're the cloud provider making bus of money, that's great.
[817.52 → 822.90] But if you're one of the companies out there that maybe is spending on that, but maybe not
[822.90 → 828.36] seeing an ROI on that expenditure, that is a different story right there.
[828.36 → 834.08] And so, you know, I, you know, maybe it's boom for one and a bubble for another.
[834.64 → 839.20] Maybe it's not just a universal bubble, but it depends on who you're talking to, to some degree.
[840.02 → 840.16] Yeah.
[840.34 → 848.50] And I guess that's where maybe this is murky is the some people might define bubble differently.
[848.80 → 855.38] I think that, that is one of the kind of key arguments for the kind of affirmative of this,
[855.38 → 859.54] that we are in an AI bubble is this kind of valuations and speculation.
[859.54 → 865.76] I mean, we've highlighted a few stories over time, the last couple of years of these crazy
[865.76 → 870.84] valuations where essentially there is an unproven revenue model.
[871.52 → 879.00] So I'm looking at, at one source here that's, that's saying over 50% of VC funding in, in
[879.00 → 888.42] Q2 of this year, 2025, went into AI companies and there's, you know, VC is, is risky, of course,
[888.42 → 892.96] as, as an investment model, most of those businesses will fail.
[892.96 → 898.50] That's kind of always expected in, in the AI space, but also this year, just from looking
[898.50 → 903.60] around at different folks, you know, raising these companies are getting much, much higher
[903.60 → 906.82] multiples or higher valuations.
[906.82 → 914.00] So for people that, that need a reminder, sometimes your, your company might receive a valuation
[914.00 → 917.68] that's a certain multiple of the revenue that you're bringing in.
[917.82 → 926.82] And so that, that may, might be 15, 20, 25 X, 30 X for, you know, plus for an AI company
[926.82 → 933.38] where other companies kind of your normal run-of-the-mill SaaS company in tech that's
[933.38 → 938.56] raising is definitely not raising at those multiples, um, right, right now.
[938.56 → 944.50] So that, that would be, I guess the argument or an argument for that affirmative is these
[944.50 → 951.44] kind of, uh, speculation and valuation that's maybe reminiscent of that.com era.
[951.86 → 952.00] Yeah.
[952.00 → 957.36] By the way, another term just to connect kind of that financial world with, with, you know,
[957.40 → 962.58] what we're talking about in terms of observations is, um, those of you invest, some of you may
[962.58 → 972.08] have heard, uh, the notion of a beta, uh, which is, um, essentially a, a multiple of valuation
[972.08 → 973.48] against your earnings.
[973.48 → 980.06] And so if you have a very high beta, that's saying you're being valued very high against what
[980.06 → 985.10] your actual real life earnings are and a lower beta, which would be considered less risky
[985.10 → 989.12] would be, um, that that valuation is not so extravagant.
[989.12 → 993.70] And so I guess, and that's another way of, of looking at this is if you're looking at a
[993.70 → 1000.08] company's, um, you know, portfolio analysis, you know, that some analyst is doing, um, and
[1000.08 → 1004.90] there might be a beta number attached if you're, is that, and this was pointed out in some of
[1004.90 → 1011.14] the articles is that the betas of today while high are not nearly as high as the betas of
[1011.14 → 1012.04] the.com era.
[1012.52 → 1015.22] Um, and so, you know, that's another sign.
[1015.58 → 1022.08] Well, you know, is there some bubble maybe, uh, is it as bad in terms of the sheer speculation
[1022.08 → 1023.38] of the.com era?
[1023.62 → 1027.96] Maybe not, you know, as that's one metric by which we can evaluate.
[1027.96 → 1047.76] Well, friends, it is time to let go of the old way of exploring your data.
[1048.02 → 1051.32] It's holding you back, but what exactly is the old way?
[1051.64 → 1056.96] Well, I'm here with Mark Duppy, co-founder and CEO of FBI, a collaborative analytics platform
[1056.96 → 1058.58] designed to help big explorers like yourself.
[1058.82 → 1060.90] So Mark, tell me about this old way.
[1061.38 → 1066.40] So the old way, Adam, if you're a product manager or a founder, and you're trying to get
[1066.40 → 1070.58] insights from your data, you're, you're wrestling with your Postgres instance or Snowflake or
[1070.58 → 1075.22] your spreadsheets, or if you are, and you don't maybe even have the support of a data analyst
[1075.22 → 1077.40] or data scientist to, to help you with that word.
[1077.40 → 1083.24] Or if you are, for example, a data scientist or engineer or analyst, you're wrestling with
[1083.24 → 1086.68] a bunch of different tools, local Jupyter notebooks, Google co-lab.
[1086.68 → 1091.22] Or even your legacy BI to try to build these dashboards that, you know, someone may or may
[1091.22 → 1092.50] not go and look at.
[1092.50 → 1098.24] And in this new way that we're building at FBI, we are creating this all-in-one environment
[1098.24 → 1103.18] where product managers and founders can very quickly go and explore data regardless of
[1103.18 → 1103.84] where it is, right?
[1103.88 → 1106.88] So it can be in a spreadsheet, it can be in Airtable, it can be in Postgres, Snowflake.
[1107.06 → 1112.08] Really easy to do everything from an ad hoc analysis to much more advanced analysis if,
[1112.26 → 1113.56] again, you're more experienced.
[1113.56 → 1118.98] So with Python built in, you know, Python built in right there in our AI assistant, you
[1118.98 → 1121.14] can move very quickly through advanced analysis.
[1121.72 → 1127.06] And a really cool part is that you can go from ad hoc analysis and data science to publishing
[1127.06 → 1133.50] these as interactive data apps and dashboards, or better yet, at delivering insights as automated
[1133.50 → 1139.28] workflows to meet your stakeholders where they are in, say, Slack or email or spreadsheets.
[1139.28 → 1142.54] So, you know, if this is something that you're experiencing, if you're a founder or product
[1142.54 → 1146.66] manager trying to get more from your data or for your data team today, you're just underwater
[1146.66 → 1151.42] and feel like you're wrestling with your legacy, you know, BI tools and notebooks, come check
[1151.42 → 1152.80] out the new way and come try out FBI.
[1153.16 → 1153.68] There you go.
[1153.84 → 1157.16] Well, friends, if you're trying to get more insights from your data, stop resting with it,
[1157.50 → 1160.12] start exploring it the new way with FBI.
[1160.42 → 1163.42] Learn more and get started for free at fabi.ai.
[1163.68 → 1166.72] That's F-A-B-I dot A-I.
[1166.72 → 1169.12] Again, fabi.ai.
[1169.28 → 1178.88] Yeah, Chris, I think you were starting to get into maybe something we've alluded to,
[1178.98 → 1186.28] which is the other side, the negative side of saying, you know, we're not in a bubble
[1186.28 → 1192.84] corresponding to this first argument of the speculative investing, which is that, you know,
[1192.84 → 1199.24] maybe the earnings or the kind of business fundamentals or the scale is, you know, the diversification
[1199.24 → 1206.40] is a bit stronger in this particular time than in the dot-com time.
[1206.40 → 1214.10] So, you know, on the one side, Jerome Powell talking about real earnings, right, which is maybe
[1214.10 → 1216.60] different from some of the dot-com era.
[1216.60 → 1227.08] On the other side, there does seem to be a diversified set of revenue streams in the AI space.
[1227.08 → 1230.56] So it's not just AI models, for example.
[1231.20 → 1233.42] There's infrastructure related to this.
[1233.42 → 1240.08] There's chips, right, GPUs and even like unique types of chips that are being developed for AI.
[1240.38 → 1243.68] There's service offerings on top of AI.
[1243.68 → 1253.36] We've talked a lot on this show about how the service providers, the large consultancies are doing quite well in the AI space.
[1253.96 → 1261.42] And those things are things that are already scaling, whether that's chipping or the service offerings, etc.,
[1261.42 → 1264.08] cloud offerings around these things.
[1264.08 → 1269.80] And I guess this is something I wasn't aware of, and maybe it's connected to what you were talking about before.
[1269.80 → 1285.94] But this is the magnitude of the investment relative to kind of the GDP is still relatively low compared to other kind of if you want to think back to actual, you know,
[1285.94 → 1293.10] other transformative revolutions like railroads or electrification and that sort of thing.
[1293.10 → 1306.98] So this kind of counterargument would be, no, there 's's really something more here in terms of the earnings and business fundamentals with a lot of these AI companies where there are earnings, there's diversification.
[1307.38 → 1310.82] And the magnitude of the investment is kind of different.
[1310.82 → 1317.90] I think I agree with that, though, once again, on kind of on the other, if you're countering that just a little bit,
[1317.90 → 1327.78] then I think that you're going to find that there is a selection of companies that absolutely fit that that profile that you just outlined and stuff.
[1327.78 → 1335.26] But I think that there's still also quite a few out there to balance that have no earnings and stuff like, you know, are very little.
[1335.78 → 1344.86] And that the business model is still quite questionable and thus leading into kind of that hype based speculation and stuff.
[1344.92 → 1349.22] So I think I definitely feel like we're seeing both sides of that.
[1349.22 → 1363.20] And it kind of comes back to something I mentioned at the beginning of the call of like, you know, the the the bubble less good nature for if we're is we're is we're in that kind of dot com Internet period as an event,
[1363.32 → 1367.72] you know, like as our contextual reference that it doesn't quite fit that.
[1367.72 → 1373.56] And it's it seems to be very much in like how you're engaged and what you're you know what your idea is.
[1373.60 → 1380.90] Do you have customers? Are you providing services and thus have earnings that that support that versus the ones that are not?
[1380.98 → 1389.12] And I think, you know, we've spent so much time on the show over the years really trying to cut through the hype cycle.
[1390.06 → 1396.68] Sometimes quite literally, you know, we'll get it will get the current year published hype cycle and start talking about some of that.
[1396.68 → 1405.44] And I think if you're deeply engaged as we and our listeners and the people who listen to the show regularly are, it's probably easier to do that.
[1405.44 → 1414.16] But I also think that there are probably a lot of folks out there that are doing investing that don't have that don't have as much, you know, knowledge of that.
[1414.60 → 1421.96] I had a conversation earlier today with someone who was that person and was kind of asking about some stuff.
[1422.06 → 1424.86] And I was kind of doing a little bit of mentoring, maybe.
[1424.86 → 1431.60] But I realized just, you know, that there are a lot of people out there that still really don't know much about it.
[1431.66 → 1435.58] And all they hear is the hype and they have very little ability to get through it.
[1435.58 → 1449.56] So, you know, is if they're looking to invest, it's almost a little bit of a flip of the coin on whether they look into the profile that you were just describing or that other one where it's a little bit less substantial.
[1449.56 → 1453.56] Yeah, I think it's definitely, definitely good points.
[1453.56 → 1475.20] I think part of the reason here that things are hard to parse through, which we've also talked about on the show, is just that it's kind of hard to pin down at this point what AI means and what is part what is actually part of what would be considered the bubble and what is not.
[1475.20 → 1482.52] Part of that is there are a lot of companies that are trying to ride the hype cycle.
[1483.00 → 1489.16] And their product really is not AI powered at all, but they feel the pressure to tack on.
[1489.74 → 1491.14] This is an AI powered thing.
[1491.40 → 1496.20] Maybe they have a, you know, a linear regression model or even a rules based thing.
[1496.20 → 1500.32] And this say this is AI, and they're riding that hype cycle.
[1500.32 → 1520.78] And so on the one side, they're kind of riding that on the other side, there's, you know, very sophisticated, whatever, you know, computer vision systems and other things that maybe are not viewed as part of the AI hype cycle because they're not generative AI or something like that.
[1521.32 → 1524.58] And so it's its kind of hard to tell what fits there.
[1524.58 → 1536.86] And in addition, no one really knows kind of at the application layer what the kind of end highest value things that are going to come out of the AI world are going to be.
[1537.10 → 1539.30] I, you know, we've talked about this on the show.
[1539.38 → 1542.16] I certainly don't think it's a general chat interface.
[1542.50 → 1548.72] There's much more valuable things already in terms of some of the agentic and verticalized things.
[1548.72 → 1568.18] And so there's a lot of just diversification, both in terms of people trying to ride the wave, but also in terms of defining what is AI and what is not, because it could range from a chip producer that's making a unique chip that is specialized for AI workloads,
[1568.18 → 1587.02] all the way to a very thin wrapper on top of the open AI API to a proprietary computer vision model that's taken 20 years to develop to a SaaS platform that has actually no AI component,
[1587.24 → 1590.68] but is labelled AI because if they can sell it for more money.
[1590.68 → 1594.98] Right. So maybe that all of that just feeds into this bubble.
[1595.20 → 1603.80] But also, I think it creates a lot of a lot of confusion, which may maybe is not, I guess, in thinking about it, it's not.
[1604.54 → 1609.50] It is similar to that dot com era because it's like everything related to the web.
[1609.50 → 1616.98] Right. And you did have servers, you did have hardware, you did have kind of websites or platforms and that sort of thing.
[1617.40 → 1624.54] Yeah. I mean, even then, people were buying hardware and platforms and software and, you know, left and right, you know, during that period.
[1624.72 → 1636.86] But again, the kind of the winners out of that dot com era was a fairly small group of companies, you know, that were that that were feeding the the the purchase frenzy during that.
[1636.86 → 1646.64] And I think that is a that is a similarity we have to today where you have a small group of companies that are providing a lot of capability and stuff.
[1646.64 → 1665.22] I think, you know, when it comes to the others, you know, in that like you just identified, you know, with the A.I. label being so marketable and yet having almost no meaning because of the immense diversity of possibilities that you could apply A.I. labelling to.
[1665.22 → 1688.22] It really comes down to solving business problems that are real business problems as opposed to trying to put an A.I. thing out there, you know, and I think I know that the the and me in our roles hosting the podcast here, we get pitched by a lot of companies, a lot.
[1688.22 → 1695.62] A lot. And so we see a lot of a lot of different, you know, positions and possibilities out there.
[1695.62 → 1715.90] And I think, you know, if you look at that, probably the ones that really catch our attention are the ones that aren't the most Grammy A.I. things necessarily in terms of how they're marketing, but where you can really see that they're using these technologies to solve business problems in novel ways that hadn't been addressed before.
[1715.90 → 1722.96] And I think, you know, that's probably, you know, the basis for our own way of doing these evaluations.
[1723.40 → 1736.28] I wonder, you know, how the general population who is not just living and breathing A.I. every minute of every day, how they're looking at some of these different things that are coming at them in every advertisement and marketing effort.
[1736.28 → 1739.18] You know, how do they how do they tell the difference?
[1739.32 → 1743.90] You know, I think that has a lot to do with bubbles as well.
[1743.96 → 1754.52] It's just that inability to understand the difference between a great investment and something that is really, really sketchy and risky and not being able to tell the difference between the two.
[1755.08 → 1758.34] Yeah. Just anecdotally, it kind of has gone.
[1758.34 → 1766.08] I remember I don't know if you had this similar experience, Chris, but obviously we've been doing this show for quite some time.
[1766.08 → 1771.46] We talk about A.I. here for the most of the time of this podcast.
[1771.46 → 1781.92] We didn't really talk about A.I. or A.I. was not a kind of topic of general, you know, general discussion and was not represented kind of.
[1781.92 → 1787.72] I don't know, in the environments in which you walk through day-to-day like an airport or something.
[1787.86 → 1793.30] I remember seeing the first I think it was an anthropic ad when I was in.
[1794.02 → 1797.42] I forget what airport it was, an airport in Europe somewhere.
[1797.98 → 1801.78] And I and I saw an anthropic ad, and I was like, whoa, there's an A.I.
[1801.84 → 1804.46] And, you know, I don't live in I don't live in San Francisco.
[1804.62 → 1806.34] You go like San Francisco is different.
[1806.44 → 1807.26] You go to San Francisco.
[1807.26 → 1816.86] It's all like on the billboard is advanced monitoring for your Kubernetes cluster billboard, which, you know, wouldn't work anywhere else in the U.S.
[1817.02 → 1822.76] But outside of San Francisco, it's like you don't you don't see that sort of thing.
[1822.76 → 1826.42] Right. And so I thought, oh, man, like this is crazy now.
[1826.54 → 1830.32] And that was in like a major airport in some hub in Europe.
[1830.32 → 1832.72] And I'm like, OK, well, that makes sense.
[1832.72 → 1849.22] But I just got back from a trip this morning and I as I was walking through the Indianapolis airport, there were multiple billboards and banners that I saw that all had some A.I. slant related to a product or service.
[1849.22 → 1851.46] So it's pervasive now.
[1851.46 → 1855.60] And it is kind of the soup that that we live in.
[1855.60 → 1863.36] It is, you know, so like, you know, as we are trying to navigate that world, I think it's funny.
[1863.52 → 1865.60] You know, you mentioned how long we've been doing this.
[1865.60 → 1876.38] And a lot of our listeners that have been with us for years going through this evolution with us are probably seeing similar takes on this and that they're they're watching it.
[1876.38 → 1893.68] But I've also I've also I've also come to realize that there's still quite a massive segment of our general population that is only in these last few months really becoming aware of this stuff and are still trying to take it in early on.
[1893.68 → 1904.92] And so they are suddenly I mentioned that conversation I had earlier today and that individual said this A.I. thing seemed to have come out of nowhere.
[1904.92 → 1909.70] And, you know, that's about as far from my experience as you could possibly be.
[1909.70 → 1913.12] But I made me realize that that's that's quite common.
[1913.12 → 1921.40] And more recently, I mentioned, you know, that that my mom in her mid 80s was now talking about A.I. and stuff.
[1921.52 → 1923.10] So times are changing quickly.
[1923.68 → 1940.64] What if A.I. agents could work together just like developers do?
[1940.64 → 1944.42] That's exactly what agency is making possible.
[1944.94 → 1946.82] Spelled A.G.N. T.C.Y.
[1946.94 → 1953.62] Agency is now an open source collective under the Linux Foundation building the Internet of agents.
[1953.68 → 1963.16] This is a global collaboration layer where the A.I. agents can discover each other, connect and execute multi-agent workflows across any framework.
[1963.16 → 1979.08] Everything engineers need to build and deploy multi-agent software is now available to anyone building on agency, including trusted identity and access management, open standards for agent discovery, agent to agent communication protocols and modular pieces.
[1979.08 → 1981.88] You can remix for scalable systems.
[1981.88 → 1993.18] This is a true collaboration from Cisco, Dell, Google Cloud, Red Hat, Oracle and more than 75 other companies all contributing to the next gen A.I. stack.
[1993.18 → 1996.32] The code, the code, the specs, the services, they're dropping.
[1996.48 → 1997.42] No strings attached.
[1997.66 → 1999.50] Visit agency.org.
[1999.58 → 2000.62] That's A.G.N.
[2000.62 → 2001.62] T.C.Y.
[2001.62 → 2004.14] dot org to learn more and get involved.
[2004.14 → 2005.74] Again, that's agency.
[2005.74 → 2006.58] A.G.N.
[2006.58 → 2008.30] T.C.Y.
[2008.30 → 2009.26] dot org.
[2013.82 → 2032.50] Well, Chris, I think one, if we just kind of bring out another argument here that people are making at this time, and I'm curious to know actually your opinion on this, we might as well give some of our own opinions or else what else are we doing here?
[2032.50 → 2034.30] That seems like fun.
[2034.30 → 2053.98] But one of the arguments for the fact that we are not in an A.I. bubble is that the kind of rationale, the structural and economic rationale for A.I. deployment is much deeper than previous bubbles.
[2053.98 → 2058.02] I think the hyperbolic example would be like crypto, maybe.
[2058.68 → 2079.06] But the fact that A.I. is already being integrated into enterprise workflows, into even manufacturing and healthcare, it's not just kind of technology that is looking for an application, an interesting technology that's looking for an application.
[2079.06 → 2083.26] But it is actually being applied across a variety of industries.
[2083.26 → 2101.86] The second piece of this would be kind of the tie of A.I. to a very long lead up of scientific research and deep roots that have been going on since the 60s, 70s, 80s and on.
[2101.86 → 2115.36] And had all of these things leading up to it, which gives it kind of roots in kind of rigorous science and mathematics and that sort of thing.
[2115.36 → 2122.04] The technology didn't kind of come out of nowhere, similar to kind of the revolution of electrification.
[2122.70 → 2122.84] Right.
[2123.28 → 2128.58] People had actually been studying these topics or at least thinking about them for centuries.
[2128.58 → 2129.30] Right.
[2129.64 → 2135.84] Thinking about these phenomena, even though maybe they weren't fully understood.
[2135.84 → 2142.74] And then kind of there were breakthroughs that created this electrification of the world.
[2142.74 → 2143.30] Right.
[2143.52 → 2144.00] Totally.
[2144.56 → 2163.34] You know, one of the things to your point right there that actually gives me a little bit of confidence, maybe that we're not in a classic bubble, at least in the dot com context, is the fact that the fundamental underlying algorithmic technology that we're looking at here today.
[2163.34 → 2172.22] And 2025, as we do the show is actually about 40 years old is the basis being neural networks.
[2172.22 → 2180.44] And while we don't use that phrase as much as we used to anymore, you know, we call everything A.I. these days.
[2180.44 → 2197.58] But fundamentally, the A.I. that is powering everything that is of significant value of today is fundamentally neural networks that have been enhanced and embellished and designed further and, you know, next iteration, that kind of thing.
[2197.58 → 2205.00] And so we're building on a 40-year history of this particular line of algorithmic technology.
[2205.60 → 2217.70] And so, you know, that that's a great point you raised there a second ago, that this is not fly by night, that there has been a, you know, the majority for me, you know, the majority of my lifetime.
[2217.70 → 2232.24] This has been around for listeners just as a two-second thing for listeners who may not have followed the show for years, because I know I've mentioned this before, but my parents were working on neural networks back in the early 90s.
[2232.24 → 2238.62] And so like and that's actually was my first exposure to this when I was in college.
[2238.62 → 2241.64] And so this is not new stuff.
[2241.72 → 2242.80] It's evolved.
[2243.00 → 2253.04] And I think the biggest piece of it is you've had you've had NVIDIA's come about able to make GPUs that could support the continuing evolution of the technology.
[2253.20 → 2259.42] It is thoroughly embedded in a bunch of industries and some implement like anything.
[2259.54 → 2261.48] Some implementations are better than others.
[2261.48 → 2264.32] But yeah, great point you're making in terms of that.
[2264.40 → 2271.26] This is not a solution in search of a grounding or in search of an an a market to use it.
[2271.86 → 2272.26] Yeah, yeah.
[2272.26 → 2280.72] And I also tend to agree now, of course, I'm biased on this show and maybe my bias is not that surprising.
[2281.38 → 2289.92] I think some of the valuations and the way people are treating investment in this area is crazy.
[2289.92 → 2292.98] Not to say that you can't invest in prediction guard.
[2293.70 → 2296.34] Uh, uh, and I'll talk to you.
[2296.46 → 2301.78] But, uh, but I do think that generally like there have been many examples of craziness there.
[2301.94 → 2307.36] At the same time, I think that those crazy investments.
[2307.36 → 2328.54] Are partially founded maybe not in kind of the earnings or like a proven business model, but in a kind of deeper understanding that this technology is actually shifting how work is done and is fundamentally transformative for many industries.
[2328.54 → 2331.38] And that actually is going to happen.
[2331.38 → 2336.74] And so it's not it's maybe speculative in a certain way.
[2336.74 → 2347.24] But I think there are real kinds of foundations to that speculation that, um, that I don't know, I would almost, uh, I would almost use the metaphor.
[2347.24 → 2354.14] It's kind of like when people go out and look for gold or, or oil, right?
[2354.28 → 2363.42] The concept of gold or oil is known, and it's known that there is value if you get this material out of the out of the ground.
[2363.42 → 2363.74] Right.
[2363.74 → 2369.42] But there's speculation and risk in trying to figure out where that is here.
[2370.34 → 2377.36] It's not like you're trying to discover a new precious metal or a new thing that's not known to anyone.
[2377.36 → 2377.64] Right.
[2377.66 → 2378.76] You know, this thing exists.
[2378.76 → 2380.40] It's a matter of, of finding it.
[2380.40 → 2385.78] And certainly many people lose a lot of money in, in that, uh, speculation here.
[2385.78 → 2386.60] It's, it's similar.
[2386.82 → 2393.04] There is a kind of known, uh, or, or there is at least a feeling and an intuition.
[2393.04 → 2401.92] That there will be very transformative companies that will be long-lasting and this technology will be long-lasting, and it will be impactful.
[2402.34 → 2406.18] Um, it's not that that that's maybe doubted.
[2406.18 → 2417.88] Um, but the crazy valuations are in some cases are driven by that because, you know, who knows going, who's going to, to survive this, this AI craziness.
[2417.88 → 2423.98] But, but the technology, it seems will be kind of pervasive and long-lasting and transformative.
[2424.18 → 2425.14] I think so.
[2425.20 → 2430.72] I think, uh, I'll throw, I'm going to throw a wild card into the, into the mix here, uh, for a moment.
[2430.72 → 2436.68] And, um, one of the I think the things that no one really knows where things are going for sure.
[2436.68 → 2454.62] And we sure talk about it a lot is the fact that at this point you have a lot of, um, of companies, especially some very large companies such as Amazon, uh, who, uh, are doing massive layoffs, you know, and they're doing that on the notion.
[2454.62 → 2458.48] Uh, in Amazon's case, 14,000 middle managers.
[2458.78 → 2476.26] Um, and that's just one, that's just one organization, one very large organization, but one, um, and this is happening in a lot of places is that, you know, we're definitely seeing the replacement efforts by companies to use technology to replace, uh, humans in that.
[2476.26 → 2481.40] And, and this has been something we've talked about for years, you know, certainly coming and that would be happening.
[2481.40 → 2488.90] And, you know, where would the balance be between a synergy between AI and humans and a competition between AI and humans?
[2488.90 → 2500.16] And so we've had many conversations over the years about this, but, um, you know, we're definitely at that point right now where, uh, a lot of companies are beginning to bet on AI technologies.
[2500.16 → 2513.06] Um, but it's also happening at a time when, as we talked about some of those ROIs on different, uh, efforts are not, are not yielding, you know, meaningful results.
[2513.06 → 2525.00] And so aside from what happens with that, when you have, uh, unemployment rising from AI, uh, induced layoffs, um, that will affect the economy too.
[2525.00 → 2546.58] So there's, it's not just whether the investment in these particular companies is, uh, is, is wise or speculative and, you know, based on their fundamentals, uh, and their earnings, but also, you know, uh, as, as we have groups of folks in the economy being laid off, um, and therefore their purchasing power is reduced.
[2546.58 → 2547.94] How does that play back in?
[2547.94 → 2563.84] And I've seen a lot in the news about like all of this together, not only the ROI and, and speculative nature or lack or, you know, whether it's a bubble or not going back to our, our kind of original phraseology, but also whether this is going to affect workplaces.
[2563.84 → 2566.34] So it's, it is quite a complex thing.
[2566.34 → 2575.66] And when we look back on.com, it seemed, uh, there were complexities there, but I think the, the raw speculation of that era made the bubble.
[2575.66 → 2587.34] It was a little bit more of a black and white thing as you looked back on it, you know, historically, um, after we had lived through it and looked back and kind of said, well, yeah, you know, I guess with 2020 hindsight, we can see that coming.
[2587.58 → 2601.30] As we've noted here, um, it kind of depends on who you are, uh, and how you're doing and what you're claiming is your AI and whether you're solving a real business problem, uh, on whether you're in that bubble group or not in a bubble group.
[2601.30 → 2612.76] So as we see the mixture, uh, pouring through the economy, it will be, uh, definitely interesting to see how this plays out, uh, in the, in the weeks, months and years ahead here.
[2612.76 → 2632.76] Do you think that, because we also talked recently on the show about almost the, the both cognitive and emotional, you know, change and shift or even manipulation that some of these, these systems are doing, you know, um, across the population.
[2632.76 → 2655.06] If you look at it, there's people having, you know, romantic relationships with AI systems or, you know, using these systems maybe for therapeutic purposes rather than their therapist and, uh, cognitive load of work is changing because you're, you know, vibe coding and, and all of these things.
[2655.06 → 2670.00] So do you think that that sort of cognitive and emotional, almost like lifestyle shift is more impactful with this technology or, or with something like the.com era and people kind of all, all coming online?
[2670.70 → 2683.46] You know, dot com era, uh, was, uh, and, and sadly I was well into adulthood, you know, as we hit that, you know, uh, you know, for those who don't realize that I'm, I'm getting, uh, a little bit older than I like to imagine.
[2683.46 → 2693.04] But like fundamentally we went through the bus because of all the speculation, but eventually everything kind of, you know, we, we did realize what it was going at.
[2693.12 → 2703.40] It just wasn't on a timeline and the and what you could achieve in that short of time, given the valuations just wasn't real, but it was real in the long-term.
[2703.40 → 2712.96] And I think here, what we're seeing is something a little bit different in that, um, you weren't having relationships with your, with your ISP at the time.
[2713.06 → 2718.80] You know, it wasn't that kind of relationship, uh, that you had with that wave of technological innovation.
[2719.10 → 2721.54] This one, it's, it's a little bit worrisome.
[2721.88 → 2726.06] Um, like I, I don't believe in vibe coding being a great strategy personally.
[2726.06 → 2745.10] I think that thinking of AI as a pair programming partner is a much sounder way of approaching it in terms of turning out, continuing to turn out very good software products, um, that you understand and that you can maintain over time and that you have humans that, that understand how their business is working.
[2745.26 → 2754.54] So I'm a little, uh, pure vibe coding where someone who doesn't really know what they're doing is just asking the system, and then they end up with something, you know, so it kind of depends on what you're doing with it.
[2754.54 → 2767.02] I see there's also been some research, and we may have an episode coming up on it, uh, that was done recently about the human dependence on AI causing basically degradation.
[2767.02 → 2781.38] Like they were measuring, uh, brain activity and, and P and, uh, the subjects that were in this, uh, study that were using, uh, their AI for everything were showing decreased brain capability, um, over time.
[2781.38 → 2795.88] And so like, it worries me that we're giving up some of what makes us so wonderfully human at the same time that maybe we're creating a strong dependence that we have in these ways that didn't exist in previous revolutions.
[2795.88 → 2808.80] So I think, I think that there's a real risk here of, I think how you, how you use AI capabilities today makes a difference on what your own personal human future is going to be.
[2808.80 → 2821.48] And I very specifically, uh, choose how I use AI capabilities, uh, in a way that enables me versus, uh, kind of, uh, creates a crutch for me.
[2821.72 → 2826.08] So, uh, that's, that's kind of how I would answer that's a little bit roundabout way of answering that.
[2826.44 → 2834.60] But I think the way you use AI has a lot to do with this long-term effect on, on your, your own personal life in a as an individual.
[2834.60 → 2846.80] Makes sense. Yeah. I think that's a that's a great way to look at it. Um, well, as, as we close out here, Chris, what would you say? Are we in an AI bubble or not? What's your, what's your vote? Yes or no?
[2846.80 → 2857.28] I'm going to say no in the classic bubble analogy, I think. And, and I, I came into this conversation not really knowing, uh, I think it's this, us talking it through.
[2857.44 → 2866.64] So I would say no in the classic bubble context, like.com bubble, but yes. And that there might be, instead of one big bubble, there might be lots of little bubbles.
[2866.64 → 2874.56] Uh, yeah. Uh, fizzy, like our, uh, like our PIB zero and, and Coke zero that we, that we started talking about.
[2874.76 → 2878.34] The fizzy. Yeah, there you go. The fizzy economy. You heard it here first, folks.
[2878.34 → 2899.12] The fizzy AI soup on my end. I would tend to go with the, the no, I, I, I definitely think that compared to some other technologies and cycles, this is already kind of at a level of utility and, and permeating many, many, uh, enterprises and that sort of thing.
[2899.12 → 2912.08] And I do think that creates a trickle down of things that we will have to deal with and learn how to cope with, you know, workforce wise and emotionally and otherwise, but yeah, I'll, I'll go with no as well.
[2912.08 → 2917.98] So, so you heard it here. Um, New York Times, you can quote us if you like, we are not in an AI bubble.
[2918.30 → 2919.44] Cause Dan and Chris said so.
[2919.44 → 2922.54] I'm glad that I'm glad that we put that one to rest, Chris.
[2922.78 → 2926.38] Yeah. Well, there we go. Solving world problems. One episode at a time.
[2926.38 → 2933.94] Well, um, I guess until next time we can, we can solve the next world crisis in, in the next episode, Chris. Thanks for chatting.
[2934.46 → 2936.24] Absolutely. Talk to you next time.
[2943.34 → 2945.58] All right. That's our show for this week.
[2945.58 → 2952.92] If you haven't checked out our website, head to practical AI.fm and be sure to connect with us on LinkedIn X or blue sky.
[2952.92 → 2958.84] You'll see us posting insights related to the latest AI developments, and we would love for you to join the conversation.
[2959.16 → 2963.12] Thanks to our partner prediction guard for providing operational support for the show.
[2963.46 → 2965.44] Check them out at prediction guard.com.
[2965.84 → 2969.48] Also thanks to break master cylinder for the beats and to you for listening.
[2969.74 → 2972.66] That's all for now, but you'll hear from us again next week.
[2972.66 → 2980.88] Thanks for reading this week.
[2980.90 → 2981.00] Look over the event этом area.
[2981.00 → 2985.08] Check out what we find when questions are the best of these services.
[2985.30 → 2990.06] Take care for information that we can check out with us all right now, love us and see you next time.
