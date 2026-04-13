[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 23.38] on Linde servers. Head to linode.com slash Changelog. Welcome to Practical AI, a weekly
[23.38 → 28.28] podcast about making artificial intelligence practical, productive, and accessible to everyone.
[28.28 → 33.86] This is where conversations around AI, machine learning, and data science happen. Join the
[33.86 → 37.92] community and snag with us around various topics of the show at Changelog.com slash community.
[38.46 → 42.02] Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[46.70 → 51.90] Welcome to another Fully Connected episode where Daniel and I keep you fully connected with everything
[51.90 → 56.42] that's happening in the AI community. We'll take some time to discuss the latest AI news and dig
[56.42 → 62.04] into learning resources to help you level up on your machine learning game. I am your co-host,
[62.28 → 68.60] Chris Benson. I am Chief AI Strategist with Lockheed Martin RMS APA Innovations. And with me is my co-host,
[68.76 → 72.72] Daniel Whiten ack, data scientist with SIL International. How's it going, Daniel?
[72.86 → 74.66] It's going great. How about with you, Chris?
[75.02 → 79.66] It's going very well. I am very excited about this episode. We've been talking about having one here
[79.66 → 85.98] around New Year's, give or take. And we are going to talk a little bit about the year behind and the
[85.98 → 91.16] year ahead. We've had so much happen that I am fully, fully psyched about this. But, you know,
[91.22 → 95.82] not the least of which is, hey, we have done essentially our first year of the Practical AI
[95.82 → 99.00] podcast. Got some content out there. We started a thing. How about that?
[99.00 → 104.40] We did start a thing. And you pointed out to me a little while ago that we have 25 episodes out.
[104.60 → 109.34] And, you know, when you're hosting a show like this, and we tend to get into our rhythm of putting
[109.34 → 114.04] them out. And I think it just hit me that we had a lot of content out there and a lot of stuff that
[114.04 → 118.20] I think we're both pretty proud of. Some pretty amazing episodes and guests that we've had this
[118.20 → 124.70] past year. Yeah. So thank you out there to all the loyal listeners and those that have been with us
[124.70 → 129.92] from the beginning and also those that are maybe this is you're just joining for the first episode.
[130.08 → 136.32] We're really excited that this thing exists now and that we're able to talk about AI
[136.32 → 142.66] practically and bring on a bunch of awesome guests and have these conversations. It's been super great.
[142.76 → 150.32] We've talked to people from NVIDIA and Google and all over the place. It's been it's been a great
[150.32 → 154.56] year. You know, one of the things I really love is the community that we've that we've
[154.56 → 159.56] built up. And a lot of our listeners have joined the Slack community and joined us on LinkedIn
[159.56 → 165.18] and give us feedback and suggestions. And I got to say that when you wake up in the morning,
[165.18 → 169.68] like I did this morning, and we had a new listener who had joined the Slack community and was just
[169.68 → 173.74] saying, hey, great job. And they say where they're listening from. It's it just feels amazing.
[174.16 → 179.40] And so I hope that more folks will engage us in a very direct way. Its this is not just a
[179.40 → 185.70] one way conversation. Yep. Looking forward to a great 2019 of episodes. If is you have suggestions
[185.70 → 191.12] for topics you want to hear about, please let us know in Slack or on LinkedIn. And we're just really
[191.12 → 196.36] excited to get more plugged into the community and talk about the things that are on people's
[196.36 → 200.78] minds and the things that they're having success with, the things that they're struggling with as
[200.78 → 206.82] far as AI goes. Yep. So I guess to kick things off, you know, what really stood out to you in 2018?
[207.58 → 213.60] Yeah, I mean, we talked about a ton of things on the podcast. Of course, we talked to a lot of people
[213.60 → 219.80] both recorded and not recorded as associated with the podcast, but also we're in the community. And,
[220.08 → 224.78] you know, I've talked to a ton of people doing workshops and other things. And I think one of the
[224.78 → 230.52] things that stood out to me this year, in terms of what people were talking about when they came on the
[230.52 → 235.76] show and what I heard people talking about at conferences and that sort of thing was really
[235.76 → 242.84] around, you know, transitioning from talking about AI and machine learning in a strictly supervised
[242.84 → 251.66] setting to these more complicated ways of framing problems. And, you know, things like semi supervised
[251.66 → 258.94] learning and generative models, reinforcement learning. We heard about this a lot, you know, at least I did
[258.94 → 266.30] both on the show and off the show. We talked to Wojtek Marimba from OpenAI and episode 14 talking about
[266.30 → 272.30] robots and reinforcement learning. And this came up several times and in other conversations as well.
[272.42 → 279.22] And I think that this is a general trend that we saw in 2018, the people pushing AI and pushing it with
[279.22 → 285.72] this kind of more challenging problem statements and methodologies rather than just a strictly supervised
[285.72 → 291.60] setting. I think that's really insightful. The field of deep learning and AI in general has really
[291.60 → 298.58] expanded in 2018. I think when we were starting the year out a year ago, most of the conversations I was
[298.58 → 306.38] having were around supervised learning. And, you know, we were talking about CNNs, we were talking about
[306.38 → 312.98] RNNs. And really, I think there was discussion of GANs that were out, but not a lot of people that I was
[312.98 → 318.32] talking to knew what to do with them. And we've really seen an explosion of use cases for these new
[318.32 → 324.48] architectures this year. And what this technology can do in real life in a practical sense has really
[324.48 → 325.98] broadened over that time period.
[326.40 → 332.30] Yeah, that's well put, Chris, in the language that you just said. And speaking of speaking and language,
[332.92 → 338.02] I think that one other thing that really stood out to me over this year, which I think is really
[338.02 → 345.66] exciting as kind of a shift, almost a shift back or towards natural language methods. We saw for a
[345.66 → 351.06] long time, mostly what people are talking about with deep learning, especially was image based and
[351.06 → 358.02] video based stuff. So, you know, style transfer and facial recognition and other things. But I think over
[358.02 → 363.52] the past, you know, three, four or five months, and really, maybe throughout the year, maybe I just
[363.52 → 370.02] started noticing it recently. But there seems to have been a shift to a lot of focus on natural
[370.02 → 377.88] language processing. We had the episode where we dove into BERT, which was episode 22, which seemed
[377.88 → 382.62] to be getting a lot of press at the time. Of course, there were a lot of other advancements in natural
[382.62 → 385.52] language. And I think that will influence what happens in 2019.
[386.38 → 392.56] You know, I think you're absolutely right with the NLP really, really, you know, became part of the AI,
[392.56 → 397.68] you know, conversation in a much bigger way this year. I know that I was at a former employer.
[398.32 → 403.96] And beginning of the year, the NLP conversation was really not an AI conversation. It was not
[403.96 → 409.02] about neural networks. It was about some of the older legacy techniques. And over the course of the
[409.02 → 414.80] year, really deep learning took hold in the NLP world for us. And that way. So I'm speaking in a
[414.80 → 421.00] very personal sense. And watching that, watching that transition and an organization and a large
[421.00 → 426.06] organization that was moving into this new set of technologies to drive its business forward was
[426.06 → 432.04] pretty exciting. And then obviously, with BERT's release, the excitement around NLP is really
[432.04 → 433.38] skyrocketed in a big way.
[434.06 → 441.08] Yeah. And I think the other thing that I've noticed skyrocket as of recent is fears about AI. Do you hear
[441.08 → 446.54] about this as you're as you're talking to your as you were at the Thanksgiving table with your
[446.54 → 449.28] friends and family? Were you talking about the fear of AI?
[449.94 → 454.34] Well, I wasn't at the Thanksgiving table because my wife has forbidden me from doing so.
[455.14 → 461.44] It's off limits for me, lest I drive her insane because I never stop. But I do hear about it. I know
[461.44 → 467.58] that we both do a lot of conference talks and stuff. And there's rarely conversation or talk that I get
[467.58 → 473.94] into where that's not asked where either the question of jobs or the question of other fear-based
[473.94 → 480.40] things are out there. And so I spent a fair amount of time trying to share with people what,
[480.40 → 486.16] you know, what, in my view, is real and what's not and trying to take the fear out of it, so people can
[486.16 → 491.44] make rational judgments about how these tools can be used in all sorts of use cases.
[492.12 → 498.88] Yeah. And I'm thinking back to our episode 25, the most recent one with Susan Ettinger,
[498.88 → 505.34] where we kind of talked about this kind of Terminator or singularity thing really distracting
[505.34 → 511.42] from a lot of the real world dangers of AI that we're experiencing now around bias and government
[511.42 → 517.42] use of AI and other things. And so, yeah, I mean, I guess it's not so those questions around
[517.42 → 522.90] consciousness and other things are interesting. And I think that, you know, someone should be having
[522.90 → 529.56] those conversations, probably. In this year, it seems to have shifted the conversation more towards
[529.56 → 535.36] those things and away from, you know, distracting from things that are really happening practically
[535.36 → 538.20] that are problems for us as AI practitioners.
[538.50 → 539.34] I agree.
[539.60 → 545.30] Yeah. So hopefully, I mean, I hope really that's a trend that is corrected or at least expectations
[545.30 → 546.78] are set a little bit better.
[547.04 → 551.46] I think it started. I think that's going to keep going for a while because there's a lot of people
[551.46 → 555.82] out there that whose lives are not nearly as entwined in AI as ours are, and they're just
[555.82 → 560.70] coming into the conversation. And so, but I think, I think the bottom line is to the best of my
[560.70 → 565.90] knowledge, there's no substantial research pushing forward consciousness. That's not what AI is in the
[565.90 → 573.58] foreseeable future. So that entire line of speculative thinking, there's not really a basis in fact for that
[573.58 → 577.58] at this point. And I think, I think, I suspect you and me and a lot of other people in this field are
[577.58 → 581.82] going to continue to have to message that out to people that are just really learning about this
[581.82 → 586.90] new for that to get by. So I'm, I'm, I'm pretty tolerant with it. I think it's just a question of
[586.90 → 587.76] ongoing education.
[588.68 → 597.78] So quiz, Chris, there in my mind were two huge things that rocked the AI machine learning software
[597.78 → 605.54] engineering world this year that really stand out to me. I'm curious if those same things come to your
[605.54 → 609.64] mind. Do you know what I'm talking about? I can guess at it. We've talked a lot. So I'm probably
[609.64 → 616.22] guessing at least one of those I'm guessing is the GDPR. Yes. The year of the year of the GDPR.
[616.38 → 621.02] It's very exciting depending on, depending on your perspective, I guess.
[621.50 → 626.10] And for those who don't know, that's the European in the, in the EU, the general data protection
[626.10 → 634.04] regulation, which is the first large scale regulation of data and AI technologies out there. And it's,
[634.04 → 639.36] it's certainly a it's certainly an imperfect with its, it has people for and against not only it as
[639.36 → 645.06] a whole, but different aspects of it. But we're now in a world where regulation and AI is, is something
[645.06 → 650.28] to think about and consider and maybe a reality. So that definitely rocked a lot of people on their
[650.28 → 655.98] heels this year. Yeah. If you're interested in, I mean, there's definitely implications for machine
[655.98 → 661.84] learning and AI practitioners based on the GDPR around explainability of your models and what that
[661.84 → 666.98] exactly means. Some of the finer points in the details of that we discussed in, in episode four
[666.98 → 672.66] with some individuals from the company Immune. Um, I think that was really instructive and I kind of
[672.66 → 679.80] learned a lot, uh, of, you know, what I should expect at least in the near future, as far as GDPR
[679.80 → 684.72] from that conversation. But it, it made me, you know, consider that it's a serious thing,
[684.72 → 691.46] but maybe not it tempered a few of my fears, I guess. So yeah, Matthew, Carol, and Andrew Burt from
[691.46 → 695.90] Immune definitely for my perspective, they definitely schooled me in that. So I came away
[695.90 → 700.24] from that episode with a different perspective from the start of the recording, certainly. And
[700.24 → 705.98] that, that definitely helped educate me along the way. Yep. So what's the what do you think is the
[705.98 → 711.40] the second thing that, uh, I was guessing you're thinking maybe Cambridge Analytica,
[711.40 → 716.28] cause that was big or am I on the wrong track? You're reading, you're reading my mind. Yep.
[716.38 → 722.10] Am I? Okay. I wasn't as sure about that one. Yeah. So I think probably whether you were in
[722.10 → 729.16] AI or not in AI, you probably heard about a lot about Facebook and Cambridge Analytica this year and
[729.16 → 736.54] a lot of snapshots of Mark Zuckerberg and with kind of weird looks on his face, which, uh,
[736.82 → 740.44] was definitely an interesting period of, of 2018 for me.
[740.44 → 745.22] In a non-technical sense, I think that the thing that really stuck in my mind was watching some of
[745.22 → 750.90] the hearings associated with that and realizing that our U S Congress people, uh, really had a lot
[750.90 → 756.08] to learn. They really were clueless. I w I remember watching that on YouTube and other things and just
[756.08 → 763.88] going, wow, somebody, somebody needs to educate Congress a bit. Yeah. I think it's definitely an
[763.88 → 770.00] eye-opener, but I think also it's, it's one of those things where for us working in this industry that,
[770.00 → 778.62] that utilize data and AI, I think we need to, uh, kind of reset our expectations for what we,
[778.62 → 784.86] we think people know about the technology that they use. And also, you know, maybe have a little
[784.86 → 791.54] bit more empathy as we're, as we're creating, creating technology, not really assume that people
[791.54 → 797.12] are totally aware of that. They're always reading the terms and conditions, or they know,
[797.12 → 803.18] you know, they know or expect how we're using their data and that sort of thing. So I think
[803.18 → 810.14] that kind of, uh, reset that empathy for me, I think. Yeah. You know, the other thing about 2018
[810.14 → 816.82] that really struck me was the maturing process that the whole field went through, uh, everything from
[816.82 → 823.14] open source tools to how organizations were entering into this new space and trying to figure it out.
[823.14 → 828.80] I had a kind of, as a personal, I had, uh, previously I had been with Accenture and then
[828.80 → 832.76] I went to Honeywell for a while. And then I'm currently with Lockheed Martin. And as I've gone
[832.76 → 836.26] into each of these, then these are large organizations, you know, that with, with,
[836.26 → 842.70] with commitments to these technologies. And as I've gone, the maturity of each one,
[842.92 → 849.12] figuring out how it was going to do to have operations around this has had, uh, has,
[849.12 → 853.46] I've seen a lot of advancement considering how short a time it's been. We're now seeing, uh,
[853.46 → 858.94] a lot of the large organizations involved offering their best practices and, and those are getting
[858.94 → 863.02] incorporated. And I know we've talked about those, uh, that, uh, a number of times in our episodes.
[863.22 → 868.06] So we're just seeing a maturing of this industry, uh, going at, at just breakneck,
[868.24 → 873.28] breakneck pace as, as well as, uh, open source projects and frameworks that are advancing, uh,
[873.28 → 878.26] at lightning speed. Yeah. I'm, I'm just reading a list. Well, we'll put a bunch of links from this
[878.26 → 883.44] show in the show notes, of course, but just looking at a list from, from one article about,
[883.44 → 888.70] you know, about all the open source projects that were introduced or significantly updated this,
[888.70 → 894.28] this year as related to AI. And, you know, of course there were, uh, things like horizon
[894.28 → 901.48] from Facebook for, uh, reinforcement learning. There were various libraries for graph nets and other
[901.48 → 907.54] things from, from deep mind and just a ton of stuff, uh, happened and was open source this year.
[907.54 → 914.24] And that's, that's really exciting to, to look at, um, as you know, a whole, uh, toolkit of things
[914.24 → 920.44] that we can use in, in 2019. Yeah, I agree with you. It's, uh, compared to the beginning of the year,
[920.50 → 925.60] the number of different tools come out and the number of different, I guess, constituencies that
[925.60 → 930.66] they were appealing to, not just data scientists, but software developers, people in different
[930.66 → 936.30] programming languages, different ways of, of approaching it, whether it be, uh, things like
[936.30 → 941.76] auto ML and, and you'd hear people that were talking about TensorFlow or maybe upcoming TensorFlow
[941.76 → 949.62] too versus PyTorch and that whole discussion. Um, it's really, really democratized the field in the
[949.62 → 955.50] past year, having so many new capabilities and tools to where there's now quite a lot of choice
[955.50 → 961.38] in, in how you might choose to get into the field. Okay, Chris. So in 2018, of course,
[961.38 → 967.62] we talked about a bunch of amazing stuff on the show. We started the show, we recorded 25 episodes.
[967.84 → 974.92] We talked about everything from ethics to natural language processing to robots. What do you think
[974.92 → 981.78] we're going to be talking about in 2019? Or what do you want to see on the show in 2019? What are
[981.78 → 985.84] going to be some of the biggest topics that you think are going to be coming across our desks this
[985.84 → 990.74] coming year? Well, I think a lot of the conversations that we have already started are going to continue
[990.74 → 997.06] to develop and grow and mature. Not the least of which is the issues of trust, transparency,
[997.06 → 1002.30] and there are so many aspects of that. There's, there's, there's bias. We've already talked about
[1002.30 → 1009.94] regulation and different types of use cases, uh, on how we use these tools there. We've just started
[1009.94 → 1013.78] down that path. And I think that's going to be something we'll see a lot this year and a lot in the
[1013.78 → 1019.90] years ahead. Any thoughts maybe on bias? I know you, I've heard you bring up bias so many times
[1019.90 → 1022.80] through our episodes. I'd love to hear your thoughts on where that's going.
[1022.80 → 1030.02] Yeah. I mean, I think bias and also like government and large organization use of, of ML is something
[1030.02 → 1037.72] that I hope we'll be talking about a lot. I think it's, um, you know, one thing that, that I kind of
[1037.72 → 1043.14] think happened in, in 2018, as we already talked about was people's eyes were opened somewhat through
[1043.14 → 1049.50] Cambridge Analytica and other things about some of the ways that we're using data. And if we're using
[1049.50 → 1055.92] data in those ways to do these things, whether it's in hiring or advertising or, uh, social media
[1055.92 → 1062.62] influencing and all of those things, then bias in our data sets really becomes a problem. And also
[1062.62 → 1068.66] there's probably certain things that we really just shouldn't be doing. You know, we've, we brought
[1068.66 → 1074.30] up the use case of government use of facial recognition a few times on the, on the show.
[1074.30 → 1080.26] Of course, that's a big controversy right now. So I think people's eyes have been opened in 2018 to
[1080.26 → 1087.14] how their data is being used somewhat. And, um, in 2019, I think there's got to be kind of more
[1087.14 → 1095.78] reckoning around how we can actually develop trust in systems based on AI methodologies. And also it's
[1095.78 → 1101.90] going to be, I think it's going to weigh on us as practitioners to make some of those methodologies
[1101.90 → 1107.98] a little bit more transparent and interpretable, especially, you know, as we're forced to more and
[1107.98 → 1116.64] more by things like GDPR. So yeah, I think 2018 was kind of a year of eye-opening and 2019 maybe will be
[1116.64 → 1120.32] a year of practical reckoning. And in some ways, I hope.
[1120.88 → 1124.88] I think you're absolutely right. No, I hope you're right. I would even say that, you know,
[1124.88 → 1129.28] we, we talked about, you know, so much of the conversation in 2018 had been around
[1129.28 → 1134.98] fear of AI and, and such. And I think that this is a big part of the solution to that
[1134.98 → 1140.46] is if we can focus on trust and transparency much more so than we ever have had to do with
[1140.46 → 1146.92] previous technologies and understand and explore what's possible and, and then, you know, why we
[1146.92 → 1151.80] may not want to go down certain paths or how we do certain paths safely is really crucial.
[1151.80 → 1159.36] So I've been really happy this past year to see kind of the, the ethics of AI be such a big part
[1159.36 → 1164.06] of the conversation. And I really think that's going to continue going forward. And I think,
[1164.14 → 1169.50] I think the realization that that has to be right up there with your technical solutions in almost
[1169.50 → 1174.54] every conversation is a big part of where things are going in the months ahead. And I know that we,
[1174.80 → 1180.12] you and I talk a lot about AI for good. We try to illustrate all the, the amazing, we've had so many
[1180.12 → 1186.62] guests that have done some pretty amazing things in some cases, life, life-saving techniques that
[1186.62 → 1192.04] they've used AI tools to achieve. And so I would like to see us do more of that going forward.
[1192.04 → 1197.96] And I'm hoping that if we continue to have this trust and transparency and ethical conversations
[1197.96 → 1202.54] about the tool set as part of our right alongside our technical conversations,
[1202.54 → 1209.46] we're less likely to make missteps and, and, and maybe the worry about fear-based outcomes will,
[1209.60 → 1210.48] will start to diminish.
[1211.04 → 1219.34] Yep. Now, speaking of, of more trends for, for 2019, you and I have, have talked quite a bit. I have,
[1219.48 → 1225.22] I have confidence that, that you're a real person, but our listeners have, have listened to us and,
[1225.22 → 1231.66] you know, never met us in person. So, um, likely this last year, they would have assumed that we're real
[1231.66 → 1239.94] people because we talk like real people. But I think in 2019, the AI assistants and the, the, uh,
[1239.94 → 1247.38] way that they're able to be conversational and better, uh, generative voice techniques and text
[1247.38 → 1253.24] to voice techniques kind of combined with these NLP techniques that we already brought up around BERT
[1253.24 → 1259.28] and other things. I think that's all going to be kind of a, a perfect storm to advance AI assistance
[1259.28 → 1265.70] and, and voice interfaces and such where maybe in the end of next year, there will be some,
[1266.08 → 1270.88] at least some conversations we have where it's maybe not as obvious whether we're talking to a
[1270.88 → 1275.24] computer or a person. What do you think? I know, I totally agree. And we've already seen
[1275.24 → 1281.98] specific instances of those happening. We obviously saw the demo. I think it was, uh, Amazon,
[1281.98 → 1287.42] uh, duplex. Is it duplex? Is that maybe it was? Yeah. We've had so many things this year when,
[1287.42 → 1291.54] where they were indistinguishable, you know, that, that AI assistant was indistinguishable.
[1291.60 → 1296.30] It sounded human. And there are a number of organizations working on that. And then when
[1296.30 → 1301.62] you combine that with what GANs generative adversarial networks have been doing, especially
[1301.62 → 1308.40] on image generation, just last week, I was sharing a post that was, had a bunch of,
[1308.40 → 1313.28] you'd swear they were real people's faces. I mean, they were indistinguishable from a photograph
[1313.28 → 1319.86] and none of those people were real. And if you take that kind of capability and apply it, uh,
[1319.86 → 1325.46] within, within a video context and have this, uh, this conversational capability that's evolved,
[1325.46 → 1332.38] then yeah, the ability for us to distinguish between us as real human beings and, and, you know,
[1332.60 → 1338.06] essentially AI assistants that are, that appear to be, but maybe not. Um, and that obviously raises
[1338.06 → 1342.66] more of the ethical questions and how do you, how do you interact? What does that user experience,
[1342.86 → 1346.08] uh, what should it be? When you, when should you know you're talking to a human?
[1346.60 → 1352.50] Absolutely. And, um, it also reminded me of something else. Um, I know that, uh, a stat that I,
[1352.58 → 1357.50] I throw out commonly at talks is that Gartner a while back was predicting that by 2025,
[1357.50 → 1364.30] half of all of our primary care in, in terms of medical attention would come through AI assistance.
[1364.30 → 1368.36] And I know when they first put that out, I was thinking, well, some of it, but I, you know,
[1368.36 → 1372.60] I don't know, but I'm, I think they might be right. And maybe even most of our medical care,
[1372.60 → 1378.70] because if you have this ability to have that visual and audio experience that is almost
[1378.70 → 1384.54] indistinguishable from talking to a human, all the, uh, AI enabled medical capability that might
[1384.54 → 1389.68] be behind that, then yeah, I think, I think the way that we are living our lives in terms of seeking
[1389.68 → 1394.78] primary care and lots of other use cases really change over the next few years. And we may see
[1394.78 → 1400.50] a lot of that this coming year. Yeah, for sure. And I mean, a lot of that is going to come in the
[1400.50 → 1407.88] form of new products. I think for us on this show, one trend that I think has already started,
[1407.88 → 1414.62] but I think is just going to be a huge trend in 2019 is a focus on practicality. And by that,
[1414.62 → 1419.58] I mean, kind of less of a focus on what can you do with deep learning in terms of research
[1419.58 → 1426.04] and more of a focus on how can we take these techniques, develop good processes around them,
[1426.18 → 1431.20] integrate them into software systems, integrate them into APIs, integrate them into mobile apps.
[1431.56 → 1437.56] How can we train our, you know, our data scientists, our AI people better so that they're actually better
[1437.56 → 1442.62] at building things, not just good at proving out research ideas, but better at building things.
[1442.62 → 1448.52] And then also the development of, you know, kind of system integrations and infrastructure that will
[1448.52 → 1457.48] really support that infusion of AI products and the development of those AI products into a company's
[1457.48 → 1466.16] workflow. Totally. I think inferencing APIs, prediction APIs are going to become so standard in our stacks,
[1466.24 → 1472.06] in our software stacks that are running our organizations, our enterprises, that it'll seem almost
[1472.06 → 1477.10] funny to look back, not too far down the road and look back and think, well, of course it was, it was kind of obvious.
[1477.54 → 1481.26] I think a lot of, a lot of people are still trying to wrap their heads around that right now.
[1481.40 → 1485.68] We're seeing a race to the bottom in terms of commoditization happening right now.
[1485.96 → 1492.04] And in terms of democratization of the field, we've already talked about the immense number of tools
[1492.04 → 1496.46] that came out in 2018. That only seems to be accelerating as we go into 2019.
[1496.46 → 1501.68] And that's allowed a lot of people who are not strictly data scientists by background to get into
[1501.68 → 1507.02] this field. And as you start having some software engineers and developers that have an interest in
[1507.02 → 1513.58] this moving largely over into doing inference-based programming, it will no longer be the domain of
[1513.58 → 1517.64] just data scientists anymore. And I'm hoping to avoid the hate mail from data scientists, but I think,
[1517.74 → 1523.20] I think that you're going to see just as once upon a time, you had computer scientists focusing mainly
[1523.20 → 1528.56] on programming. And then that democratized early as the internet came out. And I think we're seeing
[1528.56 → 1534.18] the beginning of a similar trend where it will be accessible to so many more people going forward.
[1534.64 → 1539.42] Yeah. And I think it's, in my opinion, it's not. So I do think you're right in terms of
[1539.42 → 1546.14] a lot of this kind of being a new layer in the software stack that's accessible to kind of non-AI
[1546.14 → 1551.62] experts. But I also think that there's going to be a lot of pressure on data scientists and AI
[1551.62 → 1558.02] people themselves to really be more responsible with the way that they build things and additional
[1558.02 → 1563.96] tooling around that. So we had the conversation with Joe from Packager in episode 23, which is
[1563.96 → 1570.06] really an infrastructure for AI. There are projects like Below and others that are really meant to
[1570.06 → 1578.94] provide a platform for responsible and tracked and versioned and scalable, both training and inference
[1578.94 → 1584.94] on common infrastructure like Kubernetes, which is a container orchestrator. So I think that there's
[1584.94 → 1591.76] going to be pressure on data scientists and AI people to say, not just like figure out a good way
[1591.76 → 1597.54] to do this and do your research job, but to actually say, okay, you know, step into the role of actually
[1597.54 → 1604.58] building something that scales and can be integrated into our systems and be more involved in the
[1604.58 → 1611.42] on the engineering side of things and maybe less on the cutting edge research sort of things. Although I'm sure
[1611.42 → 1617.14] that there will still be organizations that focus on research. I think people have figured out that yes, we can
[1617.14 → 1624.08] apply AI in the real world, but we need some tooling and infrastructure around it. I think that that's going to
[1624.08 → 1625.10] increase this coming year.
[1625.74 → 1631.64] Yeah, I think the thing that's really driving this field is the amount of money that is pouring into it. And the reason that
[1631.64 → 1637.34] money is pouring into it is because you are, you're getting a return on your investment. So, and that is done
[1637.34 → 1643.32] by generating products and services where AI technologies are enhancing those, you know, they're, they're helping
[1643.32 → 1648.50] you better serve your customer. And so because of that, there will always, I think, you know, research will
[1648.50 → 1656.58] continue to grow, but I think the explosion of numbers of people, practitioners who are getting in to generate
[1656.58 → 1661.38] their own products and services, just like we saw in the software engineering world, where they're no longer
[1661.38 → 1664.62] trying to figure out the new protocol, but they're saying, Hey, we have a bunch of great tools. Now
[1664.62 → 1668.70] let's go out and make stuff and sell it to our customers. That's really going to drive it. And
[1668.70 → 1675.06] because of that, I think you're going to see so much growth on the product and service creation side,
[1675.20 → 1680.36] even though both are growing rapidly, it will almost eclipse the research side because for everyone
[1680.36 → 1684.70] that's doing research, you're going to have many, many, many that are out there generating products
[1684.70 → 1689.10] and services that they can make a profit on. So I think we're, we're, we're already starting to see us
[1689.10 → 1696.90] turning very much that way. And I've seen, even in just 2018, I saw a substantial swing toward that
[1696.90 → 1702.04] direction. It's no longer at the beginning of 2018, a lot of organizations were just thinking
[1702.04 → 1707.42] about getting into AI. As we get into 2019, many of those organizations are now trying to do it.
[1707.42 → 1708.34] They're at least starting.
[1709.22 → 1715.34] And obviously they can automate it with AutoML, which we talked about maybe a little bit this last year,
[1715.34 → 1722.90] but I think people will be talking about it more in 2019. What are your feelings on AutoML?
[1723.24 → 1729.48] So for those that maybe are new to AutoML, there's a whole series of techniques that are kind of
[1729.48 → 1735.26] lumped into this discussion around AutoML, which basically is kind of like machine learning on machine
[1735.26 → 1741.80] learning. So doing machine learning to kind of adjust or modify your neural network architecture,
[1741.80 → 1746.80] the layers of your neural network or doing machine learning to figure out the best sort of,
[1746.80 → 1752.28] you know, loss function or way to do gradient descent or, you know, updates or whatever it is.
[1752.52 → 1757.90] There are a lot of automatic techniques to kind of figure out these things. Up until recently,
[1757.90 → 1763.90] I think a lot of those were experimental, but of course there's, there are products now built around
[1763.90 → 1769.38] AutoML. What is, what is your impression about what, what AutoML will be in 2019, Chris?
[1769.38 → 1773.88] I think a lot of organizations are just starting to look at it. And when it kind of came out,
[1773.94 → 1778.22] it rocked the world, you know, in terms of, you know, people going, oh man, you know,
[1778.24 → 1782.26] it was a totally different way of thinking about this field as a tool. And it kind of,
[1782.42 → 1787.00] it was a revolutionary thought, but I think we're, I think it was the first of many innovative tools
[1787.00 → 1793.36] that we're going to be seeing in the coming years, a lot of them in 2019, that is making this
[1793.36 → 1800.46] field more accessible. I think early on, there was a naivety that because of the mathematical
[1800.46 → 1806.58] underpinnings and because of the, the technical barriers to entry that it would, that a lot of
[1806.58 → 1811.08] people assume that there would be a fairly narrow set of people that could engage in this, but you're
[1811.08 → 1816.70] seeing these innovators in, in this case, AutoML, it's Google just doing amazing work to make,
[1816.84 → 1823.02] to make this, this set of tools more accessible. And so I think I'm a big fan of AutoML. I think it has
[1823.02 → 1828.36] a long way to go, and I think it will grow a long way as well, many other similar tools, but this is
[1828.36 → 1832.12] one of the reasons I really believe that this field is opening up. It's becoming so much more
[1832.12 → 1841.44] accessible. So I kind of think AutoML is cool, disclaimer, but I'm also skeptical about its, you know,
[1841.90 → 1848.50] widespread use in, in 2019, practically. I think that it's interesting. I think it will be utilized
[1848.50 → 1855.34] in certain, in a certain limited set of scenarios in the real world, maybe those that are more, uh,
[1855.34 → 1861.62] more standardized, but, uh, but I'm a little bit skeptical about it. It's, it's widespread use.
[1861.70 → 1866.50] So hopefully I'm not offending very many people out there. I do, in my mind, the thing that is,
[1866.68 → 1874.20] would drive much more kind of, uh, democratization of machine learning and AI is transfer learning.
[1874.20 → 1879.84] I think that's kind of the at least my mind in 2019, a lot of what's going to drive,
[1879.92 → 1886.34] you know, application of, of complicated machine learning models and industry is, uh, is transfer
[1886.34 → 1892.82] learning, which is the ability to kind of take, take a model that was trained on for one task and
[1892.82 → 1900.12] then transfer, transfer it to, uh, another task via some fine-tuning. So that's my personal opinion.
[1900.12 → 1904.46] And I'll, I'll get that out of the way on this show. No, I think, I think that's a fantastic point.
[1904.46 → 1909.10] And I, and we have discussed this in the past and kind of to reiterate, I know that in my own
[1909.10 → 1916.40] experience, transfer learning is almost the gateway into implementation because in reality, you know,
[1916.42 → 1920.82] a lot of people, as they get into this, and they are not neural network research scientists, and
[1920.82 → 1924.72] they're going off and creating their own architectures from scratch, you might go into Google brain.
[1924.72 → 1930.32] And that is a very common thing for people at that level. But for a lot of midsize companies,
[1930.32 → 1934.42] or, you know, it's a couple of people speculative, speculatively getting into it and trying to talk
[1934.42 → 1938.54] their managers into it. What they're really doing is they're taking their framework of choice and
[1938.54 → 1942.58] they're looking through the example capabilities and saying, you know what, this thing, my boss wants
[1942.58 → 1948.44] me to do. It's not so dissimilar from this example I see here. And they take it, and they try to make
[1948.44 → 1953.48] the adjustments to get that to work in their own world and, and, and move in. So I, it's really,
[1953.48 → 1956.28] that's how it's done in real life for most people.
[1956.90 → 1960.90] Yeah. And I mean, you've kind of brought up cultural shifts in that statement,
[1960.90 → 1965.92] and that would certainly maybe be one cultural shift. Are there others of those that you,
[1966.16 → 1973.56] I mean, you're probably more in a standard enterprise setting than I am or have been over
[1973.56 → 1978.12] the past few years. What do you see with regard to those cultural shifts in that setting?
[1978.70 → 1983.30] Yeah, I'm definitely seeing that. And I was at a lot of smaller or mid-sized organizations
[1983.30 → 1988.68] for a while, but in recent years, I've been with these large organizations and very much by design,
[1988.84 → 1994.54] super happy with where I'm at now because of that. But what I'm really seeing is that as the
[1994.54 → 2002.86] maturing of this field is coming about so rapidly, and these data oriented possibilities are getting
[2002.86 → 2007.48] to a point where they can affect the bottom line, that it's really changing how organizations are
[2007.48 → 2012.94] seeing this. It's for a long time, your analytics teams and data science teams were kind of a very
[2012.94 → 2018.88] back office function. And now we're seeing it move into the C-suite. A lot of organizations are creating
[2018.88 → 2024.38] positions for chief data officers and chief artificial intelligence officers and such. And so,
[2024.72 → 2030.24] and they have a seat at, you know, the big kids table where they can really inform the rest of the
[2030.24 → 2034.24] leadership team how, how that's doing. And that cultural shift is making its way all the way through the
[2034.24 → 2039.24] organization. And especially in the technology sector, in the various technology sectors, but even
[2039.24 → 2045.52] moving into some that are not traditional technology sectors, you're seeing data oriented strategy and AI
[2045.52 → 2051.24] oriented strategy being prerequisite. You can't do strategy without considering that going forward.
[2051.38 → 2056.06] And when you're looking at the competitive landscape in an organization, you have to assess not only what
[2056.06 → 2060.70] your capability, but what are your competitors going to do on behalf of your customers, their customers.
[2060.70 → 2066.74] And so it's really changing a cultural mindset we're seeing in organizations and, and also allowing
[2066.74 → 2071.38] more specialization. You don't just have an analytics team, but you might actually drive to where you
[2071.38 → 2075.78] separate your AI team from your traditional data science team, from your analytics team, which might
[2075.78 → 2080.40] be doing more reporting or even something as specialized as prognostics. I work at Lockheed Martin and
[2080.40 → 2085.40] prognostics is a big thing, um, since we're dealing with aircraft and other, uh, other vehicles.
[2085.40 → 2089.76] I've seen huge shifts in a very, very short amount of time. And I think that's going to trickle down
[2089.76 → 2093.76] into small organizations. I don't think you have to be a Lockheed Martin to be thinking that way
[2093.76 → 2101.26] anymore. I think for me, maybe 2019 will be the year of stop you from stopping to use, uh, various
[2101.26 → 2106.02] terms, like loaded terms, like machine learning and AI and analytics and data science. Maybe I shouldn't
[2106.02 → 2111.78] say that since I co-host the practical AI podcast, but all of these terms are kind of, maybe they'll
[2111.78 → 2118.96] become clear this year, but I think the there's so much terminology out there. Maybe, you know,
[2118.96 → 2122.20] maybe we should rebrand as practical data stuff. I don't know.
[2123.86 → 2125.22] Doesn't sound as sexy though.
[2125.38 → 2126.56] No, I guess not.
[2126.90 → 2131.68] I have seen people actually looking at the responsibilities in these different areas
[2131.68 → 2135.30] and what they're trying to accomplish on behalf of a customer and segment, the different ways
[2135.30 → 2139.72] of segmenting it, but, and you could apply different labels if you wanted, but I've seen
[2139.72 → 2144.88] different functions, responsibilities start getting segmented out. And then people put the left best
[2144.88 → 2148.88] label on it that they can for that. And I think, I doubt we're going to get out of that in 2019.
[2148.96 → 2150.58] I think we, we have a ways to go.
[2151.04 → 2156.20] Yeah. Yeah. And I mean, we've already kind of talked about one other trend that, that probably
[2156.20 → 2163.48] is going to characterize 2019, but, um, maybe just kind of to emphasize a few elements of it.
[2163.58 → 2168.52] We talked about the voice interaction element of conversational bots and that sort of thing.
[2168.92 → 2176.00] I think there's going to be a lot of changing relationships between humans and, and automation
[2176.00 → 2181.96] or humans and services and different things, you know, like robots that's kind of taking some first
[2181.96 → 2188.46] steps, IOT devices that are all through our houses now and, and, uh, smart speakers and watches and
[2188.46 → 2195.12] other ways of, of interacting with things. And of course, you know, a lot of augmentation of jobs.
[2195.12 → 2199.92] So we always like to stress on this podcast that it's not really about automating jobs away, but
[2199.92 → 2205.20] augmenting people to do their jobs better. Like, you know, in healthcare with doctors trying to
[2205.20 → 2212.08] get them to be more efficient or, or have a higher accuracy of, of diagnosis or salespeople getting to,
[2212.24 → 2218.06] uh, more efficiently to, uh, high priority leads and, and things like that. So there is going to be a lot
[2218.06 → 2225.32] of infusion of this kind of updated interactions with machines and in 2019, which is something we've
[2225.32 → 2230.84] already seen in those first steps towards that, but it'll kind of continue to be a bit of transformation
[2230.84 → 2233.92] and augmentation of the way that we do day-to-day things, I think.
[2234.42 → 2238.10] Yeah. I mean, coming from this field, that's what the data is showing us. It's showing us not
[2238.10 → 2242.58] that, you know, we're just replacing people wholesale, but, but we're augmenting them with
[2242.58 → 2247.70] tools that make them much more capable than they ever were before. And, and that is a
[2247.70 → 2252.48] a theme that I'm seeing recurring over and over and over again in a lot of different settings.
[2252.48 → 2257.78] And so, yeah, we have, you know, we're already seeing IOT things. IOT is almost losing its
[2257.78 → 2262.78] meaning in my view because everything can be IOT at this point by putting a microchip and,
[2262.78 → 2268.00] and network connectivity to it and, and doing some cool stuff in the programming. But robotics are
[2268.00 → 2273.68] really finally becoming cheap. I have a six-year-old who is in first grade and for Christmas,
[2273.68 → 2279.46] she's going to get her fourth robot. And what, this weekend we were, I was showing her how to use,
[2279.46 → 2285.06] uh, scratch the programming language from MIT to control a little tells drone. It's actually my
[2285.06 → 2289.62] drone, but we were sitting there, and she was pulling things onto it. And so it's, it's really,
[2289.70 → 2292.80] I know as a parent, it's changing the way that I'm thinking about raising my daughter.
[2292.96 → 2297.18] And ironically, it's tied very much into what I'm doing for a living here. Uh, so I'm, I'm actually
[2297.18 → 2302.80] thinking about what do I teach my daughter so that she will be the best of whatever it is that she
[2302.80 → 2307.76] wants to be going forward. And, and it's certainly changing. I have two grown kids and the way I'm
[2307.76 → 2313.72] raising my first-grader is very different from the things I was teaching my now grown kids because
[2313.72 → 2318.56] the world has changed out from under us. So we're really incorporating ourselves with these
[2318.56 → 2323.72] technologies on a day-to-day basis. Um, so far we've seen, I would argue, we've seen very much
[2323.72 → 2328.42] a net good. I know people worry about that, uh, but I'm, I'm seeing some pretty amazing things happen.
[2328.42 → 2334.52] So I'm pretty encouraged, actually. Yeah. And I think that's a good place to kind of wrap up our
[2334.52 → 2341.14] perspective on, on 2019. I'm super excited to talk about all of these things in 2019 on practical AI.
[2341.36 → 2347.00] I don't know about you, Chris, that's going to be a really great year ahead talking about all of these
[2347.00 → 2352.96] things that, that really are impacting the industry and new things and AI exciting things,
[2352.96 → 2358.10] things that are really making an impact on our day-to-day lives. I'm glad that our jobs of,
[2358.10 → 2364.08] of hosting this podcast won't be automated away at least this year. And I'm really excited to talk
[2364.08 → 2370.26] about all of these things as you look forward to 2019. Please let us know if there are any topics you
[2370.26 → 2376.00] want to hear about on practical AI, definitely let us know in Slack, um, join our community on,
[2376.04 → 2381.42] on LinkedIn, and we'll be really excited to hear from you and, and interact with you this coming year.
[2381.42 → 2384.74] So congrats again on, uh, on 2018, Chris.
[2384.74 → 2388.22] Congrats again. We made it through this year. I know when we started it,
[2388.46 → 2394.12] we were both new at this and, uh, we've come a long way ourselves. So, um, I am really stoked.
[2394.48 → 2400.22] And a big thank you to Changelog for helping us get started with this podcast and doing a lot of
[2400.22 → 2405.82] the really hard work around editing and, and, uh, production and marketing and all of that. So
[2405.82 → 2411.00] a big thank you to them for getting us up and running in 2018. Definitely check out their other
[2411.00 → 2415.92] shows as well. It's totally a team effort. I'm really glad you said that everyone just hears
[2415.92 → 2420.58] you and me talking, uh, from week to week, but there's a whole team behind us that makes this
[2420.58 → 2424.90] whole thing work. And I'm immensely thankful. I never realized what a team effort it was until
[2424.90 → 2430.24] I got into this. Awesome. Thanks for the review, Chris. And I will talk to you in the new year.
[2430.50 → 2432.84] Talk to you in the new year, Daniel. Take care. Happy new year.
[2433.10 → 2433.60] Happy new year.
[2433.60 → 2440.48] All right. Thank you for tuning into this episode of practical AI. If you enjoyed this show,
[2440.56 → 2445.32] do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it. If you are
[2445.32 → 2449.04] on Twitter or social network, share a link with a friend, whatever you got to do, share the show
[2449.04 → 2453.58] with a friend. If you enjoyed it and bandwidth for Changelog is provided by Vastly. Learn more
[2453.58 → 2458.00] at fastly.com, and we catch our errors before our users do here at Changelog because of Rollbar.
[2458.18 → 2463.40] Check them out at rollbar.com slash Changelog. And we're hosted on Linde cloud servers.
[2463.40 → 2466.84] Head to Leno.com slash Changelog. Check them out. Support this show.
[2467.24 → 2472.36] This episode is hosted by Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith.
[2472.60 → 2478.48] The music is by Break master Cylinder. And you can find more shows just like this at ChangeLog.com.
[2478.66 → 2483.04] When you go there, pop in your email address, get our weekly email, keeping you up to date with the
[2483.04 → 2489.02] news and podcasts for developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2493.40 → 2496.82] I'm Nick Needed. This is K-Ball.
[2496.96 → 2498.20] And I'm Rachel White.
[2498.36 → 2502.40] We're panellists on JS Party, a community celebration of JavaScript and the web.
[2502.66 → 2506.10] Every Thursday at noon central, a few of us get together and chat about JavaScript,
[2506.48 → 2510.24] Node, and topics ranging from practical accessibility to weird web APIs.
[2510.76 → 2516.36] You could just evil the text that you're given and then, and that's basically what it's doing.
[2516.54 → 2517.74] What could go wrong?
[2517.74 → 2522.80] Yeah, exactly. This is not legal advice to evil text as it comes in.
[2523.18 → 2527.50] Join us live on Thursdays at noon central. Listen and slack with us in real time or wait
[2527.50 → 2530.02] for the recording to hit. New episodes come out each Friday.
[2530.32 → 2535.92] Find the show at changelog.com slash JS Party or wherever you listen to podcasts.
