[0.00 → 19.00] Welcome to Request for Commits, a podcast that explores different perspectives in open
[19.00 → 23.72] source sustainability. On this show, we talk to people about the human side of code. We
[23.72 → 28.12] cover everything from community and governance to businesses and licensing. If you've ever
[28.12 → 32.70] wondered how open source projects get started, survive, die, or flourish, then you're going
[32.70 → 38.14] to love this show. I'm Nadia Elba. And I'm Michael Rogers. On today's show, Michael and I talk
[38.14 → 43.24] with Max Ogden, creator of DAT, an open source decentralized tool for distributing datasets.
[43.72 → 47.78] Max has also done a lot of work in the Node.js ecosystem, including help start Node School
[47.78 → 52.36] and publishing hundreds of modules at NPM. He was also one of the first Code for America fellows.
[52.74 → 56.98] Our focus on today's episode with Max is around grant funding. We talked about how we figured
[56.98 → 60.32] out grants were right for developing debt and how he managed to find his first funders.
[60.62 → 64.52] We also get into the mechanics of grant funding. Max shared what it's like to work with grant
[64.52 → 68.08] funders and how to build those early relationships if you're looking for grants yourself.
[71.50 → 76.92] So Max, you have an interesting story in terms of how you ended up at Code for America. Can you
[76.92 → 82.50] tell us a little bit about how you ended up there? Yeah, actually, it was kind of fortuitous or random,
[82.50 → 88.30] at least to me at the time. Maybe it was all planned out. I have no idea. But I was attending
[88.30 → 92.72] an event around Auscon, which used to be in Portland every year. And they moved it down to Austin
[92.72 → 98.38] last year. But Auscon was kind of cool. I could never afford to go. But it was kind of interesting
[98.38 → 103.26] because it would bring all these open source people into Portland. And one year, there was like
[103.26 → 108.30] a civic apps competition here in Portland that I was participating in. It was the city was trying to
[108.30 → 116.44] get people to use their open data. And so I was at an award ceremony for that and received like an
[116.44 → 122.08] award for some civic app that I had made. I had a thing called the PDX API that took the data sets
[122.08 → 129.48] from the city of Portland and made them accessible to developers. And in the audience was Tim O'Reilly,
[129.74 → 134.54] who, you know, owns O'Reilly Books and runs Auscon. And he came up to me afterwards, and he goes,
[134.54 → 139.66] hey, we're starting this new thing called Code for America. Here's my card. You should definitely
[139.66 → 145.12] apply to be a fellow. And this was about like nine months before the first Code for America
[145.12 → 151.98] fellowship term started. And so I was just like, holy cow, this is crazy. I had to, I started talking
[151.98 → 156.82] with the Code for America folks and applied for the fellowship and then got the fellowship, had to quit
[156.82 → 163.36] my job and then move to California. And so it was like a big, it was like a very quick succession of
[163.36 → 168.86] events that I didn't see coming that totally changed my life. Definitely. In many ways. So
[168.86 → 173.16] it was kind of just like this one. I mean, I guess it was, it seemed random to me at the time, but
[173.16 → 176.68] because I was in the right place in the right time kind of thing.
[177.36 → 181.92] I actually met you when you got that award. I was at the same thing. And that was the first time
[181.92 → 185.36] that I met you, and you were like 19 or 20 at the time, but you still had that giant beard.
[187.46 → 190.58] Nice. I didn't realize that you were there. That's crazy. I never knew that.
[190.58 → 195.84] Yeah. Yeah. We were there with Jay Chris and talked about Couch TV stuff and, and the upcoming
[195.84 → 200.70] event, the upcoming couch camp thing that we were going to do. Max is actually the first person
[200.70 → 204.72] to buy a ticket to the first event that I ever ran in 2009.
[206.12 → 207.04] Way to go, Max.
[207.52 → 212.30] Yeah. And I remember when I first went to Oakland's right after I moved down to the Bay Area,
[212.90 → 216.04] or maybe I visited the Bay Area ahead of time, but basically the first person I met up with
[216.04 → 221.84] was Michael. We like, I, he had like biked to a really cool coffee shop, and I was like,
[221.90 → 225.82] whoa, Oakland is awesome. And then I ended up living there for four years. So a lot of
[225.82 → 228.08] transformative things happened for me in 2010.
[229.54 → 235.14] Can you talk about that a little bit? Just sort of like how, I think you're at a startup
[235.14 → 239.70] before you were at Code for America. And it sounds like Code for America just helped you think about
[239.70 → 244.76] different applications of code and ways you hadn't necessarily done before, for work.
[244.76 → 251.00] Yeah. Before that I was working at a great team at a company, but the product wasn't anything
[251.00 → 258.14] that I was like passionate about. It was qualitative market research. And so it's just kind of boring.
[258.64 → 263.24] I didn't really, I didn't feel strongly about helping companies target their products or whatever.
[264.50 → 271.66] But I got super lucky because the team was super supportive, and it was a perfect place for me
[271.66 → 276.06] as a college dropout to learn all the things that I needed to learn to be a functioning,
[276.68 → 282.92] contributing programmer to society. And so I really feel like I got, like nowadays, I feel like I was
[282.92 → 289.84] ahead of the curve. This was like the mid 2000s, late 2000s. I was a junior programmer and I, and like
[289.84 → 293.98] the dream of a junior programmer is to get on a team where you're supported and mentored and given
[293.98 → 300.14] challenges and not expected to, you know, work weekends and like all this kind of thing. And Portland is
[300.14 → 305.32] pretty cool because the culture here is very family oriented and like personal oriented and
[305.32 → 312.52] not about, you know, like working for your company at all costs. And so I feel like now I'm ahead of
[312.52 → 315.62] the I was ahead of the curve then because now I talked to junior programmers, and they're like,
[315.70 → 319.38] Oh, I wish that I could get any job where I'm like supported and mentored, but there's like no
[319.38 → 324.14] jobs available for that. And there's this huge influx of people coming in. And I don't think a lot of
[324.14 → 328.68] companies know how to mentor people. So I'm just like incredibly grateful that I had an awesome mentor
[328.68 → 335.82] early on. So shout out to Dan Herrera. If he's, if he's listening, he taught me everything that I
[335.82 → 341.40] know. That's a really lucky opportunity. Yeah. Yeah. That's awesome. Uh, so like when you did
[341.40 → 347.24] the X API, one of the one of the premises of it was sort of, uh, don't try to provide data to
[347.24 → 351.06] developers and something that they can understand, just give me the data, and I'll make it accessible
[351.06 → 355.88] to developers. Um, which was interesting because you didn't have a lot of kinds of inroads with the
[355.88 → 360.40] people publishing the data at the time. Um, but when you went into code for America there,
[360.40 → 364.62] you're sort of paired with a municipality, and you're working with the government to,
[364.62 → 368.20] to kind of produce something. Can you tell me a little bit about what that transition was like?
[368.20 → 373.48] So rather than just sort of pushing something to developers, um, that you get over a wall,
[373.48 → 379.00] but actually working with the civic governments. Yeah. And, uh, the human side of code, I think is
[379.00 → 385.26] that I learned through that process was like previously, I think you nailed it in the question.
[385.26 → 391.16] Actually, previously I was sort of an outsider. I was a volunteer and I didn't feel like I could
[391.16 → 394.32] actually influence the things that the people that were working for the government could do.
[394.40 → 400.16] Technically, I just assumed that their process was set in stone and that, um, they weren't interested
[400.16 → 405.76] in me as some random person, um, who wasn't, you know, official and wasn't paid to help them.
[405.76 → 411.26] Um, and so I just did what I could. I took their data and tried to make it more useful on the outside.
[411.92 → 416.26] Um, but I think that the stroke of genius in the model of code for America, which I think, I mean,
[416.26 → 422.84] they, they copied teach for America, which is, um, like very, it's very overtly modelled on that.
[423.10 → 427.76] And I think that the teacher America model is you embed people. And the code for America model is
[427.76 → 433.32] also about embedding. And, uh, the one of the really cool things about the code for America program
[433.32 → 439.10] was you show up and the first week is about, um, understanding government culture and how you can
[439.10 → 443.96] be an agent of change to show them like alternate alternative ways of doing things with technology,
[443.96 → 450.06] but an emphasis that it's not technical. It's like a human problem. Um, or it's a lot of social
[450.06 → 455.48] problems and sort of incentives problems. And we actually had like a negotiation workshop, which
[455.48 → 460.26] is, was really, really useful. I still use the principles that I learned in that, like every day.
[460.26 → 467.30] Um, I had thought negotiation was, was about, um, like if somebody is trying to detonate a bomb or
[467.30 → 471.72] something, you like to have to talk them down off of a ledge, but it turns out that negotiation is just
[471.72 → 477.20] like, if you're talking to anyone in your day-to-day life, and you're trying to be nice to them, like,
[477.26 → 481.16] that's what negotiation is about. It's about like having respect for other people's points of view and
[481.16 → 487.36] coming to like a positive outcome. So the fact that code for America didn't have us do like, you know,
[487.36 → 491.26] like a bunch of technical things on our first week, but instead they had us talk about being
[491.26 → 496.88] change agents and being like effective negotiators, I think speaks a lot to how they knew that it was
[496.88 → 503.26] essentially about embedding us inside of government and having us kind of like inspire people, um,
[503.26 → 507.80] with new ideas and have like an influx of, um, like crazy ideas that came out of it.
[508.40 → 513.46] So the thing that it, at the end of it, like, so going into it, I thought it was a technical thing.
[513.46 → 518.66] I thought I was going to be like, okay, I'll go make a bunch of cool like APIs or whatever, or build a bunch
[518.66 → 525.76] of cool apps. And, um, then by the end of it though, I realized it was, uh, that people inside
[525.76 → 531.62] government aren't exposed to ideas like open source as much, um, because the hiring and the procurement
[531.62 → 537.40] systems are essentially broken. So they don't have, I mean, they just don't have any way to get the like to compete
[537.40 → 542.60] with talent for people that go and work at Google or whatever. So by like the code for America model
[542.60 → 547.54] is you literally get people to quit their jobs at Google for a year or like go on sabbatical and then
[547.54 → 552.62] you get them to become government employees. And so, um, I didn't come from Google. I came from,
[552.62 → 558.28] um, this like smaller company, but the general idea is just people from the like practicing people from
[558.28 → 563.66] the tech industry, um, get to go and do a year of public service. And so what was cool about it is that
[563.66 → 568.06] I actually became a government employee. I went through the ethics training at the city of Boston.
[568.06 → 573.24] I had a city of Boston.gov email address. Um, I mean, it was the whole shebang. I was like an
[573.24 → 578.76] official, um, employee in the mayor's office. And so that was actually really empowering for me because
[578.76 → 584.08] now I was on the other side of the wall, so to speak. Like when I was in Portland, I was just this
[584.08 → 588.76] random person that was like volunteering. Um, didn't feel like I had any power to actually change
[588.76 → 593.64] anything, but then now suddenly I was like a city of Boston employee. And so now I felt like
[593.66 → 598.48] my opinions were valid on things and I could like, you know, set up meetings with CIOs and
[598.48 → 601.62] talk to them about like, Hey, why are you procuring this horrible software? Why are you
[601.62 → 606.28] not trying to set up more open? Uh, or like, why aren't you procuring open source software,
[606.28 → 611.96] for example? So that was super cool. Just, I feel like it was a hack. Like they were hacking
[611.96 → 616.20] the code for America hacked two things at once. It like gave me a lot of confidence that I actually,
[616.86 → 621.42] like my opinions did matter because it made me feel like I was like the expert coming in and trying to
[621.42 → 627.26] help people understand that they don't have to buy horrible software and hire people with horrible
[627.26 → 631.34] credentials. They can actually, um, do things in a more progressive and modern open source way.
[631.38 → 637.40] But, and then also to them, it was like exciting because they had somebody coming in and, um,
[637.62 → 643.68] had a lot of excitement and enthusiasm. And I think I had, I definitely got a lot of people telling me
[643.68 → 648.06] they were surprised that they didn't make me shave to work in Boston city hall. I had a giant beard
[648.06 → 651.78] walking around Boston city hall. So it was like a bit of like a it was definitely a bit of a culture,
[651.98 → 659.10] culture change thing on purpose. Like it was the point of it was you go into, um, a city for a year
[659.10 → 663.08] and you try to make some cool things, but by the end of it, you don't just leave, and the things go away.
[663.56 → 669.14] The idea is that by the end of it, you've, um, given the city, like a different lens to view,
[669.14 → 674.60] like a process for developing software. So actually the hardest thing about it was we had to come up
[674.60 → 678.50] with a way of contracting for support for the open source apps that we did because they were
[678.50 → 684.46] deployed on, um, Heroku and they didn't know how to, uh, maintain Heroku services. And so
[684.46 → 688.96] it turned out that the biggest outcome of the entire thing was like, we now had a way,
[689.10 → 694.74] we like had to draft a new procurement policy for the city of Boston that let them support open
[694.74 → 700.56] source software, um, like have a support contract with an open source vendor. And that was like a
[700.56 → 704.56] totally new groundbreaking thing for them because usually the support contracts are built into
[704.56 → 708.84] these huge multimillion con multimillion dollar contracts. But the idea that they could have
[708.84 → 714.06] like a $5,000, um, open source support contract, just so that if the app went down, they had somebody
[714.06 → 719.84] that could, they could call to help them. Um, like it was like those kinds of small wins that actually
[719.84 → 725.48] were the long-lasting effects. Whereas going into it, I thought we were going to, um, I didn't know
[725.48 → 728.08] that procurement was going to be like the focus of all of our efforts.
[728.08 → 736.82] It's an awesome story. And you started, so that was 2011, right? And then you started debt a couple
[736.82 → 741.74] years later, right? Um, yeah. And I'm assuming some of those experiences ended up feeding into
[741.74 → 744.28] the kind of work you ended up doing moving forward.
[744.66 → 749.16] Yeah. Like in the last couple of months, um, when I was working at the city of Boston, I ended up, um,
[749.54 → 755.16] working on a bunch of different like little prototype applications and, um, we were working with the
[755.16 → 760.52] public school system. And so we ended up another big thing that we didn't see was how much time we
[760.52 → 766.56] spent talking to lawyers about student data, um, and learned a lot of things about what we can and
[766.56 → 773.68] can't use in terms of datasets to build applications, um, because of privacy issues. Um, and so it was
[773.68 → 779.28] like, uh, for the year-long fellowship near the end, I started working on kind of the thing that I had
[779.28 → 784.28] been working on in Portland, which was a better way to disseminate the data that the city had and
[784.28 → 791.00] make it available to people, um, to build things. And, um, so like data platforms sort of, and my,
[791.14 → 797.96] my motivating factor was, um, data is read only usually like when a city has data, data that they
[797.96 → 802.32] collect, they collect it for their own purposes. And then if they have an open data policy, they make
[802.32 → 807.14] it is available to people, but they don't make it available in like a GitHub way. They make it
[807.14 → 814.92] available in like a download our CSV way. Um, and so people, if they use the data and found errors
[814.92 → 821.26] in the data, or they wanted to clean up the dataset, um, like say that I'm building an application and I
[821.26 → 826.20] have users that are contributing data that the city might want to know about. Um, like for example,
[826.20 → 834.04] if I'm, uh, if I have like a running, like a jogging application and I have, um, a better data set that
[834.04 → 841.72] the city has of where the, the, um, jog gable paths are inside of parks, like, wouldn't the city want to
[841.72 → 848.70] know, um, like have higher quality data about where the pathways are versus their like, um, potentially
[848.70 → 853.26] out of, out of date dataset. So like the idea of having the dataset be read, right. Was like a
[853.26 → 858.64] motivating factor for me, but there wasn't any, um, there were, there's basically no like version
[858.64 → 863.10] control tool for datasets that was out there. And so I started kind of like going down that rabbit
[863.10 → 867.92] hole a little bit. And then I was like, Oh, this is a huge project. It's going to take a lot of time.
[868.00 → 873.42] So then I didn't work on it after the fellowship for about a year or maybe like a year and a half.
[873.52 → 878.30] And then I was like, Oh, nobody's doing this still. I should probably do it. And then I started
[878.30 → 882.36] pursuing the idea of debt, like more as like a full-time thing.
[882.36 → 887.78] So it sounds like the Genesis of it was around, uh, government data, but the project now is mainly
[887.78 → 893.40] focused on like scientific data and scientists. So like, how did that transition get made?
[893.78 → 899.30] Um, it was actually also kind of this fortuitous meeting. I had gone to the Mozilla festival,
[899.86 → 905.94] um, which is an awesome festival. It's basically like nine conferences at once in this big building
[905.94 → 910.22] in London. And it's all these different open knowledge, open culture, open science, open source,
[910.22 → 915.14] open journalism, open data. It's like all of these different, awesome overlapping communities.
[915.96 → 923.74] Um, so I went to this thing and I had, um, I had like a prototype of debt, um, that I had developed.
[923.92 → 930.38] And then, uh, I think I gave like a lightning talk on it or something. And this, uh, grant officer
[930.38 → 936.44] from a foundation actually came up to me who was at the conference. And he said, um, Hey,
[936.44 → 941.78] I saw that you were doing stuff around, uh, dataset sharing and, you know, better tools for
[941.78 → 947.48] syncing data, datasets. Um, and you're, you're working on government. Have you ever thought
[947.48 → 953.58] about scientific, um, users? And I was like, well, I think science is really cool, but I,
[953.86 → 959.02] you know, I'm a college dropout, and I've never, I have no credentials and I don't really know.
[959.02 → 964.56] Um, and he's like, well, I think it's the same. He actually kind of like said, I think that what
[964.56 → 968.66] you're doing is exactly what a lot of scientists need right now, but you don't know it yet.
[969.48 → 973.78] And I was like, Whoa, okay. That's interesting. And I think he ended up being totally right.
[974.02 → 979.64] And so the funder actually approached me and convinced me to work on their, like, um,
[980.14 → 985.50] their like social issue, so to speak. I thought that that was fascinating that, um, just getting
[985.50 → 989.58] a prototype out there and going to the right conference where you have this interdisciplinary
[989.58 → 994.76] crowd, um, and kind of saying like, Hey, like declaring to the world, like, Hey, I'm working
[994.76 → 999.92] on this thing. Here's like a demo or here's like a prototype for me. It worked out because somebody
[999.92 → 1004.78] said, Oh, I totally need that. But it's in this area that you don't know that you should be working
[1004.78 → 1011.20] on yet. And it helps that they were also a person that could write grants. So that was kind of like,
[1011.20 → 1016.56] that was another moment that totally changed the course of like my last four years was like this
[1016.56 → 1022.48] one chance meeting at the Mozilla festival. And I think it was 2013. Awesome. Um, we're about to
[1022.48 → 1028.26] head to our break, but when we return, we'll dive into the grant process and, um, some of the more
[1028.26 → 1037.58] organizational aspects. Hey everyone, Adam Stachowiak here, editor-in-chief of Changelog. And if you're
[1037.58 → 1046.30] looking to hire the best freelance talent out there at the top.com that's top.com power, the top 3%
[1046.30 → 1053.42] of freelance talent out there, the world's best developers and designers, white glove service, risk
[1053.42 → 1060.06] free trial. That means that if you're not happy, you do not pay. You can hire developer, you can hire
[1060.06 → 1065.66] designer, you can hire both. If you need to scale your team, this is the place for you to get started,
[1065.66 → 1072.78] head to top.com that's T O P T A L.com. Tell them Adam from the change log sent you. They'll take
[1072.78 → 1079.26] great care of you. If you'd like a more personal introduction, email me, Adam at change log.com.
[1087.42 → 1092.94] All right, we're back with Max Ogden of the DAT projects, and we're talking about grant funding.
[1092.94 → 1098.38] So I'm curious, Max, uh, when you started doing this, it sounds like your sort of fell into this
[1098.38 → 1103.50] fortuitous meeting with a grant funder, but how did you know that grant funding was right for you
[1103.50 → 1108.94] with this project? Why didn't you just build that in your spare time? Um, so I would give a lot of
[1108.94 → 1113.98] credit to the Knight Foundation. They have been doing a lot of work to try to make grant funding less
[1113.98 → 1119.02] scary. Um, one of the things that they've done is they, which I was, I think I was the first person
[1119.02 → 1124.30] that got one of these, um, just because of like a right place, right time kind of thing. Um, it was
[1124.30 → 1130.14] called the Knight prototype funds. And usually cause their grants are, um, multi-year commitment and they
[1130.14 → 1134.62] take a lot more work up front because you're planning kind of waterfall style for this multi-year period.
[1134.62 → 1139.66] Um, that's like the traditional, um, kind of grant structure is you're doing these bigger projects.
[1140.30 → 1145.02] And Knight said, um, it takes, if it takes three years to evaluate if something worked or not,
[1145.02 → 1151.10] that's kind of a long turnaround time. So instead they came up with a prototype, and it's, uh, originally,
[1151.10 → 1156.38] it was $50,000 for six months for one person to make a prototype of something and test an idea out.
[1156.86 → 1161.50] And then they revised it. And I think now it's $30,000. So it's kind of like a part-time, um,
[1161.50 → 1166.22] full-time or part-time kind of like, if you don't have the time to quit your job, or you don't
[1166.22 → 1170.22] want to make a like a huge risk doing like a multi-year thing on something that you're not
[1170.22 → 1174.78] sure about yet, or they even want you to take the prototype and develop it into a full grant.
[1174.78 → 1180.30] That's kind of how they see the pathway going. So I think that progressive thinking around, um,
[1180.30 → 1185.02] smaller funding is fascinating. And I think Knight, the only reason that I got into this was
[1185.02 → 1189.50] because I could start small and because I didn't know enough to write a huge grant at the beginning,
[1189.50 → 1193.50] or I mean, huge meaning more than one person for six months.
[1193.50 → 1198.86] Yeah, definitely. I want to like explicitly plug the Knight prototype thing. Because I think that's like,
[1198.86 → 1203.90] I've heard perfect experiences around it. Um, and I think we'll get into it later,
[1203.90 → 1207.74] but just sort of like why grants are so scary to people. I think part of it is that you have these
[1207.74 → 1213.98] like enormous, uh, amounts of money or these like multi-year commitments. And so I really like that
[1213.98 → 1216.78] that one is much shorter and smaller amounts of money.
[1216.78 → 1221.10] Yeah. So let's get into that a bit, like in deconstruct this, like what is grant writing?
[1221.10 → 1222.62] Like, how does this even work?
[1224.14 → 1228.86] I probably have a different answer than a lot of people. Um, because there's the word grant is,
[1228.86 → 1234.62] you know, it could mean government grants. It could mean, um, EU, EU grants. Um, I've noticed,
[1234.62 → 1242.54] I have a someone that I work with that's in Denmark. Um, and the they don't have this phenomenon of
[1242.54 → 1247.98] like eccentric billionaires that are either alive or dead that give away all their money through a
[1247.98 → 1252.46] trust because they're trying to evade taxes. And so they set up like a giant charitable trust,
[1252.46 → 1257.58] like Howard Hughes. Uh, I think it's the third-largest endowment in the world that was started
[1257.58 → 1262.06] at. So Howard Hughes could hide his tax money from the U S government. And then when he died,
[1262.06 → 1266.70] um, there was all this money. And so they're like, oh, we could start a medical institute and make grants
[1266.70 → 1271.98] with it. Um, and they actually run an entire neuroscience research facility off of the income,
[1271.98 → 1277.26] like the accrued interest or whatever on the, the original endowment, because there's just so much
[1277.26 → 1282.22] money in that thing. So that's kind of like an American thing is the philanthropic private
[1282.22 → 1287.42] foundations that are like these eccentric, mostly white male, rich billionaire people are all of our
[1287.42 → 1292.22] grants have been, uh, dead rich billionaires. However, there are also alive, rich billionaires,
[1292.22 → 1296.86] um, such as Bill Gates. So that, but that, that's totally, I didn't realize, but that's totally
[1296.86 → 1301.10] American phenomenon in the in Europe, they have a functioning government that makes grants. So
[1301.82 → 1306.62] most of the grants, like in say that you're Danish and you want to go get a grant, like,
[1306.62 → 1311.42] because everybody pays so many taxes, and they don't have as much private philanthropy,
[1312.06 → 1315.02] you end up getting your grants from the government, but they have like way more developed
[1315.02 → 1319.66] government grant programs in the U S when you get a government grant, it's usually like huge
[1319.66 → 1323.66] and you have to be a pretty big institution. So those are actually pretty intimidating. Um,
[1323.66 → 1328.06] I don't think I'll ever get a U S government grant. I think that I could get an EU grant if I
[1328.06 → 1332.86] was an EU citizen doing what I do now because they're targeted at smaller things. A lot of the time,
[1332.86 → 1335.66] the EU grants also get a lot bigger. So it kind of depends on where you're at.
[1336.22 → 1341.02] Um, so that's the first thing is like, don't expect, like if you've heard one person's grant
[1341.02 → 1346.22] experience, like there's probably way different levels of grants. Um, so just learning how to
[1346.22 → 1351.90] navigate like which grants you actually want to go for, um, is like the first step. Um, but also,
[1352.46 → 1358.54] uh, I think that to me, it's not about the grant writing. Um, the grant writing happens once you've
[1358.54 → 1363.42] developed the relationship with the person that you're writing the grant for. This is like, if you
[1363.42 → 1369.66] don't take anything away from this entire interview, um, I would say that if you want to go down the path of
[1369.66 → 1375.74] getting grant money for open source, you have to start building the relationships now. And it takes years of
[1375.74 → 1380.94] time to develop those relationships. So that's the biggest disappointment when I talk to people
[1380.94 → 1385.90] about like, because people are like, okay, I could go get VC and try to start like a company that does
[1385.90 → 1389.82] this open source thing and then figures out a way to make money off of it. And what's really cool about
[1389.82 → 1396.46] VC is you get money like really quickly. Um, but then you have to like down the road, make these
[1396.46 → 1402.70] compromising decisions where you have to weigh like your values across against like the shareholder
[1402.70 → 1409.10] income returns and stuff like that. So with grants, you don't get money quickly, you get money slowly,
[1409.10 → 1414.46] but then you never have to make you do. Yeah. And sometimes very slowly. Um, but the cool thing
[1414.46 → 1421.98] about it is you never have to make those like, um, judgment calls. Like you're, you're always working
[1421.98 → 1427.66] on what you want to be working on because you had to go through this process that you've like through the
[1427.66 → 1433.34] grant process to me is finding somebody that trusts you and then writing like the grant itself is the
[1433.34 → 1437.50] thing. That's like the contract between you and the funder. That's like, here's the mission that
[1437.50 → 1443.02] I'm working on. And they're never going to be like, um, like I haven't had any experiences like this,
[1443.02 → 1448.38] at least I think some people have had this happen to them, but I guess I've been lucky. I've never had
[1448.38 → 1454.06] the funder come to me and say, Hey, change what you're working on. Um, like we, you have to do
[1454.06 → 1459.26] this now. It's not like they have, um, I, I at least don't feel like they have influence over my
[1459.26 → 1464.30] day-to-day direction because like I've already upfront established like what it is that the
[1464.30 → 1469.10] mission is. And they basically just give you money for a time window so that you can pursue
[1469.10 → 1473.02] that mission. And all they want at the end of it is to know what happened and what went wrong.
[1473.82 → 1479.58] So they want like a report. So it's like, you end up doing a grant. That's a grant right up at
[1479.58 → 1483.02] the beginning. That's like the pitch. That's like, here's what I want to work on. Can we agree?
[1484.06 → 1489.90] But, and then you do a report like in the middle and at the ends. Um, but that all actually comes
[1489.90 → 1496.46] after you spent a lot of time finding the right foundation in the U S for example, find the foundation,
[1496.46 → 1502.86] building the relationships. Um, and ideally you want the funder to, um, like approach you and say,
[1503.02 → 1509.74] Hey, it would be really cool if you applied to us with this idea. Um, so that process is
[1510.54 → 1514.94] probably, uh, people have different ways of doing it. For me, it was, I worked at Code for America,
[1514.94 → 1521.58] which was funded by, I think like six foundations. Um, Code for America was pretty well funded in the
[1521.58 → 1527.42] private foundation space. And, uh, I also, because I was working at Code for America, that was the year
[1527.42 → 1533.18] that I got, um, I got to start doing open source full-time, um, because Code for America encourages
[1533.18 → 1538.78] all the fellows to do open source for everything so that it can be reusable. And so because I was
[1538.78 → 1542.46] doing open source full-time, I started getting more involved in open source communities. And I started
[1542.46 → 1547.82] going to more events like community events and meeting more people and networking. And so the
[1547.82 → 1553.34] combination of working for a nonprofit that was grant funded and going to events, um, in that
[1553.34 → 1559.10] ecosystem, um, meant that I met funders face to face. And I can't stress how important that is.
[1559.10 → 1563.98] Like if, um, like I said, like, if you take one thing away from this entire thing, it's that
[1564.78 → 1569.82] don't go to like, you're not going to, I mean, I love Scoff for example, and I love Nodemon,
[1569.82 → 1574.70] but you're not going to meet like people from the Knight Foundation at a JavaScript conference.
[1574.70 → 1579.98] Like you meet them at, uh, like I used to go to this conference called the civic media conference,
[1579.98 → 1585.66] which was the MIT would host it. And I was living in the city of Boston for, um,
[1585.66 → 1590.14] the code for America fellowship. And when you go to a conference, that's like about, uh,
[1590.14 → 1593.82] it can still be a technical, technically focused conference or like a technology conference,
[1593.82 → 1598.22] but when it's focused on a specific issue, like the civic media conference is about like the way
[1598.22 → 1603.18] that information is used in society. It's kind of like this high level idea, but at least it's like a
[1603.18 → 1608.22] particular like social direction. When you go to those kinds of conferences, you, you immediately start
[1608.22 → 1612.38] meeting other people that are funded by grants, or you meet the people that make the grants,
[1612.38 → 1619.18] like the foundation people. So I think that the key to grant funding is not just looking at it
[1619.18 → 1623.66] through a technical lens, but looking at it through a holistic lens of like, what am I actually going
[1623.66 → 1627.74] to do with the technology? And then finding out the events for that and going to those events and
[1627.74 → 1632.46] then meeting the people. And then once you have the relationships, um, then the rest of it,
[1632.46 → 1636.54] the actual grant writing process starts. But I don't think if, I think if you start,
[1636.54 → 1639.98] start writing grants without any of those relationships, you'll have like nine out of
[1639.98 → 1643.82] 10 grants won't get approved. I would echo that like, yeah, a thousand percent.
[1644.86 → 1647.74] Um, it's actually, it's fine. Like even hearing you talk about it, um,
[1647.74 → 1652.06] it reminds me a lot of venture capital. Um, and the advice is really similar, which is
[1652.54 → 1657.98] like to build real relationships with investors. Um, ideally you want them coming to you saying,
[1657.98 → 1663.02] this is a really great fit for us. Um, versus just sort of like cold applying to an email
[1663.02 → 1668.22] address and hoping that someone will get back to you. And I think you did a great job just
[1668.22 → 1673.34] sort of deconstructing how some of that could be less scary than you think, but that, yeah,
[1673.34 → 1679.90] I mean, meet them where they're at and go to events where they are or find, um, like the way I got
[1679.90 → 1686.22] my forward funding was through a mutual connection. Um, and I wasn't even looking for funding, but I just
[1686.22 → 1690.94] sort of explained what I was doing. And that person was like, oh, I know who you should be talking to.
[1690.94 → 1694.86] But I think there's sort of like this running theme, even in this conversation around
[1695.66 → 1701.58] intersectionality and going sort of like out of your own sector to get inspiration from different
[1701.58 → 1706.70] sectors, which is both creatively stimulating, but also just allows you to meet people outside
[1706.70 → 1712.62] like your most say like technical network. I think that's really important. Yeah. Yeah. I mean,
[1712.62 → 1717.34] you mentioned, you know, you've gotten a lot of grants, and they seem to be stepping up in terms of
[1717.34 → 1721.42] the amount of money that you're getting over time. Um, I'm wondering if you could just walk us
[1721.42 → 1725.74] through like the grants that you've gotten and any changes that may have happened to the project or
[1725.74 → 1730.62] changes in direction that you may have gone down in order to get those grants or to work with those.
[1730.62 → 1734.38] Cause you said that, you know, you're not changing mid-course, but it does seem like if you're,
[1734.38 → 1738.38] if you're now going from, you know, a $500,000 grant to like a $3 million grant,
[1739.42 → 1744.62] lining up with their goals in the beginning might shift, um, some of the project direction a little bit.
[1744.62 → 1750.62] Mm-hmm. Um, so I've got four grants to dates, um, and working on a fifth, but I can't really,
[1750.62 → 1756.06] um, that one's not like done. So I can't really talk about that one. Um, not that I'm trying to
[1756.06 → 1762.06] be transparent or not that I'm, I want to be transparent as much as I can, but, um, I grant
[1762.06 → 1765.90] people like to wait until it's announced so that there can be like a PR thing. So I can't really
[1766.54 → 1770.14] announce that one. Because you want to be open, but you also want to get down here, right?
[1770.14 → 1775.58] Exactly. Exactly. So I just want to be clear though, that I am very pro transparency. So if
[1775.58 → 1780.06] anybody listening, like has questions that I didn't cover, like, feel free to email me or DM me on
[1780.06 → 1785.58] Twitter, and I'll like, you know, I can send you my budget and everything like that. So the four
[1785.58 → 1790.46] grants that I've got, um, the first one was the prototype and that was $50,000, and it was for me
[1790.46 → 1795.90] to work for six months on the prototype of debt. And I basically, the Knight Foundation said, Hey,
[1795.90 → 1799.34] you were working on this stuff at code for America. You never really continued working on it.
[1799.90 → 1805.26] Um, we have this new thing, the prototype grant. We are wondering if you're interested in, um,
[1805.26 → 1809.82] building a prototype of that stuff that you never got a chance to finish working on a code for America
[1809.82 → 1816.06] and just kind of see what happens. And so I was like, okay, awesome. That's like $50,000 to work on
[1816.06 → 1821.50] an open source project is pretty cool. So I did that and it was just me. And then, um, that was like in the
[1821.50 → 1828.06] summer of 2013, I think. And then I went to Modest that winter, and it was like at the tail ends.
[1828.06 → 1832.54] So I was like, okay, I'm about to have to go figure out what I'm going to do next. But then I met this
[1832.54 → 1838.54] funder from the Sloan Foundation, whose name is Josh Greenberg. And, um, Josh basically is the person
[1838.54 → 1844.62] who came up to me and said, Hey, have you thought about working on scientific stuff? Um, so, so far I'm
[1844.62 → 1849.26] like two for two. I had the foundations like to come to me and find me and say, do you want to work on this
[1849.26 → 1853.66] stuff? Because I had, I mean, at that point I had invested years of unpaid open source work
[1854.38 → 1859.34] into the ecosystem or like a code for America. I actually took a pay cut to move to San Francisco.
[1859.34 → 1865.66] So, um, I mean, it doesn't really make a lot of sense financially up until this point. And it's
[1865.66 → 1869.98] still, I mean, I still, I would, I want to be clear. I could make like twice as much. I'm not being
[1869.98 → 1874.54] arrogant. I'm just, I can make twice or three times as much working at a startup than I do now.
[1874.54 → 1881.42] Um, but relative to nonprofits, I think I make more than average. So at first I was,
[1881.42 → 1887.26] I think 50 K for six months was about the same burn rate that I have now. So actually everybody
[1887.26 → 1893.26] on my team makes $96,000 a year because that's, um, $8,000 a month, which makes the, the grant
[1893.26 → 1898.62] forecasting really easy. Um, so all full-time employees right now, we, we all make $96,000 a
[1898.62 → 1903.58] year, which is if you talk to tech people, that's like really low. But if you talk to nonprofit people,
[1904.30 → 1908.30] it's, um, above average. So it's kind of like, we tried to strike a balance between
[1908.94 → 1914.30] not making tech people not want to have the jobs, but at the same time, like supporting people.
[1915.18 → 1923.26] So the first grant was six months. The second grant, I think it was $260,000 for a year. And so that was
[1923.26 → 1929.10] because I basically said, Hey, I don't want to work on this alone. I need, um, a team. And so
[1929.10 → 1934.86] then I was able to hire two people. So that was a huge moment for me was going from, um, and I remember
[1934.86 → 1940.54] I had discussions with, um, my partner, Jessica at the time. And I was like, well, I'm working on this
[1940.54 → 1945.10] thing alone and it kind of sucks. Because I don't have any coworkers, and I've been doing it for a while.
[1945.10 → 1950.78] And it would be awesome if I had, you know, people like teammates. And so I remember when I,
[1951.58 → 1957.42] when I got that first Sloan grant, it was huge because, um, now I could actually like start
[1957.42 → 1962.38] building a team up, then it would, the project went to three people. And so after a year, um,
[1962.94 → 1969.66] and so we got the Sloan grant and what happened was Josh said, um, I want to pay you so that you
[1969.66 → 1974.94] prioritize scientific use cases, because if we don't pay you, like he basically justified the
[1974.94 → 1981.90] grant as if he doesn't pay us, then we're going to go like find funding from other sources to focus
[1981.90 → 1987.26] on other problems. But he wanted to like to prioritize us to work on his issue, which was, um, scientific
[1987.26 → 1994.06] reproducibility. So I haven't really said anything about that yet, but, um, the TLDR on that is, um,
[1994.70 → 1999.42] when scientists publish their work online, it's important that other scientists are able to access
[1999.42 → 2004.62] the paper that they wrote and also all the underlying data and code that they use to produce the papers.
[2004.62 → 2009.58] So that, um, like an actual collaborative process can occur or like a fact checking, um,
[2010.22 → 2014.86] peer review sort of process can occur. So essentially like all the public money that
[2014.86 → 2019.50] gets poured into public research, it's important that all of those research outputs are saved forever
[2020.14 → 2025.10] so that, um, science can still happen in the future. But what happens today is that the data
[2025.10 → 2029.74] like never gets shared, or if it does get shared, the link breaks and then nobody can find the data
[2029.74 → 2033.90] set, or the researcher moves to a different university. And it was like on a hard drive
[2033.90 → 2037.66] that nobody knows where it is anymore because the person's not working there anymore. So
[2038.70 → 2043.58] there's just a lack of good solutions in this space around ensuring that the data that underlies
[2043.58 → 2048.38] research is still available, um, or available at all in the first place.
[2048.38 → 2054.70] So that's like the mission of the Sloan foundation is, um, among other things, I think that there,
[2054.70 → 2059.50] you may have heard their slogan. If you listen to other podcasts there, let me try to channel it.
[2059.50 → 2064.30] It's like the Alfred P Sloan foundation supporting the furthering of science and technology in the
[2064.30 → 2066.86] modern world or whatever. So that they're like very science focused.
[2066.86 → 2069.82] Uh, now we're proper like NPR podcast.
[2069.82 → 2075.26] Yeah. Maybe they'll find this podcast now. Because they'll be like, Hey, you said the thing now we'll
[2075.26 → 2080.70] give you money. Uh, so there's, I mean, they're very science focused, and they are very clear about
[2080.70 → 2084.22] saying we want to prioritize you to work on science. And I actually thought that was cool
[2084.22 → 2090.46] because I think science is cool. So what happened was we had, uh, this, this like first one year grant
[2090.46 → 2095.74] that established the team. What we had to do was make a commitment to working with scientists.
[2095.74 → 2101.18] And, um, but it, it was basically like an R and D project because nobody knew what the
[2101.74 → 2106.22] like solutions were like there basically, they only knew what the problems were. The problem was that
[2106.22 → 2111.34] no data is getting shared. They don't know what the solution is though. So we were kind of in a unique
[2111.34 → 2115.74] position where we had to figure out what we were building. And the only way that I knew how to do that
[2115.74 → 2121.58] was by getting embedded into the problem. And so the way that we wrote that first grant was,
[2121.58 → 2128.62] um, let's partner like grant people always want you to have metrics so that they can measure
[2128.62 → 2132.86] if you're slacking off or not, or if you're, you know, at the end of it, they can evaluate
[2132.86 → 2136.86] because they write a lot of grants. They want to be able to evaluate grants using like high level
[2136.86 → 2143.26] metrics. And so our metrics were let's partner with a certain number of labs. That was like our main,
[2143.26 → 2148.62] um, requirement was that we made a commitment. Like they're going to pay us. We're going to get people
[2148.62 → 2153.10] to work with directly with a certain amount of scientific labs and really try to understand
[2153.10 → 2158.46] their process. And so, and then at the end of it, we'll try to produce, um, some software that
[2158.46 → 2163.98] is usable by these people in order to change their workflows, um, or encourage like better data sharing
[2163.98 → 2169.74] workflows. And so it's actually really fun because in the grant was like, okay, we'll do like four.
[2169.74 → 2175.26] I think we said we'll do four really in-depth, um, partnerships labs. And so we got to work with
[2175.26 → 2182.14] astrophysicists, with, um, DNA researchers, um, with social scientists. It was like super fun because
[2182.14 → 2188.14] I got to learn a lot and I got to really like to challenge my notion of what data sharing was
[2188.14 → 2192.14] because I had stuff that worked for like city governments. But then when we went to work with
[2192.14 → 2197.18] scientists, they're like, well, my data is literally a million times bigger than that. Or, um, you know,
[2197.18 → 2200.78] I'm using this file format that no one else has ever heard of except the 19 people that
[2200.78 → 2206.70] like use this or whatever. And so it was like a lot of perfect challenges. And so for me,
[2206.70 → 2211.42] that was what the grant, that was like why the grant existed was nobody was working on these problems
[2211.42 → 2217.02] because, um, in science you're not paid to write software. And that's one of the big issues. I mentioned
[2217.02 → 2221.90] incentives earlier. I think grants are a great way to create new incentives because you just pay people
[2221.90 → 2227.18] and that's a pretty good incentive in public institutions like science and government. There's
[2227.18 → 2233.82] often not great incentives, um, to do things. So for example, it doesn't further your career
[2233.82 → 2238.38] in science. Like you're not going to, um, get a faculty position by writing open source.
[2239.02 → 2244.46] Um, you get a faculty position by getting published in a prestigious journal by writing open source.
[2244.46 → 2250.78] Like there's no prestigious journal that publishes open source. So that doesn't help you. So as a result,
[2250.78 → 2254.70] they never do it because it doesn't help. Right. But there is a fair amount of prestige,
[2254.70 → 2259.34] right. For developers to take on really hard problems. Like, like, I liked that aspect where
[2259.34 → 2263.82] he was saying, I want to pay you to do this so that like good people are focusing on hard problems.
[2263.82 → 2267.98] Um, I think like a lot of people are probably thinking, well, if you only have $96,000, you're
[2267.98 → 2272.86] not going to get great people. Um, but actually, I mean, you, you have some severely hard problems
[2272.86 → 2277.82] you've been working on, and you've gotten some really amazing people to, to work on them. I don't think
[2277.82 → 2282.54] that people really appreciate the scope of some of the technical problems in that. Um,
[2282.54 → 2286.86] Speaker 1 But you were able to, you know, get Matthias Spouse, who's like one of the most prolific
[2286.86 → 2291.58] programmers in the world. Um, and you, you've essentially, you know, implemented a custom
[2291.58 → 2296.70] Merkel tree, which is like basically like, uh, for, for audience that doesn't know what that is,
[2296.70 → 2301.42] you basically re-implemented Git, uh, and then you backed it by like a BitTorrent network for efficient
[2301.42 → 2306.38] sharing and stuff like that. Like it's, this is not simple work. Um, and, and you have a small team
[2306.38 → 2311.66] of like really amazing people and were able to get really amazing people. Like how, how did you go about getting all of
[2311.66 → 2316.46] those people and getting such great people to work for, you know, less than, uh, you know,
[2316.46 → 2320.46] San Francisco market rate, but, but, you know, a fair amount of money. Um, that's a good question.
[2320.46 → 2326.62] I think Matthias was the obvious choice for me. I had never met him actually, but, um, I published a
[2326.62 → 2333.26] lot of no JS modules. And, um, so I was aware of him because he also was publishing a lot of like
[2333.26 → 2338.14] modules to NPM. And, um, I felt like the NPM community was really cool because there was a lot
[2338.14 → 2344.06] of people trying to produce reusable software and, um, also produce like efficient streaming
[2344.06 → 2349.74] software for writing like data infrastructure. And Matthias actually had a file sharing startup.
[2350.06 → 2354.78] Um, that we joke now that he was, he was basically doing everything that we're doing now, except
[2354.78 → 2359.74] doing it in like a centralized way. And now he's doing, he's just been working on the same
[2359.74 → 2365.50] like user experience, like sharing a bunch of files in a browser. But, um, now we're doing it in a way
[2365.50 → 2372.30] that like works for that's like decentralized. And so he was like, uh, I just knew he was awesome.
[2372.30 → 2377.34] And I actually just DMed him on Twitter and was like, uh, Hey, I don't know if you have a job right
[2377.34 → 2382.14] now, but, uh, I just got this grant and I can hire people to work on these problems. Like, are you
[2382.14 → 2387.90] interested? And, um, he still had a job, but he was in Denmark. So it was like, even though it was a
[2387.90 → 2392.22] full-time job, it's a Denmark full-time job. So it's like a part-time job in America.
[2392.22 → 2398.86] Yeah. And, uh, so he just said, yeah, cool. I'll work part-time. And then, uh, he eventually
[2398.86 → 2403.02] quit his job and has been working full-time for about a year and a half or two years now.
[2403.58 → 2408.14] And then Carissa is another, um, like the next person that we hired and she is awesome. She
[2408.14 → 2412.14] was working at a startup that got bought, and they were trying to build a GitHub for data,
[2412.14 → 2416.06] but then it got bought, and it turned into like an enterprise thing that she didn't want to work on
[2416.06 → 2420.62] anymore. And she just found our project because we were out there, and we were at open source
[2420.62 → 2424.70] conferences. And that's the way that I found Matias was I was involved in open source and
[2424.70 → 2429.42] I was involved in the community and I had, you know, like I went to, I've been going to open
[2429.42 → 2435.26] source conferences since like, uh, I was 19 or whatever. So I just had a lot of, um,
[2436.14 → 2440.86] time invested in the community. So I think if I was going to underscore like one thing, it's that like,
[2441.74 → 2445.34] if you're a coder that wants to go down the path of supporting yourself through grants,
[2445.34 → 2449.74] it's really important that you go to as many community events as possible, both to meet funders,
[2449.74 → 2456.30] but to meet coworkers and expose yourself to different ideas. Um, and like the intersectional
[2456.30 → 2460.06] thing that Nadia mentioned, like, I think that's huge. Like having an interdisciplinary,
[2460.06 → 2464.86] interdisciplinary view of like, you should be able to tell people what your software, like,
[2465.66 → 2471.18] what communities your software affects, not just like, um, like in a topic way or whatever,
[2471.18 → 2475.74] but like in a concrete way, like for us, because we spent so many years figuring it out,
[2476.70 → 2481.02] um, our key focus areas, I guess, is science, journalism, and government. We think that those
[2481.02 → 2487.18] are three really cool areas that there's actually a lot of fun, like funding to try to, um, like not,
[2487.18 → 2493.02] I don't want to say fix, but there's a lot of funding to, um, invest in better solutions because
[2493.58 → 2497.50] everybody knows journalism is trying to reinvent itself because nobody's buying papers anymore.
[2497.50 → 2503.42] And, um, government has had a lot of innovation lately because of code for America and healthcare.gov
[2503.42 → 2509.98] being such a disaster. And there's this us digital service now. And, um, science is kind of what we've
[2509.98 → 2515.50] been working on mostly, but I think that science journalism and government are three fascinating
[2516.70 → 2522.46] areas that if you're a programmer, there are tons of exciting and challenging problems. And they're also
[2522.46 → 2528.30] like, they're the foundations of our society that we should all support anyway. Um, like going to work
[2528.30 → 2534.78] at a startup, like getting people to like to engage with advertising more, um, doesn't have the same
[2535.42 → 2541.42] like moral imperative as, uh, like fixing the way that people are informed about what's happening in
[2541.42 → 2546.46] their community or whatever, like fixing local government or making scientific results, like more
[2546.46 → 2553.42] available in the long-term things like that. So like, we do definitely play a little bit. I mean, it's not like
[2554.06 → 2559.90] coercive, but, um, the reason we're able to get like, or the reason that my team, we don't have that many
[2559.90 → 2566.54] people, by the way. Um, we just went from three to five, and then we have a couple of part-time contractors.
[2567.18 → 2572.86] So we're not like a huge team, but, um, I think that the reason that we're able to get, I think everybody on our team is
[2572.86 → 2578.94] super world-class and the reason we're able to get world-class people are because we are, uh, we give
[2578.94 → 2584.70] people a huge degree of freedom. So people are basically their own bosses if they want to be,
[2584.70 → 2591.18] but I also try to support them as much as I can. Um, and everything you get to do is open source
[2591.18 → 2597.18] and you're impacting like an actual, like there's a direct impact of your work because we're, we're
[2597.18 → 2602.70] essentially like, like working directly for a specific community. In our case, it's been mostly scientists.
[2603.66 → 2609.58] Um, and so it's like meaningful. So I think it's important that, um, it's not just like you show
[2609.58 → 2615.58] up to work, and you get stock options and compensation, and you work on like a backlog of issues, but I feel
[2615.58 → 2620.78] like everybody on our team is more like, um, like I encourage people to have their own projects that
[2621.58 → 2625.26] are, that they're passionate about, that they can be the owners of, which also helps in a remote
[2625.26 → 2629.90] working context. Cause if you have your own projects that you're the owner of, then you don't have to,
[2629.90 → 2635.90] um, sync up with other people to work on it. But then we also have like team level projects that we
[2635.90 → 2642.70] all try to collaborate on. I think that we basically use the grant money to hire a bunch of really smart
[2642.70 → 2651.10] people and are not smart, but, um, like passionate and invested people into the problem. And then just
[2651.10 → 2658.06] pay them to basically like almost like bell lab style. Um, just like incentivize them to work on a
[2658.06 → 2663.26] set of problems that are like pretty high level and contribute to the ecosystem. And I really view
[2663.26 → 2670.14] it as like, we're just a bunch of people getting paid to like, try to explore like the future of
[2670.14 → 2675.74] how scientific data is shared. Um, but we're not, if we were running ourselves like a startup, we would
[2675.74 → 2682.06] try to, um, you know, have everything be branded under our name and have everything be like productized
[2682.06 → 2687.02] or whatever, or like strategically open source things and strategically close source things. But for us,
[2687.02 → 2692.06] I feel like everybody on our team is like acting as an individual. And then sometimes we work together
[2692.06 → 2696.70] on bigger projects, but really it's like, we just try to get the best people and get them working in
[2696.70 → 2700.46] this space because otherwise they won't be incentivized to work on these problems. They'll go and
[2701.90 → 2707.58] get funding from elsewhere, like AKA get a job and go and work on some other problem. That's not
[2707.58 → 2712.14] supporting the scientists. And I mean, some of the solutions to those problems are going to end up being
[2712.14 → 2716.94] better as their own thing, not attached to that. Right. Like, you know, it's about what's best for
[2716.94 → 2721.10] the project and for the solution to the problem, not necessarily, you know, tying everything and
[2721.10 → 2725.74] making it on brand the way that you would in a startup. Right. Right. Totally. Yeah. Yeah. Yeah.
[2726.38 → 2730.30] All right. I think we're, uh, we're coming up for a break pretty soon. Um, in a few minutes,
[2730.30 → 2736.30] we're going to deep dive, uh, into what it's like to get paid to work on your passion. We'll be right back.
[2736.30 → 2743.82] Hey everyone. Adam Stachowiak here, editor-in-chief of change log. And I want to tell you about
[2743.82 → 2751.90] our cloud server of choice, linode.com. Head to linode.com slash RFC, get an SSE server running in
[2751.90 → 2757.74] seconds. Plan started just 10 bucks a month. And when I say our cloud server of choice, what I mean is
[2757.74 → 2766.14] that all change log is hosted on Linde. Everything we do at changelog.com is on a Linde server.
[2766.14 → 2773.02] What I'd like you to do is go to linode.com slash RFC, pick a plan, pick a distro, pick a location,
[2773.02 → 2780.14] and start your server today. Use our promo code RFC 20 for a $20 credit. Linode.com slash RFC.
[2787.34 → 2791.98] And we're, uh, we're back with Max Ogden. All right, Max. So, uh, I want to get into,
[2791.98 → 2796.06] to kind of the whole paying people to work on open source thing. And especially a lot of the
[2796.06 → 2799.90] stuff you said about giving people a lot of autonomy, kind of letting them deal with whatever,
[2799.90 → 2805.50] um, because I've seen that go bad as well as good. Um, I think the classic example is that
[2805.50 → 2810.46] Tim O'Reilly paid Larry Wall to work on Pearl. And that was when Pearl stopped really caring about
[2810.46 → 2815.66] its users and went down this Pearl six things for like a decade. Um, and so like when you change the
[2815.66 → 2820.38] incentive structures around open source, and you're just paying people to work on whatever, um, does it
[2820.38 → 2824.62] end up getting mismatched with the actual audience for that and the rest of the community around that?
[2824.62 → 2828.78] Um, and, and how do you, how do you make sure that you're kind of staying on track and staying really
[2828.78 → 2833.82] on mission, uh, for your organization? Yeah. I think, um, the way that my coworker,
[2833.82 → 2839.98] Carissa likes to put it is, um, we can write code really efficiently because we're all professionals.
[2840.54 → 2844.54] So we could go a thousand miles, but if we go a thousand miles in the wrong direction,
[2844.54 → 2849.66] like we're actually hurting ourselves. So having the direction is the hardest part and scoping
[2849.66 → 2855.66] everything. And so, uh, what we try to do is always have deadlines for ourselves. So we sign
[2855.66 → 2860.38] up for talks, uh, because if you have to give a talk, then like we encourage everybody on the team
[2860.38 → 2865.66] to always have like a personal deadline, like they commit to doing a presentation on something and then
[2865.66 → 2871.26] they end up getting it finished because they have a presentation. If you never, are you saying that
[2871.26 → 2875.18] your organization actually uses conference driven development as a development strategy?
[2875.18 → 2885.02] Like this is key. Definitely. Yeah. Yeah. Uh, I definitely endorse it because like for me,
[2885.02 → 2888.94] for example, if you go to the DAP project, GitHub, you won't see that many projects.
[2888.94 → 2894.22] It's mostly administrative repositories to find all of our projects. You go to all of our individual
[2894.22 → 2899.74] team members pages. So I think it's really important that people have the credit for the work that they're
[2899.74 → 2904.14] doing because they're not going to work for the DAP project forever. They're going to go and have
[2904.14 → 2908.78] their own career that goes into other places afterwards, or there might, I hope that they
[2908.78 → 2915.02] start their own grants. Like my, my ultimate long-term goal is that we're not a giant nonprofit of like
[2915.02 → 2920.62] 25 people, but instead we're five projects of five people that all are in the same ecosystem as each
[2920.62 → 2924.46] other supporting each other, but everybody can have their own, like find their own niche and their
[2924.46 → 2929.50] mission and have their own funding and, and whatever. So I think it's really important that people,
[2930.14 → 2935.50] all the work that people are doing that I'm paying them for goes onto their own, um, GitHub account.
[2936.14 → 2943.10] And, um, similarly, I think it's important that they personally are speaking on behalf of the community.
[2943.10 → 2948.94] Like we don't have like a developer evangelist that does that full-time. Um, we have every, like,
[2948.94 → 2955.66] I just encourage everybody to kind of be the evangelism for themselves. Um, and if, and I,
[2955.66 → 2960.22] I also don't want people to get DAT talks. I want them to talk about whatever they're passionate about.
[2960.78 → 2964.70] So it's not, you know, that's kind of like how we're different from a like a startup or whatever.
[2965.50 → 2971.10] Um, like basically the only contract I have with the people on the team is like, I give you money and
[2971.10 → 2977.10] then you just try to come up with creative ways to contribute to the ecosystem and solve the problem in
[2977.10 → 2981.58] some way. But like, at the same time, we can't just be like willy-nilly, like giving people infinite
[2981.58 → 2986.46] amounts of time to work on stuff. So another super important thing is getting physically together.
[2986.46 → 2991.42] This is just like remote team stuff, but, um, we are a remote team. You don't have to be a remote
[2991.42 → 2997.42] team, but I think it's valuable for us because if we were physically or like geographically constrained,
[2997.42 → 3004.46] it would make it harder to attract the talent that we do. So by being remote, we can be more flexible.
[3004.46 → 3010.46] Um, and I also have a lot of experience doing remote stuff. Um, like I worked at coffee shops for four
[3010.46 → 3018.54] years, I think the last four years. Um, and so yeah, coffee shop team. Um, and so it's like,
[3018.54 → 3022.46] you know, you just, there are too many things. I mean, you could spend hours talking about it, but,
[3023.18 → 3027.26] um, I was just going to say that the a really important thing for us is we have a travel budget
[3027.26 → 3033.26] in our grants that allow us to, um, convene, and we end up convening fairly regularly. Like I would say
[3033.26 → 3038.46] every two months or three months, we see each other face to face, like not the entire team,
[3038.46 → 3043.66] but at least one person seat like travels to the other person's city, like every other month.
[3043.66 → 3050.30] Like I was just in, um, Copenhagen visiting Matias two weeks ago. And then, uh, he just decided to come
[3050.30 → 3056.30] out here, um, in two weeks because he was like, we're, we're just doing all these new projects
[3056.30 → 3060.06] because of this new grant that we just got. And he's like, oh, I don't want to be on a different
[3060.06 → 3064.22] time zone. I'm like really excited to work on this stuff. So he's going to come out, and it's also,
[3064.22 → 3068.70] you know, summer in the U S so it's a good time to visit and everything. So, um, we've done a lot
[3068.70 → 3073.42] of like renting cool cabins in the woods in Oregon and going to hack for like three days and then
[3073.42 → 3078.30] people fly back home. And so we spend that three-day period getting really excited and doing project
[3078.30 → 3082.06] planning and coordination and coming up with what our like prototype that we're trying to build is,
[3082.06 → 3086.06] or like what the alpha release of something looks like. And then we can all go back to our,
[3086.06 → 3090.38] our day-to-day lives and be independent and work on it. And then kind of like,
[3090.38 → 3095.02] so that's like the that's kind of like the so the two phase thing is we have like an intensive
[3095.02 → 3099.34] project planning phase. And then we, once we get scope out a roadmap for a couple of months
[3099.34 → 3105.42] for every individual, then we can go back and kind of work in parallel. Um, we still like ping each other
[3105.42 → 3111.66] with questions every day, but it's, we don't have like a daily centralized, like planning process.
[3111.66 → 3115.18] We have like a we try to decentralize and asynchronous as much as possible.
[3115.18 → 3118.54] I mean, budget wise, that's probably still cheaper than an office, right?
[3118.54 → 3123.10] Yeah. Oh, yeah. I mean, now that we're more people, I'm not sure how the economics are going
[3123.10 → 3127.58] to work out for travel budget, but, um, I have noticed that grant funders are generally open to,
[3127.58 → 3133.10] um, convenience. Like they love it. Yeah. They love convenience. Like you can pitch,
[3133.10 → 3136.46] once you have a relationship with a funder, you can be like, Hey, I wanted to get like 20 people
[3137.18 → 3141.98] that are like, you know, the, the leaders in this open source community together with like
[3141.98 → 3147.18] a bunch of scientists. Can you pay for us to like, I'll fly out to some place? And they're like, okay.
[3147.18 → 3149.26] That's always called a convening.
[3149.26 → 3154.14] Yeah. Yeah. They're like $50,000 to fly a bunch of people for like a weekend conference. Like, okay,
[3154.14 → 3159.74] that's $50,000 to them is like totally, um, as long as you're like pitch them on a thing that's like,
[3159.74 → 3166.62] oh, we'll definitely write a report for you afterwards. Um, they actually like that. So
[3166.62 → 3172.62] we're going to try to do that soon. Because we're, um, I'm starting to, um, build up a consortium or
[3172.62 → 3177.74] alliance. We don't know the word yet with a bunch of other project based, um, open source teams,
[3177.74 → 3185.50] or I'm sorry, grant based open source teams. Um, and we're trying to figure out, like,
[3185.50 → 3189.58] we're trying to like to write a manifesto for what it means to be a project like this.
[3189.58 → 3192.86] Because we don't really fit. Like our team is really weird. Like we don't fit in a
[3193.34 → 3200.14] traditional category. Like we're not, um, in academia, but we work with academics, and we're,
[3200.14 → 3206.06] um, we're a nonprofit except we write like pretty much all software. Um, which I don't know a lot of
[3206.06 → 3211.34] nonprofits that are like just software focused. And we're also not a startup, although people think
[3211.34 → 3215.98] we're a startup because we have a logo and a name. So they just assume like we're a startup.
[3216.78 → 3220.94] And, uh, so we just, we're just kind of weird. We're an open source project, but we have a budget
[3220.94 → 3225.90] and people are paid to work on it. So that's also weird. Um, so we're trying to figure out like what,
[3226.54 → 3231.98] like, what is the name that we can call ourselves that people will understand. And like, also all the
[3231.98 → 3236.06] stuff that I'm like sharing here, like, it'd be cool if we had it written up in an accessible way
[3236.06 → 3238.30] so that people could kind of start down that path.
[3238.30 → 3243.50] So zooming out a little bit, uh, I don't know how much you've paid attention to the past year or so,
[3243.50 → 3249.18] but there've been a bunch of grant programs, whatever grant means coming from different
[3249.18 → 3257.42] organizations like Mozilla and Linux, um, and Stripe. And I'm curious to hear your take on sort
[3257.42 → 3262.46] of like, what do you think, what role do you think grants could or should be playing in funding open
[3262.46 → 3267.66] source work? Does it cause in your case, this, it was for funding a new project, right? And in other
[3267.66 → 3272.86] cases it's for funding an existing project. And where's the sweet spot in terms of like,
[3272.86 → 3274.86] where should that money be deployed most effectively?
[3274.86 → 3279.58] I'm yeah, I think it's interesting that like, for example, Stripe has an open source
[3279.58 → 3284.06] program. Um, I mean, I don't know what percentage of their, uh,
[3285.02 → 3290.70] their budget goes to that. I, the reason that I like private philanthropies is that the people
[3290.70 → 3295.34] working, for example, at the Gates Foundation or whatever, like we're not a Gates Foundation grantee,
[3295.34 → 3299.66] but the people working there, obviously Bill Gates is a computer programmer. So
[3300.54 → 3304.54] like most people that are working there are focused on like the humanitarian side or like
[3304.54 → 3308.54] the social impact side, and they're not technologists. And so you have to be able to
[3308.54 → 3313.34] learn to speak their language. But then once you do, you're kind of like locking in your agreement
[3313.34 → 3320.06] with them to addressing their like societal problem using technology. And so I think it's really
[3320.06 → 3325.18] important to have that yin and that yang of you're going to use technology as like one tool, but the
[3325.18 → 3331.66] end goal isn't to build the technology. The end goal is to affect change in some area. And I'm curious,
[3331.66 → 3337.34] like with Stripe, like what they're, I don't know if like, I would consider making payment
[3337.34 → 3343.34] infrastructure more robust to be like affecting positive change in society. So I, I think like if
[3343.34 → 3347.26] they're just, like I said earlier, there's like a bunch of different ways to define the word grant.
[3347.26 → 3356.86] For me, what that has meant is forcing myself to learn how to pitch my projects in a way that
[3356.86 → 3363.26] actually like affects some community or like, you know, has some sort of social impact. That's where
[3363.26 → 3367.34] kind of like the nonprofit side comes in. Like people assume like if you're a nonprofit, you have
[3367.34 → 3371.58] some sort of social mission. And I think that's super important for open source people to be able to
[3371.58 → 3376.62] link their project to a social mission. So I think that that's really important. And I'm not sure
[3377.34 → 3383.58] if you have like for-profit companies who are giving the grants out, like it could just be,
[3383.58 → 3389.74] I mean, I think grants can be a really simple way to, to just like funds infrastructure because
[3389.74 → 3394.62] otherwise you would have to go work at that company and be an employee to get paid. So grants are a way
[3394.62 → 3398.94] to just have people like they can basically say, Hey, there's this person that doesn't work for us,
[3398.94 → 3403.90] but it's super qualified. Let's just give them a grant. But I'm not sure. Like, I don't think
[3403.90 → 3409.02] that's the long-term. I don't know what the long-term goal of that is because by forcing me,
[3409.02 → 3413.66] for example, this grant process has forced me to learn how to become not just a programmer,
[3413.66 → 3419.58] but also like a project leader and a grant writer and like learning how to run an organization.
[3420.46 → 3425.98] If I got like a Stripe grant to build, to like work on open SSL or whatever, I don't think that I
[3425.98 → 3430.54] would learn like any of those other things. I would just like get paid to work on open SSL for
[3430.54 → 3436.22] a bit, make open SSL better, but then like run out of money and then have to go get a job anyway.
[3436.22 → 3440.62] It sounds like what it really separates into it. I think nonprofit and for-profit is probably like
[3440.62 → 3446.46] the wrong way to look at this. It's more that is the impact of this grant to improve a technology
[3446.46 → 3451.34] or is it to improve like a social outcome? Right. Because you have, you have plenty of nonprofits and
[3451.34 → 3456.78] for-profits that depend on, and then we'll, you know, subsidize or put money into a technology
[3456.78 → 3463.34] because they're dependent on it in some way. Right. But you know, when you look at the social
[3463.34 → 3468.46] good of something, the only way to fund it is going to be with a grant. Right. I mean, if you're,
[3468.46 → 3472.14] if your primary outcome, that's like the only way to get any money for it.
[3472.14 → 3477.58] Yeah. I mean, economically there is the term, the public good, which is like things that by definition,
[3477.58 → 3482.62] like the light, like lighthouses are the typical example where nobody wants to build the lighthouse
[3482.62 → 3488.54] because there's no like ROI on a lighthouse. It's a public infrastructure, but like, if you don't have
[3488.54 → 3494.62] it, then like everyone dies. So you need somebody to build it, and how are you going to build a lighthouse?
[3494.62 → 3500.06] So if you're building a lighthouse, like its grants are good. Yeah. That's, um, that's partially why
[3500.06 → 3505.10] I've been interested in exploring, like, or thinking of open source software as public software, um,
[3505.10 → 3511.18] to make that link between like a public good. And, and when I describe open source software to people
[3511.18 → 3515.66] who don't use it, it's sort of like, this is a thing that exists in the public domain that you can use
[3515.66 → 3521.50] for whatever purpose you want to use. But it's sort of a, a new concept for people to think about
[3521.50 → 3525.98] software that way. If they're not familiar with software, I mean, anyone outside of open source
[3525.98 → 3530.22] thinks of software is like Silicon Valley and tech and whatever. And it's like, well, there's also a lot that is
[3530.22 → 3535.98] just like being created in the commons and being used. And how do you end up supporting that stuff?
[3535.98 → 3542.30] Mm-hmm. Well, and I mean, I think that it's, it's important to, to draw this distinction though,
[3542.30 → 3547.18] between like what you're doing, like, like the no JS foundation is a nonprofit, but at the end of the
[3547.18 → 3552.62] day, it's there to make sure that that technology succeeds and there is social good outcomes built on
[3552.62 → 3556.46] top of the technology. But the mission of the foundation is to make sure that the technology is
[3556.46 → 3561.74] there. It's not necessarily to focus on those social outcomes. I mean, it enables that, but that
[3561.74 → 3566.14] is not, you know, part of the social mission there. And a lot of the modules that you build,
[3566.14 → 3570.46] I'm sure could be used by a company to do some awesome, like big data research or whatever.
[3571.02 → 3575.26] But your mission and what you're focused on is actually building things for a particular social
[3575.26 → 3579.82] outcome. Right. Yeah, definitely. Like we're, I would say, yeah, the Linux foundation, for example,
[3579.82 → 3584.62] is a lot lower level in the stack because, and that's like one of the trade-offs you have to make is like,
[3584.62 → 3591.02] how detached from the issues do you want to be? I think that the more attached to social issues
[3591.02 → 3596.22] you are, the easier you'll find it to get grants because that's all grant people care about is you
[3596.22 → 3601.10] being able to contextualize your technology in their existing mission. So that's like the whole art form
[3601.10 → 3606.30] is if you can say like, Hey, my project helps scientists, then they'll be like, Oh, we fund science.
[3606.30 → 3610.46] We'll write you a grant. Like that's the that was the thing that three years ago, I wouldn't have been
[3610.46 → 3615.42] able to like to say because I didn't know scientists had these problems until somebody approached me and
[3615.42 → 3622.38] like convinced me to work on it. So yeah, it's like if you're detached from the social issues,
[3622.38 → 3625.66] then you have to find other ways of like supporting it. But like the Linux foundation
[3625.66 → 3630.46] found a way to support it, which is like all these companies like use it, and they can help,
[3630.46 → 3631.90] you know, support the overall project.
[3631.90 → 3639.58] Where do you think there are gaps in knowledge between, um, grant makers and open source communities?
[3640.06 → 3644.22] What do you wish that like more funders knew about open source or vice versa?
[3644.70 → 3650.62] Um, so the biggest issue that I have is the way you have to write the grants up front with all the
[3650.62 → 3656.14] budget and all the plans. It's the same kind of, uh, distinction as like waterfall versus agile,
[3656.14 → 3661.74] for example, for example, this grant that we just got, the money arrives. We don't have to get into
[3661.74 → 3666.54] the mechanics of how you receive money from grant, but I'll just say that we, we had access to the
[3666.54 → 3672.78] actual grant money in essentially June. It was like two weeks ago. And, um, I wrote the grant with
[3672.78 → 3679.26] Carissa in October of last year. And so that's like a pretty long amount of time. I think it's like,
[3679.82 → 3684.94] almost nine months. So we had an idea, we wrote a grant and then nine months later we get the money.
[3684.94 → 3690.30] And I would say that's like a that's on the longer side for a film topic grant, but it's not uncommon.
[3690.30 → 3695.98] So, I mean, if you, if I had to tell you what I was going to work on in nine months from now,
[3695.98 → 3700.38] I wouldn't be able to tell you, but that's like another art form of grant writing is being able to
[3701.02 → 3705.34] write a grant that's vague enough that you can still, once you start getting the money,
[3705.34 → 3708.94] you can still like to use the money to work on the thing you said you were going to work on nine months
[3708.94 → 3716.06] ago. And so on thing that I wish that foundations would understand is, um, timelines and agility and
[3716.06 → 3720.30] like basically what I would much rather have. And I understand that there's like,
[3720.94 → 3724.70] you have to have a high level of trust to do something like this, but what I, my preferred
[3724.70 → 3729.90] situation would be like, I have a relationship with a funder. I convinced them that we're the
[3729.90 → 3734.38] right people to work on the right issues. And so we get the people in the issues locked down
[3734.38 → 3741.34] and are like the causes. And then, um, I can basically go back to them and say, okay, now
[3741.34 → 3746.54] I need a budget for the next three months to do this. And that can be like a lightweight process
[3746.54 → 3752.70] once I've like got in the door with them. Um, but right now the way it works is you do everything in
[3752.70 → 3756.78] one big proposal, including the budget. And then you're locked into that for the entire duration of
[3756.78 → 3761.66] the grant budget. So it means that you have to plan ahead a lot, and you're, you're constrained by
[3761.66 → 3766.70] the budget as you're doing the project. So for example, like say Nadia, that you wanted to come
[3766.70 → 3772.54] work on my team. I couldn't hire you today because I don't have any extra budget. I, what I could do is
[3772.54 → 3776.62] say, let's write a grant together. And then in nine months, maybe we'll have a budget to hire you.
[3776.62 → 3781.34] So it's, it's kind of like annoying because most startups have this slush funds that they can
[3781.34 → 3786.62] draw from, uh, as they need to, um, which is like the initial investment. But the way grants work is
[3786.62 → 3793.26] you, you, um, your budget is not a big slush fund. It's like a paid out in increments, like burn rate
[3793.26 → 3800.22] that they like to be constant. So I can't hire people on a day-to-day basis and can't like readjust
[3800.22 → 3806.38] the budget, like as the thing is in flight. So that's annoying. Um, so there's definitely some
[3806.38 → 3812.70] cultural differences in the way that they actually fund. Um, and also I think if you ask most nonprofits,
[3812.70 → 3818.06] like they don't think about open source, um, and most funders probably aren't thinking about
[3818.06 → 3821.74] open source, but I think that is changing. I think there's like the perception that there's
[3821.74 → 3828.62] not any funding out there for open source stuff. Um, I think if you ask most open source developers,
[3829.66 → 3835.18] um, to write a grant, they'll write a grant that's like super technical and has no social impacts,
[3835.18 → 3840.46] like linkage or whatever, like what I've been talking about. And so then they'll think that,
[3840.46 → 3844.54] oh, well I wrote a grant to write like a new encryption scheme for this thing or whatever,
[3844.54 → 3850.14] or like a new database. And, um, like, there's probably not a lot of places that will just fund
[3850.14 → 3856.14] you to work on random technology. But, um, if you make your grant about fixing an actual problem in
[3856.14 → 3862.38] society, then I think grant people will be like, oh, you want to fix this problem, and you're going to
[3862.38 → 3866.86] do it as open source. Like that's actually a competitive advantage over our other. Because I think
[3866.86 → 3870.46] that what they've done is they've like a lot of grant people have been funding technology
[3871.02 → 3875.58] over the last 10, 15 years. And they've seen, they're starting to understand how
[3876.14 → 3880.30] funding technology works, which is things like, um, like they have a lot of technical debt.
[3880.30 → 3883.34] They have a lot of projects that have horrible project management, or they have,
[3883.82 → 3887.18] like people will say in the grant, like, oh yeah, we're going to make awesome reusable software.
[3887.18 → 3891.98] And then they make software that's very difficult to reuse. Um, these are all just like inherent to
[3891.98 → 3896.70] software in general, like anybody that works on software will like to tell you that it's,
[3896.70 → 3901.10] it's really easy to have a lot of technical debt and make a giant app that is really inflexible.
[3901.66 → 3906.38] So if you can make a pitch, you still have to make your pitch be about a social cause,
[3906.38 → 3912.22] but I think if you can make it, um, if you can say like, by the way, we're like, we're doing it as
[3912.22 → 3916.14] open source, and we actually want to invest in building up this ecosystem around this problem,
[3916.14 → 3920.70] that that's actually an advantage to you. But I don't think open source is like the reason you get
[3920.70 → 3924.14] the grant. It's just like a thing that helps. The reason you get the grant is that
[3924.86 → 3926.86] you're committing to like a cause that they care about.
[3926.86 → 3930.70] Well, and just like you were saying earlier, right? Like grants want to be tied to the social
[3930.70 → 3935.90] cause, right? Like they want, so, you know, how do we, and it's not that programmers don't care
[3935.90 → 3939.74] about social causes. I mean, if they, if they didn't, you wouldn't be able to get such great
[3939.74 → 3944.70] people working on them. Um, it's really just that, you know, getting them to speak in that language,
[3944.70 → 3947.90] um, and getting them to be on the page, the same page as the grant writer is. Right.
[3947.90 → 3949.34] Yeah. Yeah, definitely.
[3949.34 → 3953.50] In an ideal world, how do you picture that people would be able to work on
[3954.06 → 3958.38] open source? How could that be like, because right now, I mean, there's so many different
[3958.38 → 3963.50] grants that are, I think there's still sort of ad hoc opportunities. Um, but if you were to think
[3963.50 → 3967.50] about this on an institutional level, how could that actually be supported and funded?
[3967.50 → 3973.58] Um, so that is an awesome question. One way that I would answer it is procurement reform in
[3973.58 → 3978.38] government, which is like the most boring phrase that you could possibly say. But, um,
[3979.42 → 3984.22] like think about the amount of money that is spent on software and government. Well, I mean,
[3984.22 → 3988.46] most people probably don't know, but there's like, uh, an average project in the federal government
[3988.46 → 3992.54] for like, like there was a actually, this isn't even a federal government. This is the city of New York.
[3992.54 → 4001.18] They spent $600 million, two thirds of an Instagram on, uh, a time tracking app for
[4001.18 → 4007.66] employees, and it never ships. Right. Right. And one of the reasons, right. Is that how much does it
[4007.66 → 4013.02] cost to apply to get that money? Right. Yeah. Because you have to like, have invested
[4013.02 → 4018.14] dozens of years into the nepotistic system of existing government procurement. And so it's like,
[4018.78 → 4023.82] it's not a technical problem to fix procurement, but if somebody fixes procurement, and by the way,
[4023.82 → 4028.62] it is being worked on now because, um, like I mentioned this earlier, but healthcare.gov was so bad
[4029.26 → 4035.18] that, um, the silver lining around that, that's actually pretty exciting is that there's, um, two new
[4035.18 → 4040.38] organizations in the federal government that are hiring remote, and they're hiring, um, technologists and
[4040.38 → 4046.78] they're paying people to work on open source inside of government. Um, one is called the US digital
[4046.78 → 4055.18] service and the other is called 18 F, uh, or one eight F, and they're sort of like a brother,
[4055.18 → 4061.66] sister organization. So one is inside the executive branch and they're like the technology advocates.
[4061.66 → 4067.02] They're almost like, um, the role that like the EFF plays where they, they have people come up with, um,
[4067.02 → 4071.98] policies, and they get the different agencies to adopt policies, and they go, like, I have a friend
[4071.98 → 4077.66] that works there. He gets to go into like the VA or like the social security office. And they're like,
[4077.66 → 4082.30] Hey, check out this new a hundred million dollar, like database that we contracted. What do you think?
[4082.30 → 4086.62] And he's like, um, if I was like, he used to build data centres at Twitter, and he was like,
[4086.62 → 4091.50] if I was building this, I could have done it for $5 million and saved you $95 million. Like,
[4091.50 → 4094.78] why did you build this for a hundred million dollars? And they're like, that's what the vendor told us.
[4094.78 → 4101.10] Um, like Oracle said, this was a great deal or whatever. And so that is a really important
[4101.10 → 4105.58] cause right now that actually has a fair amount of momentum. Um, 18 F is where you go to work. If
[4105.58 → 4110.38] you actually want to build the, the solutions, they're like, like an actual contractor, um,
[4110.38 → 4115.18] that is government employees that, um, like hires people to work on the actual projects.
[4115.74 → 4122.30] And a, uh, USES is kind of like where you go to set the policy. So for instance, they are doing a
[4122.30 → 4128.22] lot of stuff around making all federal websites have mandatory SSL. Um, so that the NSA can't
[4128.22 → 4133.34] snoop on what you're browsing, for example. So there's like a lot of really cool momentum in
[4133.34 → 4138.94] fixing that system. And so if I was going to place a bet on where all the grants are going to be in
[4138.94 → 4143.82] the future, it's around like delivering government services in a more efficient way and actually
[4143.82 → 4147.58] competing for government grants, because that landscape is about to get a lot more accessible
[4147.58 → 4150.54] to open source stuff because of all the work that's happening at the federal level.
[4151.26 → 4157.90] Um, and another way I would answer that is this question is, um, like procurement reform is the
[4157.90 → 4163.58] first thing when that's happening. So like, keep an eye on that space. The other thing is, um, like I
[4163.58 → 4167.58] mentioned, like, we don't know how to describe our project in terms of like, are we a nonprofit? Are we,
[4167.58 → 4171.90] uh, academic project? Like we don't really know what our label is. And we're trying to figure out
[4171.90 → 4177.34] with some other groups, a model for supporting projects in this ecosystem. And, um, so a great
[4177.34 → 4181.58] example to look at, I think they're doing some great work is, um, if you look up this thing called
[4181.58 → 4188.22] the substance consortium, there's this awesome text editor. It's like a JavaScript, um, like rich text
[4188.22 → 4193.26] editor and editing environment called substance. It's like really beautifully designed, and it's all
[4193.26 → 4199.42] open source. And, uh, they had been working for this open access scientific journal, writing a journal
[4199.42 → 4205.90] article viewer and editor. And, um, they had all these other organizations, like they were basically
[4205.90 → 4211.74] being contracted by this one journal, um, called life. And they built this thing called life lens,
[4211.74 → 4216.38] which is like a really beautiful, um, way to read papers. Because most people read papers on PDF,
[4217.10 → 4222.14] but, um, trying to read a paper on your phone or whatever on a PDF, it has like super wide columns.
[4222.14 → 4227.34] And it's like, why can't I just have this be a webpage? So they're trying to fix some of these
[4227.34 → 4232.46] problems. Um, and, but they had all these other organizations in the space that were like, well,
[4232.46 → 4239.26] we also want to like to invest together in better editing tools for science, um, or just editing tools
[4239.26 → 4247.10] for the web in general. And so, um, they set up this thing called the, uh, the substance consortium,
[4247.10 → 4252.62] which is like, there's four stakeholders that all, um, help pay for the development of substance,
[4252.62 → 4257.98] but they're not like exclusively hiring the substance team, um, to work as like employees
[4257.98 → 4262.94] of their projects. And so what's really cool about it is substance itself can still be a standalone
[4262.94 → 4269.02] project that can make like reusable open source tools. Um, but it has like an open governance
[4269.02 → 4272.94] structure so that any of like the member organizations can help influence the project
[4272.94 → 4277.10] direction positively and like work together to support the project without, um,
[4277.10 → 4281.42] controlling the project. So their whole thing is like cooperation without control. And, um,
[4281.42 → 4286.30] that work is being facilitated by a group called the collaborative knowledge foundation,
[4287.02 → 4291.74] which is one of the stakeholders, um, or one of the people paying the substance team.
[4291.74 → 4296.46] And so for example, substance is just like the components, like the editor components.
[4297.18 → 4301.58] Um, but the substance team doesn't have like, they're just two people. They don't have, uh,
[4302.22 → 4307.66] the, the linkage to like the social issue, or they don't have the grant writing capability.
[4307.66 → 4312.62] Um, at this point, they want to get to that point, but they need like incubating, and they need support
[4312.62 → 4317.58] for their project. Um, collaborative knowledge foundation is a couple of folks that started it
[4317.58 → 4322.94] that are really focused on fixing the scientific publishing ecosystem. Like they want every journal
[4322.94 → 4327.02] to be using open source publishing tools. So they have the social mission. Like that's a huge social
[4327.02 → 4334.62] mission. Access to, um, research is like a huge cause right now. Um, and so what's cool is that
[4334.62 → 4340.06] the collaborative knowledge foundation has got some grants to work on fixing scientific publishing.
[4340.62 → 4344.46] And instead of like hiring the substance people as employees, they're just like, let's support
[4345.26 → 4350.70] like everyone in this ecosystem together and have substance still be standalone because they think
[4350.70 → 4354.78] it would be toxic if they actually like exclusively hired the substance people that work on their one
[4354.78 → 4359.34] thing. They would rather have substance like flourish and have a whole ecosystem because I mean,
[4359.34 → 4362.70] that's where open source works really well is when you have a bunch of interests that are
[4362.70 → 4369.02] supporting like a factored out common infrastructure. Um, so I think that the substance
[4369.02 → 4373.50] consortium model is really exciting, and we're trying to figure out how to, um, we need to come up with a
[4373.50 → 4380.54] cool name for that way of doing things. And, uh, I think ideally the DAT project, since we are like, um,
[4380.54 → 4385.02] like a distributed file system, sort of, it's a pretty low level component. Um, and there's a bunch of
[4385.02 → 4389.42] different interests. It'd be awesome if we could get a similar thing for debt. So we'd have like a DAT
[4389.42 → 4393.98] consortium, and we would have the DAT project itself just be the technology, but then we would have all
[4393.98 → 4400.30] the different, um, like organizations that have a specific cause be able to support our work. And
[4400.30 → 4405.50] maybe, maybe we split up into two teams. Like one of us is the science cause and then all the low
[4405.50 → 4410.86] level people go and work on just the infrastructure stuff. Awesome. Thanks so much for coming on here
[4410.86 → 4415.90] and talking to us about grant funding. Yeah. Anytime. And, uh, definitely if you're listening to this and you
[4415.90 → 4421.82] want to learn more, um, feel free to reach out to me and I can send you some concrete examples of
[4421.82 → 4432.78] grants that I've written and stuff like that. Great. Thanks, Max.
[4445.90 → 4451.82] Thank you.
[4451.82 → 4453.82] Thank you.
[4453.82 → 4455.82] Thank you.
[4455.82 → 4457.82] Thank you.
