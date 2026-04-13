[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.76] Head to linode.com slash Changelog.
[17.38 → 22.28] Do not underestimate the power of the independent open cloud for developers.
[22.50 → 24.58] Yes, I'm talking about Linde.
[24.86 → 29.38] Linde is our cloud of choice, and it's the home of Changelog.com.
[29.38 → 34.32] What we love most about Linde is their independence and their commitment to open cloud.
[34.74 → 39.92] Open cloud means being unencumbered by outside investment and maximizing value for the community,
[40.28 → 41.12] not shareholders.
[41.54 → 43.16] And that's exactly what Linde represents.
[43.56 → 44.56] No vendor lock-in.
[44.92 → 46.32] Open at every layer.
[46.74 → 49.24] If you want to learn more, head to linode.com slash open.
[49.50 → 51.86] Again, linode.com slash open.
[59.38 → 68.50] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[68.88 → 69.84] and accessible to everyone.
[70.28 → 74.22] This is where conversations around AI, machine learning, and data science happen.
[74.66 → 79.24] Join the community and Slack with us around various topics of the show at Changelog.com slash community
[79.24 → 80.60] and follow us on Twitter.
[80.74 → 82.36] We're at Practical AI FM.
[82.76 → 83.04] Okay.
[83.04 → 84.08] Here's Daniel and Chris.
[88.12 → 91.18] Welcome to another episode of the Practical AI podcast.
[91.72 → 92.72] My name is Chris Benson.
[92.86 → 95.00] I'm Principal AI Strategist at Lockheed Martin.
[95.20 → 100.48] And with me as is always my co-host, Daniel Whiten ack, who is a data scientist with SIL International.
[100.84 → 101.64] How's it going today, Daniel?
[102.20 → 103.48] It's going pretty good.
[103.60 → 105.58] It's been a busy day of recordings.
[105.94 → 108.52] We were just talking about this before the episode started.
[108.52 → 113.52] I just shoved a bunch of cashews in my mouth as a snack, and I think you had some breakfast
[113.52 → 115.54] troubles in between episodes.
[116.04 → 117.46] Yeah, I had not had breakfast.
[117.66 → 119.54] And so in the last few minutes, I went to get breakfast.
[119.54 → 122.94] And as I was putting it together, I have multiple dogs.
[123.02 → 124.12] One of my dogs did something.
[124.22 → 126.20] I think it was an organized thing.
[126.30 → 129.80] One dog was trying to pull me to the side while the other dogs went and got my breakfast.
[130.26 → 132.84] So I'm going to sit here, and we're going to do this podcast hungry.
[132.94 → 133.38] That's right.
[133.82 → 134.60] You know what?
[134.66 → 136.32] We persevere no matter what.
[136.48 → 136.92] We handle it.
[136.92 → 137.52] Practical AI.
[137.52 → 137.82] Okay.
[138.08 → 140.70] These are the sacrifices we make for practical AI.
[140.90 → 141.46] That's right.
[141.54 → 142.00] That's right.
[142.04 → 143.28] We're hardcore podcasters.
[143.68 → 145.36] So, you know, it's interesting.
[145.66 → 151.20] I got to say, I know you live up north, but I'm about to head out today for the Denver,
[151.34 → 155.22] Colorado area, Littleton, where Lockheed Martin has part of its space division.
[155.58 → 160.22] And I looked at the weather for packing, and it's like, it's going down to like zero degrees
[160.22 → 160.60] Fahrenheit.
[160.98 → 163.72] And for listeners who don't know, I'm from Georgia.
[163.92 → 166.02] I'm a Southern boy, used to warm weather.
[166.02 → 171.02] I'm quite frightened to get on this plane and go to this place with such frigid temperatures
[171.02 → 171.30] coming.
[171.70 → 171.98] Yeah.
[172.16 → 172.38] Yeah.
[172.80 → 175.98] I'm being tough in two ways, both with the dogs and with the weather.
[176.14 → 176.68] I'm just saying.
[177.04 → 177.98] You're levelled up.
[178.26 → 178.80] There you go.
[178.88 → 179.48] I'm ready to go.
[179.64 → 180.00] Okay.
[180.14 → 183.84] Well, you know, we have a pretty interesting episode coming up here.
[183.94 → 185.08] It's going to be a little bit different.
[185.28 → 185.64] Hopefully.
[186.00 → 186.60] I think so.
[186.60 → 191.36] From what our listeners usually hear, typically we'll have either a guest on to talk about
[191.36 → 195.48] what the guest is involved in, or you and I will do what we call our fully connected episodes,
[195.48 → 198.70] where we will talk about a topic between the two of us.
[198.74 → 201.10] And we're doing a little bit of a blend of those today.
[201.10 → 205.18] So, we're going to address AI with local languages.
[205.84 → 210.90] And today, instead of strictly being the host, you're here representing SIL International,
[211.32 → 213.94] which is a nonprofit in local languages.
[214.42 → 217.74] I'm allowed to speak more than just questions this episode.
[218.06 → 220.62] You're allowed to speak more than just questions on this episode.
[220.82 → 225.80] And also with us today, we have Dan Jeffries, who is the chief technical evangelist at Pachyderm.
[226.00 → 226.64] Welcome, Dan.
[226.70 → 227.10] How's it going?
[227.64 → 228.58] It's going wonderfully.
[228.70 → 229.76] Thanks for having me on the show.
[229.76 → 230.54] No worries.
[230.68 → 234.40] And for listeners up front, I'm going to try to go with, for Daniel Whiten ack, we're going
[234.40 → 235.62] to say Dan W.
[235.84 → 238.44] And for Daniel Jeffries, we're going to say Dan J.
[238.62 → 241.36] So, it'll be a little bit different since we're broken out with Dan's today.
[241.72 → 248.36] Yeah, I suggested that Dan J go with Pachyderm Dan, but he informed me that he's not completely
[248.36 → 249.86] defined by his employer.
[250.08 → 250.84] Oh, my gosh.
[250.84 → 252.04] Which I guess I understand.
[252.54 → 254.56] Oh, and you've now put that out on this recording.
[254.74 → 255.76] I can't believe that.
[255.76 → 262.54] Well, Dan W. wanted to be fully defined by his employer and says that he has no other
[262.54 → 264.04] outside interests whatsoever.
[264.54 → 269.20] So, I don't know if that's a direct quote, but I'll let it slide through.
[269.20 → 270.36] Okay, boys.
[270.72 → 271.04] Okay.
[271.04 → 272.76] Let's get back in our corners now.
[272.94 → 273.28] Okay.
[273.52 → 275.92] We have a conversation to dive into here.
[276.18 → 280.08] I'm going to actually start for a second with Daniel Whiten ack, whom our listeners probably
[280.08 → 284.72] know pretty well, but they know you mostly on the practical AI host side.
[284.84 → 289.46] And I'd like you to take a moment and talk about SIL International and what you do there.
[289.54 → 292.20] And then we're going to flip over to Dan J in a moment.
[292.54 → 293.32] Sure, definitely.
[293.32 → 293.84] Yeah.
[293.96 → 299.10] So, as you know, I introduced myself as a data scientist with SIL International, which
[299.10 → 304.50] sometimes we joke as kind of SIL International is everywhere, but no one really knows about
[304.50 → 304.66] it.
[304.80 → 306.20] It's an international nonprofit.
[306.76 → 311.56] We actually have people from over 80 countries working in 90 countries.
[311.88 → 318.00] And the vision and mission of SIL is to see people flourish in communities with languages
[318.00 → 319.34] they value most.
[319.34 → 324.60] So, we do everything associated with language work, which involves a lot of things.
[324.88 → 327.44] So, that involves things like multilingual education.
[327.80 → 332.72] It involves things like literacy work, like language development, even like language survey
[332.72 → 334.46] and mapping and other things.
[334.72 → 336.68] But it's also technology related.
[336.92 → 343.00] So, one of our products is called Kerman, which is a keyboard for devices like phones and
[343.00 → 343.30] tablets.
[343.30 → 348.70] And it supports over a thousand languages, which the next biggest keyboard solution doesn't
[348.70 → 350.36] support even nearly that much.
[350.64 → 355.40] We also have a product called the Ethnologue, where we track, you know, what languages are
[355.40 → 359.98] being spoken whereby how many people, how many languages there are in the world.
[360.32 → 367.72] We're also involved in the ISO standard process for the ISO standards for languages, little codes
[367.72 → 368.78] that represent languages.
[368.78 → 373.20] But I personally work on things related to AI and language.
[373.40 → 378.98] So, SIL has actually gathered a lot of data related to languages.
[379.20 → 381.44] We've worked in over 2,000 languages.
[382.08 → 390.64] And so, part of my responsibility is to help SIL develop programs and do experiments and research
[390.64 → 398.48] to push AI tasks like translation or sentiment analysis, speech to text, text to speech, these
[398.48 → 403.26] sorts of things past the languages that are currently supported into the longer tail of
[403.26 → 404.52] languages in the world.
[404.64 → 409.72] Those local languages spoken around the world where there currently isn't support for those
[409.72 → 410.00] things.
[410.38 → 412.68] So, yeah, that's what I get the privilege of doing.
[413.56 → 417.78] Well, thank you for that unusual introduction for this podcast and kind of bring people in.
[417.78 → 422.20] And I got to say, as you finish having worked with you now all this time on all these episodes,
[422.20 → 426.42] for listeners who don't already know, you are truly a natural language processing expert
[426.42 → 426.92] in AI.
[427.10 → 429.88] And I have learned a lot from you in the time we've been working together.
[430.08 → 430.68] It's been fun.
[430.96 → 431.28] Thank you.
[431.32 → 435.40] As we turn toward Pachyderm, I wanted to actually start off by noting that we have previously
[435.40 → 440.76] had an episode on Pachyderm entitled Pachyderm's Kubernetes-Based Infrastructure for AI.
[440.76 → 447.26] It was episode number 23, and our guest representing Pachyderm on that was Joe Duller, who everyone
[447.26 → 448.02] calls JD.
[448.36 → 449.76] He's the CEO of Pachyderm.
[449.96 → 454.64] But with us today, as we kind of dive into this story about local languages, Dan Jay,
[454.72 → 457.98] can you kind of tell us a little bit about yourself and a little bit about how you arrived
[457.98 → 458.58] at Pachyderm?
[458.98 → 459.36] Sure.
[459.86 → 463.08] I arrived at Pachyderm through a circuitous path.
[463.70 → 467.32] I've been a technologist for 20 years.
[467.32 → 473.24] I had an IT consulting company for a decade that I sold, and then I spent nine years at
[473.24 → 473.78] Red Hat.
[474.00 → 480.02] I designed some of their early artificial intelligence strategy before anybody was really thinking
[480.02 → 480.64] about it.
[481.28 → 485.96] And I am also a science fiction author with four novels, professional blogger.
[486.64 → 491.60] And one of the things that started to get me very interested in artificial intelligence
[491.60 → 496.28] early was a series of articles that I wrote called Learning AI if you suck at math.
[496.28 → 502.70] And I was taking it from an engineering perspective, trying to look at it from, I'm not a data
[502.70 → 507.38] scientist, but I was trying to look at it from someone who'd spent many years setting up huge
[507.38 → 516.08] sash infrastructures, gigantic web farms, office-back infrastructure, and trying to figure out whether
[516.08 → 522.66] this stuff was learnable by someone who hadn't studied statistics and enjoyed all those things
[522.66 → 523.08] in school.
[523.08 → 525.96] And so that series of articles proved very popular.
[526.16 → 529.02] It was read by over two million people in seven different parts.
[529.38 → 534.34] And I was essentially teaching myself many of the concepts as I was going along.
[535.00 → 540.16] And at that point, I was starting to get talks around the world, both for artificial intelligence
[540.16 → 541.32] and other future technology.
[541.32 → 549.70] And I realized at a certain point in time after my beloved Red Hat was purchased, and it was
[549.70 → 556.08] starting to change in terms of its structure, that I wanted to go back to someplace that was
[556.08 → 559.88] very innovative and that was doing fresh things in the industry.
[560.00 → 565.46] And that's when I came upon Pachyderm, which falls very much into the Flops side of the house
[565.46 → 569.48] and does essentially version control for data science.
[569.48 → 577.74] So when your models, your data, and your code are all changing simultaneously, how do you keep track of all those things and create reproducibility?
[577.74 → 587.76] Because if you run a bunch of tests on a series of a million images and then an administrator comes in and crunches them all down on the back end to a smaller size,
[587.84 → 591.74] then it's going to be nearly impossible to recreate that earlier experiment.
[591.74 → 596.72] So I've been very excited to be with those folks and everybody there is fantastic.
[597.26 → 603.10] And it's exciting to be in this amazing industry now and get to work with incredible people like you two folks.
[603.76 → 604.06] Fantastic.
[604.30 → 605.54] Well, thank you for that.
[605.94 → 612.66] So, you know, starting off, I know I've learned a lot from Dan W about local languages myself just from being associated with them.
[612.78 → 615.88] And we did a keynote together recently at Project Voice.
[615.88 → 623.66] And he has been talking for a while about the partnership between SIL and Pachyderm on this.
[623.82 → 629.86] But I'd like to start off by asking, you know, now that you guys have been partnering together and working on this problem for a while,
[630.10 → 638.12] could you actually tell us, kick us off by telling us a bit about what local languages are and why they should matter to the rest of us?
[638.90 → 641.78] Yeah, I can definitely jump in and give my perspective.
[641.78 → 649.22] Something I didn't know when I started working with SIL was really just about the language situation around the world,
[649.32 → 652.08] which is maybe something we should just start out by talking about.
[652.36 → 656.74] So a lot of people don't realize, actually, we track this very, very closely.
[656.96 → 660.90] Right now, there's 7,111 languages spoken around the world.
[661.30 → 664.96] So these are living languages, not like dialects and that sort of thing,
[665.04 → 668.76] but recognized living languages that are spoken around the world.
[668.76 → 676.94] And certain countries, like let's say India or Indonesia, other countries have hundreds of these languages being spoken.
[677.28 → 679.58] Indonesia, for example, it's like about 700.
[680.44 → 688.38] And so what happens as a result of this is that there are some languages that are spoken by a lot of the world.
[688.52 → 694.84] So over half of the world speaks, I think it's 23 of those languages, which is a very small number, right?
[695.26 → 696.96] Compared to 7,000, it sure is.
[696.96 → 699.46] Yeah, the other half of the world speaks the rest of them.
[700.00 → 709.34] And so what happens is that these local language communities, which don't maybe speak one of these higher resource languages,
[709.34 → 713.24] are usually and often marginalized in some way.
[713.76 → 720.04] And so these marginalized language communities value communication in their local languages,
[720.04 → 723.54] but they aren't supported in a variety of ways.
[723.56 → 725.88] And this has implications for a lot of things.
[725.88 → 732.58] One of the ways that we think about this is in terms of the United Nations Sustainable Development Goals.
[732.74 → 738.02] So the United Nations developed these 17 goals about sustainable development.
[738.62 → 742.34] And language impacts basically every one of those.
[742.34 → 748.92] So if you think about education or humanitarian assistance, thinking about something like HIV or AIDS or Ebola,
[748.92 → 757.22] how are you going to be able to make progress in those areas where there's extreme language diversity?
[757.22 → 763.24] If you can't get out materials about HIV or other things in a language that people understand and value,
[763.30 → 765.50] that they don't consider something foreign.
[765.50 → 768.28] And this goes across the board in education.
[768.72 → 774.04] There have been studies that have shown if someone starts their education by going to school.
[774.20 → 780.44] So if they're at home and their family speaks a certain language and then, you know, their mother speaks it,
[780.48 → 783.58] their father speaks it, their whole village speaks it, and then they go to school.
[784.20 → 786.08] And the first thing their teacher says is,
[786.08 → 790.16] Oh, it's great that you speak that, but you're not going to speak that here.
[790.24 → 792.18] We're going to learn in this other language.
[792.18 → 798.98] Well, immediately right off the bat, they form an association with education as something terrible and hard.
[799.40 → 802.36] And it actually stunts their educational development.
[802.58 → 805.26] Whereas if they start education in their mother tongue,
[805.42 → 812.38] they actually have the same benefits as others in terms of their views of education and their forward momentum.
[812.38 → 817.22] So language impacts everything, and that's why we care about these local languages,
[817.22 → 820.52] because they actually make a difference for people's quality of life.
[820.52 → 825.46] I think this falls into that AI for good category as well.
[825.70 → 827.68] That's something that's very close to my heart.
[827.80 → 831.54] I started the Practical AI Ethics Alliance.
[831.86 → 837.48] It's practical-ai-ethics.org if anyone's interested in checking that out.
[837.48 → 844.94] But the basic concepts behind it are this artificial intelligence is a dual-use technology, right?
[845.04 → 848.70] It reflects everything that is good and bad about humanity.
[848.96 → 852.46] So when we're looking at a problem like languages,
[853.10 → 860.12] and I think maybe the most impressive slide and the most impactful slide that I saw at your presentation,
[860.52 → 864.04] Dan W., is where it showed that we were using maybe 100 languages
[864.04 → 869.52] for the vast majority of applications, whether that's translation or speech-to-text.
[870.12 → 874.24] And there were 7,000 other languages that half the population was speaking,
[874.50 → 876.54] and we weren't doing anything with those.
[877.08 → 881.24] And that's a surefire way, really, to continue to marginalize people
[881.24 → 887.58] or to ensure that, like you said, that people are going to find education difficult
[887.58 → 890.90] or that even finding basic services is incredibly difficult.
[890.90 → 895.14] So I think it's wonderful that you're working on a side of the house
[895.14 → 900.08] that allows you to make a difference and have an impact in this part of the world
[900.08 → 907.08] because I feel like so much of the research sometimes gets poured into, you know,
[907.14 → 910.58] getting people to click on ads or all the things that make us money.
[910.68 → 911.80] And those things are certainly important.
[911.90 → 913.20] Economics are incredibly important.
[913.20 → 921.32] But it's also amazing to realize that artificial intelligence can make the world a better place in some ways, right?
[921.38 → 924.86] It almost sounds cliché, or it sounds a little, you know, high-minded,
[925.00 → 930.06] but it is actually true that certain types of things would never be able to be done without it.
[930.12 → 935.28] I remember seeing a translation for very old Japanese
[935.28 → 939.70] that only maybe 100 scholars in the world can speak now,
[939.70 → 946.26] and there are tens of thousands or millions of texts in a form of Japanese that's really not used anymore.
[947.06 → 954.04] And machine learning is able to augment the ability of those translators to scale what it is they're doing
[954.04 → 957.18] so that those texts don't die out into the pages of history
[957.18 → 961.80] simply because we don't have anybody interested anymore in being able to translate them.
[961.90 → 964.38] So I think that's where this thing can make a massive impact.
[964.38 → 970.74] Yeah, and you've kind of gotten into the idea of the importance of applying AI to the possibilities.
[970.90 → 975.44] I mean, and is there any way, do either of you have any comments on kind of expanding that a little bit
[975.44 → 981.20] in terms of, you know, why apply AI to this long tail of languages?
[981.76 → 983.24] You know, you just identified one.
[983.36 → 984.50] Any others that come to mind?
[984.50 → 992.86] Well, I think that, you know, AI and especially, I guess what I feel like we're on the verge of sort of new possibilities
[992.86 → 995.78] in terms of AI and language over the past couple of years,
[995.78 → 1002.14] you've definitely seen, like some people might refer to as an inflection point with a lot of new techniques,
[1002.34 → 1007.10] a lot of emphasis on transfer learning, a lot of emphasis on usage of monolingual data,
[1007.10 → 1012.64] and, you know, things that really impact the languages in this sort of long tail of languages,
[1012.64 → 1017.14] the languages outside of those supported by the major tech platforms.
[1017.14 → 1021.28] So I think one thing to note is that, you know, whereas used to,
[1021.38 → 1024.54] we might have been stuck with some of these things like machine translation
[1024.54 → 1026.84] because of lack of data or something like that.
[1027.12 → 1031.62] There are brand-new possibilities where, you know, what if we could translate,
[1031.62 → 1038.32] you know, translate these HIV materials or this educational material into all of these different languages?
[1038.52 → 1044.24] What if we could enable people to be part of the global conversation in their mother tongue?
[1044.32 → 1049.42] That's a very interesting one for me is, you know, oftentimes I think we feel like,
[1049.64 → 1057.92] oh, how can we get our great content as Westerners into the languages that, you know, people care about,
[1058.00 → 1059.54] which isn't a bad thing.
[1059.54 → 1064.50] It's great to try to get those materials, those educational materials, scientific materials,
[1064.94 → 1068.02] you know, entertainment media into local languages.
[1068.24 → 1070.78] But these people in these local language communities,
[1070.78 → 1074.54] they have so much to contribute to our understanding of the world,
[1074.68 → 1077.96] to scientific research, to all sorts of different areas.
[1078.14 → 1084.36] And so on of the things that I think AI could enable with things like speech-to-speech translation,
[1084.86 → 1088.16] with things like predictive text and other things like that,
[1088.16 → 1092.96] are enabling those local language communities to be part of a global conversation,
[1092.96 → 1095.94] not just to be consumers,
[1095.94 → 1101.00] but to actually contribute in a back and forth sort of way to global conversations around
[1101.00 → 1105.32] the things that actually impact their life and the things that they can contribute,
[1105.64 → 1108.12] like politics and education and all those things.
[1108.56 → 1111.48] I think it's interesting that you're talking about it from a two-way street.
[1111.48 → 1115.96] And I think that that's an amazing way to frame it, because what is it that we can learn,
[1116.02 → 1121.90] not just what is it that we can translate from our own content into what other people can consume,
[1121.94 → 1125.90] but really what is it that we're missing on the other side of the equation?
[1126.40 → 1129.46] And historically, if you look at how language has been used,
[1129.58 → 1134.34] sometimes it's been used as a way to dominate other cultures or as a way to socialize.
[1134.34 → 1136.08] It's almost been used as a weapon.
[1136.24 → 1140.70] The farther that a language can spread, the more that people think in your own way.
[1141.22 → 1145.48] If you think about something like the Etruscans and the Roman Empire,
[1145.48 → 1149.04] we know pretty much nothing about the Etruscans,
[1149.40 → 1153.00] primarily because they were completely consumed by the Roman Empire,
[1153.14 → 1155.20] not in small part due to language.
[1155.60 → 1157.86] And we've seen this in other parts of the world,
[1157.86 → 1161.28] but that sort of slash and burn mentality,
[1161.28 → 1165.44] there are a lot of things that are lost in the same way when we,
[1165.54 → 1167.66] you know, destroy a huge part of the forest,
[1167.82 → 1171.44] what medicines get lost that we would never have been able to find,
[1171.50 → 1176.24] what compounds were hidden in the species of plants that were wiped out.
[1176.66 → 1182.26] And in the same way, different types of languages allow us to think differently.
[1182.42 → 1185.28] And in fact, we just had the wonderful Super Bowl on the other day,
[1185.28 → 1188.46] and there was a commercial, believe it or not, that stopped me for a second,
[1188.46 → 1191.62] where they said that there were four words in Greek for love.
[1192.10 → 1195.52] And I went and looked up each of the words, and they were fascinating,
[1195.84 → 1199.06] in that each one of those words conveyed something very different
[1199.06 → 1203.40] about the nature of love, from Eros, which is more of a passionate,
[1204.06 → 1206.86] you know, kind of love, to agape,
[1207.08 → 1211.26] which was more of a selfless kind of love or a love for a country.
[1211.26 → 1214.80] And each of those words convey something very different.
[1215.12 → 1216.54] And so when we lose these languages,
[1216.54 → 1221.70] or we assume that we have the words that perfectly convey things,
[1222.18 → 1224.68] we lose a lot of nuance and meaning,
[1225.02 → 1230.20] and we lose people's ability to connect in a fluid way with us.
[1230.22 → 1233.36] So I think it's amazing that you framed it as a two-way conversation.
[1233.36 → 1234.32] That's very important.
[1234.32 → 1246.10] This episode is brought to you by Brave.
[1246.48 → 1248.30] We deserve a better internet.
[1248.62 → 1251.96] That's why the team behind Brave reimagined what a browser could be.
[1252.48 → 1254.42] Brave is like Chrome, the good parts.
[1254.70 → 1256.34] Even your extensions will just work.
[1256.56 → 1258.22] It has built-in ad and tracker blocking,
[1258.54 → 1260.36] easy anonymization with the Tor network,
[1260.56 → 1261.80] earn tokens while you browse,
[1261.80 → 1263.86] and use them to tip your favourite creators,
[1263.86 → 1265.82] and did I mention it's lightning fast?
[1266.16 → 1268.76] Turns out the web is superfast when you remove all the cruft.
[1269.10 → 1271.30] Download Brave today using the link in the show notes
[1271.30 → 1273.80] and give tipping a try on changelog.com.
[1284.52 → 1286.56] So Dan W.,
[1286.56 → 1291.64] what is SIL kind of doing in terms of AI for local languages these days?
[1291.64 → 1295.82] And what are you interested in doing to tackle in terms of,
[1296.00 → 1296.14] you know,
[1296.18 → 1300.56] the types of problems and issues that SIL is attending to,
[1300.66 → 1302.28] specifically on your AI roadmap?
[1302.88 → 1303.52] Yeah, definitely.
[1303.78 → 1305.04] So in the longer run,
[1305.54 → 1306.36] like I say,
[1306.40 → 1310.72] we want to see the sort of two-way street that we've been talking about in terms of
[1310.72 → 1313.24] local languages being part of a global conversation.
[1313.24 → 1320.76] And I think maybe a natural place to start with that is the sorts of AI technology that have already,
[1320.76 → 1321.66] you know,
[1321.66 → 1324.52] been groundbreaking in our everyday life,
[1324.56 → 1328.22] maybe as English speakers or other high resource language speakers.
[1328.22 → 1330.76] And so like if you do a Google search now,
[1330.86 → 1331.08] right,
[1331.28 → 1332.74] that's hitting an AI model,
[1332.74 → 1335.04] now integrated BERT into that.
[1335.58 → 1336.74] If you're writing an email,
[1336.74 → 1339.00] you've got predictive text along with that,
[1339.08 → 1340.10] that helps you.
[1340.58 → 1342.42] If you're dealing with a chatbot,
[1342.48 → 1346.54] you have these things like sentiment analysis and entity recognition.
[1347.06 → 1351.16] If you're talking to an assistant or a smart speaker or other things,
[1351.28 → 1352.68] you're using speech to text,
[1352.74 → 1356.12] you're using maybe those same assistant capabilities,
[1356.40 → 1358.80] you might be using text to speech.
[1358.80 → 1366.40] And so these sorts of building block AI technologies are what we're thinking about a lot right now.
[1366.68 → 1369.54] And how could we take those building blocks,
[1369.60 → 1373.00] which now only support sort of high resource languages,
[1373.52 → 1374.78] maybe up to a hundred,
[1375.02 → 1376.30] but as Dan Jay mentioned,
[1376.44 → 1377.90] that's kind of a drop in the bucket.
[1378.48 → 1381.88] How do we push those into the longer tail of languages?
[1382.22 → 1384.34] And what really excites us is,
[1384.44 → 1384.98] you know,
[1385.02 → 1387.26] how could we not just do that language by language?
[1387.26 → 1389.80] Like, oh, we add the next language,
[1389.88 → 1391.12] and then we add the next language,
[1391.18 → 1392.44] and then we add the next language.
[1392.54 → 1396.18] How could we knock our 40 languages at a time, right?
[1396.58 → 1399.74] And I think those are the things that get us really excited.
[1400.04 → 1404.14] And so some of the things that contribute to those sorts of advances,
[1404.32 → 1404.70] I think,
[1404.84 → 1406.14] are first,
[1406.28 → 1407.26] multilingual models.
[1407.38 → 1413.02] So we've seen this shift recently into massively multilingual models that support things like Google
[1413.02 → 1413.66] Translate,
[1413.78 → 1416.22] where one model actually can process
[1416.22 → 1418.60] multiple different language pairs.
[1419.14 → 1421.26] And something people may not know is,
[1421.48 → 1421.68] you know,
[1421.82 → 1424.48] I think no one's been able to challenge me on this,
[1424.58 → 1430.80] but I think SIL and its partners have access to the most massively multilingual corpus that there is.
[1430.96 → 1433.64] So we've done work in over 2000 languages.
[1433.64 → 1435.56] We have some type of data,
[1435.64 → 1437.08] whether that be text or audio,
[1437.08 → 1439.18] and depending on what partners we gather together,
[1439.24 → 1440.72] maybe like 1200 languages.
[1440.72 → 1443.22] So there's a lot of data there.
[1443.38 → 1445.62] And part of what we're excited about is,
[1445.98 → 1446.32] you know,
[1446.38 → 1451.28] what happens if we take the largest multilingual model that there is now,
[1451.36 → 1455.10] which I think the most multilingual one is around 103.
[1455.10 → 1457.32] What if we push that to something like 300?
[1458.10 → 1458.26] You know,
[1458.32 → 1461.18] how does that affect adding the next language in?
[1461.24 → 1462.14] Does it make it easier?
[1462.14 → 1466.78] How should we structure these types of models into language families and other things?
[1466.84 → 1468.16] So we're exploring those things.
[1468.32 → 1469.10] At the same time,
[1469.12 → 1476.46] we're exploring a lot of the low resource machine translation technology that's been developed around transfer learning and fine-tuning,
[1476.92 → 1478.22] iterative back translation.
[1478.22 → 1490.82] There are just a lot of different techniques out there now that allow you to maybe take a high resource language and adapt it to a lower resource language or even make use of multilingual data.
[1491.44 → 1497.36] And so those are all the things that we're interested in exploring first in terms of experiment and research,
[1497.36 → 1502.70] and then in terms of making strategic partnerships with tech companies,
[1502.84 → 1508.94] but also local institutions and governments to pilot out some of these possibilities and actually get them used.
[1509.54 → 1511.80] And that really begs the question for both of you is,
[1511.98 → 1512.18] you know,
[1512.20 → 1513.40] as you talk about these partnerships,
[1513.62 → 1519.76] what specifically brought SIL and Pachyderm together to tackle these kinds of problems that you've just addressed here?
[1520.00 → 1520.56] And why,
[1521.18 → 1522.22] from each of your perspectives,
[1522.34 → 1523.90] why did that partnership make sense?
[1524.48 → 1524.78] Sure.
[1524.78 → 1528.08] I'm very pleased that Pachyderm wanted to work with us.
[1528.14 → 1529.68] So I'm really happy about that.
[1529.86 → 1533.30] Thank you to Dan Jay and the team who wanted to work on this.
[1533.38 → 1543.72] But I think that despite SIL having a ton of data and a very multilingual corpus and an amazing amount of language information and linguistic expertise,
[1544.04 → 1545.12] we're not a tech company.
[1545.38 → 1550.94] We're a nonprofit that has done language related work for a very long time,
[1550.94 → 1554.42] but isn't really an AI company per se.
[1554.78 → 1558.96] And isn't operating a ton of computational infrastructure.
[1559.30 → 1563.10] So whereas we have a lot of this sort of data and language information,
[1563.30 → 1564.60] that side of the equation,
[1564.60 → 1571.80] part of what we want to do is partner with people that have a lot of expertise on the infrastructure side,
[1571.80 → 1575.14] on the AI methodology and AI,
[1575.46 → 1575.64] you know,
[1575.70 → 1577.96] practical AI training side.
[1577.96 → 1581.16] And Pachyderm definitely fits into that component.
[1581.32 → 1582.30] So from my perspective,
[1582.30 → 1591.38] that's what I was excited about working with Pachyderm is actually building something useful that we can use over time and repeatedly use and scale up.
[1591.44 → 1593.18] Because this is a large scale problem,
[1593.26 → 1593.44] right?
[1593.52 → 1594.38] 7,000 languages.
[1594.38 → 1597.18] We need something that's going to scale and something that's going to work.
[1597.18 → 1601.02] And so that's what originally got me thinking of partnership with Pachyderm.
[1601.26 → 1601.28] And,
[1601.28 → 1601.82] you know,
[1602.04 → 1604.24] Dan Jay can speak from Pachyderm's perspective,
[1604.24 → 1606.62] but I hope that they were excited about this sort of,
[1606.62 → 1607.14] you know,
[1607.22 → 1608.28] AI for good problems.
[1608.54 → 1608.98] Well,
[1609.02 → 1611.28] we definitely are excited about this AI for good problems.
[1611.28 → 1612.04] And frankly,
[1612.04 → 1615.24] we've been looking for a number of these types of things in the field.
[1615.24 → 1618.36] So if folks are out there interested in doing those types of things,
[1618.42 → 1618.58] we,
[1618.68 → 1619.52] we want to talk.
[1619.64 → 1619.68] We're,
[1619.68 → 1620.50] we're certainly not,
[1620.50 → 1621.50] you know,
[1621.50 → 1623.38] deep mind or open AI or,
[1623.38 → 1624.94] or have an infinite,
[1624.94 → 1625.68] uh,
[1625.68 → 1626.98] lead deep pockets to,
[1627.10 → 1628.54] to be able to throw at some of these things.
[1628.54 → 1634.68] But we do feel it's of tremendous importance for us to help enable projects like this.
[1634.68 → 1634.86] And,
[1634.86 → 1635.46] and frankly,
[1635.56 → 1636.56] Pachyderm is,
[1636.74 → 1639.06] is more of the infrastructure side of the house.
[1639.06 → 1641.66] So we recently launched the Pack Hub product,
[1641.66 → 1643.94] which runs on Google cloud,
[1643.94 → 1644.38] uh,
[1644.38 → 1649.60] and allows people to automatically spin up clusters and add GPUs to them and parallelize their resources.
[1650.14 → 1651.68] And those types of things,
[1651.82 → 1659.90] I think Pachyderm is one of the solutions that people don't realize they need until they start doing data science at scale.
[1660.06 → 1660.42] Uh,
[1660.42 → 1661.00] and I think we're,
[1661.00 → 1669.04] we're seeing a development of a canonical stack probably over the next two to five years when the tools become,
[1669.06 → 1670.06] uh,
[1670.06 → 1672.46] that allow data scientists like,
[1672.46 → 1673.44] like Dan W,
[1673.44 → 1674.44] uh,
[1674.44 → 1676.68] to really do their job easier.
[1676.80 → 1678.98] And if you think about the
[1678.98 → 1681.74] the history of how these things have worked,
[1681.74 → 1686.66] a lot of times data scientists were just passing around a text file between them,
[1686.66 → 1691.30] or maybe FTP something somewhere and cobbling together infrastructure.
[1691.30 → 1695.22] That's not really going to work as you get,
[1695.22 → 1695.82] uh,
[1695.82 → 1697.58] this technology out of the hands of the
[1697.58 → 1703.16] the unicorns that have a billion dollars to just throw at things and,
[1703.16 → 1705.20] and create the infrastructure on the fly.
[1705.20 → 1710.38] So if you think about a company like Google or some of the research foundations doing their own work,
[1710.44 → 1717.30] they're all building all their pipeline tools and their training visualization tools and their explainer tools,
[1717.38 → 1718.30] all of these types of things.
[1718.30 → 1722.62] And they're experimenting with lots of different frameworks and libraries,
[1722.62 → 1724.14] but over time,
[1724.14 → 1725.20] we're going to start to see,
[1725.20 → 1725.64] you know,
[1725.64 → 1742.30] more and more standardization and a problem like being able to version control your data and understand the entire data lineage of where things got from point A to point B to point C is incredibly important for being able to reproduce experiments.
[1742.30 → 1744.30] I read in,
[1744.30 → 1744.78] in,
[1744.78 → 1746.10] in venture beat the other day,
[1746.10 → 1750.86] that something like 87% of data science projects never make it to production.
[1750.86 → 1752.10] And that's a massive number,
[1752.10 → 1752.50] right?
[1752.50 → 1754.78] Considering that we've spent upwards of,
[1754.78 → 1755.30] you know,
[1755.42 → 1756.94] 60 or $70 billion,
[1757.30 → 1758.14] I think was the number,
[1758.14 → 1762.46] or we're spending hundreds of billions of dollars more or hundreds of millions of dollars more in the
[1762.46 → 1762.82] uh,
[1762.82 → 1763.70] the coming years.
[1763.70 → 1767.18] And that means we've wasted that much if we don't improve that.
[1767.24 → 1768.46] And if we don't improve that,
[1768.62 → 1769.44] we're in serious trouble.
[1769.48 → 1772.28] And one of the ways to improve that is by having that level of reproduction.
[1772.30 → 1773.10] And,
[1773.10 → 1776.30] and being able to work across a diverse team.
[1776.64 → 1781.42] And so getting our tools into the hands of people are doing amazing things,
[1781.42 → 1781.92] uh,
[1781.92 → 1784.40] is definitely the way to get our name out there,
[1784.40 → 1786.28] but also really make a difference in the world.
[1786.28 → 1787.84] And I think both goals are,
[1787.94 → 1788.96] are incredibly important.
[1789.50 → 1789.98] Yeah.
[1790.10 → 1791.74] And on a practical level,
[1791.74 → 1795.06] since I'm always interested in keeping this podcast practical,
[1795.20 → 1800.38] I'll kind of walk through our internal workflow and thought process on this.
[1800.38 → 1800.62] I mean,
[1800.62 → 1801.30] if you imagine,
[1801.30 → 1803.64] let's just take a machine translation,
[1803.94 → 1804.58] for example,
[1804.98 → 1806.70] which is one of the things that we're working on.
[1807.04 → 1807.26] Well,
[1807.30 → 1810.30] I can spin up a collab notebook and,
[1810.30 → 1810.68] um,
[1810.88 → 1811.14] you know,
[1811.16 → 1812.08] develop the
[1812.18 → 1817.64] kind of pull the data together from a source that we have access to inside SIL,
[1818.14 → 1818.38] um,
[1818.38 → 1820.26] do some pre-processing on that,
[1820.34 → 1821.80] do the training test,
[1822.02 → 1822.24] you know,
[1822.24 → 1823.00] do the testing,
[1823.00 → 1825.36] get the inference bit worked out.
[1825.36 → 1826.14] But now if,
[1826.32 → 1833.66] if we're really serious about like our goal of pushing this sort of thing into many languages at once,
[1833.66 → 1834.54] right now,
[1834.54 → 1837.56] I have to think about other sorts of problems.
[1837.56 → 1838.44] And one of those,
[1838.68 → 1838.94] you know,
[1838.96 → 1842.82] on the data side is the data that SIL has access to.
[1842.82 → 1843.70] And that we use is,
[1843.88 → 1845.28] is a big mix of data.
[1845.28 → 1847.16] So it's partly internal data.
[1847.16 → 1848.96] And most of the time,
[1848.96 → 1853.02] like formatted in sort of maybe non-standard formats,
[1853.02 → 1855.34] as far as AI people are thinking,
[1855.70 → 1857.68] it might be data from partners.
[1858.10 → 1859.70] It might be a mix of public data.
[1860.08 → 1866.60] And so we have all of these sorts of data that we may want to bring together in unique ways.
[1866.82 → 1869.22] And the combinations of those data for,
[1869.62 → 1871.40] let's say if we're targeting 40 languages,
[1871.70 → 1874.16] they might be different for the different languages,
[1874.42 → 1874.62] right?
[1874.62 → 1881.04] And so there's this complicated issue of how do I combine all these things together in a sane sort
[1881.04 → 1883.24] of way with a bunch of pre-processing.
[1883.38 → 1885.86] And then I've got the problem of,
[1886.10 → 1886.28] okay,
[1886.48 → 1886.72] well,
[1886.72 → 1888.66] I need to kind of standardize those.
[1888.84 → 1889.08] I might,
[1889.30 → 1892.50] those data sets might be updating at certain times.
[1892.50 → 1897.66] And then I've got to connect all of those data sources with the correct pre-processing,
[1897.76 → 1898.18] like I said,
[1898.26 → 1898.98] but then training.
[1898.98 → 1903.98] And that training needs to happen on GPUs where maybe the pre-processing is happening on CPUs.
[1904.62 → 1907.14] And then I need to connect those output models.
[1907.22 → 1912.02] I need to actually export them and optimize them in a way where they can be exported to a certain
[1912.02 → 1914.64] place where they can actually be used in a product.
[1914.92 → 1917.00] So all of those things for like,
[1917.52 → 1917.98] even,
[1918.28 → 1918.58] you know,
[1918.64 → 1922.04] a few languages or 40 languages or whatever we're looking at,
[1922.10 → 1923.64] that gets complicated fast.
[1923.64 → 1928.36] And so the ability to track all of that very rigorously,
[1928.36 → 1935.26] but also be able to scale it as we might want and do it in a sort of way that isn't like,
[1935.80 → 1936.14] you know,
[1936.24 → 1939.00] there's only so many technical people at,
[1939.00 → 1939.64] at SIL.
[1939.86 → 1941.14] So we can write,
[1941.24 → 1942.14] you know,
[1942.34 → 1945.42] small bits of code to do these various things,
[1945.42 → 1948.98] but we're not going to write the whole infrastructure and logic around this.
[1948.98 → 1953.26] So we needed something that was able to handle this sort of data elements,
[1953.62 → 1954.00] scaling,
[1954.22 → 1956.68] pre-processing across lots of data sets,
[1956.68 → 1960.46] and also scaling our training while utilizing certain GPUs.
[1960.90 → 1963.48] And so Packet Earn project and the
[1963.80 → 1969.20] and what's available in that project in the pipelining and data management allowed us to do those sorts of things.
[1969.20 → 1969.52] And it,
[1969.54 → 1971.28] it really comes down to the fact that,
[1971.64 → 1971.90] you know,
[1971.92 → 1973.36] we want to scale this out.
[1973.44 → 1975.78] We want to push it to many,
[1975.90 → 1976.54] many languages.
[1976.54 → 1978.32] And so to do that,
[1978.32 → 1985.44] we're going to have to do it reproducibly, and we're going to have to do it over and over and maybe scale it out horizontally as well.
[1985.58 → 1989.96] So there's a lot that goes into that and very thankful to get help on that front.
[1990.54 → 1990.56] So,
[1990.72 → 1991.12] you know,
[1991.26 → 1997.24] I know Daniel W when we were doing our keynote together at project voice,
[1997.24 → 2005.60] you had a fascinating example that you as SIL and Packet Durham work together on around these sorts of problems.
[2005.60 → 2008.30] And it kind of outlined what both sides,
[2008.40 → 2010.82] how both sides approached and what you were able to do,
[2010.92 → 2013.96] including the benefits of doing the activities on Packet Durham.
[2014.06 → 2014.68] Could you kind of,
[2014.86 → 2016.30] kind of go through that example?
[2016.56 → 2018.42] And I would also invite Dan J to,
[2018.42 → 2019.16] to pipe in,
[2019.28 → 2019.58] you know,
[2019.58 → 2021.42] so you guys can kind of relay that together a bit.
[2021.42 → 2022.22] Yeah,
[2022.28 → 2022.58] sure.
[2022.74 → 2027.10] So the problem we were looking at was text to speech or speech synthesis and
[2027.10 → 2036.12] specifically adapting an existing text to speech model to a local language or a local dialect or a local accent.
[2036.74 → 2043.04] And so you could think of examples like there's a bunch of vernacular Arabic's that are spoken around the world.
[2043.46 → 2047.12] There's a bunch of world Englishes that are different in certain ways.
[2047.12 → 2048.50] And so we took,
[2048.76 → 2049.36] for example,
[2049.82 → 2050.22] English,
[2050.36 → 2054.38] which is a dialect that's spoken in Singapore.
[2054.98 → 2059.68] So it's actually a mix of like English and some other languages that's spoken together.
[2060.18 → 2064.02] This is kind of an interesting problem because as a dialect,
[2064.40 → 2066.70] it has these elements from,
[2066.84 → 2067.42] you know,
[2067.48 → 2069.30] at least four or more languages,
[2069.30 → 2074.52] but it also has various kinds of standard accents that go along with it.
[2074.52 → 2077.22] So there's like an Indian accent, and it's English,
[2077.44 → 2078.88] Chinese accent, and it's English.
[2079.28 → 2085.14] And it's a nice kind of proving ground for some of this adaptation to accents and other things.
[2085.54 → 2092.00] And so we wanted to create some text to speech models for English because for one,
[2092.08 → 2092.92] these don't exist.
[2093.50 → 2094.08] And for two,
[2094.20 → 2101.30] we were able to access some data through one of our partners in Singapore to get some of this data for English
[2101.30 → 2104.40] and to utilize it to test out these methods.
[2104.76 → 2109.28] The downside to that is like there was a lot of processing that had to happen here.
[2109.42 → 2111.96] So our partners were able to actually get us,
[2112.44 → 2114.62] I think it was like 800 gigabytes of data.
[2114.84 → 2116.42] So this was between our partner,
[2116.56 → 2117.44] Wordly in Singapore,
[2117.44 → 2120.82] and the government institution there,
[2121.08 → 2121.60] IMA,
[2122.00 → 2124.36] that has gathered a lot of this data.
[2124.36 → 2128.38] All of that data is formatted in specific ways.
[2128.50 → 2130.86] Some of its kind of noisy.
[2131.64 → 2133.78] It corresponds to a lot of different speakers,
[2133.92 → 2135.26] like 2000 different speakers.
[2135.42 → 2137.16] And so there was a lot of like,
[2137.26 → 2139.40] how are we going to actually pre-process this?
[2139.54 → 2142.78] And then how are we going to like to make this efficient?
[2142.78 → 2145.42] So we're not running these models for like,
[2145.78 → 2146.04] you know,
[2146.16 → 2148.06] weeks on end without progress.
[2148.06 → 2153.28] So that's where we consulted a lot with Packet Arm, and they were able to kind of guide us through like,
[2153.56 → 2153.72] well,
[2153.78 → 2162.38] here's how maybe similar people have set up their pipelines in the past and the type of infrastructure that they've used and how they've scaled it.
[2162.54 → 2162.98] I know.
[2163.14 → 2164.08] So Dan Jay,
[2164.14 → 2166.90] I know we worked through some issues with like data,
[2167.16 → 2168.96] like how do we upload that much data?
[2169.20 → 2171.20] How do we pick out the
[2171.30 → 2171.40] like,
[2171.60 → 2173.88] you don't want to load 800 gigabytes into memory.
[2173.88 → 2176.76] So how do you like access some of that data,
[2176.88 → 2180.22] but not all of it to like figure out what you need.
[2180.48 → 2181.76] So I think these are,
[2182.00 → 2182.12] you know,
[2182.18 → 2182.90] from my understanding,
[2182.98 → 2187.56] these are problems that other people are facing, and they were kind of going to,
[2187.56 → 2187.78] you know,
[2187.82 → 2189.26] help us solve some of those.
[2189.36 → 2191.94] I remember the one problem of like accessing some data,
[2192.06 → 2195.70] but not all of it was kind of key to this whole problem.
[2196.18 → 2196.76] I mean,
[2196.78 → 2199.96] being able to split up the data, and we rely a lot on,
[2200.16 → 2203.48] I think we made an intelligent choice in going with Salinities and,
[2203.48 → 2204.98] and Docker early.
[2205.16 → 2208.64] So we could leverage a lot of the scaling that happens now.
[2208.94 → 2211.44] If you really think about the history of containers,
[2212.04 → 2216.12] it really Googles was running billions of these containers even before Docker
[2216.12 → 2216.90] existed.
[2217.14 → 2219.48] And so the industry was moving in this,
[2219.68 → 2220.76] in this direction.
[2220.98 → 2225.76] And they had originally an internal service called Borg that was then shifted
[2225.76 → 2228.24] over into the Kubernetes open source project.
[2228.24 → 2228.70] And that,
[2228.78 → 2233.94] that really took off and allowed people to kind of build these massive
[2233.94 → 2237.36] infrastructures that scaled much faster than these virtualization
[2237.36 → 2238.78] infrastructures,
[2238.78 → 2244.04] where you ended up having an entire operating system that was built into this
[2244.04 → 2246.54] little box that you were processing things in.
[2246.54 → 2247.64] It was very,
[2247.78 → 2249.68] the virtualization era was very effective,
[2249.68 → 2251.44] but once we got to,
[2251.44 → 2257.30] to need lots of ephemeral machines or being able to quickly spin up a thousand
[2257.30 → 2263.58] different nodes to split up data and process it into little chunks so that
[2263.58 → 2267.20] you're not trying to load everything into a massive virtual machine and
[2267.20 → 2268.20] saturating the memory.
[2268.70 → 2270.94] We spoke with one customer recently,
[2270.94 → 2274.96] there's a case study coming out where they were doing a lot of language
[2274.96 → 2277.08] processing, and they built their pre-processing tools.
[2277.94 → 2285.54] And they were taking about eight to 10 weeks on the biggest possible node that
[2285.54 → 2287.54] they could spin up in Google or,
[2287.54 → 2289.24] or AWS or,
[2289.24 → 2289.92] or Azure.
[2290.14 → 2290.90] So they were basically,
[2290.90 → 2291.72] you know,
[2291.78 → 2295.66] grabbing the most expensive node possible to try to fit everything into,
[2295.84 → 2298.62] into memory and stack the GPUs in there.
[2298.62 → 2302.88] And it was taking them about 10 weeks, and they were able to parallelize it with
[2302.88 → 2308.20] pachyderm and get it down to about six or seven days.
[2308.64 → 2310.42] So that is a massive increase.
[2310.58 → 2314.38] And that's basically because they're able to split it up across multiple nodes
[2314.38 → 2319.56] without actually really having to worry about precisely how they split it up.
[2319.66 → 2322.62] Pachyderm does a lot of the heavy lifting for folks in,
[2322.74 → 2326.20] in the backend and allows it to work across multiple nodes,
[2326.20 → 2329.52] as opposed to having to try to figure out within your own code,
[2329.52 → 2332.16] because you're already worrying about a data scientist.
[2332.16 → 2336.42] Like Dan W is already trying to worry about how do I solve a problem like
[2336.42 → 2338.74] transfer learning or a noisy data set?
[2338.76 → 2339.70] And how do I clean that up?
[2339.70 → 2342.88] Or I've got a number of different formats.
[2342.88 → 2347.42] How do I either use all of those formats or standardize on a different format
[2347.42 → 2350.20] before I can even do any of my work?
[2350.20 → 2355.12] The last thing you need to be worrying about is then figuring out how to also be an infrastructure
[2355.12 → 2361.06] engineer and auto-scale lots of different nodes yourself and spin them down.
[2361.34 → 2363.08] And suddenly you're forgetting about them.
[2363.26 → 2368.04] And then your company gets an AWS bill for a million dollars at the end of it.
[2368.24 → 2373.70] So that's, I think, where we really make a big difference for folks doing this kind of work.
[2373.70 → 2374.14] Gotcha.
[2374.96 → 2379.56] I have a kind of follow-up question to the example itself that you guys have worked on.
[2379.72 → 2384.80] And that is, you know, if there's one thing that's become clear to me as the person not
[2384.80 → 2389.70] involved in this, it's what a target rich environment this is to work on in terms of,
[2389.72 → 2392.18] you know, 7,000 plus languages.
[2392.74 → 2396.56] And, you know, you're even with as much work as you're working on at this point,
[2396.86 → 2400.58] it's still, you're only hitting a fairly small fraction, at least at the moment.
[2400.58 → 2404.44] You have addressed this first example that you've kind of relayed to us.
[2404.70 → 2405.54] Why that one?
[2405.72 → 2410.06] Where can this particular approach that you've talked about lead to next?
[2410.48 → 2413.70] What do you envision as being kind of next steps for extending this?
[2414.36 → 2419.70] Well, I think one thing to emphasize with this and one other reason why we were really
[2419.70 → 2424.52] interested in this partnership to enable this sort of thing is Packet Arm as part of the
[2424.52 → 2427.86] open source community and part of the Kubernetes community.
[2427.86 → 2434.80] And so anyone can run a Packet Arm pipeline and anyone can spin up a Kubernetes cluster in
[2434.80 → 2436.96] the cloud or on premises or wherever.
[2437.62 → 2442.52] And so we're thinking about this sort of work as a sort of template, right?
[2442.96 → 2449.42] So I created with the help of the Packet Arm team created this template for training speech
[2449.42 → 2451.26] models using this pipeline.
[2451.50 → 2456.12] You could plug in any sort of speech data set you want, assuming you could pre-process it
[2456.12 → 2457.18] into the right format.
[2457.88 → 2464.18] And so the idea is we showed this for, let's say, one accent and one speaker of this data
[2464.18 → 2465.12] set that we worked with.
[2465.14 → 2466.56] And we're working on others as well.
[2466.76 → 2472.66] But I could publish that pipeline on GitHub, which I have.
[2472.86 → 2474.88] And anyone could pull that down.
[2475.20 → 2478.82] Anyone could access the IMA data if they knew where to look.
[2478.82 → 2480.28] And we put the links in, right?
[2480.72 → 2485.82] And anyone could generate their own speech model, run the same Packet Arm pipeline on
[2485.82 → 2492.38] their own Kubernetes cluster because everything is portable and everything is built on this
[2492.38 → 2494.50] great open source community.
[2495.38 → 2502.42] And people could collectively work on this for a greater impact than any one certain person.
[2502.64 → 2506.20] So we're not going to, like you say, this is a target rich environment.
[2506.20 → 2513.12] So the only way that we're going to make progress here is if we make this sort of reproducible
[2513.12 → 2519.80] templates and enable people to run them for their own context and their own data and scale
[2519.80 → 2521.06] things up that way.
[2521.18 → 2526.38] So that was another really appealing thing to me about setting this stuff up is internally
[2526.38 → 2533.40] to SIL, we could rerun this pipeline on any sort of for any language where we have audio
[2533.40 → 2538.68] data to train our own text to speech, but we're not going to get to them all at once, right?
[2538.76 → 2544.50] So other people could run this pipeline with their own speech data on their own cluster to
[2544.50 → 2545.58] create their models.
[2545.78 → 2551.80] And so by creating this sort of reproducible template, it's actually enabling a different
[2551.80 → 2553.04] sort of scaling.
[2553.68 → 2558.26] You know, I touch on the open source, the essential part of open source.
[2558.26 → 2561.20] And I'm admittedly a true believer in open source.
[2561.38 → 2568.96] I was, like I said, at Red Hat for nine years and saw the early days there were recruiters
[2568.96 → 2571.04] told me, why are you going into this Linux thing?
[2571.16 → 2574.34] Polaris is where it's at and where all the money is.
[2574.60 → 2575.78] Polaris isn't where it's at?
[2576.16 → 2576.44] No.
[2576.66 → 2579.30] And I told them, I said, it might not exist in 10 years.
[2579.30 → 2581.26] And they thought, what are you talking about, right?
[2581.26 → 2585.22] And we spent a lot of time in the early days going and saying, what is Linux?
[2585.54 → 2586.98] Why won't it fall over?
[2587.32 → 2589.40] Why would I bet my future on something like this?
[2589.80 → 2594.56] And it's been amazing to watch the transition to an open source over the course of those
[2594.56 → 2597.82] years to become the default model for how things are done.
[2597.90 → 2601.64] It used to be that it would happen, things would happen in a proprietary world.
[2601.96 → 2608.04] And then open source would come along and kind of build a commoditized, almost good enough
[2608.04 → 2608.48] version.
[2608.48 → 2613.74] But nowadays, everything, including most of artificial intelligence work, starts in open
[2613.74 → 2614.16] source.
[2614.74 → 2618.38] And there's a huge advantage, I think, with something like Picketers being completely
[2618.38 → 2624.12] agnostic to the tools that are built on top of it, especially versus some of the pure cloud
[2624.12 → 2631.70] services that have to, because of limited resources, take a fully opinionated stance on
[2631.70 → 2632.30] every project.
[2632.30 → 2638.46] They have to support it for it to run, as opposed to us, which allows data scientists to
[2638.46 → 2643.26] really bring whatever tools they need to the project and then publish anything that
[2643.26 → 2643.88] they create.
[2644.10 → 2648.02] So we don't just have to explicitly support something like PyTorch.
[2648.22 → 2653.56] We spoke with another group that I mentioned earlier was using a more obscure speech recognition
[2653.56 → 2657.60] toolkit called Cali that they had heavily modified themselves.
[2657.60 → 2664.98] And the chances of something like that being supported in one of the cloud providers' choices
[2664.98 → 2669.38] with the limited resources, even if they are a billion-dollar unicorn, and they've got a
[2669.38 → 2672.20] thousand programmers, they still only have so many resources.
[2672.54 → 2678.78] So something like Scikit-learn or PyTorch or TensorFlow and 50 different Python libraries are
[2678.78 → 2679.68] going to get supported.
[2679.68 → 2684.00] Where something like Cali is not going to get supported in the same way that the languages
[2684.00 → 2687.86] are not going to get supported across the world because of resources.
[2688.68 → 2692.84] So allowing people to do things with open source and bring whatever they want to the party,
[2692.84 → 2699.94] I think, allows this kind of collaborative creativity to happen and allows a kind of scaling that
[2699.94 → 2705.06] wouldn't be allowed to happen with smaller projects or being able to move towards languages
[2705.06 → 2706.42] that might not be represented.
[2706.60 → 2709.82] And I think those two concepts are intricately interwoven.
[2710.72 → 2710.84] Yeah.
[2711.14 → 2717.44] I remember, Chris, when we were talking about our talk at Project Voice, one of the things
[2717.44 → 2722.30] that kept coming up is this sort of idea of collaboration for collective impact.
[2722.70 → 2727.98] And the problems that I have are actually not like I can get data for languages.
[2728.30 → 2730.44] I can get information for languages.
[2730.68 → 2733.36] I can get linguistic information for languages.
[2733.50 → 2734.56] I can get dictionaries.
[2734.56 → 2735.40] I can get grammars.
[2735.48 → 2737.22] I can get all of these sorts of resources.
[2737.74 → 2745.72] But I'm limited in certain areas as related to maybe, you know, some of these more infrastructure
[2745.72 → 2746.74] related things.
[2746.74 → 2748.62] I'm related resource wise.
[2749.14 → 2753.04] I work in an organization that's primarily a language related organization.
[2753.04 → 2759.30] And we're doing a lot with AI now, but we're still kind of figuring out a lot of those things.
[2759.30 → 2764.94] Whereas you at Lockheed Martin, you have a lot of resources in terms of computation.
[2764.94 → 2771.40] You have a lot of AI knowledge, but you might not have those language related things that I have easy access to.
[2771.40 → 2782.10] So a great way for us to make an impact in the area of language is in this sort of collaborative way for collective impact, where we're not just kind of siloed in our own world.
[2782.10 → 2787.94] Like Dan Jay was saying, we're not limited to our own sort of implementations, but we can work together.
[2787.94 → 2789.68] We can open source things.
[2789.68 → 2794.62] We can bring all of our resources together to solve kind of larger, harder problems.
[2794.62 → 2795.46] Yeah.
[2795.58 → 2809.78] You know, I think the collaboration that we did, especially for Project Voice and really all along, as I've been learning from you over time about this, is it really brought home where local language is and how important it is.
[2809.86 → 2816.86] I know for me personally, I know I've mentioned before working on humanitarian assistance and disaster relief initiatives at Lockheed Martin.
[2817.08 → 2821.32] And I know we've talked quite a lot about educational impacts.
[2821.32 → 2833.42] You know, it's so critical that you be doing this kind of work, what your two teams are involved in, so that we don't leave behind enormous populations of people on the planet and grow that digital divide.
[2833.54 → 2840.02] I think it's kind of a little bit of a stealth issue to many of us because it's not something we necessarily think about all the time.
[2840.30 → 2849.32] But if there's one thing that I've come to realize in my own introduction to this has been just how incredibly important this is to everybody going forward.
[2849.32 → 2858.18] You can't, in a humanitarian assistance or disaster relief scenario, go in if you can't communicate effectively in the languages of the people that you are trying to work with.
[2858.38 → 2860.14] And same with education, as you pointed out.
[2860.36 → 2872.10] So I think if there's anything I'm coming away with, it's that we're at a very special time for kind of the integration of artificial intelligence and language and that there are so many possibilities that could now be realized.
[2872.10 → 2881.78] And so I guess I want to finish up by asking you both, you know, what do you think the future is looking like for local languages and AI from this point forward?
[2881.84 → 2884.46] It's a remarkable moment we're in at this kind of turning point.
[2884.56 → 2885.66] But what do you see ahead?
[2886.14 → 2895.58] And like, you know, as an example, how do you think SIL would work with Pachyderm and other organizations out there to enable all the possibilities that we have before us?
[2895.58 → 2897.64] I have so many ideas.
[2898.02 → 2900.00] My problem is not lack of ideas.
[2901.54 → 2902.68] I'm so excited.
[2903.08 → 2906.68] And I'm sure, Dan Jay, you probably have a lot of ideas.
[2906.88 → 2909.12] I mean, maybe you can go first.
[2909.30 → 2912.30] I don't want to still always be hopping in first.
[2912.52 → 2913.68] What are you excited about?
[2913.84 → 2914.90] Dive into it, Dan Jay.
[2915.36 → 2915.72] Yeah.
[2916.16 → 2917.00] Steal my thunder.
[2917.00 → 2934.90] Well, you know, I think actually when we had dinner together the other night at the conference, we talked about a larger misconception in artificial intelligence, which is it seeming like everybody's pouring resources into this concept of generalized artificial intelligence.
[2934.90 → 2936.20] And that's a noble goal.
[2936.36 → 2940.78] And I think we get there eventually at some point, maybe even in our lifetimes, maybe not.
[2941.00 → 2944.86] Maybe it proves to be a lot more intractable than we imagine.
[2944.86 → 2949.52] But you said that you were thinking more in terms of augmentation.
[2950.02 → 2968.24] And the way that I tend to think about artificial intelligence these days is very much in that augmentation model as well or that centaur model, right, where the artificial intelligence is helping humans scale their abilities and use their higher order learning and understanding and intuition.
[2968.24 → 2971.84] The types of things that are still intractable in machines.
[2971.96 → 2981.34] We see some of this behaviour that we might be able to call intuition and something like Alfaro as we combine three or four different algorithms.
[2981.68 → 2986.64] And maybe when we've got 20 algorithms working together, we could mimic it even more.
[2987.28 → 2993.52] But in the short term, this was really about scaling and about augmentation and about allowing people to do more.
[2993.52 → 3010.10] And if you think about something like language, especially when you're working with a language where there aren't necessarily as many speakers or there aren't as many experts in that field or there isn't as much data, you absolutely have to have augmentation.
[3010.50 → 3014.00] You have to be able to scale what those folks are doing.
[3014.00 → 3016.80] And that creates more leverage, right?
[3016.82 → 3021.96] If you think about trying to lift a giant rock by yourself, you can only do so much.
[3021.98 → 3027.62] But if you get a really long pole and put it under that rock, you've got a better chance of lifting it.
[3028.32 → 3033.04] And that's the way I think of artificial intelligence now in the speech side of the house, right?
[3033.04 → 3039.36] We need to be able to help all the folks out there if they've only got a thousand experts in a particular field.
[3039.36 → 3058.58] If the work that you're doing is able to combine a lot of different data sets and look across a thousand languages or a hundred languages or 50 languages and find the similarities and therefore make the fact that there is not as much data for that largely irrelevant and still create a very robust translation model.
[3058.58 → 3076.02] That could then make it easier for a thousand different texts to be translated and then a human to go over each of those quick and enhance them versus that person trying to scale themselves to do a thousand different translations and quickly getting burned out.
[3076.02 → 3079.56] And so I think that's really the wonderful part of this aspect.
[3079.80 → 3097.88] And from the Pachyderm side of the house, being able to scale the infrastructure automatically on the back end for folks to help data scientists do this kind of work so they don't have to also be specialists in machine learning operations and trying to figure out how to slice that data set up into a thousand nodes so that they can train it and do preposterously.
[3098.16 → 3103.56] We're very happy to partner and make a big difference in a small impact in what you're doing as well.
[3103.56 → 3105.94] Yeah, I think you hit the nail on the head.
[3106.30 → 3122.08] I think what you got to there at the end around augmentation, but also this sort of idea of leveraging the language information that we have access to and things that are already out there to kind of grease the wheels and get things moving for local languages.
[3122.08 → 3131.46] I really am fascinated by the concept that like we have all these pre-trained models out there, right, for certain languages and for certain language families.
[3131.46 → 3136.06] We have these open data sets, plus we have data sets internal to SIL.
[3136.96 → 3144.12] We also have this Ethnologue resource, which is information about all the languages of the world and how they're related.
[3144.40 → 3150.28] I'm just really fascinated by the idea that we could have all of that information together.
[3150.28 → 3159.20] So what languages exist, what are their populations, but also what languages currently have data and what languages currently have pre-trained models.
[3159.20 → 3168.34] And that way, when we have a packet or in pipeline, let's say, and we want to train a new text to speech model, or we want to train a new machine translation model.
[3168.34 → 3179.40] If we put in the front end, like, oh, I want to train a new language, you know, Kaunda, an Angolan language that doesn't currently have any support.
[3179.98 → 3195.96] What is the closest related language that has either a pre-trained model or has a lot more data and kind of use tools like AutoML and some of this automation to pull those resources in and sort of augment the development of that next language.
[3195.96 → 3202.10] Those are the things that really, you know, excite me and fascinate me and excited to dig more into.
[3202.76 → 3205.10] Well, this has been a truly fascinating conversation.
[3205.34 → 3206.76] I know I learned a lot.
[3207.08 → 3216.02] Thank you both for kind of diving deeply into local languages and how AI can impact and move that right along for the benefit of all.
[3216.16 → 3218.20] Truly an AI for good initiative.
[3218.60 → 3219.72] I'm pretty excited about it.
[3220.02 → 3224.28] And so Daniel Whiten ack, Daniel Jeffries, thank you both for coming on the show.
[3224.90 → 3225.34] Thank you.
[3225.34 → 3226.28] Thanks for having us.
[3226.34 → 3227.14] Really appreciate it.
[3230.14 → 3235.04] Comment on this and every episode of Practical AI on changelog.com.
[3235.20 → 3240.12] Just pop open your show notes, click the discuss on changelog news button and let your voice be heard.
[3240.54 → 3242.10] Hey, do you have a friend who'd enjoy the show?
[3242.40 → 3248.78] Shoot them a quick text or an email, slack them, WhatsApp, send them a Snapchat, I don't know, write a message in a bottle, throw it into the sea.
[3248.96 → 3250.94] We don't care how, but we do appreciate the effort.
[3251.44 → 3254.22] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[3254.22 → 3256.10] It's produced by me, Jared Santo.
[3256.44 → 3258.88] Our music is by the Beat Freak, Break master Cylinder.
[3259.18 → 3260.78] And we're brought to you by awesome sponsors.
[3261.22 → 3261.82] Support them.
[3261.96 → 3262.70] They support the show.
[3262.92 → 3266.76] We've got Vastly on Bandwidth, Linde on Hosting, and Rollbar on Bugs.
[3267.22 → 3268.90] Are you receiving our free email every Sunday?
[3269.10 → 3270.22] If not, you're missing out.
[3270.42 → 3273.52] It's our editorialized take on this week in the world of software.
[3273.70 → 3275.00] What's interesting and why.
[3275.22 → 3277.36] Head to changelog.com slash weekly to check it out.
[3277.56 → 3279.12] Subscribe for the price of a free egg roll.
[3279.48 → 3280.30] Thanks again for listening.
[3280.52 → 3281.40] We'll talk to you next week.
[3281.40 → 3281.42] We'll talk to you next week.
