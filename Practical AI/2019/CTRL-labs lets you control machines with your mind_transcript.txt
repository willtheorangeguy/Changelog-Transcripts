[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.04]  And unlike standard droplets, which use shared virtual CPU threads,
[29.04 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.42 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.22 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[106.82 --> 108.90]  Welcome to Practical AI.
[109.40 --> 111.26]  This is Daniel Whitenack.
[111.38 --> 113.94]  I'm a data scientist with SIL International.
[114.38 --> 120.16]  And I've got Chris, my co-host on the line, who's chief AI strategist at Lockheed Martin.
[120.28 --> 120.96]  How are you doing, Chris?
[121.14 --> 121.68]  Doing great.
[121.74 --> 122.34]  How's it going, Daniel?
[122.72 --> 123.88]  It's going well.
[123.88 --> 126.58]  You just came back from O'Reilly AI, right?
[126.90 --> 127.06]  Yep.
[127.14 --> 130.44]  I spent last week in New York City at the O'Reilly AI conference.
[130.64 --> 132.52]  Had a lot of fantastic conversations.
[132.96 --> 134.00]  Did a little bit of recording.
[134.46 --> 136.78]  And so maybe some of that's to come down the road.
[137.36 --> 137.70]  Awesome.
[137.82 --> 140.72]  I can't wait to hear that.
[140.84 --> 141.94]  Any highlights?
[141.94 --> 143.90]  I really was talking.
[144.06 --> 146.06]  I talked to quite a few people about TensorFlow 2.
[146.82 --> 152.46]  Everyone seems to love going from 1 to 2 and truly adopting Keras as the blessed way.
[153.14 --> 158.78]  And so I'm probably biased because I've been pushing into TensorFlow 2 myself, trying it out a bit.
[159.08 --> 161.82]  So yeah, I had a lot of great conversations.
[161.96 --> 162.92]  Met a lot of great people there.
[163.48 --> 163.86]  Awesome.
[164.12 --> 166.28]  I can't wait to hear more about it.
[166.28 --> 177.96]  Well, today on the show, I think it's going to be a lot of fun because we're going to talk about something that might seem a little bit sci-fi-like to certain people.
[178.10 --> 184.62]  But I think we're going to try to bring it down and make it practical because after all, this is practical AI.
[185.22 --> 191.12]  I'm really excited because we've got Adam Behrenzweig from Control Labs with us.
[191.22 --> 191.68]  Welcome, Adam.
[192.14 --> 192.54]  Thanks.
[192.66 --> 193.56]  I'm excited to be here.
[193.56 --> 207.76]  Yeah, Adam's going to help us dig into a little bit of what Control Labs is doing specifically around neural interfaces or processing our brain signals to control machines.
[208.12 --> 209.64]  So I'm pretty excited about this.
[209.90 --> 217.32]  Adam, do you want to start by just giving us a little bit of your background and how you got into AI and ended up at Control Labs?
[217.70 --> 218.50]  Yeah, absolutely.
[219.14 --> 222.12]  So academically, I studied speech recognition.
[222.12 --> 234.36]  I have a PhD in speech and signal processing, which is kind of, if you think about it, it's the branch of machine learning that's closest to kind of a human computer interface application area.
[234.58 --> 241.74]  In general, if you think about machine learning as, you know, one big aspect of machine learning anyway is artificial perception, sight and sound and hearing.
[242.18 --> 247.90]  You know, a big part of the world that we as humans need to perceive is communication from other humans.
[247.90 --> 257.08]  And so speech recognition is, I guess, the branch of machine learning that's always been focused on understanding the output of human brains in the form of speech.
[257.56 --> 262.40]  So maybe that's going to set some of the context for what we'll talk about later with what we're doing at Control Labs.
[262.40 --> 271.28]  So after my PhD, I actually sort of, in the middle of my PhD, I went to Google as an intern and decided it was too amazing.
[271.50 --> 272.38]  And I stayed.
[272.72 --> 282.76]  I did go back and finish my degree later, which was, I consider one of the most heroic things I've ever done is to actually leave Google for a bit and go back and finish it.
[282.76 --> 291.76]  And so at Google, I was there for 10 years and I worked in general, I'd say my beat was kind of building products around machine learning.
[291.76 --> 303.96]  So I was no longer really doing hardcore kind of deep research, but taking what was coming out of the lab, taking stuff that was being worked on in academia and of course within Google and thinking about how to apply that to products.
[303.96 --> 305.56]  And that was across a number of domains.
[305.72 --> 308.98]  I worked on text with Google News and the recommendation algorithm there.
[309.18 --> 310.54]  I worked on Google Music.
[310.78 --> 320.76]  My PhD was actually, you know, I was talking about speech before, but I was particularly interested at the time was music and non-speech audio and understanding just the world of sound around us.
[321.18 --> 323.62]  Computational auditory signal processing, sometimes it's called.
[324.18 --> 328.14]  And this was kind of post-Napster, it was late 90s.
[328.14 --> 344.26]  And so I was also a little bit kind of, you know, idealistically, politically motivated to come up with technological solutions that would allow musicians to connect directly to their fans without these intermediary giant corporations controlling all the intellectual property in the middle.
[344.64 --> 349.54]  So, you know, I thought as many people did at the time that recommendation algorithms are going to be this great equalizer.
[350.22 --> 355.58]  You know, we'd already had a great way to distribute music and we had a great way to produce music cheaply.
[355.58 --> 362.10]  You know, people can make little recording studios at home, but in order for people to find music, we had to, you know, solve that problem.
[362.20 --> 365.72]  So I was interested in doing recommendation, but from the audio signal.
[365.78 --> 372.50]  So actually analyzing the content of music from the audio and then using that to understand it and make recommendations to people.
[372.64 --> 378.20]  So then that turned into Google Music and I helped the music recommender for Google Play.
[378.20 --> 385.76]  And then eventually I started to work on images and I worked on goggles, which was one of the early image recognition mobile phone apps.
[385.84 --> 389.12]  You could point your camera at something in the world and we would tell you what it was.
[389.38 --> 392.50]  This was all pre-deep learning, actually, while I was working on that project.
[392.84 --> 402.08]  And so the project at the time I joined was the app had already been launched and it was kind of an amazingly cool toy, but it wasn't quite yet like a really useful tool for people.
[402.08 --> 408.48]  So the obvious thing to do next was to put this into, you know, to run this technology, run recognition on people's photos.
[408.76 --> 410.84]  At the time, Google didn't have a photos project.
[411.10 --> 416.56]  It had, there was the Android camera, there was photo, visual search on the web, you could upload photos.
[417.00 --> 419.08]  There was Picasa, a desktop app.
[419.34 --> 426.84]  So at the time, the photos project at Google was kind of in its nascent form, but that was clearly where the technology wanted to have its home.
[427.22 --> 428.92]  So I worked on images for a while with that.
[428.92 --> 435.24]  Then I left and I helped start a company called Clarify, which was an early deep learning image recognition company.
[435.70 --> 441.94]  So yeah, in between the time when I joined Goggles and when I left Google, the deep learning, this was about 2012, 2013.
[442.56 --> 447.72]  So working on Goggles, I saw some of the early, you know, large confinets that were coming out of research.
[447.72 --> 454.44]  And there was an intern at Google, Wojciech, who, you know, basically was the first, you know, deep content I'd ever seen.
[454.50 --> 458.68]  And it was doing things that, you know, we'd never seen possible from an image recognizer.
[459.08 --> 462.80]  Before that, it was really clear that, oh my God, this is really going to change everything.
[462.80 --> 465.68]  And it was a technology that was ready for prime time.
[465.68 --> 476.44]  Yeah, so for some of us, I mean, for me, I guess, in particular, I feel like a lot of what I've been exposed to is kind of like post the deep learning revolution.
[476.78 --> 488.78]  So for someone that was involved in machine learning for quite a while before that, for how did you perceive all of these things coming in around deep learning and the acceleration that happened?
[488.78 --> 498.60]  Oh, it was magic. It was incredible. I mean, you know, the field had been making advances, sort of incremental advances for 15 years at that point.
[499.50 --> 503.80]  And, you know, SVMs were kind of still the hot things, statistical machine learning.
[504.10 --> 513.66]  And we were, you know, we could do, you know, a lot of the technologies were okay and pretty good for, you know, a narrow range of things and a narrow range of classes.
[513.66 --> 516.36]  You could get a binary classifier that would work fairly well.
[516.36 --> 527.70]  But the whole idea of having a single network that could recognize a thousand things at once or, you know, eventually 10,000 and upward was enormously, it just, you know, changed a lot.
[528.48 --> 535.96]  And, you know, similarly on the speech side, the results that were coming from the early deep learning based speech recognizers were just blowing everything away.
[536.02 --> 537.50]  It was pretty wild.
[537.50 --> 544.24]  So at what point did you, I know that you were saying that you'd kind of gotten to clarify around 2012, 2013.
[545.18 --> 549.34]  Was there anything else you did prior to jumping into Control Labs?
[549.72 --> 550.10]  Yeah.
[550.10 --> 556.28]  So I worked for a year on an idea for a startup, which I still hope somebody will go and do.
[556.52 --> 567.00]  It was actually quite different than what I'm doing now, but I was just thinking about the problem of teams collaborating together and how machine learning can wrangle all of the data that sits sort of between people on a team.
[567.00 --> 574.76]  And, you know, probably you have this problem with data scattered across, you know, Google Docs and Slack and, you know, Trello and who knows other places.
[574.76 --> 577.66]  And, you know, where is all the stuff and who knows where things are.
[577.86 --> 578.94]  You know me so well.
[579.92 --> 580.28]  Yeah.
[580.82 --> 581.92]  So I worked on that for a bit.
[581.96 --> 590.08]  We had some good ideas, but eventually I got sucked into Control Labs because the, so Reardon and crew reached out to me at some point while I was doing that.
[590.16 --> 592.74]  And it was really just up my alley.
[592.74 --> 596.48]  It touched on some ideas that I'd been thinking about for 20 years at that point.
[596.82 --> 602.64]  So can you kind of tell us all about what Control Labs is and how it came about and what you're doing there and kind of just give us an intro to it?
[602.98 --> 603.38]  Absolutely.
[603.38 --> 603.46]  Absolutely.
[604.10 --> 613.38]  So Control Labs, we're building a neural interface and maybe a bit surprisingly for what people think of when you, when you hear that phrase, the device that we build is worn on the arm.
[613.70 --> 615.90]  And I'll get into what that means in a second.
[615.90 --> 624.22]  But essentially the goal of the company is to become the new interface technology that, that allows people to connect and control machines.
[624.22 --> 630.82]  And so you can think of this as eventually, but perhaps a replacement for everything you use to control machines right now.
[630.90 --> 634.18]  Keyboards, mice, touchscreens, joysticks, all of that.
[634.18 --> 651.60]  Because when you boil it down, all of those physical and mechanical controllers are just a machine that is designed to convert signals coming out of your brain that get transmitted into muscle movement that you move your hand to touch something, which eventually gets transduced into a signal that goes into the computer to control something in software.
[651.60 --> 681.60] 
[681.60 --> 687.60]  And then eventually started to go into a machine that goes into a machine that goes into a machine.
[687.60 --> 689.60]  And now he's back.
[689.82 --> 690.82]  Now he's back in tech.
[691.08 --> 692.02]  He's back and he's, yeah.
[692.38 --> 694.26]  And this is the CEO, is that right?
[694.68 --> 694.96]  Correct.
[695.46 --> 695.68]  Okay.
[695.68 --> 696.24]  Yeah.
[696.24 --> 717.58]  So you mentioned that what most people might kind of think about when they first think about like a brain machine interface, like the first thing that I think about is like a bunch of wires coming out of my brain or like, you know, someone drilling a hole into my skull and inserting something and then like connecting it to a big server or something like that.
[717.58 --> 719.36]  And then I, you know, take over the world.
[719.50 --> 722.88]  I, you know, I've seen too many sci-fi movies.
[723.06 --> 724.20]  Maybe a bad imagery, man.
[724.20 --> 728.26]  This is, uh, this is not the case with control labs, right?
[728.68 --> 728.80]  Yeah.
[728.80 --> 731.24]  We're not going for the plug in the back of the skull just yet.
[732.34 --> 741.22]  I mean, and so there's actually some really interesting reasons why we believe that, that that's actually never going to be the right way to do this.
[741.22 --> 744.66]  If what you're interested in is control, and I'll talk about what that means.
[744.66 --> 755.86]  But if what you're interested in is having some effect in the world, then the motor nervous system is the part of your brain that is specifically evolved to do that.
[756.26 --> 763.02]  So let's maybe just talk a little bit about the neurophysiology and the neuroanatomy to kind of back up what like behind that belief of ours.
[763.02 --> 769.38]  Um, you know, not to mention the fact, of course, that it's not so, you know, user friendly to like drill holes in your skull in order to be able to play video games.
[769.60 --> 770.32]  But thank goodness.
[770.52 --> 771.06]  Besides that.
[771.38 --> 771.70]  Yeah.
[772.08 --> 782.00]  So, you know, maybe a good way to start is that, um, so one of our science advisors, uh, Daniel Wolpert, who's just incredibly brilliant neuroscientist and his expertise is in the motor nervous system.
[782.00 --> 786.16]  He's got a great TED talk that, um, that you should totally, everyone should go and watch.
[786.36 --> 788.70]  Uh, I think it's called the real reason for brains.
[789.06 --> 802.88]  And, you know, he makes this super surprising, but really cogent argument that from an evolutionary perspective, the only reason that brains exist, they're not there for thinking and feeling, even though that's like, obviously what we think of as, as, you know, our human experience of having a brain.
[802.88 --> 815.58]  But as far as an animal evolution goes, brains are there for one purpose and that's to move muscles to have some effect in the world because from a survival evolutionary perspective, like nothing else that you do has any purpose in the world.
[815.58 --> 817.38]  With the one exception that he makes is sweating.
[817.48 --> 824.08]  It's the only thing you could do to affect the world besides move a muscle, you know, breathing, talking, everything involves your motor nervous system.
[824.08 --> 832.56]  And he also gives this really cute example of, um, uh, there's a sea squirt, which is like, you know, this primitive, uh, form of life and it is an animal.
[832.70 --> 835.62]  It's born with a brain and it swims around for a while in the early part of its life.
[835.62 --> 845.36]  And then at some point it, you know, settles down, finds a nice little rock and then it digest its own brain, uh, because it no longer needs it because it's not moving anymore.
[845.36 --> 848.08]  And it doesn't need this extra baggage.
[848.44 --> 850.84]  Um, yeah, my wife claimed I did that years ago.
[850.84 --> 853.84]  Well, I, I have some evidence that you still have a brain, but.
[854.08 --> 855.32]  I'm not going to argue with your wife.
[856.14 --> 856.70]  Go ahead.
[856.74 --> 857.06]  I'm sorry.
[857.52 --> 859.00]  Um, so yeah.
[859.02 --> 867.04]  So, you know, if you think about it from that perspective, all of the, the cortical BMI, in other words, the brain machine interface that is focused on getting signals out of the cortex.
[867.34 --> 870.64]  If what you're trying to do is figure out, okay, so let's talk about control.
[870.94 --> 873.60]  So, you know, our name of the company is control labs.
[873.88 --> 882.06]  And from our perspective, what we think of control is it's the process of turning intention in the mind into action in the world.
[882.06 --> 885.18]  So you've got some desire to have some change happen in the world.
[885.18 --> 887.68]  That's, that's kind of our loose definition of intention.
[888.04 --> 891.74]  And you, and then to turn that into action, actually make something happen in the world.
[892.10 --> 900.12]  The part of the brain that does that, you might have a lot of like swirling unconscious thoughts and all the stuff that's, you know, responsible for regulating your internal organs and whatnot.
[900.12 --> 906.54]  But the moment you go to do something in the world and that intention becomes action, that's your motor cortex.
[906.72 --> 909.96]  That's the part of your brain that is like what was called the output port of the brain.
[910.48 --> 917.40]  And in fact, even people who are doing, you know, invasive cortical BMI or the, you know, opening up the skull and trying to plant electrodes in there.
[917.40 --> 919.08]  They're planting those electrodes.
[919.08 --> 923.34]  They're targeting the motor cortex because that's the part of the brain that like is involved for this stuff.
[923.82 --> 926.28]  You know, you specifically don't want information.
[926.46 --> 928.82]  You don't like all the rest of the processing that's happening in the brain.
[928.92 --> 931.42]  It's essentially background noise that you want to kind of get rid of.
[931.66 --> 936.54]  So that's the first principle kind of from a neuroscience perspective, why we're interested in the motor nervous system.
[937.02 --> 937.08]  Okay.
[937.20 --> 938.96]  The second thing is just like a matter of scale.
[938.96 --> 943.52]  Like, you know, there's billions of neurons in the brain when, where we are focused on the arm and the forearm.
[943.52 --> 948.00]  And the reason why we're there is because it controls the hand and the hand is super important for humans.
[948.34 --> 951.40]  And in fact, about a third of the motor cortex is dedicated to the hand.
[951.78 --> 954.30]  Another third goes towards the speech production system.
[954.30 --> 957.30]  And then the rest of your body, like all of your body only gets like the remainder.
[957.76 --> 961.20]  So, you know, there's on the order of 10,000 neurons, motor neurons in the arm.
[961.58 --> 967.82]  And so like, you know, we just have a much simpler problem in terms of trying to decode signal from noise being outside the body.
[967.82 --> 973.78]  And then the third thing is that there's just a signal to noise ratio question.
[974.18 --> 984.10]  And the really great thing about the neuroanatomy, when we talk about surface EMG, so the technology we use to decode the signal, I should say, is surface electromyography.
[984.10 --> 995.64]  So that's basically taking the electrical voltage changes when your muscles contract and decoding that with electrodes that sit on the surface of your skin, that are embedded in a bracelet or eventually a watch.
[995.96 --> 1000.02]  And they're just reading, you know, voltage potential differences as your nerves make your muscles fire.
[1000.52 --> 1008.96]  And the critical thing to understand and why we call this a neural interface is that, you know, nerves communicate in this kind of quasi-digital way with these spikes.
[1008.96 --> 1020.34]  So even though it's an analog signal in the sense that there's a voltage potential wave that goes down the axon of a neuron and also through the muscles, we'll talk about the shape of that wave.
[1020.38 --> 1024.24]  And in fact, the size of it, the amplitude is extremely rigid for a given kind of neuron.
[1024.38 --> 1025.76]  It basically always looks the same.
[1026.12 --> 1031.36]  And so information is encoded in the nervous system through essentially the firing rate of these spikes.
[1031.50 --> 1035.22]  It's almost like a digital binary ones and zeros sort of information flow.
[1035.22 --> 1045.14]  So when the brain is trying to move a muscle, a spike train, a series of these very fixed-shaped spikes will be sent from the motor cortex in the brain.
[1045.60 --> 1047.78]  One neuron will carry that signal down the spinal cord.
[1048.10 --> 1050.62]  Second neuron will carry it from the spinal cord out to the muscle.
[1050.76 --> 1052.84]  So there's only two neuron hops from there.
[1053.16 --> 1059.48]  And then when it hits the muscle, it's the same exact shape of the signal is propagated through the muscle as the muscle contracts.
[1059.68 --> 1064.90]  So the signal that we get is essentially the exact same information that's coming out of the motor cortex.
[1065.22 --> 1065.66]  That's cool.
[1065.84 --> 1078.30]  So this was like, you know, the whole insight that Briden and Patrick, you know, as neuroscientists understood is like, why go into the brain when the signal that you actually want, as far as control, is like available so much more easily on the surface of the skin in the muscle.
[1078.30 --> 1087.90]  And there's one more point to make, which is that the voltage signal as it's traveling, the size of the voltage in these signals as they're traveling in the nerves is like in the order of microvolts.
[1088.38 --> 1102.10]  But what happens in the muscle once a single nerve motor neuron will come and innervate, meaning, you know, attached to a nerve, a whole sort of bundle of muscle cells from these muscle fibers.
[1102.10 --> 1104.50]  And that whole thing together is called the motor unit.
[1104.62 --> 1108.02]  So one nerve and all the muscle fibers that it innervates is called the motor unit.
[1108.36 --> 1111.70]  And each of those muscle fibers in the motor unit only gets input from that one signal.
[1111.80 --> 1113.18]  So it's kind of like a one to many mapping.
[1113.58 --> 1117.20]  And that whole thing, when a spike comes down the nerve, it all fires at once.
[1117.20 --> 1118.34]  And it's basically an amplifier.
[1119.04 --> 1134.36]  So from an electrical perspective, we've got this amazingly nice built-in amplifier that takes the tiny little microvolts signal that would be traveling in a neuron and pumps it up to millivolts that's readable through all the tissues of the arm and through the skin and not worry about hair and all that stuff.
[1134.36 --> 1135.28]  All right, Adam.
[1135.52 --> 1144.76]  So maybe it's just because I don't want to have a hole drilled into my head, but you've convinced me that that's not the way to go.
[1144.76 --> 1150.34]  And, you know, there's this really great signal that we can tap into through the surface EMG.
[1150.94 --> 1170.52]  Maybe you could kind of switch directions a little bit here and kind of motivate why neural machine interaction or a neural interface, why is it important that we pursue this sort of interaction and don't just, you know, stick with the kind of mechanical interfaces that we're familiar with?
[1171.20 --> 1171.68]  Yeah, thanks.
[1171.76 --> 1172.90]  That's a great question.
[1172.90 --> 1180.06]  So I guess maybe one way to get into this is think about the transition that seems to be happening in personal computing.
[1180.28 --> 1185.44]  So, you know, a lot of people who pay attention to technology believe that we're on the cusp of a giant paradigm shift.
[1185.88 --> 1190.34]  What is going to be the personal computing platform that is going to replace the phone in your pocket?
[1190.44 --> 1198.34]  So, you know, maybe let's talk a little bit of the history of HCI and the kind of paradigm shifts as I see it, you know, over the last 40 or 50 years.
[1198.34 --> 1200.48]  So, you know, in the beginning was the command line.
[1200.78 --> 1208.64]  By the way, that's a really great essay by, I think it's Neil Stevenson, about just how cool it was when you compute, you know, just using terminals and text input.
[1208.64 --> 1210.44]  But it's also interesting.
[1210.80 --> 1216.50]  And then it's a perspective about, you know, the transition from that to GUI-based, you know, Windows, what do they call it?
[1216.54 --> 1219.40]  WIMP, Windows, icons, menus, and pointers.
[1219.64 --> 1228.76]  You know, like the desktop computing paradigm that we all know and love, question mark, maybe love, that, you know, came out of the research at Xerox PARC and Doug Engelbart's mother of all demos.
[1228.76 --> 1230.78]  And so that was a second phase.
[1231.06 --> 1234.22]  And then there was touchscreens and mobile computing.
[1234.62 --> 1250.96]  And so it seems like with VR, AR, XR, wearable computing, and the whole idea that computing is getting cheaper and smaller and will start to become embedded in the things around us and maybe just embedded into things that we can wear and a multitude of sensors and a multitude of processors around us.
[1250.96 --> 1255.14]  And so for a long time, HCI researchers have been sort of anticipating this transition.
[1256.16 --> 1259.72]  And I guess ubiquitous computing is probably the best umbrella term for this.
[1259.94 --> 1263.50]  You know, some people now calling it spatial computing, wearable computing.
[1263.76 --> 1274.20]  But so, you know, the vision is that once the display becomes mounted in your eyeglasses or your contact lenses, then you no longer have to be holding anything.
[1274.42 --> 1275.68]  So how do you do input?
[1275.68 --> 1283.60]  What is the, you're not walking around with your magic, you know, AR glasses in the future holding an Xbox controller so that you can navigate your email.
[1283.84 --> 1296.78]  And if you think about it, like every one of these big HCI paradigm shifts really comes with like a pair of technologies that play the input and the output role that together make up the new interface paradigm.
[1296.78 --> 1302.14]  So, you know, when the shift from console to computing to GUI computing, right, the mouse is the input.
[1302.50 --> 1306.76]  And then like a cheap rasterized display technology was the output.
[1307.12 --> 1313.58]  And with touchscreens, it's kind of interesting because the output and the input are fused together into the single device, but they have two very different roles that they play.
[1313.64 --> 1314.66]  And they're actually completely separable.
[1314.74 --> 1316.44]  You could have a touchscreen that's only input if you wanted.
[1316.82 --> 1318.50]  I mean, and if you go back and read the writing.
[1318.50 --> 1327.16]  So I just reread some of Jared Lanier, you know, he's one of the early VR pioneers and I think is credited as coining the term VR.
[1327.84 --> 1331.90]  And he was so focused in the beginning on the input as much as the output.
[1332.08 --> 1345.34]  You know, they did all these experiments with data gloves and all kinds of other motion capture technologies because they recognize that if you want to have a truly immersive experience, then it's not enough just to have a visual immersion, like, you know, the input side.
[1345.34 --> 1349.64]  You also have to understand, like, what is the person trying to do and let them interact with the world.
[1349.78 --> 1352.20]  And so that was a big focus in the beginning.
[1352.32 --> 1370.60]  And I think what happened around the time when, you know, when Palmer was making the hardware work on the display side, that like raced ahead and cheap and, you know, good enough display technology with good head tracking happened before there was another big shift on the input side.
[1370.60 --> 1375.34]  So that kind of leapt ahead and that leads us to where we are right now where there's this kind of a big gap.
[1375.44 --> 1378.40]  And if you use the VR systems today, it's really beautiful.
[1378.68 --> 1380.20]  Like you feel visually immersed.
[1380.28 --> 1380.80]  You look around.
[1380.88 --> 1381.30]  It's amazing.
[1381.56 --> 1388.40]  And then you just have these sticks where your hands should be, you know, with these kind of like game controllers stuck onto a positional tracker.
[1388.40 --> 1392.16]  And it's very kind of disappointing from an interactions perspective.
[1392.16 --> 1399.88]  You don't have the naturalness, the expressivity, the like incredible, you know, dexterity and agility and skillfulness that you have with your hands.
[1399.88 --> 1414.82]  So that's like, I think the big picture that we're thinking that, you know, this technology is going to be the thing that is, you know, in a device that you just are wearing all day long and is the way that you interact on a minute to minute basis with all the devices in your life.
[1414.94 --> 1421.80]  You know, trolling the volume in your car and typing an email while you're walking down the street or, you know, playing a video game, whatever it is.
[1421.90 --> 1423.90]  It's, you know, hands are the best controllers.
[1423.90 --> 1425.44]  And so all you need is hands.
[1425.60 --> 1430.40]  So we're just building a device that will just allow you to plug in directly to the signal that's controlling your hands.
[1431.06 --> 1431.16]  Gotcha.
[1431.34 --> 1435.28]  So one of the things I'm kind of wondering, and that was a great explanation, by the way.
[1435.50 --> 1442.36]  But if you're in a very practical sense, I'm imagining that person that's starting to utilize this technology going forward.
[1442.36 --> 1448.62]  And I have seen the AI conference video, you know, of the presentation.
[1448.62 --> 1455.42]  And so I have a sense of, you know, being able to utilize the technology where you're starting to remove the hardware between.
[1455.82 --> 1461.92]  But we also have other HCI, which for listeners, if you don't know, is human computer interface forms.
[1462.24 --> 1463.86]  Like voice interfaces are so popular.
[1464.62 --> 1466.20]  I have kind of a two-part question.
[1466.20 --> 1477.22]  How would you imagine what you're doing at Control Labs interfacing with these other types of HCI, you know, such as doing this chat, which is so popular now.
[1477.38 --> 1479.54]  And we're already kind of programming that in APIs.
[1479.98 --> 1487.44]  And kind of the second half to this is when you're looking at that combined world of utilizing all of these methods together.
[1487.44 --> 1496.22]  I know you guys have Control Kit that you've released, and it has, you know, what, you know, is essentially, you know, I guess you're describing as an API for the brain.
[1496.56 --> 1501.26]  How do you realize that in an API, considering that you have different modes of communication?
[1501.78 --> 1506.22]  I think there will be a lot of things used at the same time together.
[1506.22 --> 1509.18]  I think that there's going to be a multimodal approach.
[1510.08 --> 1518.62]  And, you know, maybe let's just shake the kind of the two things of voice input and this idea of a neural interface that's getting the output from your hands.
[1518.94 --> 1522.54]  And the way that those things can be used together is really fascinating.
[1522.84 --> 1525.42]  And, you know, they have different strengths and weaknesses.
[1525.64 --> 1528.84]  Obviously, there's privacy concerns or just kind of social awkwardness.
[1528.84 --> 1535.72]  You don't always want to be speaking out loud in public to control your computer or to do input in terms of text input and communicate.
[1536.36 --> 1540.16]  You know, you might be sitting in a cafe and you're writing a sensitive email or you just don't want to bother your neighbors.
[1540.60 --> 1541.74]  And so, you know, people still type.
[1542.06 --> 1545.76]  On the other hand, there might be circumstances where your hands are full and you can't use them.
[1546.30 --> 1548.80]  And speaking might be the most natural thing.
[1549.12 --> 1555.48]  Although we've been exploring some really interesting ways that you can still do quite a lot while you're holding objects.
[1555.48 --> 1564.72]  And because, you know, in some sense, we didn't really talk about how sensitive the device is, but tiny little twitches that are essentially invisible to the naked eye are enough to do control with this technology.
[1564.72 --> 1569.22]  So you could be holding your coffee cup and just doing little presses or wiggles with your fingers and be typing.
[1569.72 --> 1573.14]  And then, of course, there's a combined impact, right?
[1573.16 --> 1580.54]  If you have, you know, all channels available at once, if you're in your office and you can speak out loud, but you can also use your hands, you know, maybe we'll just get that.
[1580.66 --> 1582.78]  You can use that to boost up the bandwidth.
[1582.78 --> 1587.66]  If you think about this technology, it's just a way to increase the output bandwidth from the brain to the world.
[1588.00 --> 1589.42]  We have so much bandwidth coming in, right?
[1589.80 --> 1593.26]  High resolution video displays and great audio.
[1594.00 --> 1598.10]  And the bandwidth coming out from the brain is just lagged behind for 50 years.
[1598.22 --> 1606.78]  I mean, typing on a keyboard, you know, is one way to kind of estimate what's the maximum just in terms of pure bits per second that you can get out of the brain.
[1606.78 --> 1611.54]  You know, the fastest type is in the world doing like 150 words a minute.
[1611.72 --> 1614.14]  That's something like 30 bits a second.
[1614.54 --> 1617.98]  And, you know, compare that to like gigabytes of information coming in.
[1618.32 --> 1621.58]  So, yeah, I think this multimodal thing might be a way that it goes.
[1621.58 --> 1635.36]  And another point I was going to make is when I was working on speech recognition, it always seemed to me, especially when I was at Google and the first really great ASR systems were coming out and were put into Android in terms of, you know, speech input on Android.
[1635.58 --> 1639.96]  It always seemed to me a waste that I couldn't also use my hands while I was doing speech input.
[1639.96 --> 1648.04]  I'd be holding the phone and it would be making all these errors and, you know, hopefully not too many, but still still makes errors sometimes.
[1648.26 --> 1652.46]  And then you kind of have to slowly go back and correct things with your hands in this old school typing way.
[1653.10 --> 1657.58]  It just seemed to me that there was like had to be a better way that you could combine the input of your hands with speech.
[1657.68 --> 1659.96]  So that's one of the interesting areas that we're working on.
[1659.96 --> 1674.46]  This episode is brought to you by the O'Reilly Open Source Software Conference in Portland, Oregon, July 15th through the 18th.
[1674.68 --> 1686.88]  OSCON, the O'Reilly Open Source Software Conference is where you go to understand what's shaping software development from AI and cloud technology to distributed computing and learn how to put it to work for you and your team.
[1686.88 --> 1694.68]  Whether you're looking to understand where software development is heading or machine learning can make or break your code, OSCON is where you'll find your answers.
[1695.28 --> 1700.60]  Hear from industry leaders like Pete Skomeroach, Holden Carew, Allison McCauley, and Sam Charrington.
[1701.02 --> 1705.30]  Passes start at 796 when you register with the code CHANGELOG20 before June 7th.
[1705.30 --> 1712.80]  Again, before June 7th, use the code CHANGELOG20 and head to OSCON.com slash CHANGELOG to learn more and register.
[1716.88 --> 1733.38]  You know, because this is a podcast, it might be hard to imagine the sort of interface that you're talking about.
[1733.48 --> 1738.26]  And I know Chris mentioned that you released this kind of control kit developer.
[1739.10 --> 1741.14]  I don't know what you, I guess kit is a good word.
[1741.14 --> 1743.04]  You already picked the best word.
[1743.34 --> 1754.68]  But could you just describe to our listeners what the interface or the device looks like and kind of how you wear it and then how it connects to another device?
[1754.78 --> 1761.32]  Let's say a computer you're wanting to kind of type with your muscles, I guess, in how you're describing it.
[1761.36 --> 1765.80]  So could you kind of just describe for our listeners how that looks and how it connects?
[1765.80 --> 1771.20]  Yeah, it looks kind of like a chunky sort of cyberpunk bracelet right now.
[1771.52 --> 1774.70]  We currently wear it kind of midway up the arm and the forearm.
[1774.94 --> 1779.88]  But the goal is to get this down at the wrist and have it be able to be integrated with a watch.
[1780.60 --> 1782.42]  We have devices that work on the wrist already.
[1782.54 --> 1787.04]  It's actually the biggest challenge to getting to the wrist is really just the, your tendons move a lot.
[1787.08 --> 1794.28]  If you kind of, you know, look at your wrist as you're kind of moving, like look at the space where you would wear a watch as you move your wrist around.
[1794.28 --> 1805.50]  There's usually all these kind of divots and the topography of your, just the mechanical challenges of keeping the electrodes in contact with your wrist as you move around is the major thing keeping us from being at the wrist.
[1805.92 --> 1813.16]  But yeah, it's, it, the electrodes that make contact with your skin are on the inside of the, of the device, obviously against the skin.
[1813.72 --> 1814.66]  They're pretty cool.
[1814.82 --> 1816.52]  They're actually gold plated right now.
[1816.66 --> 1818.02]  And they got some bling.
[1818.02 --> 1825.54]  It's got some serious bling and the whole, the whole effect is this sort of like, you know, cyberpunk meets like studded biker leather look.
[1826.06 --> 1827.18]  Oh, I'm into this now.
[1827.42 --> 1827.72]  Yeah.
[1828.14 --> 1829.64]  Chris, do you think I could pull it off?
[1829.98 --> 1831.34]  Ooh, absolutely, Daniel.
[1831.34 --> 1833.66]  So that's where we are now.
[1833.74 --> 1835.78]  And of course, you know, this is, we're just beginning.
[1835.98 --> 1840.66]  This is the first device that we have that is not just like a total research prototype.
[1840.66 --> 1851.08]  You know, our previous generations of device were like literally we started with sweat bands with electrodes sewn into them and then kind of, you know, ratcheted up the ladder of, of hardware productionization.
[1851.08 --> 1853.74]  So, yeah, so it's Bluetooth.
[1853.86 --> 1856.16]  It communicates to a host computer over Bluetooth.
[1856.94 --> 1865.68]  And currently with, with the, with the developer kit, as we're shipping it right now, you need a, like a fairly, you can't connect directly to a phone.
[1865.76 --> 1868.76]  You need a host computer that can run the, the other side of the pipeline.
[1868.76 --> 1874.88]  It's actually doing the machine learning inference and the, and the processing, signal processing mostly happens off board device right now.
[1874.88 --> 1883.60]  But, you know, as we, as we go through the iterations of hardware, we're going to move more and more processing on, on board so that you can connect directly to a phone, let's say.
[1884.00 --> 1889.82]  And can you, since you've kind of segued into it, can you tell us a little bit about what you're doing in terms of machine learning for this?
[1889.92 --> 1891.26]  Where is it being used?
[1891.62 --> 1892.86]  What kind of problems are you solving?
[1892.86 --> 1898.36]  And what are some of the choices if you're, if you're able to share that you're using to, to tackle those?
[1898.70 --> 1898.84]  Yeah.
[1898.84 --> 1898.88]  Yeah.
[1899.50 --> 1911.90]  So maybe one thing to say about the machine learning side of this from the beginning is I think the most exciting thing that we're doing kind of from a machine learning perspective is this is an entirely new domain, a signal domain to work on.
[1911.90 --> 1928.70]  You know, if you think of actually you had a guest on a couple of weeks ago from IBM healthcare who, and he, he, he said something about, you know, you guys are talking about processing speech as a way to diagnose psychiatric disorders and stuff like that.
[1928.70 --> 1939.10]  And again, I think, you know, the idea of some kind of brainwaves came up and he said, you know, speech is a brainwave and we very much feel the same way about the signal that we're working with.
[1939.24 --> 1947.94]  You know, it is this bio signal, a signal generated by the brain that is extremely information rich, carrying all this content about what people want to do.
[1948.60 --> 1950.46]  And it's as rich as speech really.
[1950.92 --> 1952.16]  And it's new.
[1952.16 --> 1954.98]  It's like, you know, nobody has had access to this kind of signal before.
[1955.16 --> 1959.64]  I mean, not outside of, you know, very narrow clinical settings and neuroscience research.
[1960.22 --> 1961.52]  So that's just really cool.
[1961.62 --> 1972.32]  It's like, you know, it's like as if we just invented a microphone and we can start doing speech recognition, except instead of, you know, like the microphone, the time distance between them and the microphone was invented.
[1972.46 --> 1977.00]  And when machine learning was good enough to do, you know, speech recognition was like almost 100 years.
[1977.00 --> 1979.28]  And for us, it's like we're there already.
[1979.42 --> 1985.22]  So we've got this access to a new signal that's extremely interesting and already have great machine learning tools to work on it.
[1985.76 --> 1994.78]  And the parallels to speech actually go pretty deeply because it's a, you know, multi-channel, time-varying, continuous signal that has frequency content.
[1994.78 --> 1999.30]  And some of the information is there, but it's got this particular structure in the way that it was generated.
[1999.30 --> 2010.14]  And then there's like all these layers that you can sort of start by parsing the kind of lower levels, understanding how to do the signal processing and get rid of the noise and figure out where the information is.
[2010.14 --> 2018.12]  And then as you go up the stack of processing, you get into meaning and semantics and what is the person trying to do and actually recognizing people's intention.
[2018.68 --> 2018.84]  All right.
[2018.84 --> 2029.44]  So you kind of alluded to part of this a little bit ago where you were talking about, you know, where machine learning fits into this pipeline and there's kind of two sides of it.
[2029.44 --> 2046.68]  So is my understanding right that kind of the device that you're wearing on your arm, this super cool looking cyberpunk bracelet armband, yeah, cyberpunk armband, it's sending these continuous neural signals to a computer or to a host computer.
[2046.68 --> 2055.26]  And then you're running a model on that host computer that's kind of making inferences based on those signals.
[2055.50 --> 2059.08]  Is that kind of the overall pipeline or did I get something wrong there?
[2059.52 --> 2060.56]  No, that's exactly right.
[2060.86 --> 2066.94]  And the kind of differences that we make are dependent on what the application is and what we're interested in doing.
[2067.12 --> 2075.72]  So the basic capabilities of ControlKit, the API, as it is right now, include things like reconstructing the position of the hand.
[2075.72 --> 2081.16]  So sort of the canonical classic demo we have is essentially like you'd see something from like elite motion.
[2081.32 --> 2088.22]  It's essentially a motion capture experience where you just see a virtual rendering rendition of your hand.
[2088.40 --> 2095.64]  And what we're doing is we're predicting all the joint angles, the positions of your fingers and your wrist as you move your hand around.
[2095.64 --> 2101.16]  And we can also detect things like how strongly your muscles are contracting.
[2101.28 --> 2108.00]  And this is one of the kind of primary advantages that this technology has compared to a camera-based hand tracking system.
[2108.12 --> 2120.00]  So most of the effort and investment over the past five or 10 years in terms of hand tracking for the purposes of VR and XR have gone into camera-based systems, inside-out tracking and outside-in tracking.
[2120.00 --> 2123.48]  And with any camera-based system, you always have occlusion problems.
[2123.56 --> 2126.00]  What happens if your hands are not in view of the camera, right?
[2126.04 --> 2133.70]  So you can either try to solve that by just placing cameras everywhere, or you can have a technology that doesn't have any occlusion problems at all, which is what we're providing.
[2133.70 --> 2147.26]  So we sometimes have been talking about this as maybe like inside-in tracking, where because you're sort of wearing this device that is looking inward at your own muscle and your own neural signal, there's no possibility of any occlusion problems.
[2147.74 --> 2155.22]  So the device works as well with your hands in your pockets or in a glove or in a spacesuit or whatever could be used in the future.
[2155.46 --> 2156.56]  So you don't have occlusion problems.
[2156.56 --> 2167.66]  And since we sense the strength of your muscles contracting is an enormous signal for us, and that's really another interesting difference between camera-based tracking systems.
[2168.20 --> 2173.98]  You know, if you kind of make a fist and now make a really strong fist, visually, there's really not that much difference there.
[2174.32 --> 2181.08]  But in terms of the signal that we see, the firing rate of the neurons that are controlling these muscles, it's like huge.
[2181.16 --> 2182.30]  It's like an enormous event.
[2182.30 --> 2192.16]  So the other part of our API is recognizing stuff like forces of pinches on each finger and your fist and other interesting ways that you can kind of tense or relax your muscles.
[2192.50 --> 2198.02]  And that, I think, is going to be a really important part of the design problem around this, which is like how to use that signal.
[2198.28 --> 2208.56]  It feels extremely natural and expressive when you can kind of use muscle tension and how light or hard you're squeezing to be able to control software.
[2208.56 --> 2213.00]  But it's not how we're used to thinking about designing interfaces.
[2213.20 --> 2218.34]  So that's going to be a big challenge for us and for designers who are going to be working with this technology.
[2219.08 --> 2221.02]  Let me think if I covered everything in the API.
[2221.30 --> 2229.86]  So the hand skeleton tracking, poses and pinches, you know, also recognizing just hand pose, finger pointing and shapes.
[2229.86 --> 2237.14]  And then we're working on turning that stuff into usable, reliable controls, the equivalent of point and click.
[2237.56 --> 2245.98]  And we are working on the extremely interesting, to me personally, project of typing or figuring out how to do text input with this technology.
[2246.72 --> 2246.84]  Gotcha.
[2246.84 --> 2261.56]  So given the fairly unique type of signal that you're pulling off with the glove and passing over to the computer, what kinds of machine learning architectures are you trying to utilize and apply to these types of problems?
[2261.76 --> 2262.88]  You know, how are you approaching?
[2263.10 --> 2267.94]  I know you mentioned machine vision, which is typically done with convolutional neural networks.
[2268.18 --> 2272.98]  Would this be like with a recurrent neural network of some sort or something like that?
[2272.98 --> 2278.86]  Yeah, we do use RNNs of certain flavors and we use ComvNets in other places.
[2279.30 --> 2286.84]  It's actually a kind of grab bag of approaches and different things work better for different kinds of inference we're trying to do.
[2287.34 --> 2291.70]  I mean, one of the other interesting things is that so our current device has 16 channels.
[2291.90 --> 2297.66]  So there's 16 pairs of electrodes that go around your arm to kind of cover all of the area and pick up lots of different muscles.
[2297.66 --> 2313.94]  And the way to combine those signals from neighboring electrodes and there's actually, it parallels, you know, a branch of signal processing that's going to think about beam forming and multi-microphone array technology.
[2313.94 --> 2316.50]  This is, you know, popular in audio processing.
[2316.50 --> 2325.40]  If you're trying to isolate, you know, one signal from a crowd of background noise or you've got a room of people talking and trying to extract one signal out of many.
[2325.40 --> 2327.28]  So there's some of that kind of work as well.
[2327.68 --> 2328.54]  Yeah, we use RNNs.
[2328.60 --> 2329.34]  We use ComvNets.
[2329.68 --> 2331.76]  We're writing the machine learning stuff in TensorFlow.
[2332.32 --> 2334.36]  Our research team works mostly in Python.
[2335.14 --> 2338.70]  And then we have kind of the production system, which is in C++.
[2338.90 --> 2341.50]  And we've actually got a really nice way of blending those things together.
[2341.62 --> 2344.08]  I think that's kind of just on that kind of practical side.
[2344.08 --> 2355.98]  One of the challenges that we've always, in any machine learning based team that I've always worked on, is like there's usually a big gulf between what researchers are comfortable doing and then getting code into production can be like this big gulf.
[2355.98 --> 2365.22]  So we were very focused on making that hop very, very short and allowing researchers to work in an environment that's extremely close to what the production systems are like.
[2365.64 --> 2371.42]  And having, they natively can work in the environment that they prefer and have it be a quick hop to production.
[2371.42 --> 2384.62]  So I'm curious, I think, so I may be misremembering things, but I think you said that something about the signals that you're getting off the muscles are fairly consistent in how they're shaped.
[2384.72 --> 2398.94]  I was wondering, as far as like shipping the developer kit, is this a thing where like you train kind of models on your end on the control lab side with a ton of data that you've collected for different tasks?
[2398.94 --> 2404.26]  And then you kind of ship the models with the control kit to just be used for inferencing?
[2404.46 --> 2418.98]  Or do you have to do any sort of like transfer learning or fine tuning for a certain person's like, are my signals like different enough that you need to do some fine tuning for my signals versus like signals you've seen before?
[2419.86 --> 2425.72]  I've pinpointed one of the most probably critical problems from a research perspective that we're working on right now.
[2425.72 --> 2428.64]  So we've come at it from both ways, right?
[2428.96 --> 2429.80]  Everyone is different.
[2429.92 --> 2430.92]  Everyone's anatomy is different.
[2431.00 --> 2432.98]  The signal does look quite a bit different across people.
[2433.22 --> 2434.76]  And not just across people, but across sessions.
[2434.84 --> 2436.54]  You take the device off, you put it back on.
[2436.70 --> 2438.04]  The electrodes enter a different place.
[2438.10 --> 2442.94]  They're going to see a slightly different view of the underlying neuroanatomy and the signals will be different.
[2443.54 --> 2447.04]  So you have kind of cross-session generalization.
[2447.38 --> 2449.10]  That's, you know, take the device off, put it back on.
[2449.12 --> 2451.02]  And you also have cross-user generalization.
[2451.02 --> 2461.58]  I want to train something on people that we have available here in the office or, you know, getting people to come in and do data collection and then have it work on someone in the world who we've never seen before.
[2461.68 --> 2463.32]  And we've never seen their signal before.
[2463.54 --> 2465.18]  So there's two basic approaches, right?
[2465.20 --> 2470.30]  We can try to collect a lot of data from a lot of people and build models that will just generalize out of the box.
[2470.50 --> 2471.14]  And we do that.
[2471.14 --> 2483.04]  And then we also can go the other way where we come up with ways that can learn very quickly on the least data possible to get good performance with data from that one specific user.
[2483.20 --> 2492.80]  So in that case, you know, you have an experience where there be some kind of onboarding, calibration, training period where, you know, you would do some movements or play a little game or something like that.
[2492.80 --> 2497.00]  And it would be learning about you and your own particular signal as you're doing it.
[2497.00 --> 2512.12]  And then there's hybrid approaches where you kind of get as far as you can with generalization and then have a transfer learning or domain adaptation, as you were mentioning, approach where you try to build systems that are designed to be customized or personalized.
[2512.12 --> 2529.52]  So they might not be, the goal of them isn't necessarily to get the best out of the box performance as possible, but the goal of them is to learn about the kind of space of signal that you could see across people and learn how to adapt very quickly to a new user signal when you do get a little bit of data from that user.
[2530.08 --> 2534.90]  So as we've been talking, there's something in the back of my mind that I've kind of been wondering about.
[2534.90 --> 2539.88]  And that is, this is such a specialized domain that you're addressing.
[2540.16 --> 2546.90]  Is there a role in this for biologists or doctors in the development process to kind of capture that domain knowledge?
[2547.10 --> 2551.52]  Or is this something that you guys have been able to just to master on your own and move forward with the technology?
[2551.52 --> 2556.22]  The company was founded by neuroscientists and it's pretty important.
[2556.50 --> 2559.16]  There is a lot of domain knowledge that goes in.
[2559.74 --> 2575.88]  And even just at the very basic level of understanding what the signal that we are looking for ought to be and ought to look like, you know, the essential idea of trying to use EMG as a consumer device and, you know, for controlling computers goes back, you know, a ways.
[2575.88 --> 2586.62]  Actually, I remember when I was in grad school and we talked a little bit before about my interest in music, but I was also interested in, you know, new musical instruments and musical performance systems.
[2586.62 --> 2595.42]  And I remember reading about people who were hooking up electrodes to their body in various ways and then using that signal as a musical instrument.
[2596.28 --> 2597.90]  And so the ideas are floating around.
[2597.96 --> 2602.88]  I think it does require some deep understanding of the neurophysiology to understand.
[2602.88 --> 2608.64]  I think one of the key things was like knowing when to keep iterating on the hardware and when to stop.
[2609.20 --> 2622.68]  So Meardin and Patrick knew that if they could get the hardware to be good enough to recognize, you know, individual spikes on single motor units, then that essentially was all the information that there was to be had.
[2622.76 --> 2628.84]  And they didn't have to keep iterating after that, but they shouldn't stop making the hardware better until that point was achieved.
[2628.84 --> 2633.58]  So I think that was key and that differentiated, you know, our attempt at this from earlier ones.
[2634.18 --> 2635.92]  We do have, we've got MDs.
[2636.38 --> 2638.26]  We have MD PhDs on staff.
[2638.58 --> 2645.42]  And so, you know, some understanding of the anatomy is important, but there is some level at which, you know, machine learning is machine learning and the signal is what it is.
[2645.42 --> 2657.44]  And kind of, I mean, one of the cool things about working machine learning, I'm sure you guys have appreciated this, is that like, it's just a chance to become like a kind of mini expert on a particular domain that you happen to be working on a new problem.
[2657.58 --> 2665.04]  You know, you might come into knowing nothing about, you know, phonemes and phonetics and the way that language is constructed, but you start working on speech recognition.
[2665.04 --> 2672.02]  You learn a lot about it really quickly or, you know, if you're analyzing stock market data, you suddenly learn a lot about, you know, financial signals.
[2672.18 --> 2681.04]  And so I think that's part of the fun of doing machine learning and probably, you know, so anybody who'd come in and work at this company and learn a lot about that stuff, it's important, but, you know, it's not critical prerequisites.
[2682.30 --> 2682.38]  Yeah.
[2682.82 --> 2684.48]  So I appreciate you sharing that.
[2684.52 --> 2693.28]  That's definitely one of the things that I really appreciated about this industry and working in this area is all of the things that you constantly get to learn.
[2693.28 --> 2705.70]  Speaking of kind of people working in this space, I know I'm already kind of all of these ideas for utilizing the control kit and this technology are already popping into my mind.
[2705.70 --> 2715.10]  Like you were mentioning text input and I'm thinking about like over 350 sign languages that, you know, are known in the world.
[2715.10 --> 2729.52]  And typically, you know, people have not very good access to information that speak those sign languages and being able to have one of these devices on each hand and document those languages and get resources to these people.
[2729.74 --> 2732.80]  Like there's already all sorts of stuff popping into my mind.
[2732.96 --> 2741.52]  So if I want to like pursue something like that with control kit, kind of what's the rollout plan and what's the current access to control kit for developers?
[2741.52 --> 2747.74]  Yeah, we really want to hear about all the, you know, amazing applications that people have in mind when they hear about this technology.
[2748.32 --> 2749.86]  And we want people to start building with it.
[2749.94 --> 2752.08]  That's absolutely where we are as a company.
[2752.28 --> 2754.10]  We've got, you know, some basic stuff proved out.
[2754.50 --> 2758.62]  We really believe that this is a technology that's going to be super important in the future.
[2758.90 --> 2764.30]  And we want people to start playing with it and help us figure out how it can be used and what's it good for.
[2764.30 --> 2767.90]  So the first step would just be, you know, go to our website.
[2768.20 --> 2769.22]  It's control labs.
[2769.38 --> 2772.34]  That's CTRL-labs.com.
[2772.92 --> 2777.80]  And we've got a sign up there for the wait list on our dev kit.
[2778.28 --> 2779.42]  We're starting slow.
[2779.56 --> 2780.48]  You know, we're a startup.
[2780.64 --> 2781.22]  We're a small company.
[2781.30 --> 2787.70]  We don't have the, you know, bandwidth quite yet to support the hordes of people who may want to work with this stuff.
[2787.70 --> 2797.78]  But sign up and, you know, kind of rolling out over the next year, starting slow with developers, kind of handpicked for a couple of applications that we think are really interesting.
[2798.60 --> 2803.58]  And as we go, we're just going to pick up the pace and see what people want to build with it.
[2803.98 --> 2807.18]  The sign language thing, by the way, is super interesting.
[2807.28 --> 2810.16]  That's something I've been, you know, studying a lot about recently.
[2810.16 --> 2820.20]  And sign language is, I mean, I don't want to go into a super deep dive on it, but the grammar of sign language, the phonology of sign language, a natural sign language is extremely interesting.
[2820.38 --> 2827.46]  It's obviously, you know, as complicated as spoken language is, but it uses the articulators.
[2827.66 --> 2833.34]  And that's, you know, the technical term for like the part of your body that makes the signal go from the brain to the world.
[2833.34 --> 2845.12]  And so I think we have a lot to learn from it because it's like the main proven use case right now where we have like super high bandwidth output coming from people's brains in a communication channel using the muscles of the hand.
[2845.30 --> 2846.16]  And so it's very interesting.
[2846.98 --> 2847.10]  Yeah.
[2847.28 --> 2860.44]  Well, I know I'm going to be headed to the website after this to fill out the application and describe something about sign language and see if I can get one of these super, super dope bracelets on my arm.
[2860.70 --> 2860.98]  Awesome.
[2860.98 --> 2862.80]  I know someone who works there.
[2862.80 --> 2864.00]  Yeah, you might have an N if you.
[2864.14 --> 2864.62]  Okay.
[2865.38 --> 2866.32]  Sounds great.
[2866.58 --> 2866.74]  Yeah.
[2866.82 --> 2886.38]  Well, I really appreciate you sharing so much of the great context around this technology and also kind of bringing it down to make it practical and help people understand that there is a practical route towards kind of processing these signals and getting them into a computer to utilize them.
[2886.38 --> 2888.76]  So it's really, really been useful for me.
[2888.86 --> 2892.62]  And I appreciate you taking the time to walk us, walk us through that.
[2892.62 --> 2898.94]  We'll definitely put the links to the website and the control kit and the TED talk and all of those things that we talked about in our show notes.
[2899.08 --> 2900.34]  But thank you so much, Adam.
[2900.40 --> 2901.56]  It's been great to talk.
[2902.04 --> 2902.30]  Thanks.
[2902.34 --> 2902.88]  It was really fun.
[2903.20 --> 2904.10]  It was super cool, man.
[2904.16 --> 2904.44]  Thanks.
[2904.44 --> 2907.16]  All right.
[2907.16 --> 2909.84]  Thank you for tuning into this episode of Practical AI.
[2909.84 --> 2911.58]  If you enjoyed this show, do us a favor.
[2911.70 --> 2913.06]  Go on iTunes and give us a rating.
[2913.38 --> 2915.20]  Go in your podcast app and favorite it.
[2915.30 --> 2918.04]  If you are on Twitter or social network, share a link with a friend.
[2918.10 --> 2920.46]  Whatever you got to do, share the show with a friend if you enjoyed it.
[2920.76 --> 2923.42]  And bandwidth for ChangeLog is provided by Fastly.
[2923.54 --> 2924.98]  Learn more at Fastly.com.
[2925.16 --> 2928.36]  And we catch our errors before our users do here at ChangeLog because of Rollbar.
[2928.58 --> 2930.98]  Check them out at Rollbar.com slash ChangeLog.
[2930.98 --> 2933.80]  And we're hosted on Linode Cloud Servers.
[2934.12 --> 2935.76]  Head to Linode.com slash ChangeLog.
[2935.84 --> 2936.32]  Check them out.
[2936.38 --> 2937.22]  Support this show.
[2937.56 --> 2940.80]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2941.24 --> 2943.32]  The music is by Breakmaster Cylinder.
[2943.68 --> 2947.14]  And you can find more shows just like this at ChangeLog.com.
[2947.14 --> 2949.30]  When you go there, pop in your email address.
[2949.58 --> 2955.60]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2955.98 --> 2956.78]  Thanks for tuning in.
[2956.94 --> 2957.70]  We'll see you next week.
[2960.98 --> 2970.42]  Because you've listened all the way to the end of the show,
[2970.70 --> 2974.60]  I've got a little preview here for you of our upcoming podcast called Brain Science.
[2974.60 --> 2980.66]  This podcast is for the curious that explores the inner workings of the human brain to understand behavior change,
[2980.74 --> 2983.44]  how about formation, mental health, and the human condition.
[2983.78 --> 2989.60]  This show is hosted by myself, Adam Stachowiak, and my good friend, Mariel Reese, a doctor in clinical psychology.
[2989.60 --> 2991.74]  It's brain science applied.
[2991.82 --> 2995.94]  Not just how does the brain work, but how do we apply what we know about the brain to better our lives?
[2996.50 --> 2996.94]  Here we go.
[2998.18 --> 3002.74]  That applied brain science really stood out to me because I don't want it to just be data.
[3003.10 --> 3004.78]  I want you to go, how can this fit?
[3004.88 --> 3005.78]  What can I take away?
[3006.08 --> 3007.46]  Now, how am I going to change?
[3007.88 --> 3010.00]  And that that sort of is where you come in more.
[3010.10 --> 3013.40]  And even some of the questions like, so like I want to ask you,
[3013.40 --> 3018.28]  what are some of the most challenging things working in the tech world when it comes to relationships?
[3018.86 --> 3020.76]  Probably the most important one is isolation.
[3021.20 --> 3025.08]  More and more of the world and companies are being, for good reasons,
[3025.08 --> 3028.10]  they're being okay with what they call distributed teams.
[3028.54 --> 3028.66]  Yeah.
[3028.74 --> 3031.56]  And that means that you and I, we work for the same company,
[3031.56 --> 3032.92]  but you work from your home office.
[3032.98 --> 3034.04]  I work for my home office.
[3034.52 --> 3037.46]  I might go into the office a couple of times a week if I live local.
[3037.46 --> 3041.24]  But even if I live in San Francisco, I'm still probably a remote worker,
[3041.36 --> 3046.14]  even though I can hop in an Uber or hop on, you know, the train or whatever
[3046.14 --> 3048.44]  and go into the office and be there in a half hour.
[3048.50 --> 3049.48]  But why waste the time?
[3049.98 --> 3055.28]  You know, and this is where I would revisit what I want to talk about with resonance.
[3055.68 --> 3059.22]  And that whenever we're learning, no matter what thing,
[3059.26 --> 3062.80]  it's really helpful when we get feedback that's both immediate and specific.
[3062.80 --> 3068.96]  And so when you're by yourself and you don't have any interaction with other people,
[3069.10 --> 3070.80]  how can you get any feedback?
[3071.22 --> 3075.24]  I mean, you're losing most of the nonverbal communication
[3075.24 --> 3081.26]  and you also don't have all of the voice inflections or facial expression.
[3081.52 --> 3086.80]  Have you ever tried to, you know, be sad, feel sad and smile at the same time?
[3087.60 --> 3087.98]  Try it.
[3089.34 --> 3090.58]  It's pretty hard.
[3090.58 --> 3096.34]  Right, because facial expression is exactly what's involved when it comes to empathy,
[3096.90 --> 3098.70]  which is relationships.
[3099.26 --> 3103.74]  I was reading a research article recently and it talked about, you know,
[3103.78 --> 3109.88]  how couples who are together a really long time end up sort of looking like each other.
[3110.54 --> 3112.22]  Overhood, that's, yeah.
[3112.44 --> 3118.42]  And so what they've looked at is when we actually empathize with other people,
[3118.42 --> 3120.98]  facial expression is really key within that.
[3121.54 --> 3126.12]  And so when you empathize with the partner you're with over and over and over again,
[3126.12 --> 3130.36]  your face begins to make the same creases and facial expression
[3130.36 --> 3133.20]  as it relates to where somebody else is emotionally.
[3133.62 --> 3134.14]  Wow.
[3134.44 --> 3134.82]  Right?
[3135.46 --> 3136.02]  Say it is.
[3136.10 --> 3137.00]  So that's creepy.
[3137.00 --> 3145.74]  Well, again, this is sort of the hotbed when it comes to neuroscience these days is mirror neurons.
[3146.46 --> 3149.98]  And these mirror neurons are what are involved with empathy.
[3150.28 --> 3155.20]  And so mirroring, meaning I get another person's emotional world.
[3155.20 --> 3160.10]  And so one of the research studies looked at Botox.
[3160.74 --> 3168.38]  And what they found is that Botox, because it actually assists in paralyzing facial muscles.
[3168.50 --> 3168.80]  Right.
[3168.92 --> 3172.00]  But then you can't contort your face so you don't get wrinkles.
[3172.50 --> 3175.20]  But actually levels of empathy go down.
[3175.86 --> 3176.40]  Uh-uh.
[3177.04 --> 3177.66]  Right.
[3177.84 --> 3180.58]  Because your physical appearance can't reflect your inner appearance.
[3181.06 --> 3182.58]  Yeah, you got it.
[3182.58 --> 3189.28]  And so when you're working in these remote locations, it might facilitate better work or more focus.
[3189.38 --> 3195.54]  And it allows people to be distributed and to capitalize on the talents across the country, right?
[3195.98 --> 3196.42]  Yeah.
[3196.66 --> 3196.98]  Wow.
[3197.12 --> 3199.54]  So see, that's like a treasure trove, in my opinion.
[3200.04 --> 3205.22]  Talking about in a scientific way, you know, not just like, hey, this is my opinion.
[3205.34 --> 3205.78]  Yeah.
[3205.78 --> 3207.42]  About all the cons of that.
[3207.80 --> 3212.36]  Because I think what we can do is still have remote work, but do it in more healthy ways.
[3212.58 --> 3217.40]  Because I'm fully, I mean, I've been self-employed remote worker since 2006.
[3218.10 --> 3219.18]  Now I'm a unique animal.
[3219.58 --> 3220.72]  I know that.
[3220.82 --> 3221.86]  My wife knows that.
[3222.06 --> 3222.50]  Right.
[3222.54 --> 3223.40]  And I'm fine with it.
[3223.68 --> 3225.70]  I'm a good human being, but I've got some flaws.
[3225.88 --> 3228.68]  And I'm willing to accept and share those to some degree.
[3228.68 --> 3237.04]  And I think the problem is we just lack maybe a more purposeful or intentional feedback loop.
[3237.14 --> 3237.52]  Yeah.
[3237.68 --> 3243.80]  Which I think is super important to being able to operate in this world in just good ways.
[3243.90 --> 3248.56]  I don't know, healthy ways is probably the best way to use in this show context is healthy ways.
[3248.56 --> 3253.16]  One of the things that's fundamental, I would say, to being human is change.
[3253.78 --> 3253.96]  Right?
[3254.08 --> 3260.14]  And so sometimes people come in and are really key in our life for a period of time.
[3260.14 --> 3261.18]  And then things change.
[3261.18 --> 3265.44]  Either we grow or they grow or they change in a different direction.
[3265.44 --> 3270.98]  And then the relationship changes or that feedback loop gets modified in some way.
[3271.38 --> 3272.84]  That isn't always a bad thing.
[3272.84 --> 3281.54]  It's just going, my sense of choice actually is a critical component when it comes to feeling good about my life.
[3281.66 --> 3285.62]  If I feel like everything is sort of outside of me and I don't have any charge over it,
[3285.62 --> 3293.82]  like I didn't choose to work in a more remote location or I didn't choose to go to school or I didn't choose this person,
[3294.12 --> 3301.02]  then it feels far more oppressive as opposed to I actually participated in the outcome that I'm actually experiencing.
[3301.02 --> 3306.36]  So I then also have more charge over whether or not I want to change it.
[3307.18 --> 3314.80]  I think this feedback loop process that we're talking about here is super common to developers.
[3315.44 --> 3323.04]  You know, from people who write code to people who plan and to engineer and to manage and lead.
[3323.30 --> 3327.06]  Like there's no one in the software process that doesn't understand the feedback loop.
[3327.06 --> 3332.68]  And the reason why is because in product development, they have this concept of agile.
[3333.32 --> 3348.08]  And basically it means you produce something, you put it out there and you expect the feedback loop to happen in order to gain insights and course correction to then release another version of it that continually and iteratively becomes more and more improved.
[3348.08 --> 3352.92]  So this whole process in day-to-day work in software is normal.
[3353.42 --> 3361.52]  And I think it's interesting how we're going to apply to their lives and people's lives, you know, to take the same importance of a feedback loop, for example, and apply it.
[3361.88 --> 3362.00]  Right.
[3362.18 --> 3370.08]  Well, so this is very much how it goes in relationship, which is why there is an importance when it comes to sort of things resonating.
[3370.08 --> 3376.92]  You ever walk into a room or an interaction with a couple other people and like something just feels wonky or off?
[3377.26 --> 3380.02]  You're like, I can't put my finger on it.
[3380.14 --> 3381.22]  Definitely been there.
[3381.74 --> 3382.34]  Right.
[3382.96 --> 3395.30]  Well, and so to be able to identify that in relationships and even go, wow, I need to, I'm experiencing this person in my world with the limited interactions that I have with them.
[3395.30 --> 3397.54]  It hasn't really resonated with me.
[3397.76 --> 3399.58]  And so I don't get good feedback.
[3399.96 --> 3405.40]  So now I'm going to be more defensive because I feel as though there's a threat.
[3405.56 --> 3407.80]  It doesn't necessarily mean the person is threatening.
[3407.96 --> 3411.32]  However, my brain is going to tell me, hey, we need to be more protective.
[3411.74 --> 3416.06]  We need to do some strategies so that you're not fully exposed.
[3416.06 --> 3431.88]  You know, one way I look at scenarios like this, I would say as of late is because if you ever watched a TV show or a movie where the, you know, the narration, the storytelling part of it, they expose a character in a certain light.
[3432.10 --> 3434.36]  And you may dislike that.
[3434.44 --> 3435.96]  They may be a villain or villainess.
[3436.22 --> 3436.46]  Right.
[3436.80 --> 3437.14]  Sure.
[3437.14 --> 3449.16]  But the moment they turn the story to their backstory and why they are the way they are or why they're acting the way they're acting, you then kind of fall in love with them and you're almost rooting for them.
[3449.30 --> 3449.60]  Right.
[3449.60 --> 3468.58]  I feel like that's the same thing that happens day to day to our lives is that, you know, there are people who seem villainous or not for us, but we don't understand their backstory and why they are the way they are for us to have and employ that empathy that's required to have this, this dance, as you say, this iteration of relationship.
[3469.22 --> 3476.14]  You know, we, we just assume they are who they are and we project, you know, our worst fears onto them and they become true.
[3476.14 --> 3478.46]  Yes, you got it.
[3478.54 --> 3490.58]  This is why in the absence of, you know, a face, I don't really get to engage with people in the same sort of humanness that we are all in.
[3491.02 --> 3492.64]  And so you're exactly right.
[3492.74 --> 3498.84]  I mean, over and over and over again, because you can identify and go, oh, that's why they're harsh.
[3498.84 --> 3507.86]  Or, you know, I recently had an interaction I had shared with someone that I, I was a competitive gymnastics coach for a number of years.
[3507.86 --> 3518.28]  And so somebody thought that my response to them when they were really struggling was kind of harsh, but they remembered that I had told them I was a coach for so long.
[3518.28 --> 3522.30]  And they're like, oh, this is just another side of her coming out.
[3522.42 --> 3522.72]  Right.
[3522.72 --> 3525.88]  And I'm not sure I prefer it, but I get it.
[3525.88 --> 3531.20]  And then it switched for their reaction because then they're like, oh, wait, we're on the same team.
[3532.02 --> 3535.84]  She's not trying to like oppress me or fight back against me.
[3535.92 --> 3539.44]  She actually is helping me, trying to get me to where I want to go.
[3539.90 --> 3542.60]  My wife and I, we've learned this, this concept of goodwill.
[3542.98 --> 3543.42]  Right.
[3543.58 --> 3543.82]  Yeah.
[3543.82 --> 3548.94]  I can take your feedback or your criticisms in a different light.
[3549.04 --> 3552.20]  If, if I know that you have goodwill for me.
[3552.24 --> 3552.64]  Yep.
[3552.84 --> 3556.86]  Meaning that you're not trying to harm me, that you are for me, not against me.
[3556.86 --> 3560.76]  And sometimes change, as we all know, is painful and can be painful.
[3560.76 --> 3567.14]  So sometimes the necessary feedback and or criticism that can influence that change can also be painful.
[3567.14 --> 3575.80]  But I can accept it differently if I know that she or they or whomever is in the scenario with me has goodwill for me.
[3576.08 --> 3580.32]  You know, whereas if you know that they're not for you, then you obviously take it a whole different way.
[3580.38 --> 3582.78]  And that's, that's an okay thing.
[3582.78 --> 3590.60]  But we often are, you know, in relationship with people that are giving us crucial feedback and we need to have that kind of, that lens.
[3590.68 --> 3595.62]  Like it was significant in our marriage to understand, hey, I know there are times when you give me feedback.
[3595.62 --> 3599.80]  I am not happy about it, but, but I know you have goodwill for me.
[3599.86 --> 3602.06]  So therefore I calm down.
[3602.06 --> 3603.00]  I listen.
[3604.06 --> 3612.62]  I, you know, I take that in and I process it, whatever, but I take it in a different way because I know that she's for me and not against me.
[3612.78 --> 3613.26]  Yep.
[3613.56 --> 3634.30]  One of the key things when it comes to change is a sense of openness and even relationally, like of going, I need to be able to see some, how somebody else responds or how they're feeling as based on their perspective of what they're going through and not just my perspective of their perspective.
[3634.30 --> 3642.44]  And so this goodwill is like, I believe that we're on the same side and that you're not trying to make it harder for me.
[3642.56 --> 3649.08]  But so I can understand if I were sitting where you were sitting, had the background that you had, why you would have taken it in that way.
[3649.08 --> 3656.62]  And then I can provide an opportunity to clarify or create more connection, even when it doesn't feel good.
[3656.62 --> 3663.02]  And I, I honestly think this is so much of what's missing in people's relationships.
[3663.02 --> 3683.80]  If I look at relational interactions through, uh, the notion of conditioning, wherein I get a sort of hit of dopamine, feel good feelings, because I went to a person, I had a conversation that didn't necessarily feel good, but there was openness on both parties to hear one another's perspective.
[3683.80 --> 3692.04]  That it actually then reinforces like, oh, when I go and I have this exchange with people, I feel better.
[3692.68 --> 3702.46]  So now I'm going to go and engage with other people and get the feedback, even if I might not like the feedback, because now I'm buffered and I'm not alone in this.
[3702.46 --> 3704.76]  And I, somebody else sees my world.
[3706.88 --> 3708.88]  That's a preview of brain science.
[3708.88 --> 3716.44]  If you love where we're going with this, send us an email to get on the list, to be notified the very moment this show gets released.
[3716.78 --> 3724.60]  Email us at editors at changelog.com in the subject line, put in all caps, brain science with a couple bangs.
[3724.60 --> 3730.24]  If you're really excited, you can also subscribe to our master feed to get all of our shows in one single feed.
[3730.24 --> 3736.16]  Head to changelog.com slash master or search in your podcast app for change law master.
[3736.16 --> 3743.48]  You'll find it subscribe, get all of our shows and even those that only hit the master feed again, changelog.com slash master.
[3743.48 --> 3773.46]  Thank you.
[3773.48 --> 3774.00]  Thank you.
[3774.00 --> 3778.16]  Thank you.
[3778.16 --> 3779.00]  Bye-bye.
[3779.18 --> 3781.90]  Bye-bye.
[3781.90 --> 3782.56]  Bye-bye.
[3785.20 --> 3785.64]  Bye-bye.
[3788.36 --> 3790.68]  Bye-bye.
[3790.78 --> 3792.66]  Bye-bye.
[3792.66 --> 3822.64]  Thank you.
