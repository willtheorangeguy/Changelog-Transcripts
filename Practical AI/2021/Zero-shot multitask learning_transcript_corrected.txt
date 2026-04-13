[0.00 → 5.10] There has been more change in the last 30 years than for centuries before that.
[5.18 → 9.46] And then if you add the last couple of millennia, it's for tens of millennia before that.
[9.70 → 12.56] It's accelerating so much that we are in a unique state.
[12.56 → 16.84] If you go forward in time after you and I are gone, they're going to look back on this
[16.84 → 17.96] as pioneering days.
[18.34 → 21.84] We are the people sitting out across the American prairie.
[22.18 → 26.22] But that's where we're at right now as the world is changing more dramatically than it
[26.22 → 26.66] ever has.
[26.66 → 31.62] It's worth once in a while remembering just how far we've come in just such a short
[31.62 → 32.14] amount of time.
[35.34 → 37.96] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[38.34 → 38.90] We love Linde.
[38.90 → 40.40] They keep it fast and simple.
[40.52 → 42.88] Check them out at linode.com slash changelog.
[43.02 → 45.18] Our bandwidth is provided by Vastly.
[45.54 → 49.08] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[49.34 → 51.06] Get a demo at LaunchDarkly.com.
[51.62 → 54.94] This episode is brought to you by our friends at Rudder stack.
[54.94 → 58.64] And we're calling all data engineers to check out Rudder stack Cloud and start building smart
[58.64 → 59.66] customer data pipelines.
[60.16 → 61.90] Rudder stack is warehouse first.
[62.10 → 63.06] No more silos.
[63.52 → 67.44] Rudder stack builds your customer data lake on your data warehouse, not theirs, enabling
[67.44 → 72.56] all functionality of a CDP with more security and retaining full ownership of your data.
[72.86 → 75.32] It's open source and API first.
[75.68 → 79.10] Rudder stack can be easily integrated into your existing development processes.
[79.10 → 82.40] And because they're open source, you can see all their code.
[82.62 → 85.06] So you don't have to worry about vendor lock-in or black boxes.
[85.60 → 87.18] And best of all, they have transparent pricing.
[87.36 → 89.62] Stop paying your CDP a premium to store your data.
[90.10 → 94.96] Rudder stack is free up to 500,000 events and pricing scales transparently from there.
[95.40 → 97.44] Learn more and get started at Rudderstack.com.
[97.76 → 99.96] Again, Rudderstack.com.
[99.96 → 103.66] That's R-U-D-D-E-R-S-T-A-C-K.com.
[113.38 → 118.36] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[118.68 → 120.44] productive, and accessible to everyone.
[120.76 → 124.84] This is where conversations around AI, machine learning, and data science happen.
[124.84 → 128.58] Join the community and Slack with us around various topics of the show at
[128.58 → 129.92] changedog.com slash community.
[130.24 → 131.20] And follow us on Twitter.
[131.34 → 132.92] We're at Practical AI FM.
[139.12 → 144.48] Welcome to another fully connected episode of the Practical AI podcast.
[145.28 → 151.22] In these episodes, Chris and I keep you fully connected with everything that's happening in the AI community.
[151.22 → 154.86] We'll take some time to discuss some of the latest AI news,
[155.04 → 159.76] and we'll dig into some learning resources to help you level up your machine learning game.
[160.18 → 161.16] I'm Daniel Whiten ack.
[161.30 → 164.98] I am a data scientist at SIL International,
[165.32 → 168.18] and I'm joined as always by my co-host, Chris Benson,
[168.70 → 170.82] who is a strategist at Lockheed Martin.
[171.12 → 171.78] How are you doing, Chris?
[172.02 → 172.82] Doing great, Daniel.
[173.06 → 178.08] Just enjoying the day, tearing through all the AI and deep learning news out there.
[178.50 → 180.14] Having a good time, as always.
[180.14 → 182.12] There's always interesting stuff, right?
[182.26 → 182.72] There is.
[182.88 → 186.38] Yeah, and we're coming up on here in the States,
[186.58 → 188.60] coming up on U.S. Thanksgiving,
[189.14 → 191.56] for those that are familiar with the holiday.
[191.88 → 193.82] So we'll get a little bit of time off.
[194.14 → 195.70] And I'm looking forward to that.
[195.80 → 197.84] It's been a long couple weeks.
[198.10 → 203.04] I submitted a few conference papers to a deadline on,
[203.34 → 205.38] well, the deadline was Monday.
[205.38 → 211.92] But the deadlines for these research conferences are like midnight anywhere on Earth or something like that.
[212.06 → 214.16] So it's actually in my time zone.
[214.44 → 216.56] It was 7 a.m.
[216.62 → 219.46] The next day was the deadline, right?
[219.46 → 228.64] So basically that meant that there wasn't a lot of sleep that was happening from like Monday to Tuesday morning at 7 a.m.
[228.64 → 232.28] And I think some last minute changes and submissions.
[232.78 → 236.40] So I think I'm still catching up a little bit on sleep after that.
[236.46 → 239.88] But I'm really happy with, you know, with my team and what we submitted.
[240.10 → 240.86] So that's good.
[240.86 → 241.18] Gotcha.
[241.32 → 243.68] Well, as you're looking in, I know our listeners can't see it,
[243.70 → 247.92] but as you're looking at the video feed of me, I'm the one in the centre, okay?
[248.36 → 251.60] From the sleep deprivation, the multiple Chris's and stuff.
[251.80 → 252.42] Yeah, yeah.
[252.58 → 254.62] Well, I appreciate that clarification.
[255.04 → 256.06] That'll help throughout.
[256.36 → 261.10] And, you know, if you see me doze off, just send a virtual poke or something.
[261.20 → 261.54] You remember?
[261.80 → 262.10] Pokes?
[262.30 → 263.12] It was on Facebook.
[263.28 → 264.66] That was like one of the first things, right?
[264.80 → 265.32] On Facebook.
[265.54 → 269.10] I never figured out really how to use a poke the right way.
[269.28 → 270.56] It just never made sense.
[270.56 → 273.80] I think I poked one person, and then I felt silly, and I never did it again.
[273.92 → 275.48] So I'm not sure what it is.
[275.84 → 280.72] Maybe it is worthwhile for our listeners to kind of talk a little bit.
[280.96 → 284.46] I'm sort of taking note that conferences are happening again.
[284.64 → 288.36] And at least in a hybrid sense, you know, of course,
[288.44 → 291.26] virtual conferences happen through COVID times,
[291.26 → 294.16] but normal conferences are happening again.
[294.60 → 300.16] And maybe it would be worth for our listeners to just kind of talk through a bit of the landscape
[300.16 → 303.96] of conferences because occasionally I get questions about,
[304.18 → 311.18] hey, I'm starting my interest in AI or our team is working in AI, and we've done some cool things.
[311.18 → 314.76] I'd like to disseminate that somehow to the community.
[314.98 → 316.60] How do I do that?
[316.60 → 318.64] So some teams are getting into this.
[318.72 → 323.94] They don't know like what conferences there are and how to start involving themselves in that community.
[323.94 → 333.32] So, yeah, one thing to note is that there's sort of research focused conferences that are primarily involving academics,
[333.56 → 338.58] although industry researchers as well from groups like, you know, Google or other places.
[338.84 → 342.26] And then there are kinds of industry conferences.
[342.88 → 346.96] Well, they used to have O'Reilly AI, but yeah, they stopped doing it last I heard.
[346.96 → 348.48] I think they stopped doing that one.
[348.60 → 350.36] There's like Open Data Science Conference.
[350.84 → 352.84] Maybe you can think of some others.
[353.12 → 353.54] NVIDIA.
[353.84 → 355.28] NVIDIA is a big one.
[355.38 → 356.82] They have several, you know, each year.
[357.14 → 359.84] Yeah, NVIDIA, GTC and other ones.
[360.08 → 365.52] So there is kind of a major difference between these two types of conferences and people might not be aware of this.
[365.74 → 372.72] So some of the things like recently we saw the big science working group come out with the T0 model,
[373.00 → 375.60] which we can talk about that later in the episode, but that's pretty cool.
[375.60 → 380.56] But that was submitted as a research paper to a research conference.
[381.00 → 383.90] And that is actually a sort of peer-reviewed process.
[384.20 → 388.48] And that's what I mentioned earlier on that we were submitting early in the week is,
[388.74 → 395.70] hey, I created a new type of neural network, or I applied a neural network in a slightly different way than no one's ever done before.
[396.00 → 403.52] Or, you know, maybe I created a new data set that is in a new language, or it's different from what people have done before.
[403.52 → 405.98] Or it includes different types of data.
[405.98 → 417.20] And I want to publish that as a sort of original work and have it peer reviewed by experts giving feedback and eventually accepted as a conference paper,
[417.20 → 430.06] which basically means that it's been peer-reviewed by other researchers in the field and deemed to be original and sort of scientifically and experimentally valid,
[430.06 → 431.90] at least based on the review.
[431.90 → 439.06] That doesn't happen in an industry conference for the most part where some talks are maybe invited.
[439.66 → 442.96] And in certain cases, there's a call for proposals for talks.
[443.14 → 447.70] But those talks that are submitted are not peer-reviewed in that way.
[447.70 → 454.80] So you might say, hey, I'd like to propose a talk about our AI infrastructure at SIL International.
[455.44 → 457.08] And I could talk about that.
[457.18 → 461.32] It's not like we're doing sort of original things necessarily that others haven't done,
[461.40 → 466.80] but it's useful in a practical sense for people to also hear that information, ask questions,
[466.92 → 470.40] have it be part of the topic practically at a conference.
[470.70 → 472.06] I don't know if there's anything you want to add to that.
[472.12 → 475.84] I just thought maybe the listeners might not be familiar with that whole world.
[475.84 → 481.66] No, I think that's perfect in the sense of being able to distinguish between the two and understanding what you're going to.
[482.02 → 487.48] Most of the conferences I've been at were on the commercial slash industry side as opposed to the research side.
[487.52 → 489.76] And they're very different cultures, as you just pointed out.
[490.00 → 498.12] And there's definitely in the industry side, you know, a desire to kind of say, look what we've done from more of a business standpoint.
[498.24 → 501.34] It may not be trying to sell you something, but they both do prestige.
[501.34 → 506.34] But there's a there's kind of a different approach to it and different communities that you're you're selling it.
[506.76 → 513.16] And it makes it interesting to go to both, which I would encourage people to do because they're very different experiences going to the two.
[513.52 → 522.60] Yeah. And that's not to say that's a good point, Chris, because you don't even have to present something to go to either one of these types of conferences.
[523.12 → 525.46] Yeah. Most people are not presenting. Most are just listening.
[525.46 → 535.40] Right. Exactly. So, you know, if maybe you're out there, and you're thinking, well, how do I get connected in the AI industry or in AI research?
[535.74 → 544.42] Well, look maybe for a conference on the research side, like Neurons or ACL or EM NLP, something like this.
[544.42 → 554.08] And, you know, you could just attend and, you know, ask questions, get connected with people, see how it plays out and how papers are presented and what they look like.
[554.20 → 564.84] Or if you're on the industry side, and you just want to do that networking, get connected, see practically how people are applying AI or doing infrastructure or something like that, just attend.
[564.96 → 566.96] And, you know, you can learn a lot.
[566.96 → 572.16] So last week I went to a conference, I gave a it was just like a six-minute presentation.
[572.66 → 574.40] And so I didn't have to prepare that much.
[574.44 → 579.40] And for the other three and a half days, I was just participating as a participant.
[580.04 → 582.38] And that was great. I really enjoyed it.
[583.10 → 586.72] I'll bet. And it's been a while because of the pandemic since I've been to one now.
[586.90 → 593.88] And as the world opens up, and maybe we don't have a winter spike, if we're really, really lucky, then maybe we can get there sooner.
[593.88 → 600.04] I would also say that it's interesting that there's a different experience if you're a new conference goer.
[600.28 → 610.96] So if this is your first conference or two versus someone who's been to many, then you also, as you go more often, you learn the value of what's available that's not a session.
[611.40 → 617.98] And you end up spending a lot of time making friends and having fascinating hallway conversations.
[617.98 → 627.42] I think most people who go the first time, they feel like they need to get as many sessions in as they can and see as much because they think that that's the best way to get the value.
[627.58 → 632.24] But some of the best takeaways I've ever had were from ad hoc conversations.
[632.76 → 639.86] It's a moment where if you can get over any shyness that you might have, you should just walk up to a group of people and introduce yourself and just be bold.
[639.86 → 644.94] And they will welcome you in, and you'll hear things that you can't hear anywhere else often.
[645.20 → 650.18] And people will share in a small group, even a small group of strangers, things that they would not say on stage.
[650.50 → 659.22] So I've had some really, really memorable moments that were not in formal sessions per se and would encourage people to do that.
[659.26 → 662.36] It's one of the reasons to show up in person instead of it being a virtual.
[662.36 → 668.08] You also get a sense sometimes of things that are really kind of hard to pick up online.
[668.60 → 679.22] So online, for example, I could research experiment tracking software for my AI projects like I'm going to queue up a job.
[679.34 → 680.40] It has this data.
[680.70 → 681.58] It's going to run.
[681.66 → 683.06] It produces these metrics.
[683.10 → 684.30] I'm going to track all that stuff.
[684.60 → 688.70] Well, I could research around and see like, how are people doing that?
[688.84 → 689.64] What are they doing?
[689.72 → 690.96] Are they rolling their own?
[690.96 → 694.38] There are different types of those kinds of things out there.
[694.72 → 704.28] But if you're at a, you know, a lunch table at a conference with seven to 10 other practitioners, actual practitioners from a variety of organizations.
[704.28 → 706.36] I mean, that is a huge value.
[706.36 → 711.14] And, you know, if that topic comes up, you know, asking, hey, what do people use for this?
[711.24 → 713.90] It's not like a complete industry survey.
[713.90 → 728.56] But even just in those few seconds, you get a real good sense about like, you know, how often this is on people's mind and what they're using in terms of specific tooling and how important it is or not important it is in different organizations.
[728.56 → 731.98] And yeah, I actually want to follow up on that because you raise a great point.
[732.58 → 739.86] If you go with other people from your organization, and it's time for the lunch break or whatever, don't stay together.
[740.28 → 741.12] Everybody break.
[741.12 → 742.28] Oh, yeah, that's a good tip.
[742.28 → 742.60] Yeah.
[742.76 → 754.98] Everybody break up and go to an individual table that has nobody that you know in it and fit in on that and then start the conversation, join in the conversation that's there or start it if everyone's being too shy.
[754.98 → 764.52] And then have those rich conversations and then go back later with your colleagues separately when you're not doing that and share what happened and share what you learned and stuff.
[764.60 → 773.22] And that's a really, perfect way to get a solid investment out of those dialogues for your organization is to bring them all back and let everyone benefit from it.
[773.30 → 773.42] Yeah.
[773.46 → 775.80] Conferences are not the time to be a shy person.
[775.96 → 778.80] It's its the time to put on your bold hat and go forward.
[778.80 → 779.28] Yeah.
[779.38 → 783.86] Me as an introvert and introvert in a sort of strange way where.
[783.86 → 785.02] That is a podcast host.
[785.12 → 785.26] Yeah.
[785.44 → 791.10] I'm one of those introverts that genuinely enjoys having conversations with people, but it's incredibly tiring for me.
[791.24 → 791.42] Yeah.
[791.62 → 791.84] Right.
[791.90 → 796.90] Like if I'm talking, if I'm having a full day of meetings, I'm just dead by the end of the day.
[797.22 → 799.16] So I do that at conferences.
[799.40 → 801.94] I intentionally go and speak with people.
[802.06 → 806.26] But then I also intentionally have sometimes where I'm like, you know what?
[806.48 → 811.70] There's these few sessions happening for the next hour, but I'm going to go outside.
[811.70 → 812.06] Yes.
[812.06 → 818.96] I walk to this place and get a coffee and like no one's going to bother me, and I am going to step away for a second.
[819.18 → 820.50] I'm not going to miss much.
[820.50 → 823.02] And I need that sort of separate time.
[823.30 → 823.62] I agree.
[823.78 → 826.60] I don't think anyone ever expects me to say I'm an introvert, but I am.
[826.68 → 829.76] I have my public moments and need those.
[829.84 → 832.50] Just like you said, I need that time to myself.
[832.50 → 837.06] And I'll do that as well during the day because you'll go through a couple of hours and just be exhausted.
[837.62 → 839.40] You just need your brain to reset.
[839.56 → 845.72] So go do something alone for a short while, reset, and then get back out there and have those conversations.
[845.98 → 849.94] Just as an aside, you know, we've been doing this podcast for a while now.
[849.94 → 853.00] It's been close to three and a half years since we started all this.
[853.60 → 859.76] And the first time that I ever had someone walk up to me and say, you're with Practical AI.
[859.96 → 860.96] It's nice to meet you and all.
[860.96 → 864.06] And the first time I was going to tell was when I was having one of those quiet breaks.
[864.26 → 871.18] I was at a conference and I walked away, and I was going to get my little private time, quiet coffee, and just kind of reset my brain.
[871.26 → 874.10] And someone walked up, and it was a special moment.
[874.28 → 877.82] And it went from private time to having a wonderful conversation.
[878.00 → 881.28] So I found some private time later, but I'll never forget that moment.
[890.96 → 905.22] This episode is brought to you by merit and their upcoming ML Data Ops Summit in partnership with TechCrunch.
[905.40 → 908.58] It's a virtual event happening December 2nd, 2021.
[908.92 → 912.84] Check out the speakers and register at iMerit.net slash Data Ops.
[912.84 → 924.56] The event is gathering more than 700 attendees from top AI and ML companies and feature major speakers, including Facebook AI, Cruise, Zoo, GE Healthcare, and more.
[925.02 → 929.48] And I'm here with Ivan Lee, the founder and CEO of Database, who's also speaking at the event.
[929.86 → 935.54] Ivan, I know you'll be speaking at the conference on this subject, but can you share a teaser of what's happening right now in the NLP space?
[935.76 → 940.84] If we look at the advances in NLP over the last few years, there have been some really exciting developments.
[940.84 → 949.32] Perhaps most notably, OpenAI's GPT-3 and their ability to just really start mimicking humans in generating snippets of English language.
[949.48 → 955.20] What we've noticed is that perhaps of all the branches of AI, NLP is one of the most mature.
[955.54 → 959.04] And there were some obvious use cases when we were starting out.
[959.20 → 963.84] There are things like the ability to handle customer support, improve upon chatbots.
[964.66 → 968.40] These were very clear verticals that we wanted to go after.
[968.40 → 976.04] But as we learned more, it turns out there are applications in the legal industry, in healthcare, in financial.
[976.50 → 986.08] There were a number of nonprofit organizations using us to label COVID-19 research and be able to just make sense of all the abundance of research that was coming out.
[986.40 → 990.98] We were kind of astounded by the creativity and the ways in which NLP could be produced.
[990.98 → 996.80] All right, learn more and register to attend for this free virtual event at imerit.net slash data ops.
[997.12 → 1003.42] Again, you'll hear from top AI and ML speakers who have successfully deployed machine learning data operations in their organizations.
[1003.94 → 1006.72] Again, this event is free and it's virtual.
[1007.30 → 1010.76] Learn more and register at imerit.net slash data ops.
[1010.76 → 1036.84] So, Chris, speaking of conferences, last week at the conference I went to, you know, typically, well, I don't know if typically,
[1036.84 → 1041.46] but many conferences will have like a conference social dinner type thing.
[1041.46 → 1041.72] Yes.
[1042.18 → 1044.46] And a lot of those have like a keynote speaker.
[1045.06 → 1053.88] And I won't reveal who the keynote speaker was at this one, but the topic was technology and automation and AI type stuff.
[1053.88 → 1057.76] And the keynote speaker did a really amazing job.
[1058.06 → 1068.44] Like, you know, keynote speakers who do that so often just really know how to bring a large crowd with them on a story arc and kind of tie things together.
[1068.66 → 1069.84] So he did a great job.
[1070.02 → 1079.12] But, you know, some of the things he talked about, I think, were meant to kind of provoke people in a thought process.
[1079.12 → 1088.68] And I think he kind of coined some of his own terms in order to kind of make people think about new things.
[1088.80 → 1097.76] One of those things that he talked about was what he called homology, which was basically the mashup of humans and technology.
[1098.46 → 1105.42] So it was a way to say he said, hey, there are humans and technology specifically talking about AI and automation.
[1105.42 → 1109.62] And I'm going to just sort of combine these into this really goofy word, homology.
[1110.20 → 1113.92] And he had what he called a homology scale.
[1114.28 → 1123.28] And it was basically like a data visualization going from like over on the left, there are tasks that only humans do.
[1123.84 → 1126.76] You know, computers, technology, they don't play a part.
[1126.98 → 1132.62] And it kind of went all the way over to the other side where humans are not involved.
[1132.62 → 1134.24] And there's kind of somewhere in between.
[1134.40 → 1147.72] And he was kind of trying to challenge people to think in their own business processes, if you were sort of over on the left-hand side too far, you're likely not leveraging AI and automation in the way that you should.
[1148.14 → 1155.72] Regardless of what industry in, you're not sort of leveraging the technology that's available in the marketplace to its full extent.
[1155.72 → 1159.56] And the example that he gave, I thought was a perfect one.
[1159.70 → 1168.86] And so the example he gave was taking care of weeds in a field of like an agriculture field in the farming context.
[1169.48 → 1174.14] On the left-hand side, at a certain point, you had humans doing that completely, right?
[1174.18 → 1178.98] Like you just pay a bunch of people, they'd have a bag or something and go into the field.
[1179.10 → 1182.42] They pick the weeds, put them in the bag and, you know, move along.
[1182.42 → 1188.42] And then at a certain point, you know, you had like weed aside, is that the right word?
[1188.70 → 1189.16] Weed killer?
[1189.46 → 1193.76] We're talking about agricultural weed, by the way, just so for people, just to be very clear.
[1193.92 → 1195.98] Well, I mean, you could be growing weed.
[1196.12 → 1198.68] Oh, well, I guess that didn't clarify it at all.
[1198.88 → 1201.08] So it's not mutually exclusive, I guess.
[1201.20 → 1201.72] There you go.
[1202.12 → 1204.54] But at a certain point, you had weed killer, right?
[1204.64 → 1210.70] And people would walk through the fields and apply the weed killer to weeds.
[1210.70 → 1216.28] That also sort of brings in an element of technology or chemistry to that, right?
[1216.68 → 1221.30] And then at a certain point, they said, well, that takes a long time to apply with humans.
[1221.30 → 1225.10] So I'm going to drive this truck through my field, right?
[1225.18 → 1229.34] And just dump this weed killer, you know, all in the field, right?
[1229.36 → 1233.38] Which is maybe effective, maybe pretty terrible for the environment.
[1233.64 → 1233.86] Yeah.
[1233.86 → 1237.76] But it's faster than, you know, humans doing it.
[1238.08 → 1244.04] And now you sort of move to later or more recently, where this actually implements on
[1244.04 → 1251.32] farm equipment that will drive through, and it will use computer vision to see weeds, distinguish
[1251.32 → 1254.32] them from other plants and spray them specifically.
[1254.32 → 1256.72] So you save a lot of money on weed killer.
[1256.98 → 1260.16] You're better for the environment, everything like that.
[1260.16 → 1264.84] And then he showed a recent example where, which I hadn't seen before, but apparently
[1264.84 → 1271.44] there are like companies like John Deere and others that are working on autonomous machines
[1271.44 → 1271.96] like this.
[1271.96 → 1276.76] Cause, cause those that drive through and spray selectively still have a driver in
[1276.76 → 1277.04] them.
[1277.04 → 1277.42] Right.
[1277.52 → 1280.86] But they're, you know, working on ones that are totally autonomous.
[1280.86 → 1283.10] So it's not how he phrased it was.
[1283.16 → 1287.72] It's not totally, even that is not taking the human out because they still have to come back
[1287.72 → 1289.84] and get charged or refuelled.
[1289.84 → 1290.16] Right.
[1290.24 → 1292.94] And like turned on and put out into the field.
[1292.94 → 1298.18] So a human is still involved in some way, but it's much more towards that other side
[1298.18 → 1300.18] of the, of the scale.
[1300.18 → 1303.90] The weed spraying via CNN is actually several years old.
[1303.90 → 1308.56] You know, at this point, I remember, I remember in talks three, four years ago that I was giving,
[1308.80 → 1310.44] we were, I was using that as an example.
[1310.98 → 1315.50] The autonomy, I agree is more recent, but it only makes sense to go do that.
[1315.50 → 1320.16] And I think we're going to see that across in, in your homology, you know, context.
[1320.16 → 1324.80] I mean, thousands and thousands of use cases it's, we already are.
[1325.24 → 1325.36] Yeah.
[1325.50 → 1325.80] Yeah.
[1325.92 → 1331.54] I kind of like the line of thought that he gave because it brought out a few things.
[1331.66 → 1335.30] One was if you're not automating anything, you probably should be.
[1335.58 → 1335.64] Yeah.
[1335.66 → 1341.70] Second is sort of doing a brute force application of technology can be harmful, right?
[1341.80 → 1344.28] There is that element in that story, right?
[1344.28 → 1349.40] But that's sort of worked through over, over time, at least in that example.
[1350.26 → 1353.10] But yeah, it's, it's an interesting line of thought.
[1353.22 → 1357.30] I think it prompts a lot of, a lot of thought, which is probably why it was good for that,
[1357.40 → 1357.96] that keynote.
[1358.20 → 1362.92] It brings up though, this element of, is AI taking all of these jobs?
[1363.08 → 1368.58] It's another element of what it, what it brings up, which I know that we've, we've chatted about
[1368.58 → 1371.80] before in various contexts on this podcast.
[1371.80 → 1377.08] Which of course it is because we're evolving, and we're evolving at a fast, and when I say
[1377.08 → 1381.94] we, I mean, not just humans, but this homology concept that you're talking about because the
[1381.94 → 1384.82] technology is us, and we are the technology.
[1385.06 → 1389.36] There is a and you know, I don't mean in the, in the sense of being a cyborg, but these
[1389.36 → 1392.68] are, you know, these, this is the fire that we invented.
[1392.68 → 1394.04] This is the wheel we invented.
[1394.76 → 1399.08] This is how the modern world is working and how we're doing it.
[1399.22 → 1407.12] But as we are racing up the curve of new tool creation, ever more sophisticated, we have
[1407.12 → 1410.84] this trailing concern about how it's impacting us.
[1411.10 → 1416.22] And, you know, we've talked a great deal about AI ethics and, and such along the way, but that
[1416.22 → 1422.02] is certainly a trailing concern because we, we go do things, and we're a little bit like
[1422.02 → 1425.82] a child, you know, running around learning something new and not really understanding
[1425.82 → 1428.32] that that's a sharp knife that you're holding there.
[1428.32 → 1432.52] And as they wave it around, it's something that we're trying to figure out as we go.
[1432.74 → 1434.88] I don't think that's going to stop anytime soon.
[1435.06 → 1442.20] I think we barely even have a handle on the fact that as we are constantly finding these
[1442.20 → 1445.56] new applications, we're going to be making mistakes all over the place.
[1445.88 → 1447.12] And I think you'll see that.
[1447.26 → 1450.22] I mean, we've seen an unending series of stories.
[1450.22 → 1457.08] If you think about it over the last 10 years about data and AI applications going awry,
[1457.26 → 1459.02] but they continue to happen.
[1459.18 → 1461.82] And I don't see any end to that as we do that.
[1461.82 → 1467.20] And I think that's just part of our very, very fast evolution as we go forward.
[1467.68 → 1467.76] Yeah.
[1467.96 → 1474.24] So how do you and your, the conversations that you have with people and this idea of,
[1474.24 → 1481.66] you know, AI taking jobs and sort of the benefits and downsides of automation, do you find that
[1481.66 → 1486.52] that comes up in your conversations with non-practitioner people?
[1486.52 → 1491.86] Like maybe the people that you do like wildlife volunteering with, does that ever come up?
[1492.24 → 1492.58] It does.
[1492.58 → 1498.38] It comes up in just about every aspect of life because this is now touching everybody and
[1498.38 → 1503.06] it affects almost all the jobs out there at some point or at some level.
[1503.22 → 1506.04] It may only be as a there may be some tooling.
[1506.28 → 1508.64] There may be data about those jobs.
[1508.76 → 1512.58] It may not be the primary job thing, but, but yeah, I'm seeing that a lot.
[1512.58 → 1516.40] There's a dissonance between humans and the tools that we're creating right now.
[1516.40 → 1522.12] And that we have biological brains that have always evolved, but evolved at a much slower
[1522.12 → 1524.44] rate than, than over the last few thousand years.
[1524.44 → 1531.14] And particularly the last few centuries and particularly the last few decades and up to
[1531.14 → 1532.04] where we're at now.
[1532.04 → 1534.38] And it doesn't show signs of slowing down.
[1534.38 → 1539.48] So we're not used to this much change this fast, and yet we are doing it.
[1539.48 → 1544.28] And so, yes, it's changing what it means to have a life.
[1544.52 → 1547.18] I have a as you know, a nine-year-old daughter at this point.
[1547.82 → 1551.60] As we've had these episodes, I've said six-year-old, seven-year-old, all that stuff.
[1551.92 → 1557.50] Nine-year-old at this point, I am struggling as a parent to try to figure out how to steer
[1557.50 → 1561.60] her so that long after I'm gone, she has a good productive life.
[1561.66 → 1566.64] And I think it is a fairly unique challenge given the steepness of the curve of change right
[1566.64 → 1568.94] now compared to any time in history.
[1568.94 → 1576.00] She's going to have to find a way to add value to the world enough to earn a living and do
[1576.00 → 1582.12] that cooperatively with all the technology things around her that once upon a time, my
[1582.12 → 1583.70] dad might've done that, but no more.
[1583.70 → 1584.30] Yeah.
[1584.52 → 1592.28] It's also just interesting in the sort of aspect of knowledge discovery and all that, like used
[1592.28 → 1593.82] to be the problem.
[1593.82 → 1601.54] Like if I think of even my parents' generation, my mom growing up in very small town in Oklahoma,
[1602.10 → 1606.48] Miami, Oklahoma, spelled Miami, but clearly Miami, Oklahoma.
[1607.02 → 1612.98] You know if you think about what information was available there, you know, there's no internet.
[1613.12 → 1617.02] So there was information available at the library, right?
[1617.02 → 1623.26] The access pattern to that information was, you know, looking up various subjects, finding
[1623.26 → 1627.50] the book, trying to parse through what information was there.
[1627.66 → 1634.04] So now even that pattern is really disrupted because so much is available to us.
[1634.08 → 1639.78] The problem is not like, I can't find information on this subject, but I find way too much information
[1639.78 → 1645.72] on this subject and I can't either, I can't verify what I need to verify, or I can't sort
[1645.72 → 1652.56] of distill down the pieces of information that I need to distill down, which I mean, that personally
[1652.56 → 1658.06] for me, in terms of like, it's exciting that all that information is available, but it's also
[1658.06 → 1664.62] exciting that sort of AI techniques or machine learning techniques are starting to be applied
[1664.62 → 1671.42] in that realm as well in terms of helping us find relevant things and connect the dots.
[1671.76 → 1676.16] Of course, there's a danger in that as well in terms of bias and what's presented to us.
[1676.26 → 1681.38] But I think in its best form, it can be applied with, you know, really great benefit.
[1681.86 → 1688.22] At risk of acting a little bit like father time on this, I'm going to leverage my old age
[1688.22 → 1689.78] at 51 currently.
[1689.92 → 1692.02] I looked up things in a library too, Chris.
[1692.02 → 1696.78] I'm going to go there for one second, just for some context.
[1697.10 → 1702.10] There were no cell phones at all until I was 20 years old, around 20, give or take.
[1702.88 → 1707.84] And I spent a lot of time as a kid at the public library, hoping that that little tiny local
[1707.84 → 1713.20] library with its world book encyclopedia, you know, that was my way of getting to the world.
[1713.34 → 1720.12] And the reason I'm saying this isn't just to emphasize my geriatric state, but to point out
[1720.12 → 1726.62] that the world, that's 30 years ago, the world has changed enormously in that time.
[1726.70 → 1729.56] And we tend to lose sight of that very easily.
[1730.08 → 1735.62] There has been more change in the last 30 years than for centuries before that.
[1735.70 → 1739.92] And then if you add the last couple of millennia, it's for tens of millennia before that.
[1740.16 → 1743.26] It's accelerating so much that we are in a unique state.
[1743.26 → 1747.96] If you go forward in time after you and I are gone, they're going to look back on this as
[1747.96 → 1748.84] pioneering days.
[1749.20 → 1754.72] We are the people sitting out across the American prairie with a little backpack and horses.
[1754.96 → 1756.44] It's just in this case, it's-
[1756.44 → 1758.60] With only a single GPU in my computer.
[1758.60 → 1761.56] With only a single GPU to do your calculations.
[1761.88 → 1762.36] Exactly.
[1762.90 → 1768.10] But that's where we're at right now as the world is changing dramatically, more dramatically
[1768.10 → 1768.92] than it ever has.
[1768.92 → 1774.92] And so I won't belabour this any longer, but it's worth once in a while remembering just
[1774.92 → 1777.42] how far we've come in just such a short amount of time.
[1791.10 → 1796.60] I'm Karl AAU, host of Ship It, a show with weekly episodes about getting your best ideas
[1796.60 → 1798.60] into the world and seeing what happens.
[1798.92 → 1803.98] We talk about code, ops, infrastructure, and the people that make it happen like charity
[1803.98 → 1805.06] majors from Honeycomb.
[1805.42 → 1808.34] We act like great engineers make great teams.
[1808.54 → 1810.48] It's exactly the opposite, in fact.
[1810.48 → 1813.62] It is great teams that make great engineers.
[1814.02 → 1817.52] And they finally win the founders of continuous delivery.
[1817.92 → 1820.68] Start off assuming that we're wrong rather than assuming that we're right.
[1820.92 → 1821.92] Test our ideas.
[1822.06 → 1823.54] Try and falsify our ideas.
[1823.70 → 1825.68] Those are better ways of doing work.
[1825.74 → 1827.98] And it doesn't really matter what work it is that you're doing.
[1827.98 → 1829.82] That stuff just works better.
[1830.04 → 1836.22] We even experiment on our own open source podcasting platform so that you can see how we implement
[1836.22 → 1841.38] specific tools and services within changelog.com, what works and what fails.
[1841.38 → 1845.62] It's like there's a brand-new hammer, and we grab hold of it and everyone gathers around.
[1845.72 → 1849.52] We put our hand out, and we strike it right on our thumb.
[1849.80 → 1852.60] And then everybody knows that hammer really hurts.
[1852.76 → 1855.22] When you strike it on your thumb, I'm glad those guys did it.
[1855.30 → 1856.66] I've learned something instead.
[1856.82 → 1856.92] Yeah.
[1857.10 → 1861.68] I think that's a very interesting perspective, but I don't see it that way.
[1861.84 → 1862.08] Okay.
[1862.18 → 1865.28] It's an amazing analogy, but I'm not sure if that applies here.
[1865.28 → 1867.94] Listen to an episode that seems interesting or helpful.
[1868.12 → 1869.74] And if you like it, subscribe today.
[1869.92 → 1871.00] We'd love to have you with us.
[1871.00 → 1893.16] Okay, Chris.
[1893.16 → 1898.74] Well, we probably should mention a couple of things that have run across our or have crossed
[1898.74 → 1900.72] our paths in the news recently.
[1901.04 → 1901.46] Current affairs.
[1901.60 → 1903.52] Current affairs in the AI world.
[1903.92 → 1908.26] One of the ones that I wanted to mention and also make people aware of more so because
[1908.26 → 1918.38] it is an ongoing project is this project that it's being run as a highly distributed collaborative
[1918.38 → 1922.88] research effort called the Big Science Research Workshop.
[1923.58 → 1927.36] Now, the Big Science Research Workshop, I think was inspired.
[1927.68 → 1932.12] And first, we'd love to have some people from there on the show at some point, but I didn't
[1932.12 → 1933.54] want to make people aware of it.
[1933.54 → 1939.56] So 600 researchers from 50 countries and more than 250 institutions.
[1940.32 → 1949.18] And what they're doing is they're getting together in sort of massive science collaboration
[1949.18 → 1956.68] project in the same vein as, you know, some people from my world originally in physics might
[1956.68 → 1960.54] be familiar with the CERN project or something like that where...
[1960.54 → 1961.16] Absolutely.
[1961.16 → 1967.48] There are a bunch of physics researchers that got together because what they realized is
[1967.48 → 1974.90] in high energy physics, the scale of the experiment that we need to do is larger than any experiment
[1974.90 → 1978.16] that any of our institutions can do in and of itself.
[1978.82 → 1984.44] And so now we need to have a massive global collaboration in order to create this new high
[1984.44 → 1989.70] energy physics accelerator and learn about the fundamental, you know, things of our universe.
[1989.70 → 1998.18] Well, in the same vein, this kind of Big Science Workshop is a large workshop or research project
[1998.18 → 2001.88] focused on large multilingual models and data sets.
[2002.34 → 2008.80] So as we've talked about over the past, however long, you know, NLP has been advancing rapidly.
[2009.50 → 2013.92] And one of the trends are these big multilingual language models.
[2013.92 → 2020.58] And typically at this point, those are so big that you need huge infrastructure to run them.
[2020.74 → 2030.08] You need sort of a huge data governance and curation sort of system and method to get all the data together,
[2030.08 → 2035.76] to manage it, to distribute it across your trainings and manage those trainings.
[2035.76 → 2038.48] And so that's really the goal of this project.
[2038.48 → 2045.04] And the reason why I bring it up now is that they released one of their first models recently called T0.
[2045.68 → 2053.70] And a lot of people are kind of talking about that because it outperforms in many ways, not in all ways,
[2053.78 → 2063.36] but in some ways it outperforms GPT-3, but it's also 16 times smaller than GPT-3, which is a huge model, of course.
[2063.36 → 2065.66] So fascinating.
[2065.78 → 2068.08] There's a couple other interesting things about it that I want to mention,
[2068.28 → 2076.20] but any initial reactions to that kind of, I guess, the strategy that they're employing to make this happen?
[2076.42 → 2079.98] I think that's a natural evolution of, you know, what we've been talking about.
[2080.06 → 2083.48] We were in those pioneering days from what we were saying a few minutes ago.
[2083.72 → 2089.20] And there's a point where to get progress, you've got to scale, and you've got to try new techniques
[2089.20 → 2091.42] and it can't be every little pioneer on their own.
[2091.42 → 2094.08] So I'm delighted to hear about this.
[2094.50 → 2100.40] And I want to learn a little bit more about what T0 can do.
[2100.50 → 2101.48] I don't know enough about it.
[2101.60 → 2102.84] What have you learned about it so far?
[2102.98 → 2107.34] Yeah, well, I wasn't part of the group that did this,
[2107.46 → 2114.00] although I've attended a couple of related things in one effort to kind of get some of the data together.
[2114.18 → 2117.50] They're sort of hosting these different workshops to help get data together.
[2117.50 → 2125.24] At least in my understanding, some sort of, or maybe the most interesting thing about it is that GPT-3,
[2125.84 → 2135.48] so an example of large language models like GPT-3, for the most part have been trained on sort of proxy tasks like masking,
[2135.74 → 2143.84] which means like I'm going to take some words out of various places and see if I can sort of figure out how to slot them back in into text.
[2143.84 → 2152.92] And that has been used as a proxy task in order to kind of help learn these really useful language representations.
[2152.92 → 2160.08] The strategy that they took with T0 had to do with prompts, which is quite interesting.
[2160.38 → 2166.92] So they took a bunch of different data sets that had to do with a bunch of different NLP tasks,
[2167.06 → 2174.14] like paraphrasing or summarizing, question answering, named entity recognition, natural language inference.
[2174.14 → 2177.34] These are all different types of tasks that people do with language.
[2177.96 → 2183.30] And they reframed all the labelled examples as prompts to the model.
[2183.46 → 2188.60] And what I mean by that is a prompt means like, here are a couple of examples that I have pulled up.
[2189.00 → 2192.12] For question answering, it could be something like,
[2192.28 → 2199.42] I know the answer to what team did the Panthers defeat is in blah, blah, blah, blah, blah.
[2199.96 → 2201.32] Can you tell me what it is?
[2201.32 → 2209.98] So it's literally just like a prompt like you'd give to another person, but it's flexible to other kinds of tasks.
[2210.26 → 2214.64] Like suppose the banker contacted the professors and the athlete.
[2214.88 → 2218.62] Can we infer that the banker contacted the professors?
[2219.18 → 2224.18] So that's more of a natural language inference thing, which has to do with logical agreement.
[2224.38 → 2226.34] You could reframe like sentiment.
[2226.68 → 2228.22] You could reframe summarization.
[2228.22 → 2232.08] Summarization would be like, you know, blah, blah, blah, blah, blah.
[2232.44 → 2235.18] How would you rephrase that in fewer words?
[2235.62 → 2240.84] All of these statements are just prompts paired with the corresponding output.
[2241.44 → 2247.16] And that I think is one thing that makes this kind of really stand out versus other models that have been trained.
[2247.76 → 2252.34] And for our listeners, I'm going to embarrass you and say Daniel really knows his NLP very well.
[2252.42 → 2253.26] He's quite the expert.
[2253.26 → 2256.98] And I know you won't say that about yourself, but I've known you long enough to know that's true.
[2256.98 → 2262.62] What do you see as the advantage of that particular strategy relative to previous ones?
[2263.00 → 2266.68] What is the value that they are managing through that approach?
[2267.36 → 2267.48] Yeah.
[2267.48 → 2273.08] So I think you have to think about how they're optimizing this model to be used.
[2273.52 → 2283.70] I think that they have recognized very significantly that this is the sort of zero shot thing that people want to do with modern language models.
[2283.70 → 2290.42] They want to give it their own unique prompt and have it immediately sort of know what to do.
[2290.42 → 2290.78] Okay.
[2291.12 → 2303.02] And so an example of this would be recently we needed to create a data set in our own work that showed some like contradictions in text.
[2303.02 → 2310.04] But we had a bunch of text, and we needed to sort of transform some of that text to where it contradicted itself.
[2310.04 → 2321.18] And so what we did was we created prompts like this and fed it in that case, we fed it to GPT-3 because you can do a similar type of interaction there where we kind of gave it a couple.
[2321.38 → 2323.24] In that case, it was sort of few shot.
[2323.34 → 2325.98] We gave it a couple examples of the prompts that we wanted.
[2325.98 → 2330.32] Like, you know, if this is this, then this is not this sort of thing.
[2330.32 → 2334.12] And it learned how to produce this sort of samples for us.
[2334.26 → 2342.68] This is the sort of thing I think this model is geared toward where people can come up with their own unique custom flexible prompts.
[2342.84 → 2348.94] And this should generalize quite well across a whole variety of tasks that people come up with.
[2348.94 → 2360.64] And so I think the advantage is that they're really focusing from the start in the training data around this sort of zero shot usage of the model.
[2361.06 → 2365.60] Just to ask a very basic question, this is yet another transformer approach, right?
[2365.60 → 2381.56] Yeah, so I believe that the model architecture that they base this on was similar to that of T5, which was a text to text model that's transformer based.
[2381.74 → 2389.92] So it's an encoder decoder sort of language model that I believe was from Google research not too long ago.
[2389.92 → 2397.02] Correct me if I'm wrong listeners, and I'm getting the wrong information, but I believe it came out from Google and that's been around for some time.
[2397.30 → 2398.20] So that's why they called it.
[2398.32 → 2401.78] I think T0 was partially it's the first model that they came out with.
[2401.78 → 2407.36] So zero, and it's kind of inspired by T5, this transformer based encoder decoder.
[2407.78 → 2411.50] Let me ask you a question while we're on this line of conversation.
[2412.08 → 2419.38] In recent years, we've really seen, you know, transformers came out and, you know, have just completely revolutionized the NLP space.
[2419.38 → 2424.84] In your view, just summarize, would you say that's really the only thing that matters right now?
[2424.90 → 2435.42] Because that's what we've been talking about the last couple of years every time we hit is, is there anything outside that kind of transformer approach that you've seen that is still valid?
[2435.42 → 2444.82] Have we eclipsed some of the older model approaches at this point or is there still any diversity there in terms of completely different mechanisms?
[2445.86 → 2447.68] Yeah, it's a good question.
[2447.68 → 2455.14] I think there's a lot of people doing sort of interesting things neural network architecture wise.
[2455.42 → 2473.64] I know in the natural language type of space, in particular around speech, I've seen some of the recent sort of streaming and space efficient speech models utilizing various new kinds of convolutional architectures.
[2473.64 → 2480.92] And so I think that's still, you know, like we kind of talked about with the weed spraying thing in the fields.
[2480.92 → 2483.64] That's what was used at that time quite some time ago.
[2483.68 → 2488.04] And it's still finding new, slightly different applications.
[2488.04 → 2498.94] But then there's also other new things that people are exploring to either combine multiple kinds of data, multiple modes of data, you know, video, audio, text.
[2498.94 → 2509.10] There are things that people are doing with natively graph structured data in graph neural networks, which I think is pretty fascinating stuff.
[2509.10 → 2515.38] So I think there's a variety of things that I wouldn't, I wouldn't phrase it as transformers is all that matters.
[2515.38 → 2521.04] But I think transformers have been, you know, no pun intended transformational.
[2522.02 → 2522.58] Transformational.
[2522.82 → 2530.42] That's also I mean, it's impacting video and computer vision and that sort of thing, too, because it's now being applied and in those spaces.
[2530.42 → 2532.54] So it's definitely been a big deal.
[2532.92 → 2533.76] Sounds interesting.
[2533.76 → 2536.90] Well, that was fascinating conversation there.
[2537.20 → 2540.04] I'm glad to have prompted it.
[2541.02 → 2545.68] My puns are getting worse or my jokes are getting worse as the episodes going along.
[2546.18 → 2547.78] Well, we're almost at an end.
[2547.86 → 2552.98] I was going to say, we'll get on the hook of going into some of those new approaches.
[2553.12 → 2554.52] The multimodal sounds fascinating.
[2554.66 → 2557.62] So we'll have to have an upcoming episode to dive into that.
[2557.84 → 2558.66] Yeah, for sure.
[2558.66 → 2565.72] You know, in each of those these episodes, we like to provide some learning resources for people.
[2565.98 → 2567.90] I think that you found a couple.
[2568.10 → 2573.62] It seems like both of us have been seeing quite a few things recently from IEEE spectrum.
[2573.62 → 2575.10] So great, great work.
[2575.16 → 2580.54] If is any of those working on those articles are out there, it seems like you've been doing good recently.
[2580.54 → 2586.48] But this how deep learning works inside the neural networks that power today's AI.
[2586.48 → 2589.00] I appreciate you forwarding this along to me.
[2589.12 → 2591.06] So what caught your attention about this?
[2591.44 → 2597.14] Just it was another take, you know, for a long time, we had seen kind of introductory articles out there.
[2597.14 → 2601.76] But as over the last few years, as things have progressed, we haven't seen as many of those lately.
[2602.04 → 2602.94] And so it was kind of nice.
[2603.00 → 2603.78] This was a fresh one.
[2603.88 → 2604.68] This was a new one.
[2605.00 → 2606.56] And it still just hits the basics.
[2606.80 → 2611.76] But there are people coming into our field every day right now that are just learning the basics.
[2611.92 → 2618.30] And I like the idea of throwing out one that takes another take at the basics and tries to communicate it well.
[2618.30 → 2623.92] It was as simple as that is keeping it fresh with the new material for people are just coming into the field.
[2624.22 → 2629.66] And then I saw another one, which is five deep learning activation functions you need to know.
[2630.12 → 2641.50] I remember back when I was learning this, understanding what the activation functions are, not just mathematically, but then knowing how to use them and where to use them is one of those things that sometimes catches people.
[2641.58 → 2643.58] It caught me a little bit when I was trying to learn it.
[2643.58 → 2650.32] And so the article basically kind of walks you through a quick summary of each one and talks about where you could use them.
[2650.46 → 2658.82] And I thought that was also as an introductory article would be a perfect thing for people to get to because it knocks over one of those hurdles quickly.
[2659.02 → 2662.94] And so I just wanted to throw out those for the people that are just coming into the field.
[2663.28 → 2663.68] Welcome.
[2664.02 → 2666.02] And there's lots of good material out there.
[2666.04 → 2667.54] And some of it remains brand new.
[2667.54 → 2669.26] Yeah, I would echo that.
[2669.26 → 2677.46] It's worth getting into the weeds a little bit if you're getting into this field and understanding things like activation functions.
[2677.82 → 2680.18] As time goes on, the tooling gets easier and easier.
[2680.32 → 2683.14] So you can just sort of pick stuff off from the shelf and use it.
[2683.58 → 2688.32] But there is a real value, I think, in getting some intuition around these things.
[2688.48 → 2689.98] So great finds, Chris.
[2690.10 → 2692.30] I really enjoyed our conversation today.
[2692.70 → 2695.18] Appreciate your thoughts on all the subjects.
[2695.30 → 2695.78] I did too.
[2695.82 → 2696.50] It was a good one.
[2696.50 → 2702.44] We'll talk to you soon and look forward to new guests next week and carrying on the conversation.
[2703.00 → 2706.40] And have a very good, I know you're taking a little time off around Thanksgiving.
[2706.68 → 2707.62] So enjoy your vacation.
[2707.88 → 2709.38] Veggie turkey day for us.
[2709.54 → 2709.98] Absolutely.
[2710.56 → 2711.46] Talk to you soon, Daniel.
[2711.70 → 2712.36] Happy Thanksgiving.
[2712.58 → 2712.72] Bye.
[2712.88 → 2713.52] Happy Thanksgiving.
[2717.06 → 2718.18] That's our show.
[2718.38 → 2719.02] Thanks for listening.
[2719.54 → 2721.84] For more like this, check out our master feed.
[2721.84 → 2725.92] It is all Changelog podcasts in one easy to consume place.
[2726.26 → 2731.14] Let your podcast app snag everything we produce and then pick and choose which ones to listen to.
[2731.48 → 2737.50] Subscribe today at changelog.com slash master or just search for Changelog Master in your podcast app of choice.
[2737.78 → 2738.30] You'll find it.
[2738.82 → 2743.58] Special thanks to Break master Cylinder for providing our music and to our longtime sponsors,
[2743.94 → 2745.80] Vastly, Launch Darkly, and Linde.
[2746.32 → 2747.64] That's all for this week.
[2747.90 → 2749.12] We'll talk to you again next time.
[2749.12 → 2779.10] We'll talk to you again next time.
