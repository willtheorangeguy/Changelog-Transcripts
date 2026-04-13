[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.38] And we're hosted on Linde cloud servers.
[12.74 → 14.74] Head to linode.com slash changelog.
[15.58 → 18.86] This episode is brought to you by Linde, our cloud server of choice.
[19.04 → 21.00] It is so easy to get started with Linde.
[21.34 → 23.20] Servers start at just $5 a month.
[23.44 → 26.44] We host Changelog on Linde cloud servers, and we love it.
[26.52 → 28.24] We get great 24-7 support.
[28.24 → 31.22] Zeus-like powers with native SSDs.
[31.38 → 34.42] A superfast 40 gigabits per second network.
[34.70 → 36.60] And incredibly fast CPUs for processing.
[37.06 → 39.16] And we trust Linde because they keep it fast.
[39.32 → 40.26] They keep it simple.
[40.62 → 43.04] Check them out at linode.com slash changelog.
[43.04 → 63.48] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[63.48 → 68.40] This is where conversations around AI, machine learning, and data science happen.
[68.86 → 73.14] Join the community and slack with us around various topics of the show at changelog.com slash community.
[73.36 → 74.30] Follow us on Twitter.
[74.42 → 75.90] We're at Practical AI FM.
[76.16 → 77.22] And now onto the show.
[77.22 → 85.98] Welcome to another episode of Practical AI.
[86.36 → 87.58] I'm Daniel Whiten ack.
[87.68 → 90.72] I'm a data scientist with SIL International.
[91.10 → 98.60] And I'm joined, as always, by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[98.94 → 99.62] How are you doing, Chris?
[99.94 → 100.58] I'm doing fine.
[100.62 → 101.46] How's it going, Daniel?
[101.96 → 102.86] It's going good.
[103.12 → 106.52] Well, today, I think it's going to be a great show.
[106.52 → 114.62] We've got a chance to talk about something that we've mentioned here and there and definitely talked about a little bit, but haven't had a whole show devoted to.
[115.14 → 119.46] And that's some ideas around AI and automation in manufacturing.
[120.02 → 126.22] Specifically, we have Costas Bulbs with us, who is the chief scientist at Bright Machines.
[126.40 → 127.36] Welcome, Costas.
[127.68 → 128.68] Thank you for having me.
[129.02 → 133.66] Maybe before we jump into Bright Machines and manufacturing and all of that stuff,
[133.66 → 143.24] if you could just give us a little bit of your background, and maybe we could learn a little bit about how you got into machine learning and AI and ended up at Bright Machines.
[143.44 → 143.98] Sure, yeah.
[144.14 → 148.16] So I started machine learning when I was doing my PhD here.
[148.16 → 158.20] And I really fell in love with working with data and what this data means for everything, for so many applications of machine learning.
[158.74 → 166.58] One of the things that I have done, and I've enjoyed doing in my career is kind of work in different aspects of machine learning and artificial intelligence.
[166.58 → 179.76] So I'm not kind of the type of person that would stay with the same kind of problem for 20 years working on some specific aspects, for example, of, I don't know, some natural language processing and never seeing anything else.
[180.52 → 185.86] I think that there are many commonalities across broad areas of machine learning models.
[185.86 → 196.34] And there's a tremendous value when someone kind of tries to have the perspective that was gained from one area to apply to another area.
[196.86 → 200.26] So that's what also brought me to Bright Machines.
[200.38 → 203.72] I have worked in, well, I've done academic work.
[203.82 → 215.50] I also worked at Microsoft and at Amazon in different projects in detecting malware and phishing, in computer vision, in natural language processing as well.
[215.50 → 234.26] And the very interesting thing here with Bright Machines is that they're trying to apply AI into a big area, huge area, manufacturing that has not really yet been kind of touched by the revolution that is happening in so many other areas.
[235.04 → 235.16] Yeah.
[235.26 → 243.92] So you would say that like manufacturing in particular maybe has been lagging a bit behind in terms of adoption of AI technologies?
[243.92 → 246.36] Yes, that is definitely the case.
[246.76 → 255.32] And I guess there are a number of reasons why this was happening all these years, like at least like starting 20 or maybe 30 years back.
[255.80 → 260.86] Labour was always cheap, especially in places like China and always available.
[261.06 → 269.78] So if you wanted to manufacture a product, any product, it was definitely an option to say I'll hire a number of workers for a few months.
[269.78 → 273.20] It would be pretty inexpensive to compensate them.
[273.30 → 275.02] And then I'll just move to another product.
[275.84 → 277.36] Be smart about it.
[277.62 → 279.70] I'll just throw more people to the problem.
[280.30 → 283.60] And this is less of an option right now.
[283.76 → 287.82] Even for places like China, labour is becoming more and more expensive.
[288.52 → 294.14] And demand for products is becoming bigger and bigger, especially for electronics products.
[294.14 → 303.14] Because clearly, you know, if we want to keep doing what we're doing and want to enhance what we're doing, we cannot rely on the old ways of doing it.
[303.24 → 307.84] We have to have smarter robotics that do the work for us.
[307.84 → 323.16] So I know just from some of the things that I was exposed to right when I came into industry, it seems like manufacturing has had some like software influence in terms of process control and control systems.
[323.16 → 339.50] But in terms of like the human element and automation, are you talking about the sort of end to end automation we're kind of striving after has been lacking or maybe just the sophistication of the methods that are used in that sort of thing?
[339.54 → 342.04] I would say both, but especially because of the end to end.
[342.04 → 345.78] So, for example, you look at electronics products.
[346.56 → 350.14] There's a line of different machines that do different things.
[350.14 → 360.08] So you have your printed circuit board, and then you start putting smaller components, the capacitors and the resistors and integrated circuits.
[360.36 → 362.32] That part is actually very well automated.
[362.58 → 366.52] There is these surface-mounted components and the machines that do this.
[367.02 → 371.64] And that initial part is, I would say, automated pretty well.
[372.04 → 374.14] But this is not where things stop.
[374.14 → 379.40] So after you have your smaller components, you have some bigger components you have to put in.
[379.52 → 387.60] You have to have like heat sinks or some kind of all those ports, the Ethernet ports and all these like kind of bigger things.
[388.10 → 394.72] Also, you're going to have your board, your electronics board, and then you're going to have to put more boards on top of that.
[394.72 → 402.32] Like, for example, if it's a motherboard, you have the RAM chips and other PCBs that you put on top of that.
[402.58 → 406.54] And you have to put everything or some kind of casing, your TV remote control.
[406.76 → 410.68] There's a PCB that is encased in a plastic case.
[411.26 → 413.96] Anything right now, home alarm systems, anything you can imagine.
[414.56 → 417.90] So the later parts are not really automated.
[417.90 → 427.80] So if you want to, for example, get those RAM chips, those DIM chips, insert them into a motherboard, that part is not very well automated.
[427.96 → 431.24] This is what people are usually doing the job.
[431.86 → 439.32] And this is the part that, you know, it's kind of complex enough yet because there are different objects that you can encounter.
[439.84 → 445.52] And it's not clear right now how you're going to pick this object, how you're going to grip it, how you're going to place it.
[445.92 → 447.52] Humans are very good at that.
[447.52 → 451.94] We don't have to explain really much to a person how to do these tasks.
[452.38 → 455.74] And that's why, you know, this has not been fully automated.
[455.96 → 458.68] And it still, you know, it still relies on people.
[458.88 → 465.72] If you walk into a manufacturing kind of a line, the first thing that you're going to notice is that there are many people there.
[466.04 → 472.40] Although, you know, there's automation, there's still many, many people involved in the process.
[472.40 → 484.48] So what we are trying to do in Bright Machines, we're trying to automate automation, automate the end-to-end process, increase the sophistication of every aspect of what has been done.
[484.48 → 491.38] So, you know, it's clear as you, I'm kind of looking at the Bright Machines website as we're talking about this.
[491.56 → 494.58] And you kind of got to my question almost before I did here.
[494.74 → 497.36] And I'd like to understand what you're trying to accomplish.
[497.56 → 505.20] It's very clear that Bright Machines believes that robotic systems are finally ready for prime-time deployment.
[505.20 → 509.02] And obviously, the market is bearing that out in a giant way.
[509.40 → 516.78] You guys are number 13 on the Forbes list of AI-50, America's most promising artificial intelligence companies.
[517.16 → 525.02] What's just happened that's enabled you guys to suddenly hit the sweet spot in the market that you are fulfilling at this point?
[525.12 → 525.88] What's changed?
[526.34 → 528.56] Well, it's not an abrupt change.
[528.56 → 537.04] It's a realization in the manufacturing world that the current state of manufacturing or automation is not enough.
[537.40 → 544.56] So if you're trying, for example, to automate the later parts of the manufacturing process,
[544.94 → 552.56] and you try to use whatever tools and digital libraries or other means that you have available in order to automate that,
[552.56 → 558.02] you may be able to have a solution, but it will take you a very long time to build that solution.
[558.56 → 560.68] It will take you months to build a solution.
[561.10 → 564.14] And also, that solution will not be robust.
[564.36 → 567.48] So if things change, your solution may break.
[568.34 → 572.30] So imagine that you go, you know, a manufacturer wants to start a new product,
[572.30 → 577.90] and someone is going to tell them, you know, the first product is going to roll out after eight months.
[578.22 → 586.54] And the solution that we have maybe breaking once, you know, or a few times per day or per week, maybe.
[586.54 → 588.48] Then that's definitely not acceptable.
[588.72 → 591.78] I mean, the manufacturer wants faster deployment times.
[591.92 → 594.68] They want to crank out products as soon as they can.
[595.00 → 599.50] And also, they want to have a solution that works for them.
[599.80 → 603.96] So everything that we do in Bright Machine is targeted to these two things.
[604.16 → 609.54] These are our main tenants, trying to reduce deployment time for automation, for manufacturing,
[609.54 → 612.74] and also try to build more robust solutions.
[613.52 → 618.52] Everybody's going to have confidence that they work, even if conditions change.
[618.84 → 624.00] So as part of that making things robust and reducing the deployment time,
[624.42 → 628.44] I'm reading about some of your efforts in this sort of micro factories.
[628.44 → 635.22] Is the idea there to, like, have this sort of modular tasks that can be spun up very quickly?
[635.22 → 639.48] Or is that really getting more at the sort of end-to-end automation piece?
[639.60 → 640.40] Or maybe it's both?
[641.04 → 649.64] So what we're trying to do, maybe start with some of the difficulties that the current manufacturing process is having.
[650.08 → 654.64] One of the sorts of difficulties is that the manufacturer has to,
[654.64 → 659.00] let's say they're trying to build a new product, so the manufacturer has to repurpose hardware.
[659.32 → 659.50] All right?
[659.54 → 664.76] So they decided to build a new home alarm system, and they were building something different before.
[665.02 → 669.02] So they have to get some hardware from the other lines, add a number of components,
[669.74 → 673.38] maybe add some, I don't know, lights there, or modify the conveyor belt,
[673.84 → 677.72] and modify the tray feeder or a bunch of other things.
[678.06 → 682.16] And then they have to build a vision solution from scratch, basically,
[682.34 → 684.38] and they have to test the whole thing.
[684.64 → 693.00] So there are two sources of kind of errors or of things that can go wrong.
[693.00 → 697.46] The first thing is that hardware is, in a typical manufacturing line,
[697.52 → 699.30] is not standardized right now.
[699.84 → 707.04] And also the second thing is that modern computer vision and AI and machine learning solutions
[707.04 → 714.10] are not being used extensively to understand better what the robot is looking at and what to do.
[714.64 → 718.40] I'm just going to ask there, since you mentioned it, with computer vision and stuff,
[718.50 → 723.62] how does that really integrate into how you guys are approaching this problem?
[723.82 → 726.58] You know, when you're having microfactories, and you're using the robotics,
[727.16 → 730.22] how does AI fit into that picture?
[730.22 → 730.92] Yeah.
[730.92 → 730.98] Yeah.
[731.30 → 738.78] So AI and computer vision is one of the main efforts we're having here in order to,
[739.30 → 742.00] certain deployment times, have more robust solutions.
[742.54 → 751.56] Right now, like a lot of the vision that is happening in a manufacturing line seems to be stuck in the past.
[751.56 → 754.32] There is usually a camera, a manufacturing line.
[754.44 → 757.16] So there's a camera that takes pictures or there's a video.
[758.08 → 763.32] And from these images, people are trying to build some, you know, vision solutions
[763.32 → 770.42] on to how to kind of locate the specific point that they care or, you know, how to complete that task.
[770.42 → 774.20] But the things that they're using are very low level.
[774.78 → 779.68] So they're using things like edge detection or blob detection,
[780.26 → 782.44] or they're doing some kind of histogram equalization,
[782.90 → 788.16] or they're doing some kind of image preprocessing, like contrast enhancement.
[788.70 → 790.20] So very low level stuff.
[790.28 → 795.00] So imagine that you have, let's say, insert a DIMM into a DIMM slot.
[795.22 → 796.76] You have a DIMM slot in a motherboard.
[796.76 → 799.64] So you have to find where the DIMM slot is.
[800.20 → 803.66] So what people usually do is that they say, you know,
[803.74 → 805.54] I'll define a region of interest.
[805.54 → 809.08] It's basically a specific area in the image they're looking at.
[810.14 → 813.08] In that region of interest, there's going to be some kind of marker,
[813.24 → 814.66] some kind of distinct pattern.
[815.26 → 819.64] This is like a very rigid pattern, some lines there that are kind of printed there.
[820.02 → 824.18] And from that marker, they're going to define some other region of interest.
[824.18 → 827.72] And in that region of interest, they're trying to find another marker,
[827.90 → 830.56] some kind of very rigid structure that they can count on,
[830.62 → 831.78] some kind of anchor point.
[832.14 → 834.68] And from there, they're going to move some X or Y points.
[834.84 → 838.14] And maybe, you know, they're going to have the centre of the DIMM slot
[838.14 → 839.26] that they really care about.
[839.72 → 842.62] That is like how a blind person would navigate the world.
[842.70 → 845.06] They would just, you know, touch and find an edge.
[845.38 → 847.44] And from an edge, you know, they're going to say,
[847.56 → 849.64] oh, I know I have to go 10 steps that way.
[849.74 → 850.92] I'm going to find another edge.
[850.98 → 853.92] I'm going to find some, you know, some other door maybe to walk in.
[853.92 → 857.30] So there's not a lot of understanding that is happening.
[857.42 → 858.68] The robot is looking at something,
[858.78 → 860.34] but it's not understanding what it's looking at.
[860.40 → 862.64] Everything is edges and lines and blobs.
[863.20 → 865.92] And you don't want, you know, edges and lines.
[866.02 → 869.28] You want edges and lines because you want to synthesize information
[869.28 → 870.88] to something that is higher level.
[871.34 → 873.54] So what you really want to do is see an understanding.
[873.70 → 875.04] You want to know the objects.
[875.62 → 878.84] You want to have a model that says, hey, I know what I'm looking at.
[878.84 → 884.02] I know how to find theme slots and I know how to find hit syncs.
[884.18 → 887.26] And I know I will always find them and detect them and understand them.
[887.44 → 891.94] And I'm not going to rely on those low level primitives to do this kind of things.
[892.10 → 894.18] They're trying to understand what they're looking at.
[894.24 → 896.30] They say this is a traffic light and this is a person.
[896.76 → 899.34] And this is a crosswalk.
[899.68 → 904.24] Car would never navigate themselves by edges and lines because people would die.
[904.24 → 908.46] In our world, we would want to move to this scene understanding,
[908.64 → 915.78] higher level kind of object models that will kind of allow us to very quickly
[915.78 → 918.56] and more robustly build those solutions.
[918.56 → 923.08] Because imagine like in the previous solution that I mentioned before with the markers
[923.08 → 928.34] and the origin of interest and moving X and Y, you know, you find, you know,
[928.42 → 933.94] you take all this time to craft a solution, and then you find a specific point.
[934.52 → 938.20] And then let's say tomorrow there's another customer that says,
[938.34 → 942.00] hey, I hear you guys are having a theme slot project.
[942.14 → 943.26] Can you build one for me?
[943.40 → 946.24] Sure, you know, three months from now we'll get it to you
[946.24 → 947.96] because we have to start from scratch.
[948.46 → 952.92] We have to say, all right, let's take another picture of that motherboard
[952.92 → 956.60] of that new customer and let's find again where that specific,
[956.88 → 960.36] where new markers are, new ROIs, everything from scratch.
[960.36 → 962.46] It's like a groundhog day.
[962.46 → 967.46] You know, you know that you did this before, but you have to go through this again and again.
[967.54 → 968.66] And again, there's not a lot of reuse.
[969.30 → 977.86] So fundamentally what we're trying to do is make the robots less blind, less dumb, I guess,
[978.02 → 982.28] and also less numb because robots are numb.
[982.44 → 983.78] They don't feel the world.
[984.02 → 987.02] They don't get any feedback also about what is happening.
[987.02 → 990.24] And both vision can give this feedback.
[990.50 → 992.52] We can also have other ways of getting feedback.
[992.60 → 996.58] We can have sensors, for example, that apply pressure and get some kind of force feedback.
[997.12 → 999.46] So that's the high level.
[999.46 → 1010.16] You like this show, so I bet you'd love listening to Go Time.
[1010.48 → 1011.28] Not working with Go?
[1011.56 → 1012.68] Don't fast-forward quite yet.
[1012.94 → 1015.76] Go Time covers a wide range of topics, including cloud infrastructure,
[1016.22 → 1019.28] distributed systems, microservices, Kubernetes, and Docker.
[1019.64 → 1023.24] Here's a ridiculous clip from a recent episode about the defer keyword.
[1023.24 → 1027.76] I think I really think that Matt missed his calling as a standup comedian.
[1029.18 → 1029.58] Totally.
[1030.08 → 1030.74] Yeah, it's funny.
[1031.12 → 1032.16] I mean, he can still be one.
[1032.22 → 1034.58] He just has to choose his audience very wisely.
[1034.66 → 1035.74] It's got to be a tech audience.
[1036.30 → 1038.86] Well, he has Go Time FM.
[1039.86 → 1043.44] I think the funniest low-key podcast out there.
[1043.66 → 1046.48] Thing is, in tech, no one likes a standup comedian.
[1046.72 → 1047.96] You just want them to get on.
[1048.06 → 1049.02] Tell us what you did yesterday.
[1049.22 → 1049.98] Tell us what you're doing today.
[1049.98 → 1052.12] And if you've got any blockers and get off.
[1053.24 → 1053.92] You know what I mean?
[1054.10 → 1055.98] No one wants the, uh...
[1055.98 → 1056.78] Yeah, there you go.
[1056.82 → 1056.96] See?
[1057.20 → 1057.96] That's why I didn't.
[1058.54 → 1059.66] I'll stick to programming.
[1060.36 → 1062.24] I mean, there's only three people here.
[1062.84 → 1065.60] You might have a whole audience that's live listeners that's laughing right now.
[1065.84 → 1066.96] Oh, yeah, let's assume that.
[1071.76 → 1075.56] I'm pretty sure this could be edited to make me not sound like an idiot.
[1076.44 → 1077.36] You heard, Carmen.
[1077.64 → 1079.28] Go Time is low-key hilarious.
[1079.56 → 1082.06] Check it out at changelog.com slash Go Time,
[1082.06 → 1084.98] or just search for Go Time in Apple Podcasts, Spotify,
[1085.28 → 1086.70] or your favourite podcast directory.
[1086.80 → 1087.32] You'll find it.
[1087.64 → 1089.96] Once again, that's changelog.com slash Go Time.
[1089.96 → 1091.16] Go Time.
[1091.22 → 1091.50] Go Time.
[1091.50 → 1091.86] Go Time.
[1092.00 → 1092.34] Go Time.
[1092.34 → 1092.54] Go Time.
[1092.54 → 1092.64] Go Time.
[1092.64 → 1093.06] Go Time.
[1097.08 → 1097.40] Go Time.
[1097.40 → 1098.32] Go Time.
[1100.00 → 1104.96] So as you were talking about the ways in which you're trying to reimagine these sort
[1104.96 → 1111.36] of vision solutions for manufacturing, I was thinking of some of the more recent research,
[1111.70 → 1117.92] particularly the methods that OpenAI is developing around their robot hands and stuff.
[1117.92 → 1123.40] And we were talking about that in a previous episode where they were using sort of randomization
[1123.40 → 1128.70] methods to make the solution a little bit more robust against perturbations.
[1128.84 → 1134.32] Are those the sorts of solutions that you're talking about here where you might encounter
[1134.32 → 1139.30] a slightly different motherboard or a slightly different component, and you want to be able
[1139.30 → 1145.60] to generalize quickly to that other component that's almost the same but a little bit different?
[1145.96 → 1146.28] Yes.
[1146.52 → 1146.66] Yeah.
[1146.76 → 1152.36] So we definitely want to have models that can kind of take care of all these variations
[1152.36 → 1153.14] that are happening.
[1153.70 → 1155.64] So let's say that you have even the same line.
[1156.18 → 1158.96] You know, things do change now in a manufacturing line.
[1158.96 → 1162.36] The environment lights can change.
[1162.96 → 1170.46] The cameras may be not calibrated as well over time because, you know, things move around
[1170.46 → 1174.32] and the camera may move a bit around or maybe of temperature differences.
[1175.00 → 1178.60] Let's say the boards, the PCB that come into the line, they're not going to be perfectly
[1178.60 → 1181.32] aligned to some kind of reference point.
[1181.32 → 1188.76] So if things are not aligned, we have to kind of, our solutions need to take this into account
[1188.76 → 1190.90] and continue working.
[1191.28 → 1198.86] So all this variation can really be addressed very well in, you know, through computer vision
[1198.86 → 1204.70] in a software first world because traditionally what people have been doing in manufacturing
[1204.70 → 1211.20] in order to eliminate this variation and have, you know, automation work for them is that
[1211.20 → 1216.72] they were putting hardware first because most of the people are mechanical engineers
[1216.72 → 1217.90] and that's what they were trained to do.
[1218.00 → 1221.36] You know, they could not see an object very well, for example, for the camera.
[1221.66 → 1226.08] So they would add a light source about, you know, the alignment problem.
[1226.58 → 1233.88] If something is not aligned, then, you know, they're going to put something into some kind
[1233.88 → 1237.62] of a 3D print cradle, and it just brings to align everything.
[1237.82 → 1240.88] So these are mechanical solutions that can address some of these variations.
[1241.20 → 1245.62] But the thing with mechanical solutions is that they don't scale.
[1246.00 → 1251.16] Like you have to do the same thing again and again for different projects and still, you
[1251.16 → 1252.84] know, you haven't really solved the problem.
[1253.10 → 1257.46] You're kind of mitigating it, but not totally solving it.
[1258.04 → 1264.04] And we think we can solve it in a much more scalable way, in a much better way in a software
[1264.04 → 1264.86] first world.
[1264.86 → 1269.14] So I'm kind of curious as that was a great explanation.
[1269.48 → 1274.10] How do microfactories really fit into this as you start applying this?
[1274.58 → 1281.06] And how do your AI efforts in terms of vision and maybe other problems that are related to
[1281.06 → 1286.52] this and in terms of getting your robotics to where they need to be for your customers?
[1286.96 → 1288.22] How does that all fit in?
[1288.22 → 1291.56] How do you transition into microfactories given all this?
[1292.06 → 1298.12] Yeah, microfactories, the thing that they really give us is that they standardize a number
[1298.12 → 1302.94] of hardware components so that we don't have to grapple with things like, how do we control
[1302.94 → 1303.44] the camera?
[1303.92 → 1307.18] Or, you know, what happens if there is another conveyor belt?
[1307.32 → 1309.54] How do we, you know, how would you understand that?
[1309.54 → 1320.44] So it definitely helps us to build these solutions in a much more scalable way by having the standardized
[1320.44 → 1320.98] hardware.
[1322.24 → 1325.98] That's the main thing that they're buying to us.
[1326.94 → 1332.84] And the fact that we have kind of a full cell that we know, you know, we have the full 3D
[1332.84 → 1337.48] model of the cell, and we know where kind of where things, you know, how things can change
[1337.48 → 1342.92] there that also helps us model what to expect from a computer vision perspective.
[1343.54 → 1348.36] And maybe just before we get too far into that, could you just describe what bright
[1348.36 → 1353.20] machines like what the microfactories are them themselves?
[1353.64 → 1354.26] Yeah, exactly.
[1354.40 → 1358.66] So the bright machines, microfactories is basically like a full cell.
[1359.16 → 1362.04] It has an industrial arm.
[1362.18 → 1365.68] These are the arms that do pick and place operations.
[1365.68 → 1370.06] They're going to pick a specific component and basically a wide variety of different components
[1370.06 → 1371.66] and then place it on different tasks.
[1372.48 → 1377.54] And they have is a conveyor belt there that kind of moves the different products.
[1377.70 → 1382.06] These are the things that the different components will be placed on top of.
[1383.32 → 1386.06] There's also the different light sources into that cell.
[1386.42 → 1386.98] There are cameras.
[1386.98 → 1390.86] There is a place where the tray feeder will go.
[1390.98 → 1395.76] The tray feeder is where the components that we're going to be picking and placing are.
[1396.50 → 1402.34] And that these microfactories are intended to be kind of the last step of the line of an electronics product.
[1402.54 → 1410.06] This is where, for example, a person can pick a heat sink with their own hands and put it into a board.
[1410.06 → 1412.56] This is where our microfactories can help.
[1413.14 → 1416.00] They can also perform some of those tasks.
[1416.44 → 1420.20] So you mentioned standardization is one of the goals of the microfactories.
[1420.42 → 1425.54] And you also mentioned kind of trying to make AI models a little bit more robust.
[1425.64 → 1428.78] I was wondering if you could go into a little bit of the process.
[1429.02 → 1433.08] We like to be fairly practical on this podcast, given that it's practical AI.
[1433.08 → 1446.46] So I was wondering if you could kind of share a little bit about the workflow you went through in terms of data gathering and what you've done to create this sort of new types of AI models.
[1446.82 → 1454.08] Did you start out with your microfactories in that sort of controlled environment and create some vision models there and then try to extend them to other places?
[1454.08 → 1455.94] Or was it kind of the other way?
[1455.94 → 1465.68] Did you start with kind of existing customer video and imagery and start there and then figure out what you needed to standardize and then standardize it down?
[1465.76 → 1466.96] How did that process work?
[1467.18 → 1471.64] And where did the sort of data gathering, annotation and model building fit in?
[1471.96 → 1472.18] Yeah.
[1472.30 → 1483.28] So, for example, I mean, we want to build high level computer vision models in order to build high level computer vision models, as you mentioned, with data.
[1483.28 → 1504.90] And this is where kind of the first challenge appears, because while the deep learning revolution that started a few years back, the kind of the main region or a catalyst for this revolution was ImageNet and a number of other data sets that were available that people could just rely on and start developing their algorithms.
[1504.90 → 1510.72] ImageNet, for those folks that are not aware, is a data set of about 14 million images.
[1510.72 → 1517.06] And it has close to, I think, like 22,000 different categories or classes.
[1517.94 → 1525.22] And it's geared towards kind of classification and also object detection tasks and other tasks as well.
[1525.84 → 1533.86] And ImageNet was possible because of Google Image Search and Bing Image Search and Flickr.
[1533.86 → 1539.42] So, people built crawlers that were able to find all those images and download them.
[1539.48 → 1541.46] And then they had a mechanical track annotating them.
[1541.70 → 1547.62] So, the big kind of challenge in the manufacturing world that there's no Google Image Search for manufacturing data.
[1548.00 → 1554.90] We cannot, like, easily build this because many of those things are kind of – many of the components are customs.
[1554.90 → 1559.54] There are all sorts of different – there are literally hundreds of different, for example, heat sync types.
[1559.96 → 1566.08] And there's, like, just so much variation that people would not put into a, you know, in their Flickr account and share it with the world.
[1566.56 → 1571.82] So, that's one of the bigger kind of initial challenges that we cannot use exactly the same path.
[1572.22 → 1578.56] Now, what we have – one of the biggest assets we have in Bright Machine is the digital twin.
[1578.56 → 1585.74] The digital twin is basically kind of a virtual version of the physical robot.
[1586.06 → 1597.32] So, it's kind of a digital replica where we can – we tell the digital twin to move to a particular position in this virtual world or do a task.
[1597.90 → 1599.82] And, you know, it's running some code there.
[1599.94 → 1606.58] And we have confidence that if we take the same code, and we deploy it to a physical robot, it will do the same thing.
[1606.58 → 1613.32] So, we make the digital twin to be as close as possible to a digital replica of the physical robot.
[1613.48 → 1618.74] So, now that we have a digital twin, we can be doing things there.
[1618.88 → 1634.48] We can be using the digital twin to explore the world and to build what-if scenarios and can kind of simulate some of the variation that we cannot kind of naturally take in other sources like download from the web.
[1634.48 → 1648.30] So, in the last years, the last few years, people have been using GANs, the generative adversarial networks to simulate aspects of variability in their data that are missing.
[1648.76 → 1653.46] For example, let's say that you're building a fraud detection system.
[1653.46 → 1660.26] And it's hard to get data from a fraud detection system because fraud is, you know, kind of rare.
[1660.68 → 1663.18] And especially if you're looking for sub-cases of this fraud.
[1663.26 → 1667.38] Let's say you're looking for cases for fraud from a particular country.
[1667.56 → 1669.78] It's hard to get this data, hard to acquire.
[1669.94 → 1671.00] It will take a long time.
[1671.36 → 1676.46] It will also take the right people to annotate them, properly annotate them, and say, yes, this is really fraudulent.
[1676.46 → 1683.46] So, one thing that people are doing is that they are kind of assimilating this.
[1683.60 → 1690.52] And they're going to say, well, how can I, you know, simulate what this fraud data for that country would look like?
[1690.84 → 1698.12] And then use this to basically understand better, you know, the variability that I'm missing.
[1698.12 → 1708.54] So, we can do this even better with a digital twin because, you know, digital twin, we have a kind of full knowledge of this digital world.
[1708.70 → 1710.72] We can simulate it much better.
[1710.88 → 1714.88] My company, Lockheed Martin, we're also using digital twins for all sorts of stuff.
[1715.00 → 1719.24] And I'm fascinated that you guys are doing this in the space that you're working in.
[1719.24 → 1735.56] I think it's not something that we've really talked about on the podcast before, but digital twins give you an ability when you're trying to build complex solutions to complex problems in the real world to be able to figure things out ahead of time.
[1735.96 → 1745.06] And with the ability to generate data with GANs and stuff, as you described, to be able to fill in data that you may not even have so that you can address a complex problem.
[1745.16 → 1747.22] So, I love hearing that you're addressing that.
[1747.22 → 1754.68] I would like to ask you, in terms of robotics, we've really only talked about computer vision focused models so far.
[1754.84 → 1760.36] But I'm curious whether you guys are also using things like movement strategy models and such as that.
[1760.42 → 1763.74] There are so many different types of models that go into robotics.
[1764.08 → 1774.96] And I'd love it if you could kind of take us through kind of the variety of models that you guys use in your robotic solutions for microfactories and beyond.
[1774.96 → 1780.06] Yeah, so we're developing these high-level computer vision models.
[1780.42 → 1785.42] Besides those computer vision models, we're also experimenting with reinforcement learning approaches.
[1786.12 → 1790.26] Reinforcement learning is kind of a mate for the robotics world.
[1790.40 → 1791.64] It's just perfect.
[1791.80 → 1794.18] This is exactly what it is about.
[1794.18 → 1810.60] I mean, when we are having all these industrial controllers that are trying to complete a complex task, we try to specify every instruction and try to say, go there, then do that.
[1810.70 → 1812.66] And if that happens, do something else.
[1812.76 → 1814.56] And if the other thing happens, do something different.
[1814.98 → 1816.42] It will just not work.
[1816.42 → 1824.90] So in this, for example, this is kind of a first version of this DIMM slot or DIMM insertion task.
[1825.20 → 1828.74] So the task is to get a DIMM card and put it into a DIMM slot.
[1829.50 → 1831.80] This is actually a complex task.
[1831.98 → 1833.88] DIMM slots have those latches.
[1834.30 → 1837.56] You have to kind of unlatch them first if they are latched.
[1837.72 → 1839.54] You have to apply the right pressure.
[1839.78 → 1842.64] It takes quite a lot of pressure to put them right.
[1842.64 → 1845.88] If you're not in the right place, things will break.
[1845.88 → 1858.24] So kind of the first version or the first reaction to solving this problem would be to have engineers, have people try to specify precise and full instructions for what to do.
[1858.36 → 1860.02] You know, go there, do this.
[1860.10 → 1861.64] If that happens, do something else.
[1862.24 → 1866.50] But you will spend a lot of time trying to specify everything that can go wrong.
[1866.98 → 1869.04] And you will still not have a full solution.
[1869.04 → 1880.50] So what we're trying to do is a complex task, like inserting a DIMM into a DIMM slot is something that is very well suited for the robotics world.
[1880.82 → 1884.30] And you can specify the basic things.
[1884.36 → 1888.80] You can have a reward function, and you're going to have some negative rewards, I guess.
[1889.12 → 1896.46] So for example, you can have an end of arm gripper that applies some force and then gets some force feedback.
[1896.46 → 1900.36] So that's a critical component, the feedback part.
[1900.90 → 1905.08] And then, you know, it can know when it has correctly placed a DIMM.
[1905.22 → 1907.70] So it will get a bad part in that case.
[1907.76 → 1912.02] It will know when something bad happens, like you apply pressure when you were in the wrong spots.
[1912.10 → 1920.22] You break things, or you do not complete the task in a specified time, or you hit the boundaries of the cell or something like that.
[1920.22 → 1925.38] And then you can watch it, explore the world and try to find it by itself.
[1925.88 → 1929.02] And the catalyst here, again, is a digital twin.
[1929.14 → 1937.60] Because if you try to have a physical robot experimenting and exploring the world, it will take forever.
[1937.84 → 1940.78] Because moving to different things takes time.
[1941.30 → 1944.04] And trying different things takes time.
[1944.04 → 1947.82] And in a digital twin, time is relative.
[1948.42 → 1950.14] Things can move really, really fast.
[1950.48 → 1958.76] And that's why kind of all the reinforcement learning approaches, like the open AI example that you mentioned manipulating the Rubik's Cube,
[1959.36 → 1966.24] even other approaches, the Alfaro, the chess cases, they had kind of a virtual environment.
[1966.24 → 1974.14] They were able to go through countless cases of games and learn this in an expedited frame.
[1974.36 → 1978.84] I mean, for us humans, you know, we are constrained in this physical world.
[1978.98 → 1982.46] So we started as a group trying to learn how to do tasks.
[1982.52 → 1983.42] It will take years.
[1983.76 → 1987.64] So we're trying to expedite this learning in a virtual world.
[1987.64 → 2003.04] This episode is brought to you by Brave.
[2003.40 → 2005.24] We deserve a better internet.
[2005.56 → 2008.90] That's why the team behind Brave reimagined what a browser could be.
[2009.46 → 2011.34] Brave is like Chrome, the good parts.
[2011.64 → 2013.26] Even your extensions will just work.
[2013.50 → 2015.16] It has built-in ad and tracker blocking.
[2015.48 → 2017.24] Easy anonymization with the Tor network.
[2017.24 → 2020.78] Earn tokens while you browse and use them to tip your favourite creators.
[2021.18 → 2022.76] And did I mention it's lightning fast?
[2023.08 → 2025.68] Turns out the web is superfast when you remove all the cruft.
[2026.02 → 2030.72] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[2042.90 → 2046.22] So I'm curious, as you're developing these models,
[2046.22 → 2049.72] I mean, developing them, training them is one thing.
[2049.72 → 2056.74] I was wondering if you could talk a little bit about the challenges of deployment of the models and inferencing.
[2057.20 → 2072.98] Because I know, you know, I'm not sure if specifically in manufacturing, do these models have to run, you know, at the edge, like on some type of hardware that's very close to the line in terms of how fast they need to operate and that sort of thing.
[2072.98 → 2078.08] What are the challenges around that in terms of the deployment and inferencing side?
[2078.08 → 2080.34] Yeah, these are actually great questions.
[2080.74 → 2087.26] So, yes, the one kind of constraint that we have is that this needs to run locally.
[2087.26 → 2100.82] So, because the latency requirements are very strict, the point of the goal of the manufacturer line is to have as many products per hour as possible.
[2101.22 → 2108.14] And having a very short kind of turnaround time when it comes to inferencing is very important.
[2108.14 → 2114.10] So that means that for the majority of the cases, we're going to have things on the edge.
[2114.60 → 2122.64] Now, we can be kind of smart about it, meaning that we can share some resources across different cells, and we're going to try to maximize the use of this hardware.
[2123.26 → 2131.12] But the reality is that for many cases, we do need to have kind of local models running in local hardware.
[2131.12 → 2136.46] And that's something that we are developing, and we are growing right now.
[2136.58 → 2142.14] And how much do these models need to be updated over time?
[2142.50 → 2149.18] Does the manufacturing process sort of drift over time in some ways that cause the model to be updated?
[2149.18 → 2158.68] Or is often it kind of you deploy the model to the edge device for a specific process and it kind of runs for quite a while.
[2158.80 → 2166.98] And then maybe when you want to switch to a different product or a slightly different component, things need to be kind of retrained and that sort of thing.
[2167.06 → 2168.54] What's the cycle around that?
[2168.78 → 2168.90] Yeah.
[2168.98 → 2169.86] How dynamic?
[2170.16 → 2170.34] Yes.
[2170.46 → 2175.80] This is something that we need to do, do some retraining because things do change.
[2175.80 → 2183.46] There are new defects that are coming, there are conditions that are not properly identified and recognized.
[2184.04 → 2186.96] So a key part of this is the retraining part.
[2187.36 → 2193.12] And understanding when you need to retrain is also kind of a very, very important.
[2193.58 → 2199.80] Like you would ideally you want to retrain when things are, or you detect things are different.
[2199.80 → 2206.80] If things haven't really changed, there's no need to retrain and kind of take up valuable kind of hardware resources for that.
[2206.80 → 2221.44] So both of these like detecting when things have changed, detecting drifts and also doing retraining of the different models that we have are important into the process that we have.
[2221.54 → 2230.28] This is kind of unique to the manufacturing world in the sense that both the latency and also the retraining part.
[2230.28 → 2241.58] Another thing is that those models, for example, we're talking about computer vision models is that in the manufacturing world, you really need precision.
[2242.02 → 2243.94] You really need to be highly accurate.
[2243.94 → 2256.70] Like if you look at, let's say, the more standard object detection models that try to localize an object, put a bounding box around an object or an entity that you care.
[2256.84 → 2259.88] Like find the dog in the photo, put a bounding box in that dog.
[2260.48 → 2264.76] So those models, they're not really optimized or built for precision.
[2264.90 → 2266.18] They don't care about precision.
[2267.24 → 2269.14] They care about did I find it or not find it.
[2269.14 → 2272.52] If the bounding box is a little bit off, it counts as a correct thing.
[2272.64 → 2275.56] Well, in our case, it really doesn't count as a correct thing.
[2275.64 → 2277.50] You have to find exactly where things are.
[2278.16 → 2283.54] So that means that there need to be some changes into the models themselves.
[2284.42 → 2290.68] And I mean, they kind of have the standard or the first thing that one would do there is try to have like a high resolution model.
[2290.84 → 2295.68] For example, when it comes to this object detection, they can, some of those models, they start with some kind of grid.
[2295.68 → 2299.24] And in that grid, they calculate, you know, they make different decisions.
[2299.38 → 2303.70] And then they do some kind of further compensation on top of that.
[2304.54 → 2311.50] I mean, we can make the grid more granular, but that would make the model much more expensive.
[2311.90 → 2319.96] So we have to find some ways that will be faster, but also have the precision that is required in this phase.
[2319.96 → 2328.92] So this is another kind of critical difference that the manufacturing world has with the standard, I would say, computer vision and natural image.
[2329.42 → 2329.88] Gotcha.
[2330.14 → 2335.76] I guess one of the things I was wanting to also ask about, kind of in a non-technical aspect,
[2336.06 → 2340.18] with microfactories and this amazing work that you guys are pushing forward,
[2340.18 → 2347.14] I guess, how are you seeing people fitting into this automation process?
[2347.48 → 2350.28] You know, so many industries are now moving into this automation.
[2350.28 → 2357.22] And obviously we have conversations as we should and people concerned about, you know, what is the future of employment look like?
[2357.70 → 2365.96] How do you envision the automation that you are implementing fitting in with the human workers that are also there?
[2365.96 → 2370.32] And to kind of add that in, what cannot be automated?
[2370.64 → 2375.96] Aside from the automation bits, where are humans optimized for the things that you cannot automate?
[2376.78 → 2379.46] Yeah, that's an excellent question, a very big question.
[2380.10 → 2386.08] So what will eventually happen is that there are going to be job shifts.
[2386.08 → 2396.36] So a lot of these manufacturing jobs, by the way, many or actually most of those manufacturing jobs, they're menial, repetitive work.
[2396.98 → 2402.90] People just, you know, they don't really last there because how repetitive and how boring this work is.
[2403.00 → 2404.44] They quit after a few months.
[2404.98 → 2410.52] The main issue that manufacturers have is that they cannot find people because people keep quitting.
[2410.52 → 2415.00] The turnover rates for a typical manufacturer is 300%.
[2415.00 → 2423.94] Every time they have to hire three times as many people as the entire workforce because so many people don't last for the entire year.
[2424.50 → 2427.70] So what's going to happen is that these works will shift.
[2428.70 → 2436.72] I mean, there are not going to be many works that, many jobs that, you know, you have to place a specific screw in a specific position again and again and again.
[2436.72 → 2442.60] And those jobs will shift to higher level tasks, like how you control the robots.
[2442.76 → 2445.18] How do you make sure that the robot works correctly?
[2445.36 → 2448.04] How do you monitor the work of the robot?
[2448.40 → 2449.96] And how do you program the robot?
[2450.70 → 2455.60] And hopefully those jobs are going to be less repetitive and more creative.
[2456.66 → 2460.24] But there's no question there's a transition that needs to be made there.
[2460.54 → 2465.26] And that's going to happen eventually over a longer period of a few years.
[2465.26 → 2478.40] And so when you're talking to people, and I'm sure you do talk to a lot of people, you know, just day to day, whether it's, you know, at the coffee shop or, you know, interacting with family or whatever it is.
[2478.48 → 2480.54] And this subject comes up around automation.
[2480.54 → 2486.80] Is that kind of, in terms of people that sort of, I guess, fear automation a little bit?
[2487.10 → 2504.16] Is that kind of your perspective that you give to them that maybe this transition, there might be this sort of period of hardship, but maybe in the end, the jobs are more satisfying and creativity filled in the end than what it is now?
[2504.32 → 2506.30] Is that kind of the perspective that you try to impart?
[2506.36 → 2509.72] Or what are some good ways to enter into that subject with people?
[2509.72 → 2512.52] Yeah, I mean, look what has happened in the past.
[2512.88 → 2516.46] Similar kind of transitions have been made.
[2516.64 → 2525.36] So when computers first came in the 70s and the 80s, people would say, oh, my God, you know, we're not going to have, you know, it's going to be the death of, you know, some job.
[2525.42 → 2527.22] Human calculators or something like that.
[2527.40 → 2528.10] Human calculators, yes.
[2528.10 → 2535.34] And the reality was different is that, you know, that kind of the net job gain, the net job effect was positive.
[2535.54 → 2538.32] There were actually more jobs that were created.
[2538.32 → 2550.10] And we no longer have to be making calculations by hand or having some of the kind of other bookkeeping jobs that before we were making.
[2550.10 → 2566.04] And some similar things we believe is going to happen here that there's going to be eventually a positive net job effect and that there's going to be a shift to jobs that are kind of less repetitive and more creative.
[2566.04 → 2574.86] Just like as we are having right now, there's a very big demand for software engineers, but there's not a big demand for human calculators.
[2574.86 → 2582.62] Unless you're in the world of Dune where they had these men tats, you know, just to throw a random thing into the conversation, which were the human calculators.
[2582.92 → 2583.54] Sorry about that.
[2583.60 → 2586.22] I had to throw my bizarre tangent into it.
[2586.22 → 2607.12] So, I guess, as we look forward kind of at the future of robotics and artificial intelligence and how they intersect with manufacturing, what are you seeing as kind of the most exciting things right now in the state of robotics and within the, you know, the computer vision and other strategy type models and research that are going on that robotics requires?
[2607.12 → 2617.32] Yeah, I mean, I think there's going to be a huge role for computer vision for kind of like the modern type deep learning computer vision and understanding higher level tasks.
[2617.54 → 2621.10] We're just at the beginning as an industry here.
[2621.74 → 2623.30] So, that's definitely one thing.
[2623.72 → 2626.54] Reinforcement learning will play a bigger role.
[2626.70 → 2629.66] I mean, it's already picking up kind of a research interest.
[2629.78 → 2636.06] Reinforcement learning has traditionally been kind of not on top of mind for many researchers,
[2636.06 → 2642.16] but I think it's going to be, it's picking up steam and more of it will kind of transition to actual applications of that.
[2642.66 → 2650.54] And also, the fact that, you know, in a typical production line, there are, you know, there are products that are being assembled.
[2651.44 → 2662.18] You pick up, let's say, a heat sink, you put it into a, you know, motherboard, and then, you know, the next motherboard comes in, you do this again, the next motherboard comes in, you do this again.
[2662.18 → 2668.40] There is definitely a big component for unsupervised learning to enhance those models.
[2668.62 → 2675.62] And unsupervised learning has had kind of a we'll say a mixed effect right now in computer vision.
[2675.90 → 2679.42] We don't really know if it works or exactly how it works.
[2679.54 → 2686.56] There's been some very recent kind of research work that shows us, you know, just specific settings is beneficial, is useful.
[2686.56 → 2699.92] But the good thing, I guess, in our application is that things don't change tremendously from, you know, one product to the other, from one motherboard to the next motherboard.
[2700.04 → 2705.56] There are definitely changes, but they're not as big of a change as one we would find in kind of some natural environment.
[2706.76 → 2710.62] And that kind of works to our advantage of how we model things.
[2710.62 → 2716.32] So, for example, if there are big changes in a production line, that's probably, that probably means something.
[2716.80 → 2722.52] Well, if there's a big change, for example, in a natural image, that may not mean something that is interesting.
[2723.12 → 2734.12] So, all this information, how we do, how we model it, and we encapsulate it into our models, this is going to be key to make the best out of those models.
[2734.12 → 2740.02] Awesome. Well, that gets me super excited about these sorts of things.
[2740.26 → 2749.60] And I really appreciate you digging into a lot of the details of what Bright Machines is doing, but also manufacturing and AI in general.
[2749.84 → 2755.68] Really appreciate you taking time to be on the podcast and share those things with us.
[2755.68 → 2763.84] We'll definitely link some of the Bright Machines work and also some of the topics that we've talked about in our show notes.
[2763.98 → 2769.98] And also, we have had a few episodes on reinforcement learning and the open AI work and all of that.
[2770.04 → 2772.52] So, we'll make sure and link those in the show notes as well.
[2772.68 → 2776.24] But thank you so much, Costas, for talking with us.
[2776.34 → 2778.80] It's been a real pleasure, and I've definitely learned a lot.
[2779.02 → 2780.22] Thank you so much for having me.
[2782.12 → 2785.32] All right. Thank you for tuning into this episode of Practical AI.
[2785.32 → 2787.04] If you enjoyed this show, do us a favour.
[2787.18 → 2788.54] Go on iTunes, give us a rating.
[2788.82 → 2790.68] Go in your podcast app and favourite it.
[2790.78 → 2793.50] If you are on Twitter or a social network, share a link with a friend.
[2793.56 → 2795.94] Whatever you got to do, share the show with a friend if you enjoyed it.
[2796.24 → 2798.90] And bandwidth for Changelog is provided by Vastly.
[2799.02 → 2800.46] Learn more at Fastly.com.
[2800.64 → 2803.84] And we catch our errors before our users do here at Changelog because of Rollbar.
[2804.08 → 2806.46] Check them out at Rollbar.com slash Changelog.
[2806.80 → 2809.28] And we're hosted on Linde cloud servers.
[2809.62 → 2811.24] Head to Linode.com slash Changelog.
[2811.32 → 2812.68] Check them out. Support this show.
[2812.68 → 2816.30] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2816.72 → 2818.80] The music is by Break master Cylinder.
[2819.24 → 2822.62] And you can find more shows just like this at ChangeLog.com.
[2822.72 → 2824.76] When you go there, pop in your email address.
[2825.04 → 2831.06] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2831.44 → 2832.24] Thanks for tuning in.
[2832.40 → 2833.12] We'll see you next week.
[2833.12 → 2833.14] We'll see you next week.
[2833.14 → 2835.24] We'll see you next week.
[2835.24 → 2837.24] We'll see you next week.
[2837.24 → 2838.18] We'll see you next week.
[2838.18 → 2839.24] We'll see you next week.
[2839.24 → 2840.18] We'll see you next week.
[2840.18 → 2841.18] We'll see you next week.
[2841.18 → 2842.24] We'll see you next week.
