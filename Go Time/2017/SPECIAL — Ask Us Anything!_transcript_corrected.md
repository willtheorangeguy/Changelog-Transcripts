[0.00 → 5.40] Bandwidth for Change Log is provided by Vastly. Learn more at Fastly.com.
[5.80 → 11.40] I'm Eric St. Martin. I'm Brian Kettle son. I'm Carla Pinto. And it's Go Time.
[22.52 → 27.26] It's Go Time, a weekly podcast where we discuss interesting topics around the Go programming
[27.26 → 32.54] language, the community, and everything in between. If you currently write Go or aspire to,
[32.84 → 34.18] this is the show for you.
[44.38 → 49.38] All right, everybody. Welcome back for another episode of Go Time. Today's episode is number
[49.38 → 55.44] 45, and our sponsor for today is Total. On the show today, we have myself, Eric St. Martin,
[55.44 → 58.70] Carla Pinto is also here. Say hello, Carla.
[59.16 → 60.02] Hi, everybody.
[60.74 → 61.82] And Brian Kettle son.
[62.24 → 62.54] Hello.
[63.02 → 68.16] And we've actually managed to drag Adam Stachowiak back from behind the curtain. Say hello, Adam.
[68.48 → 69.90] Hey, it's me.
[70.22 → 75.36] So our guest for today actually wasn't able to make it due to a scheduling conflict,
[75.36 → 80.10] but we had some discussions this morning and decided let's do an Ask Me Anything,
[80.10 → 87.06] where we posted in Slack and on Twitter for questions for the hosts and for the producers,
[87.32 → 92.58] which is why Adam got dragged onto the show. So we're just going to work through a document
[92.58 → 95.26] that we have of questions from everybody.
[95.82 → 96.98] It's a huge document, too.
[96.98 → 102.78] Yeah, and if you're listening live right now, feel free to... Adam's probably watching Twitter,
[102.94 → 109.32] so feel free to ask questions at GoTimeFM on Twitter, and feel free to join us on Slack
[109.32 → 113.82] and the GoTimeFM channel and ask questions there, and we'll try to keep track of any new questions
[113.82 → 114.36] that come in.
[114.84 → 115.68] What kind of questions?
[116.84 → 118.20] Any kind of questions.
[118.44 → 119.16] What's off limits?
[119.16 → 124.08] Well, they can ask. We can choose not to answer.
[124.16 → 125.66] Yeah, we can choose not to answer. That's fine.
[125.92 → 126.08] Okay.
[126.24 → 129.78] Let's ask anything. It's not an answer anything. It's an ask anything.
[130.20 → 130.60] Yeah.
[131.42 → 134.56] Don't ask anything you wouldn't ask your mother. How's that?
[135.28 → 136.86] That doesn't limit much.
[137.86 → 141.96] So, yeah, so basically, we didn't want to put anything off limits.
[141.96 → 147.70] It's questioning about Go, questions about community, questions about maybe Gopher Con,
[147.82 → 154.16] questions about personal lives, hobbies, what we do for jobs, anything anybody wants to know.
[154.32 → 156.44] It's time to get to know your hosts and producers.
[157.46 → 162.90] So, does anybody want to narrate through the list, or do you want me to ask the questions?
[164.04 → 170.86] Why don't we just go through the fun questions in any random order that sounds fun, and go from there.
[170.86 → 175.20] I'm easy-breezy. I'm port forwarding something right now, though, so we can have a little more fun later.
[176.14 → 178.08] Oh, that sounds like fun.
[178.48 → 179.30] So much excite.
[180.02 → 181.26] I'm port forwarding right now.
[181.70 → 184.18] Chris Benson in the Slack channel just asked,
[184.42 → 189.22] why didn't my artificial intelligence machine learning talk get selected for Gopher Con?
[189.46 → 191.80] Oh, I know the answer to that one.
[192.70 → 195.06] Oh, wait, I'm going to be quiet. Never mind. That wouldn't be nice, would it?
[195.76 → 199.36] So, actually, I think we can get into that a little bit later,
[199.36 → 203.02] because I do remember seeing a question about kind of like how talks are selected.
[203.70 → 207.58] So, that probably falls in line really well there and can help answer that question.
[208.24 → 213.36] I'm just going to start with the first one on the list, which actually is a co-worker of mine.
[214.12 → 217.92] Mark Mandy says, what is the weirdest project you have seen written in Go?
[220.32 → 222.00] I have the best answer for this one.
[222.64 → 223.34] All right, let's hear it.
[223.72 → 225.36] That's why I was trying to port forward a minute ago.
[225.36 → 231.10] So, when I moved into my new house last year, right around this time,
[231.56 → 233.06] I lost the remote to my television.
[233.84 → 237.38] And I am cheap and lazy, and I did not want to get a new television.
[237.90 → 240.34] So, I was Googling around for interesting things to do,
[240.42 → 243.74] and I just started Googling for the model number of my television.
[244.30 → 249.74] And it turns out that there is a home automation interface on the TV
[249.74 → 252.60] that is 100% unsecured over Telnet.
[253.78 → 257.76] And we don't need to get started about being unsecure over Telnet,
[257.96 → 258.78] but there is one.
[258.78 → 261.34] You have to explicitly enable it.
[261.92 → 263.82] It comes shipped off.
[264.32 → 265.22] So, I had to turn it on.
[265.70 → 270.50] But once I did turn it on, now I have a Telnet prompt on my television.
[270.50 → 273.62] So, I hacked up a tiny Go program.
[273.88 → 276.90] It's at GitHub.com slash kettles slash TV.
[277.66 → 282.22] And using it, you can send commands to my television to turn it on and off,
[282.70 → 285.24] turn the volume up and down, and change the input sources.
[286.02 → 289.02] So, from my laptop, I control my television.
[289.84 → 290.26] Nice.
[290.46 → 292.14] And it really is a tiny amount of code.
[292.14 → 297.26] And I was going to port forward that port on my home router
[297.26 → 299.84] so that everybody could play and turn on the TV
[299.84 → 301.18] and turn the volume up and down.
[301.56 → 304.80] But I just realized the IP address of my TV has changed,
[304.96 → 308.48] and I don't know what it is without going out to the television to find it.
[308.60 → 312.20] So, we won't play the screw up Brian's TV game right now.
[312.50 → 313.50] But that would have been fun.
[315.06 → 316.86] You get props for trying.
[317.10 → 317.36] Right?
[317.58 → 318.50] How about you, Galicia?
[318.50 → 324.12] I don't recall anything odd or weird or stupid.
[325.86 → 326.54] I don't know.
[326.62 → 329.16] Maybe I just don't pay attention, but I don't recall.
[329.86 → 331.34] So, I've got one.
[331.40 → 333.50] I don't know whether I would call it weird.
[333.96 → 336.80] But definitely something I didn't expect to find written in Go
[336.80 → 340.04] was a while back, and I think we might have even mentioned it on the show,
[340.60 → 343.22] there was a project called Regulator,
[343.78 → 346.68] which was a Nintendo emulator written in Go.
[346.68 → 348.10] And that was just kind of really cool.
[348.10 → 351.58] I didn't expect to see that written in Go, especially so early in Go's life.
[353.04 → 355.64] Now, how about the next one?
[357.10 → 358.20] I don't have an answer here.
[359.00 → 361.46] Hey, yeah, you're familiar with Go projects.
[361.96 → 363.32] I know the Go world a little bit.
[363.80 → 367.76] I was actually really excited to see, and it thought it was a little weird.
[367.92 → 368.72] I didn't expect it.
[368.76 → 370.52] That's why it's weird, but it's not a weird thing.
[370.52 → 373.56] It's Ruby, the Ruby Lang written in Go.
[373.66 → 378.86] I think that's kind of interesting to take Go and write an object-oriented language on top of it.
[379.44 → 381.22] I just thought that was like, I didn't expect it.
[381.38 → 381.88] I'll leave field.
[382.86 → 386.62] I just plus one that, because I thought the same.
[386.96 → 388.96] And by the way, do you want to introduce yourself?
[389.64 → 389.86] Me?
[390.62 → 391.00] Mm-hmm.
[391.56 → 392.12] Let me say.
[393.10 → 393.40] I'm me.
[393.80 → 393.96] Yeah.
[394.16 → 394.56] I'm me.
[394.66 → 395.86] Your name, and who are you?
[396.00 → 398.70] Because I didn't realize it was going to be on.
[398.82 → 399.28] Oh, yeah.
[399.34 → 403.68] Well, for the folks who are listening, I'm using the person behind the scenes.
[403.82 → 405.34] I'm here every single show.
[405.38 → 406.30] So this is episode 45.
[406.56 → 408.30] I've been here all 45 episodes.
[408.70 → 409.22] It's been a lot of fun.
[409.22 → 412.40] My name is Adam Stachowiak, editor-in-chief of Changelog.
[412.46 → 413.88] I've been doing this for a while.
[414.62 → 416.66] Started the Changelog back in 2009.
[416.76 → 418.26] Started podcasting back in 2006.
[418.50 → 420.00] So I've kind of been doing this for a bit.
[421.06 → 421.98] And it's a lot of fun.
[422.20 → 424.06] I like meeting people.
[424.18 → 424.90] I love the Hanger community.
[424.90 → 430.38] It's a lot of fun to do this and to do awesome shows like Go Time.
[430.38 → 443.96] And if you happen to be around 3 p.m. Eastern time, well, I guess really it's 4:5 p.m. Eastern Standard Time, the aftershow Adam usually comes on after we.
[444.14 → 444.90] I appear there, too.
[445.48 → 445.78] Yes.
[446.04 → 447.52] So if you want to hear more of Adam.
[448.04 → 448.38] Sometimes.
[449.24 → 451.62] And Adam would also be a gopher con.
[452.36 → 452.68] Yeah.
[452.82 → 453.82] I'll be a gopher con.
[454.72 → 456.48] I usually have random jobs there.
[456.58 → 457.82] Sometimes I grab the trash.
[457.82 → 460.76] I help out the staff.
[461.02 → 462.62] Other times I have a camera in my hand.
[462.80 → 468.12] And sometimes I'm just standing there with a weird face because I don't know what's going on.
[468.28 → 469.36] But I try.
[470.34 → 471.26] Anyway, Ruby.
[471.60 → 472.22] Pretty interesting.
[472.54 → 474.58] That's R-O-O-B-Y.
[475.58 → 476.12] Written in Go.
[477.16 → 477.38] All right.
[477.38 → 478.06] What do we get next?
[478.86 → 479.70] Next question.
[480.62 → 482.08] Are we going linear down this list?
[482.76 → 483.28] Why not?
[483.28 → 487.80] Where do each of you put Golang in two years time?
[487.94 → 488.52] Maybe five years.
[488.60 → 490.20] So basically, pontificate.
[490.32 → 491.24] Where's Go going?
[492.00 → 492.64] Two to five years.
[493.18 → 493.34] Yeah.
[493.44 → 495.96] These future visions are always difficult.
[497.34 → 501.08] Like right now, I mean, it really is the language of cloud.
[501.48 → 501.64] Right.
[501.76 → 504.74] Like most distributed system software is being written in it.
[505.32 → 507.10] All the tooling surrounding that.
[507.72 → 510.10] Monitoring and metric systems are all written in Go.
[510.10 → 513.94] So, I mean, I feel like it's going to continue to grow there.
[514.78 → 521.04] We keep seeing a little bit of hints at it on, you know, the phone and on embedded devices.
[521.38 → 527.06] But I think that the catalyst has kind of already happened in the distributed systems world.
[528.06 → 528.72] How about you, Brian?
[528.86 → 529.94] You love these things.
[530.82 → 534.94] I think they pinned your tweet on the GoTimeFM Twitter.
[537.10 → 538.62] Brian's doing barbecue.
[538.62 → 538.82] Thank you.
[539.36 → 539.62] Right?
[539.90 → 540.36] Are we losing?
[540.68 → 541.58] He's muted or something.
[541.70 → 544.44] That would explain why you guys didn't laugh at the thing I said earlier.
[544.56 → 545.32] Because I was muted.
[547.72 → 548.56] We'll laugh now.
[548.68 → 549.38] What'd you say?
[549.64 → 552.46] I said that you were the prince of podcasts.
[552.94 → 553.18] What?
[553.68 → 554.26] Oh, what?
[554.98 → 556.28] See, I've forgotten most of it now.
[556.34 → 562.48] The prince of podcasts, the royalty of radio, and the ocelot of open source.
[562.48 → 563.72] Whoa, okay.
[564.22 → 565.62] That's pretty interesting.
[566.18 → 571.68] I thought that was pretty good because I couldn't think of anything that was royalty that started with an O and I needed to get open source in there.
[571.92 → 572.54] So, you're an ocelot.
[572.74 → 572.94] Sorry.
[573.30 → 573.82] That's good.
[574.10 → 574.92] Yeah, I like that.
[575.16 → 576.68] Now you need a new business card.
[576.90 → 578.82] Had I heard that, I would have laughed.
[579.32 → 579.52] See?
[579.96 → 580.22] Yeah.
[580.44 → 580.84] Thank you.
[581.32 → 581.70] You bet.
[582.22 → 582.84] I'm here for you.
[582.84 → 596.10] So, I think that Go in two years will continue the trajectory it's on now, but in five years, Go will be the dominant server-side language, taking over the spot of Java.
[597.48 → 607.32] A lot of the huge server-side stuff that you see now, especially in the open source infrastructure bits, things like Kafka and Zookeeper,
[607.32 → 619.90] they are slowly being replaced by much smaller memory footprint Go applications that are a little bit faster, a little bit easier to run, and significantly easier to deploy.
[621.06 → 622.78] And that trend will continue.
[622.92 → 626.52] So, I think in five years, definitely, Go will own the server-side market.
[627.22 → 633.00] And two years, I don't think the change is going to be that drastic to see, but in five, I think Go will be on top.
[633.30 → 634.88] What do you think is perpetuating that?
[634.88 → 637.40] A single binary deploy.
[638.38 → 650.90] If you've ever tried to administer a Kafka cluster or Zookeeper cluster or any of that, I mean, just the whole deploying JVM requires a master's degree in deploying JVMs.
[651.48 → 652.22] Wow, that's a shame.
[652.84 → 655.28] And Go is significantly easier to deploy.
[655.28 → 665.86] And I honestly think the DevOps movement, the serverless movement, all of those things fit really nicely into a language that has a single binary deploy.
[666.40 → 672.00] What do you say to somebody, sort of flip side of that question, to somebody who's like Rust or Go?
[672.00 → 675.78] I think it should be Rust and Go.
[676.42 → 678.82] So, there are sweet spots for both languages.
[678.96 → 682.32] There's no reason that you have to choose one over the other.
[682.74 → 685.16] And there are places and times for each of them.
[685.74 → 690.08] I really like Rust for extreme memory safety.
[690.08 → 699.04] But I also think that Rust isn't the language to choose if you want to give it to a team of 100 people and have them build some awesome cloud project.
[700.10 → 703.06] Rust is smaller, really memory-sensitive apps.
[703.06 → 715.70] I was going to add to that, too, that I think a lot of it, too, is that these pieces of software for distributed systems are often complex and large and a lot of moving parts.
[716.36 → 728.40] So, I think that having a language that's much easier to fit the whole language in your head at one time, I think, really helps people be able to be productive writing this type of software.
[729.16 → 730.28] How about you, Galicia?
[730.66 → 732.60] What's your vision for the next two to five years?
[733.06 → 735.78] Yeah, I agree completely with Brian.
[736.20 → 746.40] Even with the time frame, I think in five years, Go will take over a lot of space that's taken up by Java right now.
[746.88 → 749.30] It will become more enterprise-y.
[749.30 → 763.76] I say this because I think it's over the past two years, independently of Go, it just has become easier to develop things in components and in a modular way.
[763.76 → 773.06] So, it will be natural to just replace pieces of systems with Go.
[773.60 → 778.54] I don't think Go is going to be homogeneous, the language that's going to be used.
[778.68 → 781.02] And that will never happen no matter what the language is, right?
[781.06 → 782.46] Because it doesn't even make sense.
[782.46 → 791.70] But I think it will take up chunks and enough to be the dominant language because of all the attributes that Go has.
[791.70 → 805.72] Now, in the next two years, what I see happening is with Steve Francia coming on board to be the sort of like product manager.
[805.72 → 810.36] He has a different title, but that's one idea of what he does.
[811.30 → 816.02] And the development group, working group coming together.
[816.42 → 824.02] I think these next four years, we're going to see a lot of changes in terms of making Go easier to onboard people.
[824.02 → 831.20] And I don't know this for a fact, but I expect that the website is going to be redone and be friendlier.
[832.02 → 834.76] I expect more training material.
[835.36 → 843.74] I expect training material for different level of developers, you know, developers that are brand-new programmers, developers who are experienced programmers, but want to learn Go.
[844.14 → 847.18] So, that's what I expect to happen in the next two years.
[847.18 → 857.48] And once that is in place, the adoption is going to be exponential even more than it is now.
[858.10 → 859.00] How about you, Adam?
[859.12 → 860.82] Do you want to take a stab at this?
[861.58 → 863.44] It's above my pay grade.
[867.14 → 868.48] What's our next question?
[869.48 → 876.44] Well, it was Martin Truck, I'm assuming, Von something long, a cool name, who asked that question.
[876.44 → 878.22] And Mark Moody, who asked the previous question.
[878.56 → 879.94] So, that was good.
[880.28 → 883.96] If we're going to be linear, I don't know who has this next one.
[884.08 → 885.24] So, there's no name attached to that.
[885.34 → 886.68] Do you want to camp there?
[886.72 → 887.40] Do you want to skip it?
[888.48 → 889.28] Actually, I think that was still Mark.
[889.28 → 890.64] Let's skip the Gopher kind of question.
[890.74 → 891.30] Let's add those.
[891.78 → 892.50] We can do those later.
[892.72 → 892.98] All right.
[893.00 → 894.02] Because there's a handful of them.
[894.54 → 896.64] And that was also by Martin Truck Von Butler.
[897.50 → 899.02] Yes, that's a cool name.
[899.50 → 903.22] I didn't see the Von Butler until I started talking.
[903.22 → 905.20] And so, that's why I was all jacked up.
[905.40 → 907.00] But that's how it works.
[907.44 → 908.90] Casey Wilson is next up, though.
[908.98 → 910.26] Thank you, Casey, for submitting this question.
[910.34 → 910.90] This was on Twitter.
[911.02 → 911.34] Is that right?
[911.54 → 912.82] Somebody, this is to you, Eric?
[913.32 → 914.22] This was on Slack.
[914.40 → 915.48] I think he was just chatting back to you.
[915.48 → 915.68] Gotcha.
[917.46 → 919.26] I'm going to summarize it, basically.
[919.38 → 921.88] Bringing up the Gopher Review channel would be cool.
[921.88 → 926.72] I think not a lot know that you can get full-on code reviews slash help.
[927.52 → 935.08] Also, how Johnny was talking about naming conventions and using more descriptive names as you get farther away from the declarative than, of course, barbecue.
[935.28 → 936.98] So, who doesn't want to talk about barbecue?
[937.22 → 941.70] So, let's start with the first one, which was the Gopher Review channel.
[941.76 → 942.32] What is this?
[942.78 → 944.24] Yeah, so I guess we'll start there.
[944.30 → 947.08] That's more of an awareness thing.
[947.08 → 957.72] So, on the Gopher Slack, there is a reviews channel with lots of people who just camp out there and are happy to do code reviews for you.
[957.92 → 962.74] So, definitely reach out with problems and questions there and send them your code.
[963.06 → 965.46] And lots of people love to provide feedback.
[966.26 → 969.36] So, yeah, that's an awareness thing more than it is a question for everybody.
[969.36 → 976.52] And then, like, Johnny Portico was talking about naming conventions the other day.
[976.58 → 980.72] We were talking about, like, whether you should have one-letter variable names and things.
[980.98 → 984.00] And those are some of the types of topics we discussed in those few channels.
[984.40 → 991.82] So, basically, this was, like, the closer you get to scope, where you define a variable, the less descriptive it can be.
[992.20 → 994.74] Yeah, that's actually in the Go-styled guide, by the way.
[995.52 → 996.54] Oh, yeah, that's right, it is.
[997.16 → 997.36] Yep.
[997.36 → 1001.52] And then the third part of it was more on a personal note, and that was barbecue.
[1001.92 → 1005.98] And what is your preferred cut of meat and wood type for smoking?
[1006.30 → 1006.94] Just saying.
[1008.04 → 1008.62] All right.
[1008.72 → 1009.04] That's a good one.
[1009.34 → 1010.32] Who wants to go first?
[1010.90 → 1012.54] I'll start with the meat.
[1013.02 → 1016.88] My preferred cut of meat these days is a sirloin roast.
[1017.38 → 1017.74] Nice.
[1017.92 → 1019.66] And I found them at Costco.
[1020.32 → 1024.18] They are roughly a third of the price of prime rib.
[1024.18 → 1028.50] And maybe 90% of the awesome flavour of prime rib.
[1029.14 → 1033.16] So, for a ridiculously lower amount, you can almost get prime rib.
[1033.94 → 1035.94] So, I had, in fact, I'm cooking one tomorrow.
[1036.26 → 1038.18] It's like an eight or nine pound roast.
[1038.30 → 1041.40] And I think I paid $27 for it.
[1041.96 → 1042.62] Crazy cheap.
[1042.62 → 1047.44] And I'm going to be smoking that with pecan wood because that's the wood I have.
[1048.72 → 1051.30] But generally, when I'm doing beef, I like oak.
[1052.24 → 1052.38] Hmm.
[1052.80 → 1054.62] What is it about the trees?
[1055.70 → 1056.50] Is it the wood?
[1056.58 → 1057.48] I guess you should say not the trees.
[1057.52 → 1058.46] There's no longer trees, right?
[1058.52 → 1059.22] They're not wood.
[1059.60 → 1060.28] They were trees.
[1060.36 → 1061.12] It's pretty funny.
[1061.12 → 1064.94] What is it about the wood type that brings out flavour?
[1065.82 → 1071.12] Each one of them kind of has their own unique flavour and how kind of potent they are.
[1071.66 → 1074.90] Like oak is a much more bold flavour.
[1075.84 → 1078.20] Hickory has a much sweeter taste to it.
[1079.00 → 1082.56] Pecan is similar, except probably milder than a hickory.
[1082.64 → 1083.44] It's mildly sweet.
[1083.68 → 1083.80] Yeah.
[1084.06 → 1084.22] Yeah.
[1085.46 → 1089.58] Mesquite is very, very potent.
[1089.58 → 1090.74] It's strong.
[1091.06 → 1092.02] It's a little bit bitter.
[1092.94 → 1097.76] But most people usually use woods that are local to them.
[1098.06 → 1102.32] So if you go to Texas, it's a lot of post oak and things like that.
[1102.38 → 1102.74] Mesquite.
[1102.80 → 1103.56] Just because that's...
[1103.56 → 1104.30] That is so funny.
[1104.38 → 1108.36] There's literally a place here in Houston and a street called post oak.
[1108.82 → 1109.08] Mm-hmm.
[1109.70 → 1110.06] Mm-hmm.
[1110.06 → 1113.96] And then Georgia uses a lot of peach tree and stuff like that.
[1114.04 → 1115.98] So a lot of people just use what's nearby.
[1115.98 → 1120.10] And that availability of wood shapes the regional flavours too.
[1120.46 → 1120.70] Mm-hmm.
[1120.86 → 1127.26] You know, in Texas, the regional flavours are sharper because of the woods that are available.
[1127.26 → 1131.54] In South Carolina, they're more sweet because of the woods that are available.
[1132.06 → 1135.02] And so that's why when you travel, food tastes different.
[1135.54 → 1135.76] Mm-hmm.
[1135.76 → 1137.42] Especially if it's smoked in this case, right?
[1137.42 → 1139.22] I mean, or at least barbecue tastes different.
[1139.22 → 1143.40] Because when you come to Texas, you come for steaks, and you come for barbecue.
[1143.90 → 1144.20] Mm-hmm.
[1144.76 → 1145.74] There's another reason to come.
[1146.36 → 1147.12] It's a different story.
[1147.56 → 1147.74] Yep.
[1148.34 → 1154.06] So I think we can probably make this question more generic to also the type you like to eat.
[1154.06 → 1157.38] So in case anybody here does not barbecue themselves.
[1157.38 → 1160.74] What's your favourite cuts of meat in woods, Eric?
[1161.26 → 1163.26] So I'm going to have to go with brisket.
[1163.68 → 1164.06] Mm-hmm.
[1164.24 → 1167.98] And I think that's just because that's like the king of barbecue.
[1168.20 → 1170.24] Like if you can perfect that, you are...
[1170.24 → 1171.56] Burn-ins, whiz cut.
[1172.48 → 1173.98] Pit master among pit masters.
[1174.86 → 1177.60] Eric's brisket is to die for.
[1178.50 → 1180.50] Some of the best I've ever, ever had.
[1181.06 → 1182.12] I need to do another one.
[1182.28 → 1183.24] But yeah, definitely brisket.
[1183.52 → 1184.92] I like hickory a lot.
[1185.02 → 1186.70] I probably cook the most with hickory.
[1187.38 → 1188.16] Oak's good.
[1188.66 → 1191.54] I've got like some black cherry that I'll throw in once in a while too.
[1191.86 → 1193.70] But for the most part, it's probably hickory.
[1194.62 → 1195.72] How about you, Galicia?
[1196.06 → 1197.14] Do you like eating barbecue?
[1197.88 → 1200.14] I don't eat much meat these days.
[1201.36 → 1203.14] But I'm also not...
[1203.78 → 1205.88] I did in the past.
[1206.32 → 1211.00] And in barbecue, in Brazilian barbecue, radio, all that kind of thing.
[1211.52 → 1216.48] I'm not as knowledgeable as you, especially when it comes to American.
[1216.70 → 1218.24] Cuts of meat.
[1218.66 → 1220.38] Because in Brazil, the cuts of meat.
[1220.48 → 1221.76] Some of the cuts of meat are different.
[1222.16 → 1222.72] Educate us.
[1222.80 → 1223.42] Well, tell us.
[1223.94 → 1225.34] I don't know enough to...
[1225.34 → 1227.46] I don't even know how you call stuff here.
[1227.46 → 1229.86] So they're just called different, right?
[1230.22 → 1232.66] I just know that because when Brazilians want to barbecue,
[1233.16 → 1234.54] and they want a specific kind of meat,
[1234.60 → 1236.54] they go to the Brazilian meat store.
[1236.74 → 1237.10] Right.
[1237.10 → 1238.86] Because they're going to cut the meat that way.
[1239.14 → 1240.66] And you don't get that kind of meat.
[1241.02 → 1243.72] We have a couple of places around here that's Brazilian.
[1244.28 → 1249.26] And when you order, it's different from a traditional steakhouse, for example.
[1250.12 → 1250.34] Yeah.
[1250.56 → 1250.72] Yeah.
[1250.84 → 1253.40] And I'm talking about Brazilians in the U.S.
[1253.56 → 1253.74] Right.
[1253.74 → 1254.48] Or outside of Brazil.
[1254.48 → 1259.14] But when I did eat a lot of meat, and I'll go to Brazilian radiation,
[1259.88 → 1262.00] I remember I liked a lot.
[1262.10 → 1264.18] My favourite, it was the hump.
[1264.78 → 1265.70] Do you know what I mean?
[1266.18 → 1266.46] Yeah.
[1266.90 → 1270.60] Like some cows or...
[1270.60 → 1271.20] Maybe it was rump.
[1271.34 → 1271.66] I don't know.
[1272.30 → 1272.82] Rump roast?
[1273.48 → 1273.70] No.
[1273.92 → 1276.02] The hump, like on the back of the animal.
[1276.08 → 1276.42] Really?
[1276.94 → 1277.38] Yeah.
[1277.70 → 1278.48] There's meat back there?
[1278.48 → 1278.84] Yeah.
[1279.56 → 1280.68] It's very fatty.
[1281.16 → 1282.42] It's very moist.
[1283.48 → 1285.36] And it holds the...
[1285.36 → 1289.00] It holds up the whatever marinade you put on it.
[1289.04 → 1290.16] It holds it up pretty well.
[1290.22 → 1292.28] For example, I would like brisket.
[1292.70 → 1294.06] But I don't think it tastes right.
[1294.28 → 1295.78] Every brisket tastes the same.
[1296.32 → 1297.44] The texture changes.
[1297.56 → 1298.48] Some are better than others.
[1299.10 → 1299.58] Yeah.
[1299.76 → 1302.62] So the difficulty, this is where you get into animal anatomy.
[1303.38 → 1307.46] So up near the back aren't as many working muscles.
[1307.46 → 1311.96] So that's like where your prime rib and all your rib eyes and all those good steaks come from.
[1312.42 → 1316.42] But on the cow, the brisket is in like the breast area.
[1316.54 → 1321.48] So it's a really tough muscle, like a working muscle for holding...
[1321.48 → 1326.06] I think they say like something like 60% of the weight of the cow is supported by it.
[1326.48 → 1326.56] Yeah.
[1326.56 → 1328.32] So really, really tough.
[1328.90 → 1329.52] So that's why...
[1329.52 → 1330.10] Their heads.
[1330.32 → 1331.78] Their heads are huge, you know?
[1332.32 → 1332.56] Yeah.
[1332.56 → 1338.72] So I think that's one of the reasons that I like that cut so much is it's so tough.
[1339.10 → 1347.10] So there's like this perfect balance between if it's not cooked enough, it doesn't break down and doesn't become tender.
[1347.20 → 1348.52] And it's just tough and bland.
[1348.84 → 1353.92] And if you cook it too far, it becomes more like just like roast beef and just shreds.
[1353.92 → 1355.56] So trying to get like that perfect...
[1356.14 → 1356.30] Yeah.
[1356.30 → 1359.30] Is that where the term fatback came from?
[1359.84 → 1360.24] Could be.
[1360.64 → 1360.78] Yeah.
[1361.44 → 1366.98] So I just looked up the cuts of meat that I was talking about in Portuguese is called Cupid.
[1367.66 → 1369.76] And in English, it's called hump steak.
[1370.64 → 1371.62] I've never heard of it.
[1371.68 → 1372.12] That's awesome.
[1372.32 → 1372.70] Me either.
[1372.82 → 1374.68] I'm going to write it down because I want some now.
[1374.78 → 1379.14] If you go to a Brazilian churrascaria, you need to ask for this.
[1379.28 → 1379.72] Wow.
[1379.82 → 1381.40] We are getting educated here, man.
[1381.60 → 1382.10] It's amazing.
[1382.10 → 1390.24] You know, there's a perfect Brazilian steakhouse in Denver that we might need to go to, Galicia, so you can educate us on all of this delicious meat.
[1390.58 → 1390.84] Yeah.
[1390.86 → 1391.68] Oh, let's do it.
[1391.88 → 1392.88] What's the name?
[1393.58 → 1394.26] Funny Chance?
[1394.70 → 1395.94] I don't remember the name.
[1396.00 → 1397.06] I just remember the location.
[1397.34 → 1398.74] So we'll figure it out.
[1399.30 → 1400.80] Galicia knows a lot of cool stuff.
[1400.90 → 1401.38] Yes, she does.
[1402.38 → 1409.84] I was out in San Diego for work and I met up with her, and we went out to dinner to like a what was it?
[1409.84 → 1410.84] Like an Ethiopian restaurant?
[1411.68 → 1411.78] Yeah.
[1412.10 → 1412.50] Yeah.
[1412.86 → 1413.96] I'd never had it before.
[1413.96 → 1414.36] What did you eat?
[1414.44 → 1415.00] Fried dirt?
[1415.42 → 1416.24] Fried dirt.
[1416.88 → 1427.12] It was actually, so one of the coolest parts about eating that way was like one of the things that I love about like barbecue and things like that is like it brings people together, right?
[1427.20 → 1429.40] Like having a cookout and having people over.
[1429.90 → 1432.54] But like the way people eat is awesome.
[1432.54 → 1438.52] So it's like you ordered everything and everything came out on one plate in the middle of the table.
[1439.24 → 1442.46] And I don't know what you call the bread that comes rolled up like that.
[1442.94 → 1444.18] It's called injury.
[1444.18 → 1444.30] Yeah.
[1444.86 → 1445.22] Yeah.
[1445.22 → 1445.26] Yeah.
[1445.36 → 1453.28] So it's like almost like pancake material or spongy, and you tear off pieces and you kind of pinch your food off in it and eat.
[1453.70 → 1454.86] So everybody kind of collectively.
[1455.10 → 1455.24] Yeah.
[1455.46 → 1456.26] That sounds cool.
[1456.26 → 1458.92] Ethiopian food is my favourite food.
[1459.30 → 1459.80] It's good stuff.
[1459.80 → 1468.44] If I'm going to go for a day, and you say you can only have one meal that day, but you can choose whatever meal is going to be Ethiopian food.
[1470.72 → 1474.72] Culturally, I thought that that was really cool because that really brings everybody together.
[1474.90 → 1478.12] It's not like I get my plate, and then I go off and eat it.
[1478.30 → 1480.34] Everybody is sitting around that plate.
[1480.62 → 1482.60] Like everybody's food is the same place.
[1483.12 → 1489.12] I'm going to jump in here and say we have a ton of questions in a finite amount of time.
[1489.12 → 1490.10] Let's do this.
[1490.38 → 1491.86] Lets that was a good subject.
[1492.00 → 1492.62] I like that.
[1492.74 → 1495.16] Why don't we take a break for our sponsor?
[1495.28 → 1497.74] Why don't we hit our first sponsor break while we're here since we've.
[1497.74 → 1498.66] Brian, that's a great idea.
[1498.98 → 1499.34] Everybody hungry.
[1499.52 → 1500.48] I love it.
[1500.56 → 1501.44] I'm starving.
[1502.18 → 1503.60] Let's break for some food.
[1504.60 → 1505.54] Oh, guys.
[1505.88 → 1510.70] Today's show is brought to you by barbecue and Total.
[1511.98 → 1512.70] Hey, everyone.
[1512.82 → 1515.38] Adam Stachowiak here, editor-in-chief of Changelog.
[1515.38 → 1520.34] Our friends at Total have been sponsoring our podcast for years, and now they're sponsoring
[1520.34 → 1521.18] Go Time as well.
[1521.48 → 1525.96] We think they're one of the best ways to hire developers and designers as well as one of
[1525.96 → 1529.28] the best ways to freelance as a software developer or designer.
[1529.68 → 1532.28] Head to TopTal.com slash go to learn more.
[1532.58 → 1534.08] Tell them you heard about them on Go Time.
[1534.44 → 1538.76] If you'd like a more personal introduction, email me, Adam at ChangeLog.com.
[1538.76 → 1540.06] And now back to the show.
[1546.16 → 1546.88] All right.
[1546.94 → 1549.04] We are back doing our AMA.
[1549.32 → 1554.16] So we went off kind of like on a tangent there with barbecue and food.
[1554.34 → 1558.12] Now that I'm hungry, what else do we have for questions?
[1558.86 → 1559.80] I think here we go.
[1559.92 → 1563.02] So our next question is from Wade Arnold.
[1563.14 → 1564.24] And this came from Twitter.
[1564.24 → 1569.44] He says, what aspects of the language have made it so popular for open source projects?
[1569.88 → 1572.86] Think of all the large code bases for complex systems in Go.
[1573.46 → 1576.94] I think we touched on this a little bit when we talked about the future of Go.
[1577.40 → 1583.48] I think that, you know, the single binary deploy, you know, basically the language not being
[1583.48 → 1587.36] as complex for people to understand makes for more manageable code bases.
[1587.72 → 1589.62] Did anybody have any additional?
[1589.62 → 1595.02] Oh, I think there's a huge reason for me, and especially in terms of the large complex
[1595.02 → 1597.30] code bases, is the readability.
[1597.74 → 1603.36] Go was very specifically built to be read, more so than it was built to be written.
[1603.86 → 1608.20] And in a huge code base, you spend far more time reading code than you do writing code.
[1608.20 → 1615.36] So having a programming language that optimizes for developer productivity by allowing you
[1615.36 → 1621.36] to easily read the code, I think Go trumps all other languages in terms of readability.
[1621.62 → 1625.60] It's so easy to see what's going on in Go compared to other languages.
[1626.40 → 1626.58] Yeah.
[1627.22 → 1629.20] I was thinking exactly that.
[1630.02 → 1631.68] I was going to say, I don't really know.
[1631.74 → 1635.32] The only thing I can think about is the readability factor, which is amazing.
[1635.32 → 1639.46] And you don't understand what it is until you're really working with it for a while.
[1640.00 → 1645.58] It's interesting to say, though, that in a large code base, you would read a lot more
[1645.58 → 1649.42] than you write, because technically somebody had to write all that.
[1649.76 → 1654.04] But reading, it would totally make sense, especially if you didn't write it.
[1654.08 → 1655.12] You're probably going to read it, right?
[1655.16 → 1656.96] Because you can't write what you didn't write.
[1657.20 → 1657.78] You got to read it.
[1658.66 → 1660.34] I totally agree with that.
[1660.38 → 1661.22] You read so much more.
[1661.22 → 1666.92] Even the code that I wrote, I keep reading to figure out, okay, what is this doing again?
[1668.58 → 1670.04] There's a lot more reading, I think.
[1670.92 → 1671.72] Like a book.
[1672.00 → 1673.56] Code is like a book, you all.
[1673.86 → 1674.24] Read it.
[1675.18 → 1675.56] You all.
[1676.40 → 1681.08] So our next question came from Casey Wilson on the GoTimeFM Slack channel.
[1681.08 → 1685.66] It says, something else I'd like to see your guys' development environment.
[1686.52 → 1689.00] What does your focus mode look like?
[1689.00 → 1690.76] That's a good question.
[1691.58 → 1692.68] What does focus mode mean?
[1693.28 → 1699.02] I think super productive, like in the zone programming is what I'm going to take that as.
[1699.38 → 1703.30] I wasn't sure if it was a term for the IDE or something like that, or an editor you might use.
[1703.58 → 1704.90] I was like, I don't know about no focus mode.
[1706.18 → 1708.00] So I'll start first.
[1708.00 → 1714.04] So typically, I work in Vim, and I use the i3 window manager on Linux.
[1714.62 → 1724.22] So typically, I have kind of i3 configured where I just have Vim taking up most of the window and another window to the side or something.
[1724.28 → 1724.92] That's my shell.
[1725.02 → 1726.74] And that's just what I do.
[1726.90 → 1729.92] I'm perfectly happy in just a command line.
[1729.92 → 1732.38] Yeah, for focus mode, mine's exactly the same.
[1732.56 → 1738.02] If I know I have some dedicated time to really sit down and focus, I'm right with you in i3.
[1739.64 → 1741.74] Usually, I'm doing i3 on a laptop, though.
[1741.86 → 1746.16] So it would be one i3 window per thing.
[1746.16 → 1751.12] So I'll have an i3 window for my editor, an i3 window for my shell, an i3 window for a browser.
[1751.52 → 1756.14] And it just popped back and forth between them using the quick i3 command keys.
[1757.32 → 1762.40] Now, I should also add, like when I'm in super focus mode, like I'm a big music person.
[1762.64 → 1765.28] So I love to jam out to music while I'm coding.
[1765.74 → 1770.52] Like my wife will come home, and that's when she knows I'm in the zone, because music will just be like blaring in the house.
[1770.68 → 1771.26] And I'll just be good.
[1772.24 → 1773.32] How about you, Galicia?
[1773.32 → 1777.48] I'm very volatile with editors.
[1777.90 → 1784.10] I come to realize sometimes I go through a stretch of times when I'm using Vim.
[1784.64 → 1789.32] And then I run into a roadblock with Vim, and I switch to...
[1789.94 → 1792.24] My go-to switch, too, was Atom.
[1793.02 → 1801.10] And then I recently changed to VS Code, which I really like, especially for the ability to navigate through, you know,
[1801.10 → 1803.90] all the way through the chain of function calls.
[1804.54 → 1807.52] But I haven't set it up yet.
[1807.62 → 1809.32] So I don't have any shortcuts.
[1810.64 → 1812.38] And there is a lot you can do.
[1812.76 → 1819.18] And we're actually going to have a show with the woman who develops the plugin for VS Code,
[1819.18 → 1822.40] the Go plugin for VS Code, in a couple of weeks, I think.
[1822.56 → 1823.60] So that's going to be pretty awesome.
[1823.72 → 1823.92] Maybe.
[1824.54 → 1826.24] I wonder how to give us a tutorial.
[1827.02 → 1828.12] But so that's one thing.
[1828.94 → 1837.34] Another part of my flow is the Divi app, app, that I can just move windows around with a couple of shortcuts.
[1837.34 → 1839.12] I can't live without that.
[1839.54 → 1842.30] I need to have headphones on my ears.
[1842.48 → 1844.06] I don't care if there's music playing.
[1844.76 → 1847.74] Sometimes I don't realize if the music's playing or not.
[1847.90 → 1848.42] That's funny.
[1849.10 → 1850.30] Yeah, it's a comfort thing.
[1850.58 → 1856.56] Like, it doesn't matter if it's over the ear, if it's my Apple headphone, I need to have them on.
[1856.74 → 1857.70] Sometimes they're not plugged.
[1857.82 → 1860.52] They're hanging on my side because I move around.
[1860.78 → 1861.80] That is so funny.
[1862.16 → 1863.46] I'm like, oh, it's unplugged.
[1863.46 → 1866.40] But yeah, but I do listen to music.
[1867.40 → 1870.20] House music is very good for me.
[1870.56 → 1871.20] For coding.
[1871.66 → 1873.32] Do you use Spotify by any chance?
[1874.04 → 1875.48] Or do you create your own list?
[1876.22 → 1877.86] I've gotten into Brained personally.
[1878.82 → 1881.80] For me, I've been on the music front at least.
[1882.04 → 1885.92] I will listen to some type of electronic music.
[1886.26 → 1888.66] And so for a while, I was just listening to Electro Now.
[1889.30 → 1890.86] But then I found myself getting upset.
[1890.86 → 1893.40] And I'm like, why am I getting upset?
[1893.46 → 1894.42] Like, what's angering me?
[1894.52 → 1897.30] And it's the music because it's too repetitive, or it's just too beady.
[1897.78 → 1899.86] And so I switch over to like Brain Food.
[1899.98 → 1901.98] It's sort of like the same thing, but a bit more.
[1902.68 → 1905.16] It's kind of like sleep music, but work music mixed.
[1905.44 → 1907.44] And it's kind of like relaxing, but yet motivating.
[1907.62 → 1908.38] I don't know how I get it.
[1908.46 → 1910.00] But yeah, I'm with you, though.
[1910.04 → 1912.94] And some sort of like house music is kind of cool, too, because you kind of have like a
[1912.94 → 1914.36] oomph, oomph, oomph, oomph.
[1915.46 → 1916.36] Maybe something like that.
[1916.42 → 1916.62] I don't know.
[1916.70 → 1916.92] Yeah.
[1918.10 → 1919.04] I'm assuming, right?
[1919.04 → 1920.44] Is that how house music goes?
[1920.56 → 1921.14] Or am I wrong?
[1922.30 → 1922.86] Let me do that again.
[1922.86 → 1924.50] Chick, bump, chick, bump, chick, bump, chick.
[1924.60 → 1925.04] Maybe it's like this.
[1925.04 → 1928.74] It reminds me of, do you guys remember the Strong Bad episodes?
[1929.42 → 1931.14] Like the little cartoon online?
[1931.48 → 1935.18] And the one where he did the how does, he answers an email?
[1936.04 → 1936.38] Mm-mm.
[1936.52 → 1937.38] It's something about.
[1937.58 → 1938.16] You lost me.
[1938.48 → 1938.66] Yeah.
[1938.70 → 1939.32] I'll look it up.
[1939.38 → 1939.88] It's hilarious.
[1940.22 → 1943.98] And it's like, he starts imitating how techno music goes.
[1944.84 → 1946.84] That's so funny, though, Carissa, with the headphones, though.
[1946.86 → 1948.76] Like, even if there's no music, you got to have them on.
[1948.92 → 1949.34] Like, that's.
[1949.36 → 1950.06] I got to have them on.
[1950.16 → 1951.04] I love hearing that.
[1951.18 → 1951.46] Because.
[1951.90 → 1953.76] It's like concentration mode.
[1954.08 → 1954.94] Headphones go on.
[1955.10 → 1955.36] Wow.
[1955.36 → 1957.96] I think that's pretty cool.
[1957.96 → 1964.56] Talking about things that I don't have, I'm very aggressive about turning off notifications.
[1965.66 → 1967.56] I don't get mail notifications.
[1968.82 → 1970.56] I don't get Twitter notifications.
[1971.22 → 1974.12] If I'm looking at it, it's because I took the time to go look at it.
[1974.12 → 1974.40] Mm-hmm.
[1974.72 → 1978.64] So, very important for me to not have stuff popping up all over the place.
[1979.14 → 1979.48] Nice.
[1979.68 → 1980.98] I'm with you on that, for sure.
[1981.12 → 1981.24] Yeah.
[1981.86 → 1984.98] So, Adam, what's your focus mode look like?
[1985.04 → 1988.32] And then I have a question to add to this that kind of came up in this discussion.
[1988.76 → 1991.18] My focus mode, it kind of depends on what I'm doing.
[1991.50 → 1994.24] So, I can't compare it to coding go.
[1994.44 → 1996.22] There are lots of times when I'm writing code.
[1996.32 → 1999.98] There are lots of times when I'm in sketch designing something.
[2000.14 → 2003.56] There are lots of times when I'm in Adobe Audition editing something.
[2003.56 → 2006.62] Or face in front of a mic recording something.
[2006.90 → 2009.34] Or in front of something else writing something.
[2009.44 → 2012.70] I often write a lot of stuff for the sponsors.
[2013.10 → 2014.58] Intro stuff for us.
[2014.80 → 2015.56] All sorts of things.
[2015.86 → 2017.10] So, it kind of depends.
[2017.24 → 2021.18] But focus mode for me is definitely, like Carlisle said, turning off notifications.
[2022.12 → 2023.98] Basically, just closing down Slack.
[2024.10 → 2026.44] I don't have email notifications.
[2026.78 → 2027.90] I silence my phone.
[2028.56 → 2031.70] I have stopped answering the phone because, basically,
[2031.70 → 2034.80] I get nothing but solicitor phone calls.
[2034.94 → 2042.34] Like, if I get a phone call, it's nine times at least, okay, I'll say maybe ten times out of ten, a solicitor.
[2042.56 → 2044.56] So, focus mode for me is, like, turning that thing off.
[2044.68 → 2049.84] I almost don't even use the phone except for maybe to call my wife or doctor or something like that.
[2049.88 → 2051.88] Like, I don't use the phone part of the phone.
[2051.88 → 2056.50] But music, though, I'm, like, a little bit there with Carlisle.
[2056.76 → 2057.96] I got to have some music on.
[2058.02 → 2063.60] Like, if I find myself in, like, a, I'm doing something that requires me to get into flow,
[2064.02 → 2066.92] to get into the flow of doing it and doing well,
[2067.60 → 2070.14] I find myself struggling if I don't have music going on.
[2070.18 → 2072.36] So, if I feel myself kind of dragging, I'm like, what's wrong?
[2072.46 → 2073.66] Why am I not in a groove?
[2074.08 → 2075.94] It's because I haven't turned on my music yet.
[2075.94 → 2081.54] So, I've learned painlessly over time just to, like, at some point turn on some music.
[2081.66 → 2085.18] But I don't always get to do it because it's just, like, if I'm editing or something like that,
[2085.22 → 2091.12] I can't have Spotify or music going on and be editing a podcast
[2091.12 → 2096.28] because it's sort of, like, counterintuitive to, like, have two things of audio competing.
[2096.56 → 2099.48] So, that's why I catch myself a lot not having audio going on.
[2099.56 → 2102.96] But that's kind of focus mode for me is notifications off.
[2102.96 → 2107.22] I do not get email notifications, close things that I'm not paying attention to.
[2107.82 → 2110.58] And I'm a big fan of focus, and that's what I do.
[2111.02 → 2112.84] Yeah, the music thing helps a lot, too.
[2112.94 → 2115.96] Like, I have ADHD, too, so it's hard to get focused sometimes.
[2116.06 → 2119.94] And sometimes just kind of, like, getting in the groove of the music is enough to kind of set you on track.
[2120.54 → 2126.42] So, the question that I had to add to all of this that sort of came up was styles of music
[2126.42 → 2128.28] because this is actually fascinating.
[2128.28 → 2133.60] We did this experiment kind of, like, on a social gathering on one of my work trips.
[2134.34 → 2138.90] And it's actually fascinating to hear what everybody likes to listen to for music,
[2139.02 → 2140.32] what their favourite type of music is.
[2140.50 → 2144.28] And the weird thing is it's usually always something and EDM.
[2145.46 → 2145.56] Right?
[2145.60 → 2149.78] Like, almost everybody's, like, you know, death metal and EDM, you know?
[2149.78 → 2153.98] Yeah, I like break beats a lot.
[2154.36 → 2157.58] I like the dub stuff.
[2157.66 → 2158.50] I like that kind of stuff.
[2158.58 → 2160.94] But then I will easily go and switch on Guns N' Roses.
[2161.36 → 2164.84] Like, I'm a huge fan of, like, their first album.
[2165.22 → 2168.32] I think it's something Destruction or something like that, if I recall correctly.
[2168.52 → 2169.46] Appetite for Destruction.
[2170.32 → 2174.60] So, I'll easily go back and just turn on Paradise City and start doing my moves.
[2174.72 → 2175.04] You know what I'm saying?
[2175.12 → 2176.40] Like, I can't help it.
[2176.40 → 2183.24] So, I'm a metal kind of rock kind of guy, classic rock, Led Zeppelin, Kansas, Styx.
[2183.82 → 2185.56] I'm speaking Brian's love language here.
[2186.24 → 2186.82] You're close.
[2187.26 → 2188.48] You're close, but not quite.
[2189.30 → 2190.90] Who's your number one?
[2190.96 → 2193.28] It's my number one, too, but I didn't say their name yet.
[2193.90 → 2194.34] Dream Theatre.
[2194.50 → 2195.02] Dream Theatre.
[2195.18 → 2195.60] I knew it.
[2195.94 → 2197.10] There is no other band.
[2197.38 → 2198.26] There is no other band.
[2198.94 → 2199.88] That is the best.
[2199.92 → 2203.42] And if you haven't listened to Dream Theatre in a while, like, it's the best.
[2203.82 → 2205.34] Did you all know this is a side topic?
[2205.34 → 2210.68] I'm sorry to take it there, but Katrina Owen, her husband, boyfriend, I'm not sure which
[2210.68 → 2213.12] it is, is a phenomenal drummer.
[2213.54 → 2214.02] Did you all know that?
[2214.88 → 2215.92] No, did not know that.
[2215.94 → 2216.16] Drum quake.
[2216.28 → 2217.78] You look up Drum quake on YouTube.
[2218.56 → 2221.92] You look at that first video, and you will be amazed.
[2222.50 → 2222.90] Amazed.
[2223.02 → 2223.94] This guy is phenomenal.
[2224.74 → 2229.42] He's got a great resume, and could totally hang with Dream Theatre.
[2230.04 → 2231.06] That's how good he is.
[2231.56 → 2232.12] That's big.
[2232.44 → 2233.08] Yeah, it's big.
[2233.08 → 2235.78] How about you, Brian?
[2236.26 → 2237.16] We just did mine.
[2237.82 → 2238.58] I was Dream Theatre.
[2239.58 → 2242.60] And honestly, it's probably the same reason that people like EDM.
[2243.06 → 2247.78] For me, it's the complex beats, complex rhythms, complex key signatures.
[2248.46 → 2251.26] I need something to distract part of my brain so I can work.
[2251.98 → 2253.64] And that's what it boils down to for me.
[2253.90 → 2257.68] I have to distract some other thing so that I can get work done.
[2257.68 → 2259.62] It's probably an ADD thing.
[2259.62 → 2266.82] So for me, I'm not super educated as far as music goes and styles.
[2267.08 → 2273.42] And I'm sure there are styles out there that I would love, but I just haven't found or haven't looked yet.
[2273.88 → 2278.50] I don't geek out on music so much just because I want to be practical.
[2278.50 → 2279.96] It's like, oh, this works.
[2280.12 → 2280.78] I don't have time.
[2281.48 → 2284.66] But I cannot listen to music that has lyrics.
[2285.12 → 2288.44] I love Guns N' Roses, but it won't work for me if I'm coding.
[2289.52 → 2291.38] Because I'll be paying attention to the lyrics.
[2291.52 → 2292.70] I mean, it sounds so nice.
[2293.22 → 2294.04] So I get distracted.
[2294.04 → 2304.86] So what I like to listen to is house music, heavy metal, Black Sabbath, Sepulture, things like that.
[2305.08 → 2305.28] Yeah.
[2305.42 → 2306.42] See, I call them Sepulture.
[2306.90 → 2309.02] Sadly, it's Sepulture's quite right, though.
[2309.74 → 2311.08] Sepulture is how you say it.
[2311.10 → 2311.62] Is that right?
[2311.88 → 2312.22] Okay.
[2312.64 → 2312.86] Yeah.
[2312.86 → 2314.56] I mean, who doesn't love that band?
[2314.64 → 2319.04] I mean, that to me, their first one, I don't even think it's like a Roman numeral, right?
[2319.40 → 2320.10] Their first album?
[2321.08 → 2321.62] I don't know.
[2321.74 → 2322.80] It's amazing.
[2322.80 → 2324.96] Like, it's death metal kind of stuff.
[2325.30 → 2328.98] Or at least the early 90s version of death metal, I guess, maybe.
[2329.12 → 2330.44] But it's amazing.
[2331.02 → 2332.80] I would totally rock out to that.
[2333.42 → 2338.02] So now, if I'm doing something super repetitive, then it's the opposite.
[2338.22 → 2339.68] It's like, I want to listen to a podcast.
[2340.10 → 2342.84] Because I don't want to pay attention to what's happening.
[2343.34 → 2344.38] It's so boring.
[2344.50 → 2345.38] I don't want to pay attention.
[2345.76 → 2346.68] I can do it.
[2347.06 → 2351.60] And then I want my brain to be out of focus from what I'm doing.
[2351.60 → 2356.78] Then I'll listen to a podcast or like Change Log or something like that.
[2357.18 → 2360.34] Dropping notes in the links in the chat there.
[2361.40 → 2361.76] Arise.
[2361.90 → 2362.84] That's the album there.
[2363.16 → 2363.50] Nice.
[2363.80 → 2366.66] I mean, that's like album one or two, I believe, of theirs.
[2366.78 → 2367.76] That might be album number two.
[2368.56 → 2369.00] Phenomenal.
[2369.22 → 2371.36] If I hadn't shaved off all my hair, I'd be headbanging right now.
[2371.46 → 2371.92] Oh, man.
[2371.92 → 2374.66] I mean, I wore the t-shirt.
[2375.08 → 2376.66] I was so young, though, when this came out.
[2376.72 → 2380.78] I think I might have been like 12, maybe 13.
[2381.60 → 2382.28] Sepulture, though.
[2382.92 → 2383.16] Nice.
[2383.16 → 2387.06] So my favourite music, though, I think I could take an entire episode.
[2387.34 → 2389.62] I like to think that I have bipolar music disorder.
[2390.40 → 2392.34] I listen to everything.
[2392.34 → 2396.02] And I think it's because my dad was a DJ growing up.
[2396.18 → 2398.40] So I always got used to listening to everything.
[2398.52 → 2399.70] So I get bored with the style.
[2400.24 → 2406.00] So usually I'll go on like several day kicks for like a week of listening to some type of music.
[2406.36 → 2406.92] I listen to everything.
[2407.08 → 2412.96] I listen to rock, like modern bands, you know, Five Finger Death Punch, Mud Bane, stuff like that.
[2413.06 → 2416.28] I listen to, you know, softer stuff like Three Doors Down and everything.
[2416.40 → 2417.18] I listen to older stuff.
[2417.24 → 2418.32] Like I love Guns N' Roses.
[2418.32 → 2421.06] I'll jam out to Madonna and Whitney Houston.
[2421.24 → 2421.66] I don't care.
[2423.12 → 2425.40] I like hip hop.
[2426.66 → 2428.78] I love EDM.
[2428.94 → 2430.68] There are certain styles I like and some I don't.
[2430.86 → 2432.32] I like dubstep.
[2432.50 → 2433.34] I love to break beats.
[2433.92 → 2437.60] Recently, a little country, but that's still a little new for me.
[2438.12 → 2441.32] I love like late 80s, early 90s freestyle music.
[2442.02 → 2444.02] That was kind of like the precursor to techno.
[2444.68 → 2446.92] Yeah, I listen to just about everything.
[2446.92 → 2452.44] It sounds like we all have similar tastes of music, and we don't even know it to some degree.
[2452.72 → 2454.20] I mean, I would think so.
[2454.30 → 2454.88] Each thing.
[2455.06 → 2456.64] Is it an is it a career thing?
[2456.80 → 2458.00] Like, I don't know.
[2458.26 → 2459.10] Could be an age thing.
[2459.84 → 2460.84] We need to have a party.
[2461.22 → 2464.12] I'd be surprised if I met a 20-year-old who knew Repulsed.
[2465.30 → 2465.66] Yeah.
[2465.74 → 2466.72] And that's not ageism.
[2466.78 → 2467.84] That's just truth.
[2467.94 → 2469.24] I'm they're just an older band.
[2469.30 → 2470.42] I don't even think they're popular anymore.
[2470.42 → 2478.08] And unless you knew somebody who turned you on to them, you probably wouldn't have heard of them because they're kind of I would say this kind of edge to me.
[2478.08 → 2483.30] Like you'd hear about Guns N' Roses for sure because they're sort of mainstream, but Repulsed was more.
[2483.38 → 2486.44] I am super surprised, you know, Repulsed.
[2486.74 → 2488.22] I did not expect that.
[2488.42 → 2489.40] Oh, yeah, for sure.
[2490.16 → 2490.72] Love it.
[2491.04 → 2496.66] There are some bands that I love that I've forgotten that if I heard, I'd tell you, and we probably listen to the same music.
[2497.80 → 2498.46] Sacred Rite.
[2499.26 → 2499.68] Like.
[2499.88 → 2500.10] Right.
[2500.26 → 2503.16] I'm not sure how you'd say it, but phenomenal music there as well.
[2503.88 → 2504.58] Lots of good stuff.
[2504.58 → 2505.72] All right.
[2506.00 → 2509.76] You guys ready to jump into some more stuff and maybe do some go questions?
[2509.94 → 2510.26] It's funny.
[2510.84 → 2511.24] Yeah.
[2511.50 → 2511.86] Kyle.
[2512.14 → 2513.04] Time channel.
[2513.14 → 2516.06] This is some of the people that is work listening for the first time.
[2516.16 → 2517.36] Is this go podcast?
[2518.20 → 2519.10] It is.
[2519.22 → 2519.70] It is.
[2519.76 → 2520.72] It's an it's a unique.
[2521.00 → 2522.58] It's episode 45, by the way.
[2522.68 → 2526.04] So if you want to go back in the backlog, do that.
[2526.64 → 2527.76] You'll find some awesome stuff.
[2527.76 → 2531.92] We are improvising our guest for today.
[2531.92 → 2535.34] I had some scheduling conflicts and could not make it.
[2535.46 → 2539.98] So we are improvising and making this episode get to know the hosts' episode.
[2540.16 → 2540.48] That's right.
[2541.16 → 2545.98] So here is a go related question from Joshua Smith on Twitter.
[2546.08 → 2550.98] He says, what are your thoughts on go as a tooling language for sysadmin slash ops people?
[2551.26 → 2553.58] What resources do you recommend for them?
[2554.16 → 2555.06] Anybody want to take this?
[2555.06 → 2562.46] In terms of resources to be recommended for sysadmin and ops people, I think everything
[2562.46 → 2566.22] that you need as a sysadmin is in the standard library, which is one of the reasons that
[2566.22 → 2574.80] so many ops people like go, especially the static compilation to sysadmins in general have
[2574.80 → 2580.44] been using things like Perl and Ruby and Python to get those jobs done.
[2580.44 → 2585.36] But when you can use go and statically compile a binary and just drop it on a bunch of machines
[2585.36 → 2590.02] and get work done, that's one less thing that you have to install somewhere else.
[2590.30 → 2593.86] But really, in terms of resources, everything you need is in the standard library to get
[2593.86 → 2595.04] sysadmin work done.
[2595.56 → 2596.60] And it's fast.
[2597.42 → 2598.44] Yeah, I'd agree.
[2598.70 → 2603.12] You don't need to install many external modules or libraries, things like that.
[2603.58 → 2607.24] When you make a tool, you can pass it around just the binary.
[2607.24 → 2610.72] You don't have to worry about each host having the proper version of Ruby or Python.
[2611.54 → 2613.32] And I write modules installed.
[2614.08 → 2615.32] That can be a lot of overhead.
[2615.42 → 2615.84] Or Node.
[2615.94 → 2618.40] There are some sysadmin tools that are written in Node, too.
[2619.02 → 2621.28] So yeah, it's just a copy of binary and done.
[2621.28 → 2621.86] Wait, wait.
[2622.10 → 2623.30] Back the truck up.
[2624.18 → 2627.24] Why would anybody write sysadmin tools in Node?
[2628.36 → 2631.40] I'm not hating on Node, but seriously, why would you do that?
[2631.96 → 2633.64] And it's the language you use.
[2634.04 → 2635.88] So it's the language you use, right?
[2635.88 → 2636.78] Oh my god.
[2636.92 → 2640.06] There isn't a nail in the sysadmin world that looks like that.
[2640.66 → 2642.06] That hammer is not built.
[2644.42 → 2645.42] Don't get me started.
[2646.30 → 2646.70] Go!
[2647.06 → 2647.92] Go, Brian, go!
[2648.00 → 2648.84] Go, Brian, go!
[2649.66 → 2650.80] Don't encourage the boy.
[2651.66 → 2654.78] So our next question is, how do you do a code review?
[2655.00 → 2658.04] Do you have a checklist, a recipe, or wiki for reviews?
[2658.04 → 2665.72] There is an awesome code review guideline that I'm pulling up right now on the wiki.
[2666.18 → 2667.38] Code review comments.
[2668.72 → 2669.22] Wait, sorry.
[2669.68 → 2670.42] That's two questions from Martin.
[2670.54 → 2671.66] This is the second question.
[2672.32 → 2672.68] Nice.
[2673.34 → 2674.98] Let me see if I can find this.
[2675.36 → 2677.04] So while you're looking for that, I'll answer.
[2677.46 → 2677.76] Okay.
[2677.76 → 2682.36] I like to have at least two people review a fresh pair of eyes.
[2682.48 → 2687.06] Hopefully one is at least familiar with the domain, which those people, usually because
[2687.06 → 2691.74] they're not trying to learn the domain of what you're doing, are typically looking for
[2691.74 → 2694.66] style and things like code correctness.
[2694.66 → 2699.80] And I like to have somebody who's not familiar with the domain because then they make me question
[2699.80 → 2700.76] my implementation.
[2701.20 → 2702.56] Like, is this the right route?
[2702.70 → 2704.48] Did I even need to build this?
[2705.14 → 2706.40] And things like that.
[2707.06 → 2708.90] Often you get too close to the problem.
[2709.44 → 2714.24] And there are some cool tools too, like Review Dog, which can automatically do some stuff.
[2714.94 → 2721.02] There's the Go meta linter that can catch a lot of stuff as far as, you know, stylistic
[2721.02 → 2722.84] things, idiomatic Go.
[2722.84 → 2727.90] I hate relying on those automated tools though, because they don't bring any domain knowledge
[2727.90 → 2732.12] and they don't bring any logic or reason to a code review.
[2732.20 → 2734.28] I think they should be part of your CI system.
[2734.98 → 2740.96] You know, you shouldn't be able to, you know, just paste sloppy code into an editor and expect
[2740.96 → 2741.90] that to go to production.
[2742.38 → 2746.14] But there has to be a human looking at that code and saying, you know, it makes zero sense
[2746.14 → 2751.58] to allocate this variable 57 times when you could have done it outside the loop.
[2751.58 → 2754.46] And those are things that the linters don't always catch.
[2755.26 → 2755.90] Oh, absolutely.
[2756.18 → 2757.80] You should not rely on that solely.
[2758.30 → 2762.30] So on that note, you got this library that's pretty popular in JavaScript right now called
[2762.30 → 2762.64] Prettier.
[2763.26 → 2768.28] And I think that's kind of what the purpose of that is, is basically like write sloppy
[2768.28 → 2769.64] code, and it cleans it up for you.
[2769.72 → 2772.24] So you're against that style of programming?
[2772.24 → 2780.84] I'm not against any style of code review tools that reduce the ugliness of your code and reduce
[2780.84 → 2782.60] computer catchable errors.
[2782.70 → 2786.36] I'm just saying that that should be, you know, the first preliminary step.
[2786.58 → 2790.34] There should be a human behind that actually looking at the code nicely.
[2790.34 → 2794.80] Just counting on Covet or any of the GoMetalinter isn't enough.
[2795.46 → 2798.48] And anybody else have anything they want to throw in there or next question?
[2798.48 → 2799.74] I got nothing.
[2800.66 → 2801.06] Me neither.
[2801.88 → 2805.38] Next question is from Daniel Morgan on the Slack channel.
[2805.88 → 2808.62] He said, what's the silver bullet for imposter syndrome?
[2810.14 → 2813.14] And even in his question, he noted that...
[2813.14 → 2813.92] I got an answer for you.
[2814.74 → 2815.02] Own it.
[2815.02 → 2815.66] Yeah, me too.
[2816.36 → 2817.64] Just be the imposter.
[2817.80 → 2818.04] Own it.
[2818.04 → 2818.34] That's right.
[2819.14 → 2819.56] Absolutely.
[2819.70 → 2820.70] That's exactly it.
[2820.78 → 2821.56] Just do it.
[2822.10 → 2822.58] Just do it.
[2822.58 → 2825.60] And if you need to take it down a notch from the thing that you really want to do,
[2825.60 → 2829.78] take it down a notch, but just go ahead and do it because you do it, you're going to...
[2829.78 → 2832.38] You figure it out is not as painful as you thought.
[2832.76 → 2832.96] Yeah.
[2833.04 → 2833.26] Yeah.
[2833.64 → 2833.96] I agree.
[2834.06 → 2834.88] Put yourself out there.
[2835.16 → 2837.66] Everybody else knows just as little as you do.
[2838.42 → 2839.12] It's okay.
[2839.62 → 2840.56] And I think...
[2840.56 → 2842.04] I don't even remember where I saw it.
[2842.06 → 2843.30] I'm pretty sure it was on Twitter this morning.
[2843.40 → 2848.24] Somebody said very specifically, you admit what you don't know and own what you do.
[2848.88 → 2853.14] And I wish it was somebody probably talking at craft conference today because that was one
[2853.14 → 2854.82] of the larger themes of Twitter this morning.
[2855.44 → 2857.52] But I think that makes wonderful sense.
[2857.64 → 2860.30] Admit what you don't know and own what you do.
[2860.82 → 2863.84] You know, the thing is, too, does people fear that kind of stuff, right?
[2863.88 → 2865.96] Like, I'm there, too.
[2866.12 → 2869.64] But, like, you just can't live in fear of judgment from other people.
[2870.02 → 2872.06] And it's so easy to say that and not live it.
[2872.18 → 2875.10] But that truly is the way out of imposter syndrome.
[2875.20 → 2876.14] It's just like, don't...
[2876.80 → 2880.46] Like, care about how people feel about you, I guess, but don't make it so important to
[2880.46 → 2883.76] you that you become paralyzed to do something, you know?
[2883.76 → 2884.04] Mm-hmm.
[2884.04 → 2890.28] Don't let fear of the crowd or fear of the impression of anybody pull you down, you know?
[2890.56 → 2891.96] Just bypass it.
[2892.62 → 2895.58] So I happened to see a tweet last night, too, and it was funny.
[2895.78 → 2899.70] The hip-hop group D12 actually tweeted this.
[2899.82 → 2900.04] What?
[2900.06 → 2904.24] But it's a clip of Gary Vaynerchuk, who I love.
[2904.84 → 2907.98] That man, like, he's such a motivational guy.
[2907.98 → 2912.78] Like, you know, but in part of his thing, he kind of talks about the movie Eight Mile
[2912.78 → 2915.16] and, you know, at the end with Eminem or whatever.
[2915.64 → 2920.80] He's like, you know what he figures out and what everybody should figure out, like, is
[2920.80 → 2924.56] that if you own the things that you're not good at, and you just put them out there for
[2924.56 → 2924.92] everybody.
[2925.04 → 2925.44] That's the truth.
[2926.00 → 2926.16] Yeah.
[2926.22 → 2927.64] There's nothing left.
[2927.74 → 2930.90] And then you can spend your time on the offence rather than the defence.
[2931.08 → 2931.54] That's so true.
[2931.60 → 2932.40] I tell you, he won that battle.
[2932.48 → 2936.04] He won that battle by saying, here's all the things you might say about me.
[2936.04 → 2937.50] And here's how I'm twisting it back on you.
[2937.58 → 2938.62] And he won the battle.
[2939.40 → 2939.62] Yeah.
[2939.96 → 2944.42] And Eminem in general, his music, that is all about owning it.
[2945.12 → 2949.68] You are, you know, just be authentic and know that you have a value.
[2949.94 → 2950.12] Yeah.
[2950.70 → 2951.44] I love Eminem.
[2952.10 → 2956.16] I think it's something you have to remind yourself of almost every day, too.
[2956.16 → 2962.30] Like a lot of people, the view that you see of people from the outside is not how they
[2962.30 → 2963.34] feel about themselves.
[2964.02 → 2969.10] You know, you might hear us on the podcast, and we may seem very outgoing and all these
[2969.10 → 2972.18] things, but it's a role we play, right?
[2972.34 → 2974.06] We're all playing games here, okay?
[2974.62 → 2975.90] We are all faking it.
[2976.12 → 2977.06] It's a mask.
[2977.88 → 2980.56] We're not all as confident as we may seem.
[2980.72 → 2983.54] Every Thursday, I hang up and go cry in the corner.
[2983.54 → 2986.78] Well, you know, that reminds me very specifically.
[2986.98 → 2989.88] Somebody asked, we would love to watch you code real time.
[2989.98 → 2991.22] Could you live stream some coding?
[2991.76 → 2995.40] And the first thing I thought was, why in the sweet name of anybody would you want to
[2995.40 → 2997.52] watch me fumbling around writing code?
[2998.34 → 2999.68] And that's imposter syndrome.
[3000.04 → 3001.02] I'll own it.
[3001.24 → 3001.64] It's true.
[3001.64 → 3003.66] I'm terrible about it.
[3003.76 → 3010.12] And I'll fully admit, like, this show is actually me forcing myself to put myself out there and
[3010.12 → 3011.76] make mistakes and say things wrong.
[3012.36 → 3015.28] It took me a while to even think about wanting to do the show.
[3015.50 → 3017.34] And I've become more and more comfortable with it.
[3017.46 → 3019.42] Like, hey, the world's not over if you say something wrong.
[3019.62 → 3021.88] But yeah, I think you just got to own that fear.
[3021.98 → 3023.02] Put yourself out there.
[3023.02 → 3029.44] You know, anybody who's willing to take those mistakes that you have and turn them against
[3029.44 → 3031.74] you are not worth your time anyway.
[3031.88 → 3033.58] So who cares what they think, you know?
[3034.16 → 3035.40] Yeah, that's true.
[3036.02 → 3042.12] Part of that is growing up and accepting constructively meant criticism or correction, too.
[3042.78 → 3047.62] You know, when you leave your ego at the door, it's easy for you to accept somebody saying,
[3047.62 → 3050.66] you know, you really shouldn't have used a pointer there or whatever.
[3050.82 → 3052.00] You forgot the mute.
[3052.66 → 3060.86] And that's perfectly acceptable for you to accept that correction without it being a sign
[3060.86 → 3062.98] of your incompetence.
[3063.32 → 3066.80] And learning that difference is harder than you would imagine.
[3067.80 → 3069.30] So the next one's kind of fun one.
[3069.42 → 3074.76] And I think it evolved from maybe a question that Scott Mansfield asked, and it's what emoji
[3074.76 → 3076.52] represents you best and why?
[3077.62 → 3078.68] I'll start.
[3079.02 → 3083.48] So I added an emoji like early on in the Slack thing.
[3083.80 → 3087.70] And it's the character's Row, but from Monsters, Inc.
[3088.46 → 3090.12] Always watching, Wazowski.
[3090.44 → 3091.14] Always watching.
[3091.74 → 3095.58] And I think that's because I usually, you know, I'm usually around.
[3095.76 → 3101.66] Like I watch Twitter, I watch Slack, but I'm not always like actively engaged, just watching.
[3102.22 → 3103.22] Anybody else?
[3103.74 → 3104.80] So you're a lurker.
[3105.48 → 3106.64] Self-professed.
[3106.64 → 3107.82] Now we know.
[3108.44 → 3109.92] Eric is totally a lurker.
[3110.66 → 3112.90] His Twitter behaviour is unique.
[3113.96 → 3116.20] But part of that's imposter syndrome, right?
[3116.32 → 3117.90] Like, it's like, should I really say this?
[3118.20 → 3118.50] You know?
[3118.84 → 3119.06] So.
[3119.76 → 3123.24] I'm going to take the easy way out and say that the barbecue gopher emoji is mine because
[3123.24 → 3123.82] it's so true.
[3124.68 → 3126.38] And if I'm not coding, I'm barbecuing.
[3126.88 → 3129.14] I was going to use that one, but I thought that was too obvious.
[3129.72 → 3130.16] It is.
[3130.24 → 3132.06] And I'm just totally copping out on that.
[3132.16 → 3132.44] I'm sorry.
[3132.94 → 3133.76] That is a cop out.
[3133.76 → 3134.78] So pretty easy.
[3134.90 → 3135.18] Well, okay.
[3135.18 → 3137.94] So which one least best describes you?
[3138.38 → 3139.58] Is that how you say that?
[3139.72 → 3140.40] Or is it?
[3140.84 → 3141.76] Yeah, that's probably good.
[3141.94 → 3142.48] Least good.
[3143.14 → 3143.92] The party parrot.
[3144.00 → 3144.46] The opposite.
[3145.46 → 3146.14] That's stupid.
[3146.64 → 3147.14] Party parrot.
[3147.14 → 3149.36] I hate that party parrot.
[3149.46 → 3150.40] I'm not sure what it represents.
[3150.50 → 3151.06] What does it represent?
[3151.62 → 3153.04] I don't know, but it's just obnoxious.
[3153.18 → 3154.36] It makes me want to have a seizure.
[3155.12 → 3156.14] We have to outlaw it.
[3156.16 → 3159.48] For me, I cannot, I can't pick just one.
[3159.90 → 3165.04] I have to pick two because it'll have to be the screaming one or the laughing one.
[3165.16 → 3169.36] The one that has tears in their eyes because that's most of the time, that's where I am.
[3169.48 → 3171.74] I'm either screaming or laughing, cracking up.
[3171.74 → 3172.22] Yeah.
[3172.48 → 3179.26] Well, if I, if I had to pick one, so in our change log slack, we actually have some custom
[3179.26 → 3179.62] ones.
[3179.70 → 3181.86] So I, my wife put my face in there.
[3181.92 → 3183.66] So technically that would be the best one.
[3183.84 → 3184.56] Oh, come on.
[3184.66 → 3190.00] But if I'm looking at my frequently used list, sadly, I like the wink a lot and thumbs up
[3190.00 → 3190.30] things.
[3190.30 → 3194.88] But I would say the one that represents me best is the 100 with two lines.
[3195.22 → 3197.64] Because I'm down always, you know, I'm excited.
[3198.20 → 3198.98] This is true.
[3198.98 → 3205.22] I'd say at least 98% of the time that the other 2%, yeah, it's just, it's a better time.
[3205.32 → 3205.94] Different time.
[3206.40 → 3207.34] Take it till you make it.
[3207.52 → 3207.68] Yeah.
[3208.44 → 3209.82] So a hundred percent.
[3209.92 → 3210.86] That's something I actually say.
[3210.92 → 3215.82] I've been seeing like, like in response to somebody, like, uh, instead of saying I agree
[3215.82 → 3218.58] or cool or whatever, I say a hundred percent.
[3219.36 → 3220.48] I've been doing it for years.
[3221.04 → 3222.22] Maybe I heard it from somebody.
[3222.36 → 3225.04] I don't know, but people coin it.
[3225.34 → 3226.70] People say I started it.
[3226.78 → 3227.96] I don't believe them.
[3227.96 → 3229.08] Next.
[3229.78 → 3229.98] Yeah.
[3230.00 → 3232.70] So there's a question here from, uh, Joe Shaw.
[3232.86 → 3234.92] He says, maybe you could talk about your day jobs.
[3235.02 → 3239.02] You mentioned them a little bit in passing and shows, but as far as I can remember, never
[3239.02 → 3241.92] really talk about what you do on a day-to-day basis.
[3241.92 → 3243.70] You work exclusively in Go.
[3244.20 → 3245.40] Anybody want to take this first?
[3246.22 → 3248.68] I think we talked about what I do on a day-to-day basis.
[3248.80 → 3250.34] I shoot actors and make barbecue.
[3252.78 → 3254.36] And think about Go while doing Go.
[3254.36 → 3255.36] What are you supposed to do?
[3255.36 → 3256.60] Not necessarily in that.
[3256.68 → 3257.40] No, that's not true.
[3257.86 → 3260.92] I, I teach Go and Kubernetes for a living.
[3261.16 → 3266.54] So if you need training for your company and Go or Kubernetes, I'm your guy.
[3267.18 → 3271.46] And lately I've been spending a lot of time since the first quarter is pretty quiet for
[3271.46 → 3277.78] training, spending a lot of time building a completely self-driven, uh, online system
[3277.78 → 3278.46] for learning Go.
[3278.46 → 3280.48] And I hope to be launching that in the next couple of weeks.
[3281.48 → 3281.84] Really?
[3281.98 → 3282.14] Yeah.
[3282.72 → 3283.10] It's true.
[3283.34 → 3284.48] And it's, it's really awesome.
[3284.48 → 3284.84] Actually.
[3285.12 → 3286.20] I'm excited about that.
[3286.60 → 3287.36] Really awesome.
[3288.20 → 3288.54] Yeah.
[3288.56 → 3290.06] I can't wait to take one of your classes.
[3290.78 → 3291.96] That's a good question.
[3292.06 → 3295.52] How can someone take a class from, from you, Brian?
[3296.18 → 3301.54] Well, they could, uh, bring me out to their company and I would do the class or if it's
[3301.54 → 3304.06] just a one-on-one, I do remote classes.
[3304.40 → 3309.30] I've been spending a lot of time over the last two months with a development group in
[3309.30 → 3312.46] Ukraine and I get up really, really early and teach them.
[3312.52 → 3313.22] And that's a ton of fun.
[3313.38 → 3313.56] Wow.
[3314.82 → 3315.68] Five in the morning.
[3316.32 → 3317.42] Uh, I wish.
[3317.58 → 3317.78] Three?
[3318.26 → 3318.98] Four 30.
[3319.10 → 3319.22] Yeah.
[3319.32 → 3319.60] Wow.
[3319.76 → 3319.96] Yeah.
[3319.96 → 3320.38] That's early.
[3321.18 → 3321.30] Too early.
[3321.30 → 3322.84] But they're really, really sharp students.
[3322.84 → 3324.86] And it's, it's been one of my favourite classes that I've done.
[3325.56 → 3325.96] Wow.
[3326.82 → 3329.56] Carlisle works at my, one of my favourite companies.
[3330.50 → 3330.90] Yeah.
[3330.90 → 3331.74] Vastly.
[3331.90 → 3332.62] I love Vastly.
[3333.78 → 3336.88] And it's funny because Joe Shaw works at Vastly too.
[3337.00 → 3339.60] And he's my coworker, and we work closely together.
[3340.08 → 3342.16] So he already knows the answer to this question.
[3343.34 → 3344.10] I know.
[3344.14 → 3344.46] Cheater.
[3344.94 → 3347.58] For one of us, he doesn't know for the two of you.
[3348.28 → 3351.72] He's the one who does code refuse for me and vice versa.
[3352.16 → 3353.20] We are on the same team.
[3354.08 → 3355.26] Joe is awesome, by the way.
[3355.26 → 3359.18] So for, for the listeners who are not Joe Shaw, what do you do?
[3359.74 → 3360.62] What do I do?
[3360.62 → 3361.06] Yeah.
[3361.06 → 3363.66] I'm only doing go what I was doing.
[3364.28 → 3367.12] So I work for Vastly and that's a CDN company.
[3367.76 → 3375.44] And I'm on a team that's rebuilding, let's say the TLS and DNS management system.
[3375.44 → 3379.22] So there is a lot for me to learn in that domain.
[3380.22 → 3384.22] And can you explain what a CDN is for those of us who do backend code?
[3384.22 → 3385.62] Yes.
[3385.62 → 3402.50] So a CDN is what you would like to use if you want to reduce the latency of your website's loading, because obviously the further physically the user is from your, where your content is sitting, the more latency there will be.
[3402.50 → 3406.68] So if you use a CDN, that CDN is going to replicate your content.
[3406.68 → 3414.68] And it's just going to greatly reduce that to the point of not even being noticeable.
[3414.68 → 3420.78] Now that's a very simplistic way of explaining what a CDN is.
[3420.78 → 3428.98] And also there are other features that you get with it, which is protection from DDoS attacks.
[3429.34 → 3431.28] You know, the CDN will take care of that for you.
[3431.28 → 3438.14] So the security, the CDN is the front gate for your system.
[3439.14 → 3445.66] So a lot of things that you should be worrying about, if you use a CDN, you won't have to.
[3445.98 → 3449.62] So besides the content replication, you get a lot of other features.
[3450.10 → 3450.18] Yeah.
[3450.22 → 3452.70] We actually use Vastly.
[3452.84 → 3460.00] So if you listen to this show via the podcast, not just live, the reason why it's so fast is because of Vastly.
[3460.00 → 3464.68] Because we use Vastly as a CDN to make our site fast.
[3464.74 → 3466.50] So if you go to changelog.com, it's superfast.
[3466.70 → 3472.04] One, because of Elixir and how fast it is in Phoenix, but also because of Vastly and our downloads for that.
[3472.18 → 3472.84] It's super awesome.
[3473.62 → 3477.32] And I'm not just saying that, but they're phenomenal.
[3477.78 → 3478.70] And it's so easy.
[3478.76 → 3482.52] Like if we have to purge something, it's easy to hop into the admin and purge something and replace it.
[3483.10 → 3484.62] Very, very easy to use.
[3484.88 → 3486.24] We track downloads through it.
[3486.28 → 3488.56] Our whole stats platform is built on the API.
[3488.56 → 3490.56] I believe we use version two.
[3491.10 → 3492.26] A lot of fun stuff.
[3492.46 → 3492.82] Love it.
[3493.28 → 3494.36] How about you, Adam?
[3494.44 → 3495.48] You want to talk about your day job?
[3496.62 → 3497.70] My day job.
[3497.92 → 3499.34] Jeez, I wear so many hats.
[3499.74 → 3500.62] What do you do?
[3500.74 → 3504.82] At any given moment, I could be on a podcast.
[3505.04 → 3508.16] Believe it or not, a large part of my job is sales.
[3509.10 → 3511.76] My lord, I do so much sales.
[3512.10 → 3512.80] It's crazy.
[3514.70 → 3515.96] Mostly relationships.
[3515.96 → 3519.92] It's really probably the easiest way to describe what I do is really about relationships.
[3519.92 → 3529.46] It's like everybody from the software development community to open source to people who are involved in open source to companies who want to sponsor our shows.
[3529.82 → 3532.06] And it's not just them giving us money.
[3532.06 → 3538.66] It's like we really like to work with companies that perfectly align with our podcast and things we do.
[3539.40 → 3544.54] And the relationships we form from that, like we have so many people we've worked with over the years that like they're good friends.
[3544.66 → 3549.46] I can call them and like just say hello and get birthday cards from there or whatever.
[3549.54 → 3550.04] Hang out.
[3550.04 → 3580.02] Hang out.
[3580.04 → 3585.44] And what we do here at the Changelog, it's our core motto is to enrich the lives of developers.
[3585.74 → 3598.00] Like our jobs to do what we do here is to hopefully bring you joy, make your jobs more fun, make life more fun, help you get to that next step, face your imposter syndrome or get over it.
[3598.00 → 3603.56] So that's the core thing we do is just make people's lives better, help people.
[3603.90 → 3604.36] That's what I do.
[3604.54 → 3605.20] Help people.
[3605.20 → 3607.54] So then I guess I'll finish this up.
[3607.90 → 3613.92] So my day job, I'm actually a systems architect at Comcast in the cable division.
[3614.78 → 3616.84] So for cable, there's really kind of two sides of it.
[3617.00 → 3623.56] There is the newer kind of IP based delivery similar to the way like Netflix or Hulu delivers.
[3623.56 → 3628.08] And then there's what we call AM, which is Quadrature Amplitude Modulation.
[3628.78 → 3632.72] And that's how cable is delivered across the coax cable that comes in your house.
[3633.42 → 3635.96] So I work on with that group.
[3636.58 → 3649.96] And currently I work on a project for replacing kind of industry specific hardware that's used to multiplex multiple video streams together into a single stream that gets modulated out of that cable.
[3649.96 → 3652.86] So I'm replacing that with software.
[3653.56 → 3655.62] So the software itself is written in C++.
[3655.90 → 3657.60] There was a question about all Go.
[3658.14 → 3659.92] I primarily work in Go.
[3660.12 → 3662.32] Occasionally I have to patch that software.
[3663.18 → 3666.72] But mostly another team works on that that's written in C++.
[3667.40 → 3672.82] But a lot of what I do is design and build kind of the orchestration system surrounding that.
[3673.16 → 3677.88] How those video streams get deployed, how they fail over when a blade goes down,
[3677.88 → 3681.66] or when an entire head end goes down, and things like that.
[3682.32 → 3686.04] So anybody who's really interested in that,
[3686.56 → 3697.34] I actually did a talk back in November at Rubicon about this project as we're kind of rolling out IP and how to leverage the same networks.
[3697.92 → 3701.12] That's actually on YouTube if anybody's actually really interested in it.
[3701.12 → 3704.62] But yeah, mostly Go, mostly Kubernetes and containers.
[3705.30 → 3713.54] I'm fortunate enough that they let me work on patches to Kubernetes and Docker to help support some of the stuff we're wanting to do.
[3714.28 → 3715.70] And not just little patches either.
[3716.00 → 3716.86] Gigantic patches.
[3717.06 → 3717.74] Awesome patches.
[3718.38 → 3719.54] The biggest patches ever.
[3720.48 → 3720.84] They are.
[3720.94 → 3722.48] Some of your patches are crazy awesome.
[3723.04 → 3724.00] Especially to Docker.
[3724.62 → 3725.34] So don't be shy.
[3725.34 → 3728.34] So another question from Joe Shaw.
[3728.64 → 3731.46] And this one especially is important because Adam is here.
[3732.30 → 3738.68] While I'm on the topic of behind the scenes stuff, I'm also interested in the production of the podcast itself.
[3739.34 → 3743.54] So you want to talk about how this show is done?
[3744.72 → 3745.82] Yeah, where to start?
[3747.00 → 3748.88] Well, we get some people together.
[3749.36 → 3749.86] I'm just kidding.
[3749.86 → 3756.14] I think this show is a little bit different from, say, other shows.
[3756.36 → 3758.50] Like, for example, I'll compare it against the changelog.
[3759.18 → 3766.32] That show is sort of like a two-on-one or a one-on-one kind of scenario where it's more conversational.
[3766.66 → 3769.44] Where this one is kind of like that, but it's more panelists conversational.
[3770.00 → 3771.52] We also don't do that show live.
[3771.64 → 3776.72] So I don't think we can get the same kind of conversation if the show was live.
[3776.72 → 3784.52] So when you do a show live like Go Time, you kind of have to inherit some things like, well, people are going to be hanging out in Slack.
[3784.64 → 3786.78] And that's part of the show.
[3787.02 → 3796.20] Like, it may not end up in the show, but it reflects and sort of, like, helps give the show some attributes and attitude, so to speak.
[3796.32 → 3799.10] You know, like, you can tell a live show versus a non-live show.
[3799.56 → 3803.82] And we just figure with Go Time, it would be best to start doing it live.
[3803.94 → 3805.26] And that's one big thing.
[3805.26 → 3810.56] So the way we make that do it, like, I guess the technical pieces of that, we have a web service called Wave Streamer.
[3810.66 → 3815.66] And we point Nice Cast to it, and we just broadcast everybody here to that.
[3815.76 → 3818.98] That's the easiest way to describe that.
[3819.36 → 3820.04] It works.
[3820.26 → 3824.52] I wouldn't say it's my favourite way of doing it, but it does work, and it's been reliable.
[3824.92 → 3827.44] We only had one issue, and it was user error.
[3827.56 → 3828.20] It was my error.
[3828.20 → 3833.44] So the time we had those live issues, it was not tech fault.
[3833.56 → 3834.64] It was Adam's fault.
[3834.76 → 3835.64] So I was an idiot.
[3836.28 → 3838.72] We have a pretty interesting setup here, though.
[3839.20 → 3842.16] We have a tower that is about 21 news.
[3842.36 → 3844.34] I don't know why it's 21 and not 20, but whatever.
[3844.34 → 3851.88] 21 news, a multichannel interface, four Mac minis, which act as individual Skype machines.
[3853.06 → 3859.82] And basically, Eric, Brian, Carissa, and the guest tend to hang out on those four individual machines,
[3859.88 → 3861.64] like each one to its own machine.
[3861.64 → 3869.82] That gets plugged into the audio interface, which then goes into the Mac Pro, which then gets tracked to whatever DAW I'm using.
[3869.96 → 3875.64] And in this case, a DAW is a digital audio workstation is what that means.
[3875.98 → 3877.90] And I use Adobe Audition.
[3878.06 → 3880.90] It's my preferred one because I love JKL.
[3881.26 → 3882.02] Long story short.
[3883.60 → 3884.40] What else?
[3884.66 → 3885.64] Yeah, we track it into there.
[3885.72 → 3887.54] It's multichannel, so I'm on my own channel.
[3887.54 → 3893.46] Eric, Brian, and Carissa, they're in their own channel, so I can independently move around the timeline and make edits
[3893.46 → 3897.72] and independently EQ or level each individual guest.
[3897.80 → 3906.70] That's why it's a little easier having crappier mics, so most of our guests don't have professional mics like we all do.
[3907.52 → 3910.52] They tend to be just like whatever headsets, you know?
[3910.52 → 3918.74] So you make that better by isolating it to its own channel, and you can then fine-tune it.
[3918.82 → 3927.08] Now, you can't correct it, make it a better mic, but it's one way we combat having bad-sounding shows is by this process.
[3927.62 → 3929.26] There are other ways to do podcasting.
[3929.40 → 3932.06] There are services out there that do some of this stuff.
[3932.34 → 3937.36] We've been educated, you know, what those services are and how they work and how they're better.
[3937.36 → 3940.00] But this is how we do it, and this is how we like it.
[3940.18 → 3941.44] And so there you go.
[3941.86 → 3943.50] But that's pretty much it.
[3943.52 → 3944.16] What else can I share?
[3944.32 → 3945.00] What do you think?
[3945.14 → 3945.34] What else?
[3945.74 → 3950.58] Yeah, so I'd like to just kind of give a shout-out to the unsung heroes.
[3950.92 → 3954.18] So behind the scenes, Adam, and Adam comes in.
[3954.44 → 3960.06] But Jared Santo, also from Changelog, he's always behind the scenes, and he's throwing in ideas.
[3960.26 → 3960.50] Santo.
[3961.18 → 3961.62] Santa.
[3962.06 → 3962.88] Not Santa.
[3963.66 → 3964.50] Not Santa.
[3964.86 → 3965.20] I said Santo.
[3965.20 → 3968.36] He brings gifts, but anyway, Santo.
[3968.66 → 3969.20] Jared Santo.
[3969.66 → 3976.54] Did a ton of the work, or maybe all the work on the Changelog and Go Time CMSs.
[3976.60 → 3976.80] Yeah.
[3977.62 → 3978.54] Somebody had mentioned it.
[3978.54 → 3979.18] It's one CMS.
[3980.08 → 3981.36] It's one CMS.
[3981.46 → 3981.74] Right.
[3981.80 → 3982.66] And one CDN.
[3983.28 → 3986.52] But everybody sees it as kind of two separate podcasts.
[3986.52 → 3997.60] Somebody this morning also mentioned the difference between kind of the sound that comes from the live stream and the final produced episodes.
[3998.22 → 4001.00] And that's a huge thank you to Jonathan Young blood.
[4001.12 → 4001.38] That's right.
[4001.38 → 4002.78] He's who makes us sound awesome.
[4003.16 → 4003.66] He does.
[4003.86 → 4005.26] He does an amazing job.
[4005.26 → 4013.18] And without him, I would be in a ball crying like Galicia does after the show.
[4013.50 → 4014.60] I would just be...
[4014.60 → 4018.54] And just to be clear, he does the editing of the show.
[4018.60 → 4019.00] That's right.
[4019.08 → 4019.34] Yeah.
[4019.74 → 4023.44] Which I appreciate because I was doing the editing.
[4023.60 → 4024.38] It's a lot of work.
[4024.50 → 4025.32] It's a lot of work.
[4025.56 → 4026.36] It's a lot of work.
[4026.52 → 4027.20] I mean, I'm sorry.
[4027.32 → 4028.84] Let me correct what I just said.
[4028.84 → 4030.56] I didn't do the editing.
[4030.80 → 4031.94] I did the show notes.
[4032.02 → 4032.18] Yes.
[4032.18 → 4035.34] And he does the editing, which is a tremendous amount of work.
[4036.36 → 4038.68] And he also is doing the show notes.
[4038.84 → 4039.18] That's right.
[4040.16 → 4049.78] The reason why we do edit the show, though, is because just to smooth it out, not to journalistic it or make it NPR.
[4050.02 → 4050.82] It's not that.
[4050.90 → 4052.00] It's just to smooth it out.
[4052.00 → 4059.26] Because the live experience, if you listen live, or you listen to the produced version that goes on the podcast feed, they sound somewhat different.
[4059.66 → 4062.18] One has ads and the other doesn't.
[4062.26 → 4063.88] So that's a reason to come listen live.
[4064.04 → 4067.36] But you kind of get this more raw take on the live version.
[4067.40 → 4070.54] And we don't produce the live version as a produced version.
[4070.64 → 4071.76] It's just meant to be raw.
[4071.96 → 4075.86] So it's not a live production that just gets turned into a show.
[4076.26 → 4079.40] We allow people to listen to a live, and we welcome that.
[4079.46 → 4080.16] We want that.
[4080.16 → 4091.08] But then we take it behind the scenes, and we polish it up and make it a little bit easier for somebody to listen to that may not be that into the raw side of things, so to speak, in terms of how the show is done.
[4091.54 → 4093.12] I love the live part of the show.
[4093.24 → 4097.88] I don't even think I would want to do it if we weren't broadcast live and if it didn't have that live feel.
[4098.16 → 4098.38] Yeah.
[4098.62 → 4099.46] For me, that's huge.
[4101.24 → 4102.64] It's part of the Go ethos.
[4102.78 → 4103.48] We're inclusive.
[4104.42 → 4105.24] Everybody's involved.
[4105.64 → 4108.80] And it's not people up on a tower handing down news.
[4108.80 → 4112.20] It's everybody in the community being part of the process.
[4112.44 → 4113.90] And that's what I love about it the most.
[4114.88 → 4115.48] I fully agree.
[4115.66 → 4122.94] The live part, that's why I like to chat after the show because it's just kind of fun having people there and hanging out and stuff like that.
[4123.10 → 4124.60] I like the raw side of things.
[4125.12 → 4125.32] Yeah.
[4125.34 → 4127.72] I love the dialogue between the listeners.
[4128.08 → 4134.06] It doesn't feel so much like just recording some material that's just going to get posted somewhere.
[4134.06 → 4137.32] It feels more like a real, true interaction with the community.
[4137.96 → 4144.58] So if people have time to come at 3 p.m. Eastern and jump in the channel, we love that stuff.
[4144.84 → 4145.04] Yeah.
[4145.12 → 4146.32] Even if you come for the aftershow.
[4146.32 → 4147.16] And appreciate it.
[4147.24 → 4148.80] I mean, we love it and appreciate it.
[4149.20 → 4155.56] It wouldn't be the show if we didn't have the Go Time FM channel and those who hang out there every single week.
[4155.60 → 4156.00] It's awesome.
[4156.00 → 4161.50] And then the other person would be Break master Cylinder who does our intro music.
[4161.82 → 4163.36] Ooh, Break master Cylinder.
[4164.02 → 4171.72] Yeah, Break master is very fun to work with, very awesome to work with, and is relentless.
[4172.44 → 4180.74] And I say that with capital letters, underlined, bolded, relentless with delivering the best stuff.
[4180.74 → 4183.54] And what I mean by that is attention to detail.
[4184.10 → 4185.40] He wants us to be happy.
[4185.40 → 4187.36] Hey, did it work out great?
[4187.46 → 4194.92] Does the Go Committee love his updated version of the which is essentially inspired by the original.
[4195.08 → 4202.54] So for those who went back to episode one through maybe 20, you'll hear one version of the intro music or our theme music, so to speak.
[4202.56 → 4205.22] And then the second version, which is Break master Cylinder.
[4205.34 → 4209.26] So when we kind of did a rebranding, we went back and updated all of our music.
[4209.40 → 4211.72] And that's why you hear the changelogs music is different as well.
[4211.72 → 4217.88] But we wanted a kind of certain thread between all of our music and Break master's awesome.
[4218.40 → 4218.50] Yeah.
[4219.10 → 4221.44] So I think that we are over time.
[4221.82 → 4222.78] And I know that there were...
[4222.78 → 4222.98] 12 minutes over.
[4222.98 → 4223.66] Yeah.
[4223.66 → 4225.22] I know that there were some other questions.
[4225.22 → 4228.36] And we will probably try to save these and talk about them later.
[4228.78 → 4230.94] I know we kind of deferred some Gopher Con stuff.
[4231.48 → 4243.66] One thing I do want to say while we're giving shoutouts is that although Brian and I are the faces of Gopher Con, just like with this show, there are a lot of unsung heroes behind the scenes making things happen too.
[4243.66 → 4245.06] So, yeah.
[4245.26 → 4249.74] I think Brian and I probably need to do a post just kind of shouting out to all the people who make it happen.
[4249.82 → 4251.10] Because it's not just us.
[4251.24 → 4253.76] There are a number of people behind the scenes with that as well.
[4254.46 → 4254.64] Yeah.
[4254.76 → 4266.54] And the biggest one I want to shout out this year, prematurely of our blog post or whatever we do, is Sarah Adams for helping us take on the scholarship applications and awarding process.
[4266.54 → 4274.94] That was a tremendous amount of help that she and her group of people that she kind of brought together gave us.
[4275.14 → 4275.56] That's awesome.
[4275.68 → 4276.64] Really, really appreciate it.
[4276.66 → 4277.28] They're not done yet.
[4277.34 → 4281.36] So, if you haven't gotten a notification that you got a scholarship, don't freak out.
[4281.48 → 4283.30] There's still plenty of time left.
[4283.36 → 4285.52] But they did start announcing yesterday or the day before.
[4285.72 → 4291.02] And it's so much fun watching the excited tweets of people who are going to Gopher Con who didn't think they could.
[4291.02 → 4292.28] All right.
[4292.38 → 4296.62] So, with that and our 12 minutes over, let's close this thing out.
[4296.84 → 4301.16] Thank you to everybody for being on the show and kind of sharing your own personal thoughts.
[4301.42 → 4304.86] And a huge thank you to Adam for actually coming out from behind the curtain.
[4305.08 → 4307.86] We've tried so long to get him to come out and talk on the show.
[4308.46 → 4311.34] Thanks to all the listeners and everybody who submitted questions for today.
[4311.66 → 4314.38] And even if we didn't get to your question, we will hang on to those.
[4314.44 → 4318.34] And maybe we can do an AMA periodically with those.
[4318.34 → 4321.42] Definitely a huge thank you to Total, our sponsor.
[4322.08 → 4325.06] Share the show with friends and coworkers.
[4325.72 → 4327.74] Easy way to subscribe is gotime.fm.
[4328.12 → 4329.86] We're at gotime.fm on Twitter.
[4330.50 → 4339.26] And if you want to be on the show, have suggestions for guests or questions for the hosts, hit us up on GitHub.com slash gotime.fm slash ping.
[4339.78 → 4341.10] With that, goodbye, everybody.
[4341.24 → 4341.82] See you next week.
[4342.42 → 4342.82] Later.
[4343.56 → 4344.20] Thanks, Adam.
[4344.58 → 4345.06] Bye.
[4345.06 → 4345.14] Bye.
[4345.14 → 4345.18] Bye.
[4347.44 → 4348.10] All right.
[4348.16 → 4350.30] That wraps up this episode of Go Time.
[4350.44 → 4353.20] Tune in live on Thursdays at 3 p.m.
[4353.24 → 4356.38] U.S. Eastern at changelaw.com slash live.
[4356.80 → 4360.90] Join the community and Slack with us in real time at the changelaw.com slash community.
[4361.36 → 4362.08] Follow us on Twitter.
[4362.18 → 4363.62] We're at gotimefm.
[4363.94 → 4366.42] Special thanks to Total for sponsoring this show.
[4366.88 → 4368.98] Also, thanks to Vastly, our bandwidth partner.
[4369.42 → 4371.12] Head to fastly.com to learn more.
[4371.38 → 4373.86] This episode was edited by Jonathan Young blood.
[4374.22 → 4377.36] And the theme music for Go Time is produced by Break master Cylinder.
[4377.62 → 4378.92] We'll see you again next week.
[4379.30 → 4380.00] Thanks for listening.
[4380.00 → 4409.98] I'll see you then.
