[0.00 --> 5.44]  There's a lot of optimizations around the GPU spend. So the way that it's being backed up for
[5.44 --> 9.82]  the volume, we're doing like intelligent backups, I guess, where we can back up just the amount of
[9.82 --> 13.30]  volume that's actually being used. So you're not paying for unused volumes, even when your
[13.30 --> 17.66]  instance is off. There's auto stop, making sure that your instances aren't costing you a lot when
[17.66 --> 23.18]  you're not using them. You can use brev scale, which lets you deallocate the GPU or get a more
[23.18 --> 27.26]  powerful instance if you need it. So flexible compute needs without having to reset up or
[27.26 --> 31.54]  install anything. And there's the obvious benefit of not running a container locally if you're on a
[31.54 --> 34.18]  Mac that kind of like casually eats up like 20 gigs of RAM.
[44.98 --> 51.28]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[51.52 --> 57.24]  and accessible to everyone. Subscribe now if you haven't already. Head to practicalai.fm for all
[57.24 --> 63.06]  the ways. Special thanks to our partners at Fastly for delivering our shows super fast to wherever
[63.06 --> 70.16]  you listen. Check them out at fastly.com. And to our friends at fly.io. We deploy our app servers
[70.16 --> 83.36]  close to our users and you can too. Learn more at fly.io. Welcome to another episode of Practical AI.
[83.36 --> 89.94]  This is Daniel Whitenack. I'm a data scientist at SIL International. And I'm joined as always by my
[89.94 --> 95.08]  co-host Chris Benson, who is a tech strategist at Lockheed Martin. How are you doing, Chris?
[95.48 --> 102.52]  Doing good. Having a good 2023. And this is going to be the best year for artificial intelligence ever.
[103.24 --> 110.56]  Yeah. Well, I mean, it must be. Yeah, we finally did our chat GPT episode. And that was really cool
[110.56 --> 115.76]  because I don't know if you saw Chris's first episode where we had, I think, like over 10,000
[115.76 --> 121.64]  downloads in the first week. So thank you to our listeners. That's awesome to see that. We're glad
[121.64 --> 127.78]  that was useful. And we're going to keep the good content rolling right along because this week we've
[127.78 --> 134.78]  got something super practical, which I think everyone deals with what we'll talk about today. But we're
[134.78 --> 142.00]  privileged today to have with us Nader Khalil, who's the co-founder and CEO at brev.dev. Welcome.
[142.72 --> 143.94]  Hey, thank you. Thanks for having me.
[144.18 --> 153.38]  Yeah. So I alluded to like a problem that we all face, which is environment management. And like,
[153.90 --> 160.18]  I'm developing on this environment. I need to have these dependencies or I use this environment.
[160.18 --> 166.48]  Now I need a GPU or Chris is on my team and he needs to replicate my environment. All of these
[166.48 --> 172.48]  sorts of things, whatever, you know, category you put those in. So how, how I guess in terms of,
[173.00 --> 178.22]  you know, you're digging into this problem now, but how did you get there? What started you along
[178.22 --> 181.48]  this path of really thinking deeply about dev environments?
[181.88 --> 186.68]  Man, we've had quite a twist and turn of a journey to get here. And yeah, I mean, the ultimate goal is
[186.68 --> 191.02]  just monotonous machine problems getting in the way of creative development. And that's, it's funny.
[191.12 --> 195.20]  When I, I went to UC Santa Barbara, I studied electrical engineering and computer science.
[195.46 --> 199.62]  And when I moved to SF to work, I was actually building cloud dev environments at Workday.
[200.00 --> 205.68]  And I did that for two years. And in December, 2018, actually just before that, I was getting a
[205.68 --> 209.52]  beer with a bar owner and he was telling me how he had a thousand clicks on his Google ads,
[209.64 --> 213.56]  but his bar was empty other than me. And he shows me that his metrics on his Google ads,
[213.56 --> 217.68]  he goes, make it make sense. And I realized he had a really good point. Digital ads work really
[217.68 --> 221.54]  well for digital businesses because if someone clicks on an ad, that's an Amazon ad, you've
[221.54 --> 225.62]  entered Amazon storefront. There's nothing like that for the physical businesses like his.
[225.98 --> 230.92]  And so he's just using a really bad medium. So my co-founder and I kind of like same co-founder
[230.92 --> 235.94]  with Brev, we pretty much realized there was like a way for us to backdoor the Uber app. And so we put
[235.94 --> 241.64]  tablets and Ubers and Lyfts and we let local businesses advertise on them. And if you tapped our screen,
[241.64 --> 246.90]  we would reroute your Uber to that location. Yeah, that's legit. Yeah. Yeah. You go out with
[246.90 --> 250.78]  friends for drinks. You see, buy one, get one free margaritas. You tap the screen and we take you
[250.78 --> 255.44]  there. You get a free drink. Our owner knows his ad work. The driver got a tip. Everyone won.
[255.56 --> 259.48]  Perfect. And so that was really exciting. I ended up, that's what I quit my job to go do. We did that
[259.48 --> 264.00]  for like two years, completely bootstrapped. We like ran out of money. I poured my 401k into it.
[264.26 --> 270.06]  We got into YC for that. We got to like a quarter mil ARR. And essentially demo day was March 2020,
[270.06 --> 275.62]  which was right when the shelter in place happened in SF. And so we got to see our 400 cars go to seven
[275.62 --> 280.90]  overnight, right. Actually the week of demo day. So, um, we didn't raise a dime obviously, but
[280.90 --> 284.72]  Oh, I feel bad for laughing, but I can't help it. Yeah.
[285.86 --> 290.10]  Have you seen that gif on the internet of the raccoon with like cotton candy? And it's just like,
[290.14 --> 297.22]  where did it go? Um, that was like very much like March, 2020 for us. But, uh, it was funny because
[297.22 --> 301.00]  with a physical business, you have a physical fleet, right? We have physical operations.
[301.06 --> 305.26]  You imagine like physical hurdles being the hardest part of that. And in January, 2020,
[305.26 --> 311.26]  we're starting YC. We're like, we got to like 15 KMRR things are working and we need to just three,
[311.42 --> 316.54]  four X the fleet. And, uh, that was like really hard for us. We found out from one of our drivers
[316.54 --> 321.32]  that, uh, Uber and Lyft have these parking lots, half a mile from SFO airport where drivers go wait for
[321.32 --> 327.04]  these really valuable airport rides. So I go to the parking lot and Uber security kicks me out right away.
[327.04 --> 331.80]  They're like, I'm not a driver. So I'm like, okay, well I'm a leaser. So I went to a gas station.
[331.86 --> 335.44]  I bought cigarettes. I light one up and just walk back on the lot. Cause now I look like a driver
[335.44 --> 340.64]  taking a smoke break. And I got right past Uber security. I'm on this lot to like 4 AM talking to
[340.64 --> 345.66]  every driver. We four X our fleet that night. So like there was never a physical hurdle that got in
[345.66 --> 351.08]  our way. But once we got those drivers live, everything else went to we had like our advertiser
[351.08 --> 356.76]  dashboards really slow. Like all these random problems. One of them was like the ads when they flipped on
[356.76 --> 361.22]  our tablets would just disappear and flash white. And if that happened at night, it's jarring.
[361.34 --> 365.34]  And so riders would turn off the screen and you lose revenue for the night. And so it was really
[365.34 --> 370.80]  funny having like really weird physical problems, but like we can sneak past Uber security and solve
[370.80 --> 375.12]  those. But like, no, when we have to like sit at our computers and fix something, it's like our dev
[375.12 --> 380.54]  environment slowing us down. And so it was almost like instantly when my co-founder and I, like when
[380.54 --> 386.14]  essentially the pandemic killed that business, my co-founder and I look at each other. And those 20 days of
[386.14 --> 389.46]  January where we were trying to deal with our dev environment issues, we couldn't replicate these
[389.46 --> 393.28]  issues locally. Just so many weird, bizarre issues. We're just like shooting in the dark.
[393.80 --> 397.38]  That was the only time with that business. I had like a pit feeling in my stomach. Like we
[397.38 --> 402.52]  forgotten assignment or something. And so we used immediately, how do we solve our previous problems?
[402.52 --> 408.22]  And so we spent like a year and a half in pivot land with a good North star. We built a very heavy
[408.22 --> 412.88]  abstraction, I guess. It was kind of like what Replit is now at the time Replit didn't have databases,
[412.88 --> 417.40]  so you couldn't really build applications in it. So we had this, we essentially said, Hey,
[417.52 --> 421.94]  if we force our dev environment opinions on you, you can't have problems we didn't already know
[421.94 --> 426.00]  about because we forced your decisions. And so you wouldn't have problems. It'd be a really smooth
[426.00 --> 430.30]  experience as long as you did everything that we supported. And so you get cron jobs out of the box
[430.30 --> 434.20]  and Twilio was already hooked up and a database was already there, but you have to use our version of
[434.20 --> 439.38]  Python for your APIs, things like that. And so it was an interesting experience in like the broader,
[439.38 --> 443.88]  like everything outside of a dev environment, when you need to start using, when you want to run
[443.88 --> 448.02]  tests and you need more tooling and those things aren't supported. So it was a great way to like
[448.02 --> 453.28]  plunge into the space, but ultimately we learned that a good abstraction is only good if it pairs
[453.28 --> 456.84]  well with the problem that's solving. And if you're good at solving problems, you're going to have new
[456.84 --> 460.80]  ones to solve, which means you'll need new abstractions or a flexible abstraction. And so that's when we
[460.80 --> 463.90]  kind of pivoted away from that and built like the current version of bread.
[463.90 --> 470.12]  And a lot of what you've described, I mean, I've never tried to sneak tablets on an Uber or something
[470.12 --> 475.64]  like that, which sounds like a really fun thing to try to do. And I love, I love that story.
[475.96 --> 483.06]  Probably a less fun thing for me in my life is like the general like arena of the very kind of
[483.06 --> 490.48]  specialized and weird dependency issues specifically related to like machine learning and AI sorts of
[490.48 --> 496.98]  environments and the differences that people have between like trying to prototype something
[496.98 --> 503.12]  locally and then trying to scale it out in a reasonable way. Did that factor into your thinking
[503.12 --> 508.20]  when you were building this in terms of like these like data science people out here, this like
[508.20 --> 514.44]  explosion of AI tooling and all of that? Or was that something that came along the way as you were kind
[514.44 --> 518.96]  of going in this journey and thinking about like what kind of problems these abstractions were
[518.96 --> 523.24]  thinking about what kind of problems these solved? Yeah. So it's definitely something that we learned
[523.24 --> 527.94]  along the way. We initially started by trying to solve our own problem. We at Bread exclusively use
[527.94 --> 531.44]  Bread for all of our own development. It's just a much kind of to your point, right? You're not
[531.44 --> 535.28]  dealing with environment issues. We upgraded, we have a blog post about when we upgraded from Golang
[535.28 --> 541.56]  version 1.17 to 18, it caused a memory leak, but our co-founder fixed it, his environment. And so when I
[541.56 --> 545.54]  wanted to update my environment, I just reset and I'm on the latest. And so being able to just
[545.54 --> 551.30]  move your environment that way, it is really, it makes everything a lot easier. What we've learned
[551.30 --> 555.70]  is that some of our power users were AI developers because AI dev environments are really complicated.
[556.06 --> 560.48]  And they specifically asked us to support GPUs. And when we started to support GPU instance types,
[560.62 --> 565.64]  it just kind of opened our eyes to how many, I guess there's kind of raw DevOps problems there are
[565.64 --> 571.44]  within the MLOps space. You know, GPUs are really expensive. A lot of times the GPU is sitting idle.
[571.44 --> 575.58]  If you need to do some sort of development, you might spin up a GPU just because there's the
[575.58 --> 579.76]  off chance you do some GPU development right now, but a CPU would have sufficed. So the way
[579.76 --> 583.48]  Brev works is it's, the idea is you can move your dev environment between different instances.
[583.70 --> 588.04]  So you can, if you're not using the GPU, deallocate it and just go to a really cheap
[588.04 --> 593.04]  pennies per hour CPU instance. And only when you need the GPU, do you turn it on. We also have
[593.04 --> 597.26]  auto-stop. So I learned from Workday, they were burning a lot of money every month because
[597.26 --> 601.56]  developers forgot to shut these instances off. This also happens from individual developers.
[601.76 --> 605.68]  So if you don't use your Brev instance, we'll automatically power it down. You can start it
[605.68 --> 610.66]  again from the CLI and it's just, and it's back up and running. So Brev is a CLI that makes it really
[610.66 --> 614.20]  easy to spin up these dev environments and we connect your local tools to that remote instance.
[614.52 --> 620.38]  So we kind of, the CLI wraps SSH. So all you have to do is run Brev start and start coding and not
[620.38 --> 622.28]  really have to worry about the actual like environment issue.
[622.28 --> 628.40]  That sounds really cool. Let me ask you a kind of a baseline question that is I'm learning about
[628.40 --> 632.90]  how you've done this, but I'm starting kind of from where I'm coming from and probably where more
[632.90 --> 638.62]  than a few of our listeners have, like I'm used to, you know, using Docker and, you know, getting in a
[638.62 --> 644.26]  container and it has, you know, access to an NVIDIA GPU, kind of the way a lot of folks are doing it.
[644.62 --> 648.76]  Can you kind of tell us a little bit about what the difference is between that kind of that
[648.76 --> 654.34]  classical approach that a lot of people use and in what ways are you differentiating and stepping up
[654.34 --> 656.60]  from, from that into Brev.dev?
[657.18 --> 661.10]  Yeah. And can you explain to me maybe like how, where are you running this container? How are you
[661.10 --> 664.64]  running this on your machine? It has the NVIDIA GPUs. Yeah.
[665.12 --> 670.18]  You have to have a set of images that you have, you know, set up. There's a bunch of configuration
[670.18 --> 676.06]  ahead of time, which I know I don't have to do on yours, but essentially I'm having to say,
[676.06 --> 682.14]  okay, I have a GPU available in some place on the network or maybe in the cloud and I'm going to
[682.14 --> 687.22]  do those configurations. And then maybe I'm on my laptop, maybe I'm on a server, but a lot of people
[687.22 --> 692.38]  are, you know, logging into containers to do the work and then trying to move the container around
[692.38 --> 698.44]  and be able to access those resources from different locations. I know that I'm starting
[698.44 --> 703.04]  from that because it has some good things, but it also has some real pain in the butt aspects to it
[703.04 --> 707.20]  in terms of having to make it all work. And so I'm kind of wanting, it sounds like what you're
[707.20 --> 713.06]  describing upfront is a really good user experience. And so I'm trying to get a sense of like what the
[713.06 --> 714.08]  differences are in the two.
[714.70 --> 719.54]  Yeah. So I think at a minimum, if you want to just run a Brev environment with or without a container,
[719.90 --> 724.18]  whether or not you have that set up, the way we kind of handle this is with a simple bash script,
[724.26 --> 728.80]  knowing that every Brev environment is running the same version of Ubuntu. We have the specific
[728.80 --> 733.92]  version listed in our docs, running a bash script is bash is ubiquitous. It's available. You can make,
[734.06 --> 737.90]  um, and you can run anything on it. So, uh, or you can install anything with it rather. So you can
[737.90 --> 741.34]  start with just a bash script. If you don't want to run a container, if you just want to like try
[741.34 --> 747.24]  something and have that run. So we leverage this a lot for some of our templates. If you have a bash
[747.24 --> 751.72]  script committed to your repo that has set up instructions, Brev can automatically run it when you
[751.72 --> 756.16]  spin up an instance. So you create a new environment, you give it the Git repo and the path to the
[756.16 --> 759.78]  script that you want it to run. And that script will get run immediately for you. When the instance
[759.78 --> 764.86]  is created, the user experience is creating the new environment, whether in the CLI or through the UI,
[765.22 --> 769.08]  setting the path to that setup script, or you can also just start with one of our templates.
[769.54 --> 773.52]  And then from your terminal, you run Brev open and we'll open up VS code connected to the remote
[773.52 --> 778.94]  instance or Brev shell. If you, um, we support Vim, Emacs, JetBrains, whatever IDE it is that you want
[778.94 --> 783.78]  to use or a code editor. And then if you do have a containerized workflow, anything that you were
[783.78 --> 786.68]  going to run in your terminal, if you're going to run Docker compose commands, if you're going to
[786.68 --> 791.36]  run cog, if you're using replicate, anything that it is you're trying to run, you can just put in
[791.36 --> 794.76]  the bash script and know that that's going to reliably run for you or someone else that you're
[794.76 --> 799.52]  sharing this with. But I think the big thing here is there's a lot of optimizations around
[799.52 --> 804.86]  the GPU spend. So the way that it's being backed up for the volume, uh, we're doing like intelligent
[804.86 --> 808.86]  backups, I guess, where we can back up just the amount of volume that's actually being used.
[808.86 --> 813.20]  So you're not paying for unused volumes. Even when your instance is off, there's auto stop,
[813.26 --> 817.72]  making sure that your instances aren't costing you a lot when you're not using them. Uh, you can use
[817.72 --> 823.10]  brev scale, which lets you deallocate the GPU or get a more powerful instance if you need it.
[823.10 --> 827.46]  So flexible compute needs without having to reset up or install anything. And there's the obvious
[827.46 --> 831.88]  benefit of not running a container locally. If you're on a Mac that kind of like casually eats up
[831.88 --> 832.70]  like 20 gigs of Ram.
[832.70 --> 838.40]  I actually, um, so I haven't used it a lot. I have to be honest, but I did spin up a couple
[838.40 --> 843.88]  of environments in brev.dev, um, leading up to this conversation. Cause I wanted to understand
[843.88 --> 847.84]  a little bit more about it. And, um, it was really fun. Uh, like Chris was saying, like,
[848.06 --> 855.26]  I think it's true that the sort of dev and onboarding experiences is really nice. And I was using like
[855.26 --> 862.20]  the, um, UI configuration and the experience I had was that, and I don't know, I'm kind of curious,
[862.20 --> 867.84]  like what you've heard from other users, I guess is my question, because my experience was similar
[867.84 --> 873.28]  to like, okay, I created the dev environment, like with the UI, it's a little bit different UI than
[873.28 --> 877.70]  I'm used to, but there's like familiarity with certain of the things, right? I'm pointing it to a
[877.70 --> 883.14]  Git repo. I'm maybe defining, like you're saying, like a startup script or something like that.
[883.14 --> 888.14]  Um, I'm naming it. Okay. It's creating this thing. I add a GPU, whatever there's similarities
[888.14 --> 893.60]  between that and like what I would create in an instance in the cloud. But then I have this dev
[893.60 --> 899.22]  environment. And I think the point where like something switched in my brain was I was, you
[899.22 --> 907.60]  know, local in my terminal and I, uh, I actually even forget the command now, but like brev, brev open
[907.60 --> 912.78]  the environment name. That's what it was brev open. And it, it just popped up VS code.
[913.14 --> 919.96]  And then I realized like I had my VS code open and I could open like a terminal VS code, but that
[919.96 --> 925.54]  was running in the environment that I created remotely. So that's where like things switched
[925.54 --> 930.22]  in my brain. Like, Oh, I'm now using that environment that I set up and I could share
[930.22 --> 934.28]  that environment with someone else. And then they could pop open their code editor and see this.
[934.40 --> 939.50]  I'm curious, other people that you've talked to people that have started using it, where are those
[939.50 --> 945.10]  light bulbs going off for them? And what are the things that they're really like getting excited
[945.10 --> 945.74]  about? I guess.
[945.74 --> 950.04]  I mean, I just did a slew of user interviews. And, uh, the first question I always ask is what
[950.04 --> 955.06]  does brev do? It's always really exciting to hear that from someone before I have a opportunity to like
[955.06 --> 960.10]  kind of accidentally influence that conversation. And the biggest things we hear is that brev is the
[960.10 --> 965.42]  most delightful or easiest experience to run anything on a GPU in the cloud. So that's been a lot of our
[965.42 --> 969.10]  focus is, you know, dev environments are, uh, kind of the thing that gets in the way of what you're
[969.10 --> 973.48]  trying to do. And so that's been our focus from the beginning, but, uh, there's a lot more
[973.48 --> 979.32]  complicated workflows, especially with AI and just the, the dramatic cost. Like we have one user
[979.32 --> 986.04]  whose Google cloud bill was like, uh, about $280 with, uh, just running on their GPU instance.
[986.04 --> 990.20]  But with something like brev scale, they brought it down to about 25 bucks. I think their exact thing was
[990.20 --> 995.06]  like 27 or something dollars. And so that's like a, you know, 10 X reduced, uh, cost just because
[995.06 --> 999.34]  that GPU was sitting idle while they were like actively coding and building things. So I think
[999.34 --> 1003.46]  our goal is just to have something that is a much more delightful and really simple experience,
[1003.46 --> 1007.06]  but also saving a lot of money. A lot of what we're focused on right now is integrating with
[1007.06 --> 1011.98]  other clouds. You know, we to get this far have been just been built on AWS, but we're, uh, partnering
[1011.98 --> 1016.58]  with like Lambda labs right now to support their GPU instances because they're a third of the cost.
[1016.58 --> 1021.30]  And we're leaning deeper into actually a container strategy, which will let us provide kind of like
[1021.30 --> 1025.94]  start and stop across clouds, which I think will be really exciting. So this is something that's,
[1025.94 --> 1030.50]  we're getting ready to release over the next two weeks. Uh, and I'm going to start kind of talking
[1030.50 --> 1035.22]  a bit more about, but actually I was just gonna say, you can go ahead if you want to dive a little
[1035.22 --> 1039.70]  bit into that right now, cause I, you really piqued my interest with that. So if you don't tell me now,
[1039.70 --> 1044.90]  I'm going to pester you later. Yeah. Well, um, the way that we're approaching it,
[1044.90 --> 1049.22]  I think is we're going to, and it's a bit experimental still right now, but we'll have something out within two
[1049.22 --> 1053.38]  weeks. Our team has pretty quick velocity. We're a small, but potent and passionate team.
[1053.38 --> 1057.94]  And so we really want to be able to support start and stop across any, uh, anywhere that
[1057.94 --> 1061.14]  there's a GPU available for us in the cloud. And it might not be at a large data center.
[1061.14 --> 1064.98]  It might be at a small one and that's okay. Uh, if it's a cheap GPU, that's in a region,
[1064.98 --> 1068.26]  that's not going to introduce a lot of latency for you. You should be able to leverage it when,
[1068.26 --> 1072.82]  while we have access to it. And if it's rugged from us, if we have, if you stop your instance,
[1072.82 --> 1076.18]  you should be able to start it again. And it might not be on the same instance in the same data
[1076.18 --> 1079.14]  center, but that's okay. We're really just trying to optimize on, you know,
[1079.14 --> 1084.26]  GPU itself, a GPU is a commodity. It's like, you just want the cheapest one and you want to be able
[1084.26 --> 1088.50]  to run your code on it easily. And so that's, yeah. In like two weeks, I think we'll have a
[1088.50 --> 1092.58]  pretty exciting launch on that. That sounds pretty cool. So there's another aspect of that. That's
[1092.58 --> 1098.34]  got me thinking with you looking at multi-cloud and, and you kind of said it could be a small
[1098.34 --> 1101.86]  data center. It could be, uh, you know, I'm getting the impression there can be a lot of diversity
[1101.86 --> 1106.82]  potentially in what you're targeting for getting your GPU. What are some of the kind of
[1106.82 --> 1113.38]  considerations somebody might have for if they're using a brev.dev, like how might they decide and,
[1113.38 --> 1120.02]  and is there any strategy yet other than just kind of whimsical on saying, Hey, I want to go with this
[1120.02 --> 1124.50]  one or that one versus, is it just a cost thing or could there be other considerations that you guys
[1124.50 --> 1129.14]  have thought about in terms of being able to provide, you know, like going to a small data center
[1129.14 --> 1135.30]  here at this company, rather than the big AWS one in Northern Virginia over here. Uh, any thinking around that?
[1135.30 --> 1139.70]  Yeah. So, uh, just to clarify on the kind of whimsical approach, are you talking for us,
[1139.70 --> 1142.18]  uh, as we have tried to find GPUs that we can offer?
[1142.18 --> 1146.50]  No, for the user perspective, because I, if I'm, am I correct in thinking they can
[1146.50 --> 1150.18]  kind of choose where to target on that, or is it something you're doing behind the scenes?
[1150.18 --> 1155.62]  Our goal is to make it really easy, but expose as many options to a user as they want. So for example,
[1155.62 --> 1159.86]  we'll default right now to a region that makes sense, but you can always open up the region and pick one
[1159.86 --> 1164.50]  that you would like. Um, again, right now we're only working with AWS, but that'll change really
[1164.50 --> 1168.82]  quickly, like in these next two weeks. Um, so we always want to make it an option for a user to
[1168.82 --> 1172.58]  see transparently where their instance is coming from. There's, I don't think reason for us to hide
[1172.58 --> 1176.98]  that. However, we do have an option for you right now to connect your AWS account. And what I've noticed
[1176.98 --> 1182.10]  is only like two users have bought like two individual users, not teams have used that. And I think what
[1182.10 --> 1188.02]  that means to me is the specific location of the GPU doesn't really matter. It's just like, Hey, I want to run
[1188.02 --> 1194.10]  this on an A100. Go run this on an A100. Gotcha. So one of the things that is sort of a question
[1194.10 --> 1198.42]  running through my mind is I thought it was really powerful. Like when I opened up the environment,
[1198.42 --> 1203.06]  I had the environment, I could run stable diffusion or whatever, because I had a GPU in the background.
[1203.06 --> 1208.26]  I had enough memory, like all of those things. That's really nice. And I could see how that would allow
[1208.26 --> 1214.18]  me to sort of understand the environment that I'm like eventually building towards in terms of what I
[1214.18 --> 1219.54]  want to release in production. And I could share that environment with other people. What would be
[1219.54 --> 1228.74]  like from your perspective as both the founder and creator, but also a user of Brev? What is like the
[1228.74 --> 1234.74]  workflow that you've seen work in terms of going from that local dev and sharing local dev environments
[1234.74 --> 1239.78]  with other team members towards like something you would run in the same type of environment
[1239.78 --> 1247.86]  in production? Like, okay, I've now used a Brev environment to like figure out how to run this,
[1247.86 --> 1255.38]  you know, fast API code that serves my model or something like that. And now I want to run the same
[1255.38 --> 1261.38]  type of environment, but I want to deploy that in my AWS or something like how, how did that work? And
[1261.38 --> 1266.66]  how does like Brev, you know, factor into that, I guess? Yeah. So it's really funny, right? Think about how
[1266.66 --> 1270.50]  many times you have to kind of do like the same redundant work and all of this being like not the
[1270.50 --> 1274.34]  thing you're trying to actually build. So you go and install everything so you can work on the dev
[1274.34 --> 1277.78]  environment. Then you go and install everything so you can go run, run your tests. If you have a
[1277.78 --> 1281.62]  pipeline, then you go and install everything so that you can deploy everything in production. And
[1281.62 --> 1286.66]  like theoretically we've already done this. And so I'm good friends with the team at banana.dev. We,
[1286.66 --> 1290.58]  we love working together. I think our products are both very synergistic and something that we're
[1290.58 --> 1295.70]  working on is if somebody has a Brev environment, they should be able to click a button and it deploys on
[1295.70 --> 1300.90]  banana. Um, it's a serverless GPU for production, right? That's, that's the helpful way to look at
[1300.90 --> 1305.22]  this is, uh, there's two types of compute. There's interactive compute and non-interactive compute. If
[1305.22 --> 1310.26]  you're deployed on production, um, that's a non-interactive compute, right? Your API is up and running. You don't
[1310.26 --> 1314.50]  need an active shell into it. And in fact, that might even be an anti-pattern. If you have interactive
[1314.50 --> 1318.58]  compute, you're actively developing, you're open in the terminal, you're, you're running things and seeing it
[1318.58 --> 1324.74]  live and making iterations to it. And so, um, if you look at Brev and banana, for example, as like interactive and
[1324.74 --> 1328.90]  non-interactive computes that are very, that work really well together, you can take your
[1328.90 --> 1333.54]  interactive dev environment on Brev, get things running. And once you're done, press a button,
[1333.54 --> 1338.42]  move it to banana so that it's non-interactive. It's not costing you as much. It's just, it's on
[1338.42 --> 1343.46]  the serverless model. And then if you have a server error, right, if you have some, so you get some sort
[1343.46 --> 1349.22]  of century log on your, uh, banana server, then you should be able to click a button and then open it
[1349.22 --> 1354.34]  up in Brev and interactive compute. So you can figure out what's wrong, fix it and send it back. And if
[1354.34 --> 1359.06]  you're able to have that kind of workflow, you're taking away a lot of this, like DevOps overhead,
[1359.06 --> 1362.90]  because at the end of the day, we're just trying to build that's, um, I think that's where I see
[1362.90 --> 1367.86]  the future kind of heading is how smooth can we kind of nap, like move between the states that the
[1367.86 --> 1373.94]  user, uh, essentially wants. Yeah. I, I think that's a really, uh, insightful sort of direction
[1373.94 --> 1379.30]  because I see this efficiency gain with Brev and sharing environments for that, like interactive
[1379.30 --> 1385.06]  compute. That's really important. But then if you can make that connection to the sort of production
[1385.06 --> 1392.26]  deploy, that's huge because now like there's still so much, so much of the time, there's this friction
[1392.26 --> 1397.14]  that you talked about where like, even if I'm developing against like a cloud instance, right,
[1397.14 --> 1403.96]  there's some sort of like non negligible labor costs of like me going through the headache of
[1403.96 --> 1409.96]  going and, you know, deploying something to production and it's still not the same, right?
[1409.96 --> 1414.60]  Or there's some issue like you were talking about when things go wrong and there's debugging. So if you
[1414.60 --> 1419.96]  can replicate that environment, both in an interactive and non-interactive way, I personally
[1419.96 --> 1427.48]  think that's really, really powerful and interesting. Um, I think actually, uh, just a note, I think we've got,
[1427.48 --> 1433.56]  uh, scheduled to have the, an interview with banana coming upcoming. So listeners, uh, watch out for that one.
[1433.56 --> 1438.52]  I'm excited about that. Really exciting product. And I just, I think a really, really exciting space
[1438.52 --> 1443.96]  of just like the ML AI operation, like ops dev tooling coming out right now. Um, yeah, definitely
[1443.96 --> 1447.40]  really excited. And to kind of take what you said even a step further, like, you know, you might be
[1447.40 --> 1451.64]  reading a research paper and you see a Google Colab notebook that has a model and you want to go take
[1451.64 --> 1455.00]  it, fine tune it for your own sale, uh, for your own, you know, whatever you want to do with it.
[1455.00 --> 1461.00]  And then you go ahead and deploy it. And I mean, Rev is kind of in the center, uh, of like interactive
[1461.00 --> 1465.48]  compute where we could take a Google, if we have an import tool for Colab notebooks, where you can
[1465.48 --> 1468.76]  kind of import it on Rev, change the compute that you want, get something more powerful,
[1468.76 --> 1472.92]  fine tune it the way you'd like, um, maybe even use a template for API framework. So you get like
[1472.92 --> 1478.76]  flask APIs, uh, set up already for you. You can kind of continue to modify from there and then hit
[1478.76 --> 1483.96]  the production button and go to banana. That's kind of like the dream workflow. I see where we're behind
[1483.96 --> 1487.80]  the scenes, always finding the cheapest GPU for you to do that. You're able to get as powerful of a
[1487.80 --> 1492.28]  compute needs as you need. It's really simple to go from like Colab to something scaffolded with
[1492.28 --> 1495.88]  like APIs that are ready for you to deploy to production. Um, and again, we just get to focus
[1495.88 --> 1502.04]  on the fun part. All right. So, um, Nader, I'm looking through the templates that you have at, uh,
[1502.04 --> 1507.88]  brev.dev and, you know, just to give people a sense of like some of the things that you can kind of
[1507.88 --> 1513.24]  spin up an environment quickly, get and do right away. Um, I see a couple of different stable
[1513.24 --> 1519.64]  diffusion, stable diffusion, stable diffusion version two dream booth, TensorFlow, whisper clip,
[1519.64 --> 1525.00]  image captioning, all sorts of different things. But then there's, you know, environments that you
[1525.00 --> 1531.72]  have templated out for things like go and rust and, you know, other environments that people might be
[1531.72 --> 1537.64]  interested in. Um, you already alluded to the fact that you're a quickly moving, you know, small team.
[1537.64 --> 1545.16]  And I'm wondering like out of all the sort of like areas that, you know, you could focus on,
[1545.16 --> 1551.40]  it's probably one of the things I would guess is it's maybe difficult to position this for a certain
[1551.96 --> 1555.64]  group of people that really need it. Cause it's kind of a common need across,
[1556.20 --> 1561.96]  you know, all dev environments. So I'm wondering how you, uh, it seems like you've kind of brought
[1561.96 --> 1568.60]  some focus to the area of GPUs and data science, AI type of workflows specifically. Do you think
[1568.60 --> 1574.04]  that's mostly been driven by this sort of GPU element and the complexity of those environments?
[1574.04 --> 1581.24]  Or how do you think about like where to head from here in terms of like the verticals and the
[1581.24 --> 1587.16]  industries and the specific dev workflows that you're thinking about and you're focusing on and, um,
[1587.16 --> 1590.44]  how is that working and what are you hearing from users in that respect?
[1590.44 --> 1595.40]  Yeah. So it's kind of funny before we, we leaned into the AI and the workflows pretty heavily.
[1595.40 --> 1600.12]  You, you, right. Right. It's a dev environments is like, who is your target audience? Uh, people
[1600.12 --> 1603.96]  who code, right. And that's kind of a very naive answer for a very early stage of the product.
[1603.96 --> 1609.00]  Um, I think what we learned is you really want to be able to solve someone's problem as quickly
[1609.00 --> 1612.68]  and acutely as possible and then get out of the way. And I think that's been a big change in direction
[1612.68 --> 1616.68]  for us. Even if you look at the, uh, like the way that the product onboards, you need to have
[1616.68 --> 1620.36]  the CLI so you can run brev open. So we used to say, oh, well, when you make an account,
[1620.36 --> 1623.56]  we'll tell you to install the CLI right there, but the user doesn't know yet why they want to
[1623.56 --> 1628.12]  install the CLI. They haven't, they haven't had expressed desire to open their dev environment yet.
[1628.12 --> 1631.56]  So the way that we changed it is it's just focused on getting your environment created.
[1631.56 --> 1635.88]  When your environment's created, then you see an open tab. When you click the open tab there,
[1635.88 --> 1640.68]  it tells you install the CLI because you haven't yet. And so that's, you know, the user says,
[1640.68 --> 1644.60]  I want a thing and then we can kind of show and not really impose. And so when we were thinking
[1644.60 --> 1649.00]  about like broadly dev environments, when we initially started this tool, uh, or when we
[1649.00 --> 1653.40]  initially started building brev, it felt like we, you know, someone says, Hey, my local environment
[1653.40 --> 1657.56]  is not working. And so we'd say, great, we can make one for you in the cloud. But now we're not
[1657.56 --> 1661.48]  just introducing brev as a tool to solve their environment issues. We're also introducing the
[1661.48 --> 1665.48]  cloud. It's a separate thing. And so in terms of like acutely solving the problem, we're not doing
[1665.48 --> 1671.00]  that. We're introducing the element of the cloud, which they have not yet expressed a desire for. And so what's
[1671.00 --> 1676.12]  great about the GPU use cases is we're meeting people where they are, which is in the cloud, right?
[1676.12 --> 1681.96]  They're saying, I am trying to access an A100 that does not exist on my MacBook Pro. And I want to
[1681.96 --> 1686.60]  get this running, right? So the cloud intention is coming from them, not us, right? And we're not kind
[1686.60 --> 1690.92]  of like sneakily trying to introduce something else that way we can get them to use brev. It's just meeting
[1690.92 --> 1694.84]  the user where they are making it in the issues with using a GPU in the cloud is that they're really
[1694.84 --> 1698.60]  expensive and they're really painful to get set up. And then of course, all the dev environment issues.
[1698.60 --> 1702.76]  And so that's been a really great focus for us. And we're leaning in as hard as possible to the
[1702.76 --> 1708.28]  MLOps tooling. The dev environment issues are much more severe here. It makes a lot more sense for,
[1709.88 --> 1714.76]  there's a lot more room for us to delight users by making a much better experience. And going back
[1714.76 --> 1719.40]  to that container strategy, if we can move between different clouds, we can also move between one
[1719.40 --> 1724.20]  local cloud, which is your actual computer. So I think the way that we kind of want to approach
[1724.68 --> 1728.52]  broader dev environments is you should be able to run something on your computer and then say,
[1728.92 --> 1734.44]  I now have a need for the cloud. I want double the RAM. I want a GPU. I want something. So you can
[1734.44 --> 1738.84]  start local and then move it to a cloud. And that's the way that I think we can ultimately
[1738.84 --> 1743.80]  broaden from ML dev environments. But this is a huge focus for us right now. And what I really want to do
[1743.80 --> 1748.92]  is rather than think about so many of those other use cases, how do we get really tight integration with
[1748.92 --> 1753.96]  banana? How do we get a really easy way to go from a collab notebook to something that you're now fine
[1753.96 --> 1759.24]  tuning on a much more powerful GPU? How do we find an interface with other clouds? And like,
[1759.24 --> 1762.12]  that's where we're focused right now. And there's a lot of work to do here.
[1762.12 --> 1768.68]  Yeah, clearly, you have such a focus on kind of accessibility in terms of the user experience.
[1768.68 --> 1773.08]  And, and, you know, you have a bunch of different ways of connecting in, you know,
[1773.08 --> 1778.92]  like I use VS code. So I went and looked at that. And you have the guides that address different common
[1778.92 --> 1782.44]  models that we would be interested in that are really popular right now, like stable diffusion.
[1782.44 --> 1787.24]  And you talk about the different clouds. Could you pick one, whatever one you want,
[1787.24 --> 1792.84]  and just kind of walk us verbally through and I know it's audio only. But if you can walk us verbally
[1792.84 --> 1797.16]  through kind of what the workflow looks like, and what people might expect, just to give a sense,
[1797.16 --> 1801.16]  it looks really good. But I'm trying in my head, I'm trying to put it all together from an end to end,
[1801.16 --> 1804.84]  and I bet you've done this before. So I'm hoping you can kind of just give us a little narrative
[1804.84 --> 1808.84]  that's easy to follow on that. Yeah, so let's say you want to run Dreambooth,
[1808.84 --> 1813.56]  and you want to make a bunch of cool photos of you and your friends. So you can go to our
[1813.56 --> 1819.80]  Dreambooth template, it says, click a link, any environment, you can actually make a URL to
[1819.80 --> 1823.56]  easily share it. So we've made one that's a URL template for running Dreambooth. So you click
[1823.56 --> 1829.00]  the link from our blog post, or from the guide in our docs, and it will take you to the dev environment
[1829.00 --> 1833.56]  page with everything filled out. It has the GPU that you'll need selected, it has the volume,
[1833.56 --> 1837.96]  the amount of hard drive that you need, the repos that you need, the setup scripts that you don't,
[1837.96 --> 1840.68]  you don't have to worry about anything, just pretty much hit the create button.
[1840.68 --> 1844.44]  When you do that, the environment, essentially what we're doing behind the scenes is spinning
[1844.44 --> 1848.60]  up the GPU that you need. We are installing everything that's needed, all the dependencies
[1848.60 --> 1853.08]  that are needed for that. When you're done with that, with the brev CLI run brev open in the name
[1853.08 --> 1857.96]  of your environment, and it'll open up the S code to that environment. And in the readme, it'll say,
[1857.96 --> 1865.16]  upload 10 photos of yourself in this folder. And we kind of show you how to run, how to train. And that's it.
[1865.16 --> 1869.48]  So the idea is that, you know, in like four minutes, you have a GPU running everything,
[1869.48 --> 1874.04]  and all you have to do really is focus on the fine tuning that's, that you kind of want to focus on.
[1874.04 --> 1880.04]  That sounds great. Yeah. Could you share a little bit also about like, because part of this, I think,
[1880.04 --> 1888.20]  is like, I'm doing a specific thing in my environment that I've created, which is special to me. But now,
[1888.20 --> 1893.88]  somehow, like, I need to share that with Chris, right? How would that work out in this type of scenario?
[1893.88 --> 1897.32]  Yeah. So there's a few things that brev does behind the scenes. There's like,
[1897.32 --> 1901.96]  things that are that we intend for you to share. But every environment that I have, I have my own
[1901.96 --> 1907.00]  get aliases. Like when I type C, that's, that's a function for get commit, right? S is get status.
[1907.00 --> 1911.80]  There's a bunch of things that I just expect. And I have set up in my Zish RC. So you can set up your
[1911.80 --> 1917.48]  own developer preferences. And every time you create a dev environment, we take whatever was shared in the
[1917.48 --> 1921.96]  template, and then we add all of your settings on top of it. There's also hash a court vault is hooked up by
[1921.96 --> 1926.52]  default into every instance. So you have like an encrypted secrets manager. So I have my AWS
[1926.52 --> 1932.44]  credentials encrypted, and it stays in my AWS account. And every time I create a dev environment,
[1932.44 --> 1936.12]  if I if my co founder shares one with me, or someone on the team gives me their environment,
[1936.12 --> 1941.24]  I reliably know that my terminal settings are all gonna be loaded in my AWS credentials will be loaded
[1941.24 --> 1948.12]  in. But also there's scopes to the encrypted secrets manager. So you can say that if someone shares
[1948.12 --> 1952.36]  this environment, make sure that these secrets are added into the environments like an environment scoped
[1952.36 --> 1957.80]  setting. So it's up to you to decide what you want to be shared. We're not going to share secrets that you
[1957.80 --> 1961.56]  don't want. You're not going to share your AWS credentials. If you don't want it, you're never sharing the
[1961.56 --> 1966.76]  machine with somebody you're we're just setting up one for them and setting it up kind of identically. So
[1967.32 --> 1972.60]  yeah, yeah, which I guess gets to that sort of idea of templates, right? You're creating a template
[1972.60 --> 1978.12]  which you intend another person to use, but maybe in a slightly different way than you used it, right?
[1978.12 --> 1983.64]  Yeah, exactly. So I'm gonna I'm gonna throw out kind of a random question. And it's okay if you
[1983.64 --> 1988.92]  haven't gone here, I just want to ask, have you ever thought about having one that is essentially,
[1989.48 --> 1994.20]  you know, we see these services that companies will run, and then they'll end up deploying it kind
[1994.20 --> 1998.68]  of on a private server or something so that it can go into a secure environment, that kind of thing,
[1998.68 --> 2003.24]  uh, as a standalone instead of being web accessible, any thought toward doing something like that,
[2003.24 --> 2006.36]  uh, where you could use it in a non public environment?
[2006.36 --> 2011.00]  Yeah, so that's how larger teams, uh, will use brev. So at a minimum, you can just deploy
[2011.00 --> 2015.32]  all of the instances that the instances themselves stay in your AWS account. But we can also deploy the
[2015.32 --> 2020.68]  entire control plane behind your VPC. So nothing's really exposed out. Um, but that's kind of more on
[2020.68 --> 2024.12]  the enterprise route. Uh, individual developers, I don't think have those.
[2024.12 --> 2028.04]  I totally get it. And it's the enterprise route that I was kind of asking about is like,
[2028.04 --> 2032.76]  you know, you'll have large organizations that have their own, uh, GPUs and stuff like that,
[2032.76 --> 2036.44]  but they're still just GPUs. And so I was wondering whether like, you know, moving into
[2036.44 --> 2040.12]  that, if the control plane can say, okay, I'm going to hook up what you have in your data center,
[2040.12 --> 2043.80]  uh, here's your workforce and you kind of have your own environment. So that's something
[2043.80 --> 2045.64]  you clearly all have been thinking about doing.
[2045.64 --> 2049.64]  Yeah. And something that we actively support and we have teams that we're talking with that are
[2049.64 --> 2053.48]  going this route. It's, uh, you get all the same benefits where, you know, you can still scale
[2053.48 --> 2057.16]  down your instances, scale up your instances. Obviously you might not benefit from some of the
[2057.16 --> 2061.64]  the cheaper GPUs and the other clouds because they're not behind the VPC, but, um, if you're
[2061.64 --> 2067.32]  on like AWS or GCP, um, we can absolutely do that. And, uh, we know from like an individual user
[2067.32 --> 2071.40]  perspective, if you're going to pay an extra eight hours by accident, cause you know, we always forget
[2071.40 --> 2076.52]  to shut our instances off. If you're a team of 180 engineers, uh, that cost just is amplified.
[2076.52 --> 2080.76]  And I saw that at work day when I worked there as well. So, uh, definitely we've kind of had
[2080.76 --> 2084.36]  some of those learnings, uh, brought into the product as well. So yeah.
[2084.36 --> 2089.64]  Yeah. That's awesome. I'm just thinking like looking back at my own sort of progression and
[2089.64 --> 2095.80]  like trying to run some of these things myself and like, just thinking back, not, I mean,
[2096.68 --> 2103.24]  the tooling has improved, right. But the environments were still difficult. Right. So like either I had
[2103.24 --> 2110.28]  like, you know, the consumer GPU card that's in my like workstation here, or I'm trying to use one in
[2110.28 --> 2115.88]  the cloud and like the GitHub repo is there and like the tooling, like I can understand what's
[2115.88 --> 2121.64]  happening in the code, right? Like that has gotten much easier. I can deploy stable diffusion in like
[2121.64 --> 2127.80]  very small number of lines. Right. But the environment is still quite difficult. So I think this is really
[2127.80 --> 2133.16]  exciting and encouraging. I'm wondering what, what encourages you and what are you thinking about
[2133.16 --> 2139.24]  kind of like looking towards the future? Um, what, what excites you about this space?
[2139.24 --> 2145.24]  Oh man. What excites me about the space? I, uh, I think I don't know how to say it. There's,
[2145.24 --> 2149.56]  there's just so much to focus on in every realm, right? Within interactive and non-interactive
[2149.56 --> 2154.60]  compute. Like I've talked to Eric at banana about just how we both, both of our teams are at the same
[2154.60 --> 2158.44]  size and we're both a hundred percent focused in our space. And it just feels like there's an infinite
[2158.44 --> 2163.08]  amount just looking down. So looking up, there's even more, uh, you guys mentioned your last
[2163.08 --> 2169.16]  episode was on chat GPT. And, uh, I think AI is really exciting, not so much in that it's going
[2169.16 --> 2173.08]  to replace us all, but it kind of lets us be more creative directors of our own lives.
[2173.08 --> 2177.72]  If you think about any creative process as having like some generative aspect and then some like
[2177.72 --> 2182.36]  malleable aspect. So if someone's making clay, they like throw a bunch of clay down, that's the
[2182.36 --> 2186.92]  generative. And then you kind of like form it nicely into the bowl or cup that you want. Right. And that's
[2186.92 --> 2192.04]  the kind of like morphing it in. So there's always those two aspects. And when AI is able to help us
[2192.04 --> 2196.52]  just kind of really push on that generative side and we're still in control of the output,
[2196.52 --> 2201.08]  we're still the ones that are kind of morphing the final product. Uh, I view it as like, uh,
[2201.08 --> 2205.32]  just an extremely empowering thing. And so it's been really exciting seeing what all the developments
[2205.32 --> 2209.88]  in the space, um, really bought into the idea that you make things a little bit easier and you can just
[2209.88 --> 2213.88]  dramatically increase the affordance for things to happen. And so as much as possible, how do we get
[2213.88 --> 2218.44]  rid of machine problems and that people who want to build really exciting things and build the next
[2218.44 --> 2222.28]  new affordances and the new models essentially be able to do that with as little friction as
[2222.28 --> 2227.64]  possible. And that's not just within their, uh, fine tuning and, uh, resource constraints that
[2227.64 --> 2232.52]  they might have, but also in terms of like moving it and shipping it and delivering it. And so, uh,
[2232.52 --> 2236.84]  on one hand, the things that are being built is very exciting, but on the other, the energy in
[2236.84 --> 2242.04]  this space is huge, right? I think everyone has been so, uh, inspired by what's been done recently with
[2242.04 --> 2247.00]  chat GPT and the recent AI models that are out that it's just, it's galvanizing a lot of people to
[2247.00 --> 2250.76]  build a lot of really cool things. Everyone I know, especially here in San Francisco, founder or
[2250.76 --> 2255.56]  not is, you know, it's funny seeing founders who have nothing to do with AI thinking about AI side
[2255.56 --> 2260.28]  projects, right? That's galvanizing people. And so, uh, everyone is really excited about building
[2260.28 --> 2264.52]  this stuff right now. And I, I just hope we don't lose that energy and, um, just make things as
[2264.52 --> 2269.08]  frictionless as possible as we do that. Um, yeah, even I, I'm guilty. I have a little Saturday
[2269.08 --> 2273.96]  project I'm throwing together with some, some generative AI stuff, right? There's a lot of really cool
[2273.96 --> 2279.00]  stuff that's happening. So that's great. Yeah. Well, um, uh, thank you Nader and your team for
[2279.00 --> 2284.12]  helping us, you know, reduce some of that friction and get people's ideas out there. Like this is,
[2284.12 --> 2288.20]  this is super exciting. And I think, you know, speaking of friction, I think one of the things
[2288.20 --> 2294.52]  that you mentioned prior to our conversation is that, um, you'll spin up a coupon code for, for our
[2294.52 --> 2302.04]  listeners, um, for, uh, some compute on brev.dev and getting some of that, you know, removing even some of
[2302.04 --> 2306.12]  those barriers for our listeners as they're getting started. So we'll make sure and include
[2306.12 --> 2312.12]  that in our show notes. So, um, please take a look at that. Um, get on brev.dev. I did it. It
[2312.12 --> 2317.24]  only takes a couple of minutes. It's awesome. So yeah, thanks Nader for, uh, coming on the show and,
[2317.24 --> 2320.60]  uh, telling us about what you're doing. Absolutely. Thank you guys so much for having me.
[2320.60 --> 2324.04]  Really love the conversation. And by the way, Chris, you mentioned Lockheed Martin earlier.
[2324.04 --> 2327.72]  Um, my mom was a nuclear engineer and worked at Lockheed Martin as well. So, uh, that's awesome.
[2327.72 --> 2331.96]  Oh, thanks for telling me that I'm definitely in good company and, uh, awesome.
[2331.96 --> 2334.92]  Cool. Yeah. All right. Thanks. See you guys.
[2342.92 --> 2349.72]  All right. That is our show for this week. If you dig it, don't forget to subscribe,
[2350.20 --> 2355.64]  head to practical AI.fm for all the ways. And if practical AI has benefited your life,
[2355.64 --> 2360.84]  pay it forward by sharing the show with a friend or a colleague. Word of mouth is the number one way
[2360.84 --> 2367.16]  people find shows like ours. Thanks again to Fastly for fronting our static assets to fly.io for back
[2367.16 --> 2372.20]  in our dynamic requests to break master cylinder for the beats and to you for listening. We appreciate
[2372.20 --> 2380.52]  you. That's all for now. We'll talk to you again on the next one.
[2380.52 --> 2388.28]  OK.
[2388.28 --> 2389.80]  It's OK.
[2389.80 --> 2393.80]  It's OK the way you're going to stretch again.
[2393.88 --> 2394.28]  OK.
[2394.28 --> 2394.60]  Man.
[2394.60 --> 2394.78]  Bye.
[2394.78 --> 2395.32]  Like a word.
[2395.32 --> 2397.42]  Get started.
[2397.42 --> 2397.86]  Listen to it.
[2397.86 --> 2398.88]  For now.
[2398.88 --> 2399.50]  .
[2399.50 --> 2399.62]  Let me know.
[2399.62 --> 2400.54]  Hello.
[2400.54 --> 2401.14]  You're канал.
[2401.14 --> 2403.40]  22 am.
[2403.40 --> 2405.50]  Get down.
[2405.50 --> 2406.36]  Bye.
[2406.36 --> 2408.56]  Bye.
