[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.02] And unlike standard droplets, which use shared virtual CPU threads,
[29.02 → 32.86] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.40 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[107.42 → 109.72] Welcome to Practical AI.
[110.12 → 115.06] This is Daniel Whiten ack, and I'm joined by my co-host, Chris Benson,
[115.42 → 118.40] who is an AI strategist at Lockheed Martin.
[118.84 → 119.68] How are you doing, Chris?
[119.84 → 120.46] Doing great.
[120.52 → 121.40] How's it going today, Daniel?
[121.78 → 123.04] Oh, it's going pretty good.
[123.04 → 131.70] I'm packing up and getting ready to do a very non-AI data science thing, which is going backpacking for a bit.
[131.90 → 132.36] So I'm going to...
[132.36 → 133.18] Oh, that sounds great.
[133.20 → 139.74] I'm going to be out of touch next week and hopefully away from any sort of cell phone signal and that sort of thing.
[139.82 → 141.48] So actually, I'm pretty excited.
[141.80 → 142.02] Fantastic.
[142.02 → 143.16] What area are you going to be in?
[143.34 → 150.54] I'm going up to Minnesota to the Superior Hiking Trail, which goes along Lake Superior.
[150.88 → 152.60] So it should be a good time.
[152.68 → 154.06] It'll be a new one for me.
[154.16 → 164.56] And I have no doubt that, you know, being in isolation a little bit will give my mind some time to think about all of those AI problems that I am trying to solve as well.
[164.68 → 166.12] So looking forward to that.
[166.30 → 166.76] Sounds good.
[166.76 → 181.44] Yeah, well, today we're very privileged to be joined by David Jakubowicz, who is a principal data scientist at Galvanize and also a fellow podcast host.
[182.02 → 184.50] He's the host of the Humane podcast.
[185.04 → 188.20] So humane, like with the AI emphasized.
[188.84 → 191.02] And we're really happy to have you here, David.
[191.28 → 192.08] Thanks so much, guys.
[192.14 → 192.58] It's a pleasure.
[192.58 → 192.98] Yeah.
[193.32 → 203.84] First off, why don't you kick things off by giving us a little bit of your background and how you got interested in AI data science things and ended up where you're at now?
[204.18 → 204.38] Sure.
[204.68 → 213.50] So ever since I was young, I loved math competition and I competed both in the state and national level in the U.S.
[213.50 → 225.58] and went to college actually for applied mathematics and physics and, you know, doing theoretical proofs and quickly realized the industry was changing from research to applied.
[225.84 → 235.30] So I started moving in the direction of code and applied research, which led me down the path of actuarial science back in 2010.
[235.84 → 236.16] Gotcha.
[236.42 → 236.62] Yeah.
[236.70 → 242.06] So this is kind of maybe just the start of a lot of the data science hype.
[242.06 → 242.70] That's right.
[242.78 → 242.92] Right.
[243.00 → 245.00] Big data wasn't even a word till 2012.
[245.74 → 249.20] You know, the AI revival was only kicking off around then.
[249.38 → 252.74] So I think in 2012, I first learned C Sharp.
[252.96 → 257.74] I was also playing with Fortran and COBOL because that's what the company I worked for had.
[257.86 → 259.68] So I was picking up some of those old languages.
[259.94 → 260.10] Right.
[260.28 → 262.26] But COBOL is never going away.
[262.38 → 262.86] I don't think.
[263.44 → 265.18] Fortran either, as far as I can tell.
[265.26 → 265.42] Yeah.
[265.46 → 266.86] Especially with financial services.
[266.86 → 270.02] So I've seen that reemerge over the years.
[270.44 → 279.56] And although that's a tangent, but I think that's interesting because as everyone's moving to cloud, you know, it's still how do we maintain these systems with these languages?
[279.56 → 284.48] But I love it because I'll go back into the background.
[284.56 → 292.18] But when I teach a lot today, I tell the students, hey, if you want to work in Jupiter, if you want to work in an IDE, guess what?
[292.24 → 293.98] It supports Fortran and COBOL.
[293.98 → 296.28] So you can always pick up those old languages.
[296.98 → 300.84] Yeah, it's something that would be definitely a fun exercise.
[301.10 → 312.56] And I've kind of done this a little bit with not those languages, but kind of trying to implement things side by side in different notebooks and see how they look and experiment that way is a fun thing to do.
[312.80 → 312.82] Yeah.
[313.00 → 315.34] Didn't you do bindings for Go, Daniel, if I recall?
[315.34 → 315.82] Yeah.
[316.08 → 326.46] So I worked originally on one of the first Go kernels for Jupiter, which is now maintained by other people who are doing great things with it.
[326.64 → 333.38] But yeah, there are a lot of fun times to be had with Jupiter and languages other than Python, I would say.
[333.76 → 334.52] That's super cool.
[334.62 → 337.24] And it's amazing how the bindings have evolved the technology.
[337.24 → 342.92] And, you know, when I was getting involved in X-Rail science, not much of that existed.
[343.14 → 346.78] Even APIs were just emerging in a certain aspect.
[347.70 → 355.56] So, you know, back in 2010, it was around the water cooler, literally at the office, in person, before remote work was even happening.
[356.02 → 358.58] Teams were saying, hey, we're thinking about getting on the cloud.
[358.84 → 360.40] Hey, we're thinking about getting these servers.
[360.94 → 363.30] And people were talking about Python and this language.
[363.30 → 370.44] And yeah, Python's been around since the 1990s, but it was just getting into the financial services back then.
[370.52 → 373.62] So I said, I'm going to pick it up and started learning it.
[374.18 → 383.70] And before you know it, the last eight years have been involved with different financial services companies, implementing data solutions with Python,
[383.70 → 395.36] and helping them build everything from analytics and dashboards to predictive models and setting up data strategy, as well as building out centres of excellence.
[396.12 → 406.24] And, you know, that led me to not only learn how to teach and how to code, but then how to help others take over processes.
[406.24 → 414.00] I think having worked with a lot of companies over the years, one of the biggest flaws we always see is not enough things are documented.
[414.62 → 419.06] And it's really challenging for those not coming from tech to pick up tech skills.
[419.52 → 425.20] So I've always been that go-to person around the water cooler to teach you how to use Excel and SQL and Python.
[425.94 → 431.96] And it just became a natural fit in the past few years when I got into learning and development, pedagogy and training.
[431.96 → 436.38] So that is a perfect segue into a first question I have for you.
[436.48 → 440.12] And that is, tell us about Galvanize and, you know, what do you do?
[440.32 → 443.00] And, you know, how does that, how did that come into your life here?
[443.30 → 445.44] Sure. So Galvanize was founded in 2012.
[445.54 → 450.32] We're one of the bootcamp providers for software engineering and data science in the United States.
[450.92 → 455.02] We have three segments of the business, a consumer, a remote, and an enterprise.
[455.02 → 463.16] I'm on the enterprise corporate arm, and that plays a lot to my previous skill set of helping other individuals learn tech in corporate.
[463.66 → 468.28] Prior to being at Galvanize, I was at General Assembly doing the same thing on our enterprise side,
[468.58 → 476.82] working with financial clients, scaling hundreds of individuals in organizations to deskill and upskill in the Python programming language,
[477.26 → 482.56] in Jupyter, in working with return on investment projects for their divisions.
[482.56 → 486.84] And, you know, at Galvanize, we have all those divisions as well.
[487.26 → 491.74] We're both consumer and enterprise facing, and we're all over the U.S.
[491.96 → 496.98] And I think what's most exciting is there's been so much growth happening in 2019,
[496.98 → 499.68] and we're seeing that even into the next three years,
[499.88 → 503.84] predominantly because everyone is wanting to deskill and upskill,
[504.14 → 507.74] and code is now the first thing that people are picking up.
[507.74 → 511.76] Yeah, and as you kind of got into that training side of things,
[511.84 → 521.12] I mean, it sounds like you got into sort of data science training pretty early in terms of when these programs were coming out and that sort of thing.
[521.26 → 528.22] What really motivated you to see that need for better data science training,
[528.22 → 534.72] or was it kind of personal thing on your side where you really kind of developed some passion for teaching
[534.72 → 538.06] or found out you were good at it, or what led you down that path?
[538.30 → 542.22] So for me, it's very mission-driven, even since middle school and the math competitions,
[542.22 → 546.50] because we would have math competitions where you not only compete individually,
[546.50 → 548.88] but you had team assessments.
[548.88 → 555.88] And that's where you would have to solve four questions between 30 and 60 seconds and come up with a group answer.
[556.38 → 562.04] It's incredible how fast-paced it was, both statewide, nationally, and internationally.
[562.54 → 568.32] And so if you had the weakest link on your team, you had to get them up to speed so that you can successfully perform.
[568.84 → 573.52] So I've always been interested in helping everyone rise to the occasion.
[574.00 → 578.62] But beyond that, I've noticed how technology has transformed so quickly.
[578.88 → 585.78] So my father actually was an entrepreneur and owned a business that worked at the schematic level
[585.78 → 592.08] to repair TVs, VCRs, DVDs, and all sort of electronic gadgets in South Florida.
[592.48 → 596.70] You know, all throughout the 80s and 90s, at one point, this company grew to over 20 people.
[597.10 → 598.12] They have three locations.
[598.40 → 600.42] They're doing millions of dollars of business a year.
[600.96 → 604.30] And then before you know it, the whole industry changed, right?
[604.30 → 606.44] All these new smart TVs appeared.
[607.04 → 608.74] You know, products disappeared.
[609.38 → 613.40] And it was so challenging to keep up with the times and technology.
[614.18 → 620.28] And before you know it, the whole servicing industry and warranty industry started to evaporate.
[620.68 → 625.92] And, you know, fortunately for our family, my dad was already in his 60s when that started.
[626.06 → 628.02] So he went into an early retirement.
[628.68 → 633.34] But then I started thinking, you know, hey, how could someone like my dad learn to code?
[633.60 → 634.62] And he really wanted to.
[634.62 → 641.42] So, and he had that capacity because he had that technical mind working with fixing electronics
[641.42 → 644.00] with capacitors and all these gadgets.
[644.68 → 650.18] And, you know, it was interesting because I, in essence, mentored my dad as he was picking
[650.18 → 653.76] up Python through some of these platforms and coaching him.
[653.76 → 659.14] And at the end of the day, what I realized is he didn't want to learn Python for data analysis,
[659.62 → 659.76] right?
[659.80 → 664.74] He knew at 63 years old that he wasn't going to become a data analyst at the Fortune 500
[664.74 → 665.26] company.
[665.56 → 671.30] But he knew if he could take the work that he did in RPA and robotics and apply Python
[671.30 → 672.92] there, it would make a lot more sense.
[672.92 → 675.24] So what did my dad naturally do?
[675.32 → 680.86] He bought Arduino boards and Raspberry Pi boards and connected sensors to refract light off the
[680.86 → 686.36] walls in the living room and sound waves when the dogs moved and sensed actually position
[686.36 → 692.92] locations for where movement was occurring because he was always sensing movement with audio and
[692.92 → 695.94] for visual on those TVs and the sound boards.
[695.94 → 702.14] So it was so interesting for me as a takeaway to realize to make code and to make languages
[702.14 → 707.28] stick, you have to make a relatable for the learners, and you have to provide them capstones
[707.28 → 709.38] that they can take back for their portfolio.
[709.76 → 712.72] And they're having a fun time learning as well.
[713.12 → 716.96] I got to say that sounds, your dad sounds super cool there, you know, getting into that.
[717.08 → 722.08] I certainly think there's a lesson to be learned there about, you know, always kind of looking
[722.08 → 726.26] for the new thing no matter what age you're at and staying engaged and diving in.
[726.38 → 732.86] To broaden it a little bit, as we look at data science training, both in industry and in academia,
[733.20 → 736.76] and kind of, you know, it's evolved so quickly over the last few years.
[737.08 → 738.52] Where is it lacking?
[738.80 → 741.44] What is industry doing well and not so well?
[741.52 → 742.16] Where could they improve?
[742.22 → 743.20] And the same for academia.
[743.42 → 748.14] And are we really doing a good job preparing data scientists for getting out there in the
[748.14 → 748.70] world at this point?
[748.70 → 754.34] So it's fascinating because at our organization, I do work a lot with the New York City government
[754.34 → 758.70] on their different programs with the small business administration and training programs.
[758.84 → 763.46] So I sit down with politicians and local leaders and talk about how are we serving constituents
[763.46 → 768.16] who are making $18,000 a year and get them up to $85,000 a year.
[768.54 → 774.08] And the truth is most programs are really rushing into industry without full preparation.
[774.32 → 777.20] So we haven't seen the best results all throughout.
[777.20 → 784.08] Many programs say, hey, you know, our average graduate makes $78,000, and they get a job,
[784.38 → 786.08] you know, within six months of graduation.
[786.20 → 787.68] But that's not always true.
[788.30 → 793.20] For us at Galvanize, we are on both course report and switch up, and we have everything
[793.20 → 796.86] that's peer-reviewed and checked through the industry to make sure that we're giving you
[796.86 → 800.20] the real facts on how our students do and perform.
[800.60 → 804.18] But, you know, even then for us, we're constantly having to innovate on the curriculum.
[804.18 → 808.86] You see now all the universities are launching data science programs and a lot of them are
[808.86 → 810.40] getting into AI programs as well.
[810.86 → 816.06] Whether you're looking at the first ones like Berkeley and Columbia or other ones popping
[816.06 → 817.12] up all around the country.
[817.50 → 822.92] I wouldn't say any of them have won the game per se because the technology is changing so
[822.92 → 823.30] fast.
[823.70 → 828.74] I think when someone's thinking about going into learning through a data science training
[828.74 → 833.24] program, whether it's a university or a boot camp, it depends on the goal you're looking
[833.24 → 833.94] to achieve.
[834.20 → 838.82] If you're going directly into an undergrad or a master's program, it makes sense to tack
[838.82 → 839.24] it is on.
[839.34 → 844.26] So you have that extra skill set that's going to help future-proof yourself in whatever
[844.26 → 846.32] role that you move into in your career.
[846.46 → 851.42] But if you're going straight into a boot camp without any other prior experience, it's often
[851.42 → 851.90] a struggle.
[851.90 → 856.40] Because as boot camps, if you're doing the full time, which is 60 to 100 hours a week
[856.40 → 860.84] for three months, and then you're expecting to get a job afterwards, there's a reality
[860.84 → 862.40] check I have to share with most students.
[862.66 → 864.78] I tell them that you need to have a basis there.
[865.06 → 868.84] The biggest students who have great success going through boot camps are those who are
[868.84 → 870.96] early software engineers or have a PhD.
[871.40 → 873.18] And that's a very limited pool, right?
[873.36 → 877.34] So if you're coming from a liberal arts movement, you can be successful in a boot camp.
[877.64 → 881.68] However, you're going to have to put in a lot of time and work to see those results.
[882.34 → 886.68] And the classic example I share with students is, if you're someone who already is a software
[886.68 → 891.98] engineer, and you only study two hours a week, and look to get that job, but you're someone
[891.98 → 896.20] who's a liberal art, but you spend 10 hours a week, you're going to ramp up a lot quicker
[896.20 → 898.36] than the software engineer, just not in the beginning.
[898.58 → 901.22] So it is all about time output and thinking smarter.
[901.58 → 903.30] Is there a program that's better or worse?
[903.30 → 904.52] There's so many out there.
[904.80 → 909.20] And I like to say that we have some of the best programs in the industry, but they're constantly
[909.20 → 909.60] evolving.
[909.60 → 914.18] And I think when you choose a program you want to be involved in, you want to make sure that
[914.18 → 920.18] that institution or that boot camp has full-time curriculum people who are constantly innovating
[920.18 → 920.88] and improving.
[921.50 → 924.50] And to be willing to ask them, yeah, what's the tech stack?
[924.60 → 925.34] What are we going to learn?
[925.74 → 926.98] You know, are we just learning Python?
[927.12 → 931.36] But what packages and what databases and, you know, what projects?
[931.54 → 936.14] And feel free to ask those big, tough questions because that's going to serve you best down the
[936.14 → 936.30] road.
[936.30 → 942.02] So, I mean, I hear a little bit of what you're saying in terms of like the helping people
[942.02 → 945.20] understand where they really want to get to, where they're coming from.
[945.32 → 953.76] Do you feel like as an industry, we've crystallized that all in terms of what like a data scientist
[953.76 → 954.46] is?
[954.46 → 961.26] It seems like for so long and maybe still to some in many ways, defining what data science
[961.26 → 967.48] is, is just like so varied that it almost loses meaning in some sense because
[967.48 → 973.90] it could be like, oh, you know, you're doing TensorFlow and deep learning all the way to
[973.90 → 980.30] sort of analytics things to like big data is kind of distributed processing things.
[980.30 → 985.26] Do you think that we've kind of crystallized around that terminal?
[985.42 → 993.32] I've noticed like recently a lot more effort in terms of kind of specialized job role titles
[993.32 → 999.92] like, you know, like machine learning engineer or, you know, even like things like data science
[999.92 → 1000.98] engineer or data.
[1001.44 → 1005.50] Of course, data engineer has been around for a while now, like AI engineer.
[1005.50 → 1010.00] It seems like a lot of people are kind of shifting to the side of like, oh, we need to
[1010.00 → 1015.02] add like engineer in the name because like these data science people coming through don't
[1015.02 → 1016.66] really know how to build anything.
[1016.84 → 1016.94] Right.
[1017.08 → 1018.04] So I don't know.
[1018.12 → 1022.62] What is your sense of that as you kind of survey people coming through these sorts of
[1022.62 → 1026.78] programs, the types of positions that they're looking for, the types of things industry are
[1026.78 → 1027.32] looking for?
[1027.44 → 1028.98] What is your perspective on that?
[1029.20 → 1029.42] Right.
[1029.42 → 1035.76] So if I look at the ML engineer, that's someone who has software experience in building applications
[1035.76 → 1042.06] and a data engineer is someone who could already work with cloud systems or distributed systems.
[1042.66 → 1047.20] And often the boot camps and the master's programs just don't give enough there.
[1047.40 → 1047.58] Right.
[1047.64 → 1049.80] And that's why you want to look at capstones for that.
[1050.02 → 1056.02] But I think the challenge is there's so much information to cover and pack into it.
[1056.02 → 1059.48] Data science has just become this term that encompasses the industry.
[1060.10 → 1065.94] And how I look at it is, you know, simply put, what used to be big data became predictive
[1065.94 → 1069.14] analytics, became data science, which is now the AI industry.
[1069.36 → 1070.46] It's constantly evolving.
[1071.02 → 1077.10] But the truth is, when you look at data science roles, 60 to 80 percent of the work is still
[1077.10 → 1077.68] in the data.
[1077.88 → 1078.82] It's cleaning data.
[1079.00 → 1079.92] It's labelling data.
[1080.04 → 1081.20] It's getting it all set up.
[1081.20 → 1087.62] I featured actually just at the beginning of August on the Humane podcast, Mark Sears,
[1087.74 → 1092.10] who runs Cloud Factory, which is one of the big data labelling companies between Europe and
[1092.10 → 1092.48] Africa.
[1093.10 → 1096.22] And, you know, they have 10,000 people just labelling data.
[1096.68 → 1101.30] And I think the reality that a lot of data scientists don't know until they join a company
[1101.30 → 1103.88] is you're not playing with algorithms all day.
[1104.14 → 1105.04] Maybe you might.
[1105.04 → 1110.78] But even an ML engineer, you're going to be working with APIs and setting up pipelines
[1110.78 → 1115.46] and systems before you get to start training and testing and working with other teams to
[1115.46 → 1116.16] see those results.
[1116.66 → 1120.18] So I definitely see a specialization occurring in the field.
[1120.44 → 1126.20] In fact, I'm calling now a new subfield emerging in data science, which we're starting to see
[1126.20 → 1128.54] in some trend reports called data science as a service.
[1128.54 → 1133.96] So similar to how we saw infrastructure as a service with things from like HashiCorp with,
[1134.06 → 1138.98] you know, Ansible and Terraform and a lot of deployment options for the cloud, we're
[1138.98 → 1139.86] going to start seeing that.
[1139.94 → 1141.90] And we already are in data science as a service.
[1141.90 → 1146.48] So we're seeing companies like Neptune and Spell and Weights and Bias and other ones, which
[1146.48 → 1151.00] have all just recently raised their series A's that are helping deploy systems.
[1151.22 → 1155.18] You even see the founders of Anaconda, a couple of them branched off and launched Saturn
[1155.18 → 1157.92] Cloud, which is, you know, launch these systems.
[1157.92 → 1160.62] And Docker containers and whoop, now do your data science.
[1161.12 → 1165.58] Paper Space also in Brooklyn got notorious for that and has been doing a phenomenal job
[1165.58 → 1170.72] partnering with companies like, you know, Fast AI and Insight Data Science Fellowship as
[1170.72 → 1170.92] well.
[1171.38 → 1175.82] You know, as a kind of as a follow-up to that, it kind of feels like our industry is starting
[1175.82 → 1176.64] to grow up.
[1177.10 → 1178.62] I'm older than the two of you guys.
[1178.74 → 1183.04] And I was around when the internet first kind of exploded and went mainstream.
[1183.04 → 1185.18] And, you know, in the early 90s.
[1185.24 → 1191.02] And it was you went from a very few job descriptions that were then kind of fragmented as it exploded
[1191.02 → 1194.32] outward and had, you know, many dozens of job descriptions very soon.
[1194.46 → 1199.72] It feels to me very much like the data science world and the AI world are kind of starting to
[1199.72 → 1205.32] do that now, where instead of every role being tied to a data scientist, you're seeing lots of
[1205.32 → 1210.76] specialization and the even the and therefore even data scientist is becoming a little bit
[1210.76 → 1214.26] specialized in terms of what activities it does in that ecosystem.
[1214.84 → 1215.94] You have any thoughts on that?
[1216.32 → 1217.26] That makes complete sense.
[1217.38 → 1221.38] You know, a lot of companies now in consulting are actually hiring staff data scientists.
[1221.38 → 1224.60] These are data scientists who are supporting many teams.
[1224.84 → 1229.56] But then some teams hire a data scientist to help with just that division.
[1229.56 → 1233.42] So I think you're going to see that where there are those who are both cross-functional
[1233.42 → 1235.76] and those focused only on a product.
[1236.82 → 1241.80] And actually, for those who are looking for data science and AI jobs now, next time you're
[1241.80 → 1246.02] checking out a company, and you're looking at their job boards, whether that's on their
[1246.02 → 1251.70] website or Indeed or LinkedIn, I encourage you to see in the job description, what are they
[1251.70 → 1252.82] talking about, right?
[1252.90 → 1253.66] Is it the product?
[1253.82 → 1254.58] Is it the team?
[1254.68 → 1255.56] Is it the whole company?
[1255.56 → 1260.54] And in fact, when you're looking at that for a role, it's important to look at the
[1260.54 → 1262.86] requirements and the recommendations.
[1263.54 → 1269.14] So often, you know, people choose to apply or not apply for jobs based on if they check
[1269.14 → 1270.98] every single box on there.
[1271.28 → 1277.04] But having interviewed and worked with on hiring teams to bring in a lot of data scientists
[1277.04 → 1282.20] at Galvanize and other companies, it's not every box that has to be checked.
[1282.38 → 1283.12] You totally agree.
[1283.12 → 1286.88] Yeah, I mean, the requirements generally, most of those boxes should be checked.
[1287.00 → 1290.00] So you do want to make sure you're covering 75% or more.
[1290.50 → 1292.46] But think of the requirements as must-haves.
[1292.58 → 1295.18] You generally should have that, but not necessarily everything.
[1295.38 → 1298.26] And sometimes that tech stack is specific to a company.
[1298.68 → 1304.20] So if you're looking at 10 data scientist positions between startups and Fortune 500s,
[1304.54 → 1305.92] all requirements could be different.
[1306.26 → 1307.18] Someone uses Python.
[1307.40 → 1308.30] Someone uses R.
[1308.42 → 1309.42] Someone uses TensorFlow.
[1309.70 → 1310.88] Someone uses Monet.
[1310.88 → 1313.82] My goodness, should you learn them all just until you get a job?
[1314.08 → 1315.42] I don't think so, right?
[1315.50 → 1318.84] Go with what you got and then start applying that.
[1319.34 → 1322.80] And in the interview, you know, companies are very flexible with that, right?
[1322.86 → 1325.94] If you're like, oh, I'm amazing at R, but I'm just picking up Python.
[1326.38 → 1328.02] Sure, I'm going to do the code interview in R.
[1328.40 → 1329.40] Let's see what you can do.
[1329.48 → 1330.80] And if you do it great, you know what?
[1331.34 → 1331.70] Phenomenal.
[1331.94 → 1333.90] And there are so many integrations happening there.
[1333.90 → 1337.86] I also think this is such a tangent, but I think R is playing catch-up.
[1338.04 → 1342.64] You know, R fell in the rankings to only the ninth most desirable language this past year.
[1342.88 → 1344.70] They used to be top five for a few years.
[1345.26 → 1346.72] And now they're playing catch-up.
[1346.84 → 1348.74] There's some really cool new packages coming out.
[1348.88 → 1352.60] So I wouldn't be surprised if R climbs back up the leaderboard in the next couple of years.
[1352.60 → 1366.72] Hey, guess what?
[1366.84 → 1369.14] Brain Science is officially launched.
[1369.44 → 1371.12] Episode number one is on the feed right now.
[1371.28 → 1374.90] So head to changelaw.com slash brain science to listen, to subscribe,
[1374.90 → 1378.46] and to join us on this journey of exploring the human mind.
[1378.46 → 1384.26] Once again, changelaw.com slash brain science or search for brain science in your favourite podcast app.
[1384.26 → 1410.66] So David, we already mentioned that you have your own AI podcast called the Humane Podcast.
[1410.66 → 1415.22] It's great to have another podcaster on the show with us.
[1415.34 → 1419.70] It's the first time we've done this, and we're really excited to kind of help bridge the gap
[1419.70 → 1422.24] between some of these different people creating content.
[1422.24 → 1425.76] So it's really great to have that opportunity.
[1426.32 → 1430.82] I was wondering if you could just share kind of the premise behind the Humane Podcast
[1430.82 → 1433.96] and why you decided to start creating it.
[1434.28 → 1435.02] Sure. Thanks, guys.
[1435.02 → 1442.58] You know, I think technology is moving at such a blistering pace in what we're now coining the fourth industrial revolution.
[1443.40 → 1448.98] And as you mentioned, the gap is continuing to grow, especially between humans and machines.
[1449.48 → 1451.72] And all these new products are coming out.
[1451.94 → 1455.46] All these new companies are coming out, which are supposed to improve our lives,
[1455.62 → 1457.90] but a lot of our jobs are at risk.
[1458.22 → 1462.32] So I created the Humane Podcast to bridge the gap between humans and machines
[1462.32 → 1464.22] in the fourth industrial revolution.
[1464.76 → 1469.76] I feature in an interview format conversations with chief data scientists,
[1470.10 → 1473.02] AI advisors, and leaders who advance AI for all
[1473.02 → 1478.60] to help everyone learn more about humans and their processes in AI,
[1478.74 → 1480.10] which is called human-centred AI,
[1480.64 → 1484.00] empathetic design, which is how we can build better processes for humans,
[1484.44 → 1488.56] and other topics like AI for social good, AI governance, and AI research.
[1488.56 → 1495.82] I think for me, coming up with the Humane Podcast was so natural with all the training and deliveries I've been doing,
[1496.08 → 1502.14] as well as seeing my dad and his own journey from going in robotics to code
[1502.14 → 1503.72] and then saying,
[1503.84 → 1506.86] all right, David, you're the one who's going to be the next generation.
[1507.50 → 1510.32] And so I wanted to make sure these conversations could be heard
[1510.32 → 1512.18] and for a broader audience,
[1512.18 → 1516.56] because so many people, whether they're working today or they'll be working tomorrow,
[1516.56 → 1521.00] are concerned about these trends and how their jobs will be impacted.
[1521.40 → 1522.88] So that's a little bit about Humane.
[1523.72 → 1527.00] Another thing about Humane, just a fun fact, not many people know,
[1527.34 → 1530.24] Humane in its spelling in French actually means to be human.
[1530.52 → 1533.18] So it's a little play in words, throw the AI in there,
[1533.54 → 1536.74] but it's a great podcast I've had a lot of fun with,
[1537.00 → 1539.00] been going on for about 10 months,
[1539.48 → 1542.28], and thanks so much for letting me talk a little bit about that.
[1542.28 → 1547.22] Sure. I love the focus on how you're addressing some of the hard questions.
[1547.38 → 1550.34] I know that Daniel and I are always out there doing talks
[1550.34 → 1552.20] and meeting people in different events and stuff,
[1552.26 → 1555.96] and those same questions come up all the time in conversations.
[1556.34 → 1558.84] And so I think it's really great to just address them head on
[1558.84 → 1560.24] and sort through the problems.
[1560.56 → 1561.64] I'm really kind of curious,
[1562.16 → 1564.52] could you kind of share with us over the last 10 months
[1564.52 → 1567.94] maybe some of the highlights of the various episodes
[1567.94 → 1569.12] or interviews that you've done?
[1569.12 → 1573.10] And I'm really curious, what are some of the peaks of content
[1573.10 → 1574.00] that you've had over that time?
[1574.34 → 1575.62] Yeah, so it's fascinating
[1575.62 → 1578.64] because I always take a different theme to the podcast,
[1578.94 → 1583.42] and so I reach out to people who I'd love to invite to my dinner table
[1583.42 → 1584.98] and talk about the industry.
[1585.98 → 1588.62] One who I had on was about synthetic data.
[1588.62 → 1593.36] I had Jeremy Kaufman from Scale Venture Partners in Foster City,
[1593.60 → 1596.70] and we talked about how startups like Keep Truckin' and Convoy
[1596.70 → 1600.14] have scaled into billion-dollar ventures by using synthetic data.
[1600.40 → 1602.92] I had the opportunity to talk with Christian Karen,
[1603.14 → 1608.02] who is a female founder who works in data science training as well
[1608.02 → 1609.78] and is based in Boston,
[1609.78 → 1613.98] and we talked about how the industry has changed from research to applied.
[1614.42 → 1617.22] I've also spoken with one of my good friends, Noel Brochette,
[1617.58 → 1622.02] who used to be an early employee at the Alexa team in Voice,
[1622.02 → 1626.40] and now just got named the number one voice advocate of 2019,
[1626.40 → 1630.76] and we recently sat on a panel at the Voice Conference in Newark
[1630.76 → 1634.98] talking about how Microsoft and Amazon are working together
[1634.98 → 1637.58] to create a universal audio bot.
[1638.08 → 1641.62] So what I really love to do is that's just three examples of conversations
[1641.62 → 1643.70] that we've had on the podcast,
[1643.94 → 1648.10] but it's to talk about different themes, talk about trends,
[1648.10 → 1651.80] and speak about how it's relatable to each one.
[1652.02 → 1655.18] So whether someone is a data scientist today,
[1655.60 → 1656.78] they're a business executive,
[1656.78 → 1660.00] or they're someone who just wants to get into the industry,
[1660.36 → 1663.24] it's a little bit of entertainment and education for all.
[1663.78 → 1665.94] So yeah, thanks for sharing those,
[1666.02 → 1671.54] and I actually can't wait to listen to some of those that you mentioned,
[1671.76 → 1676.00] but I want to try to kind of play devil's advocate a little bit here
[1676.00 → 1677.86] and kind of give you a chance to say,
[1678.40 → 1680.30] like if I'm out there, and I'm thinking,
[1680.54 → 1684.34] oh, well, the gap between humans and machines is widening,
[1684.82 → 1687.70] basically, why should I care?
[1687.88 → 1692.00] You know if Gmail is able to kind of complete my sentences
[1692.00 → 1693.66] and it's convenient for me,
[1694.12 → 1697.42] why should I care that I don't really understand that,
[1697.44 → 1700.84] or I don't understand my data that's being used for that,
[1700.92 → 1702.46] or how it's being used,
[1702.52 → 1704.90] or it's just a convenience for me?
[1704.90 → 1708.96] Why is the gap between humans and machines such a concern?
[1709.08 → 1709.78] Why should we care?
[1710.18 → 1713.70] I like to place it to something that's personal for each and every person.
[1714.04 → 1716.70] So one of our presidential candidates right now,
[1716.80 → 1718.74] Andrew Yang from the state of New York,
[1718.86 → 1722.34] is talking about being the humanity-first presidential candidate.
[1722.92 → 1725.58] And the reason he's taken that stance
[1725.58 → 1728.64] is because there are things that we see every day in our life
[1728.64 → 1729.54] that are being automated.
[1729.78 → 1732.36] For example, the self-checkout lines at the grocery store
[1732.36 → 1736.58] used to be run by staff and people who had jobs,
[1736.64 → 1740.44] whether they were improving their life or getting a steady paycheck.
[1741.00 → 1743.46] And we've now seen several presidential candidates
[1743.46 → 1747.00] just in the past few weeks actually talk about,
[1747.48 → 1749.82] do they support self-checkout lines or not?
[1749.82 → 1753.58] And it seems like this should not be something controversial,
[1753.58 → 1758.28] but the truth is there's at least a couple million people in the United States
[1758.28 → 1760.28] who work in grocery stores.
[1760.64 → 1762.40] And whether that's as assistant managers
[1762.40 → 1766.38] or helping with transactions or better customer experience,
[1766.60 → 1769.30] the truth is those are jobs that like that can go away.
[1769.78 → 1772.06] We look at places like gas stations, right?
[1772.10 → 1773.96] If we're in the Northeast in New Jersey,
[1773.96 → 1778.74] that's one of the few states that still has human service gas stations.
[1778.98 → 1780.98] But everywhere else, it's self-service.
[1781.18 → 1782.38] That's been around for many years.
[1782.46 → 1783.44] There's no AI there.
[1783.54 → 1785.78] But that shows how the jobs were eliminated.
[1786.20 → 1788.80] And I think we're going to continue to see that happening.
[1789.10 → 1792.70] What we're looking at today in customer service experiences,
[1793.06 → 1795.98] even with when you call into a company
[1795.98 → 1800.26] to have a check-in on what you're doing with your current flight
[1800.26 → 1805.06] or for paying a bill, it's been completely automated away.
[1805.32 → 1808.20] And the service has gotten even better in the last three years.
[1808.56 → 1810.12] And we don't see it often
[1810.12 → 1812.36] because we don't see these people day to day.
[1812.48 → 1814.22] They're not eating at our dinner table.
[1814.50 → 1816.84] We're not talking to them about their life.
[1816.96 → 1818.86] But the truth is those jobs are going away,
[1819.14 → 1821.08] which means it's not just impacting them,
[1821.30 → 1823.26] but it's also impacting you.
[1823.48 → 1826.06] And it soon could impact your career as well.
[1826.56 → 1829.04] And I don't like to play pessimist.
[1829.04 → 1830.82] I know we're playing devil's advocate here.
[1831.26 → 1835.60] But there is the opportunity where AI's intention, right?
[1835.66 → 1837.04] Like, what is the big goal on AI?
[1837.18 → 1840.36] Like, why should we even use AI and all this automation?
[1840.62 → 1843.20] It's for efficiency, efficient markets, right?
[1843.26 → 1846.80] And in big cities, they're notorious for being efficient systems.
[1847.26 → 1849.14] And if you can make something more efficient,
[1849.38 → 1850.60] you will make it more efficient
[1850.60 → 1853.30] because you can drive down costs or increase revenue.
[1853.64 → 1857.62] And the challenge is every industry is going to be impacted there.
[1857.62 → 1859.32] Earlier this year in April,
[1859.50 → 1862.44] Deloitte actually had their human capital management report
[1862.44 → 1865.46] and said, we're moving into a world of super jobs.
[1865.94 → 1867.88] Super jobs are jobs 3.0,
[1868.16 → 1870.42] which means the analyst at Goldman Sachs,
[1870.52 → 1872.36] who used to work on their Excel reports
[1872.36 → 1873.60] and create a PowerPoint
[1873.60 → 1876.10] and present to the investment banking manager
[1876.10 → 1878.64] and determine that this is the next investment
[1878.64 → 1880.72] that's going to help them make a lot of money,
[1881.08 → 1882.68] no longer is that same job.
[1882.96 → 1884.70] That was what they did in 2003.
[1884.70 → 1888.78] But today in 2019, they have NLP systems
[1888.78 → 1890.78] that help auto-generate reports,
[1891.06 → 1893.58] automatically create dashboards,
[1893.90 → 1897.02] and then the analysts are offering some oversight
[1897.02 → 1899.32] as well as some customization
[1899.32 → 1901.38] with the higher cognitive tasks.
[1902.04 → 1904.68] And then they'll also maybe help with that presentation.
[1905.20 → 1907.50] But that itself has eliminated the need
[1907.50 → 1909.34] for a lot of investment banking analysts.
[1909.80 → 1912.18] We used to have 200 traders or analysts
[1912.18 → 1913.52] on the floor at Goldman Sachs.
[1913.92 → 1916.82] Today in 2019, you can do that with five to 10 people.
[1917.28 → 1919.30] So there has been a constant evolution.
[1919.82 → 1921.10] It's going to keep happening.
[1921.76 → 1923.12] And I tell people,
[1923.28 → 1925.40] it's not that you need to care about it.
[1925.64 → 1927.68] It's just that if you don't care about it,
[1927.94 → 1929.94] well, then you're putting yourself at risk.
[1930.30 → 1931.18] And ultimately,
[1931.58 → 1933.98] when you are optimizing for anything in life,
[1934.26 → 1936.40] you should be minimizing your risk.
[1936.62 → 1938.34] Maybe not for investments, right?
[1938.34 → 1940.30] So there could be a little play in words there.
[1940.52 → 1941.20] But in general,
[1941.20 → 1943.06] you should be creating a better process
[1943.06 → 1945.58] if you come from that mental model
[1945.58 → 1947.26] for your moral hazard.
[1947.26 → 1950.26] Yeah, I just saw an article.
[1950.56 → 1951.38] I'm looking at the date.
[1951.56 → 1952.26] It was August 7th,
[1952.88 → 1955.82] where J.P. Morgan has now apparently
[1955.82 → 1958.26] is experimenting with an AI copywriter
[1958.90 → 1962.00] that apparently, at least in some cases,
[1962.14 → 1965.14] can write better ads than humans can.
[1965.14 → 1968.02] And so I think this is a similar trend
[1968.02 → 1969.78] to what you're talking about.
[1969.94 → 1972.84] And do you think that the main piece of this
[1972.84 → 1975.82] that really comes into play is automation?
[1976.24 → 1977.44] That's the main player there?
[1977.50 → 1980.16] Or is it also kind of logical gap
[1980.16 → 1983.10] where people are less sure
[1983.10 → 1985.90] about what their technology is doing
[1985.90 → 1987.98] or how it's operating for them
[1987.98 → 1990.22] to produce convenience and that sort of thing?
[1990.86 → 1993.48] Well, I think the three big industries
[1993.48 → 1997.28] that we're going to see rapid onset of automation
[1997.28 → 1999.44] in the next 10 years
[1999.44 → 2001.16] are data and AI,
[2001.64 → 2003.78] connected devices and Internet of Things,
[2004.22 → 2005.04] and robotics.
[2005.68 → 2007.20] And all three of those industries
[2007.20 → 2009.72] are rapidly advancing in automation.
[2010.28 → 2011.24] Particularly there,
[2011.36 → 2013.70] what's happening is the products we're using today
[2013.70 → 2016.82] are no longer being developed by humans.
[2017.14 → 2018.74] And the example that you just mentioned
[2018.74 → 2022.66] with J.P. Morgan with her copywriting AI.
[2023.46 → 2025.62] Sure, a little bit of it is public relations
[2025.62 → 2027.52] and talking about what's out here
[2027.52 → 2028.94] so they get first to market.
[2029.50 → 2031.74] But in fact, they're not first to market.
[2032.38 → 2034.44] Bloomberg and other financial companies
[2034.44 → 2036.66] have been creating articles
[2036.66 → 2039.74] with automated systems for years.
[2040.18 → 2042.62] If you're someone who invests in the stock market,
[2042.62 → 2044.80] next time you go onto any website
[2044.80 → 2048.78] like Seeking Alpha or Bloomberg or Reuters
[2048.78 → 2049.84] or any of these,
[2050.14 → 2052.78] and you look at the general news of the day
[2052.78 → 2054.28] and the article says,
[2054.92 → 2056.50] this stock has gone up 10%
[2056.50 → 2059.06] and the EPS is XYZ
[2059.06 → 2060.90] and the dollars are Y,
[2061.56 → 2063.60] that could all be written by a machine.
[2064.02 → 2065.82] And in fact, it probably already is.
[2066.20 → 2067.68] That's why earlier in 2019,
[2068.22 → 2071.08] there were over 100,000 media
[2071.08 → 2072.46] and copywriting jobs
[2072.46 → 2073.92] eliminated in New York City
[2073.92 → 2076.02] from companies like BuzzFeed,
[2076.34 → 2077.42] Vice, and others.
[2077.56 → 2079.64] Because all that is starting to be automated
[2079.64 → 2081.00] and teams are realizing,
[2081.48 → 2083.20] well, do we need 100 copywriters
[2083.20 → 2085.26] if instead we can have
[2085.26 → 2088.10] so many generated stories from a system
[2088.10 → 2090.24] and then we have a copywriter supervisor
[2090.24 → 2091.34] who checks through them
[2091.34 → 2092.84] and see which is most plausible
[2092.84 → 2095.40] and does some refinements there.
[2095.66 → 2098.10] The challenging thought is this.
[2098.46 → 2099.82] In a capitalist society
[2099.82 → 2101.16] like the United States,
[2101.76 → 2102.86] everything runs by money.
[2103.44 → 2104.96] And if money is not being made,
[2105.42 → 2107.20] automation is the first thought
[2107.20 → 2108.12] to come to mind.
[2108.62 → 2110.16] When we look at media companies
[2110.16 → 2111.48] like the New York Times
[2111.48 → 2112.68] and Washington Post
[2112.68 → 2114.38] who now run their businesses
[2114.38 → 2115.64] with digital subscriptions,
[2116.32 → 2117.72] they have more in 2019
[2117.72 → 2120.46] than they had print subscriptions in 2001.
[2121.02 → 2123.50] But when you look at other publications
[2123.50 → 2126.00] like the Los Angeles Times in California,
[2126.42 → 2128.16] the Sun Sentinel in South Florida,
[2128.16 → 2129.42] the Houston Chronicle,
[2129.68 → 2131.54] all of these are struggling.
[2131.78 → 2133.04] They don't have as many subscriptions
[2133.04 → 2135.00] so they don't have as much revenue.
[2135.54 → 2137.92] And the truth is revenue is driven
[2137.92 → 2140.24] by how much business you can bring in.
[2140.58 → 2142.18] And if the business is declining,
[2142.44 → 2144.08] the first thought that comes to mind
[2144.08 → 2146.30] is how automation can help solve it.
[2146.56 → 2148.10] So I really think that's why companies
[2148.10 → 2151.58] like J.P. Morgan are looking at AI copywriters.
[2151.88 → 2153.00] And Bloomberg and Reuters
[2153.00 → 2155.06] and Vice and BuzzFeed
[2155.06 → 2157.38] have already started getting in on those trends.
[2157.38 → 2160.74] I don't think ever all humans will be replaced.
[2160.96 → 2162.12] I think there's something to say
[2162.12 → 2165.56] with the sentiment of how we each think uniquely
[2165.56 → 2168.00] with our mental models and our perspective
[2168.00 → 2171.16] that a lot of people like to read and learn about.
[2171.32 → 2172.56] And I think that's one of the reasons
[2172.56 → 2174.58] why Substack recently raised,
[2174.72 → 2176.26] I think it was a $100 million round
[2176.26 → 2178.22] for human-based newsletters.
[2178.22 → 2181.16] So I'd like to tie a few of the threads
[2181.16 → 2183.10] that we've discussed together.
[2183.90 → 2185.92] We've been talking about kind of the relationship
[2185.92 → 2187.22] between human and machine.
[2187.86 → 2189.68] And you pointed out that you kind of have
[2189.68 → 2191.70] this kind of three points
[2191.70 → 2192.82] that are kind of coming together
[2192.82 → 2195.08] between kind of AI and data on one,
[2195.50 → 2197.06] connected devices on another,
[2197.26 → 2198.82] and robotics on a third.
[2198.82 → 2202.60] And you've talked about some use cases here.
[2202.80 → 2204.96] And it feels like we're almost dancing around
[2204.96 → 2206.96] a particular term
[2206.96 → 2209.14] that we're all talking about these days anyway,
[2209.60 → 2211.48] which is human-centred AI.
[2211.80 → 2214.64] And where it is augmenting humans,
[2214.82 → 2216.56] it's allowing for the collaboration
[2216.56 → 2218.24] between humans and machine.
[2218.60 → 2220.08] And in many cases,
[2220.18 → 2221.24] where kind of the human
[2221.24 → 2223.04] is sort of orchestrating
[2223.04 → 2225.00] a symphony of AI collaborators
[2225.00 → 2227.56] that might be working together
[2227.56 → 2230.14] to get something done for a company.
[2230.54 → 2232.32] And so I know you like to talk a lot
[2232.32 → 2233.52] about human-centred AI.
[2233.80 → 2235.28] And could you tell us a little bit more
[2235.28 → 2236.18] about what it is
[2236.18 → 2237.64] and why it's growing so fast
[2237.64 → 2238.78] and what you think the implications
[2238.78 → 2239.50] are going forward?
[2239.92 → 2240.08] Sure.
[2240.34 → 2242.74] So human-centred AI as a term
[2242.74 → 2244.86] just became big in the market
[2244.86 → 2245.94] in the last year.
[2246.58 → 2248.84] It became big because Stanford said,
[2248.98 → 2250.68] we're going to launch the High Institute,
[2250.90 → 2252.86] their own human-centred AI Institute
[2252.86 → 2253.98] with Fife Li,
[2253.98 → 2255.92] who's been a professor at Stanford
[2255.92 → 2256.82] for many years
[2256.82 → 2258.42] and ran Google Labs
[2258.42 → 2259.68] for a few years as well.
[2260.00 → 2261.04] And the intention
[2261.04 → 2263.36] is really thinking about the future
[2263.36 → 2264.62] because Stanford
[2264.62 → 2267.10] and even other major institutions
[2267.10 → 2268.56] like MIT with SAIL
[2268.56 → 2269.70] are thinking about
[2269.70 → 2271.00] what is going to happen
[2271.00 → 2273.82] when technology is everywhere.
[2274.44 → 2276.46] The elimination is already happening
[2276.46 → 2277.28] with jobs
[2277.28 → 2278.84] and it's not just in the US.
[2279.56 → 2280.98] I recently had a colleague
[2280.98 → 2283.10] travelling in Shenzhen, China
[2283.10 → 2285.70] and they stayed at the JW Marriott,
[2285.88 → 2288.38] a premium ultra luxury hotel,
[2288.72 → 2290.28] part of the Marriott Bonvoy brand.
[2290.72 → 2292.06] And when at the hotel,
[2292.40 → 2294.16] that individual wanted to get room service.
[2294.60 → 2296.66] And what did the JW Marriott do there?
[2297.04 → 2298.80] Now they have robotic butlers
[2298.80 → 2301.08] that drop off the latest Diet Coke
[2301.08 → 2301.72] that you'd like
[2301.72 → 2302.82] or your meal.
[2303.16 → 2305.12] They no longer have humans going from rooms.
[2305.12 → 2307.20] Those robotic butlers have computer vision.
[2307.20 → 2309.18] They can press the elevator button,
[2309.48 → 2310.00] go in,
[2310.44 → 2311.18] ring your doorbell,
[2311.62 → 2312.46] drop the food off,
[2312.68 → 2313.96] and they don't have to wait.
[2314.20 → 2316.80] So that provides greater access
[2316.80 → 2319.02] for on-demand service 24-7.
[2319.58 → 2320.78] So I mention that
[2320.78 → 2322.56] because that's why I think Stanford
[2322.56 → 2323.26] and MIT
[2323.26 → 2324.68] and other institutions
[2324.68 → 2325.64] have moved in
[2325.64 → 2327.56] on this human-centred AI movement
[2327.56 → 2328.22] where,
[2328.68 → 2328.86] look,
[2328.94 → 2329.94] we're moving to AI.
[2330.12 → 2330.86] We all get it.
[2330.92 → 2331.90] That is the future.
[2332.40 → 2332.96] And sure,
[2333.02 → 2333.68] there's some hype.
[2333.68 → 2335.38] It's going to be slower and faster
[2335.38 → 2336.42] in certain segments
[2336.42 → 2338.00] than we think or expect.
[2338.38 → 2339.82] But if we don't start
[2339.82 → 2341.32] placing diverse opinions
[2341.32 → 2343.36] into these processes early on,
[2343.66 → 2345.16] thinking about bias
[2345.16 → 2346.48] and how we can make sure
[2346.48 → 2348.02] the systems work for all people,
[2348.40 → 2350.22] then we're going to slip behind.
[2350.70 → 2352.04] So by thinking about that,
[2352.10 → 2352.60] you can say,
[2352.74 → 2354.02] when I design a process,
[2354.36 → 2355.24] does it work for someone
[2355.24 → 2356.54] who's 75 years old
[2356.54 → 2358.70] and someone who's 7 years old?
[2359.06 → 2360.14] Am I designing a process
[2360.14 → 2362.38] that can move in different terrains?
[2362.38 → 2364.54] Is the product going to be one
[2364.54 → 2366.52] that works across multiple languages?
[2367.06 → 2370.02] Anything that is non-accessible
[2370.02 → 2372.00] needs to be accessible with AI.
[2372.74 → 2374.30] And the reason is
[2374.30 → 2375.00] because otherwise
[2375.00 → 2377.14] you're excluding different cultures.
[2377.78 → 2378.18] Today,
[2378.60 → 2380.46] we serve all cultures
[2380.46 → 2382.40] primarily by hiring people
[2382.40 → 2383.48] who speak different languages.
[2383.98 → 2385.44] If you travel to Disney World
[2385.44 → 2386.16] or Disneyland,
[2386.78 → 2387.36] you get that.
[2387.46 → 2388.46] They have hundreds
[2388.46 → 2391.66] of fantastic park service individuals
[2391.66 → 2393.24] who speak different languages
[2393.24 → 2395.16] and support you as tour guides
[2395.16 → 2396.18] throughout your journey.
[2396.52 → 2397.38] But in the future,
[2397.46 → 2398.82] that could just be a sound piece
[2398.82 → 2400.00] with different languages.
[2400.56 → 2401.80] The challenge is
[2401.80 → 2402.88] we have to make sure
[2402.88 → 2404.26] we're being accessible for all
[2404.26 → 2406.10] and starting to design technology
[2406.10 → 2408.16] that's enabling humans
[2408.16 → 2409.06] at the onset.
[2409.86 → 2411.78] One example that's been a failure
[2411.78 → 2413.72] that has been quite prominent
[2413.72 → 2414.32] in the news
[2414.32 → 2416.28] is how Apple,
[2416.64 → 2417.20] with Siri,
[2417.50 → 2419.32] their audio-enabled assistant,
[2419.86 → 2423.12] never had an Icelandic language
[2423.12 → 2423.96] for Iceland.
[2424.60 → 2427.20] So when you were a kid,
[2427.44 → 2427.72] right,
[2428.10 → 2428.48] now,
[2428.60 → 2430.12] as an alpha generation
[2430.12 → 2432.00] or generation Z growing up,
[2432.44 → 2433.70] you were using Siri,
[2434.04 → 2435.32] the human language of English,
[2436.04 → 2437.12] to communicate with Siri.
[2437.54 → 2437.70] Right?
[2437.78 → 2438.70] So you're speaking in English
[2438.70 → 2439.84] but not Icelandic
[2439.84 → 2441.30] because Icelandic didn't exist
[2441.30 → 2442.24] for Siri.
[2442.24 → 2443.76] And what that meant is
[2443.76 → 2444.46] they've shown now
[2444.46 → 2445.60] that the Icelandic language
[2445.60 → 2447.74] is becoming extinct in Iceland
[2447.74 → 2450.16] because kids do not want to learn it
[2450.16 → 2451.88] and therefore parents
[2451.88 → 2452.82] are not going to teach it.
[2452.94 → 2453.74] And before you know it,
[2453.92 → 2456.76] we're having the diaspora of culture
[2456.76 → 2458.02] appearing again
[2458.02 → 2459.54] as a result of technology.
[2459.90 → 2460.10] You know,
[2460.12 → 2460.94] I like to think back
[2460.94 → 2463.04] to one of my favourite authors,
[2463.46 → 2464.08] Jared Diamond.
[2464.38 → 2464.56] You know,
[2464.58 → 2466.14] he's written Guns, Germs, Steel,
[2466.60 → 2467.24] Colossal.
[2467.98 → 2468.16] Yep,
[2468.34 → 2468.76] I've read it.
[2469.00 → 2469.16] Now,
[2469.24 → 2469.80] Upheaval.
[2469.80 → 2472.28] So all his fascinating books
[2472.28 → 2474.70] and how culture and society change.
[2475.34 → 2476.04] And, you know,
[2476.08 → 2478.30] I think we're now entering this new wave
[2478.30 → 2479.38] and whether we call it
[2479.38 → 2481.12] the third industrial revolution,
[2481.54 → 2483.06] the fourth industrial revolution,
[2483.52 → 2483.78] you know,
[2483.80 → 2485.36] whatever name you want to give it,
[2485.56 → 2488.38] I think the next 30 to 40 years
[2488.38 → 2490.46] is going to be a generation
[2490.46 → 2492.64] defined by connecting systems
[2492.64 → 2494.52] with internet everywhere,
[2494.88 → 2495.78] data everywhere,
[2496.46 → 2497.40] listening everywhere.
[2497.40 → 2499.48] And once that's complete,
[2499.74 → 2501.06] if we're not thinking about
[2501.06 → 2502.14] the human at the onset,
[2502.82 → 2504.06] a lot of jobs
[2504.06 → 2505.74] are no longer going to be here.
[2506.04 → 2507.16] And that might mean
[2507.16 → 2508.10] we need something like
[2508.10 → 2509.44] conditional basic income
[2509.44 → 2510.82] or we need to have
[2510.82 → 2511.68] stronger governance
[2511.68 → 2513.92] to protect our societies.
[2514.46 → 2514.82] Of course,
[2514.88 → 2516.18] that depends on your mental model,
[2516.32 → 2517.18] but we can just look
[2517.18 → 2518.16] at facial recognition
[2518.16 → 2519.38] and see how cities
[2519.38 → 2520.48] all across the U.S.
[2520.50 → 2522.32] are banning facial recognition,
[2522.58 → 2523.64] both in schools
[2523.64 → 2525.10] and in cities
[2525.10 → 2526.32] because of the concern
[2526.32 → 2527.88] of jobs going away
[2527.88 → 2529.34] and the concerns of privacy.
[2529.96 → 2530.54] So, David,
[2530.64 → 2531.52] I really appreciate
[2531.52 → 2532.50] how you brought up
[2532.50 → 2533.28] this idea
[2533.28 → 2534.48] of kind of how
[2534.48 → 2536.00] technology
[2536.00 → 2537.66] makes an impact
[2537.66 → 2538.76] on culture.
[2538.98 → 2539.76] I think that's actually
[2539.76 → 2540.42] really important.
[2540.56 → 2541.94] I think of things like,
[2542.02 → 2542.24] you know,
[2542.50 → 2543.66] everybody kind of thinks
[2543.66 → 2545.36] of Google Translate
[2545.36 → 2546.04] as being,
[2546.18 → 2546.88] you know,
[2546.88 → 2547.40] so great,
[2547.56 → 2548.26] which it is
[2548.26 → 2549.16] in many ways
[2549.16 → 2550.50] and is an amazing
[2550.50 → 2551.18] accomplishment,
[2551.56 → 2551.74] but,
[2552.10 → 2552.32] you know,
[2552.38 → 2553.10] it supports,
[2553.10 → 2554.66] I forget how many languages
[2554.66 → 2554.96] now,
[2555.08 → 2556.10] around 100
[2556.10 → 2558.12] and some of them
[2558.12 → 2559.20] better than others,
[2559.56 → 2560.66] but there's,
[2560.78 → 2561.28] you know,
[2561.66 → 2563.20] over 7,000 languages
[2563.20 → 2563.94] being spoken
[2563.94 → 2564.90] in the world right now,
[2565.28 → 2566.52] so it's kind of
[2566.52 → 2567.42] a drop in the bucket
[2567.42 → 2568.06] and,
[2568.14 → 2569.04] you know,
[2569.08 → 2570.44] over 6,000
[2570.44 → 2571.26] of those languages
[2571.26 → 2571.94] are spoken
[2571.94 → 2573.50] by 25%
[2573.50 → 2574.80] of the world's population,
[2574.80 → 2575.62] which means that
[2575.62 → 2576.58] those are basically
[2576.58 → 2577.88] marginalized communities,
[2578.36 → 2578.58] right?
[2578.64 → 2579.70] And so when technology
[2579.70 → 2580.96] has been made available,
[2580.96 → 2582.20] like you were talking about
[2582.20 → 2583.22] in certain languages,
[2583.66 → 2585.06] all it tends to do
[2585.06 → 2586.16] is kind of further
[2586.16 → 2587.64] marginalized communities.
[2588.28 → 2589.68] And what I'm wondering is,
[2590.16 → 2590.48] you know,
[2590.56 → 2591.62] what do you think
[2591.62 → 2592.40] is a way
[2592.40 → 2593.02] that we could
[2593.02 → 2594.22] incentivize
[2594.22 → 2595.48] sort of creating
[2595.48 → 2596.22] technology
[2596.22 → 2597.30] for these
[2597.30 → 2598.16] marginalized
[2598.16 → 2598.54] or,
[2598.66 → 2599.08] you know,
[2599.16 → 2600.36] using financial terms,
[2600.48 → 2601.36] emerging markets
[2601.36 → 2602.40] or whatever you want
[2602.40 → 2602.92] to call them?
[2603.28 → 2603.84] Do you think
[2603.84 → 2605.28] that there's a role
[2605.28 → 2606.68] there to be played
[2606.68 → 2607.80] by regulation?
[2607.80 → 2608.72] Is that needed?
[2608.72 → 2609.94] Or is there a way
[2609.94 → 2610.88] that kind of we
[2610.88 → 2612.70] as AI practitioners
[2612.70 → 2614.28] can kind of have,
[2614.90 → 2615.10] you know,
[2615.14 → 2616.28] adjust our practices
[2616.28 → 2617.14] and our workflows
[2617.14 → 2619.56] to better orient ourselves
[2619.56 → 2620.82] in terms of the technology
[2620.82 → 2621.48] that we're building?
[2621.94 → 2622.56] I think it could be
[2622.56 → 2624.16] a combination of both.
[2624.44 → 2625.52] I hope it's more
[2625.52 → 2627.32] that we as developers
[2627.32 → 2628.64] reorient ourselves
[2628.64 → 2629.44] and our technology.
[2630.00 → 2630.16] You know,
[2630.18 → 2630.58] think about
[2630.58 → 2631.82] if you are a developer
[2631.82 → 2633.02] building a product,
[2633.28 → 2633.94] you don't want
[2633.94 → 2635.30] your product to break,
[2635.60 → 2635.80] right?
[2635.84 → 2637.62] So whatever the user input is,
[2637.66 → 2638.74] you're designing it
[2638.74 → 2640.14] so that if that's a number,
[2640.14 → 2641.34] the number gets fed
[2641.34 → 2642.10] into the system.
[2642.34 → 2643.74] But if it's text,
[2644.00 → 2645.04] the text gets converted
[2645.04 → 2645.66] to a number
[2645.66 → 2646.68] so it still gets fed
[2646.68 → 2647.32] into the system.
[2647.74 → 2648.62] So I think just like
[2648.62 → 2649.48] data scientists
[2649.48 → 2650.98] and engineers today
[2650.98 → 2651.88] who are developing
[2651.88 → 2652.84] their APIs
[2652.84 → 2653.74] and their systems
[2653.74 → 2654.54] not to break
[2654.54 → 2655.38] based on inputs,
[2655.68 → 2656.76] the same thing should be
[2656.76 → 2658.12] that are we thinking
[2658.12 → 2659.56] about humans first
[2659.56 → 2660.30] in these systems?
[2660.72 → 2661.32] We're starting to see
[2661.32 → 2662.14] AI guidelines.
[2662.42 → 2663.86] I know the European Union
[2663.86 → 2664.66] recently launched
[2664.66 → 2665.22] their own
[2665.22 → 2666.72] AI ethics standards
[2666.72 → 2667.44] that came out
[2667.44 → 2668.32] a few months ago.
[2668.32 → 2669.96] there are similar initiatives
[2669.96 → 2671.34] going on in the US
[2671.34 → 2672.92] as well on ethics
[2672.92 → 2674.52] and about integrating
[2674.52 → 2675.70] these systems for all.
[2676.78 → 2677.20] But you know,
[2677.26 → 2677.94] it's really about
[2677.94 → 2678.98] having the conversation
[2678.98 → 2680.64] and then making sure
[2680.64 → 2681.32] you take action.
[2681.58 → 2682.70] So just like you mentioned
[2682.70 → 2683.58] about the languages,
[2684.06 → 2684.88] I had the opportunity
[2684.88 → 2685.84] to sit down
[2685.84 → 2686.78] on the panel
[2686.78 → 2688.10] and advisory session
[2688.10 → 2689.34] with one of the
[2689.34 → 2690.14] leading candidates
[2690.14 → 2691.44] for the New York City
[2691.44 → 2693.24] mayoral election
[2693.24 → 2694.32] in 2021.
[2694.32 → 2696.54] and that exact topic
[2696.54 → 2697.14] you brought up,
[2697.42 → 2698.36] we brought up as well.
[2698.74 → 2699.50] So, you know,
[2699.58 → 2700.88] you mentioned 6,000,
[2701.00 → 2702.16] 7,000 plus languages
[2702.16 → 2703.28] and in fact,
[2703.34 → 2703.90] in New York City,
[2704.38 → 2705.98] yes, over 20%
[2705.98 → 2707.08] of the people
[2707.08 → 2708.20] do not speak English
[2708.20 → 2710.70] and 10% of that,
[2710.76 → 2711.08] right,
[2711.18 → 2712.80] is about 800,000 people
[2712.80 → 2714.00] of the 8 million people
[2714.00 → 2714.38] in New York.
[2714.78 → 2716.18] So, what if you take
[2716.18 → 2716.94] some of those languages,
[2717.16 → 2719.14] just the top 10 other languages
[2719.14 → 2719.96] that are not English
[2719.96 → 2720.74] or Spanish
[2720.74 → 2723.00] is about a quarter percent,
[2723.56 → 2724.10] sorry,
[2724.18 → 2726.24] 25% of the population.
[2726.74 → 2727.48] That's enough
[2727.48 → 2728.60] to have enough votes
[2728.60 → 2729.64] to win an election.
[2730.32 → 2731.36] Not that the goal
[2731.36 → 2731.96] should be just
[2731.96 → 2732.74] to win an election,
[2733.06 → 2733.86] but it should be
[2733.86 → 2735.18] serving all constituents.
[2735.86 → 2736.56] And when you're
[2736.56 → 2737.78] in an accessible city
[2737.78 → 2738.68] like New York City,
[2739.00 → 2740.14] it should not just be
[2740.14 → 2741.18] translating services
[2741.18 → 2742.42] for eight languages,
[2742.96 → 2744.14] but how about,
[2744.30 → 2744.58] you know,
[2744.64 → 2745.88] at least 100 of them
[2745.88 → 2746.46] or more.
[2746.88 → 2748.00] And I think
[2748.00 → 2748.88] when we start thinking
[2748.88 → 2749.74] about processes,
[2749.96 → 2750.64] we need to do
[2750.64 → 2751.12] a lot more
[2751.12 → 2752.62] competitive intelligence,
[2753.02 → 2753.96] a lot of research
[2753.96 → 2755.94] on who our constituents are,
[2756.30 → 2756.88] and then
[2756.88 → 2758.26] to best serve them.
[2758.44 → 2759.28] And if that means
[2759.28 → 2760.42] rolling out a feature
[2760.42 → 2761.40] in tranches,
[2761.86 → 2763.24] that's totally fine.
[2763.44 → 2764.20] But as long as
[2764.20 → 2765.90] you have the goals there
[2765.90 → 2766.78] and you're thinking
[2766.78 → 2767.54] about excessively
[2767.54 → 2768.16] on the onset,
[2768.48 → 2769.22] it's paving you
[2769.22 → 2769.98] in the right direction.
[2770.54 → 2771.34] So, one of the things
[2771.34 → 2772.00] that I've heard
[2772.00 → 2773.52] talked about a lot lately
[2773.52 → 2775.30] and kind of almost
[2775.30 → 2777.00] as an extension
[2777.00 → 2778.16] maybe of human-centred AI
[2778.16 → 2779.34] is I've heard about
[2779.34 → 2780.90] empathetic technology
[2780.90 → 2781.94] and empathetic AI
[2781.94 → 2783.40] and kind of
[2783.40 → 2784.28] where we need
[2784.28 → 2784.90] to go with that
[2784.90 → 2785.66] and how do you
[2785.66 → 2786.32] connect those two
[2786.32 → 2787.00] from a relationship
[2787.00 → 2787.44] standpoint?
[2787.82 → 2789.20] Where is empathetic
[2789.20 → 2790.18] meet human-centred
[2790.18 → 2791.32] and, you know,
[2791.48 → 2792.04] are there other
[2792.04 → 2792.72] components there
[2792.72 → 2793.32] that I'm missing?
[2793.62 → 2794.14] Yeah, so I think
[2794.14 → 2794.90] bridging the gap
[2794.90 → 2796.08] on human-centred AI
[2796.08 → 2797.32] and empathetic design,
[2797.68 → 2799.62] there's a great story
[2799.62 → 2800.24] that came out
[2800.24 → 2801.14] in California.
[2801.50 → 2802.44] I think it was
[2802.44 → 2803.20] with Kaiser
[2803.20 → 2804.76] just a few months ago
[2804.76 → 2805.86] where there was
[2805.86 → 2806.94] this grandparent
[2806.94 → 2808.50] in his 70 years old
[2808.50 → 2810.18] on his deathbed
[2810.18 → 2811.14] at the hospital
[2811.14 → 2812.36] and they sent
[2812.36 → 2813.20] the robot in
[2813.20 → 2813.64] to say,
[2813.96 → 2814.52] there's no other
[2814.52 → 2815.40] treatment we can do
[2815.40 → 2815.98] for you,
[2816.12 → 2817.26] you're going to die,
[2817.40 → 2817.90] go home,
[2818.14 → 2818.98] something like that.
[2819.02 → 2819.78] I'm paraphrasing,
[2819.94 → 2820.26] of course,
[2820.70 → 2821.72] but, you know,
[2821.86 → 2822.72] that robot,
[2823.16 → 2824.74] not empathetic design.
[2825.30 → 2825.82] Now,
[2826.08 → 2827.16] what could be
[2827.16 → 2828.26] empathetic design?
[2828.56 → 2829.08] A robot
[2829.08 → 2830.06] that's serving
[2830.06 → 2830.72] as a nurse
[2830.72 → 2831.80] to actually clean
[2831.80 → 2832.38] a wound
[2832.38 → 2833.36] when you can't
[2833.36 → 2834.14] always have a nurse
[2834.14 → 2834.64] on call
[2834.64 → 2835.16] because they're
[2835.16 → 2836.60] working 16-hour shifts
[2836.60 → 2838.70] or a robot
[2838.70 → 2839.84] that could have
[2839.84 → 2841.10] infrared computer vision
[2841.10 → 2841.96] to detect
[2841.96 → 2843.00] where your vein is
[2843.00 → 2844.24] so to better help
[2844.24 → 2845.50] inject your medication
[2845.50 → 2847.14] or, you know,
[2847.22 → 2847.80] the insulin
[2847.80 → 2849.00] or whichever treatment
[2849.00 → 2849.64] you need.
[2849.76 → 2850.40] So that could be
[2850.40 → 2851.28] very empathetic.
[2851.74 → 2853.14] There are ways
[2853.14 → 2854.12] to do that
[2854.12 → 2854.96] and it starts
[2854.96 → 2856.00] with design thinking.
[2856.64 → 2857.34] In fact,
[2857.42 → 2858.42] on the Humane podcast
[2858.42 → 2859.22] I talked with
[2859.22 → 2859.86] Chris Butler
[2859.86 → 2860.64] from IP soft
[2860.64 → 2861.72] just about that,
[2861.72 → 2862.40] design thinking
[2862.40 → 2863.90] and all these questions
[2863.90 → 2864.90] that are critical
[2864.90 → 2866.20] because you need
[2866.20 → 2866.86] to think about
[2866.86 → 2868.54] what is the customer
[2868.54 → 2869.58] experience
[2869.58 → 2870.48] or the consumer
[2870.48 → 2871.10] experience
[2871.10 → 2871.64] and that's this
[2871.64 → 2872.30] whole new field
[2872.30 → 2874.06] that's been coined
[2874.06 → 2874.88] in 2019,
[2875.16 → 2875.72] CX,
[2875.84 → 2876.24] so now it's
[2876.24 → 2877.46] the CX industry
[2877.46 → 2879.54] about making sure
[2879.54 → 2881.38] it is about humans,
[2881.54 → 2882.38] it's about customers
[2882.38 → 2883.46] and it's about empathy.
[2883.92 → 2884.94] I think we
[2884.94 → 2886.62] as a society
[2886.62 → 2888.04] have the moral
[2888.04 → 2888.76] obligation
[2888.76 → 2890.04] to provide
[2890.04 → 2890.90] the best possible
[2890.90 → 2891.86] customer service
[2891.86 → 2893.44] and by doing that
[2893.44 → 2894.66] you build loyalty
[2894.66 → 2895.84] and you keep customers
[2895.84 → 2896.82] and create more revenue
[2896.82 → 2898.44] but if you don't do that
[2898.44 → 2899.84] you create the risk
[2899.84 → 2901.22] of not only alienating
[2901.22 → 2901.82] your customers
[2901.82 → 2902.88] but also
[2902.88 → 2903.68] losing those
[2903.68 → 2904.48] who are most valuable.
[2904.94 → 2905.80] One classic case
[2905.80 → 2906.14] of this
[2906.14 → 2906.92] is a lot of
[2906.92 → 2907.86] the cell phone companies
[2907.86 → 2908.20] now
[2908.20 → 2909.62] have been
[2909.62 → 2910.20] using
[2910.20 → 2911.10] data
[2911.10 → 2911.92] to understand
[2911.92 → 2912.54] what is your
[2912.54 → 2913.16] threshold
[2913.16 → 2914.76] of getting angry
[2914.76 → 2915.86] to switch
[2915.86 → 2916.88] from a service
[2916.88 → 2917.32] provider
[2917.32 → 2918.26] and they've been
[2918.26 → 2918.96] using that data
[2918.96 → 2919.96] to see how many times
[2919.96 → 2920.80] they could push back
[2920.80 → 2921.12] on you
[2921.12 → 2922.04] before giving you
[2922.04 → 2922.60] a discount
[2922.60 → 2923.94] or giving you
[2923.94 → 2925.56] a change
[2925.56 → 2926.20] in your service.
[2926.40 → 2926.88] I knew it.
[2927.08 → 2927.28] Right?
[2927.52 → 2928.12] It's real!
[2928.30 → 2928.72] Come on!
[2928.82 → 2929.76] We all like to think
[2929.76 → 2930.52] it's not happening
[2930.52 → 2931.16] but it's
[2931.16 → 2932.28] I call it
[2932.28 → 2933.28] hacking AI
[2933.28 → 2933.74] right?
[2933.84 → 2934.78] Which people have done
[2934.78 → 2935.54] for a while
[2935.54 → 2936.44] but you know
[2936.44 → 2937.12] when you're talking
[2937.12 → 2938.20] to one of these
[2938.20 → 2938.60] companies
[2938.60 → 2939.72] Verizon, Sprint,
[2939.96 → 2940.32] T-Mobile,
[2940.44 → 2941.44] AT&T on the phone
[2941.44 → 2943.28] you better believe
[2943.28 → 2944.56] that in real time
[2944.56 → 2945.20] they're taking
[2945.20 → 2945.86] your audio
[2945.86 → 2947.10] it's converting
[2947.10 → 2947.82] to text
[2947.82 → 2948.84] they're getting
[2948.84 → 2949.52] the sentiment
[2949.52 → 2951.36] and based on that
[2951.36 → 2952.28] they might be making
[2952.28 → 2953.42] some different decisions
[2953.42 → 2955.06] if you sound more angry
[2955.06 → 2956.68] or you sound more calm.
[2957.12 → 2957.90] So you know
[2957.90 → 2959.24] here on the
[2959.24 → 2960.58] Practical AI Podcast
[2960.58 → 2961.26] of course
[2961.26 → 2962.08] we like to keep
[2962.08 → 2962.98] things practical
[2962.98 → 2964.10] and as you're talking
[2964.10 → 2965.08] through all these things
[2965.08 → 2965.58] of course
[2965.58 → 2966.16] you know
[2966.16 → 2967.02] it's probably easier
[2967.02 → 2967.96] for me to see
[2967.96 → 2968.54] practically
[2968.54 → 2969.52] some of those
[2969.52 → 2970.14] hacks
[2970.14 → 2970.84] like you're talking
[2970.84 → 2971.34] about now
[2971.34 → 2972.02] like hacking
[2972.02 → 2972.84] to optimize
[2972.84 → 2973.76] or to
[2973.76 → 2974.42] you know
[2974.42 → 2974.86] make things
[2974.86 → 2975.42] more efficient
[2975.42 → 2976.42] or to automate
[2976.42 → 2977.60] or whatever
[2977.60 → 2978.18] those things are
[2978.18 → 2978.54] just because
[2978.54 → 2979.18] of my
[2979.18 → 2980.08] like technical
[2980.08 → 2980.64] mind
[2980.64 → 2981.52] but as you
[2981.52 → 2981.96] have gone
[2981.96 → 2982.24] through
[2982.24 → 2982.84] and you've
[2982.84 → 2983.20] of course
[2983.20 → 2983.70] advised
[2983.70 → 2984.04] a lot
[2984.04 → 2984.40] of different
[2984.40 → 2984.88] companies
[2984.88 → 2985.48] you've worked
[2985.48 → 2985.90] with a lot
[2985.90 → 2986.26] of different
[2986.26 → 2986.76] students
[2986.76 → 2987.86] and teams
[2987.86 → 2988.70] as they're
[2988.70 → 2989.32] gearing up
[2989.32 → 2990.00] what are
[2990.00 → 2991.44] some practical
[2991.44 → 2992.60] sorts of
[2992.60 → 2993.24] ways
[2993.24 → 2994.62] that like
[2994.62 → 2995.48] me as an
[2995.48 → 2996.46] AI practitioner
[2996.46 → 2997.14] are there
[2997.14 → 2998.14] some kind
[2998.14 → 2998.72] of practical
[2998.72 → 2999.50] steps I could
[2999.50 → 3000.06] take to
[3000.06 → 3000.48] start
[3000.48 → 3001.44] modifying
[3001.44 → 3002.28] my workflow
[3002.28 → 3003.28] such that
[3003.28 → 3004.66] I am
[3004.66 → 3005.28] becoming
[3005.28 → 3006.02] you know
[3006.02 → 3006.86] maybe a
[3006.86 → 3007.14] little bit
[3007.14 → 3007.96] more empathetic
[3007.96 → 3008.44] or human
[3008.44 → 3008.76] centred
[3008.76 → 3009.28] in the way
[3009.28 → 3009.62] that I
[3009.62 → 3010.34] design
[3010.34 → 3011.76] the systems
[3011.76 → 3012.26] that I'm
[3012.26 → 3012.84] building
[3012.84 → 3013.22] have you
[3013.22 → 3013.78] found anything
[3013.78 → 3014.54] that kind
[3014.54 → 3015.20] of consistently
[3015.20 → 3016.24] helps
[3016.24 → 3016.90] or is
[3016.90 → 3017.32] practical
[3017.32 → 3017.72] in that
[3017.72 → 3018.00] sense
[3018.00 → 3018.64] so if
[3018.64 → 3018.78] you're
[3018.78 → 3019.04] building
[3019.04 → 3019.68] systems
[3019.68 → 3020.16] today
[3020.16 → 3020.82] and you're
[3020.82 → 3021.18] thinking
[3021.18 → 3021.74] I want
[3021.74 → 3022.30] to integrate
[3022.30 → 3022.66] AI
[3022.66 → 3023.36] I want
[3023.36 → 3023.68] to bring
[3023.68 → 3024.44] in automation
[3024.44 → 3025.68] but I want
[3025.68 → 3025.96] to make
[3025.96 → 3026.54] sure I best
[3026.54 → 3027.10] serve my
[3027.10 → 3027.60] customers
[3027.60 → 3028.94] it's important
[3028.94 → 3029.90] to first
[3029.90 → 3030.38] decide
[3030.38 → 3030.86] are you
[3030.86 → 3031.18] going to
[3031.18 → 3031.56] go
[3031.56 → 3032.28] with a
[3032.28 → 3032.68] system
[3032.68 → 3032.98] you're
[3032.98 → 3033.56] building
[3033.56 → 3034.08] from the
[3034.08 → 3034.54] ground
[3034.54 → 3035.10] up
[3035.10 → 3036.48] with code
[3036.48 → 3037.40] and engineers
[3037.40 → 3038.22] where you
[3038.22 → 3039.30] can control
[3039.30 → 3040.50] each and
[3040.50 → 3041.50] every step
[3041.50 → 3041.72] in the
[3041.72 → 3042.08] process
[3042.08 → 3043.24] or are you
[3043.24 → 3043.50] going to
[3043.50 → 3043.98] take a
[3043.98 → 3044.96] pre-baked
[3044.96 → 3045.64] solution
[3045.64 → 3047.08] that one
[3047.08 → 3047.46] of these
[3047.46 → 3048.14] data science
[3048.14 → 3048.68] as a service
[3048.68 → 3049.18] companies
[3049.18 → 3050.10] or one
[3050.10 → 3050.32] of the
[3050.32 → 3050.58] cloud
[3050.58 → 3051.24] providers
[3051.24 → 3051.66] like
[3051.66 → 3052.08] Google
[3052.08 → 3053.08] Amazon
[3053.08 → 3053.86] Microsoft
[3053.86 → 3054.82] or IBM
[3054.82 → 3055.74] or others
[3055.74 → 3056.76] have available
[3056.76 → 3057.34] for you
[3057.34 → 3058.14] the reason
[3058.14 → 3058.54] I say
[3058.54 → 3059.10] that is
[3059.10 → 3059.40] because
[3059.40 → 3059.64] if you
[3059.64 → 3060.04] take a
[3060.04 → 3060.56] pre-baked
[3060.56 → 3061.10] solution
[3061.10 → 3062.52] that bias
[3062.52 → 3063.42] and that
[3063.42 → 3064.08] inherent
[3064.08 → 3064.94] potentially
[3064.94 → 3065.96] inaccuracy
[3065.96 → 3066.92] that exists
[3066.92 → 3067.26] in the
[3067.26 → 3067.78] systems
[3067.78 → 3068.78] will be
[3068.78 → 3069.28] present
[3069.28 → 3069.96] in your
[3069.96 → 3070.50] products
[3070.50 → 3071.22] could be
[3071.22 → 3072.06] easier
[3072.06 → 3072.84] to implement
[3072.84 → 3073.22] it
[3073.22 → 3074.08] but you
[3074.08 → 3074.76] may not
[3074.76 → 3075.08] be able
[3075.08 → 3075.64] to customize
[3075.64 → 3076.16] it as
[3076.16 → 3076.50] much as
[3076.50 → 3076.96] you want
[3076.96 → 3077.72] so you
[3077.72 → 3078.00] definitely
[3078.00 → 3078.24] want to
[3078.24 → 3078.56] consider
[3078.56 → 3079.00] first
[3079.00 → 3079.30] whether
[3079.30 → 3079.98] your
[3079.98 → 3080.76] organization
[3080.76 → 3081.62] or your
[3081.62 → 3081.96] team
[3081.96 → 3082.56] has the
[3082.56 → 3082.86] technical
[3082.86 → 3083.34] chops
[3083.34 → 3083.70] and
[3083.70 → 3084.32] availability
[3084.32 → 3084.78] and
[3084.78 → 3085.16] bandwidth
[3085.16 → 3086.44] to do
[3086.44 → 3086.70] some
[3086.70 → 3087.06] coding
[3087.06 → 3088.16] or
[3088.16 → 3088.56] use
[3088.56 → 3088.66] a
[3088.66 → 3089.00] pre-baked
[3089.00 → 3089.50] solution
[3089.50 → 3090.60] I think
[3090.60 → 3090.98] secondly
[3090.98 → 3091.30] then
[3091.30 → 3091.54] it's
[3091.54 → 3091.82] always
[3091.82 → 3092.16] thinking
[3092.16 → 3092.42] about
[3092.42 → 3092.60] your
[3092.60 → 3092.98] customer
[3092.98 → 3093.74] so
[3093.74 → 3094.78] I
[3094.78 → 3095.02] think
[3095.02 → 3095.48] design
[3095.48 → 3095.88] guidelines
[3095.88 → 3096.58] are only
[3096.58 → 3096.98] starting
[3096.98 → 3097.70] to emerge
[3097.70 → 3098.30] right now
[3098.30 → 3099.08] there's
[3099.08 → 3099.30] more
[3099.30 → 3100.00] human
[3100.00 → 3100.58] guidelines
[3100.58 → 3100.92] there's
[3100.92 → 3101.08] been
[3101.08 → 3101.36] ones
[3101.36 → 3101.80] recently
[3101.80 → 3102.14] on
[3102.14 → 3102.48] cyber
[3102.48 → 3103.04] security
[3103.04 → 3103.44] that have
[3103.44 → 3103.80] come out
[3103.80 → 3104.00] in the
[3104.00 → 3104.42] last few
[3104.42 → 3104.76] weeks
[3104.76 → 3106.06] but right
[3106.06 → 3106.22] now
[3106.22 → 3106.56] I think
[3106.56 → 3106.78] it's
[3106.78 → 3107.02] still
[3107.02 → 3107.36] a very
[3107.36 → 3108.02] nascent
[3108.02 → 3108.60] industry
[3108.60 → 3109.24] on
[3109.24 → 3109.68] determining
[3109.68 → 3110.20] the
[3110.20 → 3110.68] exact
[3110.68 → 3111.24] guidelines
[3111.24 → 3112.20] I think
[3112.20 → 3112.76] just
[3112.76 → 3113.06] starting
[3113.06 → 3113.80] to ask
[3113.80 → 3114.32] questions
[3114.32 → 3115.10] such as
[3115.10 → 3115.68] you know
[3115.68 → 3116.40] thinking of
[3116.40 → 3116.86] business
[3116.86 → 3117.20] model
[3117.20 → 3117.70] canvas
[3117.70 → 3118.36] or lean
[3118.36 → 3118.66] model
[3118.66 → 3119.06] canvas
[3119.06 → 3119.80] who are
[3119.80 → 3120.04] my
[3120.04 → 3120.62] customers
[3120.62 → 3122.02] how am
[3122.02 → 3122.44] I'm serving
[3122.44 → 3122.68] them
[3122.68 → 3123.20] I think
[3123.20 → 3123.48] that's a
[3123.48 → 3123.62] great
[3123.62 → 3123.96] starting
[3123.96 → 3124.30] point
[3124.30 → 3125.10] because
[3125.10 → 3125.62] in fact
[3125.62 → 3126.24] most of
[3126.24 → 3126.52] the times
[3126.52 → 3126.68] these
[3126.68 → 3127.10] questions
[3127.10 → 3127.46] that we
[3127.46 → 3127.84] ask
[3127.84 → 3128.04] as
[3128.04 → 3128.50] engineers
[3128.50 → 3129.58] where
[3129.58 → 3129.84] do
[3129.84 → 3130.22] all
[3130.22 → 3130.48] those
[3130.48 → 3130.90] answers
[3130.90 → 3131.24] lie
[3131.24 → 3131.72] in
[3131.72 → 3131.86] our
[3131.86 → 3132.28] mind
[3132.28 → 3132.78] we
[3132.78 → 3133.12] never
[3133.12 → 3133.40] write
[3133.40 → 3133.56] them
[3133.56 → 3133.92] down
[3133.92 → 3134.46] once
[3134.46 → 3134.64] you
[3134.64 → 3134.96] start
[3134.96 → 3135.30] writing
[3135.30 → 3135.46] it
[3135.46 → 3135.72] down
[3135.72 → 3135.94] it
[3135.94 → 3136.14] looks
[3136.14 → 3137.06] completely
[3137.06 → 3138.02] different
[3138.02 → 3138.90] and
[3138.90 → 3139.20] that's
[3139.20 → 3139.34] why
[3139.34 → 3139.60] I think
[3139.60 → 3139.76] it's
[3139.76 → 3140.16] important
[3140.16 → 3140.46] that
[3140.46 → 3140.80] if
[3140.80 → 3140.96] you're
[3140.96 → 3141.22] building
[3141.22 → 3141.42] a
[3141.42 → 3141.78] product
[3141.78 → 3141.98] or
[3141.98 → 3142.32] changing
[3142.32 → 3142.54] a
[3142.54 → 3142.78] product
[3142.78 → 3143.04] that's
[3143.04 → 3143.24] putting
[3143.24 → 3143.60] humans
[3143.60 → 3143.98] first
[3143.98 → 3144.64] think
[3144.64 → 3144.88] about
[3144.88 → 3145.30] partnering
[3145.30 → 3145.68] with
[3145.68 → 3146.02] someone
[3146.02 → 3146.60] who
[3146.60 → 3147.16] is
[3147.16 → 3147.42] a
[3147.42 → 3148.00] strategist
[3148.00 → 3148.28] in
[3148.28 → 3148.72] business
[3148.72 → 3149.20] or
[3149.20 → 3149.48] someone
[3149.48 → 3149.88] who
[3149.88 → 3150.18] might
[3150.18 → 3150.38] come
[3150.38 → 3150.52] from
[3150.52 → 3150.66] the
[3150.66 → 3150.86] liberal
[3150.86 → 3151.24] arts
[3151.24 → 3151.96] background
[3151.96 → 3152.54] because
[3152.54 → 3152.84] they're
[3152.84 → 3152.94] going
[3152.94 → 3153.04] to
[3153.04 → 3153.30] add
[3153.30 → 3153.48] that
[3153.48 → 3153.98] unique
[3153.98 → 3154.42] vantage
[3154.42 → 3154.96] that
[3154.96 → 3155.38] could
[3155.38 → 3155.92] help
[3155.92 → 3156.12] you
[3156.12 → 3156.60] think
[3156.60 → 3156.90] about
[3156.90 → 3157.26] each
[3157.26 → 3157.36] and
[3157.36 → 3157.50] every
[3157.50 → 3157.82] person
[3157.82 → 3158.48] I love
[3158.48 → 3158.76] how you
[3158.76 → 3159.10] kind of
[3159.10 → 3159.44] came
[3159.44 → 3159.66] full
[3159.66 → 3160.00] circle
[3160.00 → 3160.24] right
[3160.24 → 3160.50] there
[3160.50 → 3160.90] and
[3160.90 → 3161.04] kind
[3161.04 → 3161.10] of
[3161.10 → 3161.26] got
[3161.26 → 3161.56] back
[3161.56 → 3161.74] as
[3161.74 → 3161.94] we
[3161.94 → 3162.60] talked
[3162.60 → 3162.86] a little
[3162.86 → 3163.02] bit
[3163.02 → 3163.30] about
[3163.30 → 3163.50] those
[3163.50 → 3163.72] different
[3163.72 → 3164.20] backgrounds
[3164.20 → 3165.12] early
[3165.12 → 3165.24] in
[3165.24 → 3165.34] the
[3165.34 → 3165.62] call
[3165.62 → 3166.00] and
[3166.00 → 3166.60] so
[3166.60 → 3168.04] if
[3168.04 → 3168.56] somebody
[3168.56 → 3169.02] has
[3169.02 → 3169.48] gotten
[3169.48 → 3169.78] a little
[3169.78 → 3170.34] taste
[3170.34 → 3170.88] of
[3170.88 → 3171.46] what
[3171.46 → 3171.82] human
[3171.82 → 3172.12] centred
[3172.12 → 3172.46] AI
[3172.46 → 3172.76] and
[3172.76 → 3173.06] design
[3173.06 → 3173.42] thinking
[3173.42 → 3173.68] and
[3173.68 → 3174.14] empathetic
[3174.14 → 3174.68] technologies
[3174.68 → 3175.02] are
[3175.02 → 3175.72] in this
[3175.72 → 3176.26] conversation
[3176.26 → 3176.50] but
[3176.50 → 3176.62] if
[3176.62 → 3176.72] they
[3176.72 → 3176.88] want
[3176.88 → 3177.00] to
[3177.00 → 3177.18] dig
[3177.18 → 3177.36] into
[3177.36 → 3177.62] that
[3177.62 → 3177.82] do
[3177.82 → 3177.94] you
[3177.94 → 3178.12] have
[3178.12 → 3178.30] any
[3178.30 → 3178.80] resources
[3178.80 → 3179.58] that
[3179.58 → 3179.74] you
[3179.74 → 3179.94] think
[3179.94 → 3180.04] are
[3180.04 → 3180.40] particularly
[3180.40 → 3180.74] good
[3180.74 → 3180.88] or
[3180.88 → 3180.98] you
[3180.98 → 3181.10] can
[3181.10 → 3181.34] point
[3181.34 → 3181.46] them
[3181.46 → 3181.66] to
[3181.66 → 3181.86] that
[3181.86 → 3182.32] listeners
[3182.32 → 3183.10] can
[3183.10 → 3183.36] go
[3183.36 → 3183.58] and
[3183.58 → 3184.28] see
[3184.28 → 3184.48] more
[3184.48 → 3184.72] about
[3184.72 → 3184.82] it
[3184.82 → 3185.36] understand
[3185.36 → 3185.76] more
[3185.76 → 3185.90] and
[3185.90 → 3186.06] learn
[3186.06 → 3186.40] more
[3186.40 → 3186.92] in
[3186.92 → 3187.16] this
[3187.16 → 3187.96] effort
[3187.96 → 3188.46] yeah
[3188.46 → 3188.68] one
[3188.68 → 3188.80] of
[3188.80 → 3188.96] my
[3188.96 → 3189.56] favourite
[3189.56 → 3190.36] trend
[3190.36 → 3190.76] reports
[3190.76 → 3191.18] that's
[3191.18 → 3191.32] been
[3191.32 → 3191.80] talking
[3191.80 → 3192.38] a lot
[3192.38 → 3192.78] about
[3192.78 → 3193.02] these
[3193.02 → 3193.20] sub
[3193.20 → 3193.58] industries
[3193.58 → 3194.56] is
[3194.56 → 3195.06] from
[3195.06 → 3195.60] one
[3195.60 → 3195.68] of
[3195.68 → 3195.80] my
[3195.80 → 3196.14] mentors
[3196.14 → 3196.36] in
[3196.36 → 3196.50] New
[3196.50 → 3196.80] York
[3196.80 → 3196.98] who
[3196.98 → 3197.08] I
[3197.08 → 3197.26] went
[3197.26 → 3197.46] through
[3197.46 → 3197.92] her
[3197.92 → 3198.44] teaching
[3198.44 → 3198.76] training
[3198.76 → 3199.22] fellowship
[3199.22 → 3199.68] Amy
[3199.68 → 3200.18] Webb
[3200.18 → 3200.46] so
[3200.46 → 3200.80] Amy
[3200.80 → 3201.14] Webb
[3201.14 → 3201.68] has
[3201.68 → 3201.84] this
[3201.84 → 3202.04] new
[3202.04 → 3202.26] book
[3202.26 → 3202.44] the
[3202.44 → 3202.68] big
[3202.68 → 3203.16] nine
[3203.16 → 3203.44] she
[3203.44 → 3203.74] talks
[3203.74 → 3203.98] a lot
[3203.98 → 3204.18] about
[3204.18 → 3204.78] technology
[3204.78 → 3204.98] and
[3204.98 → 3205.34] trends
[3205.34 → 3205.56] and
[3205.56 → 3205.98] teaches
[3205.98 → 3206.16] at
[3206.16 → 3206.52] NYU
[3206.52 → 3207.20] but
[3207.20 → 3207.38] she
[3207.38 → 3207.84] has
[3207.84 → 3208.26] a
[3208.26 → 3208.44] tech
[3208.44 → 3208.66] trend
[3208.66 → 3208.98] report
[3208.98 → 3209.64] that
[3209.64 → 3209.84] is
[3209.84 → 3210.22] almost
[3210.22 → 3210.86] 400
[3210.86 → 3211.32] pages
[3211.32 → 3211.62] this
[3211.62 → 3211.86] year
[3211.86 → 3212.18] so
[3212.18 → 3212.34] it
[3212.34 → 3212.48] is
[3212.48 → 3212.88] definitely
[3217.96 → 3218.54] some
[3218.54 → 3218.80] is
[3218.80 → 3219.86] human
[3219.86 → 3220.28] based
[3220.28 → 3220.54] some
[3220.54 → 3220.72] is
[3220.72 → 3221.08] cyber
[3221.08 → 3222.08] and
[3222.08 → 3222.22] you
[3222.22 → 3222.34] can
[3222.34 → 3222.58] start
[3222.58 → 3222.76] to
[3222.76 → 3222.94] see
[3222.94 → 3223.14] what
[3223.14 → 3223.64] companies
[3223.64 → 3224.08] are
[3224.08 → 3224.54] working
[3224.54 → 3225.10] there
[3225.10 → 3225.54] and
[3225.54 → 3225.72] what
[3225.72 → 3225.86] those
[3225.86 → 3226.18] products
[3226.18 → 3226.44] look
[3226.44 → 3226.68] like
[3226.68 → 3227.34] I
[3227.34 → 3227.54] think
[3227.54 → 3228.00] also
[3228.00 → 3228.68] Matt
[3228.68 → 3228.96] Turk
[3228.96 → 3229.40] from
[3229.40 → 3229.74] First
[3229.74 → 3229.94] Mark
[3229.94 → 3230.32] Capital
[3230.32 → 3230.56] in
[3230.56 → 3230.70] New
[3230.70 → 3230.98] York
[3230.98 → 3231.60] really
[3231.60 → 3231.92] like
[3231.92 → 3232.18] him
[3232.18 → 3232.50] and
[3232.50 → 3232.74] he
[3232.74 → 3233.10] has
[3233.10 → 3233.96] every
[3233.96 → 3234.28] year
[3234.28 → 3234.50] he
[3234.50 → 3234.78] creates
[3234.78 → 3235.06] a big
[3235.06 → 3235.54] dashboard
[3235.54 → 3235.94] of all
[3235.94 → 3236.14] the
[3236.14 → 3236.54] AI
[3236.54 → 3236.92] data
[3236.92 → 3237.24] science
[3237.24 → 3237.70] companies
[3237.70 → 3238.20] and
[3238.20 → 3238.36] what
[3238.36 → 3238.54] they're
[3238.54 → 3238.90] doing
[3238.90 → 3239.86] in
[3239.86 → 3239.98] the
[3239.98 → 3240.42] industry
[3240.42 → 3241.10] that's
[3241.10 → 3241.32] really
[3241.32 → 3241.64] where
[3241.64 → 3241.86] the
[3241.86 → 3242.10] data
[3242.10 → 3242.42] science
[3242.42 → 3242.68] as a
[3242.68 → 3243.00] service
[3243.00 → 3243.28] has
[3243.28 → 3243.44] been
[3243.44 → 3243.82] emerging
[3243.82 → 3244.42] and
[3244.42 → 3244.58] he's
[3244.58 → 3244.86] also
[3244.86 → 3245.20] looking
[3245.20 → 3245.42] at
[3245.42 → 3245.86] companies
[3245.86 → 3246.08] that
[3246.08 → 3246.18] are
[3246.18 → 3246.40] starting
[3246.40 → 3246.56] to
[3246.56 → 3246.76] think
[3246.76 → 3247.04] about
[3247.04 → 3247.52] ethics
[3247.52 → 3248.00] and
[3248.00 → 3248.12] I
[3248.12 → 3248.42] think
[3248.42 → 3249.04] some
[3249.04 → 3249.16] of
[3249.16 → 3249.32] those
[3249.32 → 3249.48] were
[3249.48 → 3249.72] shown
[3249.72 → 3249.94] this
[3249.94 → 3250.16] year
[3250.16 → 3250.58] but
[3250.58 → 3250.70] I
[3250.70 → 3250.90] think
[3250.90 → 3251.18] starting
[3251.18 → 3251.46] next
[3251.46 → 3251.66] year
[3251.66 → 3251.82] we're
[3251.82 → 3251.90] going
[3251.90 → 3251.96] to
[3251.96 → 3252.12] see
[3252.12 → 3252.64] a lot
[3252.64 → 3252.76] of
[3252.76 → 3252.90] those
[3252.90 → 3253.42] companies
[3253.42 → 3254.22] emerging
[3254.22 → 3254.64] into
[3254.64 → 3254.80] the
[3254.80 → 3255.16] trends
[3255.16 → 3256.26] awesome
[3256.26 → 3256.74] well
[3256.74 → 3257.34] thank you
[3257.34 → 3257.80] so much
[3257.80 → 3258.26] for sharing
[3258.26 → 3258.50] those
[3258.50 → 3258.82] things
[3258.82 → 3259.16] I know
[3259.16 → 3259.34] I'm
[3259.34 → 3259.46] going
[3259.46 → 3259.94] to
[3259.94 → 3260.18] take
[3260.18 → 3260.34] a
[3260.34 → 3260.52] look
[3260.52 → 3260.82] right
[3260.82 → 3261.28] afterwards
[3261.28 → 3261.80] but
[3261.80 → 3262.76] really
[3262.76 → 3263.06] been
[3263.06 → 3263.32] great
[3263.32 → 3263.66] to have
[3263.66 → 3263.78] you
[3263.78 → 3263.92] on
[3263.92 → 3264.04] the
[3264.04 → 3264.54] podcast
[3264.54 → 3264.90] David
[3264.90 → 3265.30] it's
[3265.30 → 3265.52] been
[3265.52 → 3266.06] awesome
[3266.06 → 3266.58] to hear
[3266.58 → 3266.88] about
[3266.88 → 3267.20] your
[3267.20 → 3267.84] perspective
[3267.84 → 3268.54] on
[3268.54 → 3268.88] human
[3268.88 → 3269.18] centred
[3269.18 → 3269.66] AI
[3269.66 → 3270.54] to
[3270.54 → 3270.72] hear
[3270.72 → 3270.92] a little
[3270.92 → 3271.08] bit
[3271.08 → 3271.30] about
[3271.30 → 3272.08] galvanize
[3272.08 → 3272.32] and
[3272.32 → 3272.52] data
[3272.52 → 3272.86] science
[3272.86 → 3273.24] learning
[3273.24 → 3273.48] and
[3273.48 → 3273.66] all
[3273.66 → 3273.92] sorts
[3273.92 → 3274.06] of
[3274.06 → 3274.40] things
[3274.40 → 3274.70] so
[3274.70 → 3275.40] I
[3275.40 → 3275.72] really
[3275.72 → 3276.20] appreciate
[3276.20 → 3276.78] you
[3276.78 → 3277.24] being
[3277.24 → 3277.44] on
[3277.44 → 3277.60] the
[3277.60 → 3277.90] show
[3277.90 → 3278.34] and
[3278.34 → 3278.84] really
[3278.84 → 3279.58] recommend
[3279.58 → 3280.18] to
[3280.18 → 3280.54] our
[3280.54 → 3280.92] listeners
[3280.92 → 3281.42] to go
[3281.42 → 3281.70] check
[3281.70 → 3281.90] out
[3281.90 → 3282.12] the
[3282.12 → 3282.58] humane
[3282.58 → 3283.06] podcast
[3283.06 → 3284.28] and
[3284.28 → 3285.14] take
[3285.14 → 3285.34] a
[3285.34 → 3285.66] listen
[3285.66 → 3286.38] see
[3286.38 → 3286.66] some
[3286.66 → 3286.82] of
[3286.82 → 3287.04] that
[3287.04 → 3287.32] great
[3287.32 → 3287.76] content
[3287.76 → 3288.20] that
[3288.20 → 3288.82] was
[3288.82 → 3289.22] mentioned
[3289.22 → 3289.60] but
[3289.60 → 3290.04] thank
[3290.04 → 3290.18] you
[3290.18 → 3290.36] so
[3290.36 → 3290.54] much
[3290.54 → 3290.88] for
[3290.88 → 3291.44] joining
[3291.44 → 3291.68] us
[3291.68 → 3291.94] David
[3291.94 → 3292.60] thanks
[3292.60 → 3292.74] so
[3292.74 → 3292.92] much
[3292.92 → 3293.20] Daniel
[3293.20 → 3293.54] thanks
[3293.54 → 3293.66] so
[3296.06 → 3297.64] all
[3297.64 → 3297.78] right
[3297.78 → 3298.04] thank
[3298.04 → 3298.12] you
[3298.12 → 3298.24] for
[3298.24 → 3298.42] tuning
[3298.42 → 3298.64] into
[3298.64 → 3298.92] this
[3298.92 → 3299.52] episode
[3299.52 → 3299.82] of
[3299.82 → 3300.26] practical
[3300.26 → 3300.46] AI
[3300.46 → 3300.82] if
[3300.82 → 3300.92] you
[3300.92 → 3301.12] enjoyed
[3301.12 → 3301.28] the
[3301.28 → 3301.48] show
[3301.48 → 3301.76] do us
[3301.76 → 3302.18] a favour
[3302.18 → 3302.52] go on
[3302.52 → 3302.88] iTunes
[3302.88 → 3303.22] give us
[3303.22 → 3303.68] a rating
[3303.68 → 3304.26] go in your
[3304.26 → 3305.12] podcast app
[3305.12 → 3305.82] and favourite it
[3305.82 → 3306.46] if you are on
[3306.46 → 3307.62] Twitter or social network
[3307.62 → 3308.64] share a link with a friend
[3308.64 → 3309.38] whatever you have to do
[3309.38 → 3310.36] share the show with a friend
[3310.36 → 3311.08] if you enjoyed it
[3311.08 → 3312.02] and bandwidth for
[3312.02 → 3313.48] changelog is provided by
[3313.48 → 3314.04] Vastly
[3314.04 → 3314.72] learn more at
[3314.72 → 3315.58] fastly.com
[3315.58 → 3316.72] and we catch our errors
[3316.72 → 3317.84] before our users do here at
[3317.84 → 3318.58] changelog because of
[3318.58 → 3318.98] Rollbar
[3318.98 → 3320.08] check them out at
[3320.08 → 3320.64] rollbar.com
[3320.64 → 3321.62] slash changelog
[3321.62 → 3323.10] and we're hosted on
[3323.10 → 3324.40] Linde cloud servers
[3324.40 → 3324.90] head to
[3324.90 → 3326.38] lino.com slash changelog
[3326.38 → 3326.92] check them out
[3326.92 → 3327.84] support this show
[3327.84 → 3329.76] this episode is hosted by
[3329.76 → 3330.86] Daniel Whiten ack and
[3330.86 → 3331.46] Chris Benson
[3331.46 → 3332.90] the music is by
[3332.90 → 3333.92] Break master Cylinder
[3333.92 → 3335.12] and you can find more
[3335.12 → 3336.24] shows just like this
[3336.24 → 3337.78] at changelog.com
[3337.78 → 3338.60] when you go there
[3338.60 → 3339.90] pop in your email address
[3339.90 → 3341.10] get our weekly email
[3341.10 → 3341.96] keeping you up to date
[3341.96 → 3342.70] with the news
[3342.70 → 3343.62] and podcasts for
[3343.62 → 3344.72] developers in your
[3344.72 → 3345.86] inbox every single
[3345.86 → 3346.22] week
[3346.22 → 3347.38] thanks for tuning in
[3347.38 → 3348.32] we'll see you next week
[3348.32 → 3364.66] at
