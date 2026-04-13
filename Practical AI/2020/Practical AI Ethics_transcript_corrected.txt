[0.00 → 1.46] It's quite a long process, actually.
[1.66 → 5.50] I would say it starts with principles, and that's what most people think of now.
[5.70 → 10.52] But once you've done your principles, you've basically just gotten to the starting line.
[13.50 → 16.26] Bandwidth for Changelog is provided by Vastly.
[16.26 → 18.54] Learn more at Fastly.com.
[18.76 → 21.84] We move fast and fix things here at Changelog because of Rollbar.
[21.96 → 23.66] Check them out at Rollbar.com.
[23.90 → 26.08] And we're hosted on Linde cloud servers.
[26.42 → 28.42] Head to Linode.com slash Changelog.
[30.00 → 33.22] Linde is our cloud server of choice.
[33.76 → 36.68] Grab the NATO plan for just $5 a month, just $5.
[37.10 → 42.24] That gets you a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer.
[42.56 → 45.00] Let's be honest, you can go a long ways on that $5.
[45.56 → 49.88] When you do need to scale up, their prices are predictable, so you can put your calculator down.
[50.00 → 50.54] You won't need it.
[50.84 → 56.02] We've been running Changelog.com on Linde for years, and we've always impressed by their award-winning support team.
[56.54 → 59.26] Check them out at Linode.com slash Changelog.
[59.26 → 62.64] Once again, that's Linode.com slash Changelog.
[62.64 → 79.20] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[79.50 → 83.60] This is where conversations around AI, machine learning, and data science happen.
[83.96 → 88.62] Join the community and Slack with us around various topics of the show at Changelog.com slash community,
[88.62 → 89.96] and follow us on Twitter.
[90.12 → 91.76] We're at Practical AI FM.
[97.80 → 104.24] Welcome to another Fully Connected episode where Daniel and I keep you fully connected with everything that's happening in the AI community.
[104.50 → 107.14] We're going to take some time to discuss the latest AI news,
[107.24 → 110.78] and we're going to dig into learning resources to help you level up on your machine learning game.
[110.78 → 112.10] My name's Chris Benson.
[112.24 → 114.24] I am a Principal AI Strategist at Lockheed Martin,
[114.50 → 119.22] and with me as always is Daniel Whiten ack, Data Scientist with SIL International.
[119.64 → 120.66] How's it going today, Daniel?
[121.20 → 122.60] It's going pretty good.
[122.72 → 124.28] It's been an interesting week.
[124.80 → 127.16] Went to visit a couple family members,
[128.16 → 132.86] and of course travelling during COVID time is somewhat interesting.
[133.26 → 136.44] So navigating those waters and trying to stay safe.
[136.68 → 138.78] So it's been an interesting week.
[139.04 → 139.58] What about you?
[139.58 → 140.88] Same here.
[140.98 → 143.24] I've been trying to kind of reassess everything.
[143.58 → 146.00] I'm in Georgia, as long-time listeners will know,
[146.48 → 151.86] and definitely our numbers are in terms of transmission are going through the roof on COVID.
[152.16 → 155.16] Yeah, it's kind of all across the South at this point, I think.
[155.58 → 156.70] It really is.
[156.74 → 159.74] Big questions about like how we're doing schooling going forward
[159.74 → 164.52] and different local governments and such trying to figure out what they're going to do.
[164.74 → 166.84] And so it's interesting times.
[166.84 → 169.42] This whole year has been just quite a crazy year,
[169.42 → 170.48] in a lot of different ways.
[170.48 → 176.32] Yeah, and of course, it's still a lot of things going on in our country related to politics
[176.32 → 181.40] and also, you know, justice for marginalized groups and...
[181.40 → 181.52] Absolutely.
[181.78 → 185.12] ...various injustices that are trying to be righted.
[185.12 → 192.40] I mean, there's sort of a mix of encouraging things, really sad things, confusing things,
[192.40 → 194.90] and stressful things all at once.
[195.08 → 195.30] Yeah.
[195.72 → 201.70] Which I guess does interface with what we had thought about talking today.
[201.92 → 206.14] I don't know if you want to get into that a little bit about what your thoughts were
[206.14 → 209.70] in terms of what to dive into related to AI today.
[209.70 → 210.40] I will.
[210.76 → 210.98] Yeah.
[211.28 → 212.10] Yeah, I will.
[212.22 → 217.66] And I know I've alluded to it kind of, you know, in passing on a number of episodes,
[217.66 → 224.10] but one of the things I do in my own job is I lead AI ethics for the company that I work
[224.10 → 225.26] at, which is Lockheed Martin.
[225.74 → 228.92] And this show is not about specifically Lockheed Martin.
[229.04 → 233.82] I may mention it a little bit in terms of things that have been approved for public release
[233.82 → 236.84] by our communications department, but that's going to be very little.
[236.84 → 242.54] I really wanted to talk about the fact that I spend a lot of time focusing on the details
[242.54 → 247.64] of implementing AI ethics, both internally and externally in our own operations.
[248.06 → 253.70] And it is a topic that I get asked about more and more often these days in terms of people
[253.70 → 257.38] looking for guidance on how to do that in their own organizations.
[257.90 → 263.62] And in my own organization, we are fairly far along that process relative to most other
[263.62 → 265.66] organizations out there, I think.
[265.66 → 267.70] And the feedback that I've gotten is such.
[267.78 → 273.30] And so I wanted to really kind of start with what most people that have delved into this
[273.30 → 277.60] topic are probably most familiar with, which is kind of principles that are being adopted
[277.60 → 278.84] by various organizations.
[279.44 → 284.40] Kind of explore what some of those look like, but then talk beyond just principles of AI
[284.40 → 291.60] ethics and talk about how that affects your organization and your operations when you are
[291.60 → 296.86] trying to take the principles that you have chosen and move them through your organization
[296.86 → 299.76] from end to end so that they become part of what you are.
[300.08 → 301.96] So I thought that'd be a fun thing to talk about.
[302.04 → 302.56] You up for it?
[303.22 → 304.44] Yeah, I'm definitely up for it.
[304.62 → 309.30] It's probably not hard to convince people to think about AI ethics in terms of some of the
[309.30 → 314.58] things that we've seen in our world of recent times, especially usage of things like facial
[314.58 → 319.52] recognition and other things and, you know, by governments and other institutions that
[319.52 → 323.08] are trying to discriminate against certain groups or something like that.
[323.14 → 327.62] So that's sort of a very AI ethics comes up very easily in that conversation.
[327.62 → 332.38] I think that there may be, though, some people out there that are practitioners and maybe
[332.38 → 340.20] let's say they're using AI to optimize their infrastructure, or they're using AI to plan their
[340.20 → 342.44] marketing campaign or something like that.
[342.56 → 350.10] It might be a little bit less clear why AI ethics and AI ethics statement about your principles
[350.10 → 355.40] around AI ethics and how you approach AI is relevant to those scenarios.
[355.40 → 358.46] I don't know if you have any thoughts on that before we just jump in.
[358.72 → 366.60] Like, if you're doing AI, why it may be important that you start to consider some of the ethics
[366.60 → 372.90] behind how you approach your AI development, regardless of, you know, the specific use case?
[373.08 → 376.84] Are there some motivations that everyone should be thinking about?
[377.54 → 378.34] Yeah, I think so.
[378.44 → 384.66] What we are calling AI today, which is in a practical sense, it is probably the at least the
[384.66 → 389.32] area you have a lot of dispute, obviously, on what AI is out there.
[389.56 → 394.80] And every organization and really every person that's in this field kind of has their own
[394.80 → 395.18] definition.
[395.36 → 397.00] So that muddies the water a little bit.
[397.44 → 405.10] I think if there is probably one area that most people would agree is AI, you know, as we
[405.10 → 410.74] record this in 2020, it'd probably be the field of deep learning and kind of the other adjacent
[410.74 → 413.70] fields that are inclusive or tied to that.
[414.20 → 420.50] And so I think one of the notable aspects of that is that they are non-deterministic systems.
[420.50 → 427.08] And that means that you're not guaranteed that a given input is always going to yield exactly
[427.08 → 427.92] the same output.
[427.92 → 429.60] You can have variability in there.
[429.64 → 434.64] And as a matter of fact, you know, obviously, when we train a neural network, we introduce
[434.64 → 438.44] randomness on purpose, you know, for purpose of getting to a better model.
[438.44 → 443.56] It doesn't run into some of the technical issues with training, which is kind of outside the
[443.56 → 444.48] scope of this conversation.
[445.00 → 454.60] So I think given that you have these capabilities, but it's in the early days, and we've already
[454.60 → 459.82] talked in previous episodes about how AI will evolve probably fairly dramatic in the years
[459.82 → 460.36] to come.
[460.52 → 466.54] But as we're looking at it right now, today's AI, as is mostly deployed, it's not aware of
[466.54 → 467.26] right and wrong.
[467.26 → 474.92] It's not aware of values that you'd want to have governed your actions and your thinking.
[475.10 → 481.92] You don't have a framework that ties ethical considerations, moral considerations, value
[481.92 → 485.08] considerations into the output of an inference.
[485.70 → 493.12] And so you could think of AI ethics as a new field, which probably will stop in the future,
[493.12 → 498.94] stop being kind of this thing unto itself and become part of artificial intelligence development.
[499.04 → 504.14] Just like in other fields, they have ethical considerations that are part of the core field
[504.14 → 504.54] itself.
[504.68 → 507.44] But right now we're kind of building that from scratch.
[507.78 → 510.58] And so we're kind of talking about it as a thing unto itself.
[510.58 → 516.40] But that's really why we're having to do that is to ensure that we get the outcomes that we are
[516.40 → 522.14] shooting for, that we are anticipating versus the unexpected outcomes that can cause real problems.
[522.14 → 525.78] And we've certainly seen quite a few of those over the last few years.
[525.78 → 533.92] Yeah, I think that there's definitely things that are unexpected in terms of how AI behaves,
[534.06 → 541.50] that a problem set might not in and of itself appear like there are ethical issues with a certain
[541.50 → 543.22] problem you're trying to solve with AI.
[543.22 → 548.10] But they can crop up in sort of unexpected way.
[548.92 → 553.74] And, you know, I'm thinking of like, I gave the example of optimizing infrastructure, right?
[553.92 → 560.46] And while you may not be like discriminating based on race or gender or something when you're
[560.46 → 566.56] optimizing infrastructure, there are certain things about the way that we handle infrastructure
[566.56 → 574.32] as a company that are maybe like energy related and that sort of thing that might have some
[574.32 → 576.20] implications on the world at large.
[576.20 → 583.74] Whereas, you know, there are other scenarios, especially if you're doing like advertising
[583.74 → 587.76] campaigns online for hiring at your company or something like that.
[587.90 → 595.34] That, of course, is something that is very fraught with ethical and fairness issues in terms of
[595.34 → 599.42] how you're presenting job postings to people and all of those things.
[599.60 → 604.82] So I think there are certain problems, I guess, that the ethical issues are more obvious and
[604.82 → 607.22] certain problems where they're less obvious.
[607.94 → 614.32] But I guess the having principles set down for how you approach AI problems at your company
[614.32 → 618.48] is the purpose of like having that set of principles from your perspective.
[618.48 → 624.48] Is it to help tease out what ethical issues might be at play in a certain problem set?
[624.48 → 633.64] Or is it what's the real purpose behind having a set of principles that you adhere to as a
[633.64 → 635.12] group of AI developers?
[635.62 → 639.60] What's the main sort of advantage of that and how that might play out?
[640.28 → 644.98] Yeah, I think, you know, principles have been where the majority of the conversation has been
[644.98 → 645.68] so far.
[645.84 → 649.36] You know, there have been a lot of, you know, press releases between with major organizations
[649.36 → 651.42] adopting and publishing their principles.
[651.42 → 662.24] Those really are intended to explicitly establish what your values as an organization are and
[662.24 → 668.80] the kinds of things that your organization is thinking about and cares about to ensure that
[668.80 → 674.38] if you're operating the way you think you should be, then you should be in full compliance with
[674.38 → 675.58] what those principles are.
[675.58 → 683.44] And if you operate in such a way, either on a regular basis or by exception, where you feel those
[683.44 → 688.28] principle, one or more of those principles that you've adopted are violated, then it's a sign that
[688.28 → 691.84] you're moving outside that zone of normalcy for you.
[692.36 → 699.30] And so really the principles are trying to capture that organizational ethic, but it's not enough.
[699.36 → 704.00] You're going to have to take those principles and push them down through your operations in a
[704.00 → 706.64] meaningful way so that you can execute.
[706.74 → 711.42] Otherwise, you end up having, you know, a set of principles that sound very wonderful, but don't
[711.42 → 714.90] have a meaningful connection with what you're doing day to day.
[715.14 → 719.46] And so it's very important that you start with that, but then you find your way down below that.
[719.64 → 723.28] But nonetheless, we should start with principles today because there's been a lot of thinking
[723.28 → 724.60] in that area, certainly.
[724.60 → 725.14] Sure.
[725.34 → 733.42] So if you're an organization that's using AI, what's a good way to start developing a set
[733.42 → 741.02] of principles or guidelines that kind of guide your AI development team or your AI development
[741.02 → 743.26] department or whatever it is?
[743.34 → 747.22] What's maybe a good way to put a flag on the ground and get started?
[747.22 → 754.16] Well, I think what a lot of organizations have done is to collect a representative group of
[754.16 → 759.94] people from their organization that represent all the different functions that that organization
[759.94 → 761.92] tries to address in its operations.
[762.36 → 765.54] And so, you know, there could be product teams and service teams.
[765.68 → 770.16] It could be representation from your legal team or your HR team.
[770.30 → 772.72] All of these have a unique voice.
[772.72 → 778.54] And so you will bring these people together typically, and you will have a set of conversations
[778.54 → 780.96] on looking at operations.
[780.96 → 784.50] You'll tend to look at use cases and say, what does this mean for us?
[784.76 → 785.88] How do we use technology?
[786.02 → 787.26] How do we think we're using AI?
[787.50 → 791.70] What do we expect to be doing in the future with AI as far as what we understand it to be
[791.70 → 792.10] today?
[792.24 → 797.12] And you'll collect a set of cases to go through and to dive into that.
[797.12 → 802.80] And from that process and bringing all those different perspectives and diversity is so
[802.80 → 809.66] important in this process that you start kind of working together to agree on a set of things
[809.66 → 810.34] to address.
[810.50 → 812.36] Use cases is a good word for it.
[812.58 → 814.44] You know, scenarios, if you will.
[814.62 → 816.90] It can be at a functional level.
[816.96 → 820.44] It might be an internal thing, like how does AI apply to an HR system?
[820.60 → 824.92] Or it might be how does it apply to the services and the products that we offer our customers?
[825.02 → 826.40] And how does it affect our customers?
[826.40 → 830.28] So in doing that, you really say, this is what we do.
[830.36 → 835.84] And you start identifying what would you feel right about doing with your customers and with
[835.84 → 837.38] your employees and such.
[837.48 → 845.84] And you're really focusing on a set of values that will describe what a good process, a good
[845.84 → 847.34] operation looks like there.
[847.42 → 850.18] The one that you want, the outcome that you would like to achieve.
[850.38 → 855.68] And you have to narrow those down to a set of specific words that are to the principles
[855.68 → 860.96] with some kind of definition around those that describe what it means to you and your organization.
[860.96 → 865.82] Some version of that is what most organizations that we've seen have addressed.
[865.82 → 873.40] Yeah, I think maybe I naturally struggle with this process a little bit because it seems a little
[873.40 → 879.30] bit to me like, you know, when people develop like vision or mission statements for their
[879.30 → 883.28] organization, it seems to me like a similar sort of process.
[883.28 → 889.64] And I have trouble with that, maybe not surprisingly, because we named this podcast Practical AI.
[890.02 → 892.80] And I try to be a very practical person.
[893.02 → 899.64] And so a lot of times those seem so far from practicalities that I struggle understanding how
[899.64 → 902.16] they play out in everyday scenarios.
[902.30 → 903.36] I don't know if that makes sense.
[903.36 → 904.66] No, it does.
[904.86 → 907.04] And I think that a lot of people feel that way.
[907.34 → 913.68] And in particular, given the fact that AI practitioners tend to be very down to earth
[913.68 → 919.04] people, they're engineers, they're data scientists, they're people who work with the tangible side
[919.04 → 921.20] of technology to achieve something.
[921.40 → 923.72] AI principles can feel very wishy-washy.
[923.92 → 925.16] And so that's one of the challenges.
[925.40 → 930.30] But ultimately, to get those people satisfied, you're going to have to start with those principles.
[930.30 → 934.28] You're going to have to figure out what does that mean for your own policies, the policies
[934.28 → 939.02] that govern how you operate, how you're going to govern that once you reach that point.
[939.52 → 944.16] How do you know that you're in compliance with what you've decided that you want to do and
[944.16 → 944.52] govern?
[944.90 → 950.92] And then what kind of tooling and workflow integration are you going to implement to ensure that all
[950.92 → 956.02] of that happens and that it can be done by people who are not necessarily experts at
[956.02 → 956.62] ethical AI?
[956.62 → 963.38] So Chris, you were getting into some details about how companies can start getting their
[963.38 → 971.18] AI principles together and also how to connect that in a practical sense to day-to-day workflows.
[971.52 → 974.36] I was wondering if we could maybe take an example.
[974.84 → 980.96] So let's say that fairness in terms of, you know, we're a marketing company or something
[980.96 → 987.14] like that or hiring company and fairness in terms of gender and race is something that
[987.14 → 988.32] is important to us.
[988.38 → 990.14] And we have some principle around that.
[990.50 → 996.42] Where might you go from there in terms of making sure that an ethical principle actually
[996.42 → 1001.64] filters down to the people that are doing the development and building products?
[1001.90 → 1005.82] It seems like maybe that's a place where a lot of people get hung up.
[1005.82 → 1012.06] So like if you're talking about like fairness being one and by way of example, Google has
[1012.06 → 1017.56] five principles and one of those principles is fairness that they've chosen as one of the
[1017.56 → 1019.82] descriptive words for how they're operating.
[1020.02 → 1024.54] And so you really, in the beginning, it's deceptively simple.
[1024.62 → 1025.40] You think that's fairness.
[1025.56 → 1026.64] You know, I know what fairness is.
[1026.76 → 1029.96] Well, not everyone does and not everyone actually will agree on that.
[1030.00 → 1031.84] And that's pretty true all the way across.
[1031.94 → 1033.62] There are a lot of ways to define it.
[1033.62 → 1039.72] So one of the first ways that you might do that is if your organization, and this tends
[1039.72 → 1045.38] to happen probably with larger organizations more often, they may have a formal description
[1045.38 → 1046.48] about what fairness is.
[1046.76 → 1051.20] If it's a large company in particular, they may have an ethics department at the company,
[1051.30 → 1055.66] or if not, maybe a smaller company, the HR department will take this kind of thing on.
[1056.20 → 1063.48] And being able to tie the principles that you're adopting for AI back to what you already believe.
[1063.62 → 1067.28] And particularly what you've already documented is really important.
[1067.48 → 1072.24] Because otherwise, you end up having these AI principles that are kind of this beast unto
[1072.24 → 1074.26] themselves that are separate from everything else.
[1074.38 → 1079.56] But it's pretty crucial that you end up with principles that apply directly to your organization
[1079.56 → 1082.78] in a very organic way and fit in with what you already have.
[1082.88 → 1084.52] Yeah, I agree with that.
[1084.52 → 1089.64] I think maybe this is a tension that I often feel when I get into this vision and mission
[1089.64 → 1091.50] statement conversations.
[1091.50 → 1098.06] And maybe these conversations are similar around AI ethics and principles is that there's also
[1098.06 → 1105.34] a tension between who you are now and who you want to be as a company and kind of casting
[1105.34 → 1106.30] that vision out.
[1106.30 → 1111.44] All the things you're doing now, maybe they aren't consistent with the company that
[1111.44 → 1112.18] you envision.
[1112.60 → 1119.72] You're wanting to put these in place partly to push people to do, quote unquote, good development
[1119.72 → 1120.16] work.
[1120.46 → 1127.56] But then also they have to be integrated into the sort of natural sort of philosophy and
[1127.56 → 1129.92] values that already exist within your organization.
[1130.08 → 1133.74] Otherwise, it's going to be hard for a company to implement them, I think.
[1133.74 → 1136.16] So I think that there is that tension.
[1136.76 → 1144.28] You can't sort of from a top-down view just impose a new set of AI principles that just
[1144.28 → 1148.12] kind of shock and are totally coming out of left field to everyone in the company.
[1148.46 → 1153.52] But at the same time, you want to put some things in place to maybe push people to do certain
[1153.52 → 1155.32] things differently.
[1155.62 → 1158.90] I don't know if you've seen that sort of tension play out.
[1159.36 → 1160.24] Yeah, I have.
[1160.24 → 1165.24] I mean, it's kind of that aspirational tension of where you're at today versus what you have
[1165.24 → 1166.50] been thinking you want to go to.
[1166.98 → 1172.60] And when you're first designing your AI principles, and I say design on purpose because you are
[1172.60 → 1173.84] designing your way into it.
[1173.86 → 1174.64] You don't just pick them.
[1174.96 → 1180.10] It really has to feel authentic, not only to your own teams, but also it needs to feel
[1180.10 → 1183.32] authentic to the people that your organization will interact with.
[1183.80 → 1188.62] So without that sense of authenticity, like the principles are in alignment with existing
[1188.62 → 1189.22] policies.
[1189.34 → 1193.36] You know, we talked about fairness as that example that Google has, and it's notable
[1193.36 → 1195.30] that that is one that you would typically find.
[1195.42 → 1199.00] Fairness was also selected, for instance, by Microsoft as one of theirs.
[1199.38 → 1206.26] And as you're doing that, you need to ensure that whatever HR policies, for instance, that
[1206.26 → 1211.44] you have around fairness of what your employees might do internally, that that is reflected
[1211.44 → 1217.24] because, you know, with AI being an enabling mechanism, an enabling tool that you're typically
[1217.24 → 1222.58] going to apply to existing things that you're trying to do to enhance them, the output from
[1222.58 → 1226.44] your AI needs to comply with what your idea of fairness is.
[1226.58 → 1229.48] And fairness is mostly the same.
[1229.76 → 1234.52] You know, there's a general idea, but it might mean a little bit of something different to
[1234.52 → 1237.80] Google from Microsoft, at least in terms of their official policies.
[1237.80 → 1240.88] So it feels very fluffy, I know, at this level.
[1241.48 → 1245.24] But if you don't go through this, then when you get to the more pushing it down through
[1245.24 → 1247.20] the practical levels, you're going to struggle.
[1247.44 → 1252.46] This really has to represent your organization's values within a diverse context.
[1252.46 → 1259.38] It needs to be as real to your HR person as it is to your salesperson, as it is to your
[1259.38 → 1259.86] engineer.
[1260.20 → 1265.14] So all of those people need to be able to touch these principles and say, I know what that
[1265.14 → 1267.22] means to me in the context of my organization.
[1267.80 → 1274.40] So in starting out with getting a set of AI principles in place for your organization,
[1274.40 → 1282.74] since I'm mainly involved in practical development work, I tend to take the viewpoint that I think
[1282.74 → 1285.24] it was Kelsey Hightower in a talk that I saw.
[1285.38 → 1290.28] I always remember him saying that good developers copy and great developers paste.
[1291.10 → 1296.52] So looking at some examples that people have already put a lot of work into out there, I think
[1296.52 → 1297.22] is a good thing.
[1297.32 → 1301.36] I actually, while we were talking, I was looking up some papers on the subject.
[1301.50 → 1307.68] There's a paper from a group at the Chinese Academy of Sciences, and they took sets of AI
[1307.68 → 1313.62] principles from academic organizations and governments and industry organizations, including
[1313.62 → 1316.28] Google and Microsoft and IBM and others.
[1316.28 → 1318.88] And they did a bit of analysis on them.
[1318.88 → 1322.04] So they did some word to DEC analysis on them.
[1322.12 → 1329.52] It looks like kind of categorized the statements into a set of topics that occurs very frequently
[1329.52 → 1333.28] in these subjects or in these statements of principles.
[1333.64 → 1337.92] So that's actually very helpful to me because I think, you know, looking at what people are
[1337.92 → 1341.64] valuing in their principles might be a good point to kind of get you thinking.
[1341.64 → 1348.16] So these topics include humanity, and that has to do with keywords around being beneficial
[1348.16 → 1351.68] for humanity and human centred and human friendly.
[1352.04 → 1356.76] A second topic is collaboration, having to do with things like partnership and cooperation
[1356.76 → 1357.62] and dialogue.
[1358.14 → 1365.18] There is a share topic, which has to do with share and equality, inequity, inequality sort of
[1365.18 → 1365.96] topics.
[1365.96 → 1372.00] There's a fairness topic, which has to do with bias, discrimination and prejudice, transparency
[1372.00 → 1380.16] topic, having to do with things like explainability and audit and tracing, a privacy topic, a security
[1380.16 → 1386.52] topic, a safety topic having to do with, you know, controlling risk and human control, accountability
[1386.52 → 1395.06] topic, and then a topic around artificial general intelligence or superintelligence and that
[1395.06 → 1395.62] sort of thing.
[1395.92 → 1401.08] So I don't know, is that consistent with what you've seen in various statements of AI principles?
[1401.78 → 1402.30] I think so.
[1402.38 → 1406.88] I mean, we see so much commonality across different groups, different organizations, principles
[1406.88 → 1413.56] that I think it is fair to stand on the shoulders of giants, if you will, and benefit from their
[1413.56 → 1414.28] own work.
[1414.68 → 1419.10] I think there has to be a point where if you just adopt and move it in, it doesn't have a
[1419.10 → 1420.46] lot of meaning for your organization.
[1420.46 → 1425.84] So there's a point when you're applying it to your own internal policies, your own way
[1425.84 → 1426.70] of doing things.
[1427.14 → 1431.66] You have to customize it there to your own organization so that it is meaningful because
[1431.66 → 1434.36] otherwise it's just a set of words written down.
[1434.74 → 1439.04] And, you know, once you've implemented these, you should be able to have a common meaning through
[1439.04 → 1440.88] your organization that understands it.
[1440.88 → 1445.80] And from even the same word, like we mentioned fairness from one organization to another,
[1446.30 → 1451.54] it may mean slightly different things to them based on what their worldview is as an organization
[1451.54 → 1456.24] and the employees that are working there trying to affect that, what their operations are.
[1456.48 → 1460.34] So you can start by borrowing from others and stealing from others, if you will.
[1460.50 → 1461.82] I think that's perfectly reasonable.
[1462.24 → 1464.32] But at some point, you do have to make them your own.
[1464.96 → 1468.70] A good starting point would be to take some of those bigger topics.
[1468.70 → 1473.96] Like I'd say privacy and security kind of cross a lot of these statements, I think.
[1474.26 → 1479.52] But I guess what you're saying is that in privacy, like, you know, in my organization,
[1479.98 → 1485.02] SIL International, we'd have to decide what does, how does privacy impact the things that
[1485.02 → 1485.88] we do with AI?
[1486.20 → 1495.02] And how could the things that we're developing that are AI driven influence, you know, privacy
[1495.02 → 1501.26] and positive or negative ways for our specific users or customers or that sort of thing?
[1501.32 → 1502.16] Is that kind of what you're saying?
[1502.58 → 1503.48] I think so.
[1503.64 → 1504.22] It's interesting.
[1504.36 → 1508.60] One of the things that I found is that choice of words matters.
[1509.16 → 1515.38] If you look across a number of different principles as outlined by different organizations,
[1515.76 → 1517.64] they'll have different numbers of principles.
[1517.90 → 1520.34] They'll have different words that they use to describe.
[1520.34 → 1525.34] And it may be that one organization uses the word privacy and another organization does
[1525.34 → 1525.82] not.
[1526.22 → 1530.54] That doesn't mean that privacy is absent from their principles, but it may mean that they've
[1530.54 → 1536.22] taken the principles that they believe to be privacy and divided them into maybe two other
[1536.22 → 1539.58] of their principles because they see that as two subsets.
[1539.68 → 1546.22] It's really dependent upon how you see the world and how you believe you're interacting with it
[1546.22 → 1551.72] and the language that you use to do that beyond just AI ethics, the language of your own operations.
[1553.06 → 1553.16] Yeah.
[1553.30 → 1558.96] And I guess depending on the industry that you work in, some of these might be more important
[1558.96 → 1559.46] than others.
[1559.46 → 1565.42] Like if you're an actual company that works in the HR hiring space, then some of these are going to
[1565.42 → 1566.80] become extremely important.
[1566.96 → 1572.20] Whereas if you're a software as a service company or developer tools company or something like that,
[1572.20 → 1576.44] then other of these might be kind of immediately important.
[1576.74 → 1581.92] I mean, a lot of these intersect with people no matter what company they're working in.
[1581.92 → 1588.48] A lot of these, when I read them, I think could be interpreted, like depending on who's reading
[1588.48 → 1591.54] them, they could be interpreted in different ways.
[1592.08 → 1598.00] How do you make sure that, you know, what you're going after with your AI principles actually trickles
[1598.00 → 1602.44] down to the work that's going on in your AI development teams?
[1602.72 → 1607.94] Is there tooling around that or is it mostly an education sort of thing, or what's your thought
[1607.94 → 1608.16] there?
[1608.16 → 1609.62] It's going to be both.
[1609.96 → 1615.44] But what you have to start doing is you have to connect on the assumption that your operations,
[1615.68 → 1620.84] whether internal or external, are governed by some essentially policies internally.
[1620.84 → 1627.28] You really have to connect the principles to the policies that you have because those policies
[1627.28 → 1632.64] are representing the reality or at least an ideal reality that your organization is trying
[1632.64 → 1633.16] to achieve.
[1633.70 → 1640.30] And so until you can map principles to the policies that you already have in place and figure out
[1640.30 → 1646.06] if you have gaps and need to create new policies or change existing policies, that's the first
[1646.06 → 1652.86] step is saying, I understand how the principles that we've said identify our values map out
[1652.86 → 1656.54] to the policies that govern our operations and our functions.
[1656.54 → 1659.46] And so that's really the first step.
[1659.62 → 1665.26] And then you'll follow that up with how do we know that we are in compliance then?
[1665.44 → 1667.72] What's the mechanism, and how do we govern that?
[1667.80 → 1673.80] If something goes awry with the way that we're thinking about this, how does our organization
[1673.80 → 1676.24] handle that and process that?
[1676.46 → 1680.58] So, you know, like you would have in anything having not to do with AI ethics, if you have
[1680.58 → 1686.20] something in your operations that is not compliant with your expectation, how do you handle that?
[1686.24 → 1687.78] You need that for this as well.
[1688.18 → 1691.18] And then you need to connect that to the people that are doing the actual work.
[1691.24 → 1694.74] It needs to fit into the workflow, and it needs to fit into the tooling.
[1695.06 → 1699.24] And if it doesn't, or if that's not an easy thing to do, then you need to figure out
[1699.24 → 1701.62] what that delta is and figure out, do I need new tools?
[1701.62 → 1706.26] Do I need to adjust existing tools, which has a lot of variability based on are they
[1706.26 → 1711.08] vendor tools that we're paying for, and we're limited to the features that the vendor offers
[1711.08 → 1711.42] us?
[1711.52 → 1713.48] Is it stuff that we've written for ourselves?
[1713.88 → 1715.00] How do we know that?
[1715.06 → 1720.22] And how do we get these to filter in at the workflow level in terms of being productive?
[1720.46 → 1722.36] So it's quite a long process, actually.
[1722.56 → 1726.76] I would say it starts with principles and that's what most people think of now.
[1726.76 → 1732.52] But once you've done your principles, you've basically just gotten to the starting line.
[1743.90 → 1748.08] I'm Jared Santo, Go Times producer and a loyal listener of the show.
[1748.28 → 1752.62] This is the podcast for diverse discussions from around the Go community.
[1752.62 → 1756.54] Go Times panel hosts special guests like Kelsey Hightower.
[1757.26 → 1762.14] And sometimes you can leverage a cloud provider and make margins on top.
[1762.24 → 1763.42] That's just good business.
[1763.84 → 1767.50] But when we're at the helm making the decision, we're like, yo, forget good business.
[1768.06 → 1772.30] I'm about to deploy Kafka to process 25 messages a year.
[1773.34 → 1775.06] It's nerd pride, right?
[1775.82 → 1778.30] Picks the brains of the Go team at Google.
[1778.30 → 1782.98] You don't get a good design by just grabbing features from other languages and gluing them together.
[1783.64 → 1788.46] Instead, we tried to build a coherent model for the language where all the pieces worked in concert.
[1789.12 → 1792.06] Shares their expertise from years in the industry.
[1792.62 → 1794.28] Don't expect to get it right from the start.
[1794.56 → 1795.86] You'll almost definitely get it wrong.
[1795.94 → 1797.96] You'll almost definitely have to go back and change some things.
[1798.48 → 1801.58] So yeah, I think it goes back to what Peter said at the start, which is just made your code,
[1801.72 → 1803.58] write your code in a way that is easy to change.
[1804.24 → 1805.70] And then just don't be afraid to change it.
[1805.70 → 1808.72] And has an absolute riot along the way.
[1809.34 → 1813.04] Yeah, you know that little small voice in your head that tells you not to say things?
[1813.66 → 1814.74] What is that?
[1815.56 → 1816.50] How do you get one?
[1818.04 → 1819.06] You want one of those?
[1819.08 → 1820.18] Is it like an in-app purchase?
[1821.08 → 1822.50] It is go time.
[1822.90 → 1826.66] Please select a recent episode, give it a listen, and subscribe today.
[1827.08 → 1828.30] We'd love to have you with us.
[1835.70 → 1851.78] So Chris, as a practitioner, when I hear you say the word governance and that sort of thing,
[1852.42 → 1859.08] immediately I have these feelings inside of me that are just sort of naturally negative.
[1860.38 → 1861.56] I'm not surprised.
[1861.78 → 1862.46] A lot of us do.
[1862.46 → 1867.86] Yeah, I think it's sort of natural for a developer to have that feeling because it's like, oh,
[1867.98 → 1874.40] governance or a natural first thought might be that governance in some way, whether that
[1874.40 → 1880.66] be over the certain data and access to data thing, or whether it be in ensuring compliance
[1880.66 → 1885.14] to certain things, that naturally means slow.
[1885.14 → 1890.18] I think to most developers, it's like, oh, this is going to complicate my workflow.
[1890.84 → 1892.86] It's not going to allow me to get anything done.
[1893.10 → 1895.26] And it's just going to be a slow process.
[1895.96 → 1901.86] So I do think that there is, you know, some validity to that in that, you know, in order
[1901.86 → 1907.72] to check some of the things that should be checked in terms of an AI application, you're
[1907.72 → 1910.74] going to have to spend some time on those things, though.
[1910.74 → 1916.68] So but at the same time, I forget which guest it was, I actually have to look through our
[1916.68 → 1918.68] transcripts to figure out who it was.
[1918.76 → 1922.86] But I remember, and maybe it was just a conversation I had at a conference.
[1922.86 → 1931.72] But the idea was that doing good data science or doing good AI development in good meaning
[1931.72 → 1932.72] in an ethical sense.
[1932.88 → 1937.80] So being an ethical data scientist or being an ethical AI developer actually works to your
[1937.80 → 1941.02] benefit development wise in the long run.
[1941.72 → 1947.04] So one example of that is thinking about, you know, when I read those list of topics in that
[1947.04 → 1951.78] paper that I was mentioning, one of them had to do with like auditing and tracing and that
[1951.78 → 1952.36] sort of thing.
[1952.36 → 1958.44] So basically understanding like this data was used to train this model, which output this
[1958.44 → 1962.10] prediction at this time based on this data from my user.
[1962.30 → 1966.96] And so all of that sort of auditable and traceable, there's that data lineage.
[1967.74 → 1971.12] So if you put the work in, and it's extra time, right?
[1971.16 → 1976.64] But if you put the work in to putting tooling, whether that's just some good logging or whether
[1976.64 → 1983.36] that's some great, you know, there are several products now that allow you to trace experiments
[1983.36 → 1986.26] and in that sort of thing.
[1986.26 → 1993.50] But if you put the work in to implement those solutions, then actually it does help you in
[1993.50 → 1994.20] the long run.
[1994.20 → 1999.82] Because as you're doing your own training, you know, being able to trace what hyperparameters
[1999.82 → 2005.98] you selected and trained on before and what data you used before to get these certain numbers,
[2005.98 → 2010.56] it actually helps kind of elevate your future work because you have a better understanding
[2010.56 → 2014.68] of what you did in the past, and you can track things much better over time.
[2015.18 → 2021.22] So I think the argument is that, you know, yes, it's faster to just spin up a notebook
[2021.22 → 2026.64] and do the thing and export the model and just, you know, copy, paste it over to somewhere
[2026.64 → 2030.22] and run it somewhere in a totally non-traceable manner.
[2030.22 → 2036.62] But even outside the ethical side of things, you're kind of shooting yourself in the foot
[2036.62 → 2039.90] at some point if you plan on doing that over and over again.
[2040.32 → 2046.16] And so there is some of this argument that, you know, it's slower to implement some of these
[2046.16 → 2046.46] things.
[2046.46 → 2051.82] But once they're implemented, I think you can have confidence that actually doing good or
[2051.82 → 2058.38] ethical work will actually work to your benefit development wise as well in many
[2058.38 → 2058.78] cases.
[2058.92 → 2064.00] I also think of like the scenario when I teach, I often, and I think I mentioned this on the
[2064.00 → 2070.34] show maybe a time or two, like if you're developing a self-driving car in Sweden and you do make
[2070.34 → 2076.02] a great product, and then you want to export it internationally and you, you know, ship your
[2076.02 → 2081.22] car over to Australia and the first thing it sees is a kangaroo, and it runs off the road
[2081.22 → 2083.36] and kills its, you know, passengers.
[2083.78 → 2087.34] That could have been solved by thinking about the biases in your data.
[2087.34 → 2092.40] Data and the target markets that you're going after and what's represented in your data
[2092.40 → 2093.34] set and all of that.
[2093.48 → 2099.46] So these sorts of things can work to your benefit development and product wise over time.
[2099.92 → 2101.04] I totally agree with that.
[2101.30 → 2105.70] And I actually want to point a distinction is I know at the very beginning of when you
[2105.70 → 2107.14] were talking, you said governance.
[2107.34 → 2111.70] I would actually argue having listened to you just now that much of what you were talking
[2111.70 → 2113.92] about was really more on the compliance side.
[2113.92 → 2119.30] The two go together, but how do you know that as you're going through something that
[2119.30 → 2123.38] you are in compliance with what those values are and without slowing you down?
[2123.52 → 2129.16] So I think I would start with the fact that this is a great place where you can use in
[2129.16 → 2131.32] a lot of cases technology to help you get there.
[2131.58 → 2136.68] And then on the process side, the governance side of kind of being able to handle when things
[2136.68 → 2138.12] don't come out as you expect.
[2138.12 → 2140.76] And, you know, you can go back and do that analysis.
[2141.00 → 2145.08] You know, when you were talking about tooling, helping you and being able to know what data
[2145.08 → 2145.82] was used when.
[2146.08 → 2150.52] As an example, what came to mind as you were saying that was we've had pachyderm on the
[2150.52 → 2150.76] show.
[2150.90 → 2155.40] And if I recall, that sounds like some of the capability in the file system on that solution.
[2155.84 → 2159.48] So when you're implementing AI ethics, that might or might not.
[2159.56 → 2160.52] There may be others as well.
[2160.52 → 2167.14] But that might be one of your ways of trying to automate some of the abilities to be in
[2167.14 → 2171.76] compliant so that you are not necessarily just slowing yourself down with a lot of manual
[2171.76 → 2173.40] intervention with this.
[2173.68 → 2178.22] And you have a governance process so that when unexpected outcomes do arise, going back to
[2178.22 → 2184.72] your kangaroo example, you can kind of go back and figure out, you know, what went wrong
[2184.72 → 2189.24] and, you know, how did it deviate specifically from what you were trying to do?
[2189.24 → 2193.74] I know for me, I look at, we've talked about a couple of industry principles.
[2194.20 → 2198.58] I tend to work a lot with the U.S. Department of Defence principles, which are responsible,
[2199.20 → 2201.40] equitable, traceable, reliable, and governable.
[2201.48 → 2204.58] And there's verbiage with each of those that our listeners can go look at.
[2205.00 → 2211.30] But from the standpoint of your kangaroo example, you can say, well, right off the bat, that would
[2211.30 → 2214.66] at least be a violation of responsible and reliable.
[2214.66 → 2219.80] And there's specific language that tells us what those two terms mean in this context.
[2220.02 → 2225.40] And so as you're looking at that problem that you just described, then you go back, and you start
[2225.40 → 2226.76] tracing that back.
[2226.86 → 2233.04] And traceable happens to be another one of the five in terms of what goes back to allow you to assess
[2233.04 → 2233.88] what went wrong.
[2234.16 → 2239.24] Why did that model give you an outcome in that situation that was not as expected?
[2239.24 → 2241.08] And that's what governance is right there.
[2241.34 → 2245.62] That is going back and saying, how do we fix the problems that we're going to have?
[2245.66 → 2246.98] Because we certainly will have those.
[2247.20 → 2249.26] This is why you go through this whole process.
[2249.38 → 2252.72] It's to ensure that as you go forward, things do get better and better.
[2252.92 → 2255.68] And better means outcomes that you expect.
[2255.98 → 2259.98] And so I don't know if I answered everything that you posed to me at that one.
[2260.38 → 2261.88] Yeah, it's good points.
[2262.16 → 2265.20] A lot of what I'm thinking of with this is the sort of trickle down.
[2265.20 → 2270.32] And I think part of that was motivated by some of the teaching I've done on the subject.
[2270.68 → 2276.60] And oftentimes a question when I'm entering into this sort of discussion, a question comes
[2276.60 → 2284.10] up about, well, if including a sensitive feature in my model, like let's say gender or whatever
[2284.10 → 2292.96] it is, improves the model performance in terms of the accuracy on my test set or whatever
[2292.96 → 2296.64] it is, why would I not include that feature in the data?
[2296.72 → 2300.10] Or why would I be careful about how I treat that feature in my data?
[2300.40 → 2305.02] Isn't the sort of accuracy what I'm most concerned about?
[2305.18 → 2305.66] It might be.
[2305.80 → 2307.50] The answer is maybe on that.
[2307.66 → 2310.32] Go ahead and finish because I didn't mean to cut you off, but I'm going to come back
[2310.32 → 2310.56] to that.
[2310.84 → 2311.58] I agree with you.
[2311.70 → 2312.08] Maybe.
[2312.30 → 2316.82] But I think also that, so there's a paper that I was reading before a conversation today
[2316.82 → 2322.90] on the role and limits of principles in AI ethics towards a focus on tensions from a
[2322.90 → 2323.58] group at Cambridge.
[2323.94 → 2328.66] And they were talking about some of these natural tensions or tradeoffs when we're thinking
[2328.66 → 2329.34] about ethics.
[2329.34 → 2333.88] And one of those was this, you know, using data to improve the quality and efficiency
[2333.88 → 2338.48] of services versus respecting privacy and autonomy of individuals.
[2338.48 → 2340.50] And there's others of these tensions.
[2340.50 → 2348.44] But I think what it comes down to for me is that as AI practitioners, the things that
[2348.44 → 2354.82] drive that sort of performance and accuracy for us is data that has been generated in the
[2354.82 → 2355.74] real world, right?
[2355.80 → 2362.84] We parameterize our models based on observations that have happened and been recorded in data
[2362.84 → 2364.00] from the real world.
[2364.00 → 2369.58] And the bottom line is that our real world is broken in many ways, right?
[2369.66 → 2372.64] And there are very bad things that happen in our real world.
[2372.82 → 2377.36] There's over-representation and underrepresentation that happens in our world.
[2377.90 → 2382.52] And depending even on just where you get the data or how you gather it, you know, you're
[2382.52 → 2384.92] never going to have the ideal data set.
[2385.48 → 2392.70] And so really what it comes down to is for me is are you trying to get the best performance
[2392.70 → 2398.74] you can on your sample of test data, which is not representative of the whole world anyway?
[2399.34 → 2406.94] Or are you trying to ethically create a model that performs very well, but also at the same
[2406.94 → 2413.52] time does not discriminate or treat unfairly or use data in an unethical way?
[2413.84 → 2416.50] I think that those things have to be paired together.
[2416.50 → 2422.30] You can't, you know, from my perspective, it's not right, you know, to just take the
[2422.30 → 2425.72] performance at the expense of considering those other things.
[2426.18 → 2427.98] I think not only I would agree with that.
[2428.08 → 2428.96] It's interesting.
[2429.28 → 2432.22] We've used privacy as our example a bunch of times.
[2432.62 → 2438.02] And in some context, you're looking and saying, well, if I had a performance capability
[2438.02 → 2443.32] that I can add in, but I do that at the expense of privacy, do I want to do that?
[2443.32 → 2447.14] That is exactly why you want to have those ethical principles in place.
[2447.58 → 2454.06] And while on first blush, that may seem self-evident to most of our listeners and us as we sit here,
[2454.18 → 2458.42] but I'll give you an example of where it may not be as evident, you know, or at least you
[2458.42 → 2459.70] have to think about it just a little bit.
[2459.92 → 2464.88] There are cases where privacy is not necessarily one of the things that you're trying to achieve.
[2465.18 → 2469.76] An example of that, and this comes from obviously the larger world in which I work, is if you
[2469.76 → 2475.02] have an intelligence satellite that does intelligence surveillance and reconnaissance, and its purpose
[2475.02 → 2481.94] is to go over a foreign nation and get as much intelligence as you can, that is very distinctly
[2481.94 → 2485.38] not something that is putting privacy as one of your values.
[2485.54 → 2486.48] You're basically rating that.
[2486.60 → 2491.62] So in that case, in that particular example that you gave us, the performance versus privacy,
[2491.94 → 2496.60] performance wins every time because of the nature of what you're trying to do and the
[2496.60 → 2498.18] governing principles that you're using.
[2498.34 → 2504.70] But if you were to say, I work for one of the large tech firms, Google or Microsoft or
[2504.70 → 2509.20] Amazon, something like that, and said, for performance, am I willing to give up privacy?
[2509.36 → 2514.88] Well, even if you personally were willing to give up privacy, your customers probably aren't
[2514.88 → 2515.82] going to agree with you.
[2516.36 → 2522.14] And to do something like that would probably be devastating to your business, you know, particularly
[2522.14 → 2525.32] if you get caught doing something that your customers are not okay with.
[2525.32 → 2527.98] And we've seen examples of that many, many times.
[2528.10 → 2530.74] Facebook is another one that comes to mind as I talk through that.
[2531.10 → 2536.30] And so you're literally looking at the same set of value judgments, but coming out in very,
[2536.42 → 2541.80] very different ways, depending on how you're choosing to arrange those values in your principles.
[2541.94 → 2546.54] So the point I'm making is that having those principles really matters.
[2546.54 → 2551.90] And the context of what your organization does with those principles really matters.
[2551.90 → 2556.30] And you can have very, very different outcomes based on those.
[2556.62 → 2557.18] Yep.
[2557.52 → 2565.96] I guess one thing I should say is we'll put links to some of the main industry AI principles
[2565.96 → 2569.94] that Chris and I have reviewed in preparation for the show.
[2570.04 → 2573.88] We'll put a link to those in our show notes, along with the various papers that we're discussing.
[2573.88 → 2580.88] One other paper that drew my attention was talking about principles alone cannot guarantee ethical
[2580.88 → 2581.26] AI.
[2581.88 → 2586.40] And now that we're kind of getting down into how this plays out, I think that that was a
[2586.40 → 2589.46] very interesting paper that maybe people should take a look at.
[2589.54 → 2590.90] It appeared in Nature.
[2591.46 → 2599.50] And it's talking about where we might fall short in terms of the AI principles that are coming
[2599.50 → 2599.82] out.
[2600.54 → 2605.88] One of those might be this sort of trickle-down effect and creating, you know, sustainable
[2605.88 → 2611.80] pathways to impact and accountability in terms of ethical AI, which I think comes down to more
[2611.80 → 2613.48] of an implementation thing.
[2614.02 → 2619.86] But they also kind of bring up this kind of interesting idea, which I've also heard other
[2619.86 → 2621.92] people talking about in terms of AI.
[2622.06 → 2627.58] And I don't know if I fully developed a thought process around, but they talk about licensing
[2627.58 → 2632.40] AI practitioners similar to like a doctor would have a license or something because their
[2632.40 → 2636.68] profession is very risky in terms of what they do.
[2636.82 → 2641.02] Or maybe a pilot license in terms of, you know, when you're flying people around, there's
[2641.02 → 2642.48] an inherent risk in that.
[2642.48 → 2647.80] And there are risks in terms of the AI that we developed, especially if we're talking about,
[2647.92 → 2655.68] you know, cars are autonomous or maybe systems that are implemented in airplanes or, you know,
[2655.68 → 2658.14] whether you get insurance or not.
[2658.32 → 2660.26] And that's driven by certain algorithms.
[2660.70 → 2662.18] I don't know if you have any thought about that.
[2662.44 → 2662.64] I do.
[2662.96 → 2667.00] It kind of scares me a little bit because I don't know if I want to get a license, but
[2667.00 → 2668.60] I get where they're coming from.
[2668.80 → 2672.16] There's a lot of people that have put a lot more thought into this than myself.
[2672.84 → 2673.28] Yeah.
[2673.38 → 2680.10] So I think I would note that we are still in the very, very early days of artificial intelligence.
[2680.10 → 2687.76] And the world in which we're operating right now is largely devoid of legal frameworks and
[2687.76 → 2689.54] regulatory frameworks.
[2689.86 → 2694.10] Now, before people start objecting and naming their favourite one, there are some, and I'm
[2694.10 → 2694.88] acknowledging that.
[2694.88 → 2700.48] But compared to other areas that may be regulated, we are still trying to figure out what that
[2700.48 → 2700.74] means.
[2700.88 → 2707.46] So national and local laws are, and international law is trailing far behind where the technical
[2707.46 → 2708.46] capability is.
[2708.46 → 2714.50] So I think that is one of the conversations that we need to have in the years ahead is
[2714.50 → 2720.78] figuring out how to have the appropriate regulatory, whether it's licensing or whether it is other
[2720.78 → 2722.58] constructs that you may do.
[2723.18 → 2728.44] You know, our legal and regulatory frameworks are supposed to reflect our values in the world
[2728.44 → 2733.30] and the various things that we have to do to keep people safe and protect certain rights.
[2733.30 → 2739.04] And we have largely not done that, not only with AI, but with lots of different technologies
[2739.04 → 2739.88] in recent years.
[2740.06 → 2746.48] So there's a conversation and an adjustment that really needs to be had in the days ahead.
[2746.62 → 2748.46] And I think that's going to be pretty crucial.
[2748.88 → 2756.12] And it's funny, I know on this show, we are, you know, either AI practitioners or we're at least
[2756.12 → 2759.40] minimally by tuning in, you're an AI enthusiast.
[2759.40 → 2762.70] In most cases, you care about this topic and want to do that.
[2763.06 → 2767.94] And so it makes sense for us, our collective community here to want to engage in this.
[2768.04 → 2774.22] But what I would actually urge you to do is because AI impacts so many people, and ultimately
[2774.22 → 2777.40] most of the people in the world can be impacted in various ways.
[2777.98 → 2782.64] You really need to bring the people into the conversation that aren't necessarily as familiar
[2782.64 → 2785.38] with it as all of us are, because it does impact them.
[2785.46 → 2787.00] They have a right to have a voice in it.
[2787.04 → 2793.50] And I think all of us, it's incumbent upon us to explain these issues objectively, as scientists,
[2793.64 → 2800.78] you may say, ourselves, to make sure that the public understands what the implications
[2800.78 → 2801.82] of these things are.
[2802.02 → 2806.60] So we haven't really, in a meaningful way, started that conversation yet.
[2806.74 → 2809.10] I'm hoping to see that in the next few years.
[2809.10 → 2810.50] Yeah, definitely.
[2810.70 → 2812.20] I'm hoping for similar things.
[2812.78 → 2817.44] As we close out here, this episode, of course, in these fully connected episodes with just
[2817.44 → 2821.22] Chris and me, we always like to share some learning resources.
[2821.74 → 2824.58] And maybe Chris has one that he wants to share.
[2824.64 → 2825.72] I'm not sure, but...
[2825.72 → 2826.50] I do, actually.
[2826.64 → 2830.86] Yeah, one that I wanted to share, which I've mentioned a couple of times on the show, which
[2830.86 → 2838.44] is just a very practical piece of tooling, which gets to maybe some of these, but not
[2838.44 → 2843.84] all the ideas that we talked about, but at least gets started as the project from Driven
[2843.84 → 2849.52] Data called Dean, or Dean, which is an ethics checklist for data scientists.
[2849.74 → 2853.10] And what I like about this is it's just not a static checklist.
[2853.10 → 2859.32] It's an actual Python project where you can embed a checklist in your Jupyter notebooks
[2859.32 → 2866.36] or in your Python code repository and actually have that there right with your code where
[2866.36 → 2867.64] you're developing your project.
[2867.88 → 2869.06] And it's fully customizable.
[2869.30 → 2872.96] So they have a sort of default one that you can use, but you can customize it for your
[2872.96 → 2879.30] own company's ethics checklist so that actually, as you develop these things, you can implement
[2879.30 → 2884.58] them in an ethics checklist and embed that right in your project so that every project,
[2884.72 → 2889.42] even if certain things in the checklist aren't relevant to a certain project, you can at least
[2889.42 → 2894.22] check them off that you've thought about them or considered them in completing the project.
[2894.86 → 2895.70] That sounds like a good one.
[2895.94 → 2900.18] I know you've already noted that we're going to put links to a lot of these principles that
[2900.18 → 2903.42] various organizations have published out there from a learning resource.
[2903.42 → 2911.48] And I'm going to suggest folks do what I have done in quite a bit of detail is go to half
[2911.48 → 2914.84] a dozen different, you know, published principles that are out there.
[2914.90 → 2920.00] You know, go to the Googles, Microsoft's, and others like that and read what they've done
[2920.00 → 2922.24] and compare it, analyze between the two.
[2922.40 → 2928.00] Have them up on the screen at the same time with their explanations and try to discern why
[2928.00 → 2933.00] they might have chosen the verbiage and the particular ways of describing it that each
[2933.00 → 2933.50] is done.
[2933.86 → 2937.62] And you'll find a lot of commonality, and you'll find some very distinct differences.
[2937.98 → 2938.44] Do that.
[2938.54 → 2942.30] You might throw in the Department of Defence one because it has a different thing that
[2942.30 → 2944.28] it's trying to achieve from a commercial entity.
[2944.64 → 2950.44] So it allows you to see a diversity of thought that has a lot of common points, but allows
[2950.44 → 2952.50] you to kind of put some critical thinking around it.
[2952.54 → 2957.26] And then as a second step is after you've done that, choose what you think would be good
[2957.26 → 2962.28] principles for your organization and try to do a little mind exercise where you think
[2962.28 → 2964.96] about how does this work in your own organization?
[2964.96 → 2970.78] How do you get it from the principles into your own organization's approach to work and
[2970.78 → 2976.10] the policies that govern that through governance and the compliance that you're trying to implement
[2976.10 → 2980.82] into the tools and the workflow integrations that your organization is engaged in?
[2980.94 → 2987.02] How do you get from that fluffy high level all the way into something that directly affects
[2987.02 → 2990.46] your customers or whoever your organization is working for?
[2990.46 → 2993.96] So that's just going through that process is really educational.
[2994.16 → 2996.32] And then there's another one that I wanted to suggest.
[2996.66 → 3001.54] Not long ago on episode 85, we had Stuart Russell as a guest on the show.
[3002.18 → 3003.26] He's a Berkeley professor.
[3003.58 → 3008.08] He's a legend in the AI community, has been doing this for decades in its various forms.
[3008.08 → 3012.86] And he's written several editions of Artificial Intelligence, A Modern Approach, which is kind of
[3012.86 → 3017.02] one of the key textbooks in this industry as it's evolved over time.
[3017.02 → 3022.54] And he has also more recently written a book that's intended for a general audience called
[3022.54 → 3023.52] Human Compatible.
[3024.10 → 3028.42] And read that book because it talks about some of these same issues and his own thoughts on
[3028.42 → 3031.90] how he would address it and what he thinks is important on that.
[3032.00 → 3035.40] And I know in that episode, I thought that was a fascinating conversation.
[3035.54 → 3038.38] I thoroughly enjoyed the conversation with Professor Russell.
[3038.38 → 3045.04] And so he really addresses AI that avoids harmful unintended consequences and offers a path forward
[3045.04 → 3050.64] towards a future on which humans can safely rely on provably beneficial AI.
[3051.00 → 3053.66] And at the end of the day, that's what you're trying to do with AI ethics.
[3054.08 → 3056.40] You know, that is the outcome you're trying to get to.
[3056.52 → 3060.16] So I recommend the book and hope that we'll get people started on this path.
[3061.00 → 3061.12] Excellent.
[3061.34 → 3063.02] Yeah, we'll put that link in our show notes.
[3063.02 → 3068.92] Please let us know in our community online your thoughts around AI ethics and things that
[3068.92 → 3070.08] have been useful for you.
[3070.20 → 3076.16] You can find us on changelog.com slash community and in Slack and LinkedIn and Twitter.
[3076.86 → 3078.82] And looking forward to hearing from you.
[3078.96 → 3081.08] Thanks for bringing your thoughts around this today, Chris.
[3081.16 → 3084.72] Really enjoyed the conversation and looking forward to talking to you next week.
[3085.26 → 3085.74] It was good.
[3085.84 → 3086.48] Thanks a lot, Daniel.
[3086.72 → 3087.26] Bye-bye.
[3087.26 → 3093.52] Have you joined the free changelog community yet?
[3094.00 → 3095.30] I'm not sure what you're waiting for.
[3095.94 → 3101.62] You get changelog news, email notifications of new podcast episodes, access to our community
[3101.62 → 3106.72] Slack and Practical AI channel where fun and interesting AI discussions take place all
[3106.72 → 3108.98] the time, all for the price of a free hot dog.
[3109.34 → 3111.78] Check us out at changelog.com slash community.
[3111.92 → 3112.62] We'd love to have you.
[3113.18 → 3116.18] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[3116.18 → 3121.04] It's produced by me, Jared Santo, and our music is provided by the mysterious Break master
[3121.04 → 3121.48] Cylinder.
[3121.82 → 3124.44] We're brought to you by some amazing companies who get it.
[3124.50 → 3126.88] Thanks to Vastly, Linde, and Rollbar.
[3127.86 → 3128.86] That's all for now.
[3129.18 → 3130.42] We'll talk to you again next week.
[3130.42 → 3131.22] We'll see you again next week.
[3131.22 → 3131.42] We'll be right back.
[3131.42 → 3144.02] We'll see you again next week.
[3144.02 → 3148.62] We'll see you again next week.
[3148.62 → 3178.60] Thank you.
