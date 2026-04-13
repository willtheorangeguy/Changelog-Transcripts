[0.00 → 9.08] Right from the beginning, I was like that person who just discovered the existence of extraterrestrials and is out in the street just saying, no, they're real.
[9.18 → 10.08] They're already here.
[10.16 → 10.76] It's real.
[11.26 → 13.42] And people are like, oh, yeah, no.
[13.68 → 16.04] You know, wow, that dead programmer, he really lost it.
[16.32 → 23.66] But really, I'm still so excited about it because it opens up just a huge panorama of new possibilities.
[26.12 → 29.48] Big thanks to our partners, Linde Vastly and Launch Darkly.
[29.48 → 30.52] We love Linde.
[30.58 → 32.34] They keep it fast and simple.
[32.68 → 35.52] Get $100 in credit at Linode.com slash changelog.
[35.84 → 38.04] Our bandwidth is provided by Vastly.
[38.16 → 42.44] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[42.60 → 44.70] Get a demo at LaunchDarkly.com.
[47.28 → 49.96] This episode is brought to you by Source graph.
[50.40 → 54.52] Source graph is universal code search that lets you move fast, even in big code bases.
[54.52 → 59.74] Here's CTO and co-founder of Young explaining the problems that Source graph solves for software teams.
[59.98 → 60.24] Yeah.
[60.32 → 68.78] So at a high level, the problems that Source graph solves, it's this problem of for any given developer, there's kind of two types of code in the world, roughly speaking.
[68.78 → 73.22] There's the code that you wrote and understand, like the back of your hand.
[73.44 → 76.84] And then there's the code that some idiot out there wrote.
[77.14 → 84.22] Or, you know, alternatively, if you don't like the term idiot, it's the code that some inscrutable genius wrote and that you're trying to understand.
[84.22 → 87.90] And oftentimes that inscrutable genius is like you from, you know, a year ago.
[88.66 → 92.28] And you're going back and trying to make heads or tails of what's going on.
[92.42 → 103.32] And really, Source graph is about making that code that some idiot or inscrutable genius wrote feel more like the code that you wrote and understand kind of intuitively.
[103.32 → 117.42] It's all about helping you grok all the code that's out there, all the code that's in your organization, all the code that is relevant to you in open source, all the code that you need to understand in order to do your job, which is to build a feature, write the new code, fix the bug, etc.
[117.96 → 118.40] All right.
[118.46 → 123.02] Learn how Source graph can help your team at info.sourcegraph.com slash changelog.
[123.32 → 126.86] Again, info.sourcegraph.com slash changelog.
[133.32 → 139.32] Let's do it.
[139.88 → 140.94] It's go time.
[141.50 → 143.08] Welcome to go time.
[143.26 → 146.28] Your source for diverse discussions from around the go community.
[146.76 → 150.40] Are you rapping your favourite go podcast with a comfy t-shirt?
[151.22 → 154.46] Buy one today at go time.fm slash merch.
[155.18 → 155.76] All right.
[155.80 → 157.20] We have an awesome episode for you.
[157.52 → 158.34] Let's get into it.
[159.10 → 160.20] Here we go.
[163.32 → 176.28] Hello and welcome to go time.
[176.44 → 182.70] In this episode, we're going to be exploring the tiny world of tiny go, as well as those use for building hardware.
[182.70 → 191.80] We are joined today by three wonderful guest go friends, as well as my beautiful fellow panellists, Natalie, who is an overall wonderful human being.
[191.80 → 200.32] And also, poignant to this episode, her first job was as a hardware student engineer at Intel, where she used Tickle and Perl.
[200.38 → 203.10] So she is more than qualified to talk about this topic.
[203.68 → 204.98] Lovely to have you, Natalie.
[205.58 → 208.14] Thanks, Angelica, for organizing this episode.
[208.34 → 209.00] Super excited.
[209.36 → 210.06] We're very excited.
[210.22 → 212.32] And then on to our three lovely guests.
[212.42 → 220.76] First, we have Vladimir Vivian, who's a software engineer and a technologist who enjoys contributing to open source and working with go, of course.
[220.76 → 224.44] He's the author of a book titled Learning Go Programming.
[224.60 → 229.92] And currently, he works at VMware on cloud native related technologies such as Kubernetes.
[230.62 → 230.88] Hello.
[231.44 → 231.96] Hello.
[232.38 → 232.78] Hello.
[233.04 → 234.28] Lovely to have you.
[234.78 → 235.26] Thank you.
[235.36 → 236.34] Very excited to be here.
[236.68 → 242.14] Secondly, we have Tobias Thiel, also known as the always developing princess.
[242.50 → 244.12] I feel like we need to talk about that a bit more.
[244.12 → 249.82] He's a lead developer for the Fintech, Fino and the Reg Tech Clary Lab.
[250.22 → 258.52] He has 15 years expertise, including intervalic, building digital solutions to automate KYC processes.
[258.88 → 265.80] And he is an extremely enthusiastic open source maintainer, contributor to several different projects,
[265.80 → 273.30] as well as being the author of Tiny Go, creative DIY microcontroller projects with Tiny Go and WebAssembly.
[273.30 → 273.54] Hello.
[273.70 → 274.18] Hello.
[274.34 → 275.48] I'm really happy to be here.
[276.02 → 276.90] Glad to have you.
[277.20 → 279.76] Hear more about your book during this episode, I'm sure.
[280.06 → 286.34] And then finally, last but certainly not least, we have Ron Evans, aka Dead Program,
[286.64 → 291.96] who's an award-winning software developer and expert in robotics, IoT and computer vision,
[292.18 → 299.36] who's very active in the free and the open source community, as well as being a technologist for hire at the Hybrid Group.
[299.36 → 307.32] He's helped many clients such as AT&T, Intel and Northvolt solve some of their most difficult technical and business problems.
[307.44 → 310.48] Very excited to have you and your little friend with us today.
[311.02 → 312.40] Yes, I owe it all to GoFer Mod.
[312.50 → 314.86] GoFer Mod does all the work and I take all the credit now.
[315.06 → 317.30] And that is all of our lovely guests today.
[317.46 → 324.80] So I want to dive right in and talk about how did you get into this wonderful world of Tiny Go and Go using hardware.
[324.80 → 326.48] I think I'll go to you, Tobias, first.
[326.96 → 328.06] Oh, it's an easy one.
[328.26 → 328.90] A short story.
[329.02 → 335.62] A friend of mine called Lenny said one day, well, I think Go is just too big for microcontrollers.
[335.72 → 338.52] You cannot have Go on microcontrollers.
[339.02 → 340.52] So I said challenge accepted.
[341.14 → 345.80] And like a day later, I asked the mighty internet for an answer.
[345.94 → 349.10] Is it possible to have Go on microcontrollers?
[349.10 → 350.52] And the answer was simply yes.
[350.90 → 359.96] I found Tiny Go still in its early stages, but I was able to write a little program and deploy it into a microcontroller and then present it to Lenny.
[360.60 → 362.46] And well, Lenny, here you go.
[363.74 → 364.60] That's my story.
[364.80 → 365.04] Nice.
[365.28 → 366.12] Wait, what did it do?
[366.62 → 368.00] It was a really, really simple.
[368.10 → 371.62] It was just a blinking LED, but I just had to prove my point that it works.
[372.66 → 374.24] Was it blinking the message?
[374.32 → 374.92] It works.
[375.28 → 375.40] See?
[376.94 → 377.96] In Morse code.
[377.96 → 379.26] That's too bad in Morse code.
[379.36 → 379.68] I had to.
[380.14 → 383.08] It was really just a really, really, really simple, blink app.
[383.38 → 383.72] Cool.
[384.04 → 385.14] I mean, that's still awesome.
[385.82 → 388.82] And then, Ron, how did you get into this back in the day?
[389.16 → 393.86] I likewise wanted to run Go on microcontrollers for quite a long time.
[394.14 → 402.22] And I even went on Go time in the early days and was just begging the Internets, somebody needs to do this and I will help you.
[402.68 → 405.44] A few people made some attempts, not too successful.
[405.44 → 414.78] And then I don't remember exactly how I discovered the amazing work of the creator of Tiny Go, Ike van Later.
[415.44 → 422.96] So Ike had started, this I think was his second attempt at creating a Go compiler that was small enough to work on microcontrollers.
[422.96 → 427.58] And I started sending these fan emails like, I really love what you're doing.
[427.64 → 428.46] I really want to help.
[428.84 → 430.22] First, he was a little freaked out.
[430.30 → 432.30] Then he's like, oh, yeah, no, go about school.
[432.48 → 434.42] And I'm like, no, I really want to help, though.
[434.48 → 435.46] This is amazing.
[435.46 → 439.26] So people think I created it, but I'm just the biggest cheerleader.
[439.88 → 449.90] Right from the beginning, I was like that person who just discovered the existence of extraterrestrials and is out in the street just saying, no, they're real.
[450.00 → 450.90] They're already here.
[450.96 → 451.58] It's real.
[452.06 → 454.24] And people are like, oh, yeah, no.
[454.90 → 457.28] You know, wow, that dead programmer, he really lost it.
[457.28 → 464.90] But really, I'm still so excited about it because it opens up just a huge panorama of new possibilities.
[465.44 → 470.50] And then I know, Vladimir, you kind of have worked a little bit in Tiny Go, but predominantly working on hardware.
[470.64 → 472.78] I'd love to hear a little bit about how you got into that world.
[473.14 → 473.28] Yeah.
[473.36 → 481.54] So as a day job, I do what I consider to be, you know, they pay the bills, but, you know, it's something I could do in my sleep.
[481.54 → 486.36] So I started to look into what else I can do with Go.
[486.92 → 488.82] I told a story last time we talked.
[489.52 → 496.60] Of course, it was pandemic driven when we had a hard time getting cameras for a webcam.
[497.38 → 500.82] And I started to search to see if there's any way I could build my own.
[500.96 → 506.62] So I started looking into the Raspberry Pi that had just come out with the I think, the HQ camera.
[507.42 → 510.86] And there was some stuff out there that shows you how to do it.
[510.86 → 512.44] And it's multiple steps.
[512.78 → 519.36] And, of course, you have to build some kind of, you need a C tool chain to build what you need to the binary, et cetera, et cetera.
[519.88 → 524.02] But that got me thinking, hey, can these be done with Go?
[524.14 → 526.68] And it turned out that, yes, you can.
[527.12 → 531.88] And it got me thinking what else programming hardware you can do with Go.
[531.88 → 547.86] Because what I've found out is that Go actually puts you closer to the operating system that if you're just using Go for web or cloud native, you don't realize how close you are to the operating system and what sort of system programming you can do.
[547.86 → 565.48] And doing that work, you know, I started a small project to basically do, if not every, probably it's not going to be every part of the API that allows you to stream video from using what we call the Video for Linux API.
[565.48 → 571.70] But at least a good chunk of it to where you can build something useful using Go.
[571.78 → 579.58] Because, you know, I think, I seriously think when it comes to hardware and low-level programming, Go is grossly underutilized.
[579.78 → 580.40] So we'll see.
[580.98 → 587.36] So when working on that project, was you kind of forcing like Go and Tiny Go onto the project?
[587.36 → 591.00] Or do you feel like it truly was the right fit for that kind of project?
[591.38 → 593.54] So actually, even more backstory.
[595.08 → 601.32] I think last time we did something together, you had asked me to, because I've always had an interest in Tiny Go.
[601.34 → 602.96] And I think Tiny Go is a great project.
[603.06 → 615.50] I've even told Ron on Twitter that I think Tiny Go is amazing because you're taking regular Go code, and you cram it down using LLVM into code that can run in microcontrollers.
[615.92 → 616.76] Great stuff.
[616.76 → 620.18] But I wanted to do something in Tiny Go.
[620.74 → 624.04] But I think it was for the ESP32 microcontroller.
[624.16 → 626.38] And what I wanted to do wasn't there yet.
[626.52 → 627.58] So I was like, okay, fine.
[627.66 → 629.12] I'll pause that.
[629.52 → 632.74] I still had the idea to stream with the camera.
[633.24 → 635.10] So I started to look into that.
[635.46 → 639.18] I don't want to steal anyone's thunder because I'm sure we'll get into it.
[639.22 → 645.08] But Tiny Go works great in areas where there are no operating system, like on a microcontroller.
[645.08 → 652.48] But if you do have an operating system like Linux underneath inside your Raspberry Pi, you can do even more stuff.
[652.48 → 674.66] And what I found out is once you realize how to work with the Go API and talk directly to the operating system underneath, you can do a world of things that you probably didn't realize you can do, like streaming live video content from a hardware that's connected to your Linux box.
[674.66 → 677.26] So that's kind of how I ended up there.
[677.38 → 680.28] But the project is not necessarily Tiny Go specific.
[680.76 → 686.60] But it can be, you know, as long as you have an operating system, like specifically Linux, it'll work.
[686.60 → 691.30] Well, I feel like jumping in just because, Vladimir, what you're doing is really cool.
[692.16 → 704.86] And interestingly, long before Tiny Go existed, before, actually a couple of times ago when I was on Go Time, I had mentioned one of the first applications of Go running on embedded Linux were video systems.
[705.18 → 705.48] Right.
[705.48 → 719.28] When we first came out with Robot a few years back, people started popping out of the woodwork saying, oh, we're running Go on an embedded system for some type of, you know, video surveillance system or video monitoring system.
[719.48 → 721.16] And I was like, okay, great.
[721.26 → 722.08] Open source this.
[722.12 → 723.36] They're like, oh, no, no, we can't do that.
[723.44 → 724.70] This is all probably proprietary.
[725.42 → 727.46] But it's really cool that you've been working on this.
[727.46 → 732.08] I think that's a real killer application for Go is computer video.
[732.54 → 732.94] Absolutely.
[733.10 → 737.42] You know whether it's using, you know, video for Linux, which is a very powerful subsystem.
[738.04 → 753.62] Gov, which is another project that I've been really involved in, which is using Go as a wrapper around OpenCV, is actually a project that's quite popular among industrial and commercial computer vision companies.
[753.62 → 762.66] You know, we have a lot of users in China who are working on commercial systems that are deployed in production today using these things.
[763.38 → 767.94] So, I mean, what your point, I think, is really right on that Tiny Go is cool.
[768.04 → 769.92] It has its place when there's no operating system.
[770.26 → 774.34] But embedded Linux is a great option, and it gives you all these capabilities.
[774.88 → 777.82] So, Go really works there incredibly well.
[778.16 → 778.28] Right.
[778.36 → 778.80] It does.
[779.24 → 780.20] Thank you for adding that.
[780.38 → 781.86] Vladimir, I also have a question for you.
[781.86 → 789.80] So, I remember in your talk for the video for Linux stuff, you made use of Ego.
[790.02 → 794.58] And personally, I've worked with quite some years with Go now, but I never had to use Ego.
[795.02 → 801.38] So, would you say Ego is a must to know when working with Go on hardware besides Tiny Go stuff?
[801.74 → 802.18] No, no, no.
[802.26 → 804.00] So, it's the reverse, right?
[804.24 → 807.42] So, what I'm doing, I'm not using Ego at all.
[807.42 → 814.36] So, I'm making what we call IOC TL call, Biocontrol call directly to the driver.
[815.12 → 827.06] One of the I think, blessings in disguise of Go is that the type system and the memory layout of the types in Go match one-to-one with C for the most part, right?
[827.06 → 835.92] And what you could do is you can create data types and value in Go and say, here, Biocontrol API call.
[836.04 → 838.36] Here's my value that I created in Go.
[838.36 → 843.32] So, as long as you're not using any kind of esoteric type, well, you can't in Go.
[843.46 → 845.24] You have to use the types that you have.
[845.38 → 851.66] But as long as it's the type that is the values that the OS is expecting, then you're good.
[851.66 → 864.80] So, what I ended up doing is basically create, follow what is done in Video for Linux API, line by line, looking at each call, saying, oh, okay, this call expects this value.
[864.96 → 867.88] Okay, I'm going to go and encode that in Go.
[868.10 → 872.46] And as long as the data types line up properly, it should work.
[872.48 → 873.64] And it actually works.
[873.64 → 879.68] So, there's a suite of tools that comes with Video for Linux called Video for Linux Control.
[880.02 → 881.90] It's a line CLI.
[882.34 → 889.98] And what I'm doing is looking at what that CLI does and trying to replicate a good chunk of it to see how far I can go.
[889.98 → 892.06] I mean, it's something I do on weekends.
[892.38 → 894.20] So, it's a slow process.
[894.20 → 904.96] But I've gotten to a point where I can build a binary and go that query the system and give me a list of video drivers and all their capabilities, et cetera, et cetera.
[905.60 → 911.44] And obviously, we did the demo last time we got together where you can actually stream videos as well.
[911.84 → 912.52] That's really cool.
[912.84 → 920.58] So, tell us, Tobias, I'm sure you created a lot of little projects as you were writing your book and in your wonderful career thinking about Tiny Go.
[920.58 → 923.30] So, tell us, what are some interesting projects you've worked on?
[923.42 → 924.40] What are you working on at the moment?
[924.78 → 927.82] I guess I just start right out and steal the show here.
[928.36 → 928.76] I'm ready.
[929.28 → 943.78] Well, I guess the most fun project or maybe also the most interesting one I'm worked at or working on at is a thing I also presented last time on Go Bridge.
[944.62 → 949.00] It's myself trying to build my own smart home systems.
[949.00 → 952.98] So, I don't want to use some, okay, Google stuff.
[953.08 → 957.08] I don't want to use Alexa or Siri or whatever is out there in the world.
[957.26 → 961.62] I want to have my own smart hub or what I call it.
[961.72 → 970.30] So, I have some microcontroller from Arduino, the so-called Arduino NATO 33 IoT, which is capable of Wi-Fi communication.
[970.30 → 983.92] So, I use lots of these to control, for example, an LED strip, or I currently have one near my coffee machine to activate power adapter, which activates the coffee machine.
[984.06 → 988.62] So, I don't have to get up from bed to brew a coffee, which is really important for me.
[988.64 → 990.02] Okay, I need one of those.
[990.02 → 991.42] I need one of those.
[991.94 → 1004.16] So, I'm also building a Wasm application also using Tiny Go where I can observe all my little microcontroller around my home and also control them.
[1004.16 → 1015.80] So, if I want a coffee now, I can just grab my smartphone, open up my Wasm application, which currently runs on a Raspberry Pi as a server on my local network, and just say, okay, activate.
[1015.80 → 1022.10] And I can hear the coffee machine starting to brew a coffee for me, which is really, really nice because I'm lazy.
[1023.28 → 1025.96] That's for sure the lazy person's way to make coffee.
[1026.24 → 1028.24] Okay, first, we're going to implement the server.
[1031.12 → 1040.62] Although, the thing that does tie those two things together, interestingly, is the very first video on the Internet was monitoring a coffee pot, as I recall.
[1040.62 → 1047.68] The coffee pot, I think, at the MIT Media Lab, they could tell whether it was empty or needed to be refilled.
[1048.28 → 1051.36] In fact, I believe there's an RFC.
[1052.24 → 1054.48] There's a protocol for checking the coffee pot.
[1055.16 → 1059.42] You might look into implementing that if you really want to be fully Internet compatible.
[1059.62 → 1061.06] So, you mean an actual RFC?
[1061.70 → 1063.06] All right, I have to look this up now.
[1063.50 → 1065.60] This will be in the show notes, of course.
[1065.60 → 1065.72] Yes.
[1066.08 → 1072.02] I guess doing coffee-driven development is really a good cause for many features in the world out there.
[1072.28 → 1074.68] So, it's RFC 2324.
[1075.00 → 1075.48] Oh, wow.
[1075.62 → 1076.52] If you want to look it up.
[1077.04 → 1080.82] I make up a lot of things, but this one I did not have to make up.
[1082.60 → 1083.86] An actual RFC.
[1084.30 → 1084.60] Nice.
[1084.74 → 1087.74] They say it was an April Fool's prank, but I don't buy it.
[1088.20 → 1088.98] We're talking coffee.
[1089.10 → 1090.92] It's too serious for April Fool's pranks.
[1091.34 → 1094.22] The surprising thing is that there's so much around tea as well, right?
[1094.22 → 1101.56] There's the 412 HTTP status, but then there's also in computer vision a lot is about teapots.
[1102.10 → 1106.46] So, I feel that there's a serious competition between brewing coffee and brewing tea here.
[1106.92 → 1108.28] Well, do we really have to choose?
[1108.82 → 1109.98] Can't we all just get along?
[1110.82 → 1114.14] Would you rather have an instant coffee or a nice cup of tea?
[1114.72 → 1116.96] I'll take anything under the right circumstance.
[1116.96 → 1124.44] Either we're happy and love each other, or we start a typical tap versus spaces war just with coffee versus tea right now.
[1124.80 → 1125.08] Exactly.
[1125.26 → 1127.80] Unpopular opinion, coffee is way better than tea.
[1129.26 → 1129.90] Oh, wait.
[1129.98 → 1130.20] Sorry.
[1130.28 → 1131.10] That was supposed to be later.
[1131.28 → 1131.70] I'm sorry.
[1132.22 → 1133.30] I got excited.
[1135.30 → 1136.54] Maybe it was all the coffee.
[1136.80 → 1138.22] Striking the first one from the list.
[1138.22 → 1138.62] Yeah.
[1138.92 → 1140.10] We're just right into it.
[1140.32 → 1142.54] Tobias, what microcontroller do you say you're using?
[1142.90 → 1145.60] The Arduino NATO 33 IoT.
[1145.82 → 1148.20] Such a really long name for such a small controller.
[1148.70 → 1152.04] There are two Arduino NATO 33 microcontrollers.
[1152.14 → 1156.34] One with Bluetooth and one with the awesome Niner Wi-Fi chip.
[1156.84 → 1163.78] So, the one I guess only does is capable of Bluetooth stuff, and the other one is capable of Wi-Fi stuff.
[1163.78 → 1170.42] And, well, this Wi-Fi stuff really helps me as I use it to send MQTT messages over the network and so on.
[1170.76 → 1175.98] And also, this board is really, really, really well-supported in Tiny Go right now.
[1176.18 → 1176.36] Yeah.
[1176.48 → 1184.66] I think it was three years ago, Gopher Con, we had a fantastic Community Hardware Hack Day.
[1184.66 → 1193.90] Well, actually, we ran the Community Hardware Hack Day every physical Gopher Con, starting at the first one when it wasn't even an official thing.
[1193.96 → 1195.14] It was just a community day.
[1195.32 → 1195.64] Yeah.
[1195.84 → 1206.88] And I brought a bunch of flight cases full of equipment because I had to leave directly from Denver to fly to Berlin to do a conference there.
[1207.14 → 1208.46] Then also to Scotland.
[1208.60 → 1209.90] There was like this whole European tour.
[1210.44 → 1212.52] I just had a bunch of flight cases full of equipment.
[1212.52 → 1220.34] So, I just popped the cases open, took a bunch of stuff out on the honour system, like a library, you know, just play with it, bring it back.
[1220.64 → 1225.00] That was the first unofficial Community Hardware Hack Day.
[1225.50 → 1230.04] And then that just became, on the official part, an actual official event.
[1230.16 → 1235.76] And the last one, it was so big that we actually needed an overflow room.
[1236.18 → 1237.26] It was really cute.
[1237.36 → 1238.52] The organizers are running around.
[1238.62 → 1239.40] There's fire marshals.
[1239.48 → 1240.30] They're going to kick us out.
[1240.30 → 1242.86] Like, you got too many people.
[1243.08 → 1246.00] And we're like, oh, I guess we're sorry, you know.
[1246.00 → 1253.78] But one of the reasons it was so successful was Arduino, fantastic company in so many different regards.
[1254.04 → 1258.70] The pioneers of open source hardware in terms of popularity.
[1258.70 → 1275.84] There may have been open source hardware before that, but really Massimo, ANSI, and the whole crew over there, they really took and made it possible for not just programmers, but artists and creative people to create interactive installations.
[1275.84 → 1279.46] Really, that was a big part of their rationale and motivation.
[1279.46 → 1282.70] It wasn't, hey, let's do cool hardware hacking to be cool.
[1283.10 → 1283.76] But there was more.
[1284.38 → 1285.78] So there's another unpopular opinion.
[1286.40 → 1290.36] What we do with technology is much more important than the technology itself.
[1290.62 → 1293.62] I feel like you need to chill your beads on these unpopular opinions.
[1293.62 → 1297.02] This is going to be a whole episode on unpopular.
[1297.38 → 1298.56] He did warn us.
[1298.98 → 1300.30] He did warn us.
[1301.18 → 1304.96] They actually use Go extensively over at Arduino.
[1305.30 → 1305.52] Really?
[1305.52 → 1315.88] Not on the Arduino hardware itself, other than Tiny Go, but all of their command line tools and their tooling that they've rewritten in the last couple of years, it's all written in Go.
[1315.88 → 1322.78] So the Arduino IoT cloud is all written in Go and uses a lot of open source.
[1323.32 → 1330.30] So they're really, really active in the Go world without necessarily getting a lot of attention for that.
[1330.44 → 1330.76] Right.
[1330.76 → 1336.48] But they were so kind as to sponsor the Community Hardware Hack Day.
[1337.06 → 1344.46] So we had like, I forget, 300 Arduino kits using that exact board, Tobias, that you have.
[1344.46 → 1350.94] So one of the reasons why there's such great support is, well, first, we had to do it or else we were really uncool.
[1351.26 → 1355.82] But also we had all these people, like hundreds of people all at once using these.
[1355.92 → 1359.20] And so we got a lot of bug reports and pull requests.
[1359.36 → 1360.70] It was just a frenzy.
[1361.04 → 1362.94] It was so exciting and satisfying.
[1362.94 → 1372.14] And a lot of people who I really like and respect who work at Google came over because, you know, their room was empty, like sad and lonely.
[1372.24 → 1378.14] And our room was fat, was packed with people having fun and doing all this cool stuff with Go.
[1378.42 → 1381.82] Thank you very much to the Go team.
[1382.00 → 1383.26] You know, we couldn't do it without them.
[1383.26 → 1392.12] But that's one reason why it's a really well-supported board is the community that is around Arduino just in general is really strong.
[1392.36 → 1398.10] And the Tiny Go community has been really, really supportive, contributing things back.
[1398.20 → 1405.30] And so combining those together, it really spread out a lot, especially the Wi-Fi capabilities.
[1405.84 → 1407.44] That's a really important thing.
[1407.44 → 1411.80] I mean, it's Internet of Things without Internet or just things.
[1412.46 → 1414.16] I mean, which are, you know, things are cool.
[1414.34 → 1415.10] I like things.
[1415.36 → 1417.66] But you need wireless things.
[1418.38 → 1420.92] So, yeah, the Wi-Fi is really important.
[1421.26 → 1428.24] Even though the boards are named the same, the two boards that Tobias was mentioning are actually based on completely different processors.
[1428.24 → 1443.76] The NATO 33 IoT board is based on the microchip SAM D21, which is a very inexpensive but powerful chip that's used in a lot of boards.
[1443.76 → 1452.70] A lot of the boards from Ada fruit, a lot of the boards from Spark Fun, several different boards from Arduino, a lot of other manufacturers as well.
[1452.94 → 1454.90] So, very cool little chip.
[1454.90 → 1466.72] But then the other chip that they have in their other, the NATO IoT BLE, that's actually a Nordic semiconductor chip, the NRF52840.
[1467.26 → 1469.58] So, that's a really common Bluetooth chip.
[1470.14 → 1479.76] A lot of Bluetooth dongles that you might buy for a USB port for a long time have been based on Nordic semiconductor chips or chips that license their stack.
[1479.76 → 1487.30] So, unfortunately, they're two different stacks of hardware that are not really compatible with each other.
[1487.50 → 1490.36] So, if you have one chip, you can use Bluetooth.
[1490.78 → 1494.58] If you have the other chip, it actually does not have Wi-Fi built in.
[1494.94 → 1503.26] It's actually using what I think Tobias had mentioned, another chip, kind of coprocessor for Wi-Fi, which is actually an ESP32,
[1503.26 → 1508.84] which the other I think it mentioned is wanting to have the support for.
[1509.26 → 1514.40] So, that's a very common coprocessor for Wi-Fi that's bundled on a lot of the boards,
[1514.40 → 1518.14] which sort of makes sense as a pattern for hardware that you see.
[1518.48 → 1522.84] Similar to your notebook computer has many different processors in it.
[1523.10 → 1528.84] It's got a small microcontroller that does nothing more than deal with the keyboard, for example, and so on.
[1528.84 → 1533.78] And so, combining these different chips together and creating a system out of them,
[1534.22 → 1539.98] that's really what the hardware is about, is about combining these interfaces.
[1540.22 → 1542.88] And there are some standards that really exist for doing that.
[1543.58 → 1550.30] And so, a kind of our overall story arc of Tiny Go is the more of these standardized interfaces that we support,
[1550.30 → 1558.02] the more that we make it possible to do really anything that you could do with any C program,
[1558.58 → 1560.20] being able to do that with a Go program.
[1560.62 → 1560.72] Right.
[1560.92 → 1564.40] Except, of course, it's memory safe, and you have all the cool tooling.
[1564.94 → 1567.16] You've got the concurrency.
[1567.64 → 1568.90] There are a lot of great things.
[1568.90 → 1581.24] This episode is brought to you by Honeycomb.
[1581.68 → 1584.92] Honeycomb is built on the belief that there's a more efficient way
[1584.92 → 1588.36] to understand exactly what is happening in production right now.
[1588.68 → 1592.46] When production is running slow, it's hard to know exactly where problems originate.
[1592.72 → 1596.78] Is it your application code, your users, or the underlying systems?
[1596.78 → 1601.50] Teams who don't use Honeycomb scroll through endless dashboards guessing at what they mean.
[1601.80 → 1604.12] They deal with alert floods, guessing which ones matter,
[1604.50 → 1608.24] and go from tool to tool guessing at how the puzzle pieces all fit together.
[1608.50 → 1612.66] It's this context switching and tool sprawl that are slowly killing your teams and your business.
[1613.06 → 1618.94] With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving your business, production.
[1619.36 → 1622.74] Honeycomb quickly shows you the correct source of issues, discover hidden problems,
[1622.74 → 1626.70] even in the most complex stacks, understand why your app feels slow,
[1626.78 → 1627.78] to only some users.
[1628.20 → 1630.64] With Honeycomb, you guess less and no more.
[1631.08 → 1635.56] Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[1635.82 → 1638.52] Again, honeycomb.io slash changelog.
[1638.90 → 1640.84] And by our friends at Fire hydrant.
[1641.10 → 1644.00] Fire hydrant is the reliability platform for teams of all sizes.
[1644.48 → 1649.00] With Fire hydrant, teams achieve reliability at scale by enabling speed and consistency
[1649.00 → 1651.64] from a service deployment to an unexpected outage.
[1651.64 → 1656.44] When your team learns from an incident, you can codify those learnings into repeatable, automated run books.
[1656.64 → 1660.14] These run books can create a Slack incident channel, notify particular team members,
[1660.42 → 1664.42] create tickets, schedule a Zoom meeting, execute a script, or send a webhook.
[1664.68 → 1668.26] For example, your app goes down, an alert gets sent to a specific Slack channel,
[1668.38 → 1670.24] which can then be turned into an incident.
[1670.52 → 1673.30] That will trigger a workflow you define in a run book.
[1673.30 → 1679.18] A pin message inside Slack will show off all the details, the Deer ticket, the clubhouse ticket,
[1679.50 → 1684.04] the Zoom meeting, and all of this is contained in your dedicated incident channel
[1684.04 → 1685.80] everyone on the team pays attention to.
[1686.08 → 1690.24] Spend less time thinking about what to do next and get to work actually resolving the issue faster.
[1690.54 → 1693.94] What would normally be multiple manual tasks across the entire spectrum of responding to an incident
[1693.94 → 1696.64] can be automated in every way with Fire hydrants.
[1696.92 → 1698.68] Give them a try for free for 14 days.
[1698.90 → 1700.32] Get access to every feature.
[1700.32 → 1701.58] No credit card required.
[1701.82 → 1703.78] Get started at firehydrant.io.
[1704.12 → 1706.20] Again, firehydrant.io.
[1716.96 → 1718.20] So I have a question.
[1718.30 → 1721.50] You've been mentioning very specific, detailed chips,
[1721.82 → 1726.92] and somebody who once worked in hardware, I barely remember any of that,
[1726.96 → 1728.62] and I definitely don't know those.
[1728.62 → 1733.36] But if I want to try now Go for something with hardware,
[1733.74 → 1736.56] what are some kind of known limitations I can expect?
[1737.10 → 1739.62] What should be easy for me to implement quickly,
[1739.62 → 1743.08] and what should I realistically say not yet with Go?
[1743.54 → 1746.04] Well, first, go get Tobias' book.
[1746.62 → 1748.12] It's got a lot.
[1748.34 → 1749.46] When you say go get.
[1749.96 → 1753.44] Yo, I hope you have the domain Tobias' .book.
[1754.28 → 1755.18] I'm buying it.
[1755.26 → 1755.76] I'm buying it.
[1755.76 → 1756.20] No worries.
[1757.16 → 1763.28] That's a – did a really great job of going through a whole series of small projects,
[1763.82 → 1766.96] a bunch of which are projects that if you are, you know,
[1766.98 → 1773.14] an undergraduate student in computer science in a UK-based university like one of my sons,
[1773.14 → 1777.90] a couple of those projects were literally projects they had done in the previous semester.
[1777.90 → 1782.58] I'm like, oh, well, sorry, I didn't know this book was coming out, plus it's Go,
[1782.64 → 1787.10] and you had to do this in, you know, AVR assembly language just because, you know,
[1787.18 → 1788.88] I mean, you're a computer science student, kid.
[1789.44 → 1790.00] Toughen up.
[1790.66 → 1793.52] But I would say that thanks to our community,
[1794.38 → 1801.34] most of the boards that you can get from Ada fruit have software that you can run Tiny Go on it quite easily
[1801.34 → 1809.24] that would include all of their cool boards like the Pi badge, a.k.a. the Go badge,
[1809.84 → 1814.12] which if you've ever seen me going around with a Go-powered badge, that's it.
[1814.50 → 1815.34] The Pi Gamer.
[1815.34 → 1820.26] Basically, they really are the sponsors of Circuit Python,
[1820.74 → 1826.20] which is a version of Python that's designed to run on microcontrollers.
[1826.62 → 1830.20] And they've done such a great job of supporting that language
[1830.20 → 1834.00] and actually paying full-time people to work on it as well,
[1834.30 → 1841.00] that all the boards that they create have really well-documented APIs and interfaces.
[1841.00 → 1848.24] And so we've made a lot of efforts and a lot of contributors have done most of the work
[1848.24 → 1853.04] to make it possible that basically anything you order from Ada fruit that they've made in the last,
[1853.12 → 1856.14] you know, two or three years is almost guaranteed to work.
[1856.70 → 1860.20] Same true with Arduino to a lesser extent,
[1860.44 → 1866.78] only because the chips that all the original Arduino's that were based on,
[1866.78 → 1871.54] the Arduino UNO, for example, that uses an 8-bit microcontroller
[1871.54 → 1879.30] that has, in many cases, somewhere between 16 and 64K of memory.
[1879.78 → 1881.70] You can run Tiny Go on that.
[1881.98 → 1882.34] Absolutely.
[1882.58 → 1887.82] In fact, that's even larger than the smallest known target for Tiny Go,
[1887.82 → 1895.88] which is an ATtiny85 chip, which is used in a little board called the IGESPAR.
[1896.50 → 1900.90] First, it's got Tiny in the name, so that means automatically we have to make it work.
[1901.76 → 1902.78] I don't make the rules.
[1902.78 → 1910.18] But it has, it's an 8-bit processor with only 8K of RAM.
[1910.72 → 1913.12] And you can do more than just blink an LED.
[1913.38 → 1920.78] You can control a whole WS2812 strip of RGB LEDs and do other neat things.
[1920.98 → 1923.96] So it's incredible what you could do with 8K of RAM.
[1924.46 → 1926.98] Don't you feel bad now about these giant programs you've written?
[1927.08 → 1927.70] I mean, I do.
[1928.02 → 1929.94] I think like, yeah, this program's tiny.
[1930.02 → 1931.36] It's like only like five megabytes.
[1931.36 → 1934.10] I'm like, oh, you know, only five megabytes.
[1934.74 → 1938.94] If you don't have a brand new shiny cool microcontroller,
[1939.18 → 1945.02] you should go to your drawer of stuff that you've been meaning to play with for a few years
[1945.02 → 1949.18] and just rifle around in there, find one of these boards.
[1949.56 → 1953.32] And if it doesn't work, we will try our hardest to make it work.
[1953.68 → 1958.48] So the question I had quickly, how would you compare Circuit Python and Tiny Go?
[1958.48 → 1966.86] Well, Circuit Python has got one big advantage and MicroPython, which it is based on,
[1967.48 → 1970.36] which is it having a great developer experience.
[1970.88 → 1972.26] I mean, absolutely fantastic.
[1972.42 → 1977.44] If you take one of these boards like the BBC Microbic or one of the boards from Ada fruit
[1977.44 → 1982.38] and you plug it into your USB port, and it pops up as a mass storage device,
[1982.46 → 1983.36] so it's just a drive.
[1983.36 → 1988.18] And so you take your Python program that you've written in whatever text editor
[1988.18 → 1992.64] and you drop it onto this drive, and it starts to run it.
[1992.94 → 1994.38] That is so beautiful.
[1994.86 → 2003.06] Just, oh, I mean, that kind of experience for a person that maybe is intimidated by programming
[2003.06 → 2006.10] or doesn't have a lot of experience.
[2006.88 → 2008.78] They're in a room with a bunch of hardware.
[2009.40 → 2010.60] They just plug it in.
[2010.88 → 2015.50] They drop a program on there with some simple type Python, and it just works.
[2016.06 → 2016.92] That is fantastic.
[2017.44 → 2020.76] What better on-ramp to hardware hacking?
[2020.96 → 2021.86] I can't think of one.
[2022.34 → 2023.90] So, I mean, that's a real advantage.
[2023.90 → 2027.48] But the disadvantage is the same as the advantage.
[2027.72 → 2033.80] You've now used up a lot of the memory on this small chip just for the tooling.
[2034.38 → 2037.66] So, if your program fits, you're great.
[2038.00 → 2041.58] But if it doesn't fit, you really can't do anything at all.
[2041.66 → 2042.42] That's the end of it.
[2042.96 → 2045.18] So, that's one definite difference.
[2045.80 → 2047.02] Python is a great language.
[2047.02 → 2051.84] It's one of these languages that, you know, if we were charting languages on one of these,
[2051.90 → 2056.32] you know, VC investment, Python is up and to the right consistently.
[2056.60 → 2058.28] Like, it doesn't, it's a hockey stick.
[2058.76 → 2061.78] So, you know, you're not like, okay, I'm not going to get rich on Python.
[2062.00 → 2062.30] Sorry.
[2062.78 → 2066.50] But on the growth of Python and this hypothetical exercise.
[2067.14 → 2069.38] But it's just steady year-over-year growth.
[2069.80 → 2073.88] You know, it's your fixed income bond investment of programming languages.
[2073.88 → 2075.48] Like, you can't go wrong learning Python.
[2075.48 → 2078.20] But it has also some drawbacks.
[2078.96 → 2082.84] And it was a really great talk that, I'm trying to think who gave it.
[2083.48 → 2085.68] It was at Gotham Go, I believe.
[2086.18 → 2088.72] Or maybe it was at Gopherpalooza.
[2089.18 → 2090.28] I can't think of which conference.
[2090.46 → 2100.12] But it talked about programming languages evolution and how Python's transition from Python 2 to 3 had been such a massive failure.
[2100.34 → 2100.92] Oh, right.
[2100.92 → 2106.80] Which Guido and the core team of Python readily acknowledge.
[2107.24 → 2110.56] I look at that, and I think, you know, there but for the grace of God go I.
[2111.02 → 2112.78] Not like, haha, you messed up Python.
[2112.92 → 2124.06] But more like, okay, that is the future of our favourite programming language if we are not very, very cautious about the way that we develop it and compatibility with things.
[2124.06 → 2127.64] And that's one reason why Tiny Go is not a 1.0 release yet.
[2127.78 → 2142.94] Because when we say, okay, it's 1.0, we take that responsibility seriously about, okay, now we're bound by the same covenants that the main Go implementation, if you will, has demanded of itself.
[2142.94 → 2151.76] Of saying, you can count on this for the next 15 years as a stable platform to keep the world actually running on.
[2152.30 → 2160.40] Since if the computers of the world stop working all at once, it's going to be really inconvenient for the people who are, like, in flight at the time, for example.
[2161.56 → 2162.64] Yes, it would be.
[2162.76 → 2162.90] Yeah.
[2163.24 → 2167.04] Tobias, I noticed you were laughing when Vladimir asked the question.
[2167.48 → 2169.24] What is your opinion about the comparison?
[2169.24 → 2175.46] Hey, that's a little bit unfair to say that I was laughing during the question.
[2175.62 → 2177.02] You don't have to answer if you don't want to.
[2177.26 → 2178.04] I can answer.
[2178.22 → 2182.50] So I'm not the greatest fan of Python in general.
[2182.66 → 2188.44] It might be a great language for people who just get into coding or start with coding and similar.
[2188.96 → 2198.80] But personally, I love to have a statically compiled language with static types and so on, where the compiler tells me, oh, you did something wrong.
[2199.50 → 2201.06] In compile time and not in runtime.
[2201.06 → 2202.70] I really, really love it.
[2202.78 → 2210.12] Let alone having a great language server and IDE support, giving you great help while writing your code.
[2210.12 → 2217.12] In general, I prefer Go to Python, which is also why I would always prefer Tiny Go over MicroPython.
[2217.52 → 2218.24] So, yeah.
[2219.10 → 2219.94] Fair point.
[2220.14 → 2220.88] That's a fair answer.
[2220.88 → 2226.92] I mean, there's another aspect, of course, which is, all right, so this all sounds like a great idea.
[2227.32 → 2231.44] And some top executive says, yes, this is our new platform.
[2231.58 → 2235.72] And then they take this to some technical review team.
[2235.72 → 2240.76] And they're like, wait, you're saying you could just update the source code on the devices in the field?
[2240.76 → 2242.26] Like, are you out of your mind?
[2242.36 → 2245.68] That's exactly how we get ransomware or who knows what.
[2245.68 → 2250.44] Like, actually, we would like you to spend the next six months making sure that's impossible to do.
[2251.38 → 2256.60] And then without any joke, you think security in your cloud is hard.
[2257.10 → 2257.30] Okay.
[2257.80 → 2261.72] Cloud security is trivially easy compared to device security.
[2261.72 → 2264.08] And look how insanely hard it is.
[2264.44 → 2265.80] It's insanely hard.
[2265.80 → 2273.22] Device security is so much worse because somebody could just, you know, get a hammer and smash the cover off the thing.
[2273.30 → 2275.34] And now they have access to the guts of the machine.
[2275.34 → 2276.54] And now they get started.
[2276.96 → 2277.06] Right.
[2277.30 → 2282.12] That almost feels like a spoiler to the Security Go episode that we're going to have in October.
[2284.22 → 2290.90] If you need somebody in a mask to take a sledgehammer and smash a cover off of a device, you know, I can help with that.
[2290.90 → 2295.52] Or take a picture and try to do the 3D face recognition.
[2296.88 → 2297.84] Yeah, exactly.
[2298.08 → 2300.14] It was dead program all along.
[2301.72 → 2304.54] I would have gotten away with it if it wasn't for you meddling robots.
[2304.54 → 2314.26] So the question I have for Tiny Go is how much, because you mentioned that you get safety, type safety.
[2314.70 → 2320.48] Do you get the Go runtime when you compile your code for the microcontroller?
[2320.64 → 2322.18] And how much of it do you carry over?
[2322.18 → 2332.96] So, as you might suspect, the runtime that you have on your operating system generally will call the operating system, as it should.
[2333.34 → 2336.82] But when there's no operating system, what do we do?
[2337.20 → 2338.96] There is no help to be called.
[2339.20 → 2340.12] Like, it is up to you.
[2340.50 → 2340.56] Right.
[2340.56 → 2351.94] The problem in Go, the implementation of Go itself today, is that there is a lot of coupling between the runtime and the standard libraries.
[2352.30 → 2356.20] Now, some of them are more well-structured.
[2356.94 → 2359.20] And there's good reasons why this is not easy to achieve.
[2359.58 → 2361.94] It's not like, oh, they were so lazy, they just couldn't do it.
[2362.00 → 2363.84] Like, no, no, it's really hard to do.
[2364.34 → 2365.62] Okay, really, really hard.
[2365.62 → 2369.56] But we have to have a different runtime, but with the same API.
[2370.60 → 2375.86] So, if you look at the way that Tiny Go is actually built, it's written entirely in Go, first.
[2376.56 → 2377.90] So, Tiny Go is written in Go.
[2378.38 → 2384.60] And then it uses Go's internal tooling to do part of its work.
[2385.06 → 2393.84] And then it uses the LLVM framework, which is a framework for creating programming languages, to do the other half of its work.
[2393.84 → 2400.68] So, hopefully, it doesn't sound like we didn't have to do anything, because actually getting those two things to work together, there's quite a bit to it.
[2400.90 → 2408.98] But you're not going to get the same runtime or even all the same standard library abilities when you have no operating system.
[2409.46 → 2415.76] A good example might be something you take for granted, which is, I would like to read a file off disk.
[2416.70 → 2418.00] All right, so let us begin.
[2418.08 → 2418.86] You have no disk.
[2419.42 → 2419.82] Okay.
[2420.18 → 2421.30] Also, no file system.
[2421.30 → 2424.46] So, right there, you're like, oh, that sounds very interesting.
[2425.06 → 2426.44] What do you do about that?
[2426.96 → 2432.62] Well, there are two different ways you store data, besides on a fixed disk.
[2432.72 → 2436.18] One of them is an SD card, and the other one is flash RAM.
[2436.86 → 2442.16] So, you need to know how do you read from them, and how do you write from them?
[2442.56 → 2444.74] Well, you have to do all these low-level hardware calls.
[2444.86 → 2445.96] Oh, that sounds very scary.
[2446.22 → 2447.68] That's way too much work.
[2447.68 → 2461.14] Luckily, we have interfaces in Go, and a lot of the internal types of Go's standard library are written using these well-defined interfaces internally.
[2461.92 → 2468.36] You know, a good example would be all the different ways that we can have readers and writers and reader-writer closers.
[2468.36 → 2468.96] Right.
[2469.14 → 2478.42] So, if we implement those same interfaces, but the actual implementation is perhaps talking to an SD card using the low-level protocols.
[2478.98 → 2480.00] This is not just hypothetical.
[2480.22 → 2485.26] This does already exist in Tiny Go, thanks to Tagusako-San.
[2485.26 → 2505.24] And Sago35, who's one of our most active contributors, is really one of the main people in a group of gophers, Tiny Gophers in Japan, who have been doing amazing things with hardware, as well as things that are directly tied to standards used in the automotive industry, for example.
[2505.24 → 2508.78] So, a lot of fascinating work happening there.
[2508.96 → 2521.80] But you have to do a lot of preliminary work to get to that point, because that runtime that we take for granted, I mean, even when you, let's just say hypothetically, you want to write some Windows' software in Go.
[2521.80 → 2533.00] You've got the runtime that's talking to all the lower-level Windows APIs to do the work that needs to be done, and you sort of take that for granted.
[2533.50 → 2540.48] Which, by the way, shout out to all the people who work hard on making Windows and Go work together.
[2540.94 → 2546.00] That doesn't receive the love that it should, but it's very hard work.
[2546.00 → 2552.54] And there are a lot of people using Windows, especially people who are not located in Europe or the U.S.
[2552.96 → 2563.68] One thing I've noticed with Gov in particular is we have a huge community of people in China using Windows for industrial computing, because Windows is the standard for industrial computing.
[2563.80 → 2566.38] If you go to a factory, it's all Windows machines everywhere.
[2567.22 → 2572.00] Not if you go somewhere like Northvolt, a company I consult for, that's all Go.
[2572.00 → 2578.40] But, you know, the vast majority of the 20th century of manufacturing is all built entirely on Windows PCs.
[2578.90 → 2579.30] Sure is.
[2579.52 → 2580.08] Sure is.
[2580.38 → 2581.10] Thank you.
[2581.22 → 2582.26] Went a little off the track.
[2582.96 → 2584.18] Well, it's very interesting.
[2584.46 → 2584.94] Yeah, it is.
[2585.06 → 2589.24] We talked a lot about kind of what you've worked on in the past, what's going on at the moment.
[2589.40 → 2593.64] So what's the future of Tiny Go and kind of programming for hardware?
[2593.94 → 2596.30] What is your prediction for where we're going?
[2596.64 → 2599.82] Well, Tobias bet a lot of time on writing a book about it.
[2599.82 → 2601.52] So I think he's all in.
[2602.18 → 2605.64] Vladimir, you're still dipping your toe in, but don't worry, you know, we got you hooked.
[2605.82 → 2611.14] The minute you were like, I want to try to get this thing to work and go on hardware, we had you one way or another.
[2611.92 → 2612.60] All right.
[2613.54 → 2613.92] Yes.
[2614.38 → 2622.10] Well, the future of Go, there was actually a very amusing article a few years back, blog post, that said eventually everyone ends up programming in Go.
[2622.10 → 2638.84] It was a person who did a hilarious eigenvector analysis with text processing of all the blog posts on Reddit and Hacker News that were why I switched from X to Y, where X and Y are programming languages.
[2638.84 → 2649.38] So he basically took this, and they put it through their models that they built, and they concluded that in only a few years, everyone ends up programming only in Go.
[2650.04 → 2650.78] This is awesome.
[2650.86 → 2652.20] You have to share the link to that.
[2652.44 → 2653.58] It has to be in the show notes.
[2653.74 → 2654.42] I need to read this.
[2654.42 → 2655.04] It's not me.
[2655.12 → 2655.80] It's the math.
[2656.24 → 2656.90] The machine learning.
[2657.42 → 2659.86] The AI said that you should program in Go.
[2660.00 → 2661.06] Sorry, Rust-Haitians.
[2661.06 → 2666.42] Sorry, all you people using Elixir happily or Rust or Lisp.
[2666.90 → 2669.60] All you people using Lisp, you're doing it wrong.
[2669.70 → 2670.52] You should use Go.
[2671.02 → 2672.14] There is only Go.
[2672.78 → 2680.68] I thought it was very funny, but there was something to it in the sense that there's no reason why only one language should exist.
[2681.36 → 2682.62] I mean, that's completely ridiculous.
[2683.50 → 2689.84] But the more languages you use, the harder it is for people to context switch between them.
[2689.84 → 2694.18] I mean, some people are really, they have idyllic abilities to switch between languages.
[2694.82 → 2696.42] And, you know, I think that's really admirable.
[2696.66 → 2701.26] But the vast majority of people who do programming, they really like programming.
[2701.40 → 2702.08] They wouldn't do it.
[2702.12 → 2704.20] But it's not their main passion in life.
[2704.30 → 2707.98] They're just, it's a really great job where they could do good things.
[2707.98 → 2712.34] Like, they're more excited about doing the things with the software than the software itself.
[2712.70 → 2714.00] Software is a means to an end.
[2714.08 → 2714.38] I know.
[2714.56 → 2714.70] Right.
[2714.84 → 2715.86] What means to an end?
[2715.90 → 2716.76] It's an end in itself.
[2716.76 → 2719.02] What are you talking about, Heretic?
[2719.84 → 2726.38] But Tiny Go, I'm not supposed to say too many big things about Tiny Go.
[2726.74 → 2727.56] First, tiny.
[2729.16 → 2733.80] But also, since, you know, I am on the core team and clearly biased.
[2734.58 → 2737.84] But Go is a very cool language.
[2738.28 → 2739.74] It's still growing rapidly.
[2740.16 → 2741.92] It has a big place.
[2741.92 → 2747.26] It basically won the war for the cloud, just very peaceably, because it was doing great things.
[2747.40 → 2755.78] I mean, things like Docker that have themselves created entire ecosystems could not have been created without Go.
[2756.16 → 2758.46] So all these things are the layer on top of each other.
[2758.46 → 2763.04] But, you know, the next frontier for software, what is that?
[2763.62 → 2768.26] Well, it's things like Web3 and truly distributed computing.
[2768.68 → 2772.14] That's where WebAssembly and WAS come in.
[2772.68 → 2774.36] And so, unpopular opinion.
[2776.28 → 2777.40] Another one.
[2777.48 → 2778.08] Another one.
[2778.08 → 2781.58] So, I did not say this myself.
[2781.76 → 2784.18] I'm just repeating what someone else said.
[2784.40 → 2789.58] But basically, without Tiny Go, Go doesn't even have a place in WebAssembly.
[2790.22 → 2791.40] It's just too big.
[2791.82 → 2792.20] Interesting.
[2792.58 → 2793.48] It's just too large.
[2793.76 → 2794.16] It is.
[2794.16 → 2807.42] So, there's actually a bunch of, I have a whole list of projects that are using Tiny Go today with WebAssembly in all sorts of different contexts.
[2808.04 → 2814.48] I mean, I know that sort of edge computing, I've been on record as saying, that's not real edge computing.
[2814.62 → 2816.42] That's just a data centre nearest you.
[2817.24 → 2819.48] Real edge computing is the last millimetre.
[2819.90 → 2820.20] Right.
[2820.20 → 2824.78] The hardware that you literally touch, like with your fingertip, that's edge computing.
[2825.38 → 2827.24] But that's not strictly true.
[2827.56 → 2827.82] I know.
[2827.90 → 2829.46] That was just a hilarious thing to say.
[2829.74 → 2830.84] But there are many edges.
[2831.34 → 2834.78] But there are a lot of really cool projects going on right now.
[2835.32 → 2837.48] Astro, if you've heard of that project.
[2838.30 → 2844.14] Astro's build is all built using Tiny Go for WebAssembly.
[2844.14 → 2852.04] That way they could reduce the necessary runtime for their application from, I think, six megabytes to 600K.
[2852.50 → 2853.40] Something like that.
[2853.50 → 2853.90] Oh, wow.
[2854.42 → 2855.06] Suborbital.
[2855.30 → 2859.28] They're doing a lot of stuff with Tiny Go and WebAssembly.
[2859.28 → 2872.38] The proxy WASM project, which is BI specification if you want to run WebAssembly on proxies like Envoy or Into.
[2872.88 → 2877.18] The only way to use Go from that is Tiny Go.
[2877.18 → 2888.50] And they have reasons why they tell you that largely to do with the main Go implementation not providing the necessary APIs as well as being too big.
[2889.02 → 2890.20] So we got that.
[2890.80 → 2895.08] Recti, which is front-end development in Go, Tiny Go.
[2895.08 → 2908.30] So just recently, there was a really cool project that came out called WASM 4, which lets you build retro-style gaming on a web interface.
[2908.64 → 2910.30] It's kind of a fantasy console.
[2910.82 → 2912.16] It's language agnostic.
[2912.40 → 2916.66] They have Rust and Python and C++ and, oh, yeah, Tiny Go.
[2916.76 → 2917.04] Sweet.
[2917.36 → 2918.34] So that's really cool.
[2918.34 → 2930.56] Then there's actual people doing the same thing, but in hardware, one of the coolest articles I saw recently was writing a Game Boy Advance game in Go.
[2931.26 → 2938.18] And naturally, they had to actually run it on their actual Game Boy Advance hardware, not just in a WebAssembly simulator.
[2938.78 → 2941.88] So naturally, I had to go and get some hardware to do exactly that myself.
[2941.88 → 2952.58] So in an upcoming episode of my stream that I do on Fridays from here at La Pipa, I'm going to be doing some GBA hacking just because I just want to do it.
[2952.82 → 2954.02] It's just too cool.
[2954.56 → 2966.50] But, you know, those are some of the things that are happening right now as far as places where the Tiny Go community has already surpassed the wider body of the Go community.
[2967.22 → 2971.56] Although I will say we do not view Tiny Go as separate from Go.
[2971.88 → 2973.26] Tiny Go is Go.
[2973.66 → 2974.14] Right.
[2974.46 → 2976.08] I know CGO is not Go.
[2976.84 → 2977.32] Right.
[2977.56 → 2982.60] But Tiny Go is Go because Go is a programming language.
[2982.72 → 2982.96] Right.
[2983.18 → 2984.10] There's also a runtime.
[2984.80 → 2986.44] There's also a standard library.
[2987.12 → 2989.66] But ultimately, it's a programming language.
[2990.20 → 2996.54] And if you have a compiler for a programming language, it's not a different programming language unless it's a different programming language.
[2996.54 → 2998.16] I mean, there are many C compilers.
[2999.04 → 3005.56] And ARM, that little company that's had small influence on the world of technology.
[3006.16 → 3016.54] So there's a very interesting project that I just heard about coming out of ARM, which is providing really great support on ARM-based microcontrollers for LLVM.
[3016.54 → 3027.34] And their first target is C, you know, because the idea is they want to replace the GCC compiler with something that's a bit more open.
[3027.34 → 3041.62] By open, I mean somebody can make some money since you need a job that pays you to actually work on some of these things or else you just can't spend the time necessary to do it.
[3042.00 → 3043.94] Now, that's why Go is so great.
[3044.40 → 3046.12] There are full-time paid maintainers.
[3046.80 → 3049.58] That's why LLVM is so great.
[3049.58 → 3051.94] There are people who work at Apple.
[3052.30 → 3053.66] There's people who work at Google.
[3054.02 → 3055.42] There's people who work at Intel.
[3055.70 → 3059.70] Their full-time job is to do nothing but work on LLVM.
[3059.90 → 3063.52] If it wasn't for all of those people, we couldn't do the things we do.
[3064.08 → 3065.14] So, kudos.
[3065.76 → 3067.42] But there's another unpopular opinion.
[3068.28 → 3069.58] Oh, my gosh.
[3071.24 → 3074.44] Open source could not exist without big companies.
[3074.66 → 3075.62] Is that really unpopular?
[3076.12 → 3076.46] Yeah.
[3076.46 → 3080.14] I'm not saying people don't agree, but it's for sure unpopular.
[3081.34 → 3083.24] Can you say a bit more on that?
[3083.72 → 3089.46] Well, first time an open source project becomes important is as soon as somebody starts making money with it.
[3089.78 → 3091.12] Up until then, it's just a hobby.
[3091.84 → 3092.70] You know, it's an experiment.
[3092.98 → 3093.88] It's a cool thing.
[3094.18 → 3100.70] As soon as company A tells you, hey, Vladimir, we want to pay you to work on this thing.
[3100.72 → 3102.54] And you're like, oh, okay, cool.
[3103.00 → 3104.62] Tiny girl, yeah, totally know that.
[3104.62 → 3108.82] You know, like then you read Tobias' book on the way to the job in review.
[3110.50 → 3110.94] Right?
[3111.24 → 3114.24] Only now is this open source project actually matter.
[3114.54 → 3114.64] Right.
[3114.82 → 3115.90] I mean, really matter.
[3116.32 → 3119.60] Before that, it's like it's fun and it's cool.
[3120.06 → 3126.92] And I mean, I don't want to talk down on people's vanity projects because it makes them feel good or on people's love projects because they just need to share.
[3126.92 → 3128.84] Because those are wonderful things.
[3129.52 → 3138.78] But you need to have a pretty understanding boss to be like, yeah, I got to go fly halfway around the world to go do this, you know, conference and go talk about this way to make games.
[3138.88 → 3140.16] I know we're not a game company.
[3140.56 → 3143.38] And in fact, no, I'm not spending too much time on it.
[3143.38 → 3144.10] Really, I swear.
[3144.10 → 3156.20] Until you have somebody paying, you know, in the capitalist society in which we live, there is no way to have a sustainable project.
[3156.74 → 3158.96] Somebody has to come up with some money at some point.
[3159.64 → 3160.06] Unpopular?
[3160.64 → 3161.04] Yes.
[3161.48 → 3163.38] But not disagreed with, probably.
[3163.38 → 3174.06] An example from our direct experience, there's a bunch of people who work at Vastly who are working very diligently on contributing to Tiny Go.
[3174.66 → 3184.92] Now, I can't tell you exactly what they're doing right now, but they are doing a lot of fascinating work that is helping the broader community quite a lot.
[3185.68 → 3191.02] And I doubt that they would be able to devote that much time and energy if it wasn't their day job.
[3191.02 → 3198.32] Do you see a day when Tiny Go is on par with the regular flavour of Go as far as popularity, adoption?
[3198.94 → 3200.84] I mean, it serves a very different purpose.
[3201.22 → 3205.20] I think WebAssembly is the only thing that can maybe change that equation.
[3205.66 → 3216.28] Although there's the thriving ecosystem of building out cloud native, the amazing other things that are happening with other applications of Go.
[3216.28 → 3219.60] Go in the UI, whether it's Geo or Fire.
[3219.92 → 3228.72] I mean, there are so many interesting things that are happening in Go that for me to say, oh, yeah, Tiny Go is the most important.
[3229.40 → 3232.64] I don't think I could really say anything is the most important.
[3232.76 → 3238.00] But I will say hardware development is too important to be left to hardware developers.
[3238.66 → 3239.14] Right?
[3239.14 → 3241.62] That sounds like another unpopular opinion.
[3242.08 → 3242.64] Possibly.
[3243.94 → 3250.66] But as there's more and more small devices just out in the world doing things, like what are they doing?
[3251.04 → 3252.30] Well, we don't know.
[3252.52 → 3254.70] But maybe it's very bad things.
[3255.18 → 3266.44] We've heard lots of, not to complain about Google in particular, but because of the success of things like Nest, you know, and Ring, suddenly they're the bad people.
[3266.44 → 3268.06] Because they're doing bad things.
[3268.58 → 3269.02] Right?
[3269.14 → 3270.34] And so how do we prevent that?
[3270.48 → 3273.12] Well, we have to have more people doing hardware development.
[3273.40 → 3274.56] That way it's less siloed.
[3275.06 → 3284.10] If you go to a conference that specializes in hardware development, like Embedded World, it's a bunch of older gray-haired men.
[3284.60 → 3287.68] And if you go up to some of them, and you say, have you heard of Go?
[3287.86 → 3288.88] They'll be like, no.
[3289.66 → 3290.78] We use C.
[3291.18 → 3291.46] Right?
[3291.46 → 3296.08] We've been using C since, like they say, C was good enough for my grandfather.
[3296.38 → 3297.48] It was good enough for my father.
[3298.46 → 3301.82] And this is like, it's not just a figure of speech.
[3301.82 → 3304.50] They're like, yeah, my grandfather was using C.
[3304.62 → 3304.92] Wow.
[3305.02 → 3305.42] Amazing.
[3306.10 → 3309.16] I would say C has killed more people than any other programming language.
[3309.78 → 3314.12] Oh, but most of the medical devices are built in C, so that would be some sort of bias.
[3314.34 → 3314.92] That's right.
[3315.12 → 3315.78] Thank you, Natalie.
[3316.56 → 3316.96] Exactly.
[3316.96 → 3320.74] I was hoping somebody would see the logical fallacy in this argument.
[3321.64 → 3324.78] But does that mean we have to keep doing it that way?
[3324.86 → 3325.08] Right.
[3325.42 → 3326.16] I hope not.
[3326.50 → 3327.56] Should it be Tiny Go?
[3327.84 → 3329.42] We want Tiny Go to be an option.
[3329.58 → 3330.24] Should it be Rust?
[3330.40 → 3331.92] We want Rust to be an option, too.
[3332.08 → 3335.90] Rust is really cool, and a lot of interesting people are doing smart things with it.
[3335.94 → 3337.06] Very interesting things, yeah.
[3337.18 → 3340.52] What about Elixir running on Embedded?
[3340.94 → 3344.16] What about even languages that we don't know about yet?
[3344.84 → 3345.80] Those could occur.
[3345.80 → 3352.28] It's hard to say where the next exciting tangent, although I know Tobias' unpopular opinion,
[3352.98 → 3354.48] so I'll let him say that one.
[3354.82 → 3355.34] Thank you.
[3355.92 → 3356.68] At least this one.
[3359.24 → 3361.92] I told you I had a lot of the unpopular opinion thing.
[3361.98 → 3363.18] They just started flowing out.
[3364.90 → 3366.10] I couldn't stop them.
[3366.18 → 3367.84] I was like, oh, I feel so light.
[3369.68 → 3374.30] Well, not to worry, because I think we are, in fact, going to dive into unpopular opinions now.
[3374.30 → 3376.78] So, hold that door.
[3376.86 → 3377.52] I've run out.
[3378.20 → 3378.62] Oh, no.
[3382.62 → 3383.14] What?
[3385.60 → 3387.30] I actually think she'd probably leave.
[3387.30 → 3392.26] Unpopular opinions.
[3396.26 → 3396.80] Great.
[3396.90 → 3402.78] So we're going to be going straight to you, Tobias, because we've been waiting in anticipation
[3402.78 → 3404.60] for this unpopular opinion.
[3405.04 → 3405.24] Yeah.
[3405.24 → 3409.22] After we heard hundreds of unpopular opinions from Ron right now.
[3411.12 → 3411.86] That many?
[3412.02 → 3412.28] Wow.
[3412.28 → 3418.06] I'm not quite sure where on the scale of a popular or unpopular I'll end, but I'll
[3418.06 → 3418.70] throw it out now.
[3419.06 → 3423.76] So I'm of the opinion that there has been nothing significantly new in software development
[3423.76 → 3425.18] in the past 20 years.
[3425.64 → 3429.62] And additionally, it's always the same cat just with a different hat on it.
[3429.98 → 3432.90] Well, I'm going to disagree with you, Tobias, in one regard.
[3434.78 → 3435.26] Perfect.
[3436.06 → 3436.54] Congratulations.
[3436.78 → 3438.46] It's way more than 20 years.
[3438.46 → 3439.60] That's what I was thinking, too.
[3439.66 → 3440.76] I'm like, is it just 20?
[3440.76 → 3441.78] One year is none of it.
[3441.80 → 3442.36] Okay, it's easy.
[3442.46 → 3443.48] Way more than 20 years.
[3443.54 → 3447.66] And I can also give a little explanation why I am of this opinion.
[3448.12 → 3454.70] Let's have a look at all of these development process frameworks from extreme programming
[3454.70 → 3455.28] in Kanban.
[3455.48 → 3457.44] And I don't know, there are thousands of them.
[3458.00 → 3461.66] And more or less, they all boil down to the same few basic concepts.
[3461.96 → 3467.56] And the Agile Manifesto thingy has been written, I guess, around 20 years ago.
[3467.56 → 3472.76] And all of these frameworks still reside on these same principles.
[3473.38 → 3475.78] And the same is for everything else in software development.
[3475.92 → 3479.20] There's a new cool architecture structure for your software.
[3479.80 → 3484.08] The one called Onion Architecture, Layered Architecture, Clean Architecture, whatever architecture,
[3484.28 → 3485.34] Hexagonal Architecture.
[3485.74 → 3488.78] But it all boils down to the same few principles.
[3489.12 → 3491.60] So I'm saying there has been nothing new in software development.
[3492.10 → 3492.40] Interesting.
[3492.80 → 3494.04] Actual software development.
[3494.04 → 3496.24] The practice of software development.
[3496.42 → 3496.58] Okay.
[3497.20 → 3497.60] Interesting.
[3497.94 → 3498.86] We'll see on Twitter.
[3499.06 → 3500.92] Yeah, I'm excited to see where that falls.
[3501.32 → 3502.52] What the followers will say.
[3502.64 → 3503.34] How about you, Vladimir?
[3503.48 → 3504.86] What's your unpopular opinion?
[3505.42 → 3510.20] You know, it's interesting because it kind of lined up with what Ron and Tobias has been
[3510.20 → 3510.54] saying.
[3510.68 → 3517.42] Mine is, our industry takes pride in disqualifying folks because they don't use a favourite antiquated
[3517.42 → 3520.60] tool like your C, VI, Emacs, Bash, etc.
[3520.60 → 3523.82] And my unpopular opinion is that we should stop.
[3523.92 → 3530.40] There's a level of wall garden or some kind of ivory tower around these tools where, you
[3530.40 → 3535.28] know if you're not using C, if you're not using, and hopefully we don't get to that point
[3535.28 → 3542.58] with Go or Rust, but people who are using or developing in software like JS, we tend to
[3542.58 → 3549.36] not look that as a real language when we have billions of dollars of value being written
[3549.36 → 3551.88] in JavaScript probably every day.
[3552.40 → 3557.40] So that's my unpopular opinion is that we need to stop disqualifying folks around these.
[3557.78 → 3560.48] And I call them antiquated because those tools are very old.
[3561.10 → 3561.38] So yeah.
[3561.38 → 3564.58] Yeah, I have Emacs macros that are older than I am.
[3565.02 → 3565.76] Yes, exactly.
[3566.54 → 3567.96] Yeah, that's a perfect point.
[3568.46 → 3573.18] I guess my biggest struggle with Rust, not to pick on Rust in particular, but let's pick
[3573.18 → 3573.64] on Rust.
[3574.06 → 3578.48] I feel like, and I'm going to misstate it, the philosophy of Rust says, let's make it
[3578.48 → 3583.14] so hard to write programs that you can't write them anymore and therefore there won't be any
[3583.14 → 3583.78] bad software.
[3584.36 → 3587.98] You know, not literally that, but you can't write bad programs.
[3588.78 → 3588.98] Okay.
[3589.30 → 3590.44] Sorry, cannot write them.
[3590.44 → 3596.24] That sounds perfect if I think about it from like a really far away distance, like
[3596.24 → 3598.76] I'm looking at the planet on a telescope.
[3599.50 → 3603.98] But when I get up really close to all of these people who are just trying to, there are a lot
[3603.98 → 3606.70] of people whose lives have been changed by learning to program.
[3607.02 → 3610.52] I know we've like talked on about boot camps and things, but forget the boot camp thing.
[3610.52 → 3617.84] Let's just say a person who decided to read Tobias's book, figured out how to write tiny
[3617.84 → 3623.92] girl code, went to a job interview, got the job, and is now making three or four or five
[3623.92 → 3626.22] times more money and can actually pay their bills.
[3626.60 → 3629.74] Suddenly they could take care of their obligations to their family.
[3629.74 → 3634.20] They have so much less anxiety in their life, so much less stress.
[3634.20 → 3639.62] They can participate in things they couldn't participate in before, whether that's civic
[3639.62 → 3643.10] things, family things, personal things.
[3643.10 → 3645.48] That person's life has been changed.
[3645.72 → 3647.80] If it's JavaScript or if it's a spreadsheet.
[3648.48 → 3648.74] Okay.
[3648.86 → 3650.56] My unpopular opinion, another one.
[3653.26 → 3656.90] Spreadsheets are the most important development ever in software.
[3657.50 → 3662.32] The spreadsheet is the highest evolution of software to date.
[3662.50 → 3663.06] Yes.
[3663.06 → 3663.70] Okay.
[3664.18 → 3669.98] Because it has let the most human beings do the most with computing about something, a
[3669.98 → 3671.80] problem they were just trying to solve.
[3672.08 → 3673.76] Like, we're too cool for that.
[3674.04 → 3674.48] I know.
[3674.74 → 3676.44] Like, I don't use spreadsheets.
[3676.50 → 3677.20] I just hide them.
[3677.76 → 3678.32] Right.
[3679.38 → 3686.14] I just think there's a barrier between the professional programming priesthood and the
[3686.14 → 3687.52] regular human being.
[3687.84 → 3693.04] That is exactly what I don't want for me, myself, why I am in software.
[3693.06 → 3696.40] Is to do things to stop that from happening.
[3696.92 → 3702.04] And if some of those people do things with the software I don't expect, well, that's how
[3702.04 → 3702.74] life works.
[3703.22 → 3704.32] There's another one.
[3704.72 → 3708.32] Once you publish your open source software, you have no control over what people do with
[3708.32 → 3708.46] it.
[3708.52 → 3709.14] That's true.
[3709.44 → 3712.14] Don't slap a license on there saying you won't do evil.
[3712.24 → 3716.28] It's like, haha, I laugh at your license and I use it to write ransomware with, you know.
[3717.36 → 3722.48] I mean, not me personally, but I just don't think that you have that kind of control over
[3722.48 → 3723.04] your software.
[3723.68 → 3728.96] Once you release it into the world, like your children, you hope you've given it a good
[3728.96 → 3732.66] foundation, but you no longer have any control over whatever they do.
[3732.74 → 3733.96] I explained this to my parents.
[3734.48 → 3735.78] Was it your fault, mom and dad?
[3735.86 → 3738.48] It was just, I read the wrong book at some point.
[3739.26 → 3740.78] Any more unpopular opinions?
[3741.62 → 3742.06] Matt, leave.
[3742.12 → 3742.56] You got one?
[3743.00 → 3743.94] From anyone else?
[3743.94 → 3747.66] I'm just trying to channel my inner Matt Refer.
[3749.98 → 3753.16] I hear Matt and I just think, first, Matt, I miss you, man.
[3753.48 → 3755.18] I got to come over there.
[3755.42 → 3758.64] If they let people from Spain come to the UK again, I'll come and visit.
[3759.46 → 3759.92] But okay.
[3760.00 → 3761.16] Another unpopular opinion.
[3761.46 → 3762.86] This one is for Mark Bates.
[3763.62 → 3766.26] So Mark, I saw your recent photo with your beard.
[3766.74 → 3767.40] Great beard.
[3767.50 → 3768.40] You look great, man.
[3768.40 → 3771.06] But my beard is so much more distinguished.
[3773.40 → 3774.22] Sorry, Mark.
[3774.60 → 3778.62] Yours is thicker, fuller, but mine has got that distinguished.
[3779.48 → 3780.46] What does that mean?
[3780.52 → 3781.06] I don't know.
[3781.72 → 3784.10] But I did have another more serious unpopular opinion.
[3785.30 → 3786.08] I'm dying.
[3786.46 → 3788.20] What is your final unpopular opinion?
[3788.20 → 3789.14] What's the final?
[3790.02 → 3794.50] Use your final unpopular opinion wisely because you only get one more.
[3795.18 → 3796.16] No, he's changing it.
[3796.18 → 3797.02] I'm cutting you off.
[3797.06 → 3797.88] He's changing it.
[3798.76 → 3805.72] Human beings are more dangerous to other human beings than AI will ever be.
[3806.44 → 3807.38] That's understandable.
[3807.78 → 3810.98] Human beings have caused and will cause more harm to other humans.
[3811.80 → 3813.38] AI is just an excuse.
[3814.14 → 3816.52] I didn't know the gun was loaded kind of thing.
[3817.08 → 3821.72] I guess it's not very popular underneath a tinfoil hat, people.
[3823.10 → 3824.72] Maybe that was kind of a joy kill.
[3825.00 → 3827.68] Like, oh, it was so fun up until like, oh, wow, Terminator.
[3827.68 → 3828.88] Not the Terminator.
[3829.04 → 3831.14] The person flying the Terminator remotely.
[3831.48 → 3832.96] That's what you got to worry about.
[3833.28 → 3833.40] Yeah.
[3834.08 → 3835.00] Our final unpopular opinion.
[3835.66 → 3836.00] Natalie.
[3836.00 → 3839.48] My unpopular opinion is about Zoom fatigue.
[3839.48 → 3839.88] Okay.
[3840.38 → 3846.42] And people want things to be in person again because of that Zoom fatigue.
[3846.42 → 3854.92] And while I totally get that, my unpopular opinion is that I hope that events will stay hybrid at the very least, if not fully online.
[3855.10 → 3856.40] Probably not fully online.
[3856.40 → 3863.24] And the reason is that it's more environmental friendly, but it's also a lot more accessible to everyone else.
[3863.40 → 3863.66] Oh, yeah.
[3863.92 → 3864.94] Conferences, meetups.
[3865.00 → 3865.38] Agreed.
[3865.82 → 3866.22] Hackathons.
[3866.44 → 3866.78] Everything.
[3867.12 → 3867.54] Agreed.
[3867.82 → 3868.38] No, no.
[3868.44 → 3869.54] You should be disagreeing.
[3869.76 → 3870.18] No, no, no.
[3870.38 → 3870.80] I'm agreeing.
[3870.80 → 3872.46] We talked about Zoom fatigue on Twitter.
[3872.72 → 3874.62] You cannot agree with my unpopular opinion.
[3874.74 → 3875.08] I'm sorry.
[3875.26 → 3877.58] I miss the real world, my friends.
[3877.58 → 3886.20] But also, it's like, oh, we need name tags that say handshake, hug, or don't even touch me.
[3886.20 → 3886.50] Yes.
[3886.86 → 3887.30] Options.
[3887.62 → 3887.92] Elbow.
[3888.04 → 3888.24] Right?
[3888.74 → 3889.36] Colour-coded.
[3889.56 → 3889.80] Yeah.
[3890.16 → 3895.30] Just to sort of make sure there's no embarrassing, like one kiss, two kiss, no kiss.
[3895.30 → 3904.26] We'll have a whole colour-coordinated scheme where you walk into an event, and you grab a red beanie for stay away, a blue beanie for a hug, et cetera, et cetera.
[3904.68 → 3906.60] What happens when you take on the full rainbow?
[3906.60 → 3910.20] Then you're just open to whatever the other person would like.
[3910.36 → 3911.44] Whatever happens, right?
[3911.48 → 3912.52] And a tinfoil hat.
[3912.80 → 3913.02] Yeah.
[3913.98 → 3926.56] The only drawback to virtual events for new speakers, I've gotten feedback from maybe a dozen people whose first experience at presenting was online.
[3927.18 → 3929.22] And it was very, very hard for them.
[3929.78 → 3932.80] Because your first presentation experience is quite hard, generally.
[3933.40 → 3936.14] Like, it's really hard because, oh, I'm scared to get in front of people.
[3936.14 → 3938.90] It's even worse when there's no people there.
[3939.02 → 3941.16] So, like, you don't even, like, hello, is this thing on?
[3941.30 → 3942.42] Like, testing one, two, three?
[3942.64 → 3942.82] You know.
[3943.14 → 3943.46] No.
[3943.68 → 3952.22] I feel a great deal of compassion for the people who are just getting started to present some interesting things they're doing.
[3952.22 → 3958.68] Because I think you have to work a lot harder to try to find the – it's about contact.
[3958.94 → 3960.72] It's not just about, here's information.
[3961.22 → 3963.46] It's about some type of human touch to it.
[3963.62 → 3964.84] And it's very hard.
[3965.16 → 3967.40] Also, networking is very hard online.
[3968.08 → 3974.16] And my thought is that it should not be solved by going back to what we know, but by improving this new situation.
[3974.38 → 3974.60] Right.
[3974.60 → 3975.52] And we're still not there.
[3975.62 → 3978.70] There are all sorts of platforms that are trying all sorts of ways of doing that.
[3978.86 → 3980.36] And I just think we should try harder.
[3980.86 → 3981.20] Oh, yeah.
[3981.48 → 3983.54] It's definitely a technology problem.
[3983.96 → 3985.42] A lot of it is a technology problem.
[3985.42 → 3999.10] So there was a conference called Roguelike that I believe last year they did a brilliant job of creating a whole mud for their conference where you could – they had virtual items and a virtual bar.
[3999.34 → 4005.72] And you could walk – when you walked into one of the salons that the talk was in, then it would bring up the streaming video.
[4006.18 → 4008.06] I just thought that was absolutely brilliant.
[4008.46 → 4008.62] Yeah.
[4008.76 → 4011.02] I'm not sure if it was the best user experience or not.
[4011.10 → 4011.94] I did not attend it.
[4011.94 → 4017.94] I just saw it, but I just thought, at last, another approach towards how to do this.
[4017.94 → 4024.66] Just to riff on Natalie's take, yes, let's try to explore the medium and find different forms.
[4024.86 → 4025.02] Yep.
[4025.40 → 4025.84] Agreed.
[4026.04 → 4026.84] 100%.
[4026.84 → 4028.52] Keep on experimenting.
[4029.22 → 4029.60] Awesome.
[4029.82 → 4041.80] Well, I'm going to close with my unpopular opinion, which you've all heard on a lighter note, is that I think that this obsession with pumpkin in the U.S., as soon as Labour Day is over, needs to stop.
[4041.94 → 4044.26] Like, I don't need pumpkin on everything.
[4044.42 → 4049.18] I'm like, pumpkin spice latte, pumpkin bread, pumpkin cheese.
[4049.54 → 4052.30] Like, everything suddenly becomes pumpkin.
[4052.58 → 4053.84] Pumpkin cheese.
[4054.34 → 4059.30] I literally saw, like, a pumpkin sausage in the supermarket.
[4059.94 → 4065.04] Like, everything suddenly is orange, and they feel the need to put pumpkin in it.
[4065.32 → 4067.80] Which you drink a pumpkin beer with, of course.
[4068.00 → 4068.16] Yeah.
[4068.16 → 4069.22] There are no jokes.
[4069.30 → 4070.48] There is pumpkin ale.
[4070.64 → 4071.92] Pumpkin lettuce soap.
[4072.26 → 4073.84] Like, just pumpkin everything.
[4073.94 → 4075.22] I'm like, what is this?
[4075.28 → 4075.94] I get it.
[4076.20 → 4076.86] It's full.
[4077.36 → 4078.66] I don't need pumpkins.
[4079.94 → 4083.26] On that light note, thank you all.
[4083.72 → 4085.30] This has been a wonderful conversation.
[4085.30 → 4087.24] So many interesting things have come up.
[4087.32 → 4090.72] I certainly know I'm going to be Googling things for days after this conversation.
[4091.52 → 4092.82] I really appreciate your time.
[4092.94 → 4095.98] Thank you, Natalie, as always, for being my wonderful fellow panellists.
[4096.48 → 4099.02] And I hope everyone listening and watching enjoyed.
[4099.40 → 4100.28] Thank you, Angelica.
[4100.50 → 4100.96] Thank you.
[4100.96 → 4105.46] All right.
[4105.54 → 4106.40] That's our show.
[4106.50 → 4107.02] Thanks for listening.
[4107.32 → 4108.76] We appreciate you hanging with us.
[4109.66 → 4113.32] Have you rated or reviewed the show on your podcast platform of choice?
[4113.60 → 4114.46] You should.
[4114.96 → 4117.96] Because every time a review lands, a gopher gets its wings.
[4119.32 → 4122.98] Go Time is produced by Jared Santo with music by Break master Cylinder.
[4123.64 → 4126.34] We are brought to you by Vastly, Launch Darkly, and Linde.
[4126.34 → 4130.46] Our next episode is number 200, but it's more than okay.
[4130.92 → 4137.72] The OGs, Brian, Galicia, and Eric, join us to celebrate and play a crazy game of Gophers Say.
[4138.50 → 4140.42] That's something for you to look forward to.
[4140.74 → 4143.72] We'll have it ready for your next time on Go Time.
[4156.34 → 4158.34] Go Time.
