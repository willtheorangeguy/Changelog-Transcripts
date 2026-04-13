[0.00 → 10.78] Welcome back, everybody.
[10.92 → 11.88] This is The Change Log.
[12.04 → 16.48] We're a member-supported blog, podcast, and weekly email that covers what's fresh and new in open source.
[17.04 → 22.40] You can check out the blog at thechangelog.com, our past shows at 5by5.tv slash changelog,
[22.52 → 27.60] and subscribe to The Change Log Weekly, our weekly email covering everything that hits our radar in open source.
[27.60 → 30.56] Subscribe at thechangelog.com slash weekly.
[30.80 → 34.46] This show is hosted by myself, Andrew Thorpe, and Jared Santo.
[34.90 → 35.40] Say hello, Jared.
[35.88 → 36.58] Hello. How are you doing?
[37.24 → 38.00] Doing pretty good.
[38.10 → 43.54] This is the first time it'll be you and me together without Adam on the show, so we'll see how it goes.
[43.90 → 44.24] That's right.
[45.48 → 52.08] This is episode number 104, and we are joined by Gordon Williams, creator of Spring.
[52.44 → 52.98] How's it going, Gordon?
[53.70 → 54.50] Yeah, good. Thanks.
[54.50 → 59.38] Real quick, before we jump into it, I just wanted to point out that we have a sponsor for today's show.
[59.94 → 60.76] It's DigitalOcean.
[61.26 → 67.02] DigitalOcean is a simple cloud hosting provider dedicated to offering the most intuitive and easy way to spin up a cloud server.
[67.72 → 74.02] Users can create a cloud server in 55 seconds, and pricing plans start at only $5 per month for 512 legs of RAM
[74.02 → 78.56] and a 20 gigabyte SSD, one CPU, and one terabyte transfer.
[78.56 → 85.46] They feature a 99.99% uptime SLA and have data centres in New York, San Francisco, and Amsterdam.
[86.26 → 94.04] Their interface has a simple, intuitive control panel, which power users can replicate on a larger scale with their straightforward API.
[94.70 → 103.10] DigitalOcean uses KVM virtualization and additionally hosts a library of helpful walkthroughs and tutorials that cover server configuration and optimization.
[103.10 → 104.82] We have a $10 promo.
[105.02 → 110.16] When you enter your credit card info on the billing page, there's a promo code field there, and you can use the coupon code,
[110.58 → 113.58] thechangelog104, to use our $10 promo.
[113.92 → 115.70] You can check them out at digitalocean.com.
[116.24 → 118.26] Thanks so much to DigitalOcean for their support.
[119.12 → 120.36] So you do use them, Jared.
[120.42 → 120.82] Is that right?
[120.82 → 124.88] Yeah, I've been using them, I don't know, I guess since June or so.
[125.00 → 127.86] Got a few clients on VPSs there.
[127.96 → 130.90] Also have my company stuff on that as well.
[131.22 → 132.28] So I'm a big fan.
[132.28 → 138.56] Yeah, we have one of our coworkers at Pure Charity, our day job, is switching over to them.
[138.68 → 143.44] So we should see how it goes and probably get them to use the promo code to get them a little discount there.
[143.60 → 144.00] There you go.
[144.00 → 149.28] Yeah, I mean the interface is intuitive, superfast, and affordable.
[149.52 → 153.90] So I'm definitely a fan and not going to complain about – what is it, $10 off?
[154.40 → 154.88] Yeah, $10.
[154.88 → 157.82] So it starts at $5 a month.
[157.96 → 161.40] So essentially it's like two months free from what I understand, which is not bad.
[161.66 → 161.88] Right on.
[162.66 → 164.16] All right, well, let's go ahead and jump into the show.
[164.32 → 168.88] We got Gordon Williams, as I said before, and we're here to talk about Spring, JavaScript for Things.
[169.70 → 172.14] So why don't you give us a little bit of an introduction?
[172.36 → 173.64] What is Spring, Gordon?
[174.52 → 180.78] Okay, so it's basically a JavaScript interpreter that runs on very low footprint devices.
[181.82 → 188.24] So they're kind of ARM microcontrollers you get that have the RAM and Flash they need included inside them.
[189.28 → 199.00] So, you know, the normal way that you'd go about programming them is you run GCC on host computer, and then you compile it, and you send it over.
[199.00 → 207.56] But if it doesn't work, especially when you've got it in a system, and you don't have a JTAG for it, it's pretty much a black box.
[207.66 → 211.02] If it doesn't work, it's quite painful to try and figure out what's gone wrong.
[211.02 → 218.66] So Spring gives you almost like a command line interface to it where you can step through, issue commands.
[218.66 → 224.46] Yeah, and generally have a bit more fun making a project with it.
[224.82 → 227.92] You know, it may be not as capable as C++.
[228.48 → 230.48] Well, it's definitely not as capable as C++.
[230.86 → 240.30] But for, you know, for actually getting something done for Arduino style projects, it's great.
[240.64 → 242.00] It makes it a lot more enjoyable.
[242.00 → 247.28] So when did this start, the Spring, I guess, software piece?
[247.34 → 248.04] When did that come about?
[250.44 → 252.24] Probably about 18 months ago.
[253.52 → 260.68] I mean, a bit before that, I bought some of these ARM dev boards and had so much trouble getting tool chain working, especially under Linux.
[260.68 → 272.26] And it just struck me that it was absolutely crazy that you buy this board for, you know, £10 or so, and you're fighting with it.
[272.30 → 276.14] And by the time you get to flash an LED on it off, you're so bored, you just put it away again.
[276.14 → 295.18] So, yeah, I developed a JavaScript interpreter called Tiny JS, which was just a single file JavaScript interpreter, which I used in a music visualizer that I sell as kind of half a day job.
[296.26 → 302.26] And I thought I could more or less shove that into one of these microcontrollers and see what happened.
[302.26 → 308.76] So that's what I spent the kind of the next year or so trying to get working properly.
[310.46 → 310.86] Gotcha.
[311.04 → 315.04] So you at some point decided to start up a Kickstarter project.
[316.12 → 321.10] And obviously that meant that you needed some funding to get some part of this done.
[321.20 → 326.82] So where did you decide on the Kickstarter, you know, I guess, method of trying to raise funding?
[326.82 → 331.36] And what point in the project did you decide, I need funding to do X?
[332.26 → 340.08] OK, well, I mean, I've had the software actually available on the site, and it was actually closed.
[340.68 → 345.48] And what I was finding out was that it really wasn't doing what I wanted it to do.
[347.04 → 356.32] You know, generally the only people that would get to try it out were people who were already pretty experienced in embedded stuff because they'd have to get it.
[356.32 → 362.30] They'd have to figure out how to flash the board that they just bought and then put the software on and all the rest of it.
[362.82 → 366.68] So I really wanted like a sort of plug and play situation solution to it.
[366.68 → 378.66] And it just, the other thing is, you know, almost the immediate question is, well, I've got some JavaScript, but actually I want to interface it to this specific library that I've got in C or C++.
[379.60 → 384.12] You know, basically people just want to look inside, see how it works and fiddle with it.
[384.12 → 393.86] And open source is, you know, it's going to be a really nice way of working.
[394.12 → 397.72] Everyone hopefully will be able to see it, play with it, do what they want.
[398.24 → 408.50] But hopefully, again, the people who are maybe more interested in just getting started will just buy the hardware from Kickstarter, and it'll support, you know, the work on it.
[408.50 → 412.66] So the Kickstarter part of this was kind of for creating the actual hardware?
[413.82 → 414.16] Yes.
[414.36 → 415.30] Yeah, pretty much.
[416.34 → 421.04] I mean, just a way that you can take it, you can plug it in, and it'll work straight away.
[421.26 → 423.40] You know, no software or anything to install.
[423.92 → 424.22] Right.
[424.50 → 427.72] So I guess that kind of brings up an interesting question.
[427.84 → 432.78] So this is called, and the Kickstarter project is Spring JavaScript for Things.
[432.78 → 438.26] And you said, obviously, Spring, it's kind of Arduino style of stuff.
[438.38 → 444.66] But you said that the problem was people are coming with their own boards and trying to figure out how to get it up and running.
[444.74 → 447.40] So it was really just, it was like experts that wanted to fiddle.
[447.90 → 451.98] And you decided to say, we are going to kind of do both sides of this thing.
[452.02 → 454.30] We're going to do the software side, and we're going to do the hardware side.
[454.40 → 458.58] That way, when somebody gets this project, it will require very little setup.
[458.70 → 459.04] Is that right?
[459.12 → 460.08] And they'll just be able to go?
[461.40 → 461.74] Yes.
[461.74 → 462.10] Yeah.
[462.28 → 472.10] I mean, so, you know, it will still be available because it's open source, and it's quite easy to recompile it to run on different devices.
[472.48 → 481.20] So I'm hoping that you're going to get a group of people who'll run it on whatever they found and port it to all kinds of different stuff.
[481.20 → 494.84] But then you'll get the people who are, who I guess it's aimed at mainly, which is people who just want to get stuff done very quickly or want to just want to get started with it.
[494.84 → 504.14] Maybe sort of web developers or something who know JavaScript but don't really want to take the plunge to learn C and embedded software at the same time.
[504.14 → 512.08] Was the choice to go with JavaScript that just because so many people already know it or because it's a good language?
[512.50 → 514.34] Explain your decision-making with JavaScript.
[514.34 → 516.34] A little.
[516.34 → 516.70] A little.
[516.70 → 523.32] So part of me wanted effectively like a C interpreter.
[523.32 → 532.68] Something that the language looked a lot like C but that you could add stuff to data structures kind of in real time.
[532.78 → 536.48] You could change code without resetting, stuff like that.
[536.48 → 544.50] And I really didn't want to end up with some other language that wasn't standard that people had to learn.
[545.52 → 560.58] And when you think of that, there aren't actually JavaScript's kind of the obvious fit for something that the same kind of pattern as C with curly braces and plus equals and for loops done pretty much the same way.
[560.58 → 567.56] You mentioned on the Kickstarter that the event-based programming of JavaScript is also an advantage.
[567.66 → 568.40] Can you speak to that?
[569.46 → 569.68] Yeah.
[570.02 → 579.86] So I mean that – I can't say that was actually something I considered at the start but like as I started implementing it, it just made a massive amount of sense.
[579.86 → 592.02] It's that because you've got the events handled by the interpreter, you know – you basically – you know when you're idle completely, and you know when you're supposed to wake up.
[592.12 → 597.22] You either wake up because of some external event or you wake up because of some time mess.
[597.28 → 603.02] So it can put itself into really deep sleep modes which makes it really, perfect for battery-powered stuff.
[603.02 → 609.46] So I think we need to get into what Spring is and kind of the use cases.
[609.64 → 627.92] But when I look at the Kickstarter project, and we can talk a little bit more about this later, the thing that jumps out to me and I think this is true of most projects that are successful is that you wanted a – you had a 20,000-pound goal, and you were already at almost 58,000 pounds of pledges.
[627.92 → 632.30] So kind of speak a little bit to that kind of – I don't know.
[632.36 → 641.52] Does that say to you that this is something that is desperately needed or do people just think this is a cool idea or, you know, what did that response tell you when you kind of launched this thing?
[644.92 → 645.62] I don't know.
[645.62 → 659.76] Well, I mean, I think there's definitely a lot of people think it's a very cool thing, and I've heard, you know, repeatedly that people, you know, people who do JavaScript for their day job just want to kind of pick it up and run with it.
[661.20 → 672.40] There's also quite a lot of interest from the schools because there's a graphical programming language that's kind of Google Blocky, which, you know, it'll just output JavaScript code directly.
[672.40 → 675.92] So that kind of bolts on top of it.
[676.60 → 687.56] But the success – yeah, I mean, I guess it obviously is something that people are interested in.
[688.06 → 692.80] I mean, there's also TESOL that's jumped up recently as well, filling a very similar kind of niche.
[693.84 → 697.12] Were you surprised at the success or do you expect to knock it out of the park?
[700.24 → 702.26] Yeah, I am quite surprised.
[702.40 → 705.98] I mean, you know, I always hoped it would do really well.
[706.30 → 711.40] But at the same time, I kind of expected it would be one of the – what are they?
[712.06 → 713.52] 60% that just bomb.
[714.64 → 723.80] So, yeah, it was really, perfect kind of setting up on the first day and just kind of watching it pick up and thinking, you know, yes, it's going to hit the target, which is great.
[723.80 → 735.44] Yeah, it's definitely something that I think JavaScript itself kind of lends itself to a – I don't know if the word is – I don't know what the right way to say it.
[735.44 → 745.12] It may be easier to pick up for somebody that doesn't – you know, that would like to get started with programming and kind of doesn't want to spend the time learning, you know, some of the heavier languages.
[745.12 → 762.34] But to me, this speaks – you obviously somehow were able to portray to a person on Kickstarter that maybe kind of wants to dabble in technology and not just want to be a hardcore programmer, how they could, you know, do something fun in their life with a language that might be easy to learn and kind of accomplish some pretty cool tasks.
[762.34 → 771.12] So the audience probably is not just programmers but also just like, you know, people that are dabbling in technology that want to kind of tinker around with this stuff.
[771.16 → 772.10] Would you agree with that?
[773.12 → 774.20] Yes, yeah, I think so.
[774.36 → 783.96] I think probably having the fact that it's actually a thing that people can kind of get their hands on really helps, I think.
[783.96 → 793.00] And it was a very conscious decision, actually, going in versus having a Kickstarter for the software.
[793.72 → 801.06] Also because it's a little hypocritical to start off with closed software and then say, I'm going to have a Kickstarter here to open source it.
[801.06 → 813.84] But I think that – yeah, I think it's been much more successful having hardware with it on that was being part of the Kickstarter rather than just having the software.
[814.68 → 815.46] Yeah, absolutely.
[815.66 → 818.66] So the – you kind of – you talked about it a little bit.
[818.74 → 821.32] You went from closed source to open source.
[821.32 → 838.32] And you – or I guess – are you – would you consider the project to be open source right now or would you say that once the Kickstarter is funded, which, by the way, just to point out, it is still available to be backed until next Saturday, September 26th.
[839.10 → 843.36] So as of right now, there's still seven days to go for the funding of this project.
[843.36 → 844.76] So it's not done yet.
[844.76 → 852.44] So anyone out there wants to kind of get in on this thing, then you can just go to Kickstarter and look for the S Perugino JavaScript for Things project and back it.
[853.26 → 855.02] Little side note, little plug for you right there.
[855.16 → 859.12] The cool thing about these hardware Kickstarter's is you're effectively buying the product, right?
[859.44 → 859.68] Right.
[859.82 → 863.48] I mean that may play into why these types of Kickstarter's are so successful.
[863.60 → 869.44] Don't necessarily want to make this a show about Kickstarter, but it's cool that you're effectively just pre-ordering one of these things.
[869.44 → 871.28] If you get to the – what is it?
[871.42 → 873.18] The third level of backing.
[873.18 → 878.36] So you had 19 Great British Pounds is essentially you're buying the board at that point.
[878.50 → 878.70] Right.
[879.14 → 881.76] So that's good, right?
[882.04 → 886.88] Where you landed with Kickstarter and you still have seven days to go with it.
[887.78 → 893.26] You would say that it's closed source right now, but you're going to open source it after this is funded?
[894.56 → 895.00] Yeah.
[895.00 → 901.88] I mean it's effectively open source unless everyone hears this show and then cancels their pledge immediately.
[901.88 → 914.44] But, you know, at the moment, you know, I've made it for the Spring board and the other few boards that are out there at the moment.
[914.76 → 918.58] And I'd quite like to tidy up my code quite a bit before I release it.
[918.58 → 926.14] Also because, you know, if people pick it up and start looking at it, and then I start changing stuff in the first few weeks after it's out, it's going to be a disaster.
[926.76 → 930.26] So I've kind of said when the Kickstarter ends, I will release it.
[930.38 → 932.66] Source will be going up, whatever state it's in.
[933.18 → 940.86] But before the Kickstarter ends, you know, it's just to give me a bit of extra time to get things sorted, really.
[940.86 → 945.38] Gotcha. So that's a unique – I don't know.
[945.56 → 947.50] That just sounds like a unique path to go.
[948.90 → 957.24] Why don't you speak a little bit to just – to me, it sounds like this is a – you know, you're able – you're very flexible, and you're kind of going with it as the –
[957.24 → 964.46] which is the crux of open source, which is what we kind of push is being flexible, be kind of the visionary of the project,
[964.46 → 968.24] but be willing to go in the direction that the community wants you to go in.
[968.24 → 975.30] And that's kind of what this seems like is that the project maintainer, you could have very well just been very proud and said,
[975.38 → 978.82] no, you're going to do exactly what I want you to do with it, and it's my way or the highway.
[979.48 → 983.80] But it seems like you're willing to mould this into kind of what the backers of this want.
[984.08 → 986.24] And is that true or –
[986.24 → 988.56] Yeah, I think so.
[989.78 → 1001.64] I mean, at the end of the day, I guess I want to try and do it in such a way that I can kind of afford to keep spending time maintaining it,
[1001.74 → 1004.40] supporting users, you know, doing all the rest of the stuff.
[1005.06 → 1010.98] Because I'm not sure if it's really in anyone's best interests if I just have to go out and get, like, a proper job.
[1011.40 → 1011.62] Right.
[1011.72 → 1014.76] And then effectively dump it.
[1014.76 → 1024.32] But, you know, it's – you know, really I want people to use it, you know, in whatever things they want.
[1024.40 → 1030.24] And it would be amazing if it got ported to a bunch of different devices and just people got to enjoy using it.
[1030.70 → 1030.82] Yeah.
[1030.82 → 1033.34] Well, let's kind of step back for a minute.
[1033.56 → 1039.88] And can you give us any examples of where this might – what the use cases for it might be?
[1040.04 → 1045.44] And, you know, what kind of real-world projects this will make sense with and maybe some that you've already kind of used it for?
[1045.44 → 1047.00] Okay.
[1047.00 → 1057.74] So, I mean, I guess a very obvious one is maybe remote sensing, remote control kind of things.
[1057.74 → 1067.92] Because it's very easy to say, you know, set interval, do this every minute, and it'll go into its kind of low-power state.
[1067.92 → 1080.00] You can be, I don't know, reading a temperature sensor and then either send it wirelessly back or something like that.
[1081.28 → 1084.54] It's very much kind of simple control things it's quite good at.
[1085.02 → 1090.04] So, I mean, the obvious one might be like a greenhouse or a plant water away.
[1090.04 → 1096.04] You know, you've got a temperature, you've got a water level, you want to kind of tweak that.
[1096.12 → 1105.14] But also it's quite nice to get in there and see maybe you've got some kind of weird cycle you've set up.
[1105.28 → 1109.58] And, you know, you want to see what the program is actually doing, what the variables are set to.
[1111.48 → 1117.40] That's somewhere where it's probably quite a lot better than a simple C program running there.
[1117.40 → 1126.54] Because otherwise you're spending half your time writing code to output the state of the program down the serial port.
[1127.36 → 1132.54] So it's essentially like almost like embedded systems that you can interact with and debug a lot easier.
[1133.20 → 1133.92] Yes, yeah.
[1136.06 → 1143.40] Yeah, it looks like a, I don't know, the problem that I see with a lot of, I don't know if I would say the problem with a lot of Kickstarter projects.
[1143.40 → 1148.00] But I think that when you, maybe you can talk about this a little bit.
[1148.08 → 1152.16] So you released it with a 20,000 pound goal.
[1152.54 → 1157.80] So you had in mind roughly how much an spring costs you to make.
[1157.96 → 1163.96] And so if you've got 20,000 pounds supported, you're going to have to make, you know, you're going to produce this many and send them out.
[1164.00 → 1166.00] And then obviously you've tripled your goal.
[1166.00 → 1176.36] So what I've noticed in the past with some Kickstarter projects is when they get well past their goal, they have a hard time fulfilling the amount of orders that came in.
[1176.46 → 1184.82] Because obviously, you know, the bandwidth might not be high enough when you hit those higher limits or those higher thresholds.
[1184.82 → 1186.46] How are you going to kind of prevent that?
[1186.64 → 1193.80] Like, how do you make sure that you, you know, you still stick to your timeline or whatever, you know, your boundary or your limitations might be?
[1194.02 → 1198.22] How do you make sure that you don't, you know, just honestly just like piss everybody off that back this thing?
[1199.28 → 1203.00] So, yeah, I mean, that's a definite problem.
[1203.00 → 1211.96] And if I was, I guess, if I was getting them, if I was like solving the components on myself, I'd suddenly have a huge problem.
[1213.30 → 1220.32] But, you know, I've, you know, I looked at a few Kickstarter's before I did this and, you know, you see people having the problem.
[1221.04 → 1225.76] And I used Seed for this, which was Seed with three Es.
[1225.90 → 1229.02] They are like a they call themselves an open hardware facilitator.
[1229.02 → 1244.32] They do sort of, I guess, sort of small to medium large runs of hardware, you know, and I doubt they're the cheapest, but they're quite, they've got quite a good reputation.
[1244.90 → 1247.44] And, you know, they can scale up quite well.
[1247.74 → 1251.62] If I'd got like a million orders or something, then they probably would have had problems.
[1251.62 → 1258.76] But I think for the moment and for what we're going to get for this campaign, it's actually going to be going to be absolutely fine.
[1258.76 → 1261.78] And they will be able to stick to the deadline.
[1262.14 → 1266.84] Probably, I'm hoping, we'll be able to get them out significantly before the deadline.
[1267.10 → 1269.98] Like, you know, two months, maybe.
[1270.42 → 1272.40] But, you know, I can't count on that.
[1273.22 → 1273.34] Yeah.
[1273.50 → 1275.40] Well, you're guaranteeing the deadline.
[1275.52 → 1277.58] So as long as you hit that, I don't think anybody will be upset.
[1277.72 → 1281.20] Because, you know, people back it assuming that that's when they're going to get it.
[1281.24 → 1282.72] So you can delight them with early.
[1282.84 → 1283.60] But, you know what I mean?
[1283.60 → 1289.12] I think, you know, not to talk negatively about other products on Kickstarter, but that's not what this show is about.
[1289.22 → 1294.22] But, you know, I've experienced when some products, they go way beyond how much they wanted to raise.
[1294.28 → 1296.72] And then it took two years to get the product.
[1296.82 → 1298.40] And it was supposed to take three months.
[1298.40 → 1304.74] And I think as long as you can kind of avoid that pitfall, which sounds like you got your ducks in a row to kind of really take care of that,
[1305.60 → 1308.82] it doesn't, you know, I don't think you're going to really make anyone too angry.
[1308.94 → 1309.56] So that's a good thing.
[1309.56 → 1311.14] No, I hope not.
[1311.26 → 1313.60] I mean, you know, that's the thing.
[1313.72 → 1321.76] It's much better being like starting off with sensible goals than coming up with a load of goals that are just going to piss people off.
[1322.32 → 1322.46] Right.
[1322.64 → 1325.62] So you can tell by your accent that you are British.
[1326.16 → 1328.86] And you're living over, I think, are you in Cambridge?
[1328.96 → 1329.34] Is that right?
[1330.88 → 1331.32] Yes.
[1331.50 → 1333.56] Just moved, actually.
[1333.80 → 1334.88] Just in the middle of moving.
[1334.88 → 1337.22] And we will end up just outside Oxford.
[1338.82 → 1341.38] So at the moment, we're unfortunately a bit between places.
[1342.04 → 1342.42] That's all right.
[1342.50 → 1348.12] So the thing I wanted to kind of ask a little bit is the last couple of shows, we've had people from all over the world.
[1348.20 → 1348.94] We've had Amsterdam.
[1349.32 → 1351.36] We've had, I can't even remember all of them.
[1351.36 → 1355.92] But what is the community like on that side of the pond?
[1356.06 → 1358.38] Or do you find most of your interaction with Americans?
[1358.82 → 1361.42] Or, you know, are you having a lot of people from the United Kingdom?
[1361.62 → 1365.02] Or what is the like, response to this like?
[1365.08 → 1369.74] And do you notice any specific, you know, areas that seem to respond a certain way?
[1369.74 → 1384.76] Well, it's kind of interesting because I think the response to Spring itself has been probably much greater in America.
[1385.00 → 1389.72] I think there's kind of more of this idea that you can kind of, you can go out and make stuff.
[1389.72 → 1403.02] And, you know, a lot of the guys I know in England who are kind of into computer software have, you know, really, really interested in it.
[1403.76 → 1409.90] But no one's really, if they're not interested in computer software, then they're not really willing to take the leap at all.
[1410.54 → 1412.28] Which is, you know, it's a bit of a shame.
[1412.28 → 1422.94] I was kind of hoping that I'd get a few more people who were, you know, just making cool hardware things and wanted to just automate them a little bit.
[1424.46 → 1427.72] But, yeah, I think more of that side is coming from the States, actually.
[1429.92 → 1436.22] So in terms of, you know, around the area, Cambridge is a really great area for tech stuff.
[1437.46 → 1438.96] There are a whole load of people there.
[1438.96 → 1444.08] Yeah, it's, I mean, it's not a huge city by any stretch of the imagination.
[1444.44 → 1447.44] But people tend to know each other.
[1447.56 → 1452.98] You always find that, you know, you know someone else by, in the kind of tech industry.
[1453.66 → 1453.84] Yeah.
[1454.94 → 1456.14] It's interesting, actually.
[1456.32 → 1457.50] Just a little quick side note.
[1457.56 → 1464.26] I went over to, and I'm very open that I absolutely, and I told you this, Gordon, that I absolutely love my time in England.
[1464.26 → 1465.88] I'm very drawn to the culture over there.
[1465.88 → 1478.40] But I went over there a few years ago, and we actually were in Cambridge, and I got in touch with Andrew and Very Pepperell, the two that kind of created Alfred app for the Mac, and sat down with them at lunch.
[1478.76 → 1482.68] They took me out to lunch and paid for it and everything, and the community was awesome over there, right?
[1482.76 → 1483.88] I just had a great time over there.
[1483.92 → 1489.22] So I can kind of agree with that, that the technology community over there I think is a real neat one.
[1489.22 → 1492.04] Yes, yeah, I think so.
[1492.70 → 1499.78] I mean, maybe that's more of a Cambridge thing than a Britain-wide thing, but definitely around there it's amazing.
[1500.04 → 1504.18] And I was very lucky to work for Calabria for a few years.
[1504.78 → 1516.46] And, yeah, I mean, everyone in there, it's, you know, you just get to realism when you're there that there are quite a lot of the cities in that area.
[1516.46 → 1517.76] And it's really exciting.
[1519.30 → 1524.56] So looping back to the use cases a little bit, I'm thinking, I'm looking at, you say it's for beginners and experts.
[1524.90 → 1526.70] I get the beginners' thing, absolutely.
[1527.06 → 1533.44] I mean, I think kids will love this kind of thing, getting them excited about programming because they have that instant feedback.
[1533.72 → 1534.78] And I think that's very cool.
[1535.12 → 1543.00] I think on the expert side of a couple of use cases, I just kind of want to throw this past you and see if this is something that you could do possibly with Esperanto.
[1543.00 → 1550.22] You mentioned that it has wireless capability, at least can hook up to some sort of wireless kit.
[1551.10 → 1551.34] Yeah.
[1551.64 → 1557.82] So it's got, the board itself has got space to plug in a little, well, to solder a Bluetooth module.
[1557.82 → 1563.76] And the Bluetooth is, it's a standard HC-05 serial port.
[1564.10 → 1573.42] So, but when you put that on, you can connect wirelessly to it, and then you can, you can program it, you can talk to it exactly as you would have done through USB.
[1575.36 → 1575.80] Cool.
[1575.80 → 1581.38] So can you, can you also either turn it into some kind of sensor or attach some sort of sensor?
[1581.74 → 1588.14] I'm thinking of like beacons that are, you know, transmitting data from, you know, their surroundings to other devices.
[1588.90 → 1590.82] Is that kind of stuff possible or am I?
[1591.02 → 1591.88] Yeah, absolutely.
[1591.88 → 1607.86] I mean, it's, in terms of, if you have something that, in fact, you can, yeah, if you connect to it via Bluetooth with your phone, you can have it, you know, just send you whatever information is gathered.
[1608.18 → 1615.82] And of course, because it's JavaScript, you just, you stick everything into an object, and then you just serialize it into JSON and just print it out.
[1615.82 → 1623.50] So the Wi-Fi capabilities, is that one of your stretch goals was the Wi-Fi?
[1624.30 → 1624.82] Yeah, yeah.
[1624.92 → 1626.14] And that's, that's now been hit.
[1626.70 → 1631.10] So I'm going to have to start work on that a bit more heavily.
[1631.24 → 1644.30] I mean, we've got, at the moment, it's got a Node.js style HTTP server and client, but they only work when it's compiled onto Linux.
[1644.30 → 1650.30] So you can, it runs on Carambola quite nicely or Raspberry Pi, stuff like that.
[1650.70 → 1650.82] Right.
[1650.86 → 1658.30] So I can get a good idea of what it's like, but it's going to be much, much better when it's on, you know, on this small low power chip.
[1658.72 → 1664.96] And then you can kind of, you can have it running just off battery power, you know, running for months on end.
[1665.02 → 1671.70] But then just maybe, you know, midnight, it just connects to the internet, sends off the data it's gathered during the day and then shuts down again.
[1671.70 → 1674.60] If you're after like massive long battery power.
[1675.56 → 1683.74] So that was, so to kind of stick there for a minute, being a Kickstarter project and getting past your, your goal well before the deadline, you had the stretch goals.
[1683.74 → 1685.50] What I see three of them.
[1685.56 → 1695.92] So I see the, the Wi-Fi, I see the NPM, the Node.js module loading, and then the OpenWrt package are your three stretch goals.
[1696.18 → 1700.38] Seems like you're about to hit the second one with the NPM, you know, node module loading.
[1700.38 → 1708.42] The third goal, the OpenWrt package to me seems like probably the, the biggest goal.
[1708.42 → 1720.10] The one that is potential to, to really impact the, uh, the uses of Spring, uh, I don't know, greatly with, with being able to use it on other devices and stuff.
[1720.20 → 1722.48] So, I mean, is that true?
[1722.56 → 1728.02] Do you think that 70,000 pound, excuse me if I said dollar a few times, I don't really remember.
[1728.02 → 1735.80] I'm trying to stick to pound, but if, if that 70,000 pound goal gets reached, would you say that's probably like a huge milestone in the project?
[1737.38 → 1753.98] Um, I, I'm not too sure about that because I, I think probably, um, you know, as soon as the source is released, it'll take someone just like an hour or two to, to, to actually create, um, the package for OpenWrt.
[1753.98 → 1770.48] I mean, I'm hoping as part of that to do a few things like, uh, supporting, uh, SPR on it, which will at least, that, that I think will start to get a lot more interesting because then you will start to be able to take JavaScript code, um, and, and run it on the device.
[1770.48 → 1780.18] When, when, when, before it was, it was actually a bit of a pain to, to get stuff in, you know, um, to, to say port Arduino code over to C.
[1780.48 → 1780.72] Right.
[1781.00 → 1783.62] Um, to run on Linux because it's completely different API.
[1784.22 → 1784.48] Mm-hmm.
[1785.08 → 1786.44] How'd you come up with these goals?
[1788.60 → 1792.84] Um, honestly, it's mostly looking through it.
[1792.84 → 1807.16] You know, I had a big to-do list of stuff, um, and there was a definite area on that to-do list, which was kind of like, this would be really cool to have, but I can't justify doing it right now.
[1807.56 → 1812.82] Um, because, you know, it's not really going forward in the direction I want to do.
[1813.16 → 1816.08] So it's quite nice to kind of have an excuse to do that cool stuff.
[1816.08 → 1844.84] Um, and honestly, I, I really can't wait to get, you know, like the, um, WR703, the, um, those little TP-Link travel routers to, to see it on there and, you know, have people just, just buying one of them for, for 20 quid, plugging it in and, um, being able to use, like, a nicely packaged Ethernet and Wi-Fi connected and, and USB connected, um, device.
[1846.08 → 1846.52] Yeah.
[1847.18 → 1850.62] Seems like it's a, I don't know, very exciting thing.
[1850.72 → 1853.34] The, the goal is 70,000 pounds.
[1853.46 → 1857.84] I mean, you got seven days to go, so we got to put a charge out to the listeners to get it there, right?
[1858.22 → 1865.06] I mean, that's the, uh, we want to get it to that 70,000 so we can, so you can actually, in your own words, start doing the fun parts of the project.
[1865.68 → 1865.96] Yeah.
[1866.18 → 1866.92] No, it'd be great.
[1868.38 → 1868.78] Cool.
[1869.30 → 1869.70] Cool.
[1869.74 → 1872.04] Well, this, I mean, this, I don't know.
[1872.04 → 1880.00] So I'm not very, uh, I've not been very active in the Arduino, the, you know, the Raspberry Pis of the world and, and this kind of embedded stuff.
[1880.38 → 1886.78] Um, so for somebody like me that has not really dabbled in this stuff very much, how do I get started?
[1886.96 → 1890.74] Let's say I'm, I'm going to wait and, uh, let's say I'm a backer.
[1890.98 → 1892.88] January, I'm going to get my device.
[1892.88 → 1898.56] But before then, I want to do something to prepare myself so that I don't, I'm not just an idiot when it shows up.
[1898.56 → 1900.72] How do I get started and what do I need to learn?
[1902.06 → 1909.36] Um, I mean, I'm hoping that there won't, there won't be a, a great deal to learn.
[1909.74 → 1914.52] Um, you know, I mean, cause you, you already have some idea about, about how to use JavaScript.
[1914.52 → 1925.30] And, um, on the electronics side, I'm very much focusing on, um, that there's a lot of really cool hardware now that is, is very much purely digital.
[1925.30 → 1931.24] You just connect it in via, you know, sometimes two wires, but, but maybe, maybe six.
[1931.32 → 1933.44] And, you know, it's just, just plugging A to B.
[1934.10 → 1937.94] And, um, and then it just springs into life.
[1938.02 → 1942.62] You don't have to have a huge amount of electronics knowledge or, or anything like that.
[1942.74 → 1949.62] I mean, um, with F3 in itself, maybe, you know, get, get a soldering iron, have a, have a quick play around.
[1949.62 → 1954.28] Um, there, there are plenty of things that show, you know, how to solder simple things together.
[1954.60 → 1963.02] But, but for Spin, it's pretty much, you know, soldering pins onto it and then, then whacking whatever you want onto the pins.
[1964.06 → 1967.16] So where can I go to, to kind of learn about how to do that?
[1967.58 → 1974.20] I'm trying to, I'm trying to dig out of you just some, uh, some, something for our listeners that maybe have never done any of this stuff.
[1974.20 → 1986.52] Um, that is something that, um, they're actually a good post on the Kickstarter from someone who, um, who had found and learned a lot of these.
[1986.78 → 1995.10] Unfortunately, I have to say that I'd, you know, I, I, my dad was quite into electronics and I just, you know, learned as I was growing up.
[1995.18 → 1998.70] So I just, I just don't know about those myself.
[1998.70 → 2003.62] Um, but I, I can find the link, and you can post it in the on the website or whatever.
[2003.62 → 2010.34] Well, it looks like some of the money, uh, should be going to produce more documentation, tutorials, example projects and videos.
[2010.34 → 2013.02] Is that a short-term plan, a long-term plan?
[2014.66 → 2019.48] Um, I mean, that's, uh, that, that's both really short-term.
[2019.48 → 2033.12] You know, I want, as soon as people have got the, the boards, I, I want the website to have like, you know, a good getting started section, you know, which covers all this stuff about how you would go about soldering stuff on.
[2033.12 → 2038.94] Um, what are the easy things to get, to plug into it, to do, to do fun things really quickly.
[2039.76 → 2048.60] Um, going on from that, you know, I obviously want to, want to build up the, the library of drivers that are in there and, and the documentation that goes with them.
[2048.60 → 2060.32] Um, and I'm kind of hoping a load of people will, as they do like fun little projects with it, they'll kind of contribute back, you know, how they've done it, the code they used or all that stuff.
[2060.32 → 2074.64] So, um, so that people have like a good library of, of stuff to, to build from, you know, if you've just got it, and you don't actually have that many ideas about, about what you can do, you can just flip down the list and be like, oh, I can do this in, you know, an hour or two.
[2074.64 → 2077.68] So there are currently some tutorials on the website.
[2077.86 → 2078.86] I don't know if we mentioned it.
[2078.92 → 2082.40] The website is, uh, www.spruino.com.
[2082.80 → 2085.36] That's E-S-P-R-U-I-N-O.com.
[2085.54 → 2089.42] And there's already some like tutorials and examples and a forum on the website.
[2089.42 → 2102.42] And that's kind of a little bit of what I was getting at, that the, the website will probably be a place for you to kind of go and read about and get started and learn just, you know, maybe a little bit more of the basics on how a lot of this stuff, um, works.
[2102.54 → 2108.92] But I guess, will the so you kind of talked about you would like to have it by the time the, the devices get in people's hands.
[2109.00 → 2115.28] So would you say the website will look different, uh, come January than it does now, or maybe not look different, but just have, have more content on it?
[2116.16 → 2117.26] Um, yeah, definitely.
[2117.26 → 2127.74] Uh, so, I mean, for starters, I'm, um, I'm moving everything over to all the documentation is going on GitHub.
[2128.02 → 2132.50] So I'm hoping at least if people have changes to do, you know, they just give me a pull request.
[2133.22 → 2146.48] Um, and then that'll be prettified and pulled on the website as well as, um, all the code snippets are going to have a link on them, which will hopefully go to the web app, which is a, um,
[2146.48 → 2152.72] it's a Google Chrome packaged app, um, and Google Chrome has access to the serial port.
[2152.72 → 2164.94] So you literally, no software to install, even if you don't have a terminal application, you just, just get Chrome, get the web app, and then you, you know, it just connects, and you can, you can use it straight away.
[2165.22 → 2171.20] And with this, with the link, hopefully you get a code sample, you just click the button, and it'll go straight into it.
[2171.20 → 2173.72] And then you can, you can put it on the board.
[2175.88 → 2178.60] So I wanted to kind of, meant to hit on that a little bit earlier.
[2178.84 → 2188.92] Uh, you just teased it a little bit, but even if you have no idea about programming, uh, the S for Reno has a web-based, you know, graphical code editor, I think is what you actually call it.
[2188.92 → 2191.68] So, you just talked about that a little bit.
[2191.80 → 2197.90] So this is a is it a is the, the code editor itself, the Google Chrome, uh, extension?
[2198.92 → 2199.32] Yeah.
[2199.46 → 2203.66] So, uh, it's kind of three things wrapped into one.
[2203.76 → 2212.16] You've got, um, a normal serial port terminal, you know, like, um, let's say on Windows it would be Putty or Minicam on Linux.
[2212.16 → 2216.58] Um, but then that's kind of the left-hand side of the pane.
[2216.66 → 2220.52] On the right-hand side, you've got a syntax highlighted editor.
[2221.42 → 2227.00] Um, or you've got this graphical editor as well, which is, is Google Blocky.
[2227.36 → 2241.02] Um, so it looks just like Scratch, but, um, Blocky itself will, uh, it kind of serializes it into, into JavaScript or various other languages.
[2241.02 → 2245.96] So it's quite nice to just be able to take that and, and put it straight on the device.
[2246.04 → 2252.34] And the kind of, um, the structures in it are a perfect fit for event-based code.
[2252.64 → 2259.44] You know, you can have, when button one is pressed, run this instruction and this instruction and this instruction.
[2260.00 → 2269.90] Um, whereas obviously if you had like an Arduino loop, it's not quite as, as easy to, um, for people to understand exactly what they're supposed to do with it.
[2271.02 → 2274.42] Gotcha. You talked a little bit about, uh, well, you didn't talk about it.
[2274.42 → 2276.18] You just mentioned TESOL earlier in the show.
[2276.18 → 2279.94] So it sounds like that, that would be maybe who you would consider your competition.
[2280.42 → 2280.78] Is that right?
[2281.78 → 2292.24] Yeah. Well, I mean, they're, um, so they've, they are a JavaScript microcontroller, but they're going at it from, um, a slightly different angle.
[2292.24 → 2298.10] Um, they basically, you know, they're going after very internet connected.
[2298.26 → 2306.80] So it's got Wi-Fi on it, but because of that, um, they've given themselves a bunch more RAM and flash, like I think 32 megabit.
[2306.80 → 2313.40] Um, so they're going to have a lot of trouble hitting the very kind of low power consumption target.
[2313.82 → 2322.46] Um, so yeah, they're heading kind of from, um, a higher level downwards, really definitely going for Node.js.
[2322.56 → 2327.80] And I'm very much going for sort of Arduino hardware hacking kind of things up.
[2327.80 → 2341.56] So, um, you know, you mentioned earlier about, um, you know, what you'd use it for if you were, you were an expert and really the answer is, you know, just having fun hacking a project together.
[2341.56 → 2350.40] It's not, you know, it's not going to be a, um, you know, 1 million line monster you're going to make with it.
[2350.40 → 2362.58] Um, but there's a bunch of stuff that you might want to do around your house, or you might, I don't know, um, want to automate your remote control car or whatever.
[2362.58 → 2368.88] You can, you know, you can just actually, you do your day job, you get home and you can actually enjoy doing this.
[2369.00 → 2373.50] It's not just, you know, sitting in front of a computer hacking out code line after line.
[2373.64 → 2377.40] It's, you know, you're actually interacting with it, and you're, you're having fun playing with it.
[2378.02 → 2378.42] Right.
[2378.42 → 2389.82] So when you say expert, you're not necessarily meaning that I'm not going to build a commercial product on top of Esperanto, but you mean expert as in, I know what I'm doing, and I can do lots of cool stuff.
[2390.28 → 2391.14] Yeah, absolutely.
[2391.44 → 2391.76] Gotcha.
[2392.66 → 2394.54] And when somebody asks you, it's kind of interesting.
[2394.64 → 2401.50] It's like when somebody asks you what, you know, what you would use an Esperanto for, it's kind of like saying, you know, I mean, it's a microcontroller, right?
[2401.52 → 2402.40] It can kind of do everything.
[2402.40 → 2405.02] So it's kind of like saying, what can you do with programming?
[2405.20 → 2406.90] And the answer is kind of just everything, right?
[2406.90 → 2408.04] It's hard to just nail it down.
[2408.04 → 2415.20] But it sounds like the Esperanto's target is, like you said this a few times, low power consumption.
[2415.42 → 2425.14] So it's like the smaller, you know, maybe more personal style stuff that you want to accomplish in your house more so than, you know, anything on a large scale, which I guess you just said, and I just repeated.
[2425.14 → 2426.14] Yeah, yeah.
[2426.14 → 2428.30] Yeah, yeah.
[2428.30 → 2433.88] I think, I mean, you know, it, you could use it in industrial things if you want.
[2433.88 → 2444.66] I know of a few people who've contacted me who were, they were using BASIC before in their industrial systems, and they wanted to kind of modernize it a bit.
[2444.82 → 2451.94] And, you know, if you're actually using BASIC for your stuff, then Esperanto is probably a perfect, good thing to use.
[2451.94 → 2461.46] But I would imagine the majority of people have just got stuff in place to use, you know, to just use C basically for anything commercial.
[2461.46 → 2461.58] Right.
[2462.58 → 2463.28] Let me ask you.
[2463.94 → 2469.02] I saw a long time ago, and I'm sure I could bring it up, but it was a few years ago.
[2469.08 → 2479.68] I saw somebody used an Arduino to, I don't remember exactly how it worked, but basically they were controlling their lock on their front door with an Arduino and like a passcode was cloud-based.
[2480.02 → 2482.20] Can you use Esperanto to kind of do something like that?
[2482.92 → 2483.66] Cloud-based.
[2483.66 → 2486.92] It was like you had to get the colour, hit the colours in the right order.
[2487.22 → 2490.58] You know, it was like a key, essentially just like a passcode, but instead of numbers, they used colours.
[2491.28 → 2492.26] Yeah, no, absolutely.
[2492.88 → 2496.54] You know, and that kind of thing is, you know, it's going to be very simple.
[2496.66 → 2502.82] It's going to be, you know, I don't know, 20 lines of code at most to get that working.
[2503.64 → 2506.26] So, yeah, for this kind of things, it's really perfect.
[2506.26 → 2513.70] If you're interacting with a human, you know, you're never really going to have any speed issues at all.
[2513.88 → 2518.38] It's thousands of times faster than you'd need for anything like that.
[2518.70 → 2518.80] Right.
[2520.56 → 2521.18] That's cool.
[2521.46 → 2527.86] Yeah, it's definitely a neat project, and we have, I think that JavaScript is a great language for something like this.
[2527.96 → 2532.04] We have a lot of, I don't know, we hear both sides of it on different projects.
[2532.20 → 2534.58] You know, JavaScript's, nobody wants to use JavaScript.
[2534.74 → 2535.74] Everybody wants to use JavaScript.
[2535.74 → 2539.92] It doesn't really seem to fall in the middle too much, but definitely is a language.
[2540.06 → 2544.90] I think, personally, that it's great for beginners, great for people that want to just kind of put stuff together.
[2545.18 → 2552.66] And to me, this is probably the first microcontroller that I'm really excited to just actually mess around with,
[2552.72 → 2558.86] because I'm not going to, I feel like I don't have a huge barrier of entry of things I have to learn to start hacking on it.
[2558.88 → 2560.24] So I'm excited about it.
[2560.24 → 2565.14] I think we could talk about it forever, but maybe we'll have you on the show in a few, I guess,
[2565.14 → 2570.62] and, you know, longer than four months to talk about the feedback you've gotten, and the coolest thing people are doing with it.
[2571.36 → 2572.20] Cool. Thanks. Yeah.
[2572.20 → 2583.00] So for all of our listeners on the show and for the new listeners, we kind of do the same set of questions at the end of every show
[2583.00 → 2586.22] to kind of give you some insight into the person we're talking with.
[2586.36 → 2592.20] So the first one, and I don't know how appropriate this question is for the current state of the project,
[2592.38 → 2593.88] but maybe you'll know something.
[2594.00 → 2596.12] But the first one we'd like to ask is for a call to arms.
[2596.12 → 2600.40] So something you would like to see the community get involved with or help out with.
[2601.78 → 2610.14] Yeah. I mean, definitely, you know, in, well, if you can't wait now, you can, you can check it out on the website.
[2610.38 → 2614.42] The source isn't released, but there are binaries for a few popular platforms.
[2614.42 → 2619.16] You know if you, you like it, please back us on the Kickstarter because kind of the more,
[2620.04 → 2622.94] the more support we get, the more I can do, hopefully.
[2623.96 → 2632.12] But when the source is released, I mean, it would be great to have like people looking out for interfacing it to more devices,
[2633.22 → 2636.46] optimization, you know, that there are, there are quite a few areas where,
[2636.58 → 2638.52] where it can be made a bit more efficient, a bit faster.
[2638.52 → 2644.40] So, yeah, it'd be great to just have, have people looking at it, playing around with it and just giving feedback, really.
[2644.90 → 2647.70] Right. So right now, get over to Kickstarter and back this thing.
[2648.46 → 2649.10] Would be nice.
[2649.32 → 2649.40] Yeah.
[2649.46 → 2653.32] When it comes out, get over to the repository and help with this thing.
[2655.26 → 2659.38] So, Gordon, Gordon, I'm on your Kickstarter page, and I'm about to back you, but let me ask you this.
[2660.44 → 2664.82] My MacBook doesn't have a serial port. Do I need to get the Bluetooth one or?
[2665.68 → 2667.56] Does it, it has a USB port, surely.
[2667.56 → 2668.84] Oh, USB can just do serial.
[2669.32 → 2669.82] Yeah, sorry.
[2670.12 → 2671.36] So, um, this is like, I did.
[2671.36 → 2673.12] I was thinking the old school serial ports.
[2674.52 → 2686.62] No. So, um, yeah, the, the board, um, you can, you can connect via serial, but it's got USB ports on it, and it appears as a USB CDC device,
[2686.62 → 2692.32] which is kind of a pretty much a complete standard, which means that you don't need drivers or anything.
[2692.46 → 2697.10] You just plug it into your Mac, and it will be recognized, and then you can use screen to connect to it.
[2697.10 → 2697.54] Cool.
[2697.54 → 2699.16] So no software to install, no nothing.
[2699.38 → 2703.08] You just type like eight characters or something and you, you're in.
[2703.54 → 2704.38] Awesome. Thanks.
[2704.96 → 2705.30] Awesome.
[2705.30 → 2715.00] So if you weren't doing, uh, what you're doing now, so imagine yourself not touching Sparing at all, what would you like to be doing?
[2717.16 → 2718.62] Ah, now that's a question.
[2718.62 → 2731.36] Um, I mean, you know, my, my goal has always been, I'd, I'd just love to get a job doing, doing what I love doing.
[2731.36 → 2738.74] Um, and you know, a lot of that's just, just tinkering around with, with hardware or bits of software.
[2739.14 → 2742.30] Um, so yeah, I, I don't know.
[2742.30 → 2752.36] I mean, I'm hoping Sparing will, will allow me to, to at least, you know, to keep doing that without having to get a real job.
[2752.74 → 2759.04] Um, but, but outside Sparing, I'd, I'd have to think around for a bit and try and find another way of doing that.
[2759.12 → 2759.30] I think.
[2759.30 → 2765.06] Man, I just, uh, if I were you, I would just be wandering around the countryside in, in England, man.
[2765.34 → 2768.04] I think the I've been told I got to visit, what is it?
[2768.08 → 2771.44] The, uh, um, so the Lake District, is that what it's called?
[2772.82 → 2773.56] Um, yeah.
[2773.76 → 2780.04] So, um, um, my wife and I actually met doing, just basically wandering around England.
[2780.30 → 2780.98] Um, yeah.
[2781.06 → 2785.26] And it's, it's a it's a lovely place to kind of, to walk.
[2785.54 → 2788.76] Um, as long as you've got a raincoat, it's good.
[2788.76 → 2789.28] Yeah.
[2790.30 → 2796.64] And, uh, lastly, your programmer hero or just anyone in your life to give a shout-out to that's impacted you greatly with what you're doing.
[2798.44 → 2804.78] Um, so I've kind of got like a little bit too, I guess.
[2805.02 → 2813.88] Um, I mean, you know, when I was growing up around that time, you know, I was playing things like Wolfenstein and Doom and.
[2814.26 → 2814.56] Oh, yeah.
[2814.56 → 2821.72] Just seeing someone get so much out of a computer when, you know, I was, I was programming at the time.
[2821.72 → 2823.34] I was kind of interested in graphics.
[2824.02 → 2833.62] Um, and, you know, there, there's a real disconnect between kind of the speed I could manage and the speed John Carmack and its software could manage.
[2833.62 → 2842.78] Um, and that was like, you know, it's just really cool to have something where, where you can look up to it, and you can, you can say, wow, this is cool.
[2842.84 → 2843.78] I wish I could do that.
[2843.78 → 2858.48] Um, I mean, the other thing is, um, my dad, I mean, he's been electrical engineer for 40, 50 years or so doing software and hardware.
[2858.48 → 2866.86] And so there were like computers lying around the house while I was growing up, and it's just been, you know, that's been what caused me to, to get to where I am.
[2867.14 → 2873.40] Just kind of having them from sort of, well, having like a soldering iron for my seventh birthday or something.
[2873.52 → 2878.64] Not many people would, not many people would be crazy enough to do that, but not many people would do that.
[2878.64 → 2881.16] So, um, yeah, that's it.
[2881.70 → 2882.24] That's awesome.
[2882.58 → 2884.64] Well, thanks so much again for coming on the show.
[2884.72 → 2891.34] I mean, the, the, I think the project is a as an ambitious one, and it's one that's going to be exciting to see unfold.
[2891.46 → 2894.76] Um, you know, once again, you have one week left as of right now.
[2894.76 → 2899.60] So I guess September 26th is when the, uh, the project comes to a close on Kickstarter.
[2899.80 → 2902.58] So if you're listening to the show, head on over there.
[2902.70 → 2908.28] I mean, there's definitely still time to back and there's, it's not expensive to be able to get your hands on your own.
[2908.28 → 2914.64] Neutrino and start to build your own colour coded door lock or whatever you want to use it for.
[2914.72 → 2916.96] But no, seriously, thanks so much for coming on with us and just talking.
[2917.06 → 2920.92] I mean, it's a privilege to hear, uh, hear, hear some perspective from you.
[2921.58 → 2921.98] Great.
[2922.24 → 2922.88] Thank you.
[2923.50 → 2927.06] I want to give a shout-out to digital ocean again for sponsoring the show.
[2927.12 → 2935.32] Head on over to digital ocean.com to set up your cloud server today and make sure you use the promo code, the changelog 104 to get $10 off.
[2935.66 → 2937.64] And as a member, you get special benefits.
[2937.64 → 2946.26] You can head on over to the changelog.com slash benefits to access our exclusive members only $20 promo code for digital ocean.
[2946.26 → 2951.56] You can sign in or become a member today to get access to this and many other partner benefits.
[2952.18 → 2953.12] That's it for this week.
[2953.22 → 2956.96] Thanks again to Gordon for joining us as well as Jared for making a special appearance.
[2957.28 → 2960.14] And also thanks to the listeners for tuning in for your support.
[2960.48 → 2965.64] If you haven't yet subscribed to the changelog weekly, where we share everything that hits our open source radar.
[2965.64 → 2968.64] Subscribe at the changelog.com slash weekly.
[2968.96 → 2970.70] Until then, let's say goodbye.
[2971.12 → 2971.68] See ya.
[2972.40 → 2973.04] Bye.
[2995.64 → 2995.92] Bye.
[3006.14 → 3006.98] Bye.
[3007.02 → 3010.44] Bye.
[3010.86 → 3011.28] Bye.
[3019.38 → 3020.74] Bye.
[3020.98 → 3022.02] Bye.
[3022.02 → 3022.52] Bye.
