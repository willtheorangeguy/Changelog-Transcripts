[0.00 --> 8.48]  When we think of smart home at Amazon and within Alexa, we're kind of thinking if we're really going to add intelligence to the home, what can it really do for customers?
[8.58 --> 9.74]  And how do we make it really easy?
[9.84 --> 12.86]  So one part, of course, is like, OK, we're going to get Alexa into the picture.
[13.06 --> 14.94]  And so now we have voice control of the home.
[15.06 --> 17.68]  It's kind of like the great enabler, the great simplifier.
[17.82 --> 21.30]  You can just say, you know, Alexa, turn off my light and she'll turn off the lights.
[21.42 --> 23.56]  Very, very simple type of interaction.
[23.56 --> 32.98]  But the other sort of piece of that that we think about a lot is what we call kind of an actually smart home, which is it's not just sort of a fancy remote control for your home.
[33.08 --> 36.08]  It's not just sort of like I push this button and then that automation happens.
[36.22 --> 49.34]  It's having a home with this intelligent assistant, Alexa, that can really do things on your behalf, things that are really valuable to you, help you achieve high level goals like living more sustainably or just being more comfortable or keeping your family safe.
[49.34 --> 54.78]  Big thanks to our partners, Linode, Fastly and LaunchDarkly.
[55.16 --> 55.74]  We love Linode.
[55.80 --> 57.22]  They keep it fast and simple.
[57.34 --> 59.70]  Check them out at Linode.com slash changelog.
[59.94 --> 62.00]  Our bandwidth is provided by Fastly.
[62.36 --> 65.90]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[66.18 --> 67.90]  Get a demo at LaunchDarkly.com.
[70.88 --> 73.38]  This episode is brought to you by our friends at O'Reilly.
[73.74 --> 79.32]  Many of you know O'Reilly for their animal tech books and their conferences, but you may not know they have an online learning platform.
[79.34 --> 84.70]  The platform has all their books, all their videos and all their conference talks.
[85.04 --> 95.82]  Plus, you can learn by doing with live online training courses and virtual conferences, certification practice exams and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[95.82 --> 109.76]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security, and even soft skills like business management and presentation skills.
[109.88 --> 111.66]  You name it, it is all in there.
[111.98 --> 117.14]  If you need to keep your team or yourself up to speed on their tech skills, then check out O'Reilly's online learning platform.
[117.14 --> 121.24]  Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[121.34 --> 123.64]  Again, O'Reilly.com slash changelog.
[132.34 --> 139.52]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[139.52 --> 143.92]  This is where conversations around AI, machine learning, and data science happen.
[144.18 --> 150.30]  Join the community and Slack with us around various topics of the show at changelog.com slash community and follow us on Twitter.
[150.44 --> 152.04]  We're at Practical AI FM.
[158.20 --> 161.22]  Welcome to another episode of Practical AI.
[161.54 --> 163.14]  This is Daniel Whitenack.
[163.14 --> 173.62]  I am a data scientist with SIL International, and I'm joined as always by Chris Benson, who is Principal Emerging Technology Strategist at Lockheed Martin.
[173.94 --> 174.58]  How are you doing, Chris?
[174.90 --> 176.24]  I am doing fine.
[176.34 --> 178.26]  Just been like crazy busy.
[178.62 --> 181.20]  We have this beautiful spring weather.
[181.84 --> 186.14]  And, you know, I don't know if I've mentioned this before, but my wife and I are planning to move.
[186.22 --> 191.60]  And so we're thinking about a new house, and we're going to build on a five-acre plot of land.
[191.60 --> 194.78]  And you know how I am with all the animals I love during wildlife rehab and all.
[195.32 --> 199.70]  Following the trend of people getting a little bit further out after COVID.
[199.80 --> 208.10]  I know there's a lot of people sort of moving out of various places like San Francisco and other places after working remote for some time and all that.
[208.30 --> 211.92]  Yeah, the price of wood and lumber for building is at an all-time high.
[212.18 --> 213.62]  And so we're trying to figure out what our time.
[213.62 --> 215.88]  We could do it soon, but we're trying to figure out a timeline.
[215.88 --> 221.02]  But I'm having a blast trying to think about what I want in my new home.
[221.30 --> 223.24]  And as I'm trying to think about like...
[223.24 --> 224.42]  Is it going to be a smart home?
[224.86 --> 230.52]  You know, I have been bringing that up with my wife quite a bit in terms of like, you know, what could we do?
[230.76 --> 235.24]  And she, of course, I bring it up and she rolls her eyes at me because it's the kind of thing she expects from me.
[235.30 --> 238.42]  But I'm pretty excited about this idea of a smart home.
[238.56 --> 239.58]  We're building from scratch.
[239.66 --> 241.12]  We can do all sorts of cool things.
[241.12 --> 244.20]  And I need some new ideas, my friend.
[244.44 --> 244.64]  Yeah.
[245.10 --> 245.32]  Yeah.
[245.36 --> 250.22]  I mean, we've gone, you know, locks, thermostats, some other things.
[250.22 --> 258.40]  I know at my wife's business, they have a bunch of, you know, Alexas around the work because they play various music around.
[258.74 --> 261.04]  And, you know, they have them in the offices, actually.
[261.28 --> 262.98]  So, yeah, I mean, there's a lot of choices.
[263.14 --> 264.04]  Of course, you could go.
[264.04 --> 275.80]  I think there's the, like, meme from Silicon Valley where the, you know, they have the smart fridge and, you know, they all hack into it or something and display all sorts of profane things.
[275.96 --> 276.86]  But, yeah, I think you can.
[277.18 --> 278.80]  There's so many choices out there now.
[278.96 --> 282.40]  And I'm excited because I'm definitely interested in that topic.
[282.40 --> 292.72]  And today we've got a chance to talk a lot more about it with Evan Wellborn, who leads the smart home machine learning team at Amazon.
[293.04 --> 296.56]  So, who better to inform you about your new house, Chris?
[296.80 --> 297.78]  Yeah, absolutely.
[298.18 --> 298.40]  Welcome.
[298.80 --> 299.54]  Thank you so much.
[299.78 --> 300.66]  So glad to be here.
[301.06 --> 301.40]  Yeah.
[301.58 --> 309.80]  Well, before we jump into all that good smart home stuff, could you just give us a little bit of information about yourself and your background?
[311.04 --> 311.74]  Yeah, sure.
[311.74 --> 316.38]  So my background is actually focused primarily on the Internet of Things.
[316.94 --> 323.66]  And I've worked in that space for, you know, since the early 2000s when I was a grad student at the University of Washington studying computer science.
[323.90 --> 330.44]  And at that time, I was working on things like sensor networks, RFID, you know, GPS, some of the really early smartphone stuff.
[330.78 --> 338.10]  And a lot of that work was trying to infer the context of the customer or the user from, like, you know, all that diverse sensor data.
[338.10 --> 342.40]  And for things like running versus walking or are they at home or work or the commuting?
[342.88 --> 346.58]  And then trying to build and evaluate applications using that type of intelligence.
[346.58 --> 354.36]  So things like activity trackers, reminders, various types of assisted living, location-based, you know, social networks, things like that.
[354.60 --> 356.86]  And so machine learning was always a tool.
[357.22 --> 361.04]  I'm wondering if that is that sort of activity tracking technology.
[361.04 --> 369.12]  Is that really like a product of some of the sort of neural network deep learning boom of recent times?
[369.12 --> 376.06]  Or have people been trying to do this sort of activity tracking sort of thing for some time with more or less success?
[376.06 --> 382.08]  Oh, yeah. It's been going on for quite a while in research, at least, you know, 20, more than 20 years.
[382.08 --> 387.06]  People have been just experimenting with simple things like, you know, accelerometers or motion sensors.
[387.06 --> 393.80]  And then can we use, you know, I was using decision trees quite often, you know, just the most basic of models.
[393.88 --> 395.54]  You can get pretty far with basic models.
[395.72 --> 399.62]  But, of course, when you're really trying to scale something and make it work for everyone, you end up.
[399.78 --> 402.32]  Yeah, you've got to use the more sophisticated approaches.
[402.82 --> 403.42]  Yeah, it makes sense.
[403.42 --> 411.90]  So how did that activity tracking sort of work lead into later things in your career and where you're at now thinking about smart homes?
[412.20 --> 417.42]  Yeah. So sort of by the end of my PhD, it was clear that machine learning wasn't just a tool.
[417.50 --> 418.72]  It was kind of like the tool, right?
[418.76 --> 420.96]  So a lot more focus on machine learning.
[421.08 --> 432.08]  And then at that time, smartphones, you know, the iPhone had just kind of come out and it was becoming clear, like smartphones were probably going to be the technology that would kind of carry us to the next wave of Internet of things.
[432.08 --> 434.44]  And start, you know, we'd start realizing some of this vision.
[434.44 --> 440.74]  And so I went from graduate school, I went to work for Nokia Research, which was still at that time, like, you know, the big mobile phone company in the world.
[440.74 --> 443.10]  And I worked as a scientist there for a few years.
[443.52 --> 448.08]  And then I went to Samsung Research and I led the device intelligence group there.
[448.26 --> 450.80]  And that was, you know, very much similar kinds of work.
[450.80 --> 461.72]  You know, a lot of on-device machine learning, like running algorithms on the phone or on a wearable to infer fitness activities or, you know, learn preferences of the customer to sort of recommend content, that sort of thing.
[461.72 --> 471.34]  And then kind of fast forwarding from there, you know, I've more recently come to Amazon, attracted mostly by what felt like the next big wave in consumer IoT, which is smart home.
[471.60 --> 475.80]  And so, as you said, yes, at Amazon, I've been leading the smart home machine learning team.
[475.80 --> 481.34]  You know, it just is a start because I suspect most listeners kind of think they know what it is.
[481.40 --> 485.86]  But I'm curious if you can tell us what how you and Amazon think of a smart home.
[485.96 --> 492.46]  What is it, you know, just to get us all on the same idea of what that phrase means, because it's been marketed about over the years.
[492.62 --> 494.58]  What is a smart home when you work at Amazon?
[495.06 --> 496.62]  That's a great question.
[496.86 --> 498.92]  I think there's various ways to answer the question.
[498.92 --> 504.92]  I think to do justice to the area, I have to start with saying that smart home, really, it's been around since at least the 80s.
[504.92 --> 505.08]  Yeah.
[505.18 --> 510.40]  Smart home technologies, there's like X10 networking, there's devices that are connected, and you can kind of program your home.
[510.88 --> 512.24]  That stuff's been around for years.
[512.24 --> 515.98]  And there's been a lot of DIY folks that are just really heavy into that.
[516.04 --> 518.60]  And have they been developing the technology for years as well.
[518.72 --> 525.90]  So that's sort of one slice of smart home is that really sort of techie DIY, like wire up your devices to automate your home.
[525.98 --> 527.24]  A lot of that is about home automation.
[527.56 --> 527.80]  Yeah.
[527.80 --> 543.00]  And I think when we think of smart home at Amazon and within Alexa, we're kind of thinking, you know, or of course, we're sort of accepting that history and also sort of looking forward about, well, what can a home, you know, if we're really going to add intelligence to the home, what can it really do for customers?
[543.08 --> 544.26]  And how do we make it really easy?
[544.34 --> 547.38]  So one part, of course, is like, okay, we're going to get Alexa into the picture.
[547.38 --> 549.46]  And so now we have voice control of the home.
[549.62 --> 552.20]  It's kind of like the great enabler, the great simplifier.
[552.68 --> 555.80]  You can just say, you know, Alexa, turn off my light and she'll turn off the lights.
[555.94 --> 558.08]  Very, very simple type of interaction.
[558.46 --> 567.48]  But the other sort of piece of that that we think about a lot is what we call kind of an actually smart home, which is it's not just sort of a fancy remote control for your home.
[567.58 --> 570.60]  It's not just sort of like I push this button and then that automation happens.
[570.60 --> 584.92]  It's having a home, you know, with this intelligent assistant Alexa that can really do things on your behalf, things that are really valuable to you, help you achieve high level goals like living more sustainably or, you know, just being more comfortable or keeping your family safe.
[585.24 --> 588.50]  Could you kind of give some examples of how you might implement some of those ideas?
[588.64 --> 591.72]  And it can be anything you want, but I'm just trying to wrap my head around it.
[591.90 --> 593.12]  Real or a mission, maybe.
[593.76 --> 594.12]  Yeah.
[594.68 --> 596.90]  It doesn't have to be something that you've done yet.
[596.90 --> 598.40]  I'm just curious kind of what's in your head.
[598.40 --> 604.32]  Like, as we record this, we're still in our houses in the late, hopefully, pandemic period and stuff.
[604.52 --> 606.32]  What might I be doing going forward with that?
[606.92 --> 610.66]  Like, what could I do now and what might be something that you're thinking in the near term?
[610.78 --> 612.26]  We'll talk about the distant term later on.
[612.60 --> 612.94]  Yeah, yeah.
[613.00 --> 614.90]  So I think there's kind of three things come to mind.
[614.98 --> 620.06]  There's sort of three forms of sort of control or interaction with a home I think is a useful frame to think about.
[620.06 --> 622.86]  And one is what we call directed control.
[622.86 --> 630.22]  And that's where we're explicitly controlling a device with, you know, literally remote control with an app or with voice commands.
[630.36 --> 633.02]  So that's where I would say, you know, Alexa, turn on the lamp and she turns on the lamp.
[633.06 --> 635.08]  Or you can control groups of devices, all of that.
[635.34 --> 641.74]  So that's kind of one mode of interaction that can sort of simplify the management of the home and kind of an everyday experience.
[641.74 --> 648.10]  And then we have, as I was describing, there's kind of this more classic mode of smart home, which we think of as kind of programmed control.
[648.30 --> 654.24]  And this is where the customer's kind of pre-specifying procedures that they want to happen using a program.
[654.74 --> 659.46]  The customer's thinking about kind of signals, logical conditions, you know, the actions that they want to happen.
[659.88 --> 661.80]  Maybe be like shutting down your house at night.
[661.88 --> 662.92]  I say, Alexa, good night.
[662.96 --> 664.44]  And then all my lights shut down.
[664.54 --> 665.16]  The temperature goes out.
[665.22 --> 666.82]  Like all the things that I want to happen will happen.
[666.82 --> 671.28]  So we've sort of exposed that type of interface as well with our routines products.
[671.48 --> 674.38]  A lot of people really are excited about that product as well.
[674.68 --> 682.00]  And sort of more recently, we're also thinking about, well, okay, so what's sort of the next sort of actually smart experience?
[682.14 --> 685.50]  And we're thinking of this kind of mode where it's more intelligent control.
[685.60 --> 693.36]  And this is where we're trying to further simplify the experience for customers by having Alexa more autonomously manage their home.
[693.36 --> 698.56]  So here, Alexa is going to have what we think of as algorithmically derived intuitions or hunches.
[698.70 --> 699.58]  We'll probably talk about that.
[699.64 --> 701.16]  That's the name of a product, Alexa Hunches.
[701.30 --> 708.18]  And then the customer, they really just have to focus on their own life activities and kind of think about their high-level goals, like living more sustainably.
[708.36 --> 713.88]  So Alexa may have a hunch about, well, you might want to turn down or turn off the light in the basement.
[714.02 --> 715.58]  It looks like it's on anomalously.
[715.82 --> 720.64]  Or, you know, she'll automatically turn it on your thermostat to save energy while you leave home.
[720.64 --> 724.00]  Or you may have the goal to help keep your family safer.
[724.16 --> 728.50]  So Alexa might have a hunch that there's a door downstairs that looks like it's usually locked at this time.
[728.64 --> 730.06]  Maybe you forgot to lock it.
[730.42 --> 731.28]  Do you want to lock the door?
[731.40 --> 732.78]  And then she'll lock the door on your behalf.
[733.06 --> 734.84]  So kind of starting out with simple things.
[734.90 --> 739.36]  But if you look forward, I mean, there's all kinds of things that we can do on behalf of customers in a smart home.
[739.42 --> 746.88]  If you think of, you know, Alexa is really your personal assistant who has this kind of superhuman power of knowing all about things like energy consumption.
[746.88 --> 752.58]  And how to reduce it or, you know, observing at any one time how the status of your locks or your security system.
[752.58 --> 756.82]  And all the other sort of devices and sensors in your home that Alexa can manage.
[757.76 --> 763.86]  One of the things that I've been thinking about more and more, partly based on some of the conversations we've had on the podcast.
[763.86 --> 773.98]  But partly based on some of the work we're doing is human perception around AI technologies, especially when they're introduced in a new sphere.
[773.98 --> 783.38]  So one of the things that I've realized kind of over time is, for example, if you think about the smart home, I think there's a lot of people out there that are used to having a dumb home.
[783.38 --> 800.20]  Right. And so you're introducing like this whole new way of thinking about your home and devices in your home and essentially trying to introduce a new framework for people in terms of how they interact with things that they aren't used to interacting with in that way.
[800.20 --> 830.10]  I'm wondering if you have any sort of perspective or learnings on that front in terms of where are we at on that sort of human interaction spectrum with smart home technology in terms of maybe younger generations, older generations, or maybe geographically where people are sort of catching on to this technology more quickly and where the challenges are in terms of helping people adopt this sort of technology in a place where they're not really used to having a
[830.10 --> 831.10]  smart device.
[831.28 --> 839.10]  That's a great question. There's a lot there. I think there are many challenges given sort of the diversity of customers that are now interested in smart home technologies.
[839.10 --> 845.10]  Right. The long history includes lots of really tech savvy people who are going to make it work for them one way or another.
[845.44 --> 854.94]  Yeah. Yeah. There's kind of a group that's like, I really want a voice assistant and I'm going to, even if it's hard to use at the beginning, I'm going to push through and I'm going to use it.
[854.94 --> 861.40]  Right. Exactly. Yeah. Those are always, you know, the super valuable early adopters that are kind of pioneering these new technologies.
[861.90 --> 865.70]  But of course, right, we've got all kinds of other customers that are sort of less savvy.
[865.78 --> 869.20]  Their interests may not be programming their home and wiring up all these devices.
[869.20 --> 874.26]  And it may be more about just keeping their family safe or like, you know, maybe, you know, I've heard about smart home.
[874.34 --> 879.02]  It's kind of interesting. I'm not too confident about setting it up and using it, but it just seems pretty cool.
[879.02 --> 885.66]  I want to give it a try. And so it's interesting. That's one of our key challenges is trying to help customers through that journey.
[885.78 --> 895.70]  Right. From getting their first light bulb to being the kind of fully enrolled customer that has maybe multiple devices and is taking advantage of some of these kind of higher intelligence features.
[896.08 --> 901.60]  And so we do that is one of the things that my team focuses on is kind of facilitating that journey with customers,
[901.60 --> 911.14]  helping them set up devices intelligently and kind of helping them recover from really common kinds of errors that they run into when they're setting up and starting to learn how smart home works.
[911.14 --> 927.38]  Changelog++ is the best way for you to directly support practical AI.
[927.90 --> 932.14]  Join today and unlock access to a private feed that makes the ads disappear,
[932.58 --> 938.30]  gets you closer to the metal and help sustain our production of practical AI into the future.
[938.30 --> 947.36]  Simply follow the Changelog++ link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[947.66 --> 951.56]  Once again, that's changelog.com slash plus plus.
[953.16 --> 955.30]  Changelog++ is better.
[955.30 --> 973.80]  So I think that was a great segue there in terms of what you were just describing to talk about.
[973.90 --> 984.00]  I'd love to talk about how you're really putting the machine learning kind of at the central enabler of being able to make all this happen for people to where they're able to do that.
[984.00 --> 989.14]  I know you mentioned earlier that there is a service called Hunches that you guys are working on.
[989.58 --> 993.96]  And I would love to understand more about that because I think I've been waiting for something like that for years.
[994.10 --> 998.24]  I'm selfishly thinking about the new house that we're going to build and how that fits in.
[998.30 --> 999.40]  So I can't wait to hear this.
[999.56 --> 999.76]  Yeah.
[1000.16 --> 1006.48]  So yeah, Hunches is a great example of sort of a new paradigm within smart home at least.
[1006.48 --> 1011.50]  And the idea of a hunch is that it's an algorithmically derived intuition that Alexa has.
[1011.62 --> 1018.28]  And so, you know, for those of us who listen to this podcast, you know, we're using a model to make a prediction and there's a confidence score associated with it.
[1018.58 --> 1024.02]  And then there's this sort of designed experience around it that kind of supports that type of prediction.
[1024.20 --> 1026.18]  It's sort of a prediction with a confidence.
[1026.30 --> 1027.76]  We may not be 100% right.
[1027.82 --> 1030.70]  We accept that sometimes Alexa is going to be wrong, but it's a hunch.
[1030.70 --> 1034.20]  You know, like Alexa has an idea of something that might be helpful to you.
[1034.58 --> 1050.10]  And then there's this kind of collaboration with the customer around not just, you know, do we take an action in the case of a certain hunch, but how do we learn more about what the customer's intentions are and what their goals are through this sort of series of hunches each time we request feedback from the customer and we learn more.
[1050.38 --> 1054.14]  There's probably, there's kind of a few distinguishing characteristics to hunches.
[1054.34 --> 1057.22]  One is that, as you can imagine, they're personalized to the customer.
[1057.22 --> 1063.84]  You know, they're always about some particular device in their house and maybe corresponding to some behavioral pattern that Alexa has observed.
[1064.02 --> 1068.50]  They're also dynamically adaptive to the home and to the customer's current context.
[1068.88 --> 1072.74]  So, right, then the example of the basement light is still on and it's like nighttime.
[1072.96 --> 1074.18]  It looks like a time when you might go to bed.
[1074.28 --> 1078.84]  Alexa may sort of reach out and let you know that your light is on and ask if you wanted to turn it off.
[1078.96 --> 1080.66]  Or in some cases, you know, we can talk later.
[1080.76 --> 1084.64]  We also have automatic actions for hunches where Alexa would just automatically turn it off.
[1084.64 --> 1087.84]  But that's after we sort of built a little more confidence with the customer.
[1088.46 --> 1090.90]  They're also, as noted, they're non-deterministic.
[1091.14 --> 1092.90]  So, you know, we're not going to deliver hunch.
[1093.06 --> 1095.48]  We're not going to take an action unless Alexa has high confidence.
[1095.48 --> 1103.40]  So that model has to be pretty confident across all of the signals it observes that this is something the customer would actually value before we actually surface it.
[1103.40 --> 1107.36]  And then finally, as described, it's refined in the loop with feedback from the customer.
[1107.50 --> 1110.96]  So every time we're delivering a hunch, we're inviting the customer to give us feedback.
[1111.34 --> 1115.00]  Often explicitly, you know, Alexa may ask, did you want me to turn off that light?
[1115.08 --> 1116.18]  And they can say yes or no.
[1116.54 --> 1118.28]  Or, you know, they can give feedback through the app.
[1118.44 --> 1119.96]  But sometimes there's implicit feedback.
[1120.18 --> 1125.32]  So if we go and we lower the thermostat, we'll kind of watch to see if they turn it back up later.
[1125.42 --> 1128.82]  And that's another kind of feedback that we can constantly learn from.
[1128.82 --> 1135.82]  It sounds like that feedback, is it the central mechanism for establishing trust with the customer for the new service?
[1135.82 --> 1141.78]  Because we have so many conversations with people who are doing these amazing things with machine learning.
[1141.78 --> 1147.10]  And so much of it now is advanced is requiring people to make that mental shift.
[1147.10 --> 1148.78]  And we've talked a little bit about that already.
[1148.90 --> 1154.78]  But is that establishing trust so that you feel you can incorporate hunches into your life?
[1154.78 --> 1159.78]  Like, what else do you guys think about in terms of how to get there and what the next steps are?
[1159.82 --> 1164.50]  Because obviously, the trust has to be a huge part of the strategy on moving this all forward.
[1165.26 --> 1165.70]  Absolutely.
[1166.00 --> 1169.54]  I mean, feedback is absolutely its core to this idea of hunches.
[1169.72 --> 1171.92]  We think of it as a collaboration with the customer.
[1172.12 --> 1178.68]  We're earning trust continuously as we sort of get feedback from the customer, learn, personalize, adapt to their patterns.
[1178.68 --> 1189.16]  I think a few other things just about the UX or the CX, as we say at Amazon for hunches, is the kinds of hunches we started with a couple of years ago were really sort of these extemporaneous delighters.
[1189.16 --> 1192.14]  Like the case of like reminding you to turn off your light or lock your door.
[1192.34 --> 1193.38]  They don't happen that often.
[1193.46 --> 1194.68]  They're sort of targeting anomalies.
[1194.86 --> 1197.94]  But it's kind of a delightful experience when they happen.
[1198.26 --> 1202.36]  Fortunately, we've been able to kind of tune the models so that we're usually right about those anomalies.
[1202.46 --> 1204.54]  The customer does want to turn off the light or lock the door.
[1204.54 --> 1210.36]  And so like that sort of spark, even though it's like kind of a simple thing, that spark, it really earns a lot of trust.
[1210.62 --> 1216.00]  And then the customer also feels in control because they have that feedback and they can say no if it was not the right thing.
[1216.02 --> 1217.94]  And we're not going to ask them again in that scenario.
[1217.94 --> 1221.42]  That definitely kind of helps us build that trust as we go forward.
[1221.60 --> 1230.20]  And then absolutely, like, I mean, the way we've sort of continued to work on the hunches product is to incorporate gradually more and more use cases.
[1230.20 --> 1247.02]  And then most recently, just this last year, we launched the hunches automatic actions where we're working with the customer in advance to sort of help them understand that Alexa is now going to be able to take action and adjust your thermostat or turn off your lights based on her inferences about what's going on in the home.
[1247.16 --> 1249.46]  And you can sort of consent to that in advance.
[1249.60 --> 1252.74]  And then Alexa will turn off your lights if she thinks you're asleep.
[1253.16 --> 1258.22]  So that kind of gets that sort of other element of that earning trust, which is explanations for the inferences.
[1258.22 --> 1268.44]  So if we have a hunch that we should turn off that light, that'll show up in what we call the hunches dashboard within the app that shows these are the actions that Alexa took last night or the last 30 days.
[1268.58 --> 1271.62]  And you can see, you know, a very simple explanation for each one.
[1272.06 --> 1277.40]  Alexa turned off your light because she thought you were asleep or she turned on the thermostat because she thought everyone in your house was away.
[1277.62 --> 1279.68]  And then you can give feedback right in there.
[1279.76 --> 1281.98]  But you're understanding more about how Alexa is working.
[1282.62 --> 1285.70]  Yeah, I'm curious just on the practical side of things.
[1285.70 --> 1290.46]  I'm assuming as more and more smart devices are integrated in people's homes.
[1290.46 --> 1293.86]  I'm thinking about the data side of developing something like hunches.
[1293.86 --> 1301.86]  It seems to me like there's all these different customers that could have all sorts of different unique combinations of devices in their home.
[1302.40 --> 1307.14]  And so like the data is not the same for customer A versus customer B.
[1307.50 --> 1310.00]  And maybe the history of that data is not the same.
[1310.12 --> 1314.20]  And there's also like geographic factors or lifestyle factors.
[1314.20 --> 1330.32]  So how do you even, from your team's perspective, do you have any good maybe workflow hints or tips for people that are dealing with this sort of complex data situation and really exploring that data and getting down to the, because you have to start somewhere.
[1330.44 --> 1334.20]  Like you were saying, you're building in incrementally more and more of these.
[1334.20 --> 1344.76]  Any tips for people out there that are maybe dealing with this sort of complicated data situation and trying to get down to where should I start in terms of creating value?
[1344.88 --> 1349.12]  Because there's so many different varied ways that I could go about this.
[1349.52 --> 1349.88]  Absolutely.
[1350.08 --> 1351.62]  Well, it's very, very insightful.
[1351.78 --> 1355.84]  I mean, that touches on kind of a really key challenge for smart home.
[1355.84 --> 1361.90]  Just one part of that is the challenge of providing that sort of consistently high quality inference across customers.
[1362.08 --> 1365.84]  They have so many different types of homes, so many different types of devices.
[1365.84 --> 1366.90]  They use them differently.
[1367.00 --> 1367.98]  They live in different places.
[1368.12 --> 1369.42]  I mean, it's a super hard problem.
[1370.02 --> 1372.64]  And there's a few sort of maybe I think sort of three things.
[1372.72 --> 1376.16]  I mean, one, personalization is always useful in the early phase.
[1376.28 --> 1383.84]  We may not know instantly about your house or we may not know about everyone's house, but we can learn how you use your bedroom reading lamp.
[1383.84 --> 1389.14]  That's one thing that we can sort of learn over time, some basic things about that just on your data alone.
[1389.40 --> 1402.10]  And then, yeah, secondly is if you are able to, if you're empowered to kind of design a feature, including the kind of user facing interaction, then it really helps to build that feedback loop right into it.
[1402.16 --> 1402.32]  Right.
[1402.36 --> 1405.30]  Just like hunches, we propose a hunch and then we get feedback on it.
[1405.34 --> 1410.78]  And that's great for gathering training data from the only people who can really label it about the context of their home.
[1410.78 --> 1415.26]  The end customer is really the main person who can provide you that most accurate label about what they want to do.
[1415.42 --> 1432.20]  But the sort of the third area of work, I think this is really where I see kind of one of the key scientific challenges for smart home is trying to infer information about the home, like trying to infer activities in the home across such sort of varying data sets from individual customers.
[1432.20 --> 1434.80]  And it's actually pretty sparse data from an individual home.
[1434.92 --> 1437.26]  You know, someone we're just looking at the lighting data.
[1437.36 --> 1441.70]  People just turn on and off lights four times a day, five times a day.
[1441.82 --> 1444.82]  You know, you got to you got to wait a while to get data on any given house.
[1444.82 --> 1459.48]  So you've got to find ways to sort of learn across customers, not just, you know, you probably start with personalized models, but there's a lot of investment we've made in sort of deep models that are trained across millions of different customers.
[1459.48 --> 1472.54]  And there's even, you know, I could talk more about it, but there's even some, I think, fundamentally new scientific discoveries about what's possible there, like how much similarity there is between customer behavior in one home and 100 or 1000 other customers.
[1472.54 --> 1486.42]  Yeah. And is that like, because I know a lot of the devices these days, like people might have a mix of smart home devices in their home that are from different brands, even and report sort of different sets of data.
[1486.50 --> 1487.00]  Is that correct?
[1487.56 --> 1487.96]  That's right.
[1488.36 --> 1498.44]  Yeah. So like things are coming in with different, I guess, different feature sets, different things that are represented by different brands and maybe even different formats.
[1498.44 --> 1516.90]  And maybe there's some standards around that now is some of that, even just like synthesizing some of that data together and figuring out how data from different brands of different devices reporting different data is sort of matching up to, hey, this is lighting information over here.
[1516.90 --> 1518.60]  And this is lighting information over here.
[1518.60 --> 1526.24]  And it's reported slightly differently, but we can, you know, how, how much work is there in sort of synthesizing that across all the varied devices these days?
[1526.24 --> 1528.28]  Or is it more standardized than I think?
[1528.60 --> 1529.84]  Yeah, it's, that's a good question.
[1529.84 --> 1536.16]  So it is a little bit standardized, you know, we have an API that partners use to report any kind of data like that.
[1536.46 --> 1537.38]  That's certainly helpful.
[1537.38 --> 1545.42]  Of course, the reality is like, you know, across many different kinds of companies, partners, devices, the quality of the data varies, and certainly the content of the data varies.
[1545.42 --> 1551.22]  There's more than I think there's more than 140,000 different types of devices that connect with Alexa today.
[1551.22 --> 1554.20]  And so that's a lot to keep track of.
[1554.30 --> 1555.06]  No big problem.
[1555.38 --> 1556.04]  No big problem.
[1556.16 --> 1556.26]  Yeah.
[1556.96 --> 1558.76]  There's a lot of different data there.
[1558.96 --> 1560.60]  And so it is true.
[1560.68 --> 1563.08]  There's a lot of variation across partners.
[1563.08 --> 1565.42]  There's a lot of variation across device types.
[1565.96 --> 1574.84]  And there's not really any one universal solution to just immediately cleaning up all data of every type, unifying it all into one big model.
[1574.84 --> 1576.72]  But there's sort of categories of data.
[1576.92 --> 1578.74]  A lot of it's time series data, of course.
[1578.74 --> 1583.38]  And so you see these kind of point events of like light turned on or changed brightness.
[1583.38 --> 1585.52]  That's the same for all different kinds of lighting.
[1585.74 --> 1588.82]  So you can kind of develop sort of a model or understanding of lighting.
[1589.12 --> 1592.58]  Thermostats are a different picture of security systems are different smart plugs.
[1592.76 --> 1597.14]  They're kind of similar to lighting, but that, you know, they also have different types of usage patterns.
[1597.14 --> 1598.72]  You might want to model them a little bit differently.
[1598.72 --> 1603.72]  So you tend to start looking at devices and categories and standard practice.
[1603.90 --> 1609.98]  You might want to build a layer kind of above that raw data to just kind of be of lighting devices.
[1609.98 --> 1621.12]  For example, you may want to build a layer that tries to sort of smooth out any kind of noise in the data and offer you, for example, like the state of the device with a confidence score rather than just the raw information.
[1621.12 --> 1633.80]  Okay. Yeah. So you're kind of you're building that sort of middleware layer that does some sort of synthesis or correlation of that data together, smoothing and that sort of thing with confidence scores.
[1633.80 --> 1644.06]  And then I would guess that like something like hunches would then rely on the fact that, hey, I know about lighting data and the trends of lighting data generally.
[1644.36 --> 1647.26]  So I'm guessing that that would help with something like that.
[1647.32 --> 1647.78]  Is that right?
[1647.78 --> 1664.22]  Yeah, definitely. And, you know, we do for the kinds of models we use in hunches and most of our products, we do try to incorporate as much information as we can, not just from this sort of time series type of data, but even just kind of the metadata about devices.
[1664.22 --> 1667.78]  So if we're again, if we're talking about lighting, customers are able to name their lights.
[1667.94 --> 1670.64]  Sometimes they just leave it with a default name, like first light, second light.
[1670.64 --> 1675.80]  But often they name them, you know, living room lamp or reading lamp or basement lights, you know, what have you.
[1675.80 --> 1679.38]  And even just in the name of the device, there's a lot of information.
[1679.76 --> 1682.06]  We know that something is a bedroom lamp.
[1682.10 --> 1687.44]  It's probably going to be on in the evening for an hour or two, and then it's going to be off overnight versus a front porch light.
[1687.52 --> 1690.20]  Often they're on all the way overnight and they're off during the day.
[1690.34 --> 1693.56]  There's a lot that we can kind of pull in to kind of add to the model.
[1693.56 --> 1708.16]  And then by extension, of course, if you think about sort of training models across millions of customers and millions of different devices, you can start building kind of like device embeddings that kind of distill all of that information about not just, you know, is it a bedroom lamp?
[1708.20 --> 1710.10]  It's sort of like what kind of bedroom lamp is it?
[1710.22 --> 1716.30]  You know, there's a lot that you can kind of pull together between the behavioral patterns and then the names, the devices, the way customers interact with them.
[1716.30 --> 1724.12]  So you were saying something a few minutes ago that my brain has been spinning on a little bit, and I want to go back and do a kind of a late follow-up on it.
[1724.44 --> 1733.18]  When we were talking about, you know, models that could generalize across thousands and millions of people in terms of these activities, you know, the turning the lamp on and stuff like that.
[1733.18 --> 1749.66]  As we go forward in time and you're moving ever more, presumably, into kind of personalization and really not just supporting all of our lives or lifestyles, maybe the right word for it, but starting to hone in on, you know, what does Chris need?
[1749.76 --> 1752.98]  You know, what does Daniel need in our own differences and stuff?
[1753.24 --> 1760.76]  How do you approach that from the sense of you have these tools that you've built that can handle these activities or tasks in a large sense?
[1760.76 --> 1767.42]  But over time, I might be going through the house and turning on lights in a different way Daniel does because of some quirk of my own personality.
[1767.42 --> 1774.70]  And you're having to tie my activities into those otherwise kind of mainstay thing, you know, light on, light off.
[1774.78 --> 1775.50]  You're recording that.
[1775.60 --> 1776.82]  You know that that's happening.
[1777.08 --> 1786.42]  How do you think about personalization as you're moving into that world where it's not just about turning the light on, it's about why Chris would do it versus when Daniel does it versus other people?
[1786.70 --> 1789.68]  How do you think about a future where that's going and approach it?
[1789.68 --> 1792.70]  Right. Yeah, I think that's really interesting.
[1792.80 --> 1798.94]  I think part of that, if I'm understanding you correctly, part of that is kind of understanding and perhaps modeling the customer's intention.
[1799.44 --> 1799.68]  Yes.
[1799.76 --> 1801.30]  What's actually going on here?
[1801.42 --> 1804.36]  Not just, you know, I think that specific light is going to turn on.
[1804.76 --> 1807.12]  You said it much better than I did, actually.
[1807.34 --> 1812.16]  Yeah, I know in like in a chat dialogue sense, there's like the idea of user intents.
[1812.16 --> 1817.90]  I don't know if there's the idea of like user intents when you're looking at smart home data.
[1818.56 --> 1826.76]  Like, hey, they're doing this on, you know, they're doing this on a Saturday versus they're in there doing this on a work day or something.
[1826.76 --> 1828.28]  Hmm. Yes. Yeah.
[1828.40 --> 1829.74]  So the short answer is yes.
[1829.74 --> 1835.74]  At many levels, we have that concept and then we approach modeling of customer intents in different ways.
[1835.84 --> 1843.28]  So one thing to note, of course, even just in the most simple kind of directed control scenario, we have a concept of what was the customer actually trying to do?
[1843.36 --> 1844.14]  What's their intention?
[1844.14 --> 1851.94]  You know, we can sometimes see that they're trying to turn on a light and perhaps they didn't get the name of the light correct and it failed.
[1852.02 --> 1854.90]  But we can still tell that their intent is to turn on that particular light.
[1855.02 --> 1857.40]  Right. So there's there's just very simple kind of intentions.
[1857.84 --> 1864.96]  But to get into kind of like activities on a on a weekday or Saturday and, you know, what would they want to happen at this particular time?
[1865.24 --> 1866.80]  That's where it starts getting really interesting.
[1866.80 --> 1872.86]  And I feel like that problem, I think of it as modeling the context of the home and the customer.
[1872.86 --> 1877.86]  That's where the sort of ideas like the activity of the home, the activities that the customer is engaged in.
[1878.22 --> 1885.12]  Those are sort of a key part of that picture, like understanding that they're having dinner now or that they're all asleep or that they're away from home.
[1885.20 --> 1888.72]  Whatever the relevant activities are is a big piece of that.
[1889.10 --> 1901.30]  The other way I think of that and the other thing that's important and we're just sort of getting to in the scientific sort of agenda for our team is really understanding how to help customers achieve their long term goals.
[1901.30 --> 1918.24]  So not just, you know, turning on a light or not even just controlling their thermostat in a way over the day that makes them comfortable, but helping them actually save money on their energy bill next month or, you know, helping them stay safe throughout the year with their various security devices and security system.
[1918.24 --> 1920.76]  And kind of balancing those goals with each other, right?
[1920.78 --> 1926.28]  Like if you want to save money, you're going to be biasing towards turning lights off quite often, turning the temperature down.
[1926.34 --> 1931.72]  But if you want someone to be really comfortable, you might bias towards having the temperature up a little more often.
[1931.72 --> 1938.74]  Or if you want them to be really safe at home, you might also, in some cases, you might bias towards having lights on just in case someone's there.
[1938.86 --> 1941.00]  You want them to be able to see where they're going.
[1941.14 --> 1948.38]  So it's a really interesting problem of balancing these kind of long term driving goals with sort of short term actions.
[1948.92 --> 1955.82]  So I know, and as we're talking about this, I know there's going to be at least a few folks out there thinking about what about the security as you're doing this?
[1955.82 --> 1961.66]  Because I'm all excited about getting my home, you know, able to basically predict me ahead of time and do that.
[1961.74 --> 1962.42]  That's very exciting.
[1962.72 --> 1968.96]  There's going to be someone out there worrying about what happens when everything is voice controlled and you have someone who shouldn't be there and do that.
[1969.02 --> 1970.90]  How do you think about it?
[1970.94 --> 1977.72]  And I really mean security, not in the, in just basic security, but like my voice versus a stranger's voice.
[1977.72 --> 1986.32]  And, you know, whether there is any kind of recognition built into services or will be in the future as that becomes more of a real life kind of consideration.
[1986.54 --> 1993.32]  How are you thinking about that level of personalization going forward where some people should and some people shouldn't?
[1993.52 --> 1995.94]  And what's kind of the thinking around that at this point?
[1996.76 --> 1998.18]  Great, great question.
[1998.30 --> 2003.14]  I mean, it's always a lively area of work, the kind of the security and authentication question.
[2003.48 --> 2004.64]  Hard problems there.
[2004.64 --> 2010.60]  The one caveat is that my team doesn't own that space within Alexa, but I can at least comment that.
[2011.06 --> 2013.72]  So regarding the sort of security use cases, right?
[2013.80 --> 2017.74]  There's, as you may imagine, there's certain use cases we just don't support.
[2018.06 --> 2022.26]  Like you wouldn't want to allow anyone to yell from outside, you know, Alexa, unlock the door.
[2022.70 --> 2022.94]  Yeah.
[2023.02 --> 2024.42]  And then we unlock the door.
[2024.60 --> 2030.56]  There's sort of layers of security, you know, whether it's sort of voice codes or there's speaker recognition, right?
[2030.56 --> 2035.66]  That's another feature that folks have implemented for use in all kinds of cases within Alexa.
[2036.40 --> 2041.50]  And then another aspect of this really interesting is just sort of personalization in general.
[2041.76 --> 2047.26]  And how do we accommodate or deny people who are kind of not part of my smart home?
[2047.42 --> 2053.80]  You know, like if someone is a guest and comes to my home, are we going to allow them to control the lights and the music and all of this?
[2053.80 --> 2056.98]  For the most part, I can say that's a very interesting problem.
[2057.16 --> 2062.60]  And there's a lot of, you know, it's really a lot of product thinking in addition to thinking about, you know, authentication and privacy.
[2062.76 --> 2065.04]  Like what kind of experience do we want to create?
[2065.38 --> 2067.68]  You just threw one out that I had not considered at all.
[2067.80 --> 2072.92]  And that would be very different with different customers of yours, I would imagine.
[2072.92 --> 2077.88]  You know, you have guests over and you said control the lights, control the music.
[2078.24 --> 2079.58]  There would be some people, you know, it's a party.
[2079.74 --> 2080.02]  Yes.
[2080.28 --> 2085.94]  And other people, it's an interesting problem because there's a lot of nuance there, I think, to tackle.
[2086.70 --> 2089.58]  Also, no one wants me choosing the music at their party.
[2092.78 --> 2093.76]  Note to self.
[2094.06 --> 2094.14]  Okay.
[2094.20 --> 2094.82]  Note to self.
[2094.82 --> 2104.58]  So, Chris, you remember we had the guest on Nung Ho from Intuit, who is director of data science at Intuit.
[2104.68 --> 2109.04]  And she was talking about like pandemic times and like time series modeling.
[2109.68 --> 2117.80]  And of course, like time series modeling depends on your, you know, how good is the history of your data?
[2117.80 --> 2123.72]  And, you know, this last year has just totally blown all that apart for many people.
[2123.72 --> 2129.30]  So, Evan, I'm kind of curious for the smart home team, machine learning team at Amazon.
[2129.82 --> 2149.50]  What has that sort of like disruption in the history of data meant for your team in terms of maybe new opportunities, the rows of things you didn't realize before, but also in terms of like thinking about, hey, maybe we need to do things slightly different to sort of pandemic proof.
[2149.50 --> 2150.56]  Some of our processes.
[2150.92 --> 2155.26]  Curious about that aspect of your team's conversations over the past year.
[2155.90 --> 2158.02]  Yeah, it had a huge impact.
[2158.24 --> 2163.44]  It's kind of changed everything in the data that we see because, you know, all of our data is from the home.
[2164.06 --> 2170.18]  And one of the implications of a global pandemic is that people are staying home a lot more often than they were.
[2170.18 --> 2176.84]  Especially we've got at least this big chunk of the early adopter folks who are often tech workers who are probably going to work remote anyway.
[2177.46 --> 2189.32]  So one of the things we've seen, for example, as of maybe March or April last year is that suddenly weekdays started to look a lot more like weekends.
[2189.78 --> 2191.68]  You know, people are waking up a little bit later.
[2191.88 --> 2194.54]  There's more activity in the home throughout the day.
[2194.86 --> 2198.42]  People stay up a little bit later now on weekdays as well.
[2198.42 --> 2206.14]  And to that end, we've had all these models trained on customer behavior patterns across, you know, days and weeks and so on.
[2206.44 --> 2217.42]  And we had to sort of switch all those up because what looked typical back in February 2020 is very different from what looks typical in February 2021.
[2218.00 --> 2220.36]  I guess a couple other notes.
[2220.36 --> 2225.66]  One of the things that we've had to do is rely a little bit more on, I guess, again, personalization.
[2225.84 --> 2230.64]  We've got to lean into like, what do we think this particular customer is going to do rather than like any customer?
[2230.82 --> 2235.70]  Because people, you know, at least within the U.S. states are like opening up and locking down at different times.
[2235.92 --> 2242.76]  And, you know, we can't rely on people in Texas, you know, kind of predict what's going to happen in, you know, Montana.
[2242.76 --> 2244.46]  You know, it's just different places.
[2245.04 --> 2249.54]  So we've kind of leaned in a lot more on personalization to an individual customer.
[2249.88 --> 2256.28]  And then we've just sort of reset some of the assumptions the models made about the kind of like things like trips away from home, for example.
[2256.46 --> 2260.72]  You know, there used to be, of course, this very established pattern of sort of nine to five work.
[2261.32 --> 2263.06]  Commuting and be away from home and come back.
[2263.06 --> 2265.92]  And that doesn't really exist anymore.
[2266.04 --> 2273.00]  And a lot of time now, these sort of trips away from home are kind of short, short trips, like running out to get groceries and coming back, something like that.
[2273.38 --> 2274.54]  Yeah, it's true.
[2274.76 --> 2277.52]  It's kind of funny just to your point right there.
[2277.84 --> 2278.86]  And Daniel knows this.
[2278.90 --> 2280.28]  And you may have heard this on a previous thing.
[2280.34 --> 2281.40]  I'm taking flying lessons.
[2281.62 --> 2284.56]  And I told my wife the other day, you know, because I was commuting.
[2284.56 --> 2286.36]  I was going off on business trips.
[2286.36 --> 2290.74]  And I was off and away from home through the whole day and maybe for multiple days.
[2290.74 --> 2305.28]  And my life has flipped so much that with my flying lessons and these short trips out, I realized that I'm flying as an amateur private pilot student more than I'm driving my car at this point, which was kind of a bizarre realization to do that.
[2305.68 --> 2308.54]  But that raises another point that I wanted to ask about.
[2308.54 --> 2316.30]  And that is, as you're addressing smart home and you're pulling the data from the home, we're also seeing smart technology being implemented out of the home.
[2316.30 --> 2324.80]  And, you know, we're getting, you know, automotive smart capabilities and various other things in our lives that are outside our houses.
[2325.08 --> 2328.28]  Any thought into how those integrate over time?
[2328.28 --> 2334.20]  And I realize that we're still, you know, you're working your way there and there's a lot of stuff that has to go forward.
[2334.32 --> 2343.46]  But at some point, we're going to be moving around in smart vehicles, maybe fully autonomous vehicles, you know, not terribly far into the future at this point.
[2343.46 --> 2350.22]  We already have some out there. We're coming home to our smart homes and so much of our lives are being automated.
[2350.22 --> 2353.24]  And yet they're all somewhat disparate right now.
[2353.60 --> 2362.04]  How do you envision that coming together for more of an integrated feel, recognizing that it may not always be just Amazon?
[2362.16 --> 2364.74]  Amazon does a lot and you guys may be in a lot of those fields.
[2364.74 --> 2370.46]  But if you're looking even beyond that, you have a lot of different players doing different parts of life, if you will.
[2370.86 --> 2377.36]  And how does the world come together in an integrated experience that is what that consumer wants it to be?
[2377.82 --> 2379.74]  Yeah, that's a great, great question.
[2379.98 --> 2381.46]  Great observation as well.
[2381.52 --> 2385.34]  I mean, it's, I mean, you already see some of that, you know, there's Alexa for auto.
[2385.68 --> 2386.50]  Yeah, of course.
[2386.50 --> 2397.06]  And I'll tell you the way I see it and also that I think sort of aligned with Amazon's vision is that it's all kind of part of the same problem if you're focused on the customer.
[2397.22 --> 2403.20]  Really, we're just trying to help the customer live more simply, you know, achieve their goals.
[2403.20 --> 2406.48]  And, you know, a lot of that we can do with just the smart home data.
[2406.60 --> 2419.44]  But if you pull in data and sort of inferences we can make about what they do in the car, what they do out in the world, you know, maybe with it using their smartphone, there's just a lot more you can understand about their intentions and what they want to happen.
[2419.82 --> 2423.74]  It's sort of obvious for us, you know, Alexa is kind of the unifying element here.
[2423.84 --> 2431.52]  We have this ambient assistant who is able to sort of stay with you, whether you're at home, whether you're on the go, you know, with your smartphone.
[2431.52 --> 2437.06]  She's kind of present there across these elements of your life and can kind of help tie things together.
[2437.18 --> 2443.70]  I think that's sort of the metaphor we're using to sort of unify the data as well as the experience for the customer.
[2443.82 --> 2445.56]  I think the opportunities are huge.
[2445.72 --> 2449.84]  I mean, as I noted, I spent years working on smartphones and mobile inference.
[2450.04 --> 2453.14]  I know there's a lot there to add to the big picture.
[2453.88 --> 2454.66]  That's super exciting.
[2454.66 --> 2464.44]  I think that's that's a really good way to sort of tie things up here at the end is thinking about that ambient smart technology sort of permeating your life.
[2464.56 --> 2465.82]  I know it's it's really exciting.
[2465.92 --> 2466.74]  There's a lot of challenges.
[2466.74 --> 2468.34]  There's a lot of questions ahead of that.
[2468.38 --> 2470.00]  But I'm really excited about it.
[2470.00 --> 2474.42]  I'm excited to see what Chris puts in his home and we can we can hear about that.
[2474.56 --> 2475.24]  I am too.
[2475.58 --> 2479.08]  But yeah, appreciate you joining us so much, Evan.
[2479.08 --> 2488.56]  And this is a really great conversation and I'm excited to try out some of some of these hunches and other things and see how they develop over time.
[2488.66 --> 2490.68]  Really appreciate the work that your team is doing.
[2490.86 --> 2493.62]  So thank you so much for taking time to join us.
[2493.70 --> 2494.50]  Really appreciate it.
[2494.96 --> 2495.22]  Excellent.
[2495.36 --> 2495.54]  Yeah.
[2495.64 --> 2496.38]  Thank you so much.
[2496.90 --> 2498.72]  I'll look forward to listening to the podcast.
[2502.40 --> 2504.48]  Thank you for listening to Practical AI.
[2504.80 --> 2506.80]  We appreciate your time and your attention.
[2506.80 --> 2510.88]  If you enjoyed this episode, help us out by spreading the word.
[2511.44 --> 2512.22]  Think of a friend.
[2512.40 --> 2513.08]  Think of a colleague.
[2513.36 --> 2516.18]  Somebody who would benefit from listening to it and send them a link.
[2516.52 --> 2517.54]  We'd really appreciate it.
[2517.82 --> 2521.24]  Practical AI is hosted by Chris Benson and Daniel Whitenack.
[2521.46 --> 2525.00]  It's produced by Jared Santo with music by Breakmaster Cylinder.
[2525.40 --> 2528.58]  Thanks again to our sponsors Fastly, Linode and LaunchDarkly.
[2528.76 --> 2529.54]  That's our show.
[2530.00 --> 2532.68]  We hope you enjoyed it and we'll talk to you again next week.
[2536.80 --> 2566.78]  We'll see you again next week.
