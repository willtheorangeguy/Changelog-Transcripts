[0.00 → 4.52] I like to point back to 2008, where you think it's like a once in a generation event.
[5.22 → 9.36] And then like 10 years later, you have another once in a generation event.
[9.48 → 12.30] These events, like you can't write them off as one time anomalies.
[12.30 → 22.84] You actually have to figure out how to fold that in and be able to essentially like automatically regress against them, learn from them, and then figure out kind of how to apply it forward.
[23.10 → 26.08] Like you said, we're at the tail end of the pandemic right now.
[26.36 → 28.18] Hopefully, fingers crossed.
[28.74 → 28.92] Right.
[29.16 → 29.34] Yeah.
[29.34 → 33.72] But what happens if, you know, another large worldwide event happens 10 years from now?
[33.78 → 37.72] We can't just clip that chunk of data, remove it, and act as if it never existed.
[37.72 → 41.72] You need to build that into the methodology of your models.
[44.72 → 47.38] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[47.76 → 48.32] We love Linde.
[48.38 → 49.82] They keep it fast and simple.
[49.94 → 52.30] Check them out at linode.com slash changelog.
[52.54 → 54.60] Our bandwidth is provided by Vastly.
[54.94 → 58.50] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[58.50 → 60.50] Get a demo at LaunchDarkly.com.
[60.50 → 65.98] This episode is brought to you by our friends at O'Reilly.
[65.98 → 68.94] Many of you know O'Reilly for their animal tech books and their conferences,
[68.94 → 72.46] but you may not know they have an online learning platform as well.
[72.88 → 77.26] The platform has all their books, all their videos, and all their conference talks.
[77.26 → 83.74] Plus, you can learn by doing with live online training courses and virtual conferences, certification practice exams,
[84.08 → 88.40] and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[88.64 → 98.08] They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security,
[98.56 → 102.34] and even soft skills like business management and presentation skills.
[102.48 → 104.26] You name it, it is all in there.
[104.26 → 107.82] If you need to keep your team or yourself up to speed on their tech skills,
[107.92 → 109.74] then check out O'Reilly's online learning platform.
[110.28 → 113.82] Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[113.94 → 116.24] Again, O'Reilly.com slash changelog.
[125.04 → 132.10] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[132.10 → 136.52] This is where conversations around AI, machine learning, and data science happen.
[136.78 → 141.56] Join the community and Slack with us around various topics of the show at changelog.com slash community,
[141.78 → 142.90] and follow us on Twitter.
[143.06 → 144.62] We're at Practical AI FM.
[144.62 → 153.96] Welcome to another episode of Practical AI.
[154.30 → 156.00] This is Daniel Whiten ack.
[156.10 → 159.28] I am a data scientist with SIL International,
[159.58 → 162.56] and I'm joined as always by my co-host, Chris Benson,
[163.08 → 167.06] who is a principal emerging technology strategist at Lockheed Martin.
[167.40 → 168.04] How are you doing, Chris?
[168.18 → 169.36] I am doing very well.
[169.48 → 170.42] How's it going today, Daniel?
[170.42 → 172.40] Oh, no complaints.
[172.60 → 176.32] Lots of work to do, but all interesting things and fun things.
[176.46 → 177.16] You know my world.
[177.30 → 178.42] Lots of natural...
[179.02 → 179.86] About the same.
[179.98 → 182.98] Just lots of work and trying to enjoy spring weather.
[183.14 → 183.86] So I have been...
[184.94 → 187.36] Since I'm living in the South, I live in Georgia,
[187.84 → 189.32] I have a standing desk.
[189.38 → 190.88] I think I've mentioned this to you in the past.
[190.96 → 192.36] I didn't know you had a standing desk.
[192.48 → 192.90] I do.
[193.02 → 196.20] Like, I have a regular desk inside, which I need to replace.
[196.48 → 199.16] But I have a standing desk in my sunroof.
[199.16 → 200.22] Oh, okay.
[200.44 → 202.26] And so it's an open-air sunroof.
[202.46 → 205.72] For those of you that aren't from the American South,
[205.94 → 208.46] sunroof is basically just like a room.
[208.64 → 210.64] It's like a patio on the side of your house
[210.64 → 214.74] that has, like, actual glass walls instead of being open.
[215.02 → 217.40] I just realized that sunroof is jargon.
[217.54 → 218.02] Maybe so.
[218.08 → 218.50] I don't know.
[218.62 → 221.64] You know, I don't think of sunroof as jargon, but, you know, clearly...
[221.64 → 223.26] Obviously, in certain parts of the country,
[223.44 → 227.38] sunrooms aren't as maybe appealing as other parts of the country.
[227.38 → 228.94] I'm showing my bias right there.
[229.06 → 230.74] So I didn't understand that.
[230.86 → 231.46] So, okay.
[231.52 → 232.00] We're good.
[232.08 → 232.46] We're good.
[232.66 → 232.82] Yeah.
[232.92 → 235.40] And just doing work and enjoying the weather.
[235.54 → 236.72] Nice way to combine the two.
[236.84 → 238.56] I highly encourage anyone out there,
[238.64 → 241.24] if you have an outdoor area with a roof over it,
[241.56 → 242.46] put a standing desk there.
[242.50 → 242.88] You'll love it.
[242.94 → 243.84] Put a desk out there.
[244.24 → 244.66] That's right.
[244.70 → 245.08] It's great.
[245.28 → 246.10] Yeah, it's a good idea.
[246.44 → 246.60] Yeah.
[246.96 → 250.18] Today's topic I'm really excited about and the guest.
[250.28 → 252.02] We were talking before the show.
[252.02 → 254.72] This is actually a topic that's really close to my heart,
[254.82 → 256.00] because as our listeners will know,
[256.48 → 261.44] my wife owns a small business and has tried to navigate,
[261.70 → 263.08] I think with a lot of success,
[263.20 → 265.38] that business through these COVID times.
[265.82 → 269.94] And of course, that involves a lot of complicated stuff,
[270.00 → 272.84] especially her business is a manufacturing business.
[272.84 → 279.72] So there were all sorts of supply chain things and cash flow things and planning things that
[279.72 → 281.28] were just really difficult.
[281.28 → 286.82] And I think daily having very interesting financial discussions with her team
[286.82 → 293.46] to try to make it through that time from PPP loans to all sorts of things.
[293.76 → 295.10] She needs good tools, doesn't she?
[295.20 → 296.30] That's what I'm getting from that.
[296.40 → 302.32] She needs good tools and good ways to make sense of that financial data and plan accordingly.
[302.84 → 305.00] And I'm really excited on that topic,
[305.00 → 308.22] because today we have Intuited's director of data science,
[308.42 → 309.22] Sung Ho with us.
[309.38 → 309.86] Welcome, Sung.
[309.98 → 310.40] Hey, guys.
[310.46 → 311.32] Thank you for having me.
[311.46 → 311.76] Yeah.
[312.24 → 316.64] Before we get into all of that great stuff about customer experience
[316.64 → 321.10] and working with financial data and cash flow planning and all of those cool things,
[321.62 → 325.14] could you just give us a little bit of a sense of your background
[325.14 → 328.10] and how you ended up as director of data science at Intuit?
[328.30 → 328.98] Yeah, definitely.
[329.32 → 329.98] You know, it's interesting.
[329.98 → 336.06] Seven years ago, when I joined Intuit, I came from what we would then call a non-traditional background.
[336.66 → 340.24] So if you look at my background, I actually have a PhD in astrophysics.
[340.86 → 346.08] And before I started Intuit, I was doing a lot of data reduction, image processing,
[346.36 → 350.26] signal processing, and studying dark matter-dominated dwarf galaxies.
[350.26 → 351.10] Right?
[351.22 → 356.38] A whole complete other world away from, like, what I do now in applied AI.
[357.02 → 361.76] But what was interesting was that at that time, right, the field was still fairly nascent.
[362.08 → 368.50] And a lot of us who came from nontraditional backgrounds kind of came over into data science
[368.50 → 374.52] and AI as a field because we realized, like, holy heck, we actually were doing using the same techniques.
[374.52 → 378.96] We just had completely different names for these techniques in our respective fields.
[379.16 → 380.12] That's so true, right?
[380.38 → 380.86] I remember.
[381.04 → 382.32] So I came from physics, too.
[382.48 → 387.56] And I was, like, had this experience where it was, like, I was looking at all these data science methods.
[387.56 → 392.88] And I was like, oh, like, when you're saying you're doing this, you're just using ordinary least squares.
[393.10 → 395.72] Like, how many times have I done that in my life?
[395.76 → 396.92] Like, a million times.
[396.92 → 399.54] And, like, you're just using a different word for it.
[399.60 → 400.32] That's kind of weird.
[400.46 → 401.58] But, okay, I'll do that.
[401.74 → 402.58] Yeah, exactly.
[402.92 → 403.88] What is it with physicists?
[404.12 → 410.54] I'm telling you, I think that there are more people in data science and AI from physics than any other field that transfers over.
[410.76 → 413.28] You guys are ruling the world here in that way.
[413.40 → 419.40] Yeah, well, I think also physicists have this, whether it's, and maybe, Sung, you have a perspective on this.
[419.40 → 426.34] But I feel like in physics, for whatever reason, it breeds this sense of, like, I'm not qualified to operate in this area.
[426.74 → 430.02] But I do feel like I have the expertise to work in this area.
[430.16 → 431.76] So I'm going to go ahead and jump in and do it.
[432.24 → 434.52] I don't know if you get that same sense.
[435.34 → 436.40] Yeah, for sure.
[436.60 → 448.66] I mean, there was, you know, kind of, like, figuring out the language of data science and how to translate the skills that you have and the things that you know into this, like, new industry and this new accepted skill.
[448.66 → 452.56] But just knowing that, hey, you know, I write a lot of code.
[452.94 → 454.16] I know a lot of math.
[454.24 → 457.64] I do a lot of matrix math in my daily life previously.
[457.96 → 460.76] And it seems like these are all the things that we do in data science.
[460.90 → 462.00] So let's just go for it.
[462.30 → 464.42] And exactly as you said, Chris, right?
[464.50 → 472.14] Like, now, if you look at kind of the composition of the backgrounds of folks who are coming into data science, it's all over the place.
[472.52 → 474.66] And the umbrella has really expanded.
[474.66 → 481.20] But when I started, I actually had to go through a program to help me repackage all the things I knew.
[481.34 → 482.56] Like, oh, ordinary least squares.
[482.76 → 486.60] Oh, actually, like, it's regularization and regression.
[486.88 → 491.42] So just being able to speak that language to convince folks that, hey, we had the skills.
[491.42 → 504.04] Because in the past, you know, I would write these, like, massive programs to take raw data from telescopes and then actually convert them into meaningful information and then write papers.
[504.72 → 507.60] And a lot of, like, the day-to-day work is exactly the same.
[507.60 → 511.44] So that's kind of a bit, you know, my journey towards data science.
[511.64 → 519.26] And I specifically wanted to come into it because when I was in grad school, I used Mint a lot.
[519.72 → 521.10] Like, every dollar counts.
[521.28 → 524.78] And you have to kind of be, you know, pretty obsessed with it.
[525.12 → 527.94] But I had a really poor user experience with Mint.
[528.64 → 532.74] And I'm like, you know, I'm pretty sure I can do better than what exists right now.
[532.74 → 538.86] And so when I came for my interviews, and they said, hey, you know, you could totally work on me.
[538.90 → 540.14] You can come in and fix this.
[540.56 → 542.00] Like, yes, please sign me up.
[542.76 → 548.24] And it was just, you know, like, this openness to, you know, allowing us to innovate.
[548.66 → 553.66] And I found it kind of refreshing that I told my boss, hey, I actually hate one of your products.
[553.76 → 554.82] Can I come and make it better?
[555.48 → 556.18] And he's like, yes.
[557.82 → 558.54] That's great.
[558.54 → 564.80] It's great to have that environment where you can sort of be comfortable sharing those things and brainstorming solutions.
[565.20 → 568.10] Of course, I mean, there's always boundaries within a workplace.
[568.10 → 570.74] But it's really cool to hear that you found that environment.
[570.98 → 571.12] Yeah.
[571.24 → 573.40] And, you know, it's been great ever since.
[573.56 → 576.10] So as I mentioned, I've been at Intuit for seven years.
[576.26 → 584.48] And one of the things that, you know, I specialize in, and my team specialize in is we specialize on the applied AI side.
[584.48 → 590.60] So building a lot of production models, features, and systems that go directly to our end customer.
[591.12 → 594.10] Because that's something that I'm personally super passionate about.
[594.54 → 605.96] I really like to, you know, take a look at some of the core problems that our customers have right now and figure out, well, how do I bring my skill set in helping solve that for you and make it easier for you?
[605.96 → 609.04] Because I, you know, previously was a customer.
[609.34 → 616.88] And I think similar to you, Daniel, is that I have 10 siblings and half of them own small businesses.
[617.16 → 621.08] So, you know, it really is like a space that really speaks to me.
[621.62 → 627.00] And, you know, it's really fun to be able to actually build things that you can see your family using.
[627.68 → 629.36] I can really see that benefit.
[629.70 → 631.30] I just want you to know you have my sympathies.
[631.42 → 634.58] I thought I have four siblings, you know, there's five of us.
[634.58 → 638.02] And I thought we were, so yeah, lots of respect there.
[638.42 → 640.26] Do your siblings own businesses, Chris?
[640.70 → 641.56] Actually, yes.
[641.72 → 641.98] Yes.
[642.34 → 643.14] Several of them do.
[643.54 → 644.60] You can relate in that sense, I guess.
[645.12 → 645.28] Yeah.
[645.32 → 645.50] Yeah.
[645.80 → 646.00] Yeah.
[646.20 → 646.58] I can.
[646.86 → 648.50] But she's done way better than I have.
[648.60 → 650.08] I have a bigger family, and they're all doing that.
[650.62 → 651.24] So keep going.
[651.34 → 651.56] I'm sorry.
[651.64 → 652.18] I didn't mean to interrupt.
[652.70 → 652.86] Yeah.
[653.00 → 655.68] No, I think that most people are like, how do you deal with 10 siblings?
[655.94 → 661.62] It's, you know, at any one time you have a high probability of liking at least one of them.
[661.80 → 661.96] Right.
[662.80 → 663.56] There you go.
[663.56 → 665.16] So that's a good attitude.
[665.70 → 671.78] And I think also like the small business owners, they have to, like we were talking about in physics,
[671.78 → 676.92] like this sort of comfort level with like operating in a space that you're not necessarily
[676.92 → 682.78] qualified to operate in and just like relying on the skills that you have in your past and
[682.78 → 684.74] picking up what you need going forward.
[684.84 → 688.18] I feel like small business ownership is very similar.
[688.18 → 694.62] It's like, oh, I've, you know, I've never cleared a container from China through customs
[694.62 → 697.24] with, you know, my raw materials in it.
[697.24 → 701.58] It's like there's some information on the Internet about that, but I'm going to figure it out.
[701.58 → 705.32] And maybe some of that you're going to talk about the cash flow of things and other things,
[705.32 → 707.60] I think, on the financial side.
[707.60 → 713.60] But a lot of that, too, it's like maybe in, you know, I've learned a lot of terms from my wife,
[713.64 → 719.20] which I'm not a financial person, but she learned, you know, how to do like profit and loss statement
[719.20 → 722.62] and all of those things in her school, which is great.
[722.62 → 725.88] But there's all of these others like things.
[725.88 → 732.74] And like, for example, forecasting and, you know, forecasting sales and raw material need
[732.74 → 735.92] and all that, that's like it is a very data science problem.
[736.18 → 737.28] It has to be data driven.
[737.28 → 740.92] And, you know, if you get it wrong, then your business goes under.
[741.04 → 742.44] So it's very high stakes, too.
[743.00 → 748.32] But maybe before we jump into some like the individual tools that you've worked on, Sung,
[748.32 → 754.20] one of the things that you mentioned in terms of the sort of general space that you're working in
[754.20 → 758.52] within Intuit is customer experience and AI for customer experience.
[758.52 → 764.12] So when you're thinking about customer experience at Intuit, what does that mean?
[764.12 → 768.42] Maybe for data science people out there that are trying to understand,
[768.76 → 771.30] what does it mean to do data science for customer experience?
[771.42 → 772.22] How do you look at that?
[772.36 → 773.64] Yeah, that's a great question.
[773.88 → 777.72] The way that, you know, we as a company approach it is we have a system called
[777.72 → 780.20] Design for Delight and customer driven innovation.
[780.98 → 785.68] And the approach is to really get into the minds of our customers and understand
[785.68 → 788.48] what are the most important problems that they have.
[788.90 → 793.50] Because you can only build great solutions if you really understand what the problem is
[793.50 → 797.34] and not just like what it is that you want to build, but why it's actually important.
[797.60 → 803.08] And so we use this, the system called Design for Delight, where we do a lot of customer interviews.
[803.08 → 809.84] You work with a customer experience researcher and, you know, you just kind of see how your customers are using your products.
[810.26 → 811.56] Where are they getting stuck?
[812.02 → 812.18] Right.
[812.22 → 813.68] What is confusing for them?
[813.90 → 818.44] Where are the tasks that, you know, there's spending a lot of time on that they wish they were not doing?
[819.10 → 825.18] And then there's also the other piece, which is what did they wish that you actually had that would make their lives a lot easier?
[825.70 → 832.80] And these are things that, you know, like, so there are some traditional methods where you can infer it by looking how a customer uses the product.
[832.80 → 838.62] But honestly, it's just faster to talk to a wide variety of customers and have them tell you directly.
[839.16 → 844.68] So starting from that base where you really understand what the problem is, then we take it back, and we say,
[844.82 → 849.60] okay, what are some of the hypotheses that we have in creating the solution?
[850.16 → 852.58] And the solution could be done by data science.
[852.58 → 854.96] It could be done via an experience design.
[855.16 → 858.38] It could be done via some very simple rules, right?
[858.80 → 862.28] But what is the solution that you want to build to solve that problem?
[862.28 → 871.94] And then you go into the mode of decomposing it into, okay, like there's the experience piece, there's the machine learning piece, there's the engineering piece.
[872.28 → 881.50] And then we go off with these hypotheses, you know, build a couple of quick MVPs, minimum viable products for our listeners who are new.
[881.86 → 887.62] Once we have these MVPs, the thing that I learned, which actually took me a little bit to appreciate,
[887.62 → 894.44] is that, you know, when you build an MVP for a customer, and you show it to them, you're like, tell me how you would use this.
[894.52 → 896.10] Would this be beneficial to you?
[896.76 → 899.06] In the past, we would put in mock data.
[899.28 → 904.44] And then, you know, the customer would say, yeah, you know, if this was my data, I would react this way.
[904.52 → 905.98] I would see this.
[906.36 → 908.50] And it was actually not useful at all.
[908.50 → 911.66] Because you're asking them to imagine what they would do.
[912.24 → 920.68] And so we pivoted and moving forward from about three or four years ago when we found this insight, we actually just loaded the customer's data in.
[921.10 → 922.46] We ran it through our models.
[922.56 → 924.48] We made the predictions, whatever.
[925.10 → 926.46] And then we showed it to the customer.
[926.46 → 930.64] And then immediately, like, the feedback that we got back was so much richer.
[930.90 → 934.56] It actually helped us, like, narrow in on the right solution.
[935.26 → 942.18] And it was just, like, you know, this, like, aha moment for me that I guess it's obvious now but was not obvious back then.
[942.40 → 947.84] I love that as you've gone through, I've had, like, three or four questions, and you keep answering them before I ever get it.
[948.06 → 949.04] No, no, no, that's good.
[949.10 → 949.88] That's not a bad thing.
[950.06 → 951.02] I'm really curious.
[951.02 → 957.62] I was going to ask you about kind of, like, how do you know when you get to the quality of those inputs so that it can translate to data?
[957.72 → 960.32] And you were kind of saying, well, now we're just going and taking the data.
[961.00 → 963.56] What is it about when you said I took the data?
[963.78 → 974.46] Can you dive into that for a moment in terms of saying how do you know that you've just ended up with the right data set to innovate in such a way that your customers are going to be delighted at the end of the process?
[974.84 → 978.46] How do you recognize that you've achieved that moment?
[978.46 → 978.86] Yeah.
[978.86 → 989.48] Yeah, it's a little bit of an art, but I would say that, you know, as a scientist, one of the things that we do is we always have a couple of hypotheses and a couple of approaches on how to solve the problem.
[990.10 → 999.20] And so at any one time, we would have multiple solutions, and we would beforehand identify what the success criteria is first that we want.
[999.42 → 1002.10] Then we show it to the customer, and we compare them.
[1002.10 → 1008.06] So this is like a super lean, very baby early A-B test before we go full into A-B testing.
[1008.56 → 1017.04] What I find that gets in the way of this is a lot of times folks build models, but they don't think about, well, what is the success criteria for me?
[1017.28 → 1018.92] What am I trying to get the user to do?
[1019.26 → 1023.88] Like if I talk to, you know, our marketing teams, it's like we want to get a user to convert.
[1023.88 → 1027.36] But that's like maybe like 50 clicks before you even get there.
[1027.48 → 1032.10] But what is the thing that I'm going to like actually physically affect and ask a customer to do?
[1032.28 → 1033.30] That's my target.
[1034.00 → 1042.26] And so like having that very robust target and measuring it across your different hypotheses and experiments is one way to do it.
[1042.60 → 1046.92] But it can be a little bit challenging to come up with that.
[1046.92 → 1047.70] I can imagine.
[1047.70 → 1055.12] I know that I have participated in similar processes before and speaking from experience, not as much as you have.
[1055.22 → 1056.82] It was really hard to do.
[1057.16 → 1059.50] And so I'm very impressed with that.
[1059.70 → 1060.46] Yeah, I'm curious.
[1060.66 → 1072.38] One perspective on this is that like you look at the customers and this customer experience survey, and then you identify where they're getting stuck, like you said.
[1072.38 → 1088.00] What if it's like scenarios where maybe it's something that you need to develop that's outside, like the customer doesn't know that they need this yet, or it's outside their scope of maybe, you know, what they even have imagined.
[1088.00 → 1090.44] Like, oh, I didn't imagine that I could have this.
[1090.44 → 1106.46] But how do you come up with a way to validate that those are sort of good ideas, the ones that might not be driven by the specific customer pain that you've observed in an interview, but maybe sort of new data product development is a good way to put it.
[1106.60 → 1106.76] Yeah.
[1106.94 → 1113.36] That one, it's very interesting because, you know, for me, I tend to be fairly customer backed.
[1113.36 → 1120.64] And so I go back to the roots of like, well, why is this thing a pain and not focusing so much on the what?
[1120.88 → 1123.36] I think a lot of times folks stop at the what?
[1123.68 → 1125.42] Like, what is it that the customer wants?
[1125.48 → 1130.84] It's really more about why piece because, you know, otherwise you can't innovate, right?
[1130.88 → 1133.90] You can't wait for someone to say, I really want this thing.
[1134.22 → 1136.78] They might not know that they actually want that thing.
[1136.78 → 1147.78] And so getting down to the why and then working with the teams on coming up with, okay, well, what are some ways that we could actually solve this in experiences that are new?
[1147.98 → 1155.24] In my team, we do a mix of replacing really, you know, rote existing things and backing it with machine learning.
[1155.40 → 1161.04] And in other instances, we're building tools that just, you know, the customers didn't even think they wanted at all.
[1161.04 → 1172.70] One example of that is like in the cash flow space overall, like when you think about cash flow, for me, naively, I initially said money in, money out, delta between money in, money out.
[1172.78 → 1173.66] That's what I care about.
[1174.38 → 1185.92] And then you talk to a small business, and they're like, well, actually, you know, I have like invoices, I have bills, I have, you know, loans that I need to pay, I have assets.
[1186.32 → 1189.60] And I care about all of those things and I need to know where they all are.
[1189.60 → 1199.82] But when we were talking about our, to our small businesses, we said, well, okay, like you want to know your invoices, you know, what are outstanding invoices so that you can get paid?
[1200.16 → 1210.12] They said, yeah, we pushed, and we said, well, what if we can tell you not only when an invoice would get paid, but like the date range within which it would get paid?
[1210.54 → 1212.52] Would that be something, you know, you would want?
[1212.60 → 1213.90] And they were like, you can do that?
[1215.16 → 1217.32] I didn't know that was possible at all.
[1217.32 → 1217.76] Right.
[1218.12 → 1222.52] For them, they were really thinking about just send me a reminder if it's going to be due soon.
[1222.86 → 1228.56] But we expanded that, and we said, we can actually build this new capability that allows you to go much further and have more control.
[1229.14 → 1235.46] And so I think that that's like kind of one example of starting with a why, which is like they need to understand their cash flow.
[1235.46 → 1249.08] This episode is brought to you by our friends at Rudder stack.
[1249.18 → 1253.80] And we're calling all data engineers to check out Rudder stack Cloud and start building smart customer data pipelines.
[1254.30 → 1256.04] Rudder stack is warehouse first.
[1256.22 → 1257.22] No more silos.
[1257.66 → 1261.02] Rudder stack builds your customer data lake on your data warehouse, not theirs.
[1261.02 → 1266.72] Enabling all functionality of a CDP with more security and retaining full ownership of your data.
[1267.06 → 1269.50] It's open source and API first.
[1269.82 → 1273.24] Rudder stack can be easily integrated into your existing development processes.
[1273.80 → 1276.54] And because they're open source, you can see all their code.
[1276.78 → 1279.20] So you don't have to worry about vendor lock in or black boxes.
[1279.74 → 1281.32] And best of all, they have transparent pricing.
[1281.52 → 1283.76] Stop paying your CDP a premium to store your data.
[1284.22 → 1289.10] Rudder stack is free up to 500,000 events and pricing scales transparently from there.
[1289.10 → 1291.56] Learn more and get started at Rudderstack.com.
[1291.84 → 1294.12] Again, Rudderstack.com.
[1294.26 → 1297.80] That's R-U-D-D-E-R-S-T-A-C-K.com.
[1297.80 → 1323.50] So I'd really like to dive back into that even more because I'm very intrigued by you, you know, knowing the data that you have and figuring out how do you start that process?
[1323.50 → 1326.96] Because, you know, we talk to people all the time that are doing all sorts of cool things with data.
[1327.24 → 1331.72] But I'm really fascinated by your creative process that's kind of encompassing that.
[1332.20 → 1338.32] And so when you're thinking about I'm going to innovate for the customer in a way they have no idea that I can.
[1338.68 → 1339.92] How do you approach that?
[1340.06 → 1347.52] How do you know what you're going to do with the data that you have or know that you need to go get that data in order to achieve that?
[1347.52 → 1350.76] And using data science as a mechanism to get there.
[1350.88 → 1353.40] How do you put it together before you do the do?
[1353.56 → 1354.78] How do you conceive of it?
[1354.84 → 1355.94] Before I do the do?
[1356.14 → 1356.88] I like that.
[1357.00 → 1357.14] Yeah.
[1357.46 → 1357.86] Sorry.
[1357.86 → 1365.94] That's something that I think a lot of us in the field are still working through because every new problem is a little bit different.
[1366.42 → 1367.84] Some are much more straightforward.
[1368.56 → 1368.74] Right.
[1368.82 → 1371.32] You know exactly which data source you're going to get.
[1371.42 → 1373.10] You know exactly where to start.
[1373.22 → 1377.52] And you even have an idea of what the initial features are that you want to start with.
[1377.58 → 1380.14] For others, you have to get a little bit creative.
[1380.82 → 1381.04] Right.
[1381.20 → 1383.02] And trawl through the data a little bit.
[1383.02 → 1390.58] One of the ways that I've tried to fast track this is that, you know, as data scientists, we don't work in silos.
[1390.98 → 1393.16] A lot of times we work with our analytics teams.
[1393.16 → 1401.96] We work with our product partners, and we work with our design teams to jam together and say, OK, these are some, you know, pie in the sky ideas that we want to work on.
[1402.18 → 1404.14] That could really solve a big customer problem.
[1404.60 → 1411.90] Once we narrow in on that, we actually source it from the broader team because they have kind of like an initial starting point.
[1411.90 → 1417.82] And, you know, for me, I would rather not do a random walk through parameter space to figure out where to start.
[1417.98 → 1420.66] It's easier to just crowdsource it from the team.
[1421.18 → 1428.16] And so sometimes it's actually from our engineering partners who say, hmm, you know, I'm aware of this data that we're capturing right now.
[1428.22 → 1429.86] Do you think that that would be useful for you?
[1430.28 → 1432.78] We go, aha, OK, actually, never thought of that.
[1432.96 → 1434.24] Let's go and try it out.
[1434.24 → 1445.80] So it's almost kind of taking the creativity of the entire organization, the entire larger team, and then figuring out where to allocate resources against that creativity based on what's rising to the top.
[1445.88 → 1446.20] That's right.
[1446.34 → 1446.76] That's right.
[1447.22 → 1455.54] And so when we start at the problem first, and then we figure out whether we have the data, because I have never worked on a project where all the data we ever needed was available.
[1455.94 → 1458.66] Sometimes you actually need to go and capture that data.
[1458.82 → 1460.42] You need to go and buy that data.
[1460.42 → 1461.06] Right.
[1461.36 → 1468.20] Having everybody in their together kind of opens up the door and more avenues for you to kind of see what you're not seeing right now.
[1468.42 → 1471.10] I'd really like to dive into this idea.
[1471.38 → 1478.10] There's an article that we'll link in our show notes about some of the things that you've been doing during the pandemic time.
[1478.22 → 1480.94] And I'd love to dive a little bit into those.
[1480.94 → 1486.60] One of the intriguing things that I kind of noted was that pandemic hit.
[1486.60 → 1502.24] And then, of course, as any business, including Intuit, it's like there's this kind of natural inclination to be hesitant to do a lot of different things because, you know, we have no idea what's going to happen next.
[1502.24 → 1504.06] We're really unsure about the future.
[1504.06 → 1510.62] But it seems like, you know, your team and Intuit really took the vision that like, hey, now is a time to innovate.
[1510.88 → 1513.30] And now is a time to try something different.
[1513.52 → 1516.00] It seems like that really paid off well.
[1516.00 → 1528.50] But I'm wondering if you could go through that mindset and how you kind of came to be motivated that this sort of cash flow tool and things were things that you should be focusing on during this time during the pandemic.
[1528.90 → 1529.14] Yeah.
[1529.82 → 1533.96] Then, you know, a year ago, like the world kind of went upside down.
[1534.16 → 1534.40] Right.
[1534.88 → 1535.36] Yeah.
[1535.60 → 1536.78] I remember that.
[1537.22 → 1537.36] Yeah.
[1537.36 → 1544.40] And I think we all kind of had plans for ourselves and businesses had plans for what growth was going to look like.
[1544.76 → 1550.66] You know, for us, we had a roadmap of what we were going to build for our customers, assuming that the growth was going to continue.
[1551.40 → 1557.04] And then kind of overnight, you know, when the shutdown happened, like you can look at it in our data.
[1557.04 → 1561.00] For some of our small businesses, like revenue dropped 99%.
[1561.00 → 1565.28] And like you don't see step functions like that in the data ever.
[1565.28 → 1572.34] So this was just a global worldwide massive event that everybody was feeling simultaneously.
[1573.14 → 1578.28] And through every single new locale or state where a lockdown occurred, this drop happened.
[1579.08 → 1594.28] And we said this, like we have to do something for our small businesses because this not only is such a scary time for them, but it's also a huge time of uncertainty for everyone across the world.
[1594.28 → 1599.56] And your data is sort of a history book for a monumental event in world history when you think about it.
[1599.56 → 1599.76] Yeah.
[1599.90 → 1606.08] You know, seeing that financial data do that, that is a powerful story right there that you're describing, seeing that step function.
[1606.20 → 1606.36] Yeah.
[1606.48 → 1609.30] It absolutely was fairly shocking, right?
[1609.30 → 1611.10] To be able to see it so immediately.
[1611.10 → 1613.46] And it was so fast as well.
[1613.46 → 1619.38] And so, you know, we really came together, and we said, what can we do to help our small business customers?
[1619.82 → 1625.70] And, you know, like we kind of sourced across the entire company a whole host of different solutions.
[1625.70 → 1630.98] So if you can recall, you know, early on in the pandemic, there were a lot of GoFundMe's for small businesses.
[1631.40 → 1633.66] We hosted quite a few.
[1633.86 → 1637.60] We partner with GoFundMe to enable our small businesses to raise money.
[1638.06 → 1642.02] But that's a little bit of a temporary solve, right, for that moment.
[1642.48 → 1646.54] Because, you know, we didn't know how long the pandemic was going to last.
[1646.72 → 1650.08] And there's the PPP loan program, right?
[1650.08 → 1662.68] When that was announced, we realized actually a lot of our small businesses and a lot of customers in general, including my sisters and family who I helped through the loan process, eligibility was really confusing.
[1663.18 → 1669.28] Like you needed to know so much more about your business than most people were equipped to be able to do at all.
[1669.28 → 1680.16] And so we rolled out another program using like our knowledge engine to build like the aid assist, which helps small businesses like quickly say, am I eligible for these loans?
[1680.24 → 1682.58] What are the loans that I'm eligible for and get that?
[1683.28 → 1695.68] And then, you know, for my team specifically, you know, because we're so close to the data, we looked in there, and we said, wow, like cash flow right now, the historical data that we have about your cash flow is wrong.
[1695.68 → 1701.42] Like those of us in this field, like the historical data is like where you build your models off of.
[1701.94 → 1711.04] And if you have like this, this drastic shift and this drastic change, right, you need to go in and make huge modifications to your model to accommodate for that.
[1711.64 → 1719.00] And not just that, like the level of granularity of details that you provide to customers, the information they want to know is different.
[1719.26 → 1723.96] Some businesses did super well, and some are, you know, really, really suffering.
[1723.96 → 1735.52] When you're looking at that data, and you're just, you're going through the middle of this enormous event, one which we're still in the tail end of, presumably, hopefully the tail end.
[1735.52 → 1745.90] And you are, you're looking at how so many organizations are trying to cope, and you have that real-time data and the history developing on that.
[1745.90 → 1754.08] And you're, you're figuring out how your own organization is going to address that, serve its customers and deal with the same set of circumstances.
[1754.08 → 1770.14] Did that give you or the company, I'll let you answer it any way you want, any sense of insight or revelation in terms of how to approach the business of finance differently than you ever had before?
[1770.14 → 1773.96] Or something that might actually be sustained past just the pandemic.
[1774.14 → 1777.52] So truly a lesson learned, not just a coping mechanism for the moment.
[1777.52 → 1786.70] Is, is there anything that you and your colleagues talked about, about like, now that we know this, nothing will ever be the same in how we look at this and, and we're making changes?
[1787.24 → 1787.42] Yeah.
[1787.42 → 1790.20] So I'd say that there are two parts.
[1790.20 → 1805.70] I can speak for, you know, my team and how we build models, but I'll start with how we as a company realize like, and really reinforce one of our beliefs from before the pandemic and made it much stronger.
[1805.70 → 1808.84] Is that we have our product called QuickBooks Capital.
[1809.40 → 1811.92] And so we provide small business loans to our customers.
[1812.66 → 1819.44] And I would say the magic or secret sauce there is that we have a lot more data than a standard lender would, right?
[1819.52 → 1821.68] For our customers, we have all of their accounting data.
[1822.40 → 1827.74] And from that, we're able to actually offer loans to customers who traditionally would not be able to get loans.
[1827.74 → 1838.16] What we saw during the pandemic was that there's a large population who are underserved in general, who would not have been able to get loans, who we were able to offer PPP loans for.
[1838.90 → 1843.38] Because we knew their data very well, we knew their risk profile, we could actually underwrite.
[1843.56 → 1853.86] So I think that really reaffirmed our decision that, you know, we need to continue to invest in figuring out ways to continue to serve the underbanked and underserved population.
[1854.28 → 1855.70] That's at the company level.
[1855.70 → 1863.94] And there's a lot that you can do in the data to figure out whether, you know, you're capturing the population, or you're actually doing the right thing there.
[1864.48 → 1874.54] But, you know, for on the other side, the more technical side with our teams is that we've seen just, you know, with these large worldwide events, right?
[1874.60 → 1880.00] Like, I like to point back to 2008, where you think it's like a once in a generation event.
[1880.00 → 1885.22] And then, like, 10 years later, you have another once in a generation event.
[1885.84 → 1889.80] And so, you know, these events, like, you can't write them off as one-time anomalies.
[1889.94 → 1901.50] You actually have to figure out how to fold that in and be able to essentially, like, automatically regress against them, learn from them, and then figure out kind of how to apply it forward.
[1901.50 → 1901.94] Right?
[1902.38 → 1905.38] Like you said, we're at the tail end of the pandemic right now.
[1906.46 → 1906.82] Hopefully.
[1907.60 → 1908.38] Fingers crossed.
[1908.50 → 1908.72] Yeah, hopefully.
[1908.92 → 1909.12] Right?
[1909.34 → 1909.58] Yep.
[1909.66 → 1914.50] But what happens if, you know, another large worldwide event happens 10 years from now?
[1914.54 → 1919.12] We can't just clip that chunk of data, remove it, and act as if it never existed.
[1919.78 → 1919.90] Right?
[1919.94 → 1924.86] And so, you need to build that into the methodology of your models.
[1924.86 → 1927.16] Real quick, and Daniel, I saw you about to say something.
[1927.22 → 1928.96] I just wanted to say something before you left that point.
[1929.12 → 1933.80] In the different industry that I'm on in defence, I noticed it because it's directly to your point there.
[1933.98 → 1940.18] The intelligence community, which is the industry I'm in, has just released its annual assessment of world events.
[1940.30 → 1947.22] And one of the big things that goes directly to your point is the fact that they're talking about with the pandemic over,
[1947.22 → 1954.44] there will still be fallout politically and economically in various geographies and such for years to come.
[1954.44 → 1960.76] So, the outcome of today will lead to other events that are unforeseen, some of which may be significant.
[1961.22 → 1966.56] I just wanted to note that that's a great point, and it really spans across industries in different contexts.
[1966.96 → 1968.50] And Daniel, I apologize for cutting you.
[1968.58 → 1969.80] I saw you just about to speak.
[1969.86 → 1970.88] Oh, I forgive you, Chris.
[1971.08 → 1972.24] I'll always forgive you.
[1972.24 → 1991.84] Oh, so you were talking about like this idea that models that you build need to be robust against this sort of once in a generation event that you can sort of no longer expect that this is a once in a generation, but you have to be ready for them.
[1991.84 → 2000.60] Again, we'll link to this blog post in our show notes, but I'm sort of looking at the cash flow planner, and maybe you can talk a little bit about the goals there.
[2000.72 → 2004.32] But one of the things I see is like developing a personalized forecast.
[2004.32 → 2013.24] And when I think about forecasting, like you were talking about, it's like, oh, well, how much good historical data do you have to develop that forecast?
[2013.64 → 2026.16] So, how is it even possible to develop a sort of robust forecasting system that's robust against this sort of, you know, really crazy events that we're dealing with?
[2026.16 → 2030.66] Well, I can tell you it's dang hard is the short answer.
[2031.24 → 2040.06] One of the things that we got creative with in the forecasting example is, well, let's take sales as one type of input forecast, right?
[2040.20 → 2045.22] Traditionally, you take your sales in the past, and then you can project that for standard time series forecasting.
[2045.22 → 2061.10] What we were seeing during the pandemic is that there are actually a lot of customers who have extremely sparse data, because what used to be daily sales are now turning into maybe once a week, you're getting a sale, but you didn't have.
[2061.60 → 2063.78] And that was the totality of your sale.
[2063.94 → 2071.32] And so incorporating that in and being able to deal with sparsity of data is one way that we folded that in.
[2071.74 → 2073.78] There's also actually learnings to be had.
[2073.78 → 2078.20] This is where you can actually transfer the models that you build from for one business to another.
[2078.50 → 2085.16] There are certain businesses who essentially all of their sales and all of their events happen once during the year.
[2085.66 → 2088.02] Like my favourite example is a Halloween store.
[2088.38 → 2096.44] There's a very short lifetime for a Halloween store where they have nothing, they have everything, and then they have nothing again for a while.
[2096.44 → 2107.30] And so for those, we actually can take the models that we've built for them, learn for them, and actually apply them for companies who are going through somewhat similar events right now.
[2107.82 → 2115.68] So that's where it's been advantageous to have that broad view across the industry and being able to transfer across.
[2115.68 → 2132.00] Changelog++ is the best way for you to directly support practical AI.
[2132.54 → 2142.92] Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal, and helps sustain our production of practical AI into the future.
[2142.92 → 2152.00] Simply follow the Changelog++ link in your show notes or point your favourite web browser to changelog.com slash plus.
[2152.30 → 2156.20] Once again, that's changelog.com slash plus.
[2157.92 → 2159.94] Changelog++ is better.
[2159.94 → 2160.60] Changelog++ is better.
[2160.60 → 2161.26] Changelog++ is better.
[2172.12 → 2182.64] So, Sung, I'm kind of interested to, I guess, get a little bit more into the weeds of this response to these changing times in your data and your forecasting.
[2182.64 → 2186.26] and we don't have time to get into all the specifics,
[2186.26 → 2189.12] but if you take, and you look at, you know,
[2189.12 → 2191.70] some of the trends out there in AI right now,
[2192.16 → 2195.34] in terms of, well, we've got all sorts of things.
[2195.34 → 2197.48] We've got, of course, the trend to use,
[2197.88 → 2199.50] you know, neural network-based models.
[2199.50 → 2201.82] We've got sort of semi-supervised things.
[2201.82 → 2204.10] We've got reinforcement learning
[2204.10 → 2206.06] and plus this sort of, you know,
[2206.14 → 2209.14] quote, more traditional type machine learning models
[2209.14 → 2210.48] or statistical models.
[2210.48 → 2213.06] As you're thinking, and you're looking about this scenario
[2213.06 → 2214.98] where like looking to the forward,
[2215.16 → 2219.16] we don't know what sort of events is going to come up
[2219.16 → 2220.74] and we need to be able to, you know,
[2220.80 → 2225.90] adapt our models as our data increasingly changes over and over.
[2226.32 → 2229.76] So if you sort of match that landscape of AI techniques up
[2229.76 → 2232.28] with, you know, this problem that you're looking at,
[2232.56 → 2234.86] which of this sort of become most relevant
[2234.86 → 2238.56] and have you experimented with a variety of those
[2238.56 → 2240.40] or what have you found most useful
[2240.40 → 2242.22] in your context?
[2242.42 → 2243.82] Yeah, that's a great question.
[2244.24 → 2247.18] We've actually experimented with quite a bit.
[2247.46 → 2248.92] It wasn't until very recently
[2248.92 → 2251.20] that deep learning kind of beat
[2251.20 → 2253.56] your traditional time series methodology
[2253.56 → 2255.04] in terms of performance.
[2255.04 → 2257.08] In the space that, you know,
[2257.22 → 2258.90] myself and my team work in,
[2259.44 → 2262.16] one of the considerations that we have to make
[2262.16 → 2264.84] is model performance and efficacy
[2264.84 → 2269.44] compared to, in our case, explainability
[2269.44 → 2272.68] and being able to actually help our customers understand
[2272.68 → 2274.70] why we're making these decisions.
[2274.70 → 2277.84] And that's specifically because we're dealing with financial data
[2277.84 → 2280.12] and it can have very large implications
[2280.12 → 2282.86] if you don't really trust the output
[2282.86 → 2285.56] of the recommendations we provide for you.
[2285.56 → 2288.00] And so, you know, in most cases
[2288.00 → 2289.92] where it's not as customer facing
[2289.92 → 2292.34] and the decision is not directly to your dollar,
[2293.02 → 2296.52] right, we use, you know, more black box techniques
[2296.52 → 2297.44] as I call them.
[2297.88 → 2299.32] But for this case,
[2299.38 → 2301.02] specifically for time series forecasting,
[2301.22 → 2302.66] we tend to stick with models
[2302.66 → 2306.10] where we can explain why these decisions are made
[2306.10 → 2308.16] simply because like for our customers,
[2308.28 → 2310.02] like you have to be able to build trust.
[2310.14 → 2312.98] They won't use it unless they know what goes into it.
[2312.98 → 2316.58] I'm sure, you know, your wife may have comments
[2316.58 → 2318.10] and feedback about this, Daniel.
[2318.54 → 2321.48] But when you're dealing with money, right,
[2321.86 → 2323.28] you have to be fairly sensitive
[2323.28 → 2326.08] and really understand what it is,
[2326.44 → 2328.42] the tolerance level from the customer
[2328.42 → 2331.06] in terms of like how far you can go
[2331.06 → 2332.78] and how black boxy you can go.
[2333.12 → 2334.90] How might that evolve over time?
[2335.02 → 2336.74] And I'm asking a speculative question
[2336.74 → 2337.72] and I recognize that,
[2337.78 → 2339.80] but there's a lot of concern
[2339.80 → 2342.72] about anything that's sensitive.
[2342.72 → 2343.82] I'm in a sensitive industry,
[2343.90 → 2344.84] you're in a sensitive industry
[2344.84 → 2346.58] dealing with people's money and their finances.
[2347.38 → 2349.56] And as these technologies evolve,
[2349.66 → 2351.04] both on the capability side
[2351.04 → 2353.42] and the need for explainability,
[2353.86 → 2357.24] A, for the purpose of satisfying regulatory concerns,
[2357.52 → 2359.78] for the purposes of gaining trust
[2359.78 → 2361.26] so that you can continue to innovate
[2361.26 → 2363.16] the way that you and your team have been doing.
[2363.66 → 2365.66] How do you envision,
[2366.28 → 2367.82] you know, when you're thinking about it,
[2367.88 → 2369.98] how do you envision explainability evolving
[2369.98 → 2372.08] and the level of importance?
[2372.08 → 2373.84] Do you think we're just going to reach a level
[2373.84 → 2374.76] and it kind of plateaus
[2374.76 → 2376.42] or how does that weave its way
[2376.42 → 2379.02] through the industry over the years ahead
[2379.02 → 2380.16] in the way that you're thinking?
[2380.84 → 2382.96] Yeah, I mean, I think like where we are
[2382.96 → 2385.32] early now,
[2385.44 → 2387.58] especially in our space in Fintech,
[2387.72 → 2389.66] is just getting customers comfortable
[2389.66 → 2392.66] with having an AI system work on their behalf
[2392.66 → 2394.20] and making decisions on their behalf,
[2394.66 → 2395.82] right, on a daily basis.
[2395.82 → 2397.96] But if you look at, you know,
[2397.98 → 2399.62] some of the other areas
[2399.62 → 2400.62] where, you know,
[2400.76 → 2402.86] AI has kind of had a bit of a head start,
[2403.36 → 2405.34] people get comfortable real fast, right?
[2405.74 → 2406.44] And it's about...
[2406.44 → 2407.02] This is a good point.
[2407.04 → 2408.12] It's about building trust.
[2408.20 → 2410.20] And once they trust in the decision-making
[2410.20 → 2411.84] power of the system,
[2412.00 → 2412.88] what I've seen is
[2412.88 → 2414.96] they tend to need to know less
[2414.96 → 2416.06] about how it works
[2416.06 → 2418.98] because there's that like large baseline
[2418.98 → 2421.52] in time that they've had to build trust
[2421.52 → 2422.20] in the system.
[2422.20 → 2423.68] Yeah, it's a great insight.
[2423.86 → 2424.94] Like I expect, you know,
[2425.02 → 2426.06] in the near future
[2426.06 → 2427.56] that we'll be able to use
[2427.56 → 2429.36] much more sophisticated techniques
[2429.36 → 2431.46] because we've built up that trust.
[2431.70 → 2433.28] But, you know, trust takes time
[2433.28 → 2434.34] and it's very easy
[2434.34 → 2436.20] to violate that trust as well.
[2436.28 → 2437.68] So you have to be fairly careful
[2437.68 → 2439.60] and make sure like you bring
[2439.60 → 2440.80] your customers along.
[2441.10 → 2442.64] But, you know, sometimes also
[2442.64 → 2444.70] you just need to push it through
[2444.70 → 2446.00] because, you know,
[2446.12 → 2447.90] folks don't like change, right?
[2448.20 → 2449.28] So there's that balance.
[2449.72 → 2450.68] As a quick follow-up,
[2450.84 → 2452.08] you know, when you were just talking
[2452.08 → 2453.26] about folks liking change,
[2453.78 → 2455.02] you know, you've made these innovations
[2455.02 → 2455.92] that you've talked about
[2455.92 → 2458.10] through the COVID period
[2458.10 → 2459.62] because your customers
[2459.62 → 2462.00] really needed you to do that and stuff.
[2462.14 → 2463.14] And I guess, you know,
[2463.16 → 2464.28] there's that old saying about
[2464.28 → 2465.30] don't let a good crisis
[2465.30 → 2466.36] go to waste and all.
[2466.44 → 2467.92] And I realized that the sentiment
[2467.92 → 2469.24] on that is probably not appropriate
[2469.24 → 2470.04] for the COVID time.
[2470.06 → 2472.24] And I'm trying to acknowledge that.
[2472.38 → 2473.66] But at the same time,
[2473.98 → 2475.74] it's during times of change
[2475.74 → 2477.10] that great things can really
[2477.10 → 2478.32] come about and happen.
[2478.52 → 2480.62] As you're thinking about that
[2480.62 → 2482.80] and knowing that that is necessary
[2482.80 → 2483.86] and the explainability
[2483.86 → 2486.26] can be achieved to some degree,
[2486.38 → 2487.50] gain that trust and do that.
[2487.80 → 2488.66] How might that,
[2488.78 → 2490.58] as you have amazing tools
[2490.58 → 2491.80] going forward in the years ahead
[2491.80 → 2492.62] that are being developed,
[2493.00 → 2493.96] deep learning goes farther,
[2494.10 → 2494.56] reinforcement,
[2494.74 → 2495.80] other branches
[2495.80 → 2496.92] that we don't yet know about
[2496.92 → 2497.70] that could come about
[2497.70 → 2498.26] at some point
[2498.26 → 2499.52] from current research.
[2499.68 → 2500.84] How might you approach
[2500.84 → 2502.10] some of those in terms of,
[2502.40 → 2502.52] you know,
[2502.56 → 2503.46] how do you make that judgment
[2503.46 → 2505.10] on now's the time to push
[2505.10 → 2506.96] because they really need it
[2506.96 → 2508.46] and I can really help them
[2508.46 → 2509.84] and I know that they'll trust it quickly
[2509.84 → 2511.56] versus being more conservative
[2511.56 → 2512.10] and saying,
[2512.20 → 2512.94] you know,
[2513.16 → 2513.86] I'm afraid to.
[2514.24 → 2515.12] How do you assess that?
[2515.34 → 2515.52] Yeah,
[2515.70 → 2517.58] I would say just A-B test it,
[2517.66 → 2517.80] right?
[2517.92 → 2519.10] A small A-B test
[2519.10 → 2521.18] costs very little,
[2521.50 → 2521.72] right?
[2522.10 → 2523.06] And there are certain
[2523.06 → 2524.68] portions of the population
[2524.68 → 2526.84] who are okay with it,
[2527.16 → 2527.28] right?
[2527.32 → 2528.48] So doing a random test
[2528.48 → 2529.40] with a small population
[2529.40 → 2530.84] on a very bold idea
[2530.84 → 2532.06] that pushes it far ahead,
[2532.60 → 2533.42] you might get actually
[2533.42 → 2533.76] really,
[2533.92 → 2534.72] really great results
[2534.72 → 2535.44] and then you can kind of
[2535.44 → 2536.54] step your way up
[2536.54 → 2538.06] into opening up more.
[2538.06 → 2539.24] is how I would,
[2539.38 → 2539.62] you know,
[2539.66 → 2540.70] think about approaching it
[2540.70 → 2541.52] because like,
[2541.72 → 2542.44] I can tell you,
[2542.56 → 2544.38] this population we serve
[2544.38 → 2545.46] for some of our products
[2545.46 → 2546.24] with accountants,
[2546.62 → 2548.14] they're not necessarily,
[2548.60 → 2548.96] you know,
[2549.24 → 2550.60] the most open
[2550.60 → 2551.68] to trying out
[2551.68 → 2552.62] new technologies
[2552.62 → 2553.32] at all.
[2553.84 → 2554.22] But,
[2554.34 → 2555.02] you know,
[2555.04 → 2555.58] if you go through
[2555.58 → 2556.52] just with an A-B test
[2556.52 → 2556.94] and test
[2556.94 → 2558.66] without them really knowing it,
[2558.70 → 2558.86] right,
[2558.86 → 2559.64] then you really get
[2559.64 → 2560.92] the true reaction
[2560.92 → 2562.74] and then you can actually
[2562.74 → 2563.94] start like bringing
[2563.94 → 2564.74] the people along
[2564.74 → 2565.74] as you have that data
[2565.74 → 2566.40] and that evidence.
[2566.70 → 2566.84] Gotcha.
[2566.84 → 2567.70] Chris knows
[2567.70 → 2569.48] I'm always the one
[2569.48 → 2570.68] like asking
[2570.68 → 2571.84] super selfish
[2571.84 → 2572.98] practical questions
[2572.98 → 2574.52] because I always struggle
[2574.52 → 2576.00] to do practical things myself
[2576.00 → 2576.96] and I want to make sure
[2576.96 → 2578.06] I know there's people,
[2578.24 → 2578.88] listeners out there
[2578.88 → 2580.20] that are all the time
[2580.20 → 2580.62] thinking about
[2580.62 → 2582.54] practical data science things
[2582.54 → 2584.08] and I notice
[2584.08 → 2584.94] in reading about
[2584.94 → 2585.54] some of your work
[2585.54 → 2586.22] you're talking about
[2586.22 → 2586.84] having,
[2586.98 → 2587.68] you know,
[2588.28 → 2589.22] individual models
[2589.22 → 2589.90] for different
[2589.90 → 2591.34] transaction streams
[2591.34 → 2592.90] and combining,
[2593.08 → 2593.28] you know,
[2593.32 → 2594.66] aggregating those together
[2594.66 → 2595.92] and I'm just thinking
[2595.92 → 2596.78] as like
[2596.78 → 2598.30] in a practical sense
[2598.30 → 2598.84] you've got,
[2598.96 → 2599.66] you know,
[2600.16 → 2602.52] models per transaction stream
[2602.52 → 2604.16] per user
[2604.16 → 2604.54] and,
[2604.78 → 2604.86] you know,
[2604.92 → 2605.68] how many users
[2605.68 → 2607.36] does QuickBooks have?
[2607.62 → 2608.18] My question,
[2608.28 → 2608.64] I guess,
[2608.64 → 2609.16] is like
[2609.16 → 2609.80] when you're dealing
[2609.80 → 2611.12] with this many models
[2611.12 → 2613.68] and this many predictions,
[2613.68 → 2615.70] do you have any
[2615.70 → 2618.30] sort of practical advice
[2618.30 → 2620.16] for in terms of
[2620.16 → 2621.14] model management
[2621.14 → 2623.88] and like model debugging
[2623.88 → 2625.22] and that sort of things,
[2625.40 → 2625.88] you know,
[2625.98 → 2627.00] I think a lot of people
[2627.00 → 2628.30] can sometimes
[2628.30 → 2628.90] get something
[2628.90 → 2629.90] into production
[2629.90 → 2631.18] but then managing it
[2631.18 → 2631.84] after that,
[2631.92 → 2632.62] especially when you're
[2632.62 → 2633.18] managing it
[2633.18 → 2634.18] for multiple customers
[2634.18 → 2635.26] becomes really difficult.
[2635.54 → 2637.60] So any practical advice
[2637.60 → 2638.14] on that front?
[2638.32 → 2638.54] Yeah.
[2639.12 → 2639.60] Oh man,
[2639.60 → 2644.10] the operational component
[2644.10 → 2644.68] of,
[2644.82 → 2644.92] you know,
[2644.94 → 2646.42] the work that we do
[2646.42 → 2648.32] cannot be understated,
[2648.62 → 2648.90] right?
[2648.98 → 2650.04] Because it's not just
[2650.04 → 2651.24] about building the model,
[2651.40 → 2652.22] it's actually taking
[2652.22 → 2652.86] to production,
[2653.02 → 2654.28] dealing with the ETL,
[2654.38 → 2655.32] grabbing the data,
[2655.64 → 2656.80] serving the customers.
[2657.24 → 2658.02] So you need to
[2658.02 → 2658.78] really make sure
[2658.78 → 2659.56] that you have
[2659.56 → 2661.22] fairly robust monitoring
[2661.22 → 2662.02] in
[2662.02 → 2663.38] so that you can
[2663.38 → 2664.60] be proactively alerted
[2665.16 → 2666.68] if something goes wrong
[2666.68 → 2668.00] because the worst case scenario
[2668.00 → 2669.32] would be a customer
[2669.32 → 2670.20] contacting you
[2670.20 → 2670.60] and saying,
[2670.74 → 2670.86] hey,
[2671.48 → 2672.72] you totally messed up
[2672.72 → 2673.60] my cash flow,
[2673.94 → 2674.98] now I can't pay
[2674.98 → 2675.94] a vendor this month,
[2676.00 → 2676.12] right?
[2676.16 → 2677.38] That would be disastrous.
[2678.18 → 2679.12] And so building
[2679.12 → 2680.52] and monitoring,
[2681.20 → 2682.60] but you can't,
[2682.60 → 2682.88] you know,
[2682.98 → 2683.92] feasibly monitor
[2683.92 → 2684.78] for every event
[2684.78 → 2685.30] for everything.
[2685.88 → 2687.72] And so doing a sampling
[2687.72 → 2688.38] and monitoring
[2688.38 → 2688.94] along the way.
[2689.16 → 2690.22] I will also just
[2690.22 → 2690.94] put in a plug
[2690.94 → 2691.58] which is that
[2691.58 → 2692.48] when you're building,
[2692.78 → 2693.82] for us, we have,
[2693.90 → 2694.26] you know,
[2694.72 → 2695.92] 3 million customers
[2695.92 → 2696.84] in the US alone
[2696.84 → 2697.50] for QuickBooks
[2697.50 → 2698.26] and then multiple
[2698.26 → 2699.12] transaction stream,
[2699.22 → 2700.36] grabbing in all that data.
[2700.74 → 2701.86] We quickly get into
[2701.86 → 2702.82] the realm of,
[2702.90 → 2703.16] you know,
[2703.24 → 2704.28] like over 10 million
[2704.28 → 2706.70] models being built
[2706.70 → 2707.22] and served.
[2707.64 → 2709.18] Start in batch mode,
[2709.24 → 2709.40] right?
[2709.42 → 2709.96] There's this like
[2709.96 → 2711.20] obsession with building
[2711.20 → 2712.44] models in real time
[2712.44 → 2713.14] for everything.
[2713.62 → 2714.64] Like every single team
[2714.64 → 2715.08] I talk to,
[2715.12 → 2715.34] they're like,
[2715.42 → 2715.90] when am I going to get
[2715.90 → 2716.62] the model in real time?
[2716.80 → 2717.10] Well,
[2717.18 → 2717.98] let's start with batch,
[2718.08 → 2718.24] right?
[2718.34 → 2719.00] The complexity
[2719.00 → 2720.20] for a batch model
[2720.20 → 2721.08] is just much easier
[2721.08 → 2721.66] to handle.
[2722.22 → 2723.28] You validate your hypothesis,
[2723.48 → 2724.52] you validate the use case,
[2724.84 → 2726.14] and then you can say,
[2726.24 → 2726.44] you know,
[2726.44 → 2727.76] is the ROI enough
[2727.76 → 2729.14] if we move it
[2729.14 → 2729.92] to real time?
[2730.42 → 2731.22] That's one area.
[2731.46 → 2732.04] There's also,
[2732.18 → 2733.14] the thing that we've made
[2733.14 → 2733.88] an investment in
[2733.88 → 2734.84] that has really helped
[2734.84 → 2736.86] is investing in a robust
[2736.86 → 2738.02] machine learning platform
[2738.02 → 2739.28] that allows us
[2739.28 → 2740.64] to do distributed training
[2740.64 → 2742.12] and distributed scoring.
[2742.64 → 2743.28] So marrying,
[2743.50 → 2743.80] you know,
[2743.84 → 2744.92] the best of,
[2744.98 → 2746.12] essentially,
[2746.24 → 2747.34] the Map Reduce framework,
[2747.62 → 2747.90] right?
[2748.44 → 2749.18] And doing that
[2749.18 → 2750.06] distributed computing
[2750.06 → 2751.22] with our models.
[2751.22 → 2752.36] And the Cashflow
[2752.36 → 2753.48] is not the only
[2753.48 → 2754.42] use case
[2754.42 → 2755.10] where we have
[2755.10 → 2756.06] individual models
[2756.06 → 2756.88] for users.
[2757.42 → 2759.00] For transaction categorization,
[2759.40 → 2760.42] which is where
[2760.42 → 2761.82] any transaction comes in,
[2762.26 → 2762.84] we figure out
[2762.84 → 2763.72] which accounting books
[2763.72 → 2764.54] it goes into.
[2765.18 → 2766.46] We have individual models
[2766.46 → 2767.40] serving in real time
[2767.40 → 2767.90] for customers
[2767.90 → 2768.88] in that case as well.
[2769.00 → 2769.26] But,
[2769.36 → 2769.52] you know,
[2769.56 → 2770.70] you also have to figure out,
[2770.76 → 2770.94] like,
[2771.02 → 2772.54] when is the scenario
[2772.54 → 2773.32] where you actually want
[2773.32 → 2774.12] to get to that level
[2774.12 → 2774.74] of complexity?
[2775.28 → 2776.04] So for us,
[2776.04 → 2776.88] we always start
[2776.88 → 2778.54] with one base vanilla model
[2778.54 → 2779.26] for everyone
[2779.26 → 2780.80] to start with
[2780.80 → 2782.04] and then see
[2782.04 → 2782.86] how far we get.
[2783.06 → 2783.86] And then we figure out,
[2783.98 → 2784.08] okay,
[2784.10 → 2785.26] how do we blow this up
[2785.26 → 2786.04] in terms of scale
[2786.04 → 2786.68] and complexity
[2786.68 → 2788.64] and how much headroom
[2788.64 → 2789.18] is there
[2789.18 → 2789.94] in order to solve
[2789.94 → 2790.84] the problem well?
[2791.56 → 2792.28] You said something
[2792.28 → 2792.84] as you were going
[2792.84 → 2793.26] through there
[2793.26 → 2794.62] that grabbed my attention
[2794.62 → 2795.18] as well
[2795.18 → 2796.14] as you were going.
[2796.72 → 2797.20] And that was,
[2797.28 → 2798.38] you talked about platform.
[2798.62 → 2799.54] And you can answer
[2799.54 → 2800.28] this one any way
[2800.28 → 2800.74] that you want
[2800.74 → 2801.68] because not every company
[2801.68 → 2802.48] wants to talk about
[2802.48 → 2803.36] the details of
[2803.36 → 2804.10] their infrastructure
[2804.10 → 2804.74] and stuff like that
[2804.74 → 2805.56] and I totally get that.
[2805.96 → 2806.90] But how do you
[2806.90 → 2807.76] approach platform
[2807.76 → 2808.50] because that is
[2808.50 → 2809.42] one of those
[2809.42 → 2810.66] practical questions
[2810.66 → 2811.62] for practical AI
[2811.62 → 2812.68] that everybody
[2812.68 → 2813.94] has to contend with.
[2814.30 → 2815.82] And we often ask guests
[2815.82 → 2817.42] how their organization
[2817.42 → 2818.40] is tackling that.
[2818.48 → 2819.76] So I'd love to hear
[2819.76 → 2820.82] how Intuit
[2820.82 → 2822.20] is approaching
[2822.20 → 2823.42] a data science
[2823.42 → 2824.38] and AI platform
[2824.38 → 2825.94] and what that means
[2825.94 → 2826.30] to you
[2826.30 → 2826.74] because it means
[2826.74 → 2827.28] different things
[2827.28 → 2828.00] to different people.
[2828.26 → 2828.36] Yeah,
[2828.50 → 2829.68] so I've been at Intuit
[2829.68 → 2831.04] for long enough
[2831.04 → 2832.36] where I've lived
[2832.36 → 2833.02] in the world
[2833.02 → 2834.16] before we invested
[2834.16 → 2834.88] in the platform
[2834.88 → 2835.56] and the world
[2835.56 → 2837.02] after we invested
[2837.02 → 2837.70] in the platform.
[2837.76 → 2839.82] And I can tell you
[2839.82 → 2840.52] that like,
[2840.60 → 2840.74] you know,
[2840.78 → 2841.20] for us,
[2841.34 → 2841.90] a platform
[2841.90 → 2842.80] should enable
[2842.80 → 2844.12] us to be able
[2844.12 → 2845.30] to ship machine
[2845.30 → 2846.00] learning models
[2846.00 → 2847.20] that are high quality
[2847.20 → 2848.48] that have scale
[2848.48 → 2849.92] built in faster.
[2850.24 → 2851.56] So those are essentially
[2851.56 → 2852.08] kind of like
[2852.08 → 2852.82] the requirements
[2852.82 → 2854.06] of what a great platform
[2854.06 → 2854.64] would be able
[2854.64 → 2855.60] to allow you
[2855.60 → 2856.44] to do essentially.
[2857.16 → 2858.34] And so our platform
[2858.34 → 2859.50] solves for
[2859.50 → 2860.42] being able
[2860.42 → 2861.44] to deploy models
[2861.44 → 2861.90] quickly,
[2862.60 → 2863.30] train models
[2863.30 → 2864.50] consistently
[2864.50 → 2866.30] and then monitor
[2866.30 → 2867.04] the performance
[2867.04 → 2867.82] of those models
[2867.82 → 2868.54] when they go out
[2868.54 → 2868.92] the door.
[2869.48 → 2870.98] And you can find
[2870.98 → 2871.30] this,
[2871.64 → 2871.80] you know,
[2871.84 → 2872.78] we have the
[2872.78 → 2873.62] close collaboration
[2873.62 → 2874.40] with AWS
[2874.40 → 2875.86] and underneath
[2875.86 → 2876.88] we use SageMaker
[2876.88 → 2877.92] as one of the
[2877.92 → 2878.52] core components
[2878.52 → 2879.34] of our platforms.
[2880.14 → 2881.18] Different companies
[2881.18 → 2882.02] have a build
[2882.02 → 2882.88] versus buy.
[2883.12 → 2883.54] In our case,
[2883.58 → 2884.12] we partner
[2884.12 → 2886.14] specifically for this.
[2886.34 → 2886.50] But,
[2886.86 → 2887.00] you know,
[2887.04 → 2887.52] for me,
[2887.66 → 2887.94] like,
[2888.04 → 2888.92] as a data scientist,
[2889.24 → 2889.46] like,
[2889.76 → 2890.30] what I want
[2890.30 → 2891.08] out of a platform
[2891.08 → 2892.00] is to make
[2892.00 → 2893.54] the job
[2893.54 → 2893.98] of actually
[2893.98 → 2894.96] the maintenance
[2894.96 → 2895.94] of monitoring,
[2896.50 → 2897.72] the scaling easy
[2897.72 → 2898.70] so I can focus
[2898.70 → 2899.44] on the algorithms.
[2899.80 → 2900.28] That's,
[2900.52 → 2900.90] you know,
[2900.98 → 2902.34] what we've optimized for.
[2902.86 → 2903.02] Awesome.
[2903.58 → 2905.14] So at the beginning
[2905.14 → 2906.42] of our conversation,
[2906.42 → 2907.22] you mentioned
[2907.22 → 2907.88] how
[2907.88 → 2909.26] your
[2909.26 → 2910.10] engagement
[2910.10 → 2911.12] with Intuit
[2911.12 → 2911.92] really started
[2911.92 → 2913.24] from a felt need
[2913.24 → 2913.96] that you had
[2913.96 → 2914.76] and a problem
[2914.76 → 2915.44] that you saw
[2915.44 → 2915.88] and you brought
[2915.88 → 2916.44] that problem
[2916.44 → 2916.94] to Intuit.
[2917.18 → 2918.12] As we kind of
[2918.12 → 2918.82] close out here,
[2918.86 → 2919.34] I'm wondering
[2919.34 → 2919.92] as you look
[2919.92 → 2920.64] to the future
[2920.64 → 2921.74] what are those
[2921.74 → 2922.68] things in your mind
[2922.68 → 2923.06] like,
[2923.48 → 2923.64] oh,
[2923.74 → 2924.94] I really like
[2924.94 → 2926.08] I see this problem
[2926.08 → 2927.18] and I really think
[2927.18 → 2928.44] AI or data science
[2928.44 → 2929.40] has a great solution
[2929.40 → 2929.76] for it.
[2929.78 → 2930.40] I just haven't
[2930.40 → 2931.36] haven't done it yet.
[2931.48 → 2932.30] Or maybe it's
[2932.30 → 2932.98] things out there
[2932.98 → 2933.70] that you just
[2933.70 → 2934.48] like you're really
[2934.48 → 2935.66] excited to
[2935.66 → 2936.68] to try
[2936.68 → 2937.44] but you haven't
[2937.44 → 2938.02] tried yet.
[2938.12 → 2938.76] When you're looking
[2938.76 → 2939.42] to the future,
[2939.56 → 2940.26] what kind of
[2940.26 → 2941.62] keeps you up at night
[2941.62 → 2942.88] and runs through
[2942.88 → 2943.24] your mind?
[2943.48 → 2943.70] Yeah,
[2943.88 → 2944.22] man,
[2944.32 → 2946.04] I am constantly
[2946.04 → 2946.86] chasing,
[2947.32 → 2947.62] you know,
[2947.68 → 2948.14] for me,
[2948.28 → 2948.78] one of the
[2948.78 → 2950.04] the holy grail
[2950.04 → 2950.62] problems
[2950.62 → 2951.42] and like,
[2951.68 → 2952.28] I would be
[2952.28 → 2953.16] happy to retire
[2953.16 → 2953.64] if we could
[2953.64 → 2954.16] solve this,
[2954.36 → 2956.30] which is actually
[2956.30 → 2957.06] how do we,
[2957.22 → 2957.60] you know,
[2957.66 → 2958.52] go from the state
[2958.52 → 2959.08] right now
[2959.08 → 2960.08] where if you
[2960.08 → 2961.30] have to actually
[2961.30 → 2962.56] run your books
[2962.56 → 2963.60] right every month,
[2964.18 → 2965.14] if you're a small
[2965.14 → 2965.60] business,
[2966.40 → 2966.88] right now,
[2966.96 → 2967.58] a lot of small
[2967.58 → 2968.32] businesses are doing
[2968.32 → 2968.92] it manually.
[2968.92 → 2969.52] They're entering
[2969.52 → 2970.70] things by hand.
[2970.78 → 2971.58] They're like figuring
[2971.58 → 2973.12] out the complexity
[2973.12 → 2974.04] of accounting.
[2974.42 → 2974.60] Like,
[2974.74 → 2975.28] as we talked
[2975.28 → 2976.02] about early on,
[2976.10 → 2976.66] like a lot of
[2976.66 → 2977.20] small businesses
[2977.20 → 2978.18] don't go into the
[2978.18 → 2978.78] business of small
[2978.78 → 2979.54] business thinking
[2979.54 → 2980.24] about books,
[2980.40 → 2980.64] right?
[2980.70 → 2981.32] They think about,
[2981.46 → 2981.54] wow,
[2981.56 → 2982.22] I really want to
[2982.22 → 2982.98] do this thing,
[2983.32 → 2983.44] right?
[2983.46 → 2984.08] They don't,
[2984.20 → 2984.64] it's not,
[2984.72 → 2985.72] no one gets joy
[2985.72 → 2987.50] from doing accounting
[2987.50 → 2988.66] to say the least,
[2989.10 → 2989.28] right?
[2989.38 → 2990.46] But it's a really
[2990.46 → 2991.84] difficult problem,
[2992.08 → 2992.36] right?
[2992.52 → 2993.66] To go from
[2993.66 → 2996.08] raw transaction data
[2996.08 → 2997.28] to a state where
[2997.28 → 2998.10] we can actually tell
[2998.10 → 2998.44] you,
[2998.56 → 2999.56] this is what your
[2999.56 → 3000.10] books are like,
[3000.16 → 3001.10] this is your cash flow,
[3001.26 → 3002.46] this is how much
[3002.46 → 3003.64] taxes are owed,
[3003.80 → 3004.56] and this is how you
[3004.56 → 3005.04] should run your
[3005.04 → 3005.40] payroll.
[3005.40 → 3006.42] So for me,
[3006.52 → 3007.34] like I'm always
[3007.34 → 3008.76] chasing after how
[3008.76 → 3009.56] could we actually
[3009.56 → 3011.18] fully automate the
[3011.18 → 3012.06] entire accounting
[3012.06 → 3013.52] process for our
[3013.52 → 3014.14] customers so that
[3014.14 → 3014.60] they can actually
[3014.60 → 3015.68] spend time doing
[3015.68 → 3016.20] the things they
[3016.20 → 3016.52] like,
[3016.70 → 3017.42] and we can have
[3017.42 → 3017.76] the machine
[3017.76 → 3018.68] learning solve
[3018.68 → 3019.68] this problem.
[3020.36 → 3021.52] And it's really
[3021.52 → 3022.20] difficult because
[3022.20 → 3023.72] it's so multifaceted,
[3024.10 → 3024.28] right?
[3024.74 → 3025.84] And that's where,
[3025.96 → 3026.28] you know,
[3026.32 → 3026.86] in the future,
[3026.92 → 3027.66] we're really going
[3027.66 → 3028.20] to be,
[3028.20 → 3028.52] you know,
[3028.58 → 3029.58] innovating quite a
[3029.58 → 3029.82] bit,
[3029.92 → 3030.84] both on the
[3030.84 → 3031.88] algorithmic side,
[3031.88 → 3034.28] but also on
[3034.28 → 3035.36] potentially making
[3035.36 → 3036.00] fairly major
[3036.00 → 3036.76] changes to our
[3036.76 → 3038.02] product to get,
[3038.16 → 3038.68] you know,
[3038.76 → 3039.68] folks comfortable
[3039.68 → 3040.28] with this.
[3040.64 → 3041.62] So I'm super
[3041.62 → 3042.72] jazzed about that.
[3043.06 → 3043.76] I know not every
[3043.76 → 3044.76] kid grows up saying,
[3044.88 → 3045.10] you know,
[3045.10 → 3045.88] I want to be an
[3045.88 → 3047.24] accountant and I
[3047.24 → 3047.94] want to build
[3047.94 → 3048.48] machine learning
[3048.48 → 3049.04] for accounting.
[3049.22 → 3050.10] It's such like an
[3050.10 → 3051.22] old problem,
[3051.22 → 3052.06] but it's,
[3052.14 → 3052.36] for me,
[3052.40 → 3052.94] it's a super
[3052.94 → 3053.74] exciting problem.
[3054.06 → 3054.22] You know,
[3054.28 → 3054.98] it's fascinating
[3054.98 → 3055.68] to hear you say
[3055.68 → 3056.86] that because as
[3056.86 → 3057.44] you say that,
[3057.52 → 3058.22] I'm thinking back
[3058.22 → 3058.88] to what you were
[3058.88 → 3059.40] talking about,
[3059.44 → 3060.48] customer experience
[3060.48 → 3061.86] and holding
[3061.86 → 3062.68] that as high
[3062.68 → 3063.16] as you do,
[3063.44 → 3064.10] there is a
[3064.10 → 3065.12] self-awareness
[3065.12 → 3066.60] in you and
[3066.60 → 3067.38] your organization
[3067.38 → 3068.70] when you recognize
[3068.70 → 3069.70] that while your
[3069.70 → 3071.20] product is doing
[3071.20 → 3072.20] great things for
[3072.20 → 3072.98] someone's business,
[3072.98 → 3073.78] that's not what
[3073.78 → 3074.34] they want to be
[3074.34 → 3074.88] thinking about.
[3074.98 → 3075.42] That's what they
[3075.42 → 3076.08] want you to handle.
[3076.42 → 3077.06] So you're basically
[3077.06 → 3078.34] saying the highest
[3078.34 → 3079.38] thing is for them
[3079.38 → 3079.84] not to have to
[3079.84 → 3080.46] worry about us at
[3080.46 → 3080.56] all.
[3080.64 → 3081.18] We're just there
[3081.18 → 3082.10] doing the magic,
[3082.28 → 3083.30] but they never
[3083.30 → 3083.90] have to deal with
[3083.90 → 3084.16] us.
[3084.40 → 3085.04] And that is almost
[3085.04 → 3085.96] like perfect
[3085.96 → 3086.96] customer experience
[3086.96 → 3087.46] when you think
[3087.46 → 3088.04] about it because
[3088.04 → 3088.90] you're optimizing
[3088.90 → 3090.20] their own experience
[3090.20 → 3090.84] so they can do
[3090.84 → 3091.52] the thing they love.
[3091.52 → 3092.22] I loved hearing
[3092.22 → 3092.68] that answer.
[3092.92 → 3093.66] I've learned a lot
[3093.66 → 3094.54] in this and I
[3094.54 → 3095.46] think that I really
[3095.46 → 3096.30] appreciate the
[3096.30 → 3097.98] insights and thank
[3097.98 → 3098.54] you so much,
[3098.66 → 3099.40] Sung, for joining
[3099.40 → 3099.74] us.
[3099.90 → 3100.46] As I mentioned,
[3100.68 → 3101.60] I'll point our
[3101.60 → 3102.56] listeners to some
[3102.56 → 3103.86] links in the
[3103.86 → 3105.16] description, so make
[3105.16 → 3105.90] sure you check those
[3105.90 → 3107.76] things out and check
[3107.76 → 3109.14] out what Intuit is
[3109.14 → 3110.10] doing in this space.
[3110.26 → 3110.94] But really appreciate
[3110.94 → 3111.74] you taking time.
[3111.82 → 3112.42] It's great to talk
[3112.42 → 3112.82] to you, Sung.
[3113.02 → 3113.66] Thank you for
[3113.66 → 3114.40] having me, guys.
[3114.40 → 3118.64] Thank you for
[3118.64 → 3119.24] listening to
[3119.24 → 3119.92] Practical AI.
[3120.26 → 3120.80] We appreciate
[3120.80 → 3121.80] your time and
[3121.80 → 3122.26] your attention.
[3122.62 → 3123.28] Follow the show
[3123.28 → 3124.72] on Apple Podcasts,
[3124.78 → 3125.96] Spotify, or your
[3125.96 → 3126.96] favourite podcast app.
[3127.22 → 3128.26] Your neural networks
[3128.26 → 3128.80] will thank you.
[3129.24 → 3130.28] We are also on the
[3130.28 → 3130.90] web at
[3130.90 → 3132.50] PracticalAI.fm.
[3132.78 → 3133.46] There you'll find
[3133.46 → 3134.52] recommended episodes,
[3134.88 → 3135.64] listener favourites,
[3135.86 → 3136.96] and a free sign-up
[3136.96 → 3137.70] to join the community.
[3138.32 → 3139.44] Practical AI is
[3139.44 → 3140.18] hosted by Chris
[3140.18 → 3141.28] Benson and Daniel
[3141.28 → 3141.74] Whiten ack.
[3141.74 → 3142.68] It's produced by
[3142.68 → 3143.88] Jared Santo with
[3143.88 → 3145.08] music by Break master
[3145.08 → 3145.50] Cylinder.
[3145.86 → 3146.54] Thanks again to our
[3146.54 → 3147.62] sponsors, Vastly,
[3147.76 → 3149.08] Linde, and Launch Darkly.
[3149.24 → 3150.04] That's our show.
[3150.46 → 3151.44] We hope you enjoyed it
[3151.44 → 3152.26] and we'll talk to you
[3152.26 → 3153.18] again next week.
[3172.08 → 3175.88] This is DC...
[3175.88 → 3177.46] Game on.
