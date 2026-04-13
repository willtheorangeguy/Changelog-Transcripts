[0.00 → 2.66] I do think team members should be playing to their strengths.
[2.94 → 4.94] Both Angelica and I are technical product managers.
[5.20 → 7.82] So hopefully we know a little bit about the technical side of things.
[7.96 → 12.50] But really, I do think the engineers should be owning the technical side and the engineering
[12.50 → 13.12] decisions.
[13.12 → 16.96] If we're rolling out something and there's some work that needs to be done, and it's very
[16.96 → 21.34] engineering heavy, then I fully put the responsibility on the team to let me know, like, we're going
[21.34 → 23.74] to have to do this, and then we're going to have to do that, and then we're going to do
[23.74 → 26.32] this, and then we'll be ready to launch.
[26.32 → 30.66] And we'll want to plan the launch in this way and do a gradual rollout, whatever the
[30.66 → 31.38] case might be.
[31.70 → 36.46] Because the team ultimately has the ownership for building a really high quality product
[36.46 → 38.28] or feature or what have you.
[38.56 → 41.92] The product manager should be doing the product work, helping make sure that we're launching
[41.92 → 47.46] well and that we've given appropriate communications to other teams or that we've scoped what we're
[47.46 → 49.74] going to do ahead of time to give the context.
[49.98 → 53.78] But there's definitely certain responsibilities that should be owned by different individuals.
[53.78 → 58.02] And what's really important is just to have good trust with each other.
[60.02 → 62.66] Big thanks to our partners, Linde, Vastly and Launch Darkly.
[62.88 → 63.60] We love Linde.
[63.68 → 65.10] They keep it fast and simple.
[65.24 → 67.58] Check them out at linode.com slash changelog.
[67.82 → 69.88] Our bandwidth is provided by Vastly.
[70.24 → 73.78] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[74.06 → 75.78] Get a demo at LaunchDarkly.com.
[75.78 → 82.24] This episode is brought to you by our friends at Cockroach Labs, the makers of Cockroach DB,
[82.74 → 85.52] the most highly evolved database on the planet.
[85.96 → 90.60] With Cockroach DB, you can scale fast, survive anything and thrive everywhere.
[91.02 → 95.88] It's open source, Postgres wire compatible and Kubernetes friendly, which means you can
[95.88 → 97.18] launch and run it anywhere.
[97.62 → 101.42] For those who need more, you can build and scale fast with Cockroach Cloud, which is
[101.42 → 103.62] Cockroach DB hosted as a service.
[103.62 → 108.68] It's the simplest way to deploy Cockroach DB and is available instantly on AWS and Google
[108.68 → 109.04] Cloud.
[109.42 → 114.94] With Cockroach Cloud, a team of world-class Sees maintains and manages your database infrastructure
[114.94 → 117.62] so you can focus less on ops and more on code.
[118.00 → 122.00] Get started for free with a 30-day free trial or try their new forever free tier that's super
[122.00 → 122.48] generous.
[122.80 → 125.34] Head to CockroachLabs.com slash changelog to learn more.
[125.66 → 128.60] Again, CockroachLabs.com slash changelog.
[133.62 → 140.74] Let's do it.
[141.30 → 142.36] It's go time.
[143.08 → 147.80] Welcome to Go Time, your source for diverse discussions from around the Go community.
[147.80 → 151.92] We record live each and every Tuesday at 3 p.m.
[152.04 → 152.48] U.S.
[152.56 → 152.96] Eastern.
[153.22 → 158.26] Subscribe now at YouTube.com slash changelog so you're notified of when we go live.
[158.26 → 162.82] And don't forget to hop into the Gophers Slack and the GoTime.fm channel.
[162.96 → 164.24] That's where all the chatter happens.
[164.44 → 167.90] If this is your first time listening, subscribe now at GoTime.fm.
[168.06 → 169.50] Hey, let's get right into it, shall we?
[170.16 → 171.02] Here we go.
[174.62 → 178.28] Hello and welcome to Go Time.
[178.28 → 185.46] Today, we're going to be talking about whether software engineers need product managers.
[186.14 → 191.76] We're going to be discussing this with our wonderful guest, Gail Sharma, who is a senior
[191.76 → 195.18] technical product manager at the New York Times, leading the Identity Group.
[195.86 → 201.50] And I am very happy to inform you, I am joined by our wonderful panellist, Chris.
[202.14 → 202.96] So hello, Chris.
[203.16 → 203.44] Hello.
[203.78 → 206.08] Happy that you joined for us for this conversation.
[206.64 → 207.40] Happy to be here.
[207.40 → 208.40] How are you doing, Angelica?
[208.60 → 209.38] I am good.
[209.50 → 214.80] I am very excited to have this chat, given the fact that I, well, as most of you know
[214.80 → 219.02] who listen to the podcast, I'm a product manager, but I love engineers.
[219.40 → 221.40] I like to think of myself as a secret gopher.
[221.86 → 224.90] So I think this is going to be a good conversation for us to have.
[225.52 → 231.34] So first, I'm going to kick it over to you, Gail, to explain to our lovely listeners
[231.34 → 234.10] who may not be aware, what is a product manager?
[234.88 → 235.14] Yeah.
[235.34 → 236.10] Thanks, Angelica.
[236.10 → 243.94] So a product manager, and the definition I'd like to give is somebody who identifies the
[243.94 → 250.46] customer need and blends that with the larger business objectives to deliver a product that
[250.46 → 252.40] will be successful in the market.
[252.78 → 257.60] It'll help the company earn revenue, and also they'll fulfill a need for our customers.
[258.36 → 263.40] And so the product manager helps articulate a vision and rally a team towards that vision
[263.40 → 264.76] and make it a reality.
[265.06 → 267.44] So I think it's a very exciting role to have.
[268.10 → 271.24] And how is it different from a project manager?
[271.44 → 275.66] Because I don't know whether it's been your experience, but in my experience, when trying
[275.66 → 281.30] to talk to anyone about what I do, they default to, oh, okay, you're a project manager.
[281.76 → 282.32] Yeah, yeah.
[282.32 → 286.64] So a project manager oftentimes can work very closely with a product manager.
[287.22 → 294.10] A project manager will be a little bit more focused on planning or organizing and helping
[294.10 → 296.62] direct the completion of a specific project.
[296.62 → 301.26] So they'll help make sure that a project is on time or on budget and within scope.
[301.62 → 306.04] They'll really kind of like try to help track down open questions and make sure everybody's
[306.04 → 307.86] aligned and knows what's happening next.
[307.86 → 312.64] And so they're really, really focused on a project that's in progress and getting that
[312.64 → 313.10] executed.
[313.70 → 316.60] And then a product manager might be doing a couple of different things.
[316.76 → 322.20] Like a product manager could be conducting discovery with customers, like going out into the market,
[322.54 → 324.74] observing how folks are using the product.
[325.22 → 329.88] Maybe they're doing industry research and trying to figure out what a new product should be.
[330.42 → 335.56] Maybe they're doing some research and getting feedback on existing product and what could be improved.
[335.56 → 340.90] Maybe they're doing some sort of strategy work and trying to think about how the company should
[340.90 → 343.12] be evolving and what does that mean for their product.
[343.64 → 348.56] Maybe they're helping the engineering team think about tech debt and how we should be tackling
[348.56 → 348.94] that.
[349.36 → 353.68] It could be a wide variety of things, and it's not always about executing a project that it's
[353.68 → 354.02] in flight.
[354.32 → 358.74] So tell me, how did you end up as a product manager?
[359.42 → 359.70] Yeah.
[360.26 → 364.66] Well, probably like many other product managers, it was by accident.
[364.66 → 370.64] I had no idea that there was such a thing as a career for product managers.
[370.82 → 372.04] I've never heard of this.
[372.64 → 378.94] So earlier on in my life, when I was in college, I was really interested in public health and
[378.94 → 382.86] that led me following college to work at a community development bank.
[383.00 → 387.08] So I was doing a fellowship where I was learning more about the community.
[387.44 → 389.18] What did it mean to do impact investing?
[389.18 → 393.86] And how we could make loans to small businesses in Chicago.
[394.12 → 395.06] That's where I was located.
[395.06 → 401.04] And I had the chance to have a manager at the time during my fellowship who was giving me
[401.04 → 401.60] some feedback.
[402.24 → 407.82] And one day she said to me, Gail, I think you would be a great product manager and that
[407.82 → 408.86] you would really enjoy it.
[409.18 → 410.46] I had no idea what that was.
[410.80 → 414.08] So she taught me a little bit about what it was.
[414.08 → 418.08] And she explained how some of the work that I had been doing was very similar to a product
[418.08 → 422.14] manager because I had been helping create new products for the community development
[422.14 → 426.22] bank and working really closely with customers and solving customer problems.
[426.80 → 430.22] So she really kind of opened my eyes to this potential career.
[430.82 → 435.34] And then later on, as I was trying to think about what to do as a next step after the fellowship,
[435.86 → 440.06] I found some product associate positions and I decided to give it a go and apply.
[440.06 → 444.34] And it turns out I had a lot of good experience and that was it.
[444.88 → 448.14] I just kept going further and further into this career path.
[448.74 → 454.06] So yeah, just like somebody had heard about it and saw that I had like a lot of the skills
[454.06 → 458.30] or like interests that mapped on well to doing a good job in this role.
[458.66 → 460.54] And so they kind of like pushed me towards it.
[460.90 → 461.70] Yeah, for sure.
[462.04 → 467.66] And I think it's interesting how so many of the product managers that I've met have talked
[467.66 → 473.02] of this kind of falling into it, like they had no idea what it was, then someone spoke
[473.02 → 473.86] to them about it.
[473.94 → 476.52] And then they were like, Oh, actually, I'd be quite good at this.
[476.78 → 482.30] I love to hear from you, Chris, in terms of coming into the industry.
[482.30 → 487.12] I know we've talked about it before a little bit on the podcast, but you came in quite senior.
[487.44 → 492.36] So I really love to hear a little bit about your experience getting to know, you know,
[492.42 → 496.22] how to work with product managers efficiently, what your experience has been.
[496.22 → 503.24] And also maybe a little bit about the difference between the various product managers you've
[503.24 → 510.12] worked with, given that many of us have like completely different backgrounds, whereas I'm
[510.12 → 515.88] generalizing here, it seems that many software engineers know they want to do this very early.
[516.24 → 523.80] It's a very kind of direct path to a job, as opposed to this kind of falling into it that
[523.80 → 526.62] certainly has been my experience and Gail's experience.
[527.26 → 530.64] I mean, I think the last point, I mean, I kind of fell into software engineering, right?
[530.64 → 533.18] Like I don't have a CS degree or anything like that.
[533.58 → 539.24] But yeah, I mean, as coming into the industry as a pretty senior level person, I didn't actually
[539.24 → 545.44] work with a product manager until probably like two or three years into my career.
[545.74 → 549.86] There just like wasn't anybody that was kind of fulfilling that role in the places I was.
[549.86 → 553.74] My first experience with product managers were kind of like on the outskirts because I was
[553.74 → 555.32] like really working on internal stuff.
[555.44 → 560.12] So there wasn't a lot of like, you know, customer facing things I was doing.
[560.28 → 563.90] So there weren't a lot of like interactions I had with product managers.
[564.02 → 565.32] But you know, I like to hang out with them.
[565.40 → 566.00] They were cool people.
[566.54 → 571.18] I think the first time I actually like worked closely with a product manager, though, it
[571.18 → 573.06] wasn't too great of an experience.
[573.24 → 577.06] I think it was mostly, it seemed like they were a little too much on the project management
[577.06 → 577.56] side.
[577.72 → 581.98] It seemed like a lot of what they were doing was just very focused on like the day to
[581.98 → 586.08] day of what the engineers were doing and being like, oh, this is what I want you to do and
[586.08 → 590.28] not really like getting us the information that we really needed about like what it is we
[590.28 → 591.12] were supposed to be building.
[591.68 → 596.38] And I think that's been a lot of my experience with product managers in general.
[596.96 → 601.04] It's been not enough of like the perfect ones that kind of go out, and they're like,
[601.12 → 603.30] okay, here's all the information that you need.
[603.44 → 604.34] Here are the requirements.
[604.34 → 607.74] I've like thought through the things that we're going to try and build.
[607.82 → 608.66] Like, here's the scope.
[608.78 → 609.64] Here's what you need to go do.
[610.10 → 614.12] I've often found that I have to do a lot of that work and a lot of the heavy lifting
[614.12 → 614.58] myself.
[614.84 → 619.82] And then my team members who don't do that heavy lifting wind up just not building the
[619.82 → 621.30] right thing at the end of the day.
[621.30 → 625.58] And there's like features missing or something got completely miss scoped.
[625.82 → 632.52] So like my overall experience has been quite hit or miss as far as product managers are
[632.52 → 632.96] concerned.
[632.96 → 639.34] Yeah, that's interesting because I think when I first took some agile classes on how to be
[639.34 → 644.54] part of a team and play the product role on the team, the product owner role, some like
[644.54 → 647.76] the nitty-gritty details were around like, how do you write a ticket?
[648.04 → 650.44] How do you manage the backlog for the team?
[650.56 → 652.94] Like you're part of the team, and you're doing the backlog management.
[653.40 → 658.66] But I think definitely as you start to level up as a product person, you understand that really
[658.66 → 664.86] what you're bringing to the table for the benefit of the team is doing all of that really deep
[664.86 → 671.00] research of getting to know the space really well and developing those relationships with the
[671.00 → 671.44] customers.
[671.98 → 677.00] And even if it's an internal product, perhaps your customers are other teams internally and
[677.00 → 680.96] like asking the right questions and surface feedback from the teams.
[680.96 → 686.24] And once you have received that feedback, kind of packaging it in a way that's really nice
[686.24 → 689.36] to bring back to your team and be like, hey, here's what I'm hearing.
[689.70 → 690.96] Here's what's working really well.
[690.96 → 692.58] Or here's where we could improve.
[692.94 → 694.92] Here's where I see us going long term.
[695.12 → 697.32] And then like getting feedback also from the team.
[697.44 → 700.48] And like, I think it really should be a collaborative exercise.
[700.88 → 704.70] Once we're learning something to decide, okay, where do we take this learning?
[704.80 → 705.58] What's the next step?
[705.64 → 706.66] How do we keep improving?
[706.66 → 710.90] And I do think there's a little bit of an evolution that product people have to do, which is like
[710.90 → 715.90] first kind of get some of the basics down and then like start to level up more and more
[715.90 → 722.94] and learn the really key skills around doing the discovery work and the research and communicating
[722.94 → 728.60] well and like asking perfect questions that kind of get the nice meaty information out
[728.60 → 731.24] of folks and then bring that back to the team.
[731.48 → 731.82] Yeah, for sure.
[731.82 → 737.52] I mean, Gail, you talk about this collaboration between engineering and product and Chris,
[737.56 → 743.34] you've talked about the collaboration, perhaps not so successfully, but it's been a collaboration.
[744.00 → 746.74] I would love to hear from either of you.
[747.50 → 752.38] What do you think makes a successful partnership between product and engineering?
[753.56 → 756.04] Sure, I could take a first crack at it.
[756.04 → 761.70] I think when I reflect on partnerships with engineering that I really enjoyed one, it's
[761.70 → 766.92] been one where I can ask stupid questions like, well, tell me a little bit about the
[766.92 → 770.60] architecture of the app or like, why is it that we need to run this test?
[770.74 → 772.22] Why do we need to do this right now?
[772.56 → 776.90] And, you know, having that space where I can feel comfortable, and then I can be taught,
[777.10 → 778.36] you know, this is why it really matters.
[778.62 → 782.48] And then I can understand that, okay, this will make the quality of the product much better
[782.48 → 784.44] and we should be prioritizing this right now.
[784.98 → 789.86] Being able to have that conversation with my engineering partners is really helpful.
[790.18 → 794.82] And, you know, if somebody can explain something really well to me, that's valuable.
[795.46 → 797.02] I appreciate diagrams.
[797.22 → 797.90] Diagrams are great.
[798.98 → 803.42] Anyone who draws a diagram for me, typically, I don't really like to help me understand something.
[803.58 → 808.72] And then I'm likely to be able to take that information and then explain it to someone else.
[808.72 → 813.50] So that's valuable to the team if I can go to another team and explain like, hey, in this
[813.50 → 815.08] sprint, we need to be doing this and that.
[815.34 → 818.72] But following sprint, we'll be able to work on the deliverable that you need.
[819.28 → 823.30] So being able to learn from my engineering partners works really well for me.
[823.76 → 828.20] I really enjoy being, you know, truly feeling like I'm a part of the team.
[828.30 → 833.06] So I want to participate in retro and I want to hear the hard feedback on how I can improve
[833.06 → 836.28] as a product manager and make things even better for the team.
[836.28 → 841.04] Maybe I didn't deliver a product requirement that was clear enough, and it was blocking the
[841.04 → 841.38] team.
[841.54 → 843.96] I want to hear that, and I'm really open to it.
[844.02 → 848.00] So I enjoy when I have that relationship with my engineering partners.
[848.58 → 852.94] And then, you know, I think sometimes I really appreciate having a partnership where we can
[852.94 → 853.84] be creative together.
[854.10 → 858.40] So, you know, maybe I'm trying to solve something, and I'm not exactly sure what we could do,
[858.76 → 861.50] but maybe we can bounce some crazy ideas around together.
[861.50 → 866.56] And we might find something that may not be the best solution, but can get us to solve
[866.56 → 867.26] something quickly.
[867.72 → 871.76] And then we'll also talk about like, okay, yeah, that's fine for now, but here's the other
[871.76 → 873.18] solution we would prefer to do.
[873.70 → 878.94] And I like having these conversations and, you know, not being the only person that's
[879.76 → 882.66] throwing out crazy ideas and like hearing the pros and cons.
[883.20 → 887.50] So, yeah, I like a really collaborative relationship with my engineering partners.
[887.50 → 893.74] I think what comes to mind that for me, especially when you talked about like getting in a room,
[894.02 → 899.52] brainstorming with your engineers, do you need to have software engineering expertise
[899.52 → 901.32] to be a good product manager?
[901.66 → 906.06] I know we're going to talk a little bit about the difference between technical product manager
[906.06 → 910.30] and a product manager, but in general, maybe I'll turn this to Chris.
[910.68 → 915.28] Do you expect your product manager to have kind of technical skills?
[915.28 → 916.64] If so, to what level?
[916.80 → 920.52] I'd love to hear a little bit about kind of your experience there and your expectations
[920.52 → 922.50] from a product partner.
[923.64 → 923.84] Yeah.
[924.06 → 930.34] So I think in general, I found that there's not really a clear line between like where
[930.34 → 930.98] things happen.
[931.06 → 935.42] I think it's like this kind of dance you have to do between like the product team and the
[935.42 → 938.02] engineering team to figure out like where everybody is.
[938.02 → 943.56] So I do think there are some teams of engineers that are just like only care about like the
[943.56 → 948.14] low level technical stuff, like don't really have that, you know, that skill set and being
[948.14 → 952.62] able to like sums out like what types of things do we need to add to the product and figuring
[952.62 → 955.02] out all the different edge cases and things like that.
[955.42 → 958.26] So I think if there's like a team that's like that, then I think the product manager really
[958.26 → 962.58] does have to be like a technical person because they have to kind of descend to that
[962.58 → 964.00] level so they can communicate with them.
[964.00 → 967.74] And then if you have someone that's not technical, but with a team that's super technical, I think
[967.74 → 969.98] there are a lot of struggles that happen.
[970.24 → 974.56] And especially when communication, especially around like prioritizing things and backlogs
[974.56 → 975.62] and stuff like that.
[976.06 → 978.74] I am kind of on the other side of things when it comes to being an engineer.
[978.90 → 983.16] Like I'm very good at thinking about like edge cases and like what we need for like what
[983.16 → 984.52] we would want to have in a product.
[984.52 → 989.04] And like I'm capable of sitting down and talking to customers and talking to clients and whatever
[989.04 → 992.48] and kind of assessing what we need from there and extrapolating.
[992.48 → 997.26] So I think for me, I definitely prefer product managers who can focus less on the technical
[997.26 → 1000.12] stuff and more on those like higher level requirements.
[1000.66 → 1004.50] People that can like answer questions that I'm not capable of answering myself.
[1004.98 → 1008.04] And I kind of feel like that's how we should be building engineering organizations.
[1008.36 → 1013.30] I think it's not really that great to try and have someone that's not very close to the
[1013.30 → 1018.20] code and working with the code all the time, trying to make decisions about what we
[1018.20 → 1020.74] should do with the code or how we should prioritize things with the code.
[1020.74 → 1025.64] So I think it's like our engineers should kind of level up a bit more to the product people
[1025.64 → 1027.52] instead of the product people having to come down.
[1027.98 → 1030.38] So I also think if the product people have to come down, then it's like, well, who's
[1030.38 → 1033.78] going to do the other stuff the product people need to be doing?
[1034.38 → 1038.14] We can't just be like, oh, well, you just have all of this extra work to do now because
[1038.14 → 1042.66] you know, our engineers don't want to figure out how to like to assess product requirements
[1042.66 → 1046.74] and translate them into actual things that we can go out and build.
[1047.26 → 1050.04] But I think that also has implications on like who owns what.
[1050.26 → 1054.30] I think one of my, I guess, interesting opinions is I don't think product managers should own
[1054.30 → 1054.94] backlogs.
[1055.18 → 1059.34] I think in general, that's like the place of the team more than anything else.
[1059.40 → 1063.64] The team should own their backlog and should kind of prioritize it, and they should have
[1063.64 → 1064.84] input from the product manager.
[1064.84 → 1069.78] But I think giving that away to someone else takes away some of the autonomy of a team.
[1070.36 → 1073.98] This is especially true if like the product organization feels further away from the
[1073.98 → 1075.38] engineering organization as a whole.
[1075.88 → 1077.22] That is a very interesting opinion.
[1078.54 → 1083.46] Actually, like building off of that, I think I had a situation where I had to step away
[1083.46 → 1084.86] from the team for a little bit.
[1085.00 → 1089.78] So it was less involved and the team very much was operating without a product manager.
[1090.04 → 1094.46] And I think one of the things that worked really well for the team is having
[1094.46 → 1098.64] context, like the team knew what was the goals for the team, what was the vision, what we
[1098.64 → 1099.68] were trying to accomplish.
[1100.08 → 1104.90] And from then on, really, the engineers could be self-directed in determining, all right,
[1104.90 → 1109.68] we need to have these stories, this sprint, and it would really be ideal if we finished
[1109.68 → 1112.26] these milestones within this time frame.
[1112.68 → 1118.00] And I didn't really have to be, you know, like a hawk over the backlog and like moving things
[1118.00 → 1120.52] around or up and down to different sprints.
[1120.52 → 1125.92] On the other hand, I think the backlog is a good tool for a product manager when you're
[1125.92 → 1127.86] having conversations with other teams.
[1128.00 → 1132.62] Like that's where it's really helpful because you can kind of keep an eye on if there was
[1132.62 → 1136.84] a request from another team, you have an understanding of, all right, it's not going
[1136.84 → 1140.40] to go into this sprint because we'd have to drop something else, but it's likely to
[1140.40 → 1141.72] go into the next sprint.
[1141.86 → 1145.98] So I can reasonably say it'll be done around this time frame.
[1145.98 → 1148.96] And that helps build really strong partnerships with other teams.
[1148.96 → 1153.92] And then you can help kind of like move projects along if you ever have a gate from another
[1153.92 → 1154.20] team.
[1154.26 → 1157.96] It's like building that relationship and enabling teams to work really well together.
[1158.34 → 1163.16] That's really key to delivering features successfully, especially if it's like
[1163.16 → 1166.64] a really complex project that has dependencies on many teams.
[1167.12 → 1169.66] Aligning all the dependencies can get tricky.
[1169.66 → 1174.40] So I think for the product manager, that's where the backlog and kind of keeping an eye
[1174.40 → 1177.12] on where things go becomes a really useful tool.
[1177.64 → 1184.40] And I think too, part of the problem is like the tooling we have is pretty awful for most
[1184.40 → 1184.96] of this.
[1185.12 → 1190.90] Like I think any of the, you know, task slash issue managers, Jira, what have you, they don't
[1190.90 → 1194.12] really have enough of the utilities you need, especially for complex projects.
[1194.12 → 1195.90] That's something I've always found failing in the past.
[1195.90 → 1200.56] There is something that we're trying to do across multiple teams, trying to visualize
[1200.56 → 1205.72] and track that, especially at a like not fine-grained, someone will go do this individual
[1205.72 → 1206.44] unit of work.
[1206.62 → 1210.00] But in this, like, here's a thing that we need to do, and we want to track it.
[1210.18 → 1214.10] It's, you know, there's a lot of work that you have to do to actually put all of that
[1214.10 → 1217.74] together or to assemble that even within a system as powerful as Jira.
[1217.74 → 1224.50] And I think that also like not having a separate view of the tasks that need to get done, I
[1224.50 → 1228.44] think gravitates people toward just like piling everything into the backlog and being like,
[1228.54 → 1229.48] this is a source of truth.
[1229.68 → 1232.96] And then you have like different things that are supposed to be owned in there.
[1233.02 → 1234.50] And it's like not clear who owns what.
[1234.60 → 1239.50] And there's not a good way for, say, a less technical person to like be able to prioritize
[1239.50 → 1240.12] things in there.
[1240.18 → 1243.78] That's always been my problem with some, you know, product managers has been, you know,
[1243.78 → 1246.80] they kind of go into the backlog, and they start rearranging the things that they want
[1246.80 → 1249.26] and they just like shove down all the dependencies.
[1249.44 → 1250.92] And it's like, we can't do that.
[1250.96 → 1254.44] And it's like, arguably, our tooling should prevent that from being a problem.
[1254.44 → 1257.38] It should prevent you from putting things out of order.
[1257.56 → 1260.42] But that's really hard to do with the tooling that exists now.
[1260.58 → 1261.02] Yeah.
[1261.40 → 1266.34] Something you said earlier really spoke to me, which is I do think team members should be
[1266.34 → 1267.46] playing to their strengths.
[1268.22 → 1271.94] So I know Angelica mentioned both Angelica and I are technical product managers.
[1271.94 → 1274.96] So hopefully we know a little bit about the technical side of things.
[1275.14 → 1280.58] But really, I do think the engineer should be owning the technical side and the engineering
[1280.58 → 1281.20] decisions.
[1281.20 → 1284.72] If we're rolling out something and there's some work that needs to be done, and it's
[1284.72 → 1289.54] very engineering heavy, then I fully put the responsibility on the team to let me know
[1289.54 → 1291.88] like, you know, we're going to have to do this, and then we're going to have to do that
[1291.88 → 1295.28] and then we're going to do this, and then we'll be ready to launch.
[1295.62 → 1299.54] And, you know, we'll want to plan the launch in this way and do a gradual rollout,
[1299.62 → 1300.76] whatever the case might be.
[1300.76 → 1306.32] And, you know, because I think the team ultimately has the ownership for building a really high
[1306.32 → 1309.58] quality product or feature or what have you.
[1309.94 → 1314.00] So I think it's more on that the product manager should be doing the product work, helping make
[1314.00 → 1318.32] sure that we're launching well and that we've given appropriate communications to other teams
[1318.32 → 1323.08] or that we've scoped what we're going to do ahead of time to give the context.
[1323.58 → 1328.20] But there's definitely like certain responsibilities that should be owned by different individuals.
[1328.20 → 1332.38] And what's really important is just to have good trust with each other.
[1332.48 → 1338.50] Like if I know that you are working on engineering piece of it, then, you know, it's that's your
[1338.50 → 1339.24] responsibility.
[1339.34 → 1342.72] And my responsibility is to support from the product perspective.
[1343.22 → 1347.76] And so I guess to go back to the backlog management, definitely there's more like engineering heavy
[1347.76 → 1348.24] tickets.
[1348.24 → 1353.38] You know, my approach as a product person is always just to ask the team like, hey, you
[1353.38 → 1355.28] know, what's how high priority is this?
[1355.68 → 1357.22] Should I keep it towards the top?
[1357.90 → 1359.72] You know, when do you want to be working on it?
[1359.78 → 1361.26] What is it going to enable us to do?
[1361.26 → 1365.74] And, you know, just enough questions to be able to pull it into the sprint or not, depending
[1365.74 → 1366.70] on what the team says.
[1374.42 → 1377.22] This episode is brought to you by Source graph.
[1377.80 → 1382.18] Source graph is universal code search to let you move fast, even in big code bases.
[1382.70 → 1388.42] Here's CTO and co-founder, Bung Lu, explaining how Source graph helps you to get into that ideal
[1388.42 → 1389.44] state of flow and coding.
[1389.44 → 1394.64] The ideal state of software development is really being in that state of flow.
[1394.86 → 1399.70] It's that state where all the relevant context information that you need to build whatever
[1399.70 → 1404.48] feature or bug that you're focused on building or fixing at the moment, that's all readily
[1404.48 → 1404.96] available.
[1405.12 → 1408.48] Now, the question is, how do you get into that state where, you know, you don't know anything
[1408.48 → 1410.50] about the code necessarily that you're going to modify?
[1410.84 → 1413.16] That's where Source graph comes in.
[1413.38 → 1416.52] And so what you do with Source graph is you jump into Source graph.
[1416.52 → 1419.96] It provides a single portal into that universe of code.
[1420.26 → 1423.60] You search for the string literal, the pattern, whatever it is you're looking for.
[1423.70 → 1426.68] You dive right into the specific part of code that you want to understand.
[1427.10 → 1430.84] And then you have all these code navigation capabilities, jump to definition, find references
[1430.84 → 1435.98] that work across repository boundaries that work without having to clone the code to your
[1435.98 → 1439.90] local machine and set up and mess around with editor config and all that.
[1439.90 → 1443.84] Everything is just designed to be seamless and to aid in that task of, you know, code
[1443.84 → 1445.38] spelunking or source diving.
[1445.68 → 1449.32] And once you've acquired that understanding, then you can hop back in your editor, dive right
[1449.32 → 1453.56] back into that flow state of, hey, all the information I need is readily accessible.
[1453.78 → 1458.04] Let me just focus on writing the code that influenced the feature or fixes the bug that I'm working
[1458.04 → 1458.26] on.
[1458.56 → 1458.86] All right.
[1458.92 → 1460.74] Learn more at Sourcegraph.com.
[1460.86 → 1465.28] And also check out their bi-monthly virtual series called DevToolTime covering all things
[1465.28 → 1468.88] DevTools at Sourcegraph.com slash DevToolTime.
[1469.90 → 1487.60] How would you feel, Chris, about a product manager who was very technical, maybe was
[1487.60 → 1494.28] a previously a software engineer and did understand everything about the system, was able to review
[1494.28 → 1499.88] PRs, was able to really get down in the weeds and therefore could go through all things.
[1499.90 → 1503.74] The tickets to the backlog could even create all the technical tickets.
[1504.44 → 1508.58] And then perhaps it would come to you or the team and be like, okay, this is the technical
[1508.58 → 1509.52] approach we're taking.
[1509.82 → 1510.70] Here are the tickets.
[1510.88 → 1511.66] Please execute.
[1512.66 → 1518.90] That for me, I'm obviously being very kind of, I wouldn't do this, but to get that conversation
[1518.90 → 1526.02] going, that for me, even saying it now, I know a lot of people who wouldn't be happy with that.
[1526.46 → 1526.86] Yeah.
[1527.02 → 1531.64] At that point, you're not really doing, that's not really product management anymore, right?
[1531.70 → 1534.56] That's like team management to some degree, right?
[1534.62 → 1534.72] Yeah.
[1534.82 → 1538.34] You're the one that's like setting up all the work for everybody to do.
[1538.58 → 1541.94] And I would assume also like tracking to make sure that people are doing things.
[1541.94 → 1546.08] So that's like team plus project management, which is not what product management is about.
[1546.56 → 1549.24] But I think that's where, you know, there are roles you have to fill on every team, right?
[1549.26 → 1553.74] Like every team obviously needs engineers, but you also need someone to like to be the leader
[1553.74 → 1556.94] of the team so that you can get consensus around everything that you're doing.
[1557.16 → 1561.10] You need someone to keep track of whatever's going on to make sure that, you know, things
[1561.10 → 1562.44] aren't getting lost.
[1562.44 → 1567.52] You have to have someone that is out there like setting the future saying, hey, this
[1567.52 → 1568.54] is where we want to go.
[1568.70 → 1570.50] Like these are the things we want to build.
[1570.78 → 1573.54] So you can have, you know, one person that fulfills those things.
[1573.56 → 1576.48] You can have a couple of people that kind of shift between those things.
[1576.58 → 1581.72] But I think it's very important to like actually make the roles very clearly defined as to like
[1581.72 → 1583.14] what they are and what they expect.
[1583.48 → 1587.46] Because I think like part of the problem we have probably as an industry is that we're very
[1587.46 → 1592.04] bad at defining what these roles are, which I think explains why we have so many of these
[1592.04 → 1594.64] like titles that all have the same letters in them.
[1594.74 → 1598.70] Like there's product manager, project manager, technical project manager, technical product
[1598.70 → 1599.06] manager.
[1599.34 → 1600.92] It's like all of these things.
[1601.02 → 1603.10] It's like they're all kind of operating in the same space.
[1603.14 → 1604.66] We're trying to use like one thing to describe.
[1604.74 → 1607.46] It's like, okay, no, you're just like, you're doing some project management, and you're doing
[1607.46 → 1608.30] some product management.
[1608.44 → 1609.52] And like, that's okay.
[1609.64 → 1612.20] One person can do both those things, but we should call it like that.
[1612.56 → 1615.62] Because I think when you, when you don't do that, then it makes it hard for people to
[1615.62 → 1618.50] I think, A, switch between teams or move around teams and move around companies.
[1618.50 → 1624.52] But it also just makes it very unclear when you start to scale how you actually scale
[1624.52 → 1625.60] the team, right?
[1625.64 → 1629.68] Because then if your team gets, you know, that might work for one product manager when
[1629.68 → 1631.66] you have, you know, a team of five people.
[1631.80 → 1637.72] But if you have a team of 10 or 15 people, that's a lot more work to do for one
[1637.72 → 1638.04] person.
[1638.14 → 1640.74] Now you're like, okay, we need to bring a second person in.
[1641.20 → 1645.90] Finding someone that can do that mix of product and project management work is going to be really
[1645.90 → 1646.80] difficult to do.
[1647.38 → 1650.06] And if you've already defined up front, you're like, okay, well, these are my project management
[1650.06 → 1650.62] responsibilities.
[1650.74 → 1652.18] These are my product management responsibilities.
[1652.18 → 1656.04] And you're like, okay, now it seems like there's more project management that has to
[1656.04 → 1656.50] get done.
[1656.74 → 1661.16] So we'll hire another project manager and I can still do product and some of the project
[1661.16 → 1661.50] stuff, right?
[1661.50 → 1665.46] So you can start kind of dividing things out a little bit better.
[1666.08 → 1670.80] But yeah, I think for me personally, I would not want to be on a team where a product manager
[1670.80 → 1675.36] is that heavily involved in the backlog and that heavily involved in the process.
[1675.68 → 1681.92] I typically don't like teams where the engineers don't have a high degree of autonomy and a high
[1681.92 → 1683.02] degree of trust in them.
[1683.30 → 1688.12] So I think ultimately the way I kind of see things is like engineers should be trusted to
[1688.12 → 1689.30] prioritize work properly.
[1689.42 → 1692.22] They should be trusted to maintain the backlog.
[1692.40 → 1696.00] Because at the end of the day, it's like if you have a bunch of tickets and let's say that
[1696.00 → 1698.80] you wrote them all up, well, the engineers have to understand them.
[1698.80 → 1701.34] So it's like now you have to spend all this time translating it for them.
[1701.40 → 1705.32] It's easier if they just write them themselves, make sure they have the information so another
[1705.32 → 1708.04] team member could actually pick up that ticket and do it.
[1708.28 → 1712.22] And they have to own the responsibility of making sure that that information is sufficient
[1712.22 → 1714.02] for what other people need.
[1714.14 → 1718.00] So if higher ups need to be able to track what's going on, the tickets need to have enough
[1718.00 → 1719.18] information to make that happen.
[1719.54 → 1723.08] I think that's much more scalable than trying to put that all onto one person.
[1723.14 → 1726.16] And I've definitely seen it more scalable in teams like that.
[1726.16 → 1730.04] I think a lot of the teams I've been on, there's just been like one person that's trying to
[1730.04 → 1734.46] like write up all the tickets or like the team manager like it takes the epic and then
[1734.46 → 1736.14] breaks it out into a bunch of stories.
[1736.14 → 1741.24] And then like all in this, like under this, I think process that like, oh, well,
[1741.26 → 1743.50] we just want the engineers to be like writing code.
[1743.64 → 1745.86] And I think that that doesn't help us in the long run.
[1745.96 → 1747.78] It's like engineering is about more than just writing code.
[1747.88 → 1751.64] I think in the last podcast I said like writing code is the least important part of software
[1751.64 → 1752.06] engineering.
[1752.66 → 1754.80] There are so many other things that we have to do.
[1755.50 → 1758.74] And if you don't give the engineers the autonomy to do that, if you don't give them the authority
[1758.74 → 1761.92] to do that, then they're going to just not do it.
[1761.92 → 1764.70] And that's going to make it much more difficult to build software in the end.
[1765.16 → 1768.74] So I think in general, it's a long way of saying I think product managers need to be
[1768.74 → 1769.96] much higher up than that.
[1770.06 → 1773.44] I don't think that they should really be doing that project management work.
[1773.48 → 1776.72] And I don't think you should necessarily bring on a project manager until it's like,
[1777.10 → 1780.40] OK, no, we really have a team big enough that we need someone to like to manage everything
[1780.40 → 1783.56] because it's difficult for engineers to keep on top of all of it.
[1783.96 → 1787.44] So you would not be happy if I jumped on a PR and reviewed it?
[1787.44 → 1792.46] I mean, like you could, but I don't know if that's like the best use of a that's like
[1792.46 → 1796.04] half PM, half software engineer, which once again, if that's like a thing we have, then
[1796.04 → 1796.80] like, sure.
[1797.22 → 1800.44] But from like a person is a product man, that is their title.
[1800.52 → 1801.22] That is all they do.
[1801.28 → 1805.46] I'd be like, no, that person's like a product manager plus some level of engineer because
[1805.46 → 1806.32] that's what they're doing.
[1806.38 → 1807.10] And we should call them that.
[1807.16 → 1807.76] And then, yeah, sure.
[1807.80 → 1809.90] Like 50% product, 50% engineer.
[1810.06 → 1810.30] Cool.
[1810.58 → 1811.80] I don't have a problem with that.
[1811.80 → 1818.28] Yeah, I think if the product manager were that hands on, you would probably not be spending
[1818.28 → 1822.68] your time on other things that to me are the more fun things that are part of the role.
[1823.04 → 1827.26] But on the other hand, like maybe, I don't know, maybe your product is a product that
[1827.26 → 1831.84] is for other engineers at the company, and you're trying to understand like what is the
[1831.84 → 1832.56] experience?
[1832.70 → 1835.84] And so maybe that's why you're doing a PR to experience it yourself.
[1836.34 → 1838.98] You know, maybe in that case, it's appropriate.
[1838.98 → 1842.28] But yeah, I think I would strike a balance.
[1842.50 → 1846.84] Like I think the engineers should be able to write their own tickets and determine what's
[1846.84 → 1848.04] important to work on next.
[1848.66 → 1850.94] And product person should also be writing some tickets.
[1851.56 → 1855.22] Everybody on the team who identifies a need for something that the team should be working
[1855.22 → 1857.24] on should be able to write a ticket.
[1857.94 → 1861.38] And yeah, I think we should all be expecting that things can change.
[1862.16 → 1867.92] But something happens, maybe there's an incident or some new customer need or business
[1867.92 → 1872.58] has shifted in a dramatic way, maybe due to the pandemic or something else.
[1872.72 → 1875.06] We might need to be rejiggering our backlog.
[1875.66 → 1877.84] And so, yeah, I think that's a collaborative exercise.
[1878.54 → 1881.66] And I don't think it has to all be done by the product manager.
[1882.20 → 1885.64] I think the product manager can help shape maybe some of the practices.
[1886.22 → 1891.36] Like, you know, for example, one of the things I like to help make sure we're doing just for
[1891.36 → 1894.82] good team health is to be really clear on the acceptance criteria.
[1894.82 → 1898.22] So we can all agree, like, okay, this work is done.
[1898.74 → 1902.22] Here's the scope of it, you know, so that we can keep delivering.
[1902.68 → 1904.10] So like, that's one of my things.
[1904.18 → 1908.20] I like to make sure we have acceptance criteria and that we all understand what the acceptance
[1908.20 → 1909.20] criteria are.
[1909.72 → 1914.06] I don't like to be prescriptive about like how we're going to do something, especially
[1914.06 → 1915.50] not on the engineering side.
[1915.50 → 1919.46] I think that is way beyond what I should be doing and that would not be appropriate.
[1920.78 → 1925.40] So I know we've touched on this a little bit, and it's been mentioned a few times in
[1925.40 → 1929.26] regard to external team management and dependencies.
[1929.26 → 1935.88] So a lot of our time as product managers is spent having meetings with people, understanding their
[1935.88 → 1939.94] needs, understanding what work is required from our team.
[1940.50 → 1949.30] I guess, do we either Gail or Chris see a world in which a senior software engineer, an engineering
[1949.30 → 1952.00] league would take on that role?
[1952.00 → 1958.72] If we got rid of the PM role within a team, or do you feel like product managers have unique
[1958.72 → 1959.76] skill sets?
[1959.76 → 1963.36] And this is not a trick question to be able to do that.
[1963.40 → 1967.78] Just because I know, Chris, you've talked about that being something you'd like, you
[1967.78 → 1971.68] know, the engineers to be thinking around business value, being able to prioritize their
[1971.68 → 1971.94] work.
[1971.98 → 1974.34] So I'd love to hear your views on that.
[1975.02 → 1979.60] Yeah, I think it depends on what the team is doing.
[1979.60 → 1985.30] So I think if it's like internal products versus external products, I think in some cases,
[1985.40 → 1988.96] depending on the size of the company and internal product manager makes sense.
[1989.26 → 1994.06] But I think for most companies, you probably want the engineers to kind of be doing their
[1994.06 → 1997.76] own product and be able, capable of doing that sort of work.
[1998.04 → 2002.58] But I think in general, like the thing that I've always found is like, if you have good process
[2002.58 → 2009.38] for your organization as a whole, and you have good forms of communication, like the need
[2009.38 → 2014.24] to have a human that's kind of transiting information between people decreases a lot.
[2014.60 → 2018.28] So I think like, I mean, I always see it as kind of failing of an organization, even
[2018.28 → 2022.74] when like a manager has to talk to another manager to transit some information, because
[2022.74 → 2025.92] then you're going from like some engineer is telling some manager is telling another
[2025.92 → 2027.18] manager is telling an engineer.
[2027.34 → 2029.80] And it's like, we all played telephone as a kid.
[2030.14 → 2031.20] That never worked well.
[2031.34 → 2035.56] It was always like, you know, that was the fun of the game is you'd be like, oh, what weird
[2035.56 → 2038.52] thing is going to come out the other end of the telephone line.
[2038.66 → 2041.04] That's completely not what I said.
[2041.32 → 2046.76] So I think fixing those problems and reducing the friction of communication is super important
[2046.76 → 2046.88] there.
[2046.90 → 2050.92] And I think that can actually reduce the need for like as many like internal or cross
[2050.92 → 2051.92] team product managers.
[2052.28 → 2056.36] And then I think, you know, product managers really do get to go talk to the people who
[2056.36 → 2059.60] like aren't within the company and aren't going to adhere to the same sort of process
[2059.60 → 2063.66] and communication systems or like, you know, just aren't going to be able to give
[2063.66 → 2067.34] in that feedback, like if you are just building a product, and you have like some users like
[2067.34 → 2071.26] actually sit down, talk to the users, do user studies, all of that sort of stuff.
[2071.62 → 2074.58] They're not just going to kind of walk up and be like, here's everything I want you to
[2074.58 → 2078.34] build or be able to translate that into like something useful for you internally.
[2079.02 → 2082.64] So yeah, I think like when it comes to cross team communication, like it's not a good use
[2082.64 → 2084.48] of product manager skill set to be doing that.
[2084.56 → 2089.38] Really, it's not a good use of anybody's skill set to just be like transiting information
[2089.38 → 2090.52] between two humans.
[2090.52 → 2094.16] Like we're all adults, we should all be able to talk and communicate with each other.
[2094.62 → 2095.94] That's, I guess, where I fall on that.
[2096.70 → 2102.82] Yeah, I think that if, you know, there's maybe five plus engineers on the team and only one
[2102.82 → 2107.42] of me, if I have to be involved in every single conversation that the engineers are going to
[2107.42 → 2110.12] have with another team, this is going to take forever.
[2110.66 → 2115.90] And then also, personally, I think the engineers are completely capable of talking to each other.
[2115.90 → 2121.72] So yeah, I would tend to agree that there's no reason why we can't go talk to other people
[2121.72 → 2124.30] and ask questions and find out information.
[2124.54 → 2130.66] I think in terms of cross team communication, where product person can help is there's this
[2130.66 → 2137.14] interesting art form, I believe, of sharing the plans of the team with another team so you
[2137.14 → 2138.26] can set expectations.
[2138.80 → 2144.20] And I say art form because you don't want to overpromise, but also you want to be setting
[2144.20 → 2144.80] expectations.
[2144.80 → 2149.70] I think I always try to strike a balance between telling teams like, here's what's coming next,
[2150.14 → 2153.00] but also potentially anticipating that things might change.
[2153.46 → 2159.36] So you have to be specific, but also a little bit vague at the same time, not reveal timelines
[2159.36 → 2159.98] too much.
[2161.04 → 2165.60] Sometimes I've had situations where sales gets really excited, and they want to try and go
[2165.60 → 2167.78] and sell something to the market, but it's not ready yet.
[2168.10 → 2173.18] So this is why you want to be careful about what you communicate and do so in a way that's
[2173.18 → 2178.80] useful to other teams, potentially get other teams excited and can help teams prepare for
[2178.80 → 2180.06] partnering with your team.
[2180.50 → 2182.34] That's helpful conversations to have.
[2182.46 → 2186.40] And the product person can be strategic in how do we want to set up that conversation?
[2187.22 → 2191.20] What is important to share versus what we could keep to ourselves for now as we're continuing
[2191.20 → 2192.12] to do some work?
[2192.12 → 2197.02] So that is a little bit of stakeholder management and a product can help do.
[2197.28 → 2197.52] Right.
[2197.88 → 2202.52] I sort of like, I understand why we need to do that on a level, but I'm also just kind
[2202.52 → 2206.98] of like, I feel like that exposes our, like some problems that we have, especially around
[2206.98 → 2209.90] like the telling people when we'll be able to deliver something.
[2209.90 → 2214.36] That's always been something that's really irked me about the way that we do software engineering
[2214.36 → 2216.00] because like everybody's always optimistic.
[2216.00 → 2217.74] They're like, how long is it going to take?
[2217.82 → 2219.08] And he's just like, I can do that in two days.
[2219.08 → 2220.00] And it's like, you can't do that.
[2220.14 → 2221.48] And you can't do that in two weeks.
[2221.48 → 2223.16] Like, like, like, let's be reasonable.
[2224.16 → 2227.00] Which is where I think also I get back to the whole, like, we'd be a better process.
[2227.00 → 2230.12] Like we need better ways of describing how long something's going to take.
[2230.16 → 2232.56] Like giving someone a that'll be done in two months.
[2232.58 → 2234.30] Like that's not reality.
[2234.30 → 2236.30] It's like, you know, it might be two months.
[2236.34 → 2237.42] It might be two and a half months.
[2237.42 → 2243.04] You have some amount of confidence that you have in how done it'll be by what time.
[2243.22 → 2244.38] There's all of these risks.
[2244.38 → 2245.56] Like the thing might never happen.
[2245.56 → 2246.26] And it might get cancelled.
[2246.42 → 2247.82] We might have to delay it for other reasons.
[2248.40 → 2254.52] And I feel like we, we as an industry lack a lot of the language we need to actually express that well.
[2254.72 → 2259.96] You know, we try to kind of cram everything down into story points or t-shirt sizes or what have you.
[2260.46 → 2267.50] It's unfortunate that we have to use someone's skill set that could be used for like communicating with people outside the organization to communicate inside the organization.
[2267.50 → 2275.24] Like that just seems like a failing of our organizations if that's something that's happening and something we should like address and be like, no.
[2275.24 → 2277.22] Like we're all on the same team here.
[2277.22 → 2282.14] Like sales, here's what you can read to figure out if we're actually going to be able to meet something.
[2282.28 → 2285.76] And if you go oversell it, like that's your problem, not ours.
[2285.76 → 2287.06] Like don't do that, please.
[2287.06 → 2289.40] That's like hurting other people within the organization.
[2289.40 → 2290.24] Yeah.
[2290.66 → 2291.88] I mean, I feel that.
[2292.20 → 2295.54] I think what you said about we're all on the same team.
[2296.28 → 2297.54] I also feel strongly.
[2297.76 → 2299.66] I would love it if that was the case.
[2299.90 → 2301.12] But often it's not.
[2301.58 → 2311.14] Often it feels a little bit like six different cooks trying to make different dishes, and they all need the same ingredients, and they're fighting over the ingredients.
[2311.14 → 2322.14] And then the product manager, chef in this analogy, has to advocate why they would use the tartar sauce better than this other person.
[2322.14 → 2329.82] But they'll give the tartar sauce in a months as long as they finish their dish.
[2330.58 → 2334.52] And I think in my mind, that is part of the art of being a product manager.
[2334.52 → 2346.18] It's being able to have a room filled with different kind of people trying to do different things, agree on an approach and have them leave.
[2346.22 → 2351.62] Whether it's a meeting, it's an email thread, Slack thread, feeling happy and feeling great.
[2351.72 → 2352.78] I achieved something.
[2353.20 → 2354.94] I have got what I wanted.
[2355.40 → 2360.36] I'm going to be able to do what I needed to do to fulfill my goals for the business, etc.
[2360.36 → 2376.60] And that for me is, I think, the reason why it's difficult to not play this kind of game of giving enough information but holding some back, framing it in the right way.
[2376.60 → 2388.88] Especially, I think, when you are on a platform team or a team who does predominantly back-end work, and you are trying to advocate to a feature team, a front-end facing team,
[2389.16 → 2399.22] why you need six months to completely redo your back-end infrastructure, change your database, migrate to a different cloud infrastructure.
[2399.22 → 2407.78] When they then said, okay, well, is that going to enable us to do audience segmentation, personalization?
[2408.30 → 2413.34] How is that going to add some value to our end users?
[2413.66 → 2416.12] And you say, oh, well, it's not really.
[2416.50 → 2418.36] It's going to make it more resilient.
[2418.70 → 2420.60] It's going to make our platform better.
[2421.02 → 2425.06] It's going to get rid of a load of tech debt, useless code.
[2425.06 → 2440.68] I think part of the art of a product manager is being able to put it in a way that has them go away going, oh, yeah, we really need to spend these six months doing this work.
[2440.92 → 2442.80] Oh, yeah, this is going to be great.
[2443.50 → 2445.60] So I think there is a bit of an art there.
[2445.60 → 2451.12] I do like to default to taking the approach we're on the same team.
[2451.54 → 2454.14] But different teams do have different goals.
[2454.38 → 2462.70] And that introduces interesting tension where some teams might be really driving growth for the company, and they might be testing and iterating really fast.
[2462.96 → 2468.54] And perhaps another team is developing foundational platform tools.
[2468.74 → 2470.32] And those really need to be resilient.
[2470.32 → 2477.54] And so you might be a little bit more thoughtful and careful as you roll out a change because it could impact the entire company.
[2478.04 → 2485.96] So I think having tension between teams is OK, because ultimately all teams are thinking about how they can benefit the company in the best way possible.
[2486.10 → 2488.08] They just have different ways of doing so.
[2488.28 → 2489.06] And that's OK.
[2489.06 → 2498.22] And then in regard to communication, I kind of try to take the approach of thinking about, you know, if I'm the other team, what is it that I need to know?
[2498.40 → 2509.28] And that's what I prioritize telling teams like you might be interested in knowing that we're going to deprecate this thing, and you're going to have to be able to be ready to migrate to a new thing.
[2509.28 → 2513.26] And it'll be better, and it'll allow you to do X, Y, Z.
[2513.80 → 2516.24] But just know, you know, maybe you're building a new application.
[2516.82 → 2523.04] You might want to align your timeline with our timeline because you could benefit and use a new thing in your new application.
[2523.46 → 2524.24] So that's what I do.
[2524.28 → 2527.34] I try to give the information that's going to be the most useful.
[2527.86 → 2533.78] And, you know, maybe we weren't ready to tell folks yet, but I know, oh, this team, it would really help their roadmap.
[2534.22 → 2538.54] They wouldn't have to do rework, and they wouldn't lose effort if I tell them right now.
[2539.34 → 2541.58] So that's kind of like my communication practice.
[2541.92 → 2544.28] Like I share what is going to be most useful.
[2544.72 → 2548.94] I don't want teams to go off and like to spin their wheels and like to think about things too much.
[2549.06 → 2556.44] You know, like maybe sometimes I don't have enough to tell folks yet because we're still doing discovery, trying to figure out what's the best technical solution for something.
[2556.98 → 2559.60] So, yeah, I might have to just like forecast at a really high level.
[2559.84 → 2561.46] Like this thing is going away.
[2561.46 → 2565.06] I don't know yet what's the new thing, but we're going to make it better.
[2565.06 → 2568.74] And just know that you may need to plan accordingly.
[2569.04 → 2570.38] And that can be useful to teams.
[2570.76 → 2570.90] Yeah.
[2571.06 → 2574.76] So I just take the perspective of we are working together.
[2574.94 → 2576.96] We're trying to do the best that we can.
[2576.96 → 2581.34] And I may know some piece of information that might be useful to someone else.
[2581.34 → 2589.08] So because I know a little bit about what they might be working on, and I've built that relationship, and I've been kind of keeping a track of what their roadmap might be.
[2589.52 → 2591.62] And I'll be like, OK, high key stakeholder.
[2592.18 → 2593.20] Here's what I think you should know.
[2593.38 → 2594.88] And hopefully it's helpful to you.
[2594.88 → 2602.90] And then maybe they'll reciprocate and tell us like, hey, we've been exploring this really important new feature we want to launch to our customers.
[2603.44 → 2606.60] And we think we might need you to create, update something.
[2606.98 → 2610.00] And maybe a new API endpoint might need to be surfaced.
[2610.38 → 2613.22] It's helpful for me if I know about it as early as possible.
[2613.70 → 2618.28] And maybe they're still doing some customer research right now, but they're getting positive feedback.
[2618.28 → 2621.84] And so I can start to know like, OK, this might come up in the future.
[2622.38 → 2625.28] Maybe I should start having some preliminary conversations on my end.
[2625.54 → 2627.50] So I feel like there's always like benefits.
[2627.68 → 2631.78] If I share a little bit, folks might share with me and then I can anticipate better.
[2632.26 → 2636.46] So, yeah, it's all, you know, towards this like grander vision of working better.
[2636.92 → 2642.74] Although I do wonder, I guess on that level, it's like I understand the need for this now.
[2642.74 → 2649.32] But I also feel like this is just not a productive way for us to be working.
[2649.66 → 2654.80] I guess for an industry that like prides itself so much on like innovation and doing all this amazing stuff.
[2654.80 → 2660.56] It's like, well, we should be able to sit down and like if we're all in the same company, we're all trying to achieve the same goal.
[2660.78 → 2668.16] Like our leaders really should be sitting down and figuring out and talking with each other and being like, OK, well, yeah, there are teams that need to move fast and iterate quickly.
[2668.16 → 2677.68] And there are other teams that need to like move slowly, and we need to prioritize both those teams and figure out ways that they can all work together without having to like play hide Z with information.
[2678.08 → 2686.30] And I guess in my career, I've always kind of looked at, you know, that need to hide or that need to, oh, well, we won't tell them what we're really doing, or we'll deliver that thing later.
[2686.30 → 2691.30] Or just like being overly optimistic and saying, oh, well, we won't need that feature, or we won't need that thing.
[2691.30 → 2708.42] I feel like that's ultimately what kind of trickles down and leads to us like burning out our engineers or leading situations where like people are pulling 70 or 80 hour weeks for months at a time because like we just weren't able to plan things out well because we're not really projecting and looking far enough in the future.
[2708.98 → 2716.30] Like I think whenever I hear that like, you know, some platform team is having trouble justifying why they need to do what they do.
[2716.30 → 2718.26] I'm like, that's a failing of the entire company.
[2718.42 → 2728.30] Like if the organization doesn't understand like why your foundation needs to be taken care of, it's kind of like, oh, I don't see why we need to have like heating and cooling in our office and running water.
[2728.50 → 2730.80] Like we don't need to have running water on the weekends.
[2730.92 → 2732.82] So we should just like turn it off on the weekends.
[2732.82 → 2736.06] We should just like turn off the HVAC system on the weekends.
[2736.16 → 2737.92] It'll be fine to turn it in Monday morning.
[2737.92 → 2744.98] And then everybody's sitting in an 80 degree office or like an 85 degree office that has like 40, like 80 percent humidity and everybody's miserable.
[2744.98 → 2747.74] It's like, no, you have to like plan things out into the future.
[2747.96 → 2750.50] It's like there's no everything can't be instantaneous.
[2750.94 → 2752.74] Like there's lead times for things.
[2753.06 → 2761.18] So that's especially true for anything that's like big and platform where it's just like, yeah, I know these things take multiple years to build and multiple years to build well.
[2761.60 → 2765.34] You can't just look at it as building everything in two weeks sprints or whatever.
[2765.84 → 2773.06] So I think like the organization doesn't understand that that's like an organizational level that needs to be solved, which like some organizations just don't care.
[2773.06 → 2777.78] And in that case, I think like product managers can fill that useful void with their skill set.
[2777.96 → 2782.58] But also just like that seems to me to be like a miserable environment to be working in.
[2782.68 → 2785.86] It feels like I guess it depends on how you value your job at the end of the day.
[2785.92 → 2789.88] Or like if you're just like, I just want to go in and do some work and I don't care as much about the whole thing.
[2789.94 → 2790.84] So it's like I want to do a job.
[2790.92 → 2792.94] I derive happiness from other things in my life.
[2793.18 → 2796.12] I think people like that would probably thrive in these environments.
[2796.12 → 2800.20] But I think if you're like, no, no, I really deeply care about this and everything around me.
[2800.20 → 2811.86] I just imagine that it's got to be a frustrating space to live within or exist within of just like fighting this uphill battle and having people just like not really understand or not really feel like everybody's on the same team.
[2811.86 → 2827.98] This episode is brought to you by our friends at GitLab.
[2828.10 → 2834.92] GitLab is inviting you to attend GitLab Commit 2021, their upcoming user community event, August 3rd and 4th.
[2835.10 → 2835.84] It's free.
[2836.02 → 2836.92] It's virtual.
[2837.12 → 2838.42] And everyone can attend.
[2838.42 → 2844.86] Learn more about modern DevOps and how it transforms companies of all sizes and pushes teams to drive innovation to market.
[2845.32 → 2854.30] During this two-day conference, attendees across all time zones will learn how they can instill modern DevOps practices at their organizations through in-depth trainings and workshops.
[2854.60 → 2863.80] Hear firsthand stories from some of the most well-known companies and gain insight into cutting-edge CCD and security technologies that bring companies to the next level.
[2863.80 → 2868.30] Get ready to innovate together during this free event designed to help you to commit to better DevOps.
[2868.42 → 2873.44] Register and learn more at GitLabCommitVirtual2021.com.
[2873.62 → 2878.14] Once again, that's GitLabCommitVirtual2021.com.
[2878.22 → 2879.60] Or check for links in the show notes.
[2879.60 → 2903.86] This is completely just off the top of my head, a thought.
[2903.86 → 2921.12] But do you feel like some of these struggles are rooted in these companies that are not kind of technology-first companies who then try to make the move to being, you know, technology-first, digital-first companies?
[2921.12 → 2943.12] And therefore kind of try to hire hundreds of engineers, build out their technical org without really taking the time to ensure the engineering work cycle, the way that we work in technology is optimized, is ideal.
[2943.12 → 2944.12] This is completely off the top of my head.
[2944.12 → 2945.90] This is completely off the top of my head.
[2945.90 → 2946.16] Yeah.
[2946.42 → 2960.84] But I personally feel like I've talked to a lot of people who have said as product managers or as engineers, they've struggled when the org has grown substantively.
[2960.84 → 2964.92] They've suddenly said technology is first.
[2965.12 → 2967.58] Engineers are our most important employees.
[2968.62 → 2972.88] But haven't optimized for how do we work with all these engineers?
[2973.04 → 2975.04] How do they work together most effectively?
[2976.08 → 2976.46] Yeah.
[2976.76 → 2976.94] Yeah.
[2977.00 → 2980.60] I think originally I was going to say that in my experience it's been like kind of the opposite.
[2980.76 → 2990.82] It's like the organizations that are very like from the beginning, software engineering organizations or whatever, those are the ones I think are like have the worst problems when it comes to this sort of stuff.
[2990.82 → 3002.50] But I think in general it depends very much I think on what kind of operating system, but not in like OS, but like how the organization and company as a whole operates.
[3002.66 → 3016.10] Because I think organizations that tend to have fewer problems are likely those that already have a practice of like implementing processes and having processes for moving information around and having like, you know, all those nice checklists that are like, hey, you want to do a project?
[3016.20 → 3017.28] Here's all the stuff you got to do.
[3017.28 → 3021.94] I think when you have those types of organizations, they're already primed to scale.
[3022.12 → 3024.02] So it's not as big of a problem for them.
[3024.60 → 3033.28] But yeah, I think if like you just try and throw a bunch of engineers at a problem and say like, hey, we're technology first now.
[3033.36 → 3035.02] Go build a bunch of stuff.
[3035.56 → 3043.62] I think that's like honestly why a lot of these fiefdoms and a lot of these positions that like could be the skill sets people have could be better used elsewhere wind up in this.
[3043.62 → 3045.18] Because it's like no one planned it.
[3045.20 → 3046.00] No one thought it through.
[3046.06 → 3048.36] And no one said, hey, things are a little funky here.
[3048.36 → 3052.36] Let's stop and revisit and go back and, you know, fix things up.
[3052.56 → 3059.94] Because yeah, I think at the end of the day, what I've really been trying to say here is just like I think product managers are like incredibly like talented people.
[3059.94 → 3072.80] And I think that their skill sets are very much wasted shuffling information between teams and playing strategic heresies with information between groups of people that have no reason to have adversarial relationships.
[3072.80 → 3085.72] Yeah, I think to add to that, I feel like product is an interesting balance between strategy and execution because, you know, you can strategize as much as you want.
[3085.88 → 3093.96] But at the end of the day, if you don't help the team get something accomplished, then it was a bad strategy or is a poorly executed strategy.
[3093.96 → 3101.04] And so the product manager does have a role to play in ensuring that we're successful as a team and as an organization.
[3102.04 → 3111.40] And, you know, I guess in terms of like sharing information, my personal take on this is to overshare and share a lot and be as transparent as possible.
[3111.90 → 3113.20] Actually, Angelica knows this.
[3113.30 → 3114.96] I like to send out newsletters.
[3114.96 → 3124.86] I'm huge on newsletters and keeping anyone who might be interested can subscribe and like to get the information and hear like what we were up to most recently.
[3125.36 → 3134.16] But if you're not interested, if it's too much noise for you, and it's, you know, taking focus away from your day-to-day work, then you don't have to subscribe to the newsletter, and you don't need to know.
[3134.62 → 3144.14] If you do need to know, I'm going to make sure to reach out to you and be like, hey, you might care to know this will be happening, and it'll impact you, and you should be thinking about it.
[3144.14 → 3147.30] And like, please let me know if I can help you in any way.
[3148.06 → 3156.08] But yeah, in terms of information sharing, I think sharing information is really important, and it helps folks do what they need to do.
[3156.40 → 3161.46] I also agree to what you were saying in terms of like having good processes, like an operating system.
[3161.94 → 3168.10] I think that's true that that helps organizations be well set up for success when we have good practices in place.
[3168.10 → 3173.06] It's like some of the things that I've enjoyed at the New York Times is that there are some rituals.
[3173.06 → 3184.66] For example, when engineers are working on a big new initiative, typically they'll write what we call an RFC request for comments, and it'll detail everything that the team has been thinking about.
[3185.08 → 3192.32] And then it'll be sent out to the entire organization and folks can have a chance to submit comments on what's proposed.
[3192.32 → 3203.88] And this is a fascinating way to build knowledge across the teams because you can kind of get some information about what's the problem the team is looking to solve, how they thought about potentially solving it.
[3204.02 → 3209.80] And then other teams have a chance to like push back on certain proposed ideas and like help improve.
[3210.18 → 3211.76] Or if you don't have time, you don't care.
[3211.92 → 3214.72] You don't have to submit comments, but it's open to anyone.
[3214.72 → 3221.92] And that's fascinating because I've heard about projects from other teams by just like seeing what was the latest RFC that was published.
[3222.34 → 3223.72] So, yes, I agree.
[3223.80 → 3227.06] Like having good processes can really help an organization.
[3227.82 → 3236.14] So we spent a lot of this time talking about big companies and operating within this big business model.
[3236.14 → 3245.42] But I want to ask both of you, if you were starting a startup, just you, you had this great idea.
[3246.06 → 3247.58] Do you need a product manager?
[3248.28 → 3251.00] Is that going to be one of your first employees?
[3252.14 → 3253.74] Maybe not, I would say.
[3254.70 → 3256.02] Maybe this is controversial.
[3257.06 → 3260.18] You know, it depends on what the startup is doing.
[3260.64 → 3263.32] I think, yeah, it depends on what it is that you're doing.
[3263.32 → 3269.54] But I'm thinking some of the earlier folks might need to be actually building things.
[3270.22 → 3273.22] That might be one of the most important skill set to have at first.
[3273.82 → 3276.28] And, you know, in my mind, there's, we've touched on this.
[3276.38 → 3281.46] Like there's really no reason why folks can't go and ask people questions.
[3281.46 → 3285.52] You know if it's your potential customer, try to like to show them a prototype.
[3285.80 → 3287.12] Be like, what do you think of this?
[3287.20 → 3288.74] And, you know, learn from the feedback.
[3288.86 → 3290.52] I think anyone can do that.
[3290.54 → 3292.42] And it doesn't necessarily have to be a product manager.
[3292.42 → 3299.36] But I think the product manager later on can become really valuable because they can go really deep with the user research.
[3299.54 → 3306.38] Like, you know, maybe now we're ready for deeper, maybe it's a more difficult problem that we're trying to solve.
[3307.08 → 3309.70] But earlier on, I think you might need different skill sets.
[3309.70 → 3309.84] Okay.
[3310.06 → 3319.14] So your view would be a product manager is only really effective when you have a large existing product.
[3319.64 → 3321.06] Is that semi-accurate?
[3321.06 → 3322.90] Yeah, I think so.
[3323.30 → 3325.66] I have not been a part of a startup, so that's a disclaimer.
[3326.20 → 3326.24] Fair enough.
[3326.24 → 3326.92] I'm just wondering.
[3327.26 → 3330.14] But yeah, I'm thinking a startup is like looking to move fast.
[3330.64 → 3336.22] And, you know, as a smaller team, probably I think the team can be closer to the customer.
[3336.78 → 3346.92] You may have less of a need for having really detailed product requirements and conducting, you know, industry research and looking at more of the financials.
[3346.92 → 3347.68] It depends.
[3347.92 → 3352.20] Like, maybe it is helpful to have a product manager that can do some of that work.
[3352.56 → 3353.86] Maybe, you know, a step two.
[3355.00 → 3357.34] See, I disagree.
[3357.34 → 3365.22] I think you don't necessarily need to have a product manager, but you definitely need someone who can do that product thinking.
[3365.22 → 3368.80] Because my view is you're going to launch a startup.
[3369.12 → 3372.86] If it's going to be successful, you need to know that that's actually a need.
[3372.98 → 3375.48] You need to know those user needs.
[3375.68 → 3380.82] You need to know what is going to get that kind of, I don't know, financial backing.
[3381.14 → 3382.34] You need to go pitch your product.
[3382.34 → 3389.00] You need to tell people why it's important to get, you know, angel funding or whatever you need to get that thing off the ground.
[3389.38 → 3397.56] I think for me, you do need a product manager from day one, more so than established larger companies.
[3397.90 → 3398.96] Chris, thoughts?
[3399.16 → 3401.76] See, I'm just going to say, I'm going to say flat out no.
[3402.38 → 3411.22] Because A, I think that people that start the company should, like, I think that the best people to start companies are people that are building products for themselves.
[3411.22 → 3421.02] I think it's not a great idea to try and go build a product for somebody else or a product that you don't understand or don't have that.
[3421.20 → 3422.30] Because it's going to be slower.
[3422.48 → 3426.16] You're going to be way slower than someone that knows that need.
[3426.76 → 3430.98] So in that way, like, I don't think you need a dedicated product person.
[3430.98 → 3439.02] Because I think that, at least initially, the founders, at least one of the founders, has to be the person that has, that can do that product-like work.
[3439.02 → 3444.56] And I also think that you really need to hire engineers that can do product-like work.
[3444.70 → 3457.40] Because, like, I think the problem with trying to bring in a product manager at a small company or, like, you know, just when you're starting is that that means that there's some extra translation that you're doing to someone who doesn't understand product.
[3457.52 → 3457.60] Right?
[3457.72 → 3462.64] If you have someone separate that's doing product, that means that there are people within the organization that can't do that work themselves.
[3462.64 → 3464.34] Or otherwise, you wouldn't need them.
[3464.40 → 3469.38] So either your founders don't understand or your engineers don't understand.
[3469.92 → 3476.38] And in that case, like, if you're, like, a team of five or six people, like, why have someone that doesn't understand what you're building?
[3476.48 → 3476.86] Why not?
[3476.96 → 3484.28] Why have someone that's not going to be able to, like, contribute to, like, you know, actually being able to, like, kind of carry more of the weight?
[3484.28 → 3490.12] Like, I think one of the luxuries of being in a larger organization is that, like, you don't have to carry as much.
[3490.22 → 3494.58] Like, you don't have to be the person that does both engineering and product work.
[3494.64 → 3498.50] You can just be someone that picks up tickets, does them, and goes home at the end of the day.
[3498.62 → 3503.62] But I think in those smaller companies, that's not really the environment for that type of thinking or that type of work.
[3503.62 → 3512.76] And I think that could really lead to some of, like, the bloat that smaller companies start to get because they're just like, oh, well, there's one person that's good at, like, smashing out all the tickets.
[3512.82 → 3514.38] Like, they can get these things done so quickly.
[3514.80 → 3518.46] But then, like, they don't really understand what we're trying to build.
[3518.50 → 3521.78] So half the tickets are wrong and, like, we're just doing all this work that we didn't need to do.
[3522.02 → 3528.74] So I think there are probably many other roles that are even more important that I don't expect founders to be able to do.
[3528.74 → 3536.54] Things like culture shaping, like, you know, hiring a D&I officer from the beginning, D&I officer or DEI officer, whatever you want to say.
[3536.88 → 3543.40] From the beginning, I think that's super important because I think a lot of people that start organizations, they know products they want to build.
[3543.48 → 3544.40] They might have sales experience.
[3544.48 → 3545.60] They might have engineering experience.
[3545.98 → 3550.62] Unless you're building a product that's targeting diversity and inclusion, you probably don't have that sort of experience.
[3550.62 → 3554.86] Or unless you're targeting a product that's meant to build cultures, you probably don't have that sort of experience.
[3554.86 → 3562.98] So I would say, like, don't get a product person as one of your first people because, like, you should have some of that skills yourself if you're going to go on this endeavour.
[3563.46 → 3566.06] Hire someone that's going to, like, add something substantial.
[3566.24 → 3569.74] Like, you know, at some point, you have to, if you want to start a company at all, you've got to get a lawyer.
[3569.86 → 3570.60] You've got to get an accountant.
[3571.10 → 3574.40] Like, I think there's these fundamental roles that you really need to fill.
[3574.78 → 3577.20] And I think product can come later on down the road.
[3577.34 → 3579.28] So I think that's something that can, like, fill in.
[3579.44 → 3584.28] And also, like, you know, you kind of probably want to build it when you can actually build out a whole product organization,
[3584.28 → 3588.12] not just, like, one person's way of doing things and whatnot.
[3588.44 → 3592.46] So, yeah, I think it's something that's just, like, later on down the road.
[3592.64 → 3594.76] There's both other roles we can fill.
[3594.88 → 3598.34] And this is a role that, like, basically everybody should share in the beginning.
[3598.84 → 3603.96] And there I was thinking, you and me, Chris, I could be a product.
[3604.50 → 3606.18] I could do all the business strategy.
[3606.62 → 3609.14] You could build the beautiful back end.
[3609.86 → 3611.38] I mean, you're an engineer, too.
[3611.52 → 3612.60] You can write code.
[3612.60 → 3615.42] You can, it's like, this could work.
[3615.46 → 3617.42] If we want to start a company, we can start a company.
[3618.04 → 3619.38] You had it here first.
[3619.38 → 3621.16] We're doing multiple things.
[3621.26 → 3623.00] Me and Chris starting an amazing company.
[3624.94 → 3625.30] Awesome.
[3625.42 → 3628.06] We don't even have to hire a DEI person because I can do DEI.
[3628.34 → 3629.10] Oh, my gosh.
[3629.18 → 3630.06] And I'll do project.
[3630.32 → 3631.96] I'll do front-end engineering.
[3632.50 → 3633.86] I'll do some flutter work.
[3633.94 → 3634.68] I'm so ready.
[3634.78 → 3635.74] I'll do some security.
[3637.34 → 3638.24] I'm so ready.
[3640.04 → 3640.40] Awesome.
[3640.40 → 3642.40] Well, we are coming to time.
[3642.52 → 3646.68] Thank you so, so much for joining us for this fun discussion.
[3646.92 → 3653.22] But I'm not going to let you go yet because we're going to be diving into my favourite section.
[3654.04 → 3654.86] Unpopular opinions.
[3654.86 → 3658.86] Unpopular opinions.
[3658.86 → 3660.26] Unpopular opinions.
[3660.26 → 3661.36] You what?
[3661.46 → 3663.18] I actually think you should probably leave.
[3663.68 → 3668.14] Unpopular opinions.
[3668.14 → 3669.14] Unpopular opinions.
[3672.60 → 3673.16] Awesome.
[3673.50 → 3675.88] So, I'm going to go to you first, Gail.
[3676.40 → 3678.60] What is your unpopular opinion?
[3679.44 → 3679.74] Yep.
[3680.26 → 3688.94] So, I guess my unpopular opinion is that cereal should be eaten with orange juice, not milk.
[3689.10 → 3691.40] That's the better way to eat your cereal.
[3691.40 → 3696.56] And I have gotten some feedback that not everybody agrees with that.
[3696.88 → 3699.02] But that's the way I eat my cereal.
[3699.56 → 3700.90] I've always done it that way.
[3701.16 → 3703.08] I'm going to continue doing it that way.
[3703.18 → 3704.16] And I think it's delicious.
[3704.36 → 3705.86] Do you have a preferred brand?
[3706.04 → 3707.04] Is it Tropical?
[3707.38 → 3708.60] Is it freshly squeezed?
[3709.00 → 3709.74] Is there a preference?
[3710.64 → 3712.60] Yeah, I typically use Tropical.
[3712.80 → 3715.76] But, you know, freshly squeezed brings it to the next level.
[3715.96 → 3719.68] I just don't always have oranges or the time to do that.
[3719.68 → 3721.54] Yeah, okay.
[3723.30 → 3725.12] I'm not quite sure what to say to that.
[3725.70 → 3727.32] I conceptually understand.
[3727.74 → 3730.52] Like, milk seems like this random thing that we put in cereal.
[3730.74 → 3731.38] Like, why not?
[3731.56 → 3735.42] Like, what you want is, like, some liquid to go with your cereal.
[3735.76 → 3737.22] So, it's like, I don't know.
[3737.24 → 3742.10] People switch from, like, cow's milk to goat milk to, you know, oat milk.
[3742.60 → 3743.86] It's like, why not orange juice?
[3743.88 → 3746.10] It's basically just, like, orange milk.
[3746.34 → 3747.78] So, you could just, yeah.
[3748.02 → 3748.48] There you go.
[3748.48 → 3749.20] We'll call it that.
[3749.66 → 3750.14] I mean, if we...
[3750.14 → 3751.82] It's more happy looking.
[3752.12 → 3754.58] You know, you start your day off on a bright note.
[3755.16 → 3755.90] Lots of happiness.
[3756.44 → 3758.02] I feel like I just go crazy.
[3758.32 → 3759.14] What's not to like?
[3759.26 → 3763.38] I don't think anyone would like me after really sugary cereal.
[3763.84 → 3767.30] And then naturally sugary orange juice.
[3767.30 → 3769.66] I'd be going into stand-up.
[3769.88 → 3770.30] Like, hey!
[3772.30 → 3776.24] I mean, I think some folks do need a bit of extra pet in the morning.
[3776.62 → 3777.88] And here you go.
[3778.06 → 3780.80] You could just have your cereal with orange juice.
[3780.90 → 3787.08] I feel like it wouldn't be weird if someone was just like, yeah, I have, like, cereal without, like, milk.
[3787.22 → 3788.62] And then I have a glass of orange juice.
[3788.62 → 3788.86] Yeah.
[3788.86 → 3791.04] Like, that doesn't seem weird to me at all.
[3791.12 → 3791.60] It's just like, I don't know.
[3791.64 → 3793.78] Maybe you're eating some frosted mini-wheats or something.
[3794.16 → 3795.04] And you don't want to have...
[3795.04 → 3796.84] You're just, like, eating them with your hands.
[3796.90 → 3799.06] You have a glass of orange juice that you're also drinking.
[3799.22 → 3800.60] That doesn't seem weird to me.
[3800.64 → 3802.52] So, it's like, just pouring the orange juice into the bowl.
[3802.66 → 3803.86] That's not...
[3803.86 → 3804.58] That doesn't seem...
[3804.58 → 3806.44] Like, I see where you're coming from.
[3806.66 → 3807.12] See where you're coming from.
[3807.12 → 3808.98] It always ends up in your tummy in the end.
[3810.36 → 3811.94] I think I might have to try this tomorrow.
[3811.94 → 3815.24] Yeah, but, like, the experience of eating food is, like, a special thing.
[3816.02 → 3817.94] We don't blend all of our food together.
[3818.60 → 3820.54] Most of us don't blend all of our food together.
[3820.72 → 3821.38] That's what I do.
[3821.44 → 3826.36] I just get my dinner, shove it into my blender, give it a good buzz, and done.
[3829.30 → 3830.50] Thank you so much.
[3830.66 → 3834.08] I'm not sure whether that will be unpopular or not.
[3834.08 → 3841.54] As always, the view was given, and then Chris rationalizes it, and it becomes no longer unpopular.
[3842.62 → 3847.12] Do you have an unpopular, a truly unpopular opinion, Chris?
[3849.02 → 3849.42] Hmm.
[3851.12 → 3852.10] Let me think.
[3852.90 → 3853.98] I can just make something up.
[3854.04 → 3856.24] What's something I've been thinking about that's awkward?
[3856.40 → 3860.72] I secretly love product managers and think they're essential to any startup.
[3860.72 → 3866.88] That sounds like it'd actually be popular, so that's not good.
[3868.50 → 3868.86] Oh.
[3869.40 → 3874.20] I guess this one's, like, super nuanced, so it's not going to be – it's not even going to be, like, one that lands heavily.
[3874.20 → 3883.08] But, like, I think that we should stop trying to use academic terms in the general populace to explain things.
[3883.12 → 3883.28] Okay.
[3883.44 → 3887.06] And I think that the main thing I'm thinking about right now is the word privilege.
[3887.06 → 3903.44] I think that we should find words that are less prone to people immediately misunderstanding them because they're not coming from an, you know, kind of academic or, like, semantic understanding of the word.
[3903.60 → 3909.66] I think we should find words that people can grapple with more because what we're trying to get across is a concept, not, like, the word.
[3909.66 → 3912.84] And also I don't like when people are just, like, check your privilege.
[3913.06 → 3913.50] I'm like, oh.
[3913.98 → 3918.14] I know what you're trying to say, but, like – so, yeah, I think that's it.
[3918.32 → 3924.70] Like, don't just spew academic terms into the general populace as if they work when it's stripped of all of its nuance.
[3924.74 → 3931.62] Yeah, bringing in those layman terms, which actually applies to our topic of the podcast in that – I don't know about you, Gail,
[3931.62 → 3943.60] but when I got into product management, the amount of business terms, random phrases, academic language that I had no idea what it was until I asked.
[3943.70 → 3949.58] And then I was like, oh, why don't you just say it's X, Y, Z, which is so much easier to understand.
[3952.30 → 3952.78] Yes.
[3953.62 → 3955.18] I think I can get behind that.
[3955.18 → 3965.56] But on the other hand, sometimes I think there are words that are very specific and are useful because they really get at the thing we're trying to talk about.
[3965.88 → 3973.22] But, yes, I think layman terms can help more folks be a part of the conversation and also talk about the same thing.
[3974.14 → 3980.16] And that's more valuable, like being able to exchange ideas productively because we're talking about the same thing.
[3980.16 → 3994.04] I will say, though, I think there's a lot of acronyms and things and engineering, really specific words in engineering that I've had to learn so that I can seem more with it as a product manager.
[3994.42 → 3997.18] So, you know, it goes both ways, not just business talk.
[3997.56 → 3999.52] Also, lots of engineering nuance.
[3999.52 → 4000.68] Those acronyms kill me.
[4001.16 → 4002.12] It's like, I'm a PM.
[4002.64 → 4006.40] Is that a product manager, a project manager, a program manager?
[4006.40 → 4010.22] Are you a TPM, a PPM, like an APM?
[4010.74 → 4012.14] Like, so many.
[4012.14 → 4012.58] Hot take.
[4012.74 → 4013.72] Acronyms are terrible.
[4013.98 → 4015.02] We should stop using them.
[4015.50 → 4016.58] Also, hot take.
[4016.66 → 4018.38] I know they're initialisms, not acronyms.
[4018.50 → 4019.96] We're just going to call them acronyms anyway.
[4024.40 → 4025.30] Okay, awesome.
[4025.54 → 4026.50] There are too many of them.
[4026.64 → 4027.16] There are too many.
[4027.38 → 4028.48] We have some fun.
[4028.60 → 4033.44] I think that we also try to use these, like, academic things as, like, showing that you're in the in-club.
[4033.44 → 4036.52] It's like, oh, you know what CAP is.
[4036.58 → 4037.84] You know what the CAP theorem is.
[4037.90 → 4038.44] You're special.
[4038.58 → 4041.70] Oh, you know the different levels of strong consistency?
[4041.98 → 4043.94] Oh, you're super special.
[4044.18 → 4044.96] We like you.
[4045.06 → 4049.24] And it's like, can't you just make these, like, so, like, easier to understand?
[4049.48 → 4051.82] Like, you got to make up a word like invariability.
[4052.16 → 4053.72] Like, no one knows how to spell that.
[4053.90 → 4054.24] Like, what?
[4055.40 → 4055.80] Invariability.
[4055.92 → 4056.08] What?
[4056.30 → 4057.24] No, absolutely not.
[4057.64 → 4062.40] Do we feel like using letters is, or sorry, what did you say, Chris?
[4062.40 → 4063.10] What was the right way?
[4063.24 → 4064.20] I can't say acronym.
[4064.80 → 4066.38] Oh, invariability or CAP?
[4066.74 → 4067.58] No, previously.
[4067.76 → 4070.64] If I'm talking about acronyms, you said that we should call it something else.
[4070.64 → 4071.28] Oh, initialism.
[4071.68 → 4072.16] Initialisms.
[4073.52 → 4074.24] That thing.
[4075.06 → 4078.66] Are they okay in technology to refer to specific technologies?
[4078.90 → 4079.48] Like, GCP?
[4080.50 → 4080.94] AKS?
[4081.30 → 4081.70] AWS?
[4082.22 → 4083.80] Like, should we get rid of those?
[4084.30 → 4086.66] I mean, we're never going to get rid of them.
[4086.66 → 4090.76] Because if someone said to me in my first week as a product manager, like, what is GCP?
[4091.36 → 4092.64] I'd be like, I don't know.
[4092.96 → 4095.12] Go product software?
[4096.92 → 4100.12] I mean, I would prefer if people just had boring names for things.
[4100.24 → 4101.42] Like, Google's cloud, right?
[4101.46 → 4103.72] They have boring names for all of their stuff.
[4103.82 → 4109.70] Whereas Amazon is just like, like, there's that, what's that thing that was the meme on Twitter?
[4110.34 → 4110.66] AWS?
[4111.10 → 4111.92] I don't remember what it was.
[4111.92 → 4118.58] But there was this thing that was like, that sounds like a perfectly legitimate, like, Amazon product.
[4118.86 → 4124.38] But it was just like this massive post on Twitter of just like, I could just make up something.
[4124.52 → 4126.24] And then it was a thing that people were talking about.
[4126.62 → 4132.36] So it's like, if you are going to use fancy language, at least make it, like, plain and simple and boring.
[4133.50 → 4137.86] Amazon is getting a little too overboard with their product names.
[4138.30 → 4141.12] I'm like, start off simple.
[4141.12 → 4145.40] They were just like, you know, I prefer EC2 and S3 to like Aurora.
[4145.72 → 4148.22] Like, what does that have to do with databases?
[4148.66 → 4148.98] Like, what?
[4149.38 → 4151.54] I'm on the bandwagon for boring names.
[4151.84 → 4153.64] Clear, simple, boring names.
[4153.78 → 4155.04] So we all know what's happening.
[4155.34 → 4158.20] So Chris, our startup, it's called Bob.
[4159.48 → 4160.12] It's called Bob.
[4162.06 → 4165.34] Thank you so, so much for joining us.
[4165.38 → 4166.88] It was a pleasure having this chat.
[4167.00 → 4168.10] I wish we could talk more.
[4168.10 → 4174.54] I've had a million and two brainwaves of different things I want to chat about with you both, which I probably will.
[4174.76 → 4176.12] Look out for a coffee invite.
[4177.02 → 4178.66] Unfortunately, I'm going to have to go.
[4179.08 → 4179.74] Thank you all.
[4179.86 → 4180.76] Thank you all who listen.
[4181.14 → 4187.10] Thank you who are listening live in a week, in a month, in a year.
[4187.62 → 4188.70] This has been Go Time.
[4188.70 → 4195.44] Thank you for listening to Go Time.
[4195.62 → 4199.76] We have a bundle of awesome podcasts for you at changelog.com.
[4199.94 → 4203.64] That includes our brand-new show, Ship It, with Gerhard Leon.
[4203.92 → 4208.36] A podcast about getting your best ideas into the world and seeing what happens.
[4208.62 → 4212.60] It's about the code, the ops, the infra, and the people that make it happen.
[4212.60 → 4217.00] Yes, we focus on the people because everything else is an implementation detail.
[4217.26 → 4223.22] Subscribe now at changelog.com slash ship it or simply search for Ship It in your favourite podcast app.
[4223.32 → 4223.82] You'll find it.
[4224.02 → 4227.44] And of course, the galaxy brain move is to subscribe to our master feed.
[4227.60 → 4231.80] It's all changelog podcasts, including Go Time and Ship It, in one place.
[4232.12 → 4236.96] Search changelog master feed or head to changelog.com slash master and subscribe today.
[4237.44 → 4241.12] Go Time is produced by Jared Santo with music by Break master Cylinder.
[4241.12 → 4244.32] We're brought to you by Vastly, Launch Darkly, and Linde.
[4244.60 → 4252.00] Next time on Go Time, the author of 100 Go Mistakes and How to Avoid Them joins Matt, Mark, and Johnny on the show.
[4252.42 → 4255.06] Mistakes will be made, so stay tuned for that.
[4255.20 → 4256.52] We'll have it ready for you next week.
[4271.12 → 4301.10] We'll be right back.
[4301.12 → 4301.52] We'll be right back.
[4302.26 → 4303.88] We'll be right back.
[4303.88 → 4304.88] We'll be right back.
[4305.40 → 4306.92] We'll be right back.
[4313.14 → 4315.26] You all right back.
[4316.08 → 4316.48] We'll be right back.
[4316.66 → 4317.00] We'll be right back.
[4317.00 → 4318.96] We'll be right back.
[4318.96 → 4320.84] We'll be right back.
[4320.84 → 4322.40] We'll be right back.
[4322.78 → 4323.40] We'll be right back.
