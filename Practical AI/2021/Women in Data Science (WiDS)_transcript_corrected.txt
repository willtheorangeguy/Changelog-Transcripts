[0.00 → 6.46] Change happens when people are no longer seen as different, when women doing STEM, you know,
[6.52 → 12.36] the same with people from different colours, different races doing STEM, when that's normalized.
[12.98 → 15.74] And that is what we're working on with women in data science.
[15.74 → 21.38] We're trying to normalize this, that it's totally natural to have a woman tell you about AI.
[21.90 → 22.36] Why not?
[25.40 → 28.06] Big thanks to our partners, Linde Vastly and Launch Darkly.
[28.06 → 30.48] We love Linde. They keep it fast and simple.
[30.60 → 32.96] Check them out at Linode.com slash changelog.
[33.20 → 35.26] Our bandwidth is provided by Vastly.
[35.60 → 39.16] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[39.42 → 41.14] Get a demo at LaunchDarkly.com.
[41.68 → 44.24] This episode is brought to you by our friends at O'Reilly.
[44.60 → 47.18] Many of you know O'Reilly for their animal tech books and their conferences,
[47.50 → 50.72] but you may not know they have an online learning platform as well.
[51.08 → 55.52] The platform has all their books, all their videos, and all their conference talks.
[55.52 → 60.06] Plus, you can learn by doing with live online training courses and virtual conferences,
[60.58 → 66.64] certification practice exams, and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[66.94 → 76.34] They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security,
[76.82 → 80.58] and even soft skills like business management and presentation skills.
[80.72 → 82.50] You name it, it is all in there.
[82.50 → 86.06] If you need to keep your team or yourself up to speed on their tech skills,
[86.16 → 88.00] then check out O'Reilly's online learning platform.
[88.54 → 92.06] Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[92.18 → 94.46] Again, O'Reilly.com slash changelog.
[94.46 → 114.92] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[115.26 → 119.32] This is where conversations around AI, machine learning, and data science happen.
[119.32 → 124.40] Join the community and Slack with us around various topics of the show at changelog.com slash community,
[124.74 → 125.70] and follow us on Twitter.
[125.82 → 127.44] We are at Practical AI FM.
[133.94 → 137.26] Welcome to another episode of the Practical AI podcast.
[137.64 → 144.08] We are a podcast that tries to make artificial intelligence practical, productive, and accessible to everyone.
[144.08 → 146.08] My name is Chris Benson.
[146.22 → 147.70] I work for Lockheed Martin.
[148.30 → 154.68] And my co-host, Daniel Whiten ack, who is always with me, is unfortunately unable to join us today due to a family obligation.
[155.34 → 161.06] And I know he is really, really going to be missing this because, as any of our regular listeners know,
[161.52 → 164.76] we love to talk about diversity in data science.
[164.76 → 170.68] And we love to talk about a world in which all the things that shouldn't matter don't matter.
[170.68 → 172.74] And we aspire to that.
[172.90 → 179.22] And so, with me today, I have Margot Gerrit sen, who is a Stanford professor.
[179.76 → 185.02] She is co-founder and co-director of the Global Women in Data Science organization
[185.02 → 188.14] and the host of the WIDE podcast herself.
[188.64 → 190.24] So, welcome to the show, Margot.
[191.04 → 191.86] Thanks, Chris.
[191.92 → 193.40] It's really wonderful to be here.
[193.62 → 195.44] It's nice to be on the other side of the mic.
[195.78 → 196.26] Absolutely.
[196.56 → 198.06] I am really excited to have you here.
[198.06 → 204.38] One of the things that anyone who's listened to the show for a while, Daniel and I also talk a little bit about our own lives and our own family and stuff.
[204.48 → 210.12] And so, most of our longtime listeners know that I have a daughter, and I'm always thinking about her future.
[210.46 → 215.66] And so, I am very excited about this episode so that we can get some good information out there.
[216.14 → 221.70] I was wondering if you would start off telling us a bit about your own background.
[222.04 → 224.80] I'm intrigued because I believe that you're originally from the Netherlands.
[224.80 → 232.62] And I was wondering if you might even go all the way back to that and start us there and bring us forward to why we might be talking here today.
[232.80 → 233.14] Okay.
[233.26 → 234.34] That sounds great, Chris.
[234.42 → 234.74] Thank you.
[234.82 → 244.56] I was born in a relatively small village and town in the province of the Netherlands called Zeeland, which stands for the land of the sea, obviously.
[244.56 → 247.34] So, it's a collection of islands.
[247.62 → 251.54] And so, I've always been an ocean girl for that reason.
[252.08 → 253.70] But it was a pretty small place.
[253.86 → 256.98] And my dad was a teacher at the local high school.
[257.22 → 259.22] And my mom was a homemaker.
[259.80 → 261.60] And she was a nurse before they got married.
[261.72 → 266.34] But, you know, in the 60s in Holland, as soon as you got married as a woman, you stopped working.
[266.46 → 268.30] That was pretty much what you did.
[268.30 → 270.72] I have a brother and a sister.
[271.18 → 273.02] And we grew up in that place.
[273.74 → 277.36] My parents migrated there in the 60s.
[277.54 → 280.50] It was a place that was mostly agricultural before that.
[280.76 → 284.20] And it was actually flooded at some point in the 50s.
[284.28 → 286.64] That was quite a famous flood where lots of people died.
[286.64 → 294.54] And then they started what they call the Delta Works to protect the country from storm surges and flooding.
[294.54 → 302.60] And as part of this sort of reinvigoration of the area and protection, they wanted people to migrate down.
[302.76 → 308.66] And so, my dad got this offer to go to a Catholic school in this area and become a teacher.
[309.02 → 315.08] And so, he took his new wife down south, west, to the peninsula of the island.
[315.36 → 316.80] And that's where I grew up.
[316.84 → 318.20] It's an absolutely beautiful place.
[318.86 → 323.46] Funnily enough, later, I lived in New Zealand for five years.
[323.46 → 327.88] So, that was sort of a natural progression for me to go from Old Zealand to New Zealand.
[328.98 → 329.24] Yeah.
[329.30 → 335.00] New Zealand was named by Abel Tasman, who grew up and lived very close to where I grew up.
[335.14 → 337.06] So, you know, that is an interesting connection.
[337.66 → 341.84] So, when I was growing up, I was a pretty, pretty shy, introverted girl, probably.
[342.12 → 344.38] I loved being outside and biking.
[344.38 → 345.86] And I loved reading.
[346.46 → 347.60] And I loved learning.
[348.24 → 349.34] I really loved learning.
[349.34 → 353.56] And so, I was always one of these people in school who worked very hard.
[353.76 → 356.42] And I really liked science and mathematics.
[357.22 → 358.88] And I was also a pretty competitive kid.
[359.04 → 361.50] So, I always tried to do my best.
[361.62 → 366.28] But I never really, at that time, thought I would really continue in that direction.
[366.78 → 367.50] And why not?
[367.58 → 367.72] Yeah.
[367.72 → 371.46] What was it about that that made you think that maybe that's not where you're going to end up?
[371.46 → 375.82] Well, mostly just the fact that I grew up in a relatively small place.
[376.02 → 377.32] I mean, there were people with ambitions.
[377.82 → 380.68] But, you know, my parents had never been to university.
[381.50 → 383.62] And, in fact, my dad had to leave high school.
[383.76 → 386.66] He was a teenager at the end of Second World War.
[387.36 → 389.66] And there was a lot of poverty at that time.
[389.74 → 392.20] And so, there was no money for him to go to college.
[392.30 → 393.38] His older brothers could.
[393.48 → 394.96] But he was part of a large family.
[394.96 → 398.74] And so, he had to start working at the age of 16.
[398.90 → 400.52] And he worked as a kindergarten teacher.
[400.74 → 406.08] And then moved up through evening studies to finally become a teacher at high school.
[406.82 → 410.58] And my mom left high school and became a nurse in the hospital.
[410.82 → 413.36] And lived in the hospital also until she married my dad.
[413.60 → 416.92] And so, in our household, learning was definitely encouraged.
[417.48 → 423.68] But it wasn't really this culture of university and maybe becoming a professor or anything like that.
[423.68 → 426.86] So, I thought that I should go to university.
[427.18 → 431.90] I was extremely lucky to live in Holland at the time and to be raised there.
[432.38 → 438.14] Because education at the time was free, really, for everybody who qualified.
[438.44 → 441.20] So, you had to get qualified for university.
[441.44 → 443.74] Then you were assigned to university in Holland.
[443.86 → 446.10] And you would go there and pick an area of study.
[446.60 → 447.88] But it was basically free.
[447.88 → 453.26] And so, I went and studied mathematics at University of Technology at Delft.
[453.68 → 455.72] And why mathematics at the time?
[455.82 → 458.70] Because there were so many things I was interested in.
[459.04 → 463.64] And I didn't really want to pin myself down at that early stage.
[463.72 → 467.82] And I thought, let's go study something that's really general.
[468.30 → 472.50] That gives me foundation so that later I can maybe specialize in another area.
[472.84 → 475.74] Because, you know, I wanted to know about flight.
[475.74 → 477.88] And I wanted to understand fluid flow.
[478.66 → 482.58] And I was interested in the earth and geophysics.
[482.92 → 485.76] And was really interested in physics as well and design.
[485.90 → 487.24] And there were so many areas.
[487.42 → 488.82] And I thought, ah, I can't choose.
[489.10 → 492.88] So, I just studied math with a lot of physics on the side.
[493.60 → 500.58] And later also in my career, it turned out that I've gone to many different application areas with that sort of foundation.
[500.58 → 501.06] Yeah.
[501.40 → 501.66] Yeah.
[501.70 → 504.14] So, from the age of 18, I went to Delft University.
[504.82 → 507.78] Actually, from a very young age, I wanted to leave the country.
[508.12 → 511.48] I'd always been looking west over the North Sea.
[511.72 → 514.46] You know, sort of thinking, what lands are beyond here?
[515.40 → 517.48] I wanted to go away, get away.
[517.76 → 519.26] And I've always had that idea.
[519.36 → 521.40] I think I wrote it in my diary when I was eight.
[521.58 → 522.94] Saying, I'm not going to stay here.
[523.00 → 523.70] I'm going to leave.
[524.22 → 525.42] And I've always felt that way.
[525.56 → 526.32] That's remarkable.
[527.14 → 528.48] Well, I don't know if it's remarkable.
[528.68 → 530.02] It's just, I don't know what it was.
[530.06 → 531.18] But it was just a hunkering.
[531.42 → 532.78] You already knew at that point.
[533.08 → 536.40] You know, the funny thing was, I don't think I've ever said this in the podcast.
[536.64 → 542.40] But at eight, I wrote in my diary, I'm going to marry a Scot and move west.
[542.90 → 543.90] And guess what?
[543.96 → 545.32] I did marry a Scot.
[546.60 → 548.12] Self-fulfilling prophecy there.
[548.12 → 548.42] Yeah.
[548.42 → 549.64] I divorced him too.
[549.92 → 550.92] But I did marry him.
[552.04 → 553.04] I did marry him.
[553.70 → 553.94] Yeah.
[553.94 → 559.80] So I looked for opportunities and I wanted to go away for studies, but that was hard.
[559.98 → 564.86] And it's particularly difficult to go overseas for studies where studies cost you.
[565.00 → 569.18] When in Holland, there is a very good university or multiple where education is free.
[569.28 → 571.48] So I stayed until I had my engineer's degree.
[571.82 → 575.16] That's exactly what I wanted to ask you next was you are a Stanford professor.
[575.36 → 575.54] Yeah.
[575.54 → 579.90] And a lot of people will really, they're thinking, wow, you know, I wish I could be that.
[580.00 → 581.14] That's what I want to aspire to.
[581.14 → 587.98] If you hadn't had that opportunity, the access to education that wasn't free, you know, because
[587.98 → 592.36] here we're talking about the cost of education all the time, especially here in the United
[592.36 → 594.12] States, it's skyrocketed over years.
[594.44 → 598.62] Do you think if you hadn't had that access, your trajectory would have been vastly different?
[598.88 → 600.16] Would you have managed it anyway?
[600.46 → 601.56] How would that have affected it?
[601.56 → 602.18] I'm just curious.
[602.18 → 608.26] I can't say, you know, honestly, I think, like I said before, I've been just so unbelievably
[608.26 → 610.44] lucky to be born where I was.
[610.78 → 614.72] And I'm a big, big supporter of free education.
[615.06 → 620.46] I was from a middle-class family and I had two extremely supportive parents.
[620.68 → 622.98] You know, I was not from a low-income family.
[622.98 → 629.02] And with the support of my family, I probably would have been able to manage also without.
[629.34 → 633.54] I don't quite know how because, you know, I never really thought about it, but I lucked
[633.54 → 633.80] out.
[634.16 → 639.70] At that time also, honestly, I'd never, for the life of me, when I was 18, I started studying,
[639.86 → 643.68] had any notion of being a professor at the university overseas.
[644.02 → 647.10] All I knew is I want to leave the country at some point.
[647.10 → 649.62] And I like teaching and I like mathematics.
[650.50 → 654.04] And Stanford also, for me, happened purely by accident.
[654.30 → 660.58] So to leave the country, I did that with a scholarship that I won in my last year at
[660.58 → 661.08] university.
[661.76 → 664.50] And this is the International Rotary Foundation.
[664.80 → 668.92] They're known for giving scholarships to high school students, but they also give scholarships
[668.92 → 674.86] to graduate students to spend a year abroad as sort of ambassador of the country.
[674.86 → 680.28] And on the fluke, I saw the advert hanging in the hallway at some point.
[680.38 → 682.00] And I thought, oh, why not try this?
[682.72 → 688.34] And it was a competition among students of three universities, you know, Rotterdam, Delft and
[688.34 → 689.92] Leiden and nearby universities.
[690.68 → 693.96] And to my shock, I won that scholarship and could go anywhere.
[694.50 → 698.34] And I happened to be at a conference and I met this person from Colorado.
[698.68 → 701.10] And, you know, I knew the States a little bit, but it'd never been.
[701.10 → 706.58] And I looked up Colorado and I thought, oh, that's exactly what I want, you know, because
[706.58 → 713.68] I wanted to leave flat and gray and rainy Holland for a place with mountains, you know,
[713.80 → 716.58] west of here, across the ocean and sunshine.
[717.10 → 720.28] And, you know, Colorado had as many sunny days as we had rainy days.
[720.28 → 722.14] And I thought that was just fantastic.
[722.52 → 723.70] So that's what I did.
[723.78 → 725.42] So I just went there for a year.
[725.42 → 730.88] And while I was there, I had the opportunity, I was enrolled as a graduate student and I
[730.88 → 733.60] had the opportunity to do some teaching at college level.
[733.88 → 739.78] I had been teaching as a substitute teacher and as a, you know, sort of temporary short
[739.78 → 741.20] term teacher at the university.
[741.46 → 745.70] Whenever somebody was needed to teach a course, I would volunteer because I loved it so much.
[746.38 → 749.28] But then I really got the bug of teaching at college.
[749.28 → 752.74] And I thought, by golly, I really want to do this for the rest of my career.
[752.74 → 755.20] And then I realized, ah, I got to get a PhD.
[755.48 → 757.38] At that point, I hadn't even thought about the PhD.
[757.54 → 763.18] I actually thought I would leave the university after that one year and probably go work for
[763.18 → 766.54] a consulting company because McKinsey at the time had offered me a position.
[766.70 → 767.98] And I thought, oh, that sounds great.
[768.10 → 771.84] You know, I can pretend I'm very smart and give presentations and people will do what I
[771.84 → 773.28] say that sort of appealed to me.
[775.42 → 781.66] But instead, I got this teaching bug and I called up my advisor, my former advisor in Holland
[781.66 → 784.14] and said, where can I go get a PhD?
[784.32 → 786.82] And he said, well, come back to Holland, which is not what I wanted.
[787.40 → 792.68] And the second thing he said is connect with my old friend, Gene Golub, who's a huge, huge
[792.68 → 796.10] name in computational mathematics at Stanford University.
[796.44 → 798.40] And I thought to myself, oh, where's Stanford?
[798.74 → 801.32] You know, I heard, sort of heard of it, but not that much.
[802.10 → 807.06] And then I applied to Stanford and got in, and I just accepted as soon as I got into, okay,
[807.10 → 807.74] that's where I'm going.
[807.74 → 809.02] And then I looked up where it was.
[809.10 → 811.76] I wasn't quite sure if it was in Los Angeles or San Francisco.
[813.50 → 818.02] And then when I got to Stanford, I realized, oh my goodness, we have this expression in
[818.02 → 822.84] Holland that you fall with your bum in the butter, meaning that you're just unbelievably
[822.84 → 823.32] lucky.
[823.90 → 827.54] You know, I realized as I came onto campus, wow, how did that happen?
[828.08 → 831.92] So I think that was very, very lucky to have that in my life.
[831.92 → 837.80] And then I started with my PhD at Stanford and that set me up for the rest of my career.
[838.26 → 838.86] That's fantastic.
[839.26 → 843.94] I'm just curious, when you were in Colorado and you had not prior to that moment thought
[843.94 → 847.30] about the PhD at all, how old were you at that point?
[847.48 → 848.72] I was a little bit older.
[848.82 → 850.78] I was 24 when I left.
[851.02 → 854.98] At that time, we did not have a bachelor's and master's in the Netherlands.
[854.98 → 858.32] We only had sort of the equivalent of a master's degree.
[858.98 → 861.96] And that was an engineer's degree at this university.
[862.62 → 864.06] And so that would be four years.
[864.20 → 866.44] But I stopped studying a couple of times.
[866.56 → 872.30] So I spent one year at sort of student organization running that student organization
[872.30 → 873.56] with seven other students.
[873.78 → 876.48] And that took a whole year out of my study to do that.
[876.96 → 882.04] And then I spent a year, six months on an internship with the company because I wanted to learn
[882.04 → 882.78] how to code.
[883.38 → 887.46] And I thought, I'll just go work for a company for a while and I will learn by doing.
[888.16 → 893.62] And then I spent a half a year running the sports federation, the student sport federation
[893.62 → 897.64] at Delft University because they were going through a difficult period.
[897.64 → 899.62] And I thought I could maybe help out there.
[899.66 → 901.04] And I was really into sports.
[901.18 → 901.98] I still am.
[902.46 → 903.70] So I took two years out.
[904.34 → 906.04] And so it took me six years to finish.
[906.04 → 907.48] And I left at 24.
[907.86 → 910.54] And I've always been happy about that too.
[910.54 → 913.06] I think it gave me a different perspective.
[913.28 → 915.46] Also spending some time away from university.
[915.60 → 920.96] So I was absolutely not this ballistic student, you know, that would come in and just work,
[921.04 → 924.66] work, work and go from bachelor's directly to master's and PhD.
[925.06 → 926.96] I stepped back, and I was a little bit older.
[927.60 → 933.92] It was difficult to immigrate, you know, by myself and to leave my whole family, very large
[933.92 → 935.22] family, leave them behind.
[935.22 → 938.52] But I learned from that too in that one year in Colorado.
[938.52 → 939.86] And I think that helped me.
[940.52 → 943.04] But yeah, no, I had never thought of doing a PhD.
[943.24 → 943.42] Never.
[943.54 → 946.78] I always thought that was maybe not so attractive.
[947.18 → 949.34] I wanted to do something that was practical.
[949.34 → 950.70] I wanted to make a difference.
[951.36 → 957.88] And I thought a PhD and I still think a PhD can at times be a little bit of a it's an act
[957.88 → 959.20] of learning a PhD.
[959.20 → 964.80] So you're very self-involved, you know, during your PhD and many people have a time in the
[964.80 → 966.62] PhD where we think, are we not contributing?
[967.04 → 970.68] And I certainly had that also, but I was teaching along the way.
[971.24 → 974.92] And to me, the PhD at that time and research was a ways to an end.
[975.08 → 978.28] I wanted to be a college instructor.
[978.98 → 980.34] And that's why I got the PhD.
[980.34 → 983.76] And then through the PhD, I developed a love of research.
[983.76 → 1002.22] This episode is brought to you by our friends at Rutter stack.
[1002.42 → 1005.92] And we're calling all data engineers to check out Rutter stack Cloud and start building smart
[1005.92 → 1006.94] customer data pipelines.
[1007.44 → 1010.34] Rutter stack is warehouse first, no more silos.
[1010.80 → 1013.40] Rutter stack builds your customer data lake on your data warehouse.
[1013.40 → 1014.14] Not theirs.
[1014.40 → 1019.52] Enabling all functionality of a CDP with more security and retaining full ownership of your
[1019.52 → 1019.84] data.
[1020.14 → 1022.62] It's open source and API first.
[1022.92 → 1026.38] Rutter stack can be easily integrated into your existing development processes.
[1026.92 → 1029.68] And because they're open source, you can see all their code.
[1029.90 → 1032.32] So you don't have to worry about vendor lock-in or black boxes.
[1032.86 → 1034.44] And best of all, they have transparent pricing.
[1034.64 → 1036.88] Stop paying your CDP a premium to store your data.
[1037.34 → 1042.24] Rutter stack is free up to 500,000 events and pricing scales transparently from there.
[1042.24 → 1044.70] Learn more and get started at Rutterstack.com.
[1044.96 → 1047.24] Again, Rutterstack.com.
[1047.40 → 1050.94] That's R-U-D-D-E-R-S-T-A-C-K.com.
[1050.94 → 1063.12] So you've arrived at Stanford.
[1063.12 → 1064.88] You're into your PhD program.
[1064.88 → 1065.70] You're learning.
[1066.00 → 1071.62] You're going through the same thought process that many other PhD students engage in, in
[1071.62 → 1073.12] terms of learning versus contributing.
[1073.12 → 1077.64] And, you know, that period at Stanford, as you're growing from there into your career,
[1077.64 → 1082.60] and you're kind of moving toward the thing that brought us into the podcast today, which
[1082.60 → 1084.30] is women in data science.
[1084.30 → 1089.62] And there had to have been some formative, you know, events and thoughts and experiences
[1089.62 → 1091.14] that kind of led toward that.
[1091.28 → 1097.14] I'm kind of curious about what your personal experiences were that ultimately led to this
[1097.14 → 1099.06] thing that we're about to talk about afterwards.
[1099.06 → 1105.48] Yeah, if you're asking me for one thing that ultimately led to this, it was frustration.
[1106.18 → 1106.82] That was it.
[1107.12 → 1114.12] Almost 40 years ago when I was 15 and at high school, I chose to go into the STEM direction,
[1114.46 → 1114.62] right?
[1114.66 → 1116.26] So I did physics and I did math.
[1116.82 → 1123.20] And from that moment on, I'd always been one of the very few or the only girl or woman
[1123.20 → 1124.86] in a male-dominated environment.
[1125.08 → 1126.14] I've always had that.
[1126.14 → 1128.48] And the student organization was the same.
[1128.62 → 1134.28] Delft University at that time had a very, very low percentage of girls or female students.
[1134.62 → 1138.86] I was always, you know, every job that I've had, I've been the first and the only woman.
[1139.12 → 1143.52] So I've been in this male-dominated environment, and I've always managed to do quite well.
[1143.76 → 1144.64] I've liked it.
[1144.74 → 1146.82] You know, I've always gotten along with my colleagues.
[1146.96 → 1149.96] At least I hope if they listen, they agree with me.
[1150.74 → 1152.04] But I felt at home.
[1152.32 → 1154.30] But I also had some shitty moments.
[1154.30 → 1155.86] It's okay to use that word.
[1155.86 → 1156.24] You can say s***.
[1156.34 → 1156.74] It's okay.
[1157.24 → 1157.40] Yeah.
[1157.48 → 1158.52] So really s***y moments.
[1158.64 → 1161.28] So I have experienced everything that women talk about.
[1161.92 → 1165.84] Harassment, bias, misogyny, you know, all those things.
[1165.94 → 1166.44] They happen.
[1166.78 → 1167.92] So it's a mixed bag.
[1168.44 → 1172.22] And I've always thought that the positives balance the negatives.
[1172.40 → 1174.26] Don't outweigh probably, but balance.
[1174.36 → 1177.50] And in the meantime, I was working on stuff I really love.
[1177.50 → 1186.26] But it pains me that so many girls and women in the field really do struggle.
[1186.94 → 1189.88] And there are two things primarily that pains me.
[1189.96 → 1192.42] It pains me that women are often not treated well.
[1192.60 → 1194.16] That is one thing that we can talk about.
[1194.28 → 1200.24] I mean, being harassed, and I've experienced every form of that, is a horrible thing to happen.
[1200.48 → 1200.66] Right?
[1200.66 → 1203.78] And so it takes courage to go through.
[1203.94 → 1206.18] And I feel for everybody that goes through that.
[1206.34 → 1208.20] Men as well who are in that situation.
[1208.32 → 1208.80] Everybody.
[1209.02 → 1209.76] Whatever gender.
[1210.06 → 1211.24] We're not just talking about women.
[1211.36 → 1211.92] They're men, right?
[1211.96 → 1212.70] There are other genders.
[1212.86 → 1214.16] And they are really hurt by that.
[1214.48 → 1220.90] And the other thing that really pains me is that there are so many talented girls and women
[1220.90 → 1224.38] who dream of making contribution in the STEM space,
[1224.54 → 1227.76] who somehow feel they don't have what it takes.
[1227.76 → 1231.38] And when I was growing up, I heard that.
[1231.50 → 1232.52] You're a girl.
[1233.14 → 1235.70] You're not supposed to be as good.
[1235.78 → 1237.44] My brother was perfect in STEM.
[1237.60 → 1239.66] I was also very good in STEM.
[1239.86 → 1241.58] They were surprised when I was good.
[1241.66 → 1243.44] They were not surprised my brother was good.
[1243.54 → 1245.30] You know, how silly is that?
[1245.36 → 1245.50] Right?
[1245.54 → 1247.76] Teachers saying, oh, wow, you're just as good.
[1247.88 → 1251.50] Or in some ways, some areas maybe even better than my brother.
[1251.58 → 1252.92] They just couldn't get their head around.
[1252.92 → 1258.48] And it pains me because there's no reason for girls to feel that way.
[1258.78 → 1264.50] And when I had a son, when he went through elementary school, I saw that already happening there.
[1264.98 → 1265.46] Right?
[1265.50 → 1269.02] In elementary schools, there were girls saying, I just can't do math.
[1269.26 → 1272.80] Or there were female teachers saying, oh, we have to do math now.
[1272.88 → 1275.00] But later on, we'll do something fun again.
[1275.74 → 1277.20] That hurts, right?
[1277.20 → 1286.72] And so I've always felt that as one of the few women in computational mathematics, I had to try to change this.
[1287.14 → 1289.44] And I had to try to support women.
[1289.72 → 1295.02] And first, debunk the myth that still persists to this day.
[1295.12 → 1295.80] And there are two.
[1296.20 → 1303.24] One myth is that you have to have an extremely strong innate ability to do well in STEM.
[1303.58 → 1304.84] Particularly computing.
[1305.26 → 1306.36] Particularly mathematics.
[1306.36 → 1310.06] And of course, that comes in as a double whammy, right?
[1310.14 → 1311.98] Math and computing and data science.
[1312.36 → 1313.80] And that's been debunked as well.
[1314.02 → 1314.92] You don't have...
[1314.92 → 1315.42] It helps.
[1315.46 → 1317.86] Of course, it helps when you have a really strong innate ability.
[1318.00 → 1320.12] Like it helps if you're a natural good runner.
[1320.34 → 1326.40] But it doesn't mean that if you're not a naturally good runner, you can still become a pretty good damn runner.
[1326.54 → 1326.72] Sure.
[1326.84 → 1328.04] If you just train, right?
[1328.10 → 1329.80] And it's the same with data science.
[1329.80 → 1338.04] And the second myth is that women or girls simply do not have as much of this innate ability as men or boys.
[1338.04 → 1339.88] And that has also been debunked.
[1339.96 → 1344.52] But it is still so common that people think this.
[1344.52 → 1347.04] I really worry about that with my own eight-year-old daughter.
[1347.30 → 1349.68] She loves science and likes math.
[1349.82 → 1359.96] But I feel like we're having to push against, you know, even today in 2021, it feels like we're still fighting that same battle that you did for all those years.
[1360.18 → 1361.46] Maybe not as much.
[1361.68 → 1362.54] Maybe it's getting better.
[1362.76 → 1363.66] But I'm seeing that.
[1363.66 → 1365.78] I'm not sure if it's getting better.
[1365.98 → 1366.84] Oh, okay.
[1366.84 → 1372.84] I think these myths have this unbelievable stubborn nature about them.
[1373.54 → 1378.50] And of course, because this gets perpetuated in industry and so on.
[1378.66 → 1387.00] So when I was a student at high school and also in college, I heard time and time again, people say, ah, it's getting better.
[1387.12 → 1389.36] You know, the pipeline is growing.
[1389.50 → 1392.04] There are more girls coming into these fields.
[1392.04 → 1395.98] So eventually, you know, naturally this will all progress.
[1396.50 → 1397.16] And you know what?
[1397.22 → 1397.92] It doesn't.
[1398.04 → 1412.26] If you are below a certain threshold, and that's maybe 25, 30 percent, that's been my experience, and you're seen as different, it is exceedingly hard for that to change naturally or organically.
[1412.58 → 1416.26] Change happens when people are no longer seen as different.
[1416.26 → 1426.28] When people, women doing STEM, you know, the same with people from different colours, different races doing STEM, when that's normalized.
[1426.92 → 1429.66] And that is what we're working on with women in data science.
[1429.74 → 1435.30] You know, we're trying to normalize this, that it's totally natural to have a woman tell you about AI.
[1435.84 → 1436.26] Why not?
[1436.26 → 1436.94] Of course.
[1437.08 → 1440.02] It's interesting when you say you think it's perpetuating.
[1440.02 → 1446.98] I've really noticed it the last few years without diving into politics with the division that's associated with that.
[1446.98 → 1458.14] I know for me, having grown up in a family full of strong women and having had a career where I worked with people all over the world, both genders of every race, and it's all normal.
[1458.74 → 1468.86] And yet, I think when times get tough, people revert to these rather base instincts at times in terms of how they're seeing others and how they're identifying and that identity.
[1468.86 → 1471.52] I worry about where that's taking us still at this point.
[1471.82 → 1477.70] When you were saying that this is perpetuating these myths, I suppose I'm not surprised when I look at it in the big picture that way.
[1477.96 → 1478.86] How do we get out of that?
[1479.04 → 1482.00] How do we tear these myths down and make it a level playing field?
[1482.34 → 1485.10] There's a bunch of different things that we can do.
[1485.58 → 1487.44] I'm going to give you a long answer here.
[1487.58 → 1488.30] Okay, that's fine.
[1488.30 → 1500.08] The first thing is that we have to help normalize that women can be productive in these fields and are productive and that there are outstanding women already doing outstanding work.
[1500.18 → 1502.24] So we have to promote those women.
[1502.34 → 1506.18] We have to make sure that they're being heard, that they're on stage.
[1506.18 → 1523.88] And so the reason why WITS in particular started, Women in Data Science, with a conference in 2015 was really because I was invited at some point at the university to give a talk at a data science conference organized by some of my colleagues at Stanford.
[1524.72 → 1526.56] And I couldn't make it that day.
[1526.82 → 1531.10] And so later, you know, I saw the announcement, and it was just all male speakers.
[1531.28 → 1533.64] And that was the umpteenth conference at the time.
[1534.16 → 1535.54] You know, it's changed a little bit now.
[1535.54 → 1536.46] At least we're aware.
[1536.58 → 1543.08] But at the time, it was very, very common to have conferences with keynote speakers, only male and all male panels and so on.
[1543.48 → 1547.60] Even when they talked about diversity, which still be male talking about diversity.
[1548.10 → 1554.40] And I ran into one of the organizers on a nice sunny morning and I asked him, so what happened?
[1554.64 → 1557.54] And he said, but Margot, you know, we asked you and you couldn't make it.
[1557.84 → 1558.86] And I'm perplexed.
[1558.90 → 1562.32] And I said, well, how about all these other women that could talk?
[1562.32 → 1568.32] And he says, well, Margot, you know, we really tried very hard to find women, but we just couldn't find any.
[1568.66 → 1569.76] And I thought, OK, that's it.
[1569.96 → 1579.58] I was just on my way to have a cup of coffee with my friend Karen Mathis, who was working for me and with me at the time in computational mathematics, the institute that I was running on campus.
[1579.58 → 1586.72] And a former student and mentee of mine who is now at Facebook, a man, incredibly bright and supportive.
[1586.92 → 1587.98] And I said, look, this is it.
[1588.08 → 1593.72] You know, we have to make sure that that can never happen again, that people cannot say, just can't find any women.
[1594.38 → 1597.00] And I knew so many outstanding women in this field.
[1597.08 → 1597.96] I want to showcase them.
[1598.04 → 1599.12] I want to put them on the stage.
[1599.22 → 1604.04] So let's just organize a conference where it just so happens that all the speakers are women.
[1604.04 → 1605.40] I thought, let's turn it around.
[1605.52 → 1607.48] That wasn't happening much at the time.
[1608.04 → 1615.94] And most of the gatherings also that we had as women in the field was to talk about what we could possibly do to make the field better for us.
[1616.02 → 1626.20] But I said, no, technical talks, you know, just showcasing outstanding women doing outstanding technical work and normalize this and make sure that these videos are online.
[1626.20 → 1633.52] And we'll do that over and over again so that now when you, you know, after a few years, when you go online, you find a lot of this.
[1634.10 → 1639.14] And that's good for the women because they see role models, but it's also equally good for the men.
[1639.44 → 1654.20] And it's good for any gender and perfect for the men also because they see women totally capable of doing fantastic work and moving the needle and being just as creative and outstanding as any of the men that they know.
[1654.20 → 1656.06] And so that's what we did.
[1656.16 → 1658.48] And of course, then if people say, but why only women?
[1658.60 → 1661.34] I sometimes joke, say, well, we asked Joe, but he couldn't make it.
[1661.58 → 1664.72] And we really tried to look for other women, but we just couldn't find any.
[1665.72 → 1670.54] But I think this is one way is to really promote women to put them on the stage.
[1670.86 → 1672.60] And there's so many already.
[1672.90 → 1673.04] Right.
[1673.04 → 1684.52] And one of the reasons why there's so many is because the 15 or maybe 20 percent of this AI and data science workforce is female, or they identify as females.
[1684.52 → 1688.18] And they've had to overcome a lot to get there.
[1688.30 → 1692.44] So they are often, you know, incredibly accomplished women.
[1692.66 → 1692.78] Right.
[1692.82 → 1693.66] They're still there.
[1693.80 → 1696.18] So there are many, many and everywhere in the world.
[1696.18 → 1704.18] So now with WITS, we hit a nerve, and we're now a global organization, and we have over 200 conferences around the world every year.
[1704.26 → 1710.08] And this podcast series and the Marathon to help the high school students also come in and outreach program.
[1710.08 → 1713.20] And now also an educational program with WITS workshops.
[1713.20 → 1714.52] So that's in five years.
[1715.12 → 1719.84] And the reason why we could expand so quickly is that we hit a nerve.
[1719.84 → 1724.28] And this is happening now in many other fantastic organizations.
[1724.28 → 1725.44] There are women in AI.
[1725.62 → 1727.04] There are women in machine learning.
[1727.62 → 1731.44] There are so many fantastic organizations around the world that are doing the same.
[1731.54 → 1735.28] And then I haven't even talked about girls who code or pie ladies or are ladies.
[1735.40 → 1735.50] Right.
[1735.50 → 1736.86] So there's a lot of that happening.
[1737.22 → 1739.72] And the energy in this is wonderful.
[1739.88 → 1747.52] So there's one thing that we can do, of course, with support from everybody, you know, and is to make sure that people see them.
[1747.60 → 1748.68] So we normalize this.
[1748.68 → 1749.42] So that's one.
[1749.42 → 1752.82] The other thing is, of course, that we have to try to change the culture.
[1752.98 → 1760.08] We have to get to 25, 30 percent so that women are no longer in a team or in a company seen as different.
[1760.58 → 1769.10] There is a psychological barrier around 25 or 30 percent where the people in the minority no longer really see themselves as minority.
[1769.10 → 1769.92] And that helps.
[1770.46 → 1775.60] And the people in the majority no longer see the minority as just the minority and different.
[1775.78 → 1778.70] And when you're seen as different, you're not really included.
[1778.70 → 1782.16] And it's very, very hard for you to really get a voice.
[1782.16 → 1787.42] Now, to get to the 25 and 30 percent, it has been a struggle for 40 years.
[1787.42 → 1793.00] And sometimes you hear people say, like, for example, Sheryl Sandberg, you have to lean in as women.
[1793.16 → 1797.70] You've got to go in an organization and conform with my free interpretation.
[1798.28 → 1802.78] And then when you get to a leadership position, you can then change the culture from within.
[1802.78 → 1805.24] Well, I've heard that. I heard that when I was 15.
[1805.72 → 1809.14] I hear that now when I'm 55, you know, and nothing has happened.
[1809.24 → 1812.16] Right. If that worked, it should have happened a long time ago.
[1812.60 → 1821.18] I always think that a culture change needs to really be spearheaded and supported by the majority.
[1821.52 → 1824.78] It doesn't have to be the task of the minority.
[1824.78 → 1826.06] It shouldn't be. Right.
[1826.14 → 1836.00] Just like with Black Lives Matter, a lot of our black colleagues are saying, don't ask us to change your culture so that it becomes more inclusive for us.
[1836.22 → 1839.98] That is, I think, the duty and the responsibility of the majority.
[1840.16 → 1842.66] And of course, we can help as minority and we will.
[1843.18 → 1846.12] But we cannot be the one being asked to guide this.
[1846.12 → 1848.72] And so there needs to be sensitivity.
[1849.16 → 1853.04] And I've always thought that it is a total no-brainer.
[1853.36 → 1874.84] You know if you truly believe that this other gender or the other genders have just as much talent as you and you are not hiring them, and you're not ensuring in your culture that they thrive, that they get promoted, that they do really well, there's something wrong.
[1874.84 → 1887.34] Right. So either you don't really believe that they have this capability, or you're finding it just difficult, and you're not well-trained to work with people who are not like you.
[1887.80 → 1896.34] And I think that is what we see a lot of, you know, and it's a natural tendency for groups that are very homogenous.
[1896.34 → 1903.38] You know, say a group of males in the tech company to hire a like person.
[1903.38 → 1907.12] Now, you hire somebody who's like you, that's easier.
[1907.60 → 1917.30] So if you're a team lead, and you've just been promoted, you've been a technologist, you've been a computer scientist, a fantastic computer scientist say for a while you're now promoted to team leader.
[1917.46 → 1921.26] You have to hire, you have to support your team members.
[1921.34 → 1923.96] You've never really been trained to be a team leader.
[1923.96 → 1933.72] It is actually quite a courageous and difficult thing to hire somebody not like you and to invite diversity into a team.
[1933.96 → 1937.48] It's much easier and much less troublesome.
[1937.74 → 1944.00] And maybe there's not as many, many little conflicts or little tensions you have to deal with if you just hire somebody like you.
[1944.00 → 1947.60] And so we see that so much in the industry.
[1947.80 → 1958.60] We see this also at university that the metrics used to measure quality and to measure potential are metrics of the majority group.
[1958.98 → 1964.26] And they are used then to hire people just like themselves because, of course, those people meet those metrics.
[1964.82 → 1968.50] And then when you say something about it, you say, yeah, but we have to hire the best.
[1968.90 → 1971.04] Well, according to what metric, right?
[1971.04 → 1977.28] So it's this like, hire is like that I think is really the deepest problem we have.
[1977.94 → 1983.12] And that can only be changed by companies saying, wait a second, we're doing something really silly.
[1983.46 → 1987.28] We're not including all this other talent.
[1988.20 → 1994.92] And the other thing that can happen when you have these homogenous teams is you get these echo chambers, right?
[1994.92 → 2004.60] And so very often I hear male colleagues who are in a male team and feel totally comfortable with this ask, but why do we really have to do this?
[2005.36 → 2006.56] You know why would it make us better?
[2006.64 → 2007.40] We're great.
[2007.60 → 2010.74] I said, yeah, in your echo chamber, of course, you're fantastic.
[2011.02 → 2012.38] Everybody thinks like you.
[2012.86 → 2015.96] They admire the same sort of skills that you do.
[2015.96 → 2030.06] Of course, you're feeling great, but you can really surpass this even more if you challenge yourself a bit more by including different thinkers who challenge you and your way of thinking and your way of doing.
[2030.32 → 2032.08] And then together you can actually become better.
[2032.08 → 2051.68] So I always thought as a tech leader, you should see this and see, hey, if we become more diverse and that's diverse in any which way, that is diverse in getting the introverted people a voice, diverse in getting the women in, getting all genders in, getting different races in, you will actually ultimately get much better.
[2052.04 → 2053.94] But it takes courage to do this.
[2054.06 → 2056.02] And the first step is one of discomfort.
[2056.02 → 2065.76] And I think it's that discomfort that is maybe natural, but we should really not accept that keeps this from happening.
[2066.02 → 2067.46] That was a long answer, wasn't it?
[2067.56 → 2068.52] It was a good answer.
[2068.52 → 2086.56] We deserve a better internet and the Brave team has the recipe for bringing it to us.
[2086.70 → 2087.70] Start with Google Chrome.
[2087.94 → 2091.66] Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[2091.86 → 2092.72] Rip out the Google bits.
[2092.84 → 2093.50] We don't need them.
[2093.86 → 2096.36] Mix in ad and tracker blocking by default.
[2096.36 → 2099.36] Quick access to the Tor network for true private browsing.
[2099.72 → 2104.04] And an opt-in reward system so you can get paid to view privacy-respecting ads.
[2104.26 → 2108.00] Then turn around and use those rewards to support your favourite web creators like us.
[2108.32 → 2112.94] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[2122.94 → 2126.20] Okay, so I loved that last answer.
[2126.36 → 2140.32] Because it points out that people who look like me, white men who are in data science, have a responsibility to not do the thing that just feels natural and feels comfortable to them.
[2140.50 → 2143.26] Because you're introducing bias into your own team.
[2143.34 → 2144.60] You are creating your own bubble.
[2144.80 → 2145.08] Yeah.
[2145.44 → 2148.16] A bubble that will not serve you or your organization.
[2148.38 → 2150.94] You are hurting yourself by doing that.
[2150.94 → 2152.12] I really think so.
[2152.20 → 2154.60] The problem is that not everybody sees it that way.
[2154.72 → 2156.08] They say, I'm not hurting myself.
[2156.20 → 2157.04] I'm doing great.
[2157.34 → 2158.96] We're doing groundbreaking work.
[2159.10 → 2160.90] You know, and they feel defensive about this.
[2161.00 → 2162.48] And I can understand that.
[2162.52 → 2164.60] I've been in those teams a long time.
[2164.76 → 2168.14] And here, I've always been the odd one out.
[2168.26 → 2171.18] Talking about, you know, sometimes being uncomfortable.
[2171.88 → 2175.34] I know what it takes to work with people who are not like you.
[2175.38 → 2177.00] Because I've done it my whole life.
[2177.00 → 2179.70] And I've always been seen as a little different.
[2180.32 → 2182.32] So it does take something.
[2182.56 → 2185.44] And you have to trust yourself that you're going to be okay.
[2186.10 → 2193.92] But I think in general, you know, good leaders and good managers of teams see that they're missing out.
[2194.46 → 2196.26] And there are perfect ones too.
[2196.52 → 2200.20] I don't want the audience to feel that I'm just bashing everybody.
[2200.20 → 2203.12] Because there are fantastic people who really see this.
[2203.12 → 2206.70] And for a company, it really needs to also come from the top.
[2206.98 → 2210.10] The top also needs to say, we're missing out on talent.
[2210.36 → 2213.20] We're missing out on the next big ideas.
[2213.42 → 2218.42] If we don't tap into all of that talent that's out there that we're ignoring.
[2219.08 → 2222.00] You know, some people think that that's not the case.
[2222.02 → 2222.84] But we are.
[2223.12 → 2227.34] And we're losing fantastic girls and women.
[2227.70 → 2229.38] You know, like you talked about your daughter.
[2229.38 → 2235.48] I see girls being lost already in middle school or elementary school to this field.
[2236.04 → 2241.28] Because of bias and these myths that I talked about earlier.
[2241.58 → 2245.86] And these ideas that math and computing is not for them.
[2246.20 → 2247.62] And it's super sad.
[2247.62 → 2249.24] Let me ask you a question.
[2249.40 → 2259.50] In terms of, you know, we've just kind of put out this challenge, if you will, to certainly the people in power, the white males in data science and other industries as well.
[2259.94 → 2268.38] Is the right metric that your organization at any level or any scale should reflect the general population in its diversity?
[2268.60 → 2269.84] Is that the right one?
[2269.90 → 2271.14] Or is there a better one?
[2271.32 → 2273.26] In other words, it may not be a team.
[2273.32 → 2274.16] Maybe it's just interest.
[2274.16 → 2278.04] Maybe it's kidding in school with an interest in various topics.
[2278.76 → 2283.54] Should those topics, to say that there's no bias in them, should they reflect that general population?
[2283.66 → 2286.10] Or have you found a better metric to try to aspire to?
[2286.46 → 2289.98] I think that's a very nice idealistic metric.
[2291.26 → 2293.18] And we'll probably never see it.
[2293.28 → 2293.48] Okay.
[2293.76 → 2294.70] Well, set me straight.
[2294.82 → 2297.30] Give me a good one that is a good functional one.
[2297.44 → 2301.54] Just like our listeners, I'm going to take this and use it after this conversation.
[2301.78 → 2303.18] So what is it that I should use?
[2303.18 → 2331.54] Well, the one thing that I use for now is that the metric should be that nobody from whatever background they have, whatever race or gender they have, who really wants to be part of this and wants to learn and grow in this field, feels that they cannot because they're not welcome.
[2331.54 → 2341.20] And so what you look at is not just how many people are being hired, but also how many people leave.
[2341.48 → 2343.76] So you look at things like attrition, right?
[2343.76 → 2347.44] Really, really, really important to think.
[2347.68 → 2350.88] If I had a company and I would look at this and said, who's leaving?
[2351.04 → 2352.04] Who's not coming in?
[2352.34 → 2352.98] Who is leaving?
[2353.62 → 2359.46] I think when you think about the representation of the general population, I use that too.
[2359.46 → 2373.30] But in another way is that if you look at an organization, and you see certain subpopulations, like say the white males or Asian males or whatever it is, totally dominate.
[2373.92 → 2378.84] That should make you think, say, hey, this doesn't reflect the world that I see around me.
[2379.20 → 2380.14] Something is wrong.
[2380.14 → 2384.20] Sometimes it is wrong, the pipeline, right?
[2384.26 → 2389.98] And that's the excuse that a lot of people give and say, well, we want to hire, but there's just not many people applying.
[2390.14 → 2393.48] So you start thinking, am I inviting the people in the right way?
[2393.54 → 2406.52] So there's a lot of work going on about this, that in recruitment, and I've seen this firsthand also at Stanford, recruiters are not always so great, you know, when it comes to really being inclusive in the way that they recruit.
[2406.52 → 2410.56] So you start thinking about this, can I actually invite people in?
[2410.90 → 2414.86] Then you start thinking about maybe as a company, I can help improve that pipeline.
[2414.96 → 2416.24] And there are so many ways, right?
[2416.26 → 2417.64] And you can do this through internships.
[2417.64 → 2422.04] You can do this through helping with outreach and helping in the community.
[2422.36 → 2424.70] And so there are so many ways to do that.
[2424.70 → 2453.56] But the main thing, I think, is that it's really important for us to go back to debunking those myths and really collectively as an industry, as this area of research of data science, I really go to young kids, because this starts really early on, and make sure that they are getting through elementary, middle, and high school without feeling that they don't belong, right?
[2453.56 → 2456.58] And that is, I think, what we have to do.
[2457.06 → 2460.02] And people have talked about this for a very long time.
[2460.28 → 2462.16] You know, we really want to shift this.
[2462.26 → 2464.20] We really want to make this more inclusive.
[2464.20 → 2478.86] We have to be thinking about this and make sure that we have the right educational approaches and the right way of testing and judging people, which happens in education that is not biased in itself.
[2478.96 → 2481.40] And unfortunately, that is the case right now.
[2481.64 → 2483.48] That's why these myths are perpetuating.
[2483.56 → 2486.08] You do this also by creating an awareness.
[2486.08 → 2504.66] I may sound like I'm sort of scrambling back a little bit, but the thing is, that ideal of having this really, really critical area in our society, data science, data-driven decision-making, that is really impacting so many areas of our daily lives.
[2504.66 → 2506.66] To have a representation of the population.
[2506.66 → 2510.52] That is, of course, that is, of course, the end goal.
[2510.60 → 2519.94] But we're so far off because we're still facing these problems, these really deep-lying problems at the very early level.
[2519.94 → 2530.58] And so instead of thinking about companies, what we really need to think about is, are we setting everybody up for success?
[2531.54 → 2534.98] Are we closing doors way too early for people?
[2535.26 → 2536.08] So it's too late.
[2536.08 → 2539.44] By the time they get to the company, we've done the damage, right?
[2539.66 → 2541.56] There's way too little too late.
[2541.82 → 2541.96] Yeah.
[2542.04 → 2545.94] I mean, the mental problem sits at the education.
[2546.40 → 2559.00] And not just for women in STEM, but it's the same with first-generation, low-income students, students of colour who don't have the same sort of privileges and opportunities as others.
[2559.00 → 2561.90] Because there is no equity in education.
[2562.50 → 2564.18] And that is where we have to start.
[2565.26 → 2570.64] Now, of course, then, you know, people say, well, I'm not saying we shouldn't do anything at the industry level.
[2571.12 → 2580.38] Post-education, of course, we have to do everything that we can by hiring and promoting and ensuring people thrive and don't leave for the wrong reasons.
[2580.88 → 2583.74] But our biggest task, I think, is on the education side.
[2583.74 → 2584.22] Okay.
[2584.82 → 2594.42] We're kind of winding up toward the end, but I'd like to hear what some of the activities that WIDE is doing that is giving these opportunities.
[2594.42 → 2608.24] And recognizing that by the time they get there, they've already been through this series of potential, you know, derailments, you know, in terms of elementary school girls, my daughter's age, as they move into being young ladies.
[2608.42 → 2611.14] They've already had to navigate a whole series of barriers.
[2611.14 → 2628.78] But there's sort of this kind of last chance to correct that with WIDE in terms of these opportunities and getting these women who are brilliant and smart and skilled and have something to tell the rest of us to make sure that we understand their value.
[2629.08 → 2639.14] What are some of those activities that WIDE is doing around the world that is enabling that process so that maybe we can have a better shot of correcting this as they move through their careers?
[2639.14 → 2639.78] Yeah.
[2639.88 → 2642.70] At WIDE, we always say we try to do three things.
[2642.82 → 2649.98] We try to inspire through role models, mostly, you know, showcasing these outstanding women doing outstanding work everywhere.
[2650.32 → 2653.12] We try to support, and we try to educate everybody.
[2653.42 → 2653.50] Right.
[2653.96 → 2658.50] And the support comes through the networks, the local networks that the WIDE communities are creating.
[2658.64 → 2665.14] So we have over 600 ambassadors around the world that are setting up their own WIDE events and their WIDE communities.
[2665.14 → 2667.98] And the support is unbelievably important.
[2668.16 → 2673.62] You know, we hear this all the time that women come out of the woodworks and say, oh, my goodness, I'm not the only one.
[2673.74 → 2673.84] Right.
[2673.84 → 2679.18] There are so many other fantastic women that I can be with, and I don't feel different.
[2679.30 → 2681.04] I feel inspired by them.
[2681.48 → 2682.08] So that's great.
[2682.08 → 2694.38] Now, in terms of education, one of our most important programs, I think, is educational outreach where we're going to high school and middle schools and talk about girls there, about what data science really is.
[2694.48 → 2703.18] Because I think also at that time when girls are making the choice of, hey, I can't do this, they have a very poor understanding of what it really means.
[2703.18 → 2712.90] And so we have found that showing a day in the life, for example, of a data scientist who happens to be a woman really helps and girls say, oh, wow, I didn't know this.
[2713.40 → 2721.96] Showing that data science is an unbelievably interdisciplinary field, right, where people from every area of interest really need to participate.
[2722.24 → 2728.06] Everybody really needs to be data savvy nowadays anyway, because data science is penetrating everything.
[2728.06 → 2734.00] But we need the humanists, and we need the lawyers, and we need the economists, and we need, you know, we need everybody around the table.
[2734.00 → 2756.16] And so also showing that and showcasing women that, for example, studied philosophy and are now data science leads to show these girls that to become and to partake in this amazing field, you don't have to be the unfortunate stereotypical nerd, right?
[2756.16 → 2761.02] So we're trying to take the nerd out of the image of the data scientist.
[2761.68 → 2768.16] And then we have a marathon that we organize every year, and we're working together with Gaggle on this.
[2768.90 → 2777.64] And with that, we really try to also get girls who never in their lives thought about maybe participating in the Gaggle competition.
[2778.16 → 2781.34] It can be a load of fun, but it's mostly boy dominated.
[2782.04 → 2784.82] And girls are often a little bit intimidated by that.
[2784.82 → 2790.54] And to get them that first taste and to get them maybe a little bit hooked on this.
[2791.18 → 2793.98] And we have this marathon that is global.
[2794.40 → 2803.02] And the only restriction we have on this particular competition every year in which is that the team needs to be at least 50% women.
[2803.52 → 2804.76] So some teams are girls.
[2804.90 → 2806.84] Some teams are all girls.
[2807.02 → 2812.10] Some teams are 50-50, which of course would be, you know, that's the end goal that we want, right?
[2812.14 → 2814.24] That we're all participating like that.
[2814.24 → 2819.88] And that has made, I think, a big difference to some of these girls that may be in high school and say,
[2820.00 → 2825.76] Hey, I never dared do this, but now I've done it, and I've done really well in it and I want to do more.
[2825.92 → 2829.40] And we see these girls do more and not be turned off.
[2829.80 → 2831.64] And that is, of course, wonderful, right?
[2831.64 → 2841.42] And that's a great metric for us that we see girls not give up because they have this misconception that they won't do so well.
[2842.16 → 2844.06] But we want to do much more with wits.
[2844.22 → 2854.64] You know, we really want to understand better what we can do also at university level that we have such a leaky pipeline that women come in undergraduate degree programs.
[2854.64 → 2860.64] And some of them are fantastic, like Harvey Mudd had this fantastic change in the computer science program.
[2861.60 → 2864.70] Many, many, many women come in, very high percentage of girls.
[2865.44 → 2868.38] But still, it leaks, right?
[2868.44 → 2870.56] So then you come to graduate school, it's less.
[2870.62 → 2873.32] And we really want to understand more what we can do there.
[2873.32 → 2877.38] As you're thinking about where you're going with this, could you also integrate in?
[2877.64 → 2879.44] You have a bunch of people listening right now.
[2879.68 → 2884.28] And some of those people are going to say, I want to know what we can do.
[2884.32 → 2889.00] And we've talked a little bit about kind of the underlying problem and solving that in the large in society.
[2889.00 → 2895.82] But could you also, as you talk about the things that you're going toward now, how can folks help you?
[2895.82 → 2907.94] Not only bringing young ladies into the program to benefit from it, but, you know, how can organizations that want to see the same vision achieved, how can they help you get where you want to go with these new things?
[2908.20 → 2909.56] Oh, there are so many ways.
[2909.56 → 2923.76] One of the best things that you can do, I think, is for all those parents listening, be very careful and very cognizant of how you in your family, for example, talk about math and STEM.
[2923.76 → 2934.24] And one of the things that I encourage all my friends to do who have kids is that don't let the father always be the one explaining the math to the kids, right?
[2934.46 → 2936.00] So let mom do it.
[2936.34 → 2943.50] And if mom doesn't quite know it, well, tell mom to get educated a little bit, you know, and try it.
[2943.50 → 2944.28] It's not that hard.
[2944.36 → 2945.14] Everybody can.
[2945.56 → 2952.10] I've seen in families where the mom was very hesitant to do this and then also said, I never thought I was any good.
[2952.10 → 2957.18] But let me try to keep up with the kid and practice that works unbelievably well.
[2957.72 → 2961.82] See, girls, when they're young, they really, really listen.
[2962.06 → 2967.90] And research has shown this over and over again to female role models or role models of their own gender.
[2968.12 → 2968.22] Right.
[2968.26 → 2969.14] The same with boys.
[2969.26 → 2970.10] We know this.
[2970.54 → 2972.68] And at a particular age, that's very strong.
[2972.68 → 2981.48] And it's that age also in elementary school, for example, that girls, for example, listen very carefully to what female teachers tell them.
[2981.52 → 2983.94] And most elementary school teachers, of course, are female.
[2984.04 → 2990.64] So if you're listening, and you're a teacher, be very careful about the language that you're using around math in your classroom.
[2990.64 → 2993.60] Don't make comments like, oh, it's OK.
[2993.66 → 2995.54] I was never any good at this either.
[2996.18 → 3000.84] Don't say things like, well, math is hard and English is fun.
[3001.32 → 3006.32] You know, don't say things like, oh, you know, maybe this is just not your thing.
[3006.62 → 3009.30] And we hear those things over and over again.
[3009.30 → 3022.16] And if your teacher and yourself are a little bit insecure about your math ability, and that is one of the reasons why you may not convey as much enthusiasm for it as for other fields, get help, get support.
[3022.62 → 3023.16] Come to us.
[3023.28 → 3024.86] We can set you up with mentors.
[3025.10 → 3029.94] You know, I'd really like to try to change the culture in elementary classrooms.
[3030.06 → 3031.56] I'm not blaming the teachers here.
[3031.64 → 3032.96] It's perfectly logical.
[3032.96 → 3039.82] If you are a teacher who struggles a bit with mathematics, that you're not as excited, and you may not even be aware of it.
[3039.96 → 3041.42] But, you know, think about that.
[3041.78 → 3053.26] If you are a math teacher in high school or middle school, and you see that in advanced math classes here in the United States where students are selected, the percentage of girls is low.
[3053.82 → 3054.66] Question that.
[3054.82 → 3056.04] Don't just accept it.
[3056.04 → 3064.82] When my son was in elementary school, and he went to advanced math class, I came in to give a little spiel on the number pi one day.
[3064.96 → 3067.08] And I noticed there were only five girls in this class.
[3067.50 → 3068.32] They were nine.
[3069.40 → 3074.30] And then when I asked at that point some of the teachers, they said, oh, it's always been like this.
[3074.42 → 3076.20] They weren't even questioning this.
[3076.32 → 3077.52] It was what it always had been.
[3077.62 → 3078.48] It always has been.
[3078.48 → 3090.62] And I said, well, think about then how you're selecting in these advanced math classes and think just very clearly that there is absolutely no reason why advanced math classes in elementary school or middle school or high school.
[3090.70 → 3100.30] By the way, the whole thing about these advanced math classes, I think, is silly because it's so difficult for people who are maybe a little bit of a late bloomer to catch up.
[3100.50 → 3100.60] Right.
[3100.60 → 3106.16] So we're setting people up for failure right at a very young age, which is just terrible.
[3106.46 → 3111.62] But if you have them, please question yourself if you see the percentages are off.
[3111.82 → 3112.88] You know, it's funny.
[3112.98 → 3116.82] You really hit a specific spot with me just now on that.
[3116.82 → 3131.54] And I realized that even though I think of myself as very modern and progressive in this way, that when we are teaching science and math to my daughter, and because of COVID, we've been doing homeschooling as opposed to them being in the class.
[3131.54 → 3137.58] And because I'm the one doing science and math, you know, that's kind of my thing.
[3137.68 → 3141.12] And my wife had grown up doing different things.
[3141.28 → 3151.56] And I have no idea maybe there were points where she, you know, lost a chance to go down a path, which I'm going to ask her about actually after we're done with the conversation.
[3151.56 → 3158.72] But we naturally gravitate toward if it's a science thing, then she'll say, hey, come over here and teach Athena this thing.
[3158.96 → 3160.00] And that's a problem.
[3160.36 → 3164.26] And I had never thought of it, you know, that it's the way that we've always done it.
[3164.26 → 3165.44] And we didn't question that.
[3165.56 → 3171.80] And so I need to have a conversation with my wife, and we need to talk about trying to balance that a little bit.
[3172.00 → 3173.88] And it had never occurred to me.
[3173.98 → 3180.18] And I'm betting that there are people in the audience that would have to, you know, realize that they are guilty of doing the same.
[3180.18 → 3182.04] I mean, that's one of those things you're talking about.
[3182.38 → 3182.52] Yeah.
[3182.64 → 3190.18] And particularly in COVID with all this homeschooling, I've noticed this talking to young girls that they say, oh, yeah, my dad does that.
[3190.18 → 3197.18] You know, I'm not also I don't want people to think that I feel everybody needs to study mathematics, you know, because otherwise you're missing out.
[3197.58 → 3198.96] People have different interests.
[3198.96 → 3214.96] What I'm really saying is that girls, women who really like it and who would like to continue but are not doing it, not because they have no interest, but because they feel they're falling short.
[3215.50 → 3216.50] That is not good.
[3217.10 → 3222.60] You know, so that everybody who has the inclination and the desire, we should set them up for success.
[3222.60 → 3229.36] As a parent, think about what you're doing to help perpetuate these myths that girls are just not as good.
[3229.44 → 3230.28] And talk to your daughters.
[3230.38 → 3231.12] Also ask them.
[3231.60 → 3236.72] I asked my son when he went through school, said, you know, what courses, what classes are your favourite?
[3237.44 → 3242.64] But also what classes do you think, you know, you really like, but you think you may not be as good at?
[3243.04 → 3243.92] And why is that?
[3243.96 → 3244.76] What are you thinking?
[3244.88 → 3245.62] What are you feeling?
[3246.08 → 3247.48] And ask your daughters.
[3247.48 → 3253.18] Ask also when they're in high school, if they're dropping out of a math curriculum.
[3253.58 → 3256.74] And sometimes I'm not surprised because we start with algebra.
[3257.10 → 3257.48] Blimey.
[3257.78 → 3259.48] You know, we should start with something a bit different.
[3260.06 → 3261.42] But ask them why.
[3261.84 → 3266.62] And if you hear just not good enough, question that.
[3267.26 → 3269.18] But you should ask them, but do you like it?
[3269.18 → 3281.20] And if they say yes, help them and make them see that there's no such thing as needing to, you know, as a fixed mindset here.
[3281.30 → 3282.24] That is not helping.
[3282.38 → 3286.68] There's no such thing as the only people that can do this are the ones with strong innate ability.
[3286.86 → 3287.06] Uh-uh.
[3287.36 → 3289.78] The gross mindset is really fantastic on this.
[3289.78 → 3297.74] And give them, for example, a book by Carol Deck on mindset, which is one of my favourite books in the whole world that addresses those things.
[3298.14 → 3300.86] And encourage them to find a female role model.
[3301.28 → 3305.22] And again, if you don't have any of those, connect with us.
[3305.32 → 3311.66] Because we've got thousands of women around the world in this field who could potentially be a role model.
[3311.78 → 3315.38] And we'll probably have somebody in your neighbourhood, right?
[3315.38 → 3317.58] So that's one of the things that we can do.
[3317.70 → 3324.36] And what you can do and all the listeners can do is be alert, question, and don't accept it too readily.
[3324.72 → 3325.00] Okay.
[3325.24 → 3329.92] I hope that listeners have really taken this in and that they will go act on everything.
[3330.46 → 3332.96] This is certainly one of my favourite conversations ever.
[3333.56 → 3336.68] Thank you very, very much for coming on the show.
[3337.02 → 3339.12] I've got a bunch of homework to do myself.
[3339.26 → 3340.22] So thank you so much.
[3340.86 → 3341.80] Thank you, Chris.
[3345.38 → 3347.60] Thank you for listening to Practical AI.
[3347.94 → 3349.94] We appreciate your time and your attention.
[3350.40 → 3354.64] Follow the show on Apple Podcasts, Spotify, or your favourite podcast app.
[3354.96 → 3356.48] Your neural networks will thank you.
[3357.00 → 3360.18] We are also on the web at practicalai.fm.
[3360.46 → 3365.40] There you'll find recommended episodes, listener favourites, and a free sign-up to join the community.
[3366.00 → 3369.42] Practical AI is hosted by Chris Benson and Daniel Whiten ack.
[3369.62 → 3373.16] It's produced by Jared Santo with music by Break master Cylinder.
[3373.16 → 3376.78] Thanks again to our sponsors, Vastly, Linde, and Launch Darkly.
[3376.92 → 3377.74] That's our show.
[3378.14 → 3380.88] We hope you enjoyed it, and we'll talk to you again next week.
[3403.16 → 3404.72] Bye.
[3404.92 → 3405.04] Bye.
[3405.04 → 3406.24] Bye.
[3406.42 → 3406.92] Bye.
[3406.92 → 3406.96] Bye.
[3406.96 → 3407.42] Bye.
[3407.62 → 3408.56] Bye.
[3408.66 → 3408.98] Bye.
[3411.08 → 3411.64] Bye.
[3418.18 → 3418.82] Bye.
[3418.82 → 3420.88] Bye.
[3420.98 → 3421.44] Bye.
[3421.56 → 3422.20] Bye.
[3422.20 → 3422.82] Bye.
[3422.82 → 3423.02] Bye.
[3423.02 → 3423.64] Bye.
[3423.66 → 3424.00] Bye.
[3424.00 → 3424.82] Bye.
[3425.34 → 3425.86] Bye.
[3425.86 → 3426.20] Bye.
[3426.42 → 3428.04] Bye.
[3430.94 → 3431.50] Bye.
[3431.56 → 3431.78] Bye.
[3431.78 → 3432.34] Bye.
[3432.34 → 3432.82] Bye.
