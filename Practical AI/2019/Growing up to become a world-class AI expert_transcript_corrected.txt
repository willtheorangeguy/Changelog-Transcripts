[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.50 → 20.12] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.24 → 24.88] And we're excited to share they now offer dedicated virtual droplets.
[24.88 → 28.80] And unlike standard droplets, which use shared virtual CPU threads,
[28.80 → 32.66] their two performance plans, general purpose and CPU optimized,
[33.24 → 35.86] they have dedicated virtual CPU threads.
[36.18 → 40.64] This translates to higher performance and increased consistency during CPU intensive processes.
[41.08 → 44.98] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.28 → 49.76] game servers, databases, batch processing, data mining, application servers,
[49.98 → 54.70] or active front end web servers that need to be full duty CPU all day every day,
[54.92 → 57.70] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.70 → 61.04] Pricing is very competitive starting at 40 bucks a month.
[61.42 → 66.54] Learn more and get started for free with a $100 credit at DigitalOcean.com slash Changelog.
[66.68 → 69.58] Again, DigitalOcean.com slash Changelog.
[69.58 → 86.54] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.98 → 88.70] productive, and accessible to everyone.
[89.10 → 93.62] This is where conversations around AI, machine learning, and data science happen.
[94.10 → 98.34] Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.34 → 99.52] Follow us on Twitter.
[99.62 → 101.12] We're at Practical AI FM.
[101.32 → 102.44] And now onto the show.
[106.76 → 110.48] Hello there and welcome to another episode of Practical AI,
[110.90 → 116.10] the podcast where we try to make AI practical, productive, and accessible to everyone.
[116.64 → 118.72] This is Chris Benson, your co-host.
[118.72 → 124.58] And today I am at the NVIDIA GPU Technology Conference in Silicon Valley.
[125.06 → 127.06] It is Thursday, March 19th.
[127.18 → 129.36] I happen to be operating solo today.
[129.52 → 131.42] Daniel was not able to make it out here.
[131.90 → 136.52] I have a pretty amazing guest today to talk to.
[136.52 → 140.86] With me is Anima Annular.
[141.30 → 142.60] Did I get your name okay?
[142.88 → 143.38] Oh, yeah.
[143.44 → 144.66] You did an amazing job.
[145.30 → 145.58] Okay.
[145.90 → 149.96] Anyone who listens to me on this regularly knows that I screw up names all the time.
[150.38 → 151.26] So I'm glad that.
[151.56 → 155.54] You are the director of machine learning research at NVIDIA.
[155.98 → 158.52] And you're also the Been professor at Caltech.
[159.12 → 159.76] Is that correct?
[159.76 → 160.60] That's right.
[160.84 → 161.04] Yeah.
[161.16 → 162.36] I wear both the hats.
[162.86 → 169.38] And I think it really gives me an opportunity to bridge industry and academia in many interesting ways.
[169.50 → 169.92] Absolutely.
[170.18 → 175.92] So in a few minutes, you're giving two separate talks here at GTC.
[176.68 → 179.16] And I would like to kind of delve into both those.
[179.34 → 182.54] But at first, I would really like to talk to you.
[182.56 → 184.56] And I know that you talk to people often.
[184.56 → 191.26] And you've been in front of audiences quite a bit about AI and the role you play there.
[191.72 → 196.56] But I actually want to go back to the beginning and kind of find out how you got into this,
[197.00 → 203.44] what that journey has been like, and talk a little bit about some of the challenges that you may have faced along the way.
[203.82 → 206.46] And I know that you have spoken to some of those in the past.
[206.72 → 210.42] So can you tell us kind of how you got into this at all?
[210.70 → 211.54] Yeah, certainly.
[211.54 → 223.10] You know, I've had a pretty amazing childhood in terms of, you know, the people around me were always encouraging me in my passion for math and sciences,
[223.10 → 226.60] but also for dancing and arts and everything, right?
[226.70 → 232.12] So there was a lot of like, you know, like my mom is an engineer.
[232.56 → 238.54] My dad has a small scale industry that manufactures all kinds of components, builds machines.
[238.54 → 250.16] So, you know, I would go there as a kid, like both my mom and dad would take me there and to see how those machines operated and how it just seemed so magical that, you know,
[250.16 → 255.42] you could automatically, you know, build these components and there would be in all kinds of shapes.
[255.54 → 258.72] You had these machines going at this really high speed.
[259.50 → 260.68] And so that was fascinating.
[260.68 → 264.00] And I would ask my parents, you know, how is this possible?
[264.60 → 264.80] Right.
[264.84 → 266.50] And they would be like, oh, it's all math.
[266.84 → 267.24] Right.
[267.56 → 273.72] So I had like this very friendly, like math was a friendly thing to me from early childhood.
[274.30 → 276.04] How old were you about that time period?
[276.14 → 279.04] Like what do you think that, that what age were you at that point?
[279.04 → 287.14] I think when my earliest memories are either me like kind of, you know, solving some puzzles or some toys.
[287.14 → 287.62] Right.
[287.68 → 294.94] And going to industry like my parents always like, you know, took me when I was maybe three or four or so.
[295.04 → 295.90] Wow, that is young.
[295.90 → 296.62] Yeah, that is super.
[296.62 → 299.62] So you had this fascination at that really young age.
[299.70 → 299.82] Yes.
[299.96 → 300.32] Yes.
[300.32 → 311.90] Some of my earliest memories are like, you know, me like trying to solve like, you know, math problem and wondering how, you know, there is this addition, and suddenly we're subtraction.
[311.98 → 313.32] Why is there these two symbols?
[313.66 → 315.00] And, you know, what is it?
[315.10 → 316.38] How are the two related?
[316.52 → 316.72] Right.
[316.72 → 319.84] So I somehow remember being very fascinated with it.
[320.20 → 322.68] And my grandfather is a math teacher.
[323.08 → 324.64] And so he was teaching me.
[324.64 → 326.22] You had a secret weapon in your family.
[326.54 → 327.04] That's right.
[327.04 → 331.18] And my grandma would give me all these puzzles and games.
[331.62 → 339.26] And, you know, she tells me that I apparently had memorized like the calendar for a 10-year time period.
[339.26 → 344.52] And they would quiz me on what day is 12th of August, for instance.
[344.64 → 345.48] You got to be kidding me.
[345.72 → 347.20] How old were you for that?
[347.46 → 348.44] Apparently three.
[348.76 → 349.88] Oh, my gosh.
[350.06 → 350.34] Okay.
[350.34 → 351.98] This is what my grandma tells me.
[352.16 → 353.34] I don't I can't do it anymore.
[353.34 → 355.24] So don't, you know.
[355.24 → 358.26] Well, you're setting a high bar for the three-year-olds out there.
[358.36 → 362.74] I know that, you know, I'm sure we have three-year-olds listening to the Practical AI podcast.
[362.88 → 366.34] But in case for that one or two out there, you've just set the bar very high.
[366.94 → 371.00] My daughter, who's about to turn seven, has no excuses at this point.
[371.60 → 372.28] No, no.
[372.34 → 375.56] I think every child's development is different.
[375.80 → 376.04] Right.
[376.04 → 382.22] But, you know, at the same time, there is so much fascination in all aspects, too, of development.
[382.46 → 384.74] For instance, I, you know, I love dancing.
[384.74 → 386.98] I started dancing when I was three as well.
[387.12 → 389.16] So I wasn't put into a box, you know.
[389.22 → 390.64] I wasn't told, oh, this is math.
[390.72 → 391.70] You're only good at that.
[391.82 → 392.32] Do that.
[393.00 → 398.78] So do you think doing dance and other activities that have nothing to do with technology, do
[398.78 → 403.86] you think that made a difference in that having that diversity of experiences made a difference
[403.86 → 405.08] in how you progressed?
[405.40 → 406.22] Oh, certainly.
[406.32 → 407.84] That's what makes us human, right?
[407.84 → 413.54] To, you know, the artistic side of us and the humanities and the liberal education is
[413.54 → 417.76] very much a part of our growth as human beings, as a society.
[418.72 → 421.84] And to me, I would also argue it's highly mathematical.
[422.38 → 425.84] Dancing is, you know, all about rhythm, right?
[425.84 → 428.54] And you'd count one, two, three, four, four steps.
[428.98 → 433.06] And then you progress to saying it's no longer these discrete steps.
[433.26 → 435.90] It's a more continuum of movement, right?
[435.98 → 440.96] There is flow, but there's also sudden peaks and, you know, sudden changes to it that may,
[441.08 → 444.98] you know, so as you progress in dancing, to me, it's highly mathematical.
[445.26 → 446.12] It's like a wave.
[446.12 → 451.20] I have this vision of you at four years old, you know, going through a dance and then dissecting
[451.20 → 453.12] it mathematically across the board there.
[453.56 → 459.44] No, but I think the earliest memory that I have that very much relates to, you know,
[459.50 → 461.50] what I'm doing with AI today, right?
[461.60 → 469.16] I remember suddenly like stopping and questioning myself, huh, I feel so differently right now.
[469.36 → 471.62] I feel like there's something that's me.
[471.62 → 475.50] Like I had never, you know, this kind of what they call self-actualization.
[476.52 → 479.48] And again, no one had told me about it, right?
[479.54 → 484.38] Like I had no idea, but I was just playing, and I have remembered this moment very vividly
[484.38 → 489.06] where I felt, oh, there's something known as me, even though maybe that's not the language
[489.06 → 489.80] I used.
[490.56 → 495.20] And, you know, and for us taking baby steps in AI, right?
[495.22 → 496.08] That's so fascinating.
[496.20 → 501.52] How do kids learn so quickly, learn so intuitively, come up with all these developments,
[501.52 → 502.64] in their personality?
[503.02 → 503.26] Yes.
[503.60 → 507.50] There are so many things that we kind of take for granted as humans.
[508.66 → 514.22] And ironically, those of us now in the AI space look back with kind of incredulity,
[514.30 → 517.96] you know, in terms of saying, wow, you know, you don't think about that, but there's so
[517.96 → 522.24] much there that we're trying to discover now in the field of AI so that we can do amazing
[522.24 → 522.68] things.
[523.02 → 523.26] Yeah.
[523.40 → 527.86] And I would say we are still quite far away from getting anywhere close to that, right?
[528.30 → 530.84] But that's what will keep me employed for a lifetime.
[530.84 → 531.68] There you go.
[531.78 → 532.86] Job security right there.
[533.72 → 539.96] But yeah, so going from those very early childhood memories and, you know, like getting
[539.96 → 545.16] fascinated about math and all the way through like high school, right?
[545.20 → 551.02] I was just, you know, getting into like math and all the time it was, oh, let's, you know,
[551.08 → 552.04] what's the next thing?
[552.22 → 556.20] You know, like I was remembered like, oh, there were, you know, number systems and then there
[556.20 → 557.46] was suddenly complex number.
[557.46 → 558.48] And this is imaginary.
[558.88 → 561.30] Oh, you can even make up things in math, right?
[561.36 → 566.70] Before that, you think math is just concrete, and you can't make up things in math.
[566.80 → 570.78] But imaginary number is something we make up, but it's so powerful in the way we use it.
[570.78 → 579.98] So as a kid, the tangible aspects of math, looking at machines, working and realizing there was math involved and having your parents and grandparents influence that.
[580.38 → 588.86] But then it sounds like you, as you grew in mathematics and learn more and more, the abstract nature really appealed to you, it sounds like.
[588.86 → 589.84] Exactly, right.
[589.94 → 593.80] So these, you know, there is structure in the way we build math.
[594.02 → 600.06] We, you know, first start with a specific goal of counting numbers, but we said, oh, this is not enough, right?
[600.08 → 601.78] We need to expand our number systems.
[601.98 → 608.34] We then had rational, and then we said it's, you know, we also need irrational numbers and real and then complex.
[608.34 → 615.18] So it tends to get increasingly more abstract, but then it has all these applications that wouldn't be possible without it.
[615.24 → 616.58] And that's what fascinated me.
[616.96 → 622.84] It's almost like, you know, the math, even though I cannot directly, you know, relate to it, right?
[622.86 → 624.12] I can't visualize it.
[624.24 → 626.48] I can still use it in many interesting ways.
[626.80 → 630.50] And that's when I, you know, thought like abstract thinking is important, right?
[630.52 → 634.66] I shouldn't always try to get it into something physically that I can relate to.
[634.72 → 635.66] I don't need that.
[635.66 → 644.26] So as you're growing up through this process and becoming more and more proficient in mathematics through school and through home life and such,
[645.24 → 649.92] did you retain that passion for the engineering that you had as a child?
[650.22 → 655.90] Did that drive or did you get more into just the pure mathematical passion that you were discovering?
[656.56 → 657.80] No, that's a good point.
[658.24 → 663.54] So my mom and dad would take me to different, you know, industry meetings.
[663.54 → 666.34] So we'd go to like these big trade shows, right?
[666.42 → 668.72] Like GTC, but for manufacturing.
[669.54 → 676.16] And so I'd be seeing all these fascinating, like, you know, the latest machines, the computerized numerically controlled machines.
[676.64 → 682.86] You know, back then, if you remember, it was like the green screen, and it only had like some simple programs you could write, right?
[682.88 → 686.00] In terms of the capabilities, it was like, okay, which axis do you go?
[686.00 → 691.28] So what would be the set of movements of this turret that would go and which tooling do you use, right?
[691.38 → 696.58] But to me, like, oh, wow, you can program, and now you can change material, right?
[696.86 → 700.98] And this is done in such an automated way.
[701.52 → 706.56] And that was my introduction to programming, which is very non-orthodox way of thinking of programming.
[706.56 → 709.92] And about how old would you have been as you really started expressing yourself in programming?
[710.38 → 715.26] I think this, I would have been more around eight or so.
[715.44 → 717.70] Yeah, so you're still quite young at that point in time.
[718.12 → 718.48] Okay.
[718.84 → 725.16] And so, I mean, by that time, did you pretty well know that you were, this was the path that you were on as you grew up?
[725.16 → 727.48] Or were you still kind of finding yourself?
[727.96 → 729.20] So I was still dancing.
[729.50 → 730.80] I always loved dance.
[730.80 → 735.80] I should say, you know, much of my family is engineers and mathematicians, right?
[736.02 → 742.86] So although my uncle is a biotechnologist, so I would like, you know, hear from him, you know, advances in biology.
[743.32 → 746.94] So no one really put me in any one path.
[747.34 → 752.44] For me, I was generally, you know, fascinated with science and technology, math and engineering.
[752.44 → 760.10] But at that point, I was, you know, looking at documentaries, for instance, about NASA and space.
[760.36 → 765.58] And, you know, that's how Caltech actually, you know, I remember thinking like, oh, that's such a fascinating place.
[765.74 → 776.24] So for me to kind of go from there to actually be at Caltech and be at NVIDIA that's making these cutting-edge technology to enable AI is a big leap.
[776.46 → 778.88] So I guess, so you got to Caltech as an undergraduate then?
[779.18 → 780.06] No, I didn't.
[780.06 → 788.06] So how did you make that shift as you're, you know, coming through your teenage years, and it's time to pick universities?
[788.48 → 791.10] Where did you go, and what caused that decision-making process?
[791.44 → 792.16] Yeah, yeah.
[792.22 → 797.28] So I was in high school and, you know, at that point, so I was back in India, right?
[797.46 → 800.66] So, and, you know, I was looking at the local colleges.
[800.66 → 805.14] I think at that point, I was still not ready to come halfway around the world.
[805.14 → 818.08] And, you know, these Indian Institute of Science, Technology, sorry, or the Its had this really difficult entrance exam to enter them because they're highly selective.
[818.08 → 821.74] They, it's like, you know, I forget the exact number.
[821.84 → 825.08] It's some huge number, maybe 500,000 students take that.
[825.32 → 837.38] And you had to be in the top 500 or so or 600, at least when I was doing it, to be like in computer science or electrical engineering or some major that you would like to pick.
[837.38 → 842.42] And, you know, so I remember hearing about this exam in high school, right?
[842.50 → 845.78] And my first reaction was, why is that so difficult?
[845.96 → 848.04] What makes it difficult, right?
[848.18 → 853.54] I mean, why, oh, it's like, oh, it's because it's very, somebody would tell me, oh, because it has difficult math.
[853.62 → 855.52] I'm like, really, what is difficult math?
[855.52 → 861.66] You know, I, just in my own experience, I think that is a fairly unusual reaction to these tests.
[861.76 → 865.24] Most of, most of us just go, oh, my God, I have to, I have a hard test.
[865.32 → 867.36] I got to go figure out and study for it and everything.
[867.50 → 868.54] So it's interesting.
[868.64 → 874.58] You're already analyzing the test itself in terms of whether the difficulty and how to apply yourself to it.
[874.58 → 888.70] Yeah, but also I was like, oh, I really want to like to learn something where I would be challenged, right, to be honest, because maybe because I had like, you know, this lot of help from my family.
[889.08 → 894.52] And I was reading books like beyond like my schooling requirements.
[894.52 → 903.26] So I felt honestly like, oh, I need to do more that, you know, that would really help me get to like, you know, things I would see in the real world, right?
[903.26 → 907.72] Like these machines that work or, you know, I'd look at these documentaries about the space.
[907.86 → 913.78] Like I was having this huge gap about the math I'm doing in school, and how is this possible today?
[914.64 → 923.86] So I guess is you, so which school did you start into your undergraduate work and did you, and did you select mathematics as your major or?
[924.04 → 925.24] So this was IAT.
[925.50 → 929.42] So they only had engineering as most of their majors, right?
[929.42 → 931.34] So I did take electrical engineering.
[931.34 → 937.68] And that to me was a nice sweet spot of where, you know, I would like be using a lot of math.
[937.96 → 939.54] Like I would be analyzing signals.
[939.78 → 941.44] I would still be connected to the hardware.
[941.74 → 941.90] Yeah.
[942.00 → 942.20] Right.
[942.28 → 942.36] That speaks to it.
[942.36 → 945.02] You're going back to that three-year-old seeing the machine working right there.
[945.20 → 945.22] Yeah.
[945.32 → 946.58] And I would still be programming.
[946.96 → 951.00] I would be doing, you know, and it was, and I was a minor in computer science.
[951.00 → 954.44] So I'd have all these different elements put together.
[954.44 → 963.52] And so, you know, that's where this entrance exam, I felt, was an opportunity for me to really go into, like, you know, when we look at physics, right?
[963.60 → 965.20] Like what are the basic principles?
[965.20 → 973.06] Like how not only, like, you know, know about the laws of physics, but how do I apply to different systems?
[973.06 → 981.84] Because, like, what made this test challenging was, you know, at least at that point, you know, those were near to, like, Olympia-level questions.
[982.10 → 982.22] Yeah.
[982.30 → 983.94] And why are those questions challenging?
[984.10 → 989.36] That's because they're not the usual ones you would solve during your assignment or during your usual schooling.
[989.36 → 994.90] So did you dive heavily into physics at your university schooling at that point?
[995.00 → 998.48] Had you been exposed to it prior to university at all?
[998.54 → 1001.30] Or was this kind of new area that you wanted to delve into?
[1001.30 → 1003.36] I mean, this was the entrance exam to get into the university.
[1003.38 → 1004.48] Oh, to get into your undergraduate.
[1004.52 → 1004.72] Yeah.
[1004.72 → 1005.54] I misunderstood that.
[1005.54 → 1005.98] I apologize.
[1006.22 → 1006.34] Okay.
[1006.46 → 1006.72] So no.
[1006.98 → 1009.36] So it was physics, chemistry, and mathematics.
[1009.54 → 1012.10] So all these three, you had to dive deep into it.
[1012.72 → 1019.00] And so when I was faced with these difficult questions, that's when I had to really go back and understand the principle, right?
[1019.00 → 1022.34] If I had misunderstood it, I could not apply it to solve the problem.
[1022.80 → 1028.64] As you're approaching university, that is a fantastic story, even up to that point.
[1028.70 → 1029.76] It's truly inspiring.
[1030.62 → 1034.48] And I hope people will share that with their daughters like I will.
[1035.40 → 1038.42] As you got into university, how did you evolve at that point?
[1038.60 → 1039.92] You know, you're in it now.
[1040.04 → 1041.20] You're in your schooling.
[1041.42 → 1045.20] At some point, I know you would have come to the United States and ended up at Caltech.
[1045.38 → 1046.80] Tell me how that process happened.
[1047.08 → 1047.24] Yeah.
[1047.24 → 1053.04] So once I was at IAT, you know, was just surrounded with a lot of amazing people, right?
[1053.12 → 1062.44] Like the faculty, the students, you know, they've all come, you know, all the other students have come through the difficult test as well, right?
[1062.56 → 1066.72] But, you know, but I found so many amazing friends that I still keep in touch.
[1066.72 → 1076.62] And what fascinated there was, you know, we all share this common vision to ask how technology could help society, could help us have a better future.
[1076.62 → 1081.32] So I remember being very involved in this tech fest called Shasta.
[1081.50 → 1086.42] That's the annual festival that IAT Madras, where I went to school, throws.
[1086.90 → 1090.86] And we were asking, okay, what would it, you know, how do we bring in more students here?
[1090.96 → 1093.52] What kind of contest would be good?
[1093.62 → 1095.58] Where do we get the best speakers, right?
[1095.58 → 1097.30] What are the best researchers today?
[1097.78 → 1099.02] How do we get them here?
[1099.54 → 1108.06] And so to me, that was one of the highlights on, you know, how seeing this community come together and ask, you know, how do we showcase today's technology?
[1108.18 → 1110.62] Where is that going in future?
[1110.62 → 1116.72] And so that was that kind of community togetherness is what I experienced at IAT.
[1117.74 → 1128.84] And part of that was also asking, you know, at that point, I was doing research both in my undergrad school, also in Indian Institute of Science, which is in Bangalore.
[1128.84 → 1138.70] And that's when, oh, my God, this is I have so much freedom to think and to ask, you know, what's what I could be doing innovatively, right?
[1138.74 → 1142.34] What's missing today and what I could make a difference.
[1142.52 → 1142.64] Yeah.
[1142.70 → 1146.30] And create something myself and that can make a difference.
[1146.88 → 1155.14] And so during my junior year, I did this undergraduate research experience, an equivalent of what we call surf here.
[1155.22 → 1155.48] OK.
[1155.48 → 1159.30] And that summer undergraduate research fellowship.
[1159.66 → 1159.88] Right.
[1159.94 → 1161.82] So there's a similar program back in India.
[1162.00 → 1165.48] And that's when I decided I just needed to do a Ph.D.
[1165.48 → 1169.16] I had to, you know, dedicate that time to go deep into something.
[1169.40 → 1169.66] Right.
[1170.60 → 1179.04] And, you know, really being, you know, and who knows, that was the adventure because what I could do there, I didn't know.
[1179.18 → 1181.40] But the possibility seemed so exciting.
[1181.40 → 1184.36] Did you feel did you feel that you wanted to go?
[1184.36 → 1188.64] I mean, what Caltech being the world-class school it is, did that draw you at that point in time?
[1188.70 → 1190.88] Was that the natural next progression in your own growth?
[1191.00 → 1191.14] Yeah.
[1191.22 → 1193.64] So I applied to quite a few schools.
[1193.84 → 1196.96] So I ended up at Cornell University.
[1197.64 → 1201.14] So Caltech is where, you know, I think I did apply there.
[1201.26 → 1202.72] But Caltech is a smaller school.
[1202.82 → 1203.02] Right.
[1203.02 → 1205.42] So we are highly selective.
[1205.56 → 1206.78] But I'm glad I'm there now.
[1207.14 → 1207.90] Your idea.
[1208.14 → 1208.34] Yeah.
[1208.40 → 1212.14] Your idea of, you know, schools, they're all world-class schools that you're naming here.
[1212.24 → 1219.38] So it's its good to have that kind of problem to figure out which of those schools you're going to go to.
[1219.52 → 1221.34] So you got to Cornell first then.
[1221.52 → 1222.32] Yes, that's right.
[1222.42 → 1223.86] And so tell us from there.
[1224.24 → 1224.48] Yeah.
[1224.48 → 1230.04] So, you know, when I arrived at Cornell, it's just this beautiful place.
[1230.16 → 1230.36] Right.
[1230.42 → 1232.58] It is in the middle of nowhere, but it's nice.
[1232.68 → 1234.70] It's a lot of natural surroundings.
[1235.00 → 1235.64] It's called Ithaca.
[1235.78 → 1236.28] It's gorgeous.
[1236.52 → 1237.46] Good for thinking, right?
[1237.72 → 1238.58] Just birds.
[1238.58 → 1241.32] I mean, I did arrive in early fall, which.
[1242.76 → 1248.80] But, you know, I mean, it's like to me a place where, you know, like there's a lot of close-knit community.
[1248.96 → 1253.84] Like my advisor Lang Tong just was such a wonderful human being.
[1253.94 → 1259.90] He would like, you know, give me the freedom to think and grow and say he wouldn't say, oh, no, this doesn't work.
[1259.94 → 1261.02] He's never told me that.
[1261.08 → 1261.22] Right.
[1261.24 → 1262.78] He would be like, go figure it out.
[1262.78 → 1268.96] And then he would be like, oh, you know, like if it didn't work, he would be like, oh, why not?
[1269.12 → 1269.30] Right.
[1269.38 → 1273.60] Like so we'd have this very open conversation and very.
[1274.30 → 1287.22] And so honestly, he really motivated me to be a professor because when I saw him, like how he, you know, deals with students and the kind of lifestyle he has in terms of really being able to think openly.
[1287.50 → 1289.86] So you were in your Ph.D. program at this point?
[1289.96 → 1290.40] That's right.
[1290.48 → 1290.74] OK.
[1290.74 → 1291.84] That's right at Cornell.
[1292.12 → 1292.22] OK.
[1292.22 → 1296.08] And, you know, so that's when I was going to conferences.
[1296.08 → 1301.32] I was meeting other researchers and to share these ideas openly.
[1302.00 → 1314.04] That's what, you know, I decided at that point when I was graduating that I wanted to be in academia because back then, you know, like AI really hadn't taken off the way it is today.
[1314.14 → 1314.42] Right.
[1314.48 → 1320.16] So there were very few, almost no industry, industrial research in machine learning and AI.
[1320.16 → 1324.80] And as we're as we talk about that, because we're kind of now turning explicitly to AI.
[1324.80 → 1328.22] What was it being at what point in that process?
[1328.22 → 1330.74] Because we were talking about the math and the engineering for a while.
[1330.90 → 1335.78] At what point did you realize AI was the area that you wanted to focus on?
[1335.96 → 1337.42] When did that happen in that process?
[1337.62 → 1337.64] Yeah.
[1337.64 → 1342.30] So, in fact, it happened during my early Ph.D. itself.
[1342.82 → 1342.90] Right.
[1343.10 → 1347.62] So, I mean, Lang Tong is an expert in wireless networks and wireless communications.
[1348.46 → 1354.42] And back then we were, you know, as thinking about all these challenges of how to communicate over wireless channels.
[1354.42 → 1354.88] Right.
[1354.88 → 1357.12] But the question is also what do you communicate?
[1357.68 → 1363.20] And during that point, the question was, what if you just didn't blindly send all the data?
[1363.38 → 1370.12] If you could, like, make inferences, if you could make decisions on what's really relevant, you could really reduce how much you communicate.
[1370.90 → 1377.62] So I came into it from that viewpoint of, you know, how to reduce requirements in communications.
[1377.62 → 1378.02] Right.
[1378.06 → 1380.38] Which is not a traditional way of getting into AI.
[1380.38 → 1384.42] But I've never taken a traditional path in many ways.
[1384.54 → 1384.80] Clearly.
[1385.42 → 1386.74] So, yeah.
[1386.92 → 1394.52] So, and that's where, you know, it led me to asking, okay, now we need to then do some inferences.
[1394.72 → 1394.94] Right.
[1394.98 → 1397.72] I need to now think about machine learning techniques.
[1397.84 → 1403.16] You know, we called it statistical inference and estimation and more of this traditional signal processing community.
[1403.16 → 1405.60] But the tools are that foundation is the same.
[1405.70 → 1405.94] Yes.
[1406.04 → 1406.28] Right.
[1406.28 → 1418.14] So, and so that was my first project on how do we do distributed learning, like where there are a number of sensors and joint, like they don't need to communicate all the raw data they collect.
[1418.34 → 1418.58] Okay.
[1418.60 → 1424.50] But they only communicate after making some inferences what's truly relevant to your problem.
[1424.68 → 1424.78] Right.
[1424.78 → 1425.14] Understood.
[1425.20 → 1435.88] Let's say if there is, you know, it's measuring the temperature and there's something anomalous, maybe you only want to communicate that anomalous behaviour and not just keep communicating all the time.
[1435.88 → 1438.74] And so did you get your PhD from Cornell?
[1439.32 → 1439.76] Yes.
[1440.48 → 1443.48] And then specifically, what was the what was the PhD in?
[1443.66 → 1447.64] By the time you finished this long process, actually finishing is probably the wrong word.
[1447.74 → 1450.32] But as you got to this point in the journey.
[1450.44 → 1450.64] Yeah.
[1450.78 → 1451.78] What was your PhD in?
[1451.78 → 1452.00] Yeah.
[1452.00 → 1459.40] So my thesis title, if I recall, right, it's been a decade now, is distributed statistical inference.
[1460.00 → 1460.58] So, yeah.
[1460.68 → 1467.54] So my first project led to many other projects of, you know, how do you like route this in an energy efficient way in a network?
[1467.54 → 1473.54] And how do you model correlations across different sensors in useful ways, right?
[1473.58 → 1479.12] And that's when it got into this large scale machine learning because we said, oh, there should be like dependencies.
[1479.40 → 1481.06] Like what do these correlations mean?
[1481.18 → 1487.48] There should be an underlying what we call a graphical model, a probabilistic model that connects all these measurements.
[1487.48 → 1493.08] And now that's when I started getting fascinated into all the literature of machine learning, right?
[1493.16 → 1495.00] That's kind of considered core machine learning.
[1495.62 → 1499.60] And, you know, I met Alan Wil sky, who's a professor at MIT.
[1499.74 → 1500.58] Now he's retired.
[1501.10 → 1504.84] I had a conference and my advisor said, oh, just go visit him, right?
[1504.94 → 1512.00] So I took the my whole last year was actually spent at MIT because he's the expert in graphical models.
[1512.00 → 1513.90] And I wanted to dive deep into that.
[1513.90 → 1524.38] And that's when I truly started publishing in machine learning conferences, you know, at the end of my PhD and when I had a faculty job.
[1524.48 → 1533.10] So I kind of made a switch in terms of which communities I was publishing, although the core, you know, math was very much connected and related.
[1533.10 → 1537.82] So I didn't feel it's a big switch, but a lot of people felt, you know, really surprised.
[1538.08 → 1543.10] What, you're starting your faculty career, and you're suddenly going to these new conferences, right?
[1543.10 → 1550.82] And back then, these main machine learning conferences, you know, back then was called NIPS, and now it's called Neurons and ICML were tiny events.
[1551.24 → 1553.36] And signal processing events were much bigger.
[1553.74 → 1556.48] And so many people were wondering why I made the switch.
[1556.72 → 1561.76] And for me, it's always been about where the core intellectual ideas are, right?
[1561.80 → 1563.58] And where there's a lot of potential to me.
[1563.72 → 1566.98] I felt, you know, this machine learning revolution has to happen.
[1566.98 → 1568.68] It's just a matter of when.
[1569.78 → 1576.36] And so I'm happy I, you know, I went into like core machine learning before it all took off.
[1576.36 → 1590.84] The Data Engineering Podcast is a weekly deep dive on modern data management with the engineers and entrepreneurs who are shaping the industry.
[1590.84 → 1599.44] Go behind the scenes on the tools, techniques, and difficulties of data engineering so you can learn and keep up with the knowledge to make you and your business successful.
[1599.44 → 1607.32] Can you give a bit of an outline about the motivation for choosing Jupyter Notebooks in particular as the core interface for your data teams?
[1607.68 → 1607.86] Yeah.
[1608.00 → 1611.98] And actually, when I first joined Netflix, it was sort of tossed at me.
[1612.16 → 1613.76] And I was definitely like, well, are we crazy?
[1614.00 → 1615.66] And the answer was like, we might be a little crazy.
[1616.16 → 1622.48] Go to dataengineeringpodcast.com to listen, subscribe, and share it with your friends and colleagues.
[1629.44 → 1641.40] So let's, now that you've finished your PhD, let's turn toward you're now out there.
[1641.40 → 1646.74] You have your PhD, your faculty, and you are doing work in the space.
[1647.78 → 1652.06] How did you, how did you arrive at Caltech?
[1652.80 → 1657.96] There are a couple of questions I'll ask you about when you get there and then ultimately at NVIDIA.
[1657.96 → 1661.82] And then after all that, I'm going to turn you toward your talks itself down the road.
[1662.14 → 1665.52] But can you tell me, how did you, how did you move over to Caltech?
[1665.64 → 1666.92] What made that transition?
[1666.94 → 1668.52] I'm still not at Caltech.
[1668.72 → 1669.56] Oh, I'm sorry.
[1669.70 → 1670.02] Okay.
[1670.78 → 1671.58] No, no.
[1671.74 → 1674.52] That's what makes this a fascinating story, right?
[1675.08 → 1676.34] There's still suspense.
[1676.62 → 1678.16] So there's still a ways to go.
[1678.22 → 1678.48] Yeah.
[1678.64 → 1679.78] I see I'm rushing your story.
[1680.84 → 1681.64] Terrible of me.
[1681.64 → 1687.32] I actually started at UC Irvine, which is not far from Caltech, right?
[1687.42 → 1694.20] So again, Southern California, like, you know, again, a beautiful place and a lot of really amazing college.
[1694.20 → 1698.46] If the listeners could see my face right now, I'm blushing for having done that.
[1698.52 → 1699.44] But anyway, keep going.
[1699.56 → 1700.20] Sorry about that.
[1700.20 → 1702.88] No, but yeah.
[1703.12 → 1709.56] And as I said, I was getting into this new field in the sense of publishing, right?
[1709.62 → 1711.86] Like these new conferences, new people.
[1712.86 → 1716.04] And yeah, so there was a bit of me that was stressed.
[1716.14 → 1716.56] Oh, my God.
[1716.60 → 1719.50] I'm starting this faculty life and doing this.
[1719.92 → 1722.86] But, you know, there were just truly fascinating problems.
[1722.86 → 1726.66] I was looking at these probabilistic models and asking questions, right?
[1727.00 → 1729.98] You know, when can you learn these models at scale, right?
[1730.28 → 1734.02] And what do you mean, like, there's a correlation between these models?
[1734.36 → 1738.42] You know, are there a few variables that can summarize the effects?
[1738.58 → 1742.02] And that's when I got introduced into latent variables.
[1742.62 → 1745.92] You know, the idea that we can't measure everything in this world, right?
[1745.94 → 1747.50] There's always going to be something hidden.
[1748.18 → 1750.90] But it's the hidden thing is what maybe we are really after.
[1750.90 → 1754.04] That's what we'd like to learn, but we can't directly measure it.
[1754.32 → 1758.70] That seems, based on your inquisitive nature, you know, talking from childhood up,
[1758.92 → 1762.20] I'm not at all surprised to know that that's what you were going after.
[1762.32 → 1763.94] I'm always after the hidden things.
[1764.16 → 1764.70] The next thing.
[1764.82 → 1765.82] What makes that work?
[1766.00 → 1766.20] Yeah.
[1766.32 → 1766.86] So keep going.
[1767.18 → 1767.46] Yeah.
[1767.60 → 1773.94] So I was looking into these, what we call latent variable estimation, right?
[1774.02 → 1778.44] Think about, you know, like understanding text, right?
[1778.44 → 1781.48] In the last few years, we made a lot of progress.
[1782.36 → 1785.74] But you want to ask, like, what do I really want to extract from this text?
[1785.82 → 1786.46] It's the meaning.
[1786.82 → 1789.36] It's like the topics that are discussed in the text, right?
[1789.54 → 1795.68] But, you know, as human beings, no one, even if that word is not even there, you can extract what the topic is, right?
[1795.68 → 1803.22] And that level of, like, extraction is hard because, you know, we don't understand all the nuances of the language now through machines.
[1803.22 → 1804.60] Absolutely. We're struggling with that now.
[1804.70 → 1804.84] Yes.
[1804.84 → 1811.12] That's a big part of research in AI with a couple of interesting, you know, things that have happened in NLP news lately.
[1811.34 → 1812.04] But keep going.
[1812.10 → 1813.32] Yeah, exactly, right?
[1813.32 → 1818.94] So doing it in a fully generative way, like generate language and all its nuances is hard.
[1819.42 → 1823.70] And that's where I think simplicity, there's something to be said about that, right?
[1823.76 → 1826.66] So back then, deep learning was not there, right?
[1826.88 → 1834.20] And with these models and with to compute we had, and even today, actually, in fact, that's the state-of-the-art results.
[1834.20 → 1844.50] When it comes to categorizing large documents, you have these lengthy, let's say, news articles or your reports, and they could be in the millions, right?
[1844.52 → 1846.02] And all you have is this raw text.
[1846.12 → 1848.36] Maybe you have a bit of metadata, but not much.
[1848.74 → 1851.42] So you can't go laboriously, even provide examples.
[1851.56 → 1857.94] You can't go annotate each word and say, oh, this is representative of topic, let's say, justice.
[1857.94 → 1859.88] This is representative of education.
[1859.88 → 1863.52] This is representative of geography.
[1863.88 → 1868.30] You can't go manually annotate each document of what it represents, right?
[1868.38 → 1873.62] And then ultimately even each word because you want representative words for each topic.
[1874.32 → 1878.46] And so this is called unsupervised learning where we don't have these examples.
[1879.12 → 1886.26] Like no one's telling you what a topic should look like and how you should categorize your document into multiple topics.
[1886.26 → 1892.44] Even now, as fully into the age of deep learning, that is still a huge push.
[1893.04 → 1895.08] That's where so much of the research is right now.
[1895.92 → 1896.66] So keep going.
[1896.80 → 1896.92] Yeah.
[1897.44 → 1898.70] And exactly.
[1899.08 → 1903.12] And so back then, the question was, what's the simplest thing you can do there, right?
[1903.12 → 1914.24] So that's always like I tell my students and I tell my colleagues and all the researchers I work with is how, you know, first think about the simplest thing you can do.
[1914.42 → 1917.48] And if it doesn't work, then go to more and more complex, right?
[1917.52 → 1924.40] Because one of the dangers, which I'll come to later with deep learning, is you may just overtly get it complicated and not understand what's going on.
[1924.40 → 1926.20] You sound like an engineer when you say that.
[1926.28 → 1928.40] I mean, I can totally see that background there.
[1928.40 → 1931.48] You know, start with the simple, I, you, yeah.
[1932.02 → 1938.36] Yeah, no, I have a lot of respect for the traditional engineering that, you know, makes aircraft fly today.
[1938.86 → 1942.96] And all the, you know, transportation structures, everything, right?
[1942.98 → 1947.32] There's a lot, I think, which will come to my latest part in the end about my talk.
[1947.62 → 1949.52] It's blending the old and the new together.
[1949.52 → 1960.78] So anyway, coming back to this top, how to extract topics from documents and automatically categorize documents at scale in an unsupervised way.
[1961.54 → 1966.54] A simple intuition is, right, what if you look at frequency of words, right?
[1966.70 → 1968.86] Let's say the word apple occurs a lot.
[1968.96 → 1976.26] If I just told you this, then it would be like, huh, it could be about a fruit, or it could be about a company, right?
[1976.26 → 1977.72] So it's like not enough.
[1977.72 → 1984.04] Then you could say, I tell you that what if word apple and orange occurs in the document.
[1984.16 → 1984.94] It changes the content.
[1985.08 → 1986.86] You suddenly have a little bit of understanding.
[1987.20 → 1988.56] Yeah, you have more information.
[1989.60 → 1994.82] But, you know, orange is also a company, but maybe, you know, both of them may not occur that much together.
[1995.24 → 1997.52] And so then you could go to three words, right?
[1997.56 → 2000.28] You could say like apple, orange, and banana.
[2000.50 → 2004.64] And then now it's like, oh, it is really a fruit, something about fruits, right?
[2004.64 → 2017.36] So the more what we call co-occurrences, if you now look at how multiple words occur in the document together, then you can make better inferences of what the document is talking about, right?
[2017.62 → 2020.98] And note that no one is telling the algorithm, right?
[2021.04 → 2025.96] No one is writing down every triplet and saying, oh, if it's apple, orange, banana, call it fruits.
[2025.96 → 2030.22] I mean, we can't possibly do this in full scale, right?
[2030.28 → 2033.38] The size of English vocabulary is more than 100,000.
[2033.64 → 2035.44] And it's cubic in 100,000.
[2035.68 → 2039.28] So there is just no way we would ever be able to do this manually.
[2039.82 → 2042.32] And now the question is, where does math help us here?
[2042.32 → 2051.32] And the intuition of, you know, and this has kind of been there underlying almost all machine learning, right?
[2051.70 → 2052.94] Where is all the energy?
[2053.22 → 2054.80] Where is like the strong signal?
[2055.22 → 2062.62] If I can, you know, extract that strong signal, then I can really, you know, do this without writing down all the rules, right?
[2062.62 → 2068.66] The most basic algorithm, or I wouldn't call it basic because it was sophisticated for its time, right?
[2068.70 → 2071.44] It's principal component analysis or PCA.
[2071.76 → 2075.28] That's where we say, oh, this data could have a lot of noise.
[2075.40 → 2081.52] I'm going to filter out the noise by looking at only the subspace in which majority of the signal lies in, right?
[2081.90 → 2086.96] And so it's the same principle that underlies a lot of what I did at that time.
[2087.04 → 2090.26] But it was now taking it to more dimensions, into tensors.
[2090.26 → 2092.72] And, you know, how I...
[2092.72 → 2095.42] And can you identify for the audience what a tensor is?
[2095.62 → 2097.90] So a tensor is an extension of a matrix.
[2098.24 → 2100.60] You can think of it as a multidimensional array.
[2101.00 → 2106.80] So just as matrix has rows and columns, now it has more dimensions in a tensor, right?
[2106.90 → 2111.86] But just as you multiply matrices, you can also now multiply and operate and trend tensors.
[2112.04 → 2119.46] And so there's a whole algebra you can build around it, which gives a rich set of operations on which you can build algorithms.
[2119.86 → 2119.98] Sure.
[2120.26 → 2124.92] So, at this point, where are you working as we're...
[2124.92 → 2126.28] Because we've kind of talked about the work.
[2126.40 → 2127.72] Are you...
[2127.72 → 2130.28] What institution are you at this point?
[2130.40 → 2130.58] Yeah.
[2130.68 → 2132.12] So I'm still at UC Irvine.
[2132.28 → 2133.74] Although I took a break.
[2133.94 → 2138.82] This particular work when I first started doing tensors was in Microsoft Research.
[2138.82 → 2146.62] And, you know, Microsoft Research, you know, like even now in the East Coast, this is headed by Jennifer Chase.
[2147.12 → 2149.34] And again, an amazing role model, right?
[2149.42 → 2150.74] Both for women and men.
[2150.74 → 2153.56] And she wants to encourage open research.
[2153.96 → 2155.00] And I went there.
[2155.08 → 2155.84] I gave a talk.
[2155.96 → 2160.38] I gave a talk on one of my earlier topics that works on statistical physics.
[2160.38 → 2161.96] And her background is physics.
[2162.22 → 2163.56] And she was so fascinated.
[2163.72 → 2164.90] I used it in machine learning.
[2165.08 → 2168.32] There was not a connection that many people made before.
[2168.32 → 2170.24] And so she was like, oh, come over.
[2170.40 → 2171.16] Just hang out.
[2171.28 → 2172.12] Talk to researchers.
[2172.66 → 2173.90] See what comes out, right?
[2173.90 → 2174.98] So we had no agenda.
[2176.18 → 2181.62] And there was Sham Kaka day and Daniel Hsu and many other researchers around.
[2181.88 → 2186.58] And one day we started bouncing ideas about, okay, there is PCA, right?
[2186.66 → 2188.38] This kind of algorithm on matrices.
[2189.14 → 2194.88] Now, you know, this topic modelling, which is now looking at trying to extract topics.
[2195.10 → 2196.12] You know, is that enough?
[2196.26 → 2197.34] And if not, why not?
[2197.40 → 2198.66] Why should we need more?
[2199.06 → 2203.26] And that's kind of how, you know, I'm not an expert on tensors at that point.
[2203.26 → 2207.30] Nobody is because we don't really study that in undergraduate, right?
[2207.42 → 2216.40] But this kind of, I think, asking questions is where you suddenly, you know, lead into a whole new direction and whole new area that's completely unexpected.
[2216.70 → 2217.74] And is that what happened to you?
[2217.82 → 2218.12] Yes.
[2218.52 → 2220.46] So what was the next step then?
[2220.70 → 2220.90] Yeah.
[2221.02 → 2226.22] So once, you know, these tensors, we realized, oh, there is a rich history.
[2226.22 → 2234.04] In fact, it was back in the 1900s that Spearman asked questions about intelligence and tried to use tensors to solve them.
[2234.34 → 2237.78] And I mean, making a very rough simplification of what he did.
[2238.08 → 2246.76] But there is a very interesting connection where he said, oh, let's, you know, probably people have different sorts of intelligence as verbal intelligence and mathematical.
[2247.32 → 2250.34] Can I use this notion of tensors to try to separate the two?
[2250.44 → 2254.04] It's, again, separating these signals and finding these different directions.
[2254.04 → 2258.20] And it's similar to separating topics in our documents, right?
[2258.28 → 2259.86] There's this common underlying math.
[2259.86 → 2261.46] I love how you just connected that back there.
[2261.96 → 2262.52] Yeah.
[2262.60 → 2265.40] So there's math everywhere that connects things together.
[2266.36 → 2276.00] And that's what, you know, once I got into that history and got into, like, you know, Richard Feynman, Albert Einstein, right, in quantum networks.
[2276.32 → 2278.62] And there's just very much core of that.
[2278.62 → 2283.06] And then signal processing, like, for blind source separation, this was used.
[2283.38 → 2286.64] So it's looking at all this history and asking, okay, what's different now?
[2286.98 → 2289.84] What's different is we have a lot of data, right?
[2289.88 → 2291.86] We can now scale up our computation.
[2292.86 → 2301.08] And we can, you know, and we are now looking at, you know, even collecting different kinds of data, different modalities of data, right?
[2301.08 → 2305.36] Whereas in the earlier generations when tensors were used, there wasn't enough data.
[2305.94 → 2309.88] And so I felt like this is the right timing to really think about tensors.
[2310.24 → 2310.70] It is.
[2310.70 → 2318.48] So I guess at this point, are you into deep learning full or is it still in that?
[2318.48 → 2320.76] All this happened before deep learning took off.
[2320.76 → 2330.36] So, you know, there was, like, these few years when, you know, we were, like, thinking about, oh, how can I now apply tensors to these different probabilistic models, right?
[2330.40 → 2332.12] More and more challenging dependencies.
[2332.48 → 2335.04] Like, how do I learn communities of people?
[2335.18 → 2336.76] Like, you know, I look at friendship links.
[2336.76 → 2339.98] How do I know who's interested in what aspects, right?
[2340.04 → 2341.62] Like in social media and sense.
[2342.28 → 2345.16] So how did you make that leap into deep learning?
[2345.42 → 2350.16] At what point did you realize that was what you were going to be doing to carry your work forward?
[2350.16 → 2350.40] Yeah.
[2350.70 → 2361.88] And so, and as this was happening, right, so the early deep learning results came about, I would say, like, by around 2012 and 13, there were results.
[2362.64 → 2368.76] And, you know, so I was thinking about, like, analyzing optimization, like non-convex optimization, right?
[2369.28 → 2373.66] And, you know, these deep networks have highly non-convex optimization surfaces.
[2374.32 → 2381.70] But so much of my, even my theory and my experiments and the experience was telling we shouldn't be afraid of non-convex optimization.
[2382.36 → 2388.48] In fact, the tensor methods that we use are also highly non-convex, right?
[2388.48 → 2391.78] And that was kind of in the beginning, people were shooting us down.
[2391.90 → 2393.18] Oh, this is not convex.
[2393.26 → 2394.58] How do I know it works?
[2394.76 → 2397.08] You know, and we were like, we're showing you the results.
[2397.08 → 2399.48] It's like, but still, there's no proof.
[2399.78 → 2400.24] This works.
[2400.38 → 2403.36] And I'm like, oh, there's a proof, but it's under some conditions, right?
[2404.02 → 2411.20] And so it was, so I think that revolution was happening that convex is great, but so many things are not convex.
[2411.20 → 2415.76] And we can't just try to force things to be convex when they are not, right?
[2415.80 → 2417.46] We'd be limiting ourselves so much.
[2417.88 → 2418.04] Understood.
[2418.34 → 2423.90] So for the audience here, if you could see her, she is so passionate about what she's talking about.
[2424.34 → 2425.80] She's waving her arms around.
[2426.56 → 2429.52] It must be a delight to take classes from me for your students.
[2429.74 → 2431.00] So keep going.
[2431.34 → 2433.84] We're both smiling a lot because this is such a fact.
[2433.98 → 2438.60] And you've made my job so far as an interviewer so easy because you're so good at carrying it on.
[2438.60 → 2441.36] So tell us how you delved into it.
[2441.72 → 2442.36] Thanks, Chris.
[2442.56 → 2444.72] And I love talking about it.
[2444.78 → 2448.50] And by the way, my most recent class, I will make all the videos online.
[2448.68 → 2450.94] So you're welcome to go check them out.
[2451.16 → 2453.56] And we will put that into the show notes as they're available.
[2454.16 → 2458.18] So after you listen to the episode, you can go find and watch those.
[2458.98 → 2463.46] And, you know, to give like a brief intuition of convex versus non-convex, right?
[2463.46 → 2466.92] I mean, think of like the convex as this parable of like, you know,
[2466.92 → 2471.90] there is any pebble you slide from the top will only go to the bottom, right?
[2471.92 → 2476.44] It may oscillate a bit, but ultimately it'll, you know, settle all the way in the bottom.
[2476.76 → 2481.94] I mean, that's what essentially all these algorithms, optimization algorithms are analyzing, right?
[2481.96 → 2483.34] But now it's non-convex.
[2483.44 → 2487.24] It's many peaks and valleys, you know, like the natural landscapes.
[2487.24 → 2489.70] And so then you don't know where it's going.
[2490.22 → 2493.44] And that's what makes this challenging to analyze.
[2493.96 → 2497.66] And to me, this is again, like where between math and engineering, right?
[2497.70 → 2501.68] I don't want to solve problems just because they're easy for the math to solve.
[2501.78 → 2504.50] Like for the math, I understand I can express them.
[2504.96 → 2507.78] I don't want that to be the reason to solve a problem.
[2508.24 → 2508.28] Understood.
[2508.28 → 2514.34] And so when deep learning started taking off, that mirrored my experience that, you know,
[2514.38 → 2520.04] what I'd seen with tensors, which is also both are non-linear and both are non-convex,
[2520.18 → 2522.54] but things work very well in practice, right?
[2522.56 → 2526.88] And that's when I was, you know, right from the beginning, I was, yes, you know, this is,
[2527.16 → 2529.06] this should work very well, right?
[2529.06 → 2534.98] But at the same time, I think parts of it that I was, I'm still hesitant on is it's highly black box,
[2534.98 → 2538.68] you know, this requires a lot of data, but that's, those are the opportunities.
[2538.86 → 2541.20] So I was like, oh, there are, you know, this is great.
[2541.20 → 2546.86] Like what results we've seen now, but there is so much more we need to solve there.
[2547.20 → 2553.56] And so on of the first things we did there was to ask, okay, now what does it mean to have,
[2553.74 → 2556.54] you know, what is, where do tensors and deep learning come together?
[2556.80 → 2557.24] Right.
[2557.30 → 2560.82] I mean, that's natural because I understand one field very well.
[2560.82 → 2562.84] I know the other, and what is the connection?
[2562.84 → 2569.64] And, you know, and that's where we said, and I showed it in my talk on Monday,
[2570.10 → 2575.40] was asking, you know, like if you look at the current neural network models, right,
[2575.52 → 2579.16] they are processing, essentially it's matrix operation.
[2579.38 → 2580.84] You're multiplying two matrices.
[2581.16 → 2583.88] Convolution is still a form of like linear algebra.
[2584.38 → 2590.62] And that's because this methodology has been developed for our last, whatever, 60 years.
[2590.62 → 2594.80] So, you know, like we have linear algebra libraries that have been highly well-developed.
[2595.48 → 2599.82] And so that was the reason, one of the main reasons to build it as a foundation,
[2599.82 → 2601.14] even for our deep learning.
[2601.50 → 2607.50] So, and since you mentioned your Monday talk was the role of tensors in machine learning, right?
[2607.78 → 2608.18] That's right.
[2608.20 → 2611.64] And so go ahead and share with us a little bit about, you know, what you did there,
[2611.68 → 2613.58] because I think you're starting to go that way anyway here.
[2613.58 → 2614.64] Yes, exactly, right.
[2615.66 → 2622.02] And, you know, one aspect of the role of tensors was what I described earlier with these probabilistic models
[2622.02 → 2625.84] and how do we extract useful latent variable modelling.
[2626.74 → 2634.46] And so in this new one with deep learning, we asked, okay, why should it be only linear layers and linear algebra, right?
[2634.48 → 2636.38] We can do this higher order ones.
[2636.38 → 2637.86] And so what does that add?
[2638.16 → 2644.24] Like, you know, and that's when we found, like, you can get very high rates of compression of those networks
[2644.24 → 2646.30] and still get good accuracies.
[2647.10 → 2653.42] And so the intuition is if your data is in many dimensions, you'd rather also process it in many dimensions.
[2653.64 → 2654.50] That makes sense, yes.
[2654.50 → 2659.84] So why do we then limit all to two dimensions and just matrices when we go through the layers?
[2660.34 → 2662.84] And that's kind of the basic intuition.
[2662.84 → 2665.76] If you think about the image, it's width and height.
[2666.20 → 2669.26] And if it's a coloured image, it's now also RGB channels.
[2669.62 → 2673.84] And if it's going through these convolution layers, it's, you know, collecting more layers,
[2673.98 → 2676.42] it still has spatial structure, right?
[2676.52 → 2682.62] And then when it comes to fully connected layers, you destroy all that and you just do a matrix vector multiplication.
[2683.38 → 2690.06] So one of the first things we did was let's retain that 3D information throughout until the very end output.
[2690.06 → 2690.38] Okay.
[2690.54 → 2694.16] And design operations that we understand very well from tensors.
[2694.68 → 2697.58] And that showed a very high rate of compression.
[2698.24 → 2701.08] And that's when we said, oh, this is a natural thing.
[2701.34 → 2706.00] Things should come together because a deep network is nothing but a tensor operation.
[2706.18 → 2707.60] It's a big tensor in the end.
[2707.70 → 2707.90] Okay.
[2707.94 → 2708.92] You heard it here, folks.
[2708.96 → 2710.78] That was a great explanation for that.
[2710.78 → 2711.22] Yeah.
[2711.62 → 2712.06] Yeah.
[2712.56 → 2717.78] And, you know, so at that point, you know, I'm still not at NVIDIA.
[2717.86 → 2718.96] I'm still not at Caltech.
[2719.64 → 2721.76] But I'm getting closer now.
[2722.58 → 2726.06] So, you know, I was at my point of sabbatical.
[2726.22 → 2727.94] So I got my tenure at UC Irvine.
[2728.26 → 2731.88] And that's when, as the field is taking off, there's so much happening in industry.
[2731.88 → 2736.04] And AI is really getting built into practical applications.
[2736.04 → 2737.90] It's being deployed in the real world.
[2738.46 → 2740.36] And in industry, there's so much activity.
[2740.74 → 2746.50] And so I joined Amazon Web Services as a principal scientist in the AI team.
[2747.30 → 2753.36] So, you know, it was almost from the beginning when the AI services were getting launched into AWS.
[2753.36 → 2759.20] And that was, again, an amazing time because it's like, you know, what would an AI service look like, right?
[2760.00 → 2767.40] And we're also, like, doing all this in a very short amount of time because, you know, there's a lot of demand for AI services from the public.
[2767.52 → 2776.56] I am sitting here, even though you haven't even gotten to NVIDIA and Caltech yet, I'm just amazed at how much of the pioneering work that you were doing in space.
[2778.20 → 2779.80] You really stand out in that way.
[2779.90 → 2780.88] Thank you, Chris.
[2780.88 → 2788.12] And, you know, I think I've had amazing mentors and amazing support as well from the communities to enable that.
[2788.52 → 2790.70] And at Amazon, that's what I found.
[2790.90 → 2795.18] Like, I learned a lot in terms of, like, how do we, like, you know, think about the customer?
[2795.44 → 2796.30] What are the needs?
[2796.54 → 2801.34] You know, how do we have the short timeline to the product but still make the customer happy?
[2801.50 → 2803.90] What would the requirements be, right?
[2804.04 → 2810.40] And, like, PR FAQ, which is the press release with the FAQ is how we first think about the product.
[2810.40 → 2811.08] Right?
[2811.32 → 2814.48] And so that's, to me, so non-traditional.
[2815.00 → 2816.62] But, again, you know, I like that.
[2817.16 → 2818.04] So, yeah.
[2818.16 → 2822.38] So that was, again, an amazing and a very busy time there.
[2822.84 → 2829.66] You know, that's when, you know, I launched the topic detection algorithm that I described earlier to categorize documents.
[2829.66 → 2831.68] It's running today in the AWS cloud.
[2831.76 → 2832.04] Really?
[2832.04 → 2833.04] In the comprehensive.
[2833.04 → 2833.60] Exactly.
[2833.60 → 2834.72] So, yeah.
[2834.72 → 2839.54] And so, yeah, going from this basic theory all the way to something that's working.
[2839.54 → 2844.50] To applying it in a very real-world scenario that is touching a lot of people.
[2844.80 → 2845.12] Yes.
[2845.12 → 2858.30] And, you know, like, I was also managing an engineering team and looking into all the processes of the sprint, and how do we ensure good software engineering process, which was new to me because I was in academia before, right?
[2858.30 → 2864.32] So, it was a big learning process, and that's where there are a lot of great people who helped me learn new things.
[2864.96 → 2871.76] And, yeah, so seeing both the engineering side of it from a big production viewpoint and all the pain points.
[2871.76 → 2883.38] And this is where the SageMaker machine learning platform that got also discussed in the keynote yesterday when Jensen Huang invited Matt Garman from IS, right?
[2883.56 → 2884.36] I was part of the launch.
[2884.36 → 2887.06] And I've used SageMaker, so I now know.
[2887.50 → 2891.08] Yeah, so I was very much involved right from the beginning to the launch.
[2891.76 → 2895.82] And it's, yeah, so all that was great learning lessons.
[2895.82 → 2904.54] And that's when, at that point, I got an offer from Caltech when there's so much happening on Amazon and in industry in general, right?
[2904.62 → 2907.24] And that's when I asked, okay, what do I do?
[2907.30 → 2909.34] Because, you know, I'm in a great place right now.
[2909.70 → 2919.92] But I do think for the longer-term research and especially, like, going to the fundamental sciences, right, that's where, you know, Caltech in particular has such a strong strength.
[2919.92 → 2927.24] And for me, like, machine learning and artificial intelligence, for me, would make a true impact, right?
[2927.34 → 2929.04] I mean, not to downplay the other ones.
[2929.10 → 2930.84] The others are important to me.
[2930.96 → 2936.36] A holy grail would be, you know, what basic scientific discoveries can we make with that, right?
[2936.40 → 2941.32] If we can, like, truly enable that, and that can just have such transformative effects.
[2941.96 → 2944.50] So you're at Caltech now.
[2944.60 → 2944.74] Yeah.
[2944.74 → 2947.96] And I'm going to throw a little bit of a wild card in.
[2948.12 → 2961.34] Before we started recording, we were having our kind of introductory conversation, and we were talking about some of the challenges that women face in the field and our mutual desire to remedy that.
[2962.00 → 2965.84] And I know that we were talking about the fact that there was the controversy.
[2965.84 → 2974.48] I know anyone who's been in the space for a while will remember that there was a conference that used to be called NIPS, and there were connotations that may not be appropriate to that.
[2974.74 → 2979.98] And it was rebranded as Neurons, if I'm pronouncing that right.
[2980.18 → 2984.62] And so that originated out of Caltech, did it not?
[2985.10 → 2985.34] Yeah.
[2985.60 → 2994.30] So the conference actually started at Caltech, and it's, you know, very much, you know, when you think about, let's talk about the name in a bit, right?
[2994.36 → 2997.92] But the purpose of that conference was neural information processing.
[2998.12 → 2998.44] Yes.
[2998.56 → 3002.50] So it's highly multidisciplinary, and this was back in 87.
[3002.50 → 3007.22] So, you know, so it's truly visionary to think about, let's bring neuroscience.
[3007.48 → 3007.70] Sure.
[3007.86 → 3008.06] Right?
[3008.20 → 3010.38] Information, that's like information theory.
[3010.70 → 3011.10] Absolutely.
[3011.74 → 3013.32] And processing, which is computation.
[3013.70 → 3013.86] Yeah.
[3013.92 → 3020.42] It is still one of the top conferences, if maybe even the top one, depending on, in the world, in the area.
[3020.66 → 3022.50] And so I totally get that.
[3022.50 → 3033.78] And actually, the origin to that conference goes back to a course that Richard Feynman, Carver Mead, and John Hopfield taught together in 81.
[3034.08 → 3035.02] I did not know that.
[3035.02 → 3035.40] Before I was born.
[3035.70 → 3035.82] Yeah.
[3036.20 → 3037.32] I'll send you a link.
[3037.42 → 3038.64] It's just so fascinating.
[3038.64 → 3044.56] I mean, can you think of these three luminaries coming together and saying, we need to bring all these fields together?
[3045.16 → 3057.08] And ultimately, that kind of, you know, resulted in a new option we have for PhDs called, and a new division, in fact, like that's called the computational neuroscience or CNS at Caltech.
[3057.08 → 3065.04] So we have, you know, we admit students today to that discipline, and it's highly multidisciplinary, right?
[3065.16 → 3071.12] And so all that led to the formation of this conference, back then called NIPS.
[3071.56 → 3071.90] Understood.
[3072.54 → 3075.86] And, but yeah, you know, back then was a small event.
[3076.12 → 3080.94] You know, people went, they liked to ski and also discuss topics, right?
[3080.94 → 3090.02] So at that point, I mean, I mean, the name had unfortunate connotations, but no one kind of, you know, wasn't explicitly there.
[3090.60 → 3100.98] And so as long as, you know, to me, like even the beginning years of when I started attending the conference in 2010, right, before deep learning took off and the field just expanded.
[3101.28 → 3106.22] I never, you know, thought, oh, funny name, but I didn't kind of do much about it.
[3106.28 → 3109.10] And I never got bothered or harassed by it.
[3109.10 → 3109.20] Sure.
[3109.20 → 3112.98] But once the field started growing, that's when it became very problematic.
[3113.00 → 3113.80] I was just thinking that.
[3114.26 → 3119.92] When it's small enough in a very small community, people may not be thinking that direction.
[3120.06 → 3130.16] But after it grows to what it had become, and you have those negative connotations, maybe just as the conference had matured, maybe it was time for some of the surrounding branding to mature as well.
[3130.20 → 3130.60] That's right.
[3130.72 → 3135.80] And, you know, now we have to have higher standards because all eyes are upon us, right?
[3136.00 → 3136.24] Absolutely.
[3136.24 → 3140.52] And now it's in the public, and they're asking, oh, what is this name?
[3140.80 → 3146.88] And worse than that, you'd have like these few bad actors use the name to gain notoriety.
[3146.88 → 3149.84] And because any news is news, right?
[3149.94 → 3154.86] Any publicity is good because everybody's competing for talent, competing for attention.
[3155.52 → 3165.60] And so you'd have like these T-shirts like with things like, oh, you know, my nips are NP hard and all these like kind of, you know, like.
[3165.60 → 3172.70] And then, I mean, honestly, like I've been in these house parties that we'd have back then when the conference was small.
[3173.12 → 3173.32] Right.
[3173.40 → 3178.12] You'd think, you know, they were wild, but I felt so safe and so included in them.
[3178.12 → 3184.04] And suddenly these corporate parties are where I experienced really toxic environment, right?
[3184.22 → 3197.42] Like that, you know, there was this infamous party where, you know, barely clothed women were brought in just for the purpose of like, you know, like entertainment to an almost exclusively group of men.
[3197.42 → 3203.86] Yeah. So, you know, just as an aside, when I hear things like that, it's something that I just find revolting.
[3204.24 → 3221.06] Having grown up in a family of strong technical women, it wasn't until I was an adult that I realized that there were challenges for women to face because I had such amazing women in our family that were every, you know, they were, it never occurred that there could be inequality.
[3221.06 → 3228.98] So, when I hear about bad behaviours like that, perpetuating those kinds of stereotypes and other things, I find it disgusting.
[3229.26 → 3232.18] I know, though Daniel's not with me today, I know he does as well.
[3232.62 → 3242.94] And so, I am glad for people like you stepping up and doing what you can to correct the behaviour that needs it.
[3243.02 → 3250.26] Because I really worry as the field is growing, you know, that's when this kind of things can have a big effect.
[3250.26 → 3256.86] I mean, if you look into the history of programming, and there was a great New York Times article where in the beginning, it was all the women who were programming.
[3257.32 → 3260.70] I actually was sharing that on LinkedIn when it came out last week, I believe.
[3260.82 → 3268.54] And they were literally driven out, right, by the forces, by like how, you know, like, and I see the same happening today.
[3269.00 → 3271.10] And to me, that's a big concern, right?
[3271.26 → 3279.34] So, call to action to everyone listening to this is we all together need to put things right in this way.
[3279.34 → 3288.24] We need to have a global AI community that is welcoming to all and is fair to all and doesn't accept such bad behaviours.
[3288.62 → 3289.08] That's right.
[3289.24 → 3293.22] I mean, democratization of AI will come in so many different ways.
[3293.94 → 3295.24] And that's the thing.
[3295.36 → 3297.62] I mean, honestly, the name didn't bother me before.
[3298.66 → 3302.92] But, you know, once these elements started appearing, it was a big issue.
[3302.92 → 3308.16] And then for the younger women, it was even a bigger issue than me, than it was for me, right?
[3308.32 → 3311.82] So, and that's why I decided to speak out and so many others did.
[3312.10 → 3316.02] And it was just this huge collective community action.
[3316.46 → 3320.36] And I think it really helped us grow as a community better because it brought us together.
[3320.52 → 3321.48] It raised awareness.
[3321.98 → 3327.48] I mean, so many men said, oh, I had no idea it was this bad that you guys were having so many issues.
[3327.48 → 3338.76] On behalf of the community, all the listeners that will be thinking the same thought, thank you very much for being proactive and taking care of a problem that was developing in that area.
[3339.04 → 3341.64] And let's not let such things happen in the future.
[3341.76 → 3341.90] Yeah.
[3342.04 → 3343.90] And this is, to me, just the beginning.
[3343.90 → 3354.26] And there are so many efforts like AI for all that brings in underrepresented high school students or fast.ai democratizing, you know, AI to everybody, right?
[3354.42 → 3367.52] So, and there's like the, you know, human perspective of AI that was launched at Stanford just a few days ago that specifically, you know, saying ethics should be at the forefront.
[3367.52 → 3379.68] I think these are all things that we as researchers, we as, you know, people having a stake in AI in whichever different role, right, should really think about.
[3380.00 → 3383.10] So, I guess I'm going to turn us a little bit.
[3383.34 → 3391.58] And as we start to wind up, I'd like to get, you've talked a little bit about your first talk and role of tensor in machine learning, tensors in machine learning.
[3391.58 → 3401.22] But you also had a fascinating talk, and I know Daniel is going to be incredibly jealous that I was the one because Daniel came into AI from physics, and I did not.
[3401.52 → 3406.46] But your talk is infusing physics into deep learning algorithms for stable landing of drones.
[3407.00 → 3414.68] And I was wondering if you'd share a few minutes of what that was about and maybe also talk a little bit about how you came to NVIDIA as well.
[3414.80 → 3415.42] Yeah, absolutely.
[3416.00 → 3420.90] And, you know, and GTC is a place that, you know, really brings all this together.
[3420.90 → 3421.48] It sure does.
[3421.58 → 3428.16] This is a wonderful place to meet people and to have fun and to just really enjoy this field.
[3428.86 → 3429.02] Yeah.
[3429.16 → 3435.04] So, this project was done at Caltech, you know, before I joined NVIDIA, right?
[3435.14 → 3444.36] So, here, the, you know, it's very much of the Caltech nature because we are saying these are, if you look at the author list, it's from many different areas.
[3444.36 → 3449.24] So, there's people like me in machine learning, people in controls, in aerospace.
[3450.04 → 3454.32] So, you know, how we collectively asked to solve a question, right?
[3454.36 → 3461.72] It wasn't like, oh, I'm going to use my one tool or this is what should work or, but really trying to solve the problem here.
[3461.72 → 3472.88] And so, talking to the domain experts, so, Sun Jo Chang is the main professor from aerospace who is an expert, you know, in drones and all the drone flights, right?
[3472.94 → 3478.50] The main challenge even today, if you look at the commercial drones is they take a long time to land.
[3478.86 → 3482.58] And that's because the aerodynamics efforts are very hard to model.
[3482.58 → 3485.18] So, they're being extremely conservative in the landing.
[3485.76 → 3489.34] And so, the question was, can machine learning help us do this, right?
[3489.50 → 3497.24] On the other hand, like most like, you know, by machine learning, like deep reinforcement learning is about learning from scratch, right?
[3497.28 → 3506.32] You're doing it on games and, you know, there is a certain interesting aspect to it, but for most practical applications, you wouldn't do it from scratch, right?
[3506.32 → 3514.56] And the question is, what is that right blend between existing knowledge, existing physics, and what should you learn from data, right?
[3514.56 → 3525.10] And I think this is broadly a question for us to figure out, like, you know, how do, how much of, in most fields, you have some existing knowledge, existing models, but they're not perfect, right?
[3525.14 → 3527.36] You also have data, but that's also not a lot.
[3527.54 → 3528.92] How do you bring the two together?
[3529.36 → 3534.70] It's not going to be purely deep learning-based approach, at least not the standard way it's done, right?
[3534.70 → 3544.62] And in this work, we said, okay, let's now learn this unknown ground effect through deep learning, but we'll keep the existing controller and try to cancel this as a residual.
[3545.86 → 3548.88] And so, but at the same time, we want to guarantee stability.
[3548.88 → 3551.20] So, it's not going to be a standard neural network.
[3551.38 → 3554.64] And we did try that in the beginning because we start with simple things.
[3554.80 → 3555.00] Sure.
[3555.02 → 3556.64] And it just crashed the drone, right?
[3557.46 → 3563.40] You started with a simple thing, true to your engineering, didn't work, and you did then the logical thing about...
[3563.40 → 3566.64] Yeah, and it also shows, like, we shouldn't apply deep learning blindly.
[3566.98 → 3567.20] Yes.
[3567.52 → 3579.50] So, and then once we, like, stabilize the network, and we also have guarantee theoretically that this will not crash, meaning it's, you know, has layup and off stability from control theory perspective, right?
[3579.54 → 3580.90] That's the technical term.
[3581.60 → 3583.58] Then that also worked beautifully.
[3583.58 → 3592.06] So, I have videos of it where you see a very quick speed up and still a very fast but smooth landing with deep learning.
[3592.66 → 3595.48] And to me, this is just even the first step, right?
[3595.62 → 3601.30] Ultimately, what we want to ask is these autonomous drone flights that you can certify they are safe.
[3601.42 → 3606.00] And that's still today, given the recent incidents, we have so much to uncover there.
[3606.00 → 3609.32] And I think machine learning broadly can help us a lot.
[3609.46 → 3616.34] And that also speaks to many of the projects now I'm doing at NVIDIA, which looks at using, you know, simulations.
[3616.82 → 3624.64] Like, NVIDIA has just such strong simulation tools like Quiz, Flex, and all the graphics rendering and all that expertise, right?
[3624.72 → 3630.36] The first part of the keynote, if you saw, and how that blends in with the second part on machine learning and AI.
[3630.52 → 3630.88] Yes, absolutely.
[3630.88 → 3640.22] How do we bring this two knowledge together and those frameworks together for robotics, for, you know, drones, for autonomous driving?
[3640.36 → 3642.86] These are all questions that very much connect the two.
[3642.94 → 3650.20] And just as an aside for the audience, she's talking about the keynote yesterday, which was Monday afternoon.
[3651.00 → 3658.60] Jensen Huang, who is the CEO of NVIDIA, gave his keynote for this conference and was covering the topics that she was just talking about.
[3658.60 → 3662.68] And as always, it was a very impressive talk.
[3663.00 → 3665.08] It was one of those things that you don't want to miss.
[3665.96 → 3668.02] It's a marathon, but it has so many.
[3668.10 → 3671.06] Each part, you have to keep attention because it's so informative.
[3671.10 → 3675.76] Two-hour and 45-minute keynote, and yet it will actually keep you riveted all the way through.
[3676.16 → 3679.66] Yeah, so, and that's kind of my broad philosophy today.
[3679.96 → 3682.84] When it comes to deep learning, right, what is the next things?
[3682.84 → 3689.64] I mean, right now we've shown with, you know, a lot of data, label data and computation, thanks to NVIDIA GPO's.
[3689.74 → 3690.14] There you go.
[3690.52 → 3695.04] We are able to get good accuracies on deep learning in some tasks, right?
[3695.08 → 3699.84] But there are so many others where there's not going to be enough label data, but maybe you have unlabelled data.
[3699.84 → 3708.36] And then you also have no prior knowledge about what structures you should impose and how it should behave, what constraints it should have.
[3708.68 → 3714.32] And that's what I think is the future in order to make it truly applicable in a diverse set of applications.
[3715.18 → 3716.10] Well, that is fascinating.
[3716.26 → 3718.36] So, just out of curiosity, when did you join NVIDIA?
[3718.54 → 3721.12] At what point in the process did you go into the organization?
[3721.44 → 3723.30] Yeah, so, it was roughly at the end of September.
[3723.66 → 3724.82] Oh, so it's fairly recently.
[3724.82 → 3725.22] Okay.
[3725.78 → 3734.84] So, it's funny, as you have taken us through your story, that seems like such a natural place for you to end up, given the work that you've been doing.
[3735.20 → 3735.92] That's right.
[3736.24 → 3738.84] And to me, like, it's at all the levels, right?
[3738.98 → 3745.16] Like, if you, like, go back to tensors, like, the basic primitives of these tensor operations, how do we speed them up?
[3745.26 → 3748.44] They'll come at the level of, like, CUBA or even below that.
[3748.72 → 3751.70] And today, most of them we've sped up for matrix operations.
[3751.70 → 3757.28] So, we need to rethink on, you know, what would be a new way to have primitives.
[3757.40 → 3761.76] And there's going to be a talk tomorrow, like, with the title, CU tensor or CU tensor.
[3762.10 → 3762.34] Okay.
[3762.50 → 3766.00] That's going to be a new library for those tensor primitives, right?
[3766.06 → 3768.38] And now, there's all through the layers of the stack.
[3768.46 → 3775.02] How do you, like, truly take advantage of these new operations and parallelize them even more effectively?
[3775.16 → 3776.54] Like, you can get better speed ups.
[3776.64 → 3776.84] Sure.
[3776.84 → 3782.70] Right, and build better neural networks, build better probabilistic models of all different kinds.
[3783.00 → 3786.26] And we can probably, I know that NVIDIA publishes these.
[3786.36 → 3789.94] So, by the time this comes out, it may very well be out.
[3790.30 → 3792.14] And we can put that in the show notes as well.
[3792.68 → 3794.74] So, that right after you listen to this, you can go look at that.
[3794.76 → 3798.58] I'm in the library tomorrow after the talk will be available for the public.
[3798.58 → 3798.98] Fantastic.
[3799.44 → 3799.70] Okay.
[3800.22 → 3805.56] Well, I guess as this has been just an absolutely fascinating conversation.
[3806.20 → 3809.28] Listeners may know that we went a little longer than we usually do.
[3809.42 → 3813.06] But I think everybody will agree this was well worth it.
[3814.06 → 3817.72] It was just truly an inspiring story that you had to share.
[3818.44 → 3821.06] And I hope that you will come back again sometime.
[3821.06 → 3829.92] If people want to reach out to you and talk to you about this kind of work, is there a preferred way that you have of people reaching out?
[3829.92 → 3830.10] Sure.
[3830.32 → 3835.08] You know, I'm on different social media as well as my Caltech email is public.
[3835.58 → 3838.82] So, you know, my Twitter handle is Anima Anand Kumar.
[3839.30 → 3841.54] That's a lot, but that's my first and last name.
[3842.02 → 3845.06] And my Caltech email is anima at caltech.edu.
[3845.44 → 3847.66] And we'll have all of those in the show notes as well.
[3847.66 → 3851.16] So, Anima, thank you so much for coming on the show.
[3851.78 → 3854.98] It's been a truly fascinating conversation, as I'm sure everybody will agree.
[3855.52 → 3857.74] And keep up the amazing work that you're doing.
[3857.84 → 3859.04] Looking forward to seeing what you do next.
[3859.38 → 3860.18] Thanks a lot, Chris.
[3860.26 → 3861.84] And thanks for coming to GTC.
[3862.10 → 3863.10] Truly great to see you.
[3863.14 → 3863.94] Thanks for having me.
[3865.88 → 3866.38] All right.
[3866.44 → 3869.04] Thank you for tuning into this episode of Practical AI.
[3869.30 → 3870.76] If you enjoyed the show, do us a favour.
[3870.88 → 3872.26] Go on iTunes, give us a rating.
[3872.54 → 3874.40] Go in your podcast app and favourite it.
[3874.46 → 3877.24] If you are on Twitter or social network, share a link with a friend.
[3877.24 → 3879.66] And whatever you got to do, share the show with a friend if you enjoyed it.
[3879.96 → 3882.62] And bandwidth for Changelog is provided by Vastly.
[3882.74 → 3884.18] Learn more at Fastly.com.
[3884.38 → 3887.58] And we catch our errors before our users do here at Changelog because of Rollbar.
[3887.78 → 3890.18] Check them out at rollbar.com slash Changelog.
[3890.52 → 3893.00] And we're hosted on Linde Cloud Servers.
[3893.36 → 3894.96] Head to linode.com slash Changelog.
[3895.06 → 3895.52] Check them out.
[3895.58 → 3896.42] Support this show.
[3896.82 → 3899.98] This episode is hosted by Daniel Whiten ack and Chris Benson.
[3900.44 → 3902.52] The music is by Break master Cylinder.
[3902.90 → 3906.34] And you can find more shows just like this at changelog.com.
[3906.34 → 3908.48] When you go there, pop in your email address.
[3908.78 → 3913.16] Get our weekly email keeping you up to date with the news and podcasts for developers in
[3913.16 → 3914.78] your inbox every single week.
[3915.20 → 3915.96] Thanks for tuning in.
[3916.10 → 3916.88] We'll see you next week.
[3916.88 → 3919.68] Bye.
[3931.68 → 3932.58] Bye.
[3932.58 → 3932.74] Bye.
[3932.74 → 3933.36] Bye.
[3933.48 → 3933.50] Bye.
[3933.52 → 3933.90] Bye.
[3933.90 → 3933.96] Bye.
[3934.02 → 3934.76] Bye.
[3934.84 → 3935.40] Bye.
[3936.00 → 3936.46] Bye.
[3944.64 → 3945.02] Bye.
[3945.08 → 3945.28] Bye.
[3945.30 → 3945.38] Bye.
[3945.38 → 3945.84] Bye.
[3945.84 → 3946.32] Bye.
