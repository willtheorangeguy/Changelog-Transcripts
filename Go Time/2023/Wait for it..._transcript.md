[0.00 --> 11.34]  Let's do it. It's go time.
[11.90 --> 17.74]  Welcome to go time, your source for diverse discussions from all around the go community.
[18.10 --> 22.90]  Thanks to our partners for helping us bring you awesome pods each and every week.
[22.90 --> 29.28]  Check them out at fastly.com, fly.io, and typesense.org.
[29.28 --> 31.46]  Okay, here we go.
[43.74 --> 49.00]  Hello and welcome to go time.
[49.18 --> 57.64]  It's been a hot sec since I've been here and I'm extremely excited to be hosting a semi new type of episode
[57.64 --> 64.56]  where we're going to be deep diving onto a specific project that was worked on by members of our beautiful go community
[64.56 --> 71.90]  and talking through some of the trials, tribulations, issues they encountered, things that they worked on and why.
[71.90 --> 79.54]  And hopefully through exploring this specific case study, we as a community can learn a little bit of what to do, what not to do,
[79.62 --> 83.82]  and some tips and tricks for similar projects we might be working on.
[84.08 --> 91.40]  I'm extremely excited to be joined today by two wonderful women, Samantha Coyle and Anita Elizabeth Simon,
[91.40 --> 100.76]  who, along with their team at Intel, helped to create an ML pipeline that enabled image processing and automated image comparisons,
[101.20 --> 110.36]  which enabled healthcare use cases through their series of microservices that automatically detect, manage, and process images received from OEM equipment.
[110.78 --> 114.10]  So in this episode, we'll be chatting through those challenges they encountered,
[114.10 --> 120.36]  and we'll be focusing specifically on the weight strategy for their ML pipeline healthcare solution microservices.
[120.98 --> 128.14]  We'll also touch on how improvements were made to an open source package, a Go package, of course, as part of this project.
[128.58 --> 132.00]  So without further ado, I'm going to intro you to our two guests.
[132.08 --> 137.60]  As I mentioned, we have Sam Coyle, who's a software engineer at Diagrid, where she develops Go microservices
[137.60 --> 143.10]  and enables developers to run high scale modern applications using open source technology.
[143.10 --> 153.30]  She gets the opportunity to contribute to VAPA upstream and her current role and has a history of developing computer vision-based containerized applications
[153.30 --> 157.04]  and Go microservice for industrial applications at the edge.
[157.12 --> 160.24]  So she was very well placed to work on this specific project.
[160.80 --> 170.46]  She has her CKAD certificate, which she got in 2021, which is a tribute to her knowledge and her interest in distributed workloads
[170.46 --> 173.10]  and her dedication to that area.
[173.26 --> 177.68]  She also spends a lot of her time doing technical reviewing and authoring some Go textbooks.
[177.96 --> 179.50]  So clearly she's very passionate.
[179.82 --> 183.86]  She's also passionate about empowering early career gophers and engineers
[183.86 --> 186.64]  and really encouraging diversity in our space.
[187.10 --> 190.20]  She's part of a family of gophers, which I was really interested to find out.
[190.26 --> 191.90]  We have whole generations of gophers.
[191.90 --> 197.94]  We have her brother, who is the OG gopher, as you have told me, Ethan.
[198.36 --> 200.80]  Although I don't know, you know, is he still the OG?
[201.06 --> 204.46]  I feel like you've been rocking up at Gothicon giving some amazing talks.
[204.94 --> 206.76]  Yeah, may need to reevaluate.
[207.84 --> 212.00]  And then, of course, your wonderful twin sister, who's also a gopher.
[212.00 --> 217.68]  So you very cheekily slipped into your bio when I asked you to write a little bit about yourself,
[217.82 --> 223.74]  that your favorite conference experience was presenting on the mainstay of a gopher con 2022,
[224.30 --> 228.44]  which I feel like for those of you who don't know, I love gopher con on one of the chairs.
[228.66 --> 232.02]  So I don't know whether you put that in as genuinely your favorite experience
[232.02 --> 233.72]  or whether you were just trying to get in my good books.
[235.22 --> 236.50]  100% favorite.
[237.16 --> 237.50]  For sure.
[237.58 --> 238.70]  Okay, lovely to hear it.
[238.80 --> 240.12]  So how are you today?
[240.16 --> 240.68]  Are you excited?
[240.68 --> 242.62]  I think this is your first time on GoTime.
[243.06 --> 243.90]  Yes, yes.
[243.90 --> 246.86]  Super excited to be on my first GoTime podcast.
[247.14 --> 248.04]  Good day so far.
[248.48 --> 249.92]  Tacos and coffee in.
[250.08 --> 252.26]  So very happy y'all are having me.
[252.66 --> 253.96]  Really excited to have you.
[254.00 --> 257.60]  And I'm hoping the next hour will not turn your amazingly good day into a bad day.
[257.70 --> 258.92]  But we shall see.
[260.08 --> 265.76]  Next up, we have Nithu Elizabeth Simon, who's on an IoT ML team.
[265.76 --> 270.48]  She's a senior software engineer in the Network and Edge Group at Intel Corporation.
[270.68 --> 276.74]  She has vast industry experience building smart end-to-end vision-based machine learning solutions.
[277.10 --> 280.62]  Again, a great fit for the project we're going to be discussing today.
[280.98 --> 289.70]  She's currently focused on building containerized microservices for computer vision-based AI ML solutions for retail and healthcare use cases.
[289.70 --> 297.54]  She has a master's in computer science from Arizona State University and is extremely passionate about promoting girls in STEM.
[298.12 --> 304.32]  She actually won the Women Who Code for 2023 Applaud for her award.
[304.64 --> 307.22]  It was 100 technologists to watch.
[307.22 --> 308.70]  Was that the award Nithu?
[309.06 --> 310.82]  For her contributions to the space.
[310.92 --> 319.62]  And then you also have the 2020 Society of Women Engineers DNE Award for being a powerful technical contributor and advocate for STEM education.
[319.62 --> 322.60]  So a very active member in that space.
[322.62 --> 324.14]  And I applaud you myself.
[324.34 --> 325.02]  Thank you.
[325.68 --> 326.18]  For all your work.
[326.22 --> 327.00]  It needs to be done.
[327.00 --> 336.50]  And I must say, as a side note, very excited to be sitting here on this podcast with us three women on the stage talking about extremely technical project.
[336.80 --> 337.76]  It makes me very happy.
[338.36 --> 338.62]  Awesome.
[338.90 --> 343.76]  So I feel like I've been alluding to the project we're talking about today in my intro.
[343.90 --> 345.54]  So let's get straight down to it.
[345.64 --> 348.82]  So tell me, what is this project that you worked on?
[349.28 --> 349.48]  Yeah.
[349.48 --> 354.04]  So this was actually a biopharma-based healthcare kind of a solution.
[354.04 --> 363.66]  It is architected and developed in a way that we can reuse it for any other use cases in other industries like retail or industrial or something like that.
[363.96 --> 370.84]  So, I mean, I can't go explain a lot of the details because there are some customer confidentiality there.
[370.84 --> 382.58]  But we'll keep it very high level technical so that the listeners can learn from it and learn from our challenges and how did we overcome some of these challenges.
[383.36 --> 387.92]  So at the most base level, like what was the problem you were solving?
[388.56 --> 397.18]  So it was image processing at the edge, which, you know, being at the edge introduces additional complexities and considerations.
[397.18 --> 403.40]  And so that's kind of where we played into some of the EdgeX foundries community.
[404.08 --> 411.50]  And so what that is, is this way of working with IoT devices and developing Go Microservices at the edge.
[411.90 --> 416.26]  And so they have a bunch of SDKs and different features that you can use.
[416.36 --> 419.40]  So that way you can enable cool projects like ours, right?
[419.54 --> 424.02]  So kind of, yeah, edge image processing and enablement.
[424.16 --> 425.70]  I think that's it at a high level.
[425.70 --> 431.26]  Yeah, and I can add on a little bit more details on the like the project wise, right?
[431.32 --> 435.00]  It's a distributed microservices based containerized solution.
[435.32 --> 437.78]  So what we have is like two systems here.
[437.98 --> 442.48]  One we call as the OEM device, which is connected to an image capturing device.
[442.66 --> 446.80]  It can be a microscope, camera or any other such device.
[446.98 --> 453.12]  And then it automatically collects these and then transfers it to a different device called as the gateway.
[453.12 --> 456.72]  And which is running the Linux Ubuntu in our case.
[457.00 --> 459.64]  All the machine learning pipelines are run on this gateway.
[460.00 --> 464.20]  We get back the results and then all of that is sent back to this OEM device.
[464.34 --> 471.34]  So our solution basically helped automating all this image capturing, transferring, managing, processing.
[471.34 --> 476.14]  All of these processes were automated by our solution that we developed.
[476.66 --> 476.90]  Awesome.
[477.22 --> 485.52]  And as you were coming to this problem, as you were thinking through how to address it, was it a given that you would write it in Go?
[485.64 --> 487.92]  Like why was Go the language that you chose?
[488.24 --> 488.48]  Yeah.
[488.48 --> 491.40]  So me personally, I'm pretty new to Go.
[491.94 --> 494.64]  I've jumped around like languages, several languages.
[494.84 --> 498.16]  I started with Java and now I'm coding in Golang.
[498.44 --> 506.16]  So Golang is again open source programming language, which was introduced by Google to build simple and reliable softwares.
[506.42 --> 511.08]  It is very, very popular in building distributed microservices based solutions, right?
[511.08 --> 519.08]  Runs faster than most of the other programming languages that are used for non-scalable servers and large software systems.
[519.88 --> 525.44]  So for us, it was not a difficult choice to make to go with Golang.
[525.66 --> 529.36]  Also, Go is designed to run on like multiple cores, right?
[529.48 --> 533.74]  And Intel is a CPU producing company, manufacturing company.
[533.92 --> 535.38]  So that's important to us.
[535.56 --> 540.62]  So concurrency and scale is already built in for Golang, right?
[540.62 --> 548.94]  And it provides all these multi-threading capabilities, which makes it really fast to program the languages for the distributed systems.
[549.26 --> 550.82]  Yeah, it's also something.
[551.16 --> 559.62]  So like I'm not at Intel anymore, but it is kind of the go-to, well, pun intended, go-to language of the org at the time.
[560.02 --> 562.32]  So it kind of made sense for this project.
[562.32 --> 568.60]  And also, again, kind of the framework that we were working with supported working with Go.
[568.60 --> 573.46]  And so that's kind of why we just stuck with it because it was tried and true and we were familiar with it.
[573.84 --> 578.98]  And then in terms of your initial discussions about the solution and how to architect it,
[579.04 --> 584.70]  I'd be interested to hear, just because I think it's useful to hear the decision-making questions you asked yourselves,
[585.40 --> 590.56]  why you ended up going with a containerized and a microservice infrastructure.
[590.92 --> 592.46]  Like what were the questions you asked?
[592.46 --> 594.04]  How did you evaluate that decision?
[594.52 --> 598.24]  Yeah, so for our organization from like last couple of years,
[598.32 --> 602.62]  we've been pushing for these containerized microservices kind of an architecture.
[603.30 --> 608.20]  Containerized because it's, as you know, containers are like lightweight, virtual environment, right?
[608.20 --> 610.80]  Which is more economical and scalable.
[611.22 --> 616.46]  You know, what do I mean that is you don't have to set up an entire environment on a new machine.
[616.46 --> 623.62]  We can just use the Docker and Docker Compose files independent of the operating system where these applications need to run, right?
[623.66 --> 628.16]  So it's very lightweight and we don't have to install this entire OS stack.
[628.68 --> 630.36]  A virtual environment does, right?
[630.42 --> 633.16]  So containers are easy to maintain and develop.
[633.34 --> 634.30]  So that was one reason.
[634.56 --> 640.26]  And then the other piece is microservices architecture is actually a very loosely coupled architecture.
[640.26 --> 648.04]  So it's very easy to, you know, build our application services, add and remove them without affecting the, you know, overall solution architecture.
[648.48 --> 654.14]  And like San mentioned earlier, right, our project is based on the EdgeX foundry services,
[654.28 --> 657.50]  which is again an application microservices based architecture.
[657.82 --> 661.44]  We built all our applications on top of EdgeX basically.
[661.64 --> 667.16]  So that scalability we were able to achieve because of that microservices architecture.
[667.16 --> 670.34]  Awesome. So you decided kind of the broad approach.
[670.46 --> 672.00]  You've decided Go is the way to go.
[672.36 --> 673.40]  Again, no pun.
[673.82 --> 675.20]  It's going to happen all episode.
[675.62 --> 675.88]  I know.
[675.88 --> 676.96]  I would love to hear it.
[677.10 --> 681.70]  Like, how did you, and I feel like perhaps if I'm remembering right, it was you, Sam.
[682.04 --> 685.72]  How did you come across the Go implementation, the weight for it?
[685.84 --> 688.66]  And for the listeners, like, what is that?
[688.88 --> 690.02]  Where did you find it?
[690.16 --> 694.88]  And maybe you could give a little info on how you move forward thinking about using it.
[694.88 --> 699.22]  Yeah. So that's kind of, it was kind of like, it sounds obvious, right?
[699.22 --> 703.98]  And it sounds easy, like defining a weight strategy for your different services.
[703.98 --> 710.78]  And so like, in its most basic form and an example of, you could think of like a service
[710.78 --> 715.18]  waiting for its database to be up and ready before accepting requests, right?
[715.18 --> 725.16]  So it's like, you have these dependencies that you need to be up and ready for requests to go through and for your service to behave as you would expect.
[725.78 --> 728.76]  And so especially if you think about a production level environment, right?
[728.76 --> 734.52]  That's really important that you're able to write to your database or that like, you know, your dependencies are up and ready.
[734.52 --> 744.32]  And so that's kind of some of the high level context going on here when we talk about a weight strategy and having your services waiting for other services.
[744.72 --> 746.88]  So that's kind of some of the background here.
[747.12 --> 753.60]  And so for this project in particular, it was interesting because we had two different machines.
[753.94 --> 760.78]  We had that Windows machine and we had a Linux Edgebox running different microservices.
[760.78 --> 769.22]  And so we had to have some coordination between the services running on the Windows machine and the services running on the Linux Edgebox,
[769.46 --> 777.62]  just to make sure, again, that everything was up and ready as we were expecting and such that everything could process as we expect.
[778.12 --> 781.92]  And that there were no surprises, even though, you know, there are sometimes.
[782.78 --> 786.86]  So, yeah, that's kind of the background waiting for our service dependencies to be up and ready.
[786.86 --> 792.98]  And so I think it's pretty common that people have probably heard of the Vishnubob Bash script.
[793.42 --> 801.44]  So this is like a Bash script implementation to allow for that logic of waiting for other services and waiting for your dependencies,
[801.88 --> 806.32]  TCP host and port to be up and ready before starting that service itself.
[806.70 --> 814.14]  And so you'll often see that applied into the Docker layer using that Vishnubob Bash script, right, on your command or entry point.
[814.14 --> 818.22]  And so, yeah, our org was familiar with that from past projects.
[818.60 --> 828.86]  And we wanted to look at, well, hey, like we need this, right, because we need our services to work cohesively and be up and ready before proceeding.
[829.26 --> 833.54]  So we looked out, OK, well, should we use this one or are there alternatives?
[833.54 --> 841.98]  And so thankfully, the Go version, the wait for it, Go Rebo is linked to the Vishnubob Bash script.
[842.06 --> 843.58]  So that's kind of how we stumbled upon it.
[844.26 --> 845.32]  That was very long winded.
[845.96 --> 846.38]  That's great.
[846.52 --> 848.26]  And I mean, you stumble upon it.
[848.66 --> 854.96]  How do you go about thinking through whether it's the right fit, whether it's going to do what you need it to do?
[855.00 --> 859.34]  And then follow up is where to then use it and how to implement it.
[859.34 --> 867.26]  There's a lot to that and to kind of uncompact it and need to stop me and interject.
[867.96 --> 879.22]  But OK, I guess I'll start with the like at what layer is it most appropriate to add in this logic and like how can you decide what's best?
[879.60 --> 883.54]  So obviously, I will caveat that all of this is very dependent on your use case.
[883.54 --> 890.16]  So obviously, like what made sense for us for this project might not make sense for everyone for their projects.
[890.54 --> 894.32]  So for us, we looked at, OK, well, what's tried and true?
[894.72 --> 896.44]  What have people done before that's worked?
[896.58 --> 899.90]  And again, that's using the Docker layer approach.
[900.14 --> 902.30]  So it's kind of there's two options.
[902.34 --> 904.20]  You can apply it in the Docker layer.
[904.20 --> 910.30]  So your build area, right, Docker or Docker Compose, or I'm sure there's plenty of other options.
[910.30 --> 913.88]  Or you can apply it in your Go application code layer itself.
[914.42 --> 916.52]  So those are like the two main options.
[916.78 --> 921.66]  And I'll kind of dive into the Docker side, I guess, to start out with.
[921.66 --> 932.30]  So, again, for us, our team knew about the Vishnubha Bash script, which is where you'll have your Docker file right with your command to start your service.
[932.74 --> 947.62]  And then in your Docker Compose, if that's what you're using, which that's what we used, you would have an entry point where you're overriding the starting of that service, wrapping it with that wait for it script saying, hey, start my service, but wait for the other services.
[948.28 --> 949.70]  So that's typically what happens.
[949.70 --> 959.62]  But with that, if you do use the Docker Compose entry point, it also has the potential to override your Docker file command.
[960.24 --> 965.72]  So that's actually a known issue with Docker Compose that you do have to keep in mind if you go with that approach.
[965.98 --> 969.48]  So you just append your command to the overwritten entry point.
[970.72 --> 978.34]  And Docker Compose also has a depends on keyword, but it's I don't think it's a thing anymore in version three.
[978.34 --> 980.78]  So that's not really an option.
[980.98 --> 982.28]  I think people go nowadays.
[983.26 --> 985.62]  So that's kind of like the Docker side of things.
[985.86 --> 989.00]  And then there's the go side of things, which is what we went with.
[989.00 --> 998.20]  And for us, you know, it made the most sense to stick with the go side of things just because not all of our services were running with Docker.
[998.60 --> 1001.50]  So that was like a big caveat for us.
[1001.50 --> 1001.76]  Right.
[1001.76 --> 1007.36]  We wanted a homogenous solution for all of our services at test and deploy time.
[1008.16 --> 1014.64]  So that's why we went with the go wait for it, which, again, is inspired by that bash script version.
[1014.64 --> 1026.58]  It's pretty consistent with what you expect from the Vishnabha bash script, but written in Go as a Go executable that you can bring in with modification currently to your projects.
[1027.26 --> 1027.40]  Yeah.
[1027.68 --> 1031.04]  So those are the two main things and some of the considerations we had.
[1031.04 --> 1031.60]  Yeah.
[1031.72 --> 1042.22]  And just adding on to what Sam just mentioned, it was pretty simple to deploy and start our services, our existing services, without making a lot of changes.
[1042.22 --> 1042.50]  Right.
[1042.54 --> 1055.08]  After bringing in this new wait for it package, we only had to make an additional field change in our server structs to define the dependent services that it needs to wait for.
[1055.08 --> 1059.84]  But other than that, we didn't have to make a lot of changes in our existing code.
[1060.02 --> 1064.72]  So that was the one other reason why we went with that particular package.
[1065.16 --> 1078.18]  And I'd be interested to hear, Nithu, from you a little bit on how, whether with this package specifically or in general, how do you check that it's safe and it's OK and we're good to go to use it?
[1078.18 --> 1078.62]  Yeah.
[1078.62 --> 1078.74]  Yeah.
[1078.84 --> 1079.02]  Yeah.
[1079.14 --> 1090.44]  So for our projects, right, in our team, we do make sure that the open source packages that we are adopting for our projects or integrating need to have a proper license.
[1091.06 --> 1100.34]  And they need to have some kind of a developer activity on their GitHub repos in recent times to make sure it has been maintained.
[1100.50 --> 1100.70]  Right.
[1100.72 --> 1102.92]  It's not like a stale package out there.
[1102.92 --> 1110.62]  So, I mean, with that regard, we did find out, we did see that there were two other like packages which did kind of the same thing.
[1110.72 --> 1111.90]  One was this wait for it.
[1112.02 --> 1116.04]  And then there was another one which was, you know, net wait go kind of a package.
[1116.22 --> 1121.06]  So as Sam mentioned, the wait for it is based on this Vishnu Bob Bash script.
[1121.26 --> 1128.02]  It is the go utility, you know, to wait for the availability of a TCP host and port for these dependency services.
[1128.02 --> 1136.40]  Right. And this package had an MIT license and it had some kind of developer activity on their repo compared to this other one.
[1136.50 --> 1137.72]  The net fit wait go.
[1138.00 --> 1138.98]  It did not have a license.
[1138.98 --> 1146.60]  I think from last two, three years, there has been no like updates or any PR reviews or comments or anything on that package.
[1146.60 --> 1157.58]  So for us, it was an easy choice to just go with the wait for it package option that we had just to minimize the risk on the project.
[1158.10 --> 1158.46]  Yeah.
[1159.42 --> 1163.92]  I actually saw this morning that there's another option out there.
[1163.96 --> 1165.26]  So it's like one of those things.
[1165.46 --> 1167.24]  I think it's a common problem.
[1167.64 --> 1170.80]  And so there's like lots of different solutions out there for it.
[1170.80 --> 1174.44]  So I think the third one is called wait for X.
[1174.62 --> 1176.64]  Oh, just found that one today.
[1179.10 --> 1180.28]  Beauty of technology.
[1180.42 --> 1181.66]  It just keeps on new solutions.
[1181.74 --> 1183.12]  Keep on springing on up.
[1183.90 --> 1184.26]  Yeah.
[1184.46 --> 1184.70]  Okay.
[1184.72 --> 1184.96]  Awesome.
[1185.02 --> 1186.90]  So you've decided on your architecture.
[1186.90 --> 1188.04]  You're going with go.
[1188.56 --> 1189.44]  Keep on saying.
[1189.94 --> 1192.48]  And you've evaluated the package for use.
[1193.20 --> 1194.70]  How did you then move?
[1194.70 --> 1205.40]  And maybe, Sam, you could give us the granular detail from saying, okay, we want to use this to then bringing it internally and getting it ready to be used.
[1206.08 --> 1206.32]  Yeah.
[1206.50 --> 1208.14]  Yeah, that's a good question.
[1209.08 --> 1217.08]  So the thing about the wait for it, I want to say go package because it just comes very natural to say.
[1217.22 --> 1221.80]  But it's not technically a consumable package.
[1221.80 --> 1224.58]  And so that's a thing with this repo.
[1225.06 --> 1229.26]  If you do choose to use the wait for it package, I guess.
[1229.34 --> 1229.72]  I don't know.
[1229.96 --> 1238.00]  It's only using package main, which, right, for all of us gophers, that means we can't consume it unless we modify it.
[1238.66 --> 1246.18]  And so what that meant for this project in particular is, unfortunately, I had to copy paste their code.
[1246.18 --> 1255.36]  So it was nice, right, because we got all of this wait logic and, of course, giving proper attributions to the author who originated the repo.
[1255.74 --> 1267.42]  But it was really unfortunate because it wasn't the go natural way of, you know, creating open source packages such that other gophers can consume them and contribute and so forth.
[1267.42 --> 1269.50]  So that had a few side effects.
[1270.70 --> 1279.84]  So, I mean, for one, it meant like extra code for our team to maintain and, of course, modify as we found little things here and there.
[1279.84 --> 1290.82]  So one of the big things that I did was I copy pasted in the logic so that we could bootstrap all of our main.gos and all of our services to work with the logic.
[1291.30 --> 1301.08]  And as Nithu said, it was copy paste, modify, and then a minor modification to all of our server structs to define all of our dependencies, right?
[1301.08 --> 1303.68]  So we could say, hey, wait for this service, wait for that service.
[1304.16 --> 1311.24]  So it made it really clean, but it made it to where I also had to add a wrapper around their logic.
[1311.24 --> 1315.50]  So that way it was more idiomatic to look at and to consume.
[1316.02 --> 1318.92]  So I think they just had functions called wait.
[1319.30 --> 1325.06]  And so I added a wait package, naturally, and I added a for dependencies.
[1325.06 --> 1332.26]  So it was wait.for dependencies, which is very natural and very easy to understand what's going on.
[1332.64 --> 1336.16]  So a few modifications and one other learning.
[1337.08 --> 1344.36]  And this was so funny because so I brought in the logic, added my wrapper and my additional method, right?
[1344.42 --> 1346.86]  So it was pretty and nice to work with.
[1346.86 --> 1352.84]  And then our tech lead in Nithu, they were like, hey, what about an error case?
[1352.84 --> 1356.68]  Like what happens if the service never becomes available?
[1356.96 --> 1358.86]  Like what do we want in that case?
[1359.50 --> 1363.04]  And so I think it's really interesting thinking about do we retry?
[1363.20 --> 1363.86]  How often?
[1364.04 --> 1365.80]  What makes sense for our use case?
[1366.54 --> 1367.90]  And everyone's different.
[1368.80 --> 1376.38]  So what I found out in just bringing over the logic was that I didn't translate that aspect from the repo.
[1376.38 --> 1386.82]  So with the initial bringing in the wait logic for our services, it just hung if your dependent service never became available.
[1387.22 --> 1393.72]  And I don't think that's something you necessarily want, especially right in, say, a production ready environment.
[1393.72 --> 1407.46]  So I actually had to go back and add that timeout logic because in the wait for it repo, that's on the CLI side of things, not necessarily translating 100% in the wait logic that exists right now.
[1407.56 --> 1414.16]  And going through this process, I mean, you've spoken a lot about like the minor modifications, the copy-paste-ing.
[1414.26 --> 1414.46]  Yeah.
[1414.46 --> 1420.38]  Did you, if any, have any interactions with the like core authors maintainers?
[1420.44 --> 1421.64]  Like how did they support?
[1422.02 --> 1423.62]  What was the process there?
[1423.98 --> 1424.78]  Was there zero?
[1424.90 --> 1427.04]  You kind of just copy-paste, do your thing, make it work?
[1427.20 --> 1433.84]  Or did you have any communication or interaction with them around like, hey, this isn't super usable.
[1434.68 --> 1435.88]  What's up with that?
[1435.88 --> 1436.32]  Yeah.
[1436.32 --> 1437.08]  Yeah.
[1437.46 --> 1448.24]  So for the interactions with the author, I contributed back to the repo and opened a pull request in December.
[1448.74 --> 1451.18]  So I don't know, a few months ago.
[1452.04 --> 1453.58]  And crickets.
[1453.88 --> 1456.06]  It was crickets for a few months.
[1456.06 --> 1466.44]  And then very, very recently, like within the last 10 days, I think, I got a response and he was like, hey, this is awesome.
[1466.62 --> 1467.58]  Thank you so much.
[1467.60 --> 1472.56]  And he commented on how it's very readable and he was excited to try it.
[1472.56 --> 1476.92]  And of course he found, you know, an issue running it on his computer.
[1477.98 --> 1480.58]  I haven't been able to reproduce yet.
[1480.76 --> 1482.38]  I need to look into it a bit more.
[1483.10 --> 1485.48]  But yeah, so it's promising.
[1485.48 --> 1487.76]  It's promising and it's in the works.
[1487.76 --> 1490.02]  And I think it should get resolved soon.
[1490.90 --> 1491.02]  Awesome.
[1491.22 --> 1499.96]  So going forward, hopefully other gophers may not need to do the copy-paste shenaniganing, fingers crossed, that you had to go through.
[1501.96 --> 1502.52]  Okay.
[1502.52 --> 1510.56]  So in terms of that process, working with this non-package, may try to make it packageable.
[1510.96 --> 1512.86]  What were the core kind of takeaways?
[1512.86 --> 1521.72]  What were the core things that you learned trying to implement this specific part of your overall application infrastructure?
[1522.84 --> 1524.42]  And a valid answer is nothing.
[1524.82 --> 1528.24]  You just posted through and made it work.
[1528.24 --> 1538.06]  But are there any pearls of wisdom so that if anyone else does need to do this, fingers crossed they won't with this specific use case, but with others?
[1538.56 --> 1540.78]  Are there advice as to how to approach it?
[1540.90 --> 1543.62]  Is there things that you wish you had tried earlier?
[1544.06 --> 1545.50]  Different ways to approach it?
[1545.50 --> 1556.28]  Or even just like, I don't know, ping in the maintainer so that it doesn't take many a month to respond when it's a production-based issue or package you'd like to use?
[1556.28 --> 1569.84]  So I think for me, when it came to the implementation, like contributing back to the repo itself, a learning that I had, and it was just kind of nice.
[1569.84 --> 1577.46]  So I guess for me, it was nice coming from the perspective of neither my team were consuming the package, right?
[1577.54 --> 1581.12]  So we knew what we wanted out of it, right?
[1581.16 --> 1586.40]  We knew from a consumer side of things how we would want to interact with it.
[1586.70 --> 1590.00]  We knew for our use case, we did want retries.
[1590.00 --> 1599.60]  And so for us, you know, that meant we had the timeout where it would try once and check if that dependent service is up and ready.
[1599.94 --> 1603.78]  But then, you know, you could define like retry three times.
[1603.92 --> 1609.04]  Or you could say, hey, retry 15-second intervals up to 45 seconds.
[1609.04 --> 1620.16]  So it was kind of this weird learning of like, where do you draw the line in terms of how much responsibility should this package take on versus like what we needed?
[1620.42 --> 1627.46]  Because, you know, right now on the PR, the author, he was asking me because I added a max timeout.
[1627.90 --> 1629.86]  And for us, I think it was like a minute, right?
[1629.90 --> 1633.20]  So it would try on 15-second intervals up to a minute.
[1634.04 --> 1638.20]  And so the author said like, well, what's the point of the max?
[1638.20 --> 1642.76]  So I guess the learning is like, yeah, where do you draw that line?
[1642.86 --> 1644.56]  And everyone's going to want a different thing.
[1644.60 --> 1646.26]  So how do you find a good, happy path?
[1646.74 --> 1648.78]  Yeah, I can add on just that.
[1649.04 --> 1658.96]  So this particular whole wait for it project or the package that we came across was for a different project, I think, two years back that we worked on.
[1659.18 --> 1661.44]  And I think that was the December, right?
[1661.50 --> 1662.62]  Not this December.
[1662.76 --> 1666.64]  It was 2021 December that Sam, I think, worked on it.
[1666.64 --> 1668.94]  How do you look?
[1669.04 --> 1669.50]  I don't know.
[1669.78 --> 1671.54]  Yeah, I think, yeah.
[1671.94 --> 1678.34]  And after that, we had this new project where we again adopted the same strategy, right?
[1678.56 --> 1683.08]  So just the fact that it is taking so much time to write.
[1683.30 --> 1686.20]  She opened the PR, but it didn't get merged.
[1686.20 --> 1691.30]  And we had to copy paste the same thing for a different project.
[1691.54 --> 1695.02]  I think that would be, I would say, the challenge with this particular package.
[1695.48 --> 1701.42]  But I do want to mention, like, this was one of the challenges we had with this big project.
[1701.76 --> 1703.40]  There were like plenty of them.
[1703.60 --> 1703.80]  Oh, yeah.
[1703.80 --> 1711.12]  Yeah, we did actually talk together in the Open Source Summit just like recently three weeks back.
[1711.38 --> 1716.92]  And it was all about this particular project, the different challenges and learnings we had on this project.
[1716.92 --> 1726.62]  So, yeah, I would say this was like one piece of that challenge compared to, you know, the whole range of challenges we had to go through to get this working.
[1726.92 --> 1727.02]  Yeah.
[1727.26 --> 1731.34]  I'm going to assume everyone's going to go, you know, check that out after this.
[1731.34 --> 1739.46]  But if they don't, for whatever silly reason, could you give us an idea, like, what were the other kind of challenges that you encountered?
[1739.64 --> 1745.56]  What were the other things that kind of gotchas that you think it might be useful for people to learn from?
[1745.98 --> 1747.78]  Yeah, yeah, yeah, definitely, definitely.
[1748.08 --> 1749.38]  So this is my favorite one.
[1749.50 --> 1759.64]  But I feel one of the challenges which, you know, projects like us, like open source projects might run into because we are dependent on other open source projects.
[1759.64 --> 1770.76]  So what happened was we finished with our development work and everything by like last year, somewhere around August, we released our project.
[1771.18 --> 1777.04]  And then we did have a dependency on a particular package or a particular project called as the Project Air.
[1777.24 --> 1779.76]  It was developed by Tipco, Tipco Labs.
[1779.76 --> 1789.30]  And what they did was they managed the pipelines, the machine learning pipelines, helped in the visual composition of these pipelines, deploying them and execution.
[1789.62 --> 1795.40]  That entire piece was no dependent on this particular software piece that we integrated with our project.
[1795.70 --> 1800.74]  Now, after August, we get to know that Tipco is getting integrated with Citrix.
[1800.74 --> 1804.76]  So they are canceling the development on this project.
[1805.92 --> 1809.20]  No, no more support on this project.
[1809.74 --> 1815.12]  And we had to act fast and we had to pivot with what we wanted to do further.
[1815.40 --> 1822.80]  So we did decide to find replacements for these individual features that this particular project was giving us.
[1822.80 --> 1831.84]  And currently, our team is focused on replacing these individual Tipco project air pieces with other open source projects.
[1832.10 --> 1835.80]  And we are planning for a release of this project by end of this quarter.
[1836.16 --> 1842.64]  So after that, it would be available on open.intel.com for anyone to just go and play around with.
[1842.84 --> 1843.78]  It will be there on the GitHub.
[1843.78 --> 1850.26]  And is that kind of need to be agile and keep an eye out for any changes, depreciations, etc.?
[1850.26 --> 1853.02]  Is that something that you can plan for?
[1853.16 --> 1858.34]  Or is it something you just need to, if you're deciding to work with this kind of like open source packages that could change,
[1858.46 --> 1860.88]  you just have to accept things are going to be changing.
[1861.04 --> 1864.62]  You're going to have to drop everything and find replacements, as you say.
[1864.72 --> 1867.00]  Is it just like a, can you plan?
[1867.14 --> 1867.92]  Can you do anything?
[1867.92 --> 1874.16]  But I think the difficult, more difficult question is, what if you don't find replacements, right?
[1874.60 --> 1878.32]  Do you have enough time to like spend to develop these from scratch?
[1878.48 --> 1882.84]  And how does that affect your project timelines and things like that?
[1882.92 --> 1883.84]  Yeah, it's complex.
[1884.50 --> 1891.32]  And is that really, that's really the solution is, is either you just accept that it's going to be depreciated
[1891.32 --> 1895.92]  and there isn't a replacement and therefore you have to work out like, how are we going to build this internally?
[1895.92 --> 1905.62]  Is that maybe a reason to, when you're originally architecting your solution, not use open source?
[1906.06 --> 1908.40]  Like what is the, what is the trade-off?
[1908.48 --> 1909.40]  And I don't have an answer.
[1909.58 --> 1913.92]  It's just, I think, an interesting question between if you're building the original solution,
[1914.46 --> 1917.94]  advocating to build it in-house so it's internally maintained, etc.
[1917.94 --> 1929.26]  And maybe it's a longer deliverability timeline versus let's use this, this open source package or in Sal's case, non-package package.
[1929.64 --> 1937.66]  Like, is that something that both developers and just like broader, like engineering teams should be really thinking through before saying,
[1937.80 --> 1940.58]  oh great, there's this open source package available.
[1940.72 --> 1941.52]  Let's use it.
[1941.52 --> 1945.14]  I think that gets at, that's what I've been realizing.
[1945.44 --> 1954.60]  So in my current role with Diagrid, I get to work and help out with the Dapper Upstream project, which is super neat, right?
[1954.64 --> 1957.86]  Like giving back to the community and becoming part of a community.
[1957.86 --> 1964.60]  But yeah, I feel like when you hear open source, it's like butterflies and rainbows and like, it sounds awesome.
[1965.12 --> 1969.50]  But then it's like, there's so much more to it.
[1969.58 --> 1975.36]  Like considerations, like what you're saying, how to make sure it's ready, like ready, ready for release.
[1975.36 --> 1979.10]  And there's so much more to it than I think we give it credit sometimes.
[1979.80 --> 1979.88]  Yeah.
[1980.00 --> 1984.70]  I mean, to me, I think it depends from situation to situation, right?
[1984.76 --> 1987.30]  How complex is that software piece?
[1987.30 --> 1992.66]  I mean, for something like small thing, maybe we can develop it in-house, right?
[1992.76 --> 2004.28]  But something which is like a big feature, like this pipeline, composability and deployment and, you know, these things are like, if you're going to develop something, it will take a lot of development time.
[2004.78 --> 2008.34]  And the larger question to ask is like, no, is your customer going to wait?
[2008.54 --> 2010.04]  How long are they going to wait?
[2010.10 --> 2014.22]  I think we should just leave that decision completely on the customer's requirement.
[2014.22 --> 2017.38]  Like, what do they want, right?
[2017.54 --> 2017.74]  Yeah.
[2017.84 --> 2025.12]  And just make your decisions based on that instead of trying to find the right answer to that question, I guess.
[2025.36 --> 2030.62]  So to add on to that, it's kind of down to if the team has expertise, right?
[2030.62 --> 2043.98]  And so if you think about really niche areas, maybe like CV at the edge, like not everyone's going to have the machine learning knowledge, plus the app development knowledge, plus like, you know, the list goes on.
[2044.16 --> 2047.22]  Like, I mean, there is overlap between these different fields.
[2047.22 --> 2051.48]  But, yeah, that's another consideration when it comes down to that.
[2051.98 --> 2056.42]  And on the note of experience, like I don't want to bring us semi full circle.
[2056.92 --> 2068.08]  I know, Nithu, you said that you were not a full gopher, although I can debate what the requirements are for that at the start of this work.
[2068.08 --> 2073.70]  And then we had the potential OG gopher Sam vying for the title of her family.
[2074.34 --> 2076.30]  What was the learning curve like there?
[2076.38 --> 2082.00]  Like, how challenging was it both for yourselves and I'm assuming some other members of the team who maybe weren't as familiar with Go?
[2082.14 --> 2087.14]  What was that like to learn and implement in a language you weren't super familiar in?
[2087.14 --> 2095.24]  What I like most about software engineering is this vast variety of software languages and tools that you can learn.
[2095.48 --> 2101.00]  And I've been fortunate to learn some of this and jump between languages as such.
[2101.16 --> 2106.14]  To me, Golang, getting started on Golang, I think was pretty easy.
[2106.82 --> 2110.42]  I would say it was not very difficult, not as easy as Python.
[2110.96 --> 2115.32]  I do like Python because it's very, very abstract.
[2115.32 --> 2119.78]  I'll be honest, Python is very abstract when compared to Go.
[2120.00 --> 2128.18]  And Go, I felt like Go is a version of like C in a Python range kind of a thing.
[2128.68 --> 2130.58]  So because C is difficult to learn, right?
[2130.72 --> 2133.66]  And Go has some of those features that C has.
[2133.88 --> 2139.34]  And I feel like Go has made some of those C features a little bit more easier with Golang,
[2139.34 --> 2144.02]  like the concurrency and multiprocessing, threading and things like that,
[2144.06 --> 2148.26]  which is kind of difficult to understand or grasp if you're programming in C.
[2148.56 --> 2154.22]  But Go, I feel like it's a little bit more easier to understand the concepts and just go and implement.
[2154.56 --> 2159.52]  I think the biggest advantage of Go is this open source community support that's available, right?
[2159.52 --> 2165.06]  I feel like documentation wise, it's a lot better when compared to some of the other languages we have out there.
[2165.46 --> 2169.88]  So that's my and I mean, I did say I have a favorite, which is Python.
[2170.12 --> 2175.84]  But I do believe that every language has its own reason why it's there, right?
[2176.04 --> 2178.58]  Some for some applications, you need Go.
[2178.82 --> 2180.50]  And for some applications, you need Python.
[2180.70 --> 2181.70]  Some you need C.
[2181.70 --> 2185.52]  So we still use mainframes in some of the applications.
[2186.02 --> 2190.00]  So they've not replaced, they've not been able to replace mainframe, right?
[2190.10 --> 2195.24]  And like some of the banking applications, if you see people, it's still in those applications are still there.
[2195.34 --> 2197.68]  So every language has a reason why it's there.
[2197.82 --> 2200.02]  And as developers, we should be open-minded.
[2200.18 --> 2205.94]  I just feel that we should be open-minded and pick the right language for your use case.
[2206.24 --> 2209.34]  Your use case should completely depend on what you should go for.
[2209.34 --> 2216.28]  And for microservices development, Go is one of the best ones to use.
[2216.78 --> 2220.90]  So to circle back to my original question where I said, why did you choose Go?
[2221.46 --> 2226.00]  If you got this whole problem again to solve, would you still use Go?
[2226.20 --> 2227.00]  Yeah, definitely.
[2227.52 --> 2227.72]  Okay.
[2228.20 --> 2233.30]  I love that, Nithi, for those who are listening to this, Nithi was like straight, yes.
[2233.70 --> 2237.06]  Sam looked to the side and was like, hmm, maybe.
[2237.06 --> 2243.00]  I mean, Sam has found a different language or something.
[2243.50 --> 2245.54]  No, no, no.
[2245.74 --> 2253.30]  I was like, oh, because so right in my current role, I get to work again with Dapr.
[2253.44 --> 2258.18]  And so like in Intel, because we were working with edge-based applications,
[2258.18 --> 2265.10]  we worked with EdgeX foundries for developing our microservices for that framework and those SDKs.
[2265.22 --> 2271.44]  But now that I get to work with Dapr and I'm aware of it, now I'm like, what would this look like in a Dapr environment?
[2271.64 --> 2271.92]  You know?
[2272.48 --> 2273.92]  So that's why I was like, oh.
[2275.04 --> 2276.52]  Because that's also in Go.
[2276.68 --> 2278.34]  So I'm like, I don't know.
[2279.00 --> 2279.88]  The options.
[2279.88 --> 2280.28]  Yes.
[2280.70 --> 2284.66]  So my kind of final question before we jump into unpopular opinions,
[2284.86 --> 2290.94]  although I feel like the Python one was edging on the side of an unpopular opinion, given we're on Go time.
[2291.18 --> 2291.36]  I know.
[2291.36 --> 2298.42]  I mean, as we all know, you're never really done when it comes to technology, when it comes to software engineering,
[2298.52 --> 2302.82]  when it comes to anything, you're just continual iteration, launching new versions, et cetera.
[2303.38 --> 2313.24]  How are you thinking about the development, the iteration of this work, of this project going forward, post-initial launch?
[2313.88 --> 2316.12]  Are you asking about this specific project?
[2316.56 --> 2316.68]  Yeah.
[2316.88 --> 2318.36]  So, you know, just your lives.
[2318.66 --> 2319.76]  How are they going to iterate?
[2319.76 --> 2321.44]  The end of life.
[2322.86 --> 2323.34]  Yeah.
[2323.44 --> 2324.98]  Philosopher question.
[2325.70 --> 2329.26]  I think we need a whole other Go time episode if we're going to ask you that question.
[2330.38 --> 2330.60]  Yeah.
[2330.76 --> 2334.78]  So Intel does not make money by selling software.
[2335.34 --> 2336.72]  That's the first thing.
[2336.82 --> 2339.18]  They make money by selling hardware and chips, right?
[2339.26 --> 2339.86]  Platforms.
[2340.28 --> 2345.32]  So Intel is very, very big on open source community, contributing to open source projects.
[2345.32 --> 2352.84]  So the goal for our project as well or for our team is to build these open source sample projects.
[2353.32 --> 2359.42]  It's also called as reference implementations so that our partners are solution integrators who work with us.
[2359.58 --> 2359.72]  Right.
[2359.72 --> 2365.88]  They can take our solution as a base and they can build their own custom solutions on top of that.
[2365.88 --> 2372.02]  So in general, that's the goal with most of our open source, these open source sample projects that we build.
[2372.28 --> 2374.66]  Now, this particular project, it's a little different.
[2374.84 --> 2379.52]  We are planning to support it as long as we have a customer who is using it.
[2379.52 --> 2385.26]  So if we don't have a customer, then probably we are just not going to support it any longer.
[2385.26 --> 2390.88]  But if we have a customer, we are able to deploy this in a real environment, their environment.
[2391.16 --> 2394.16]  We will be supporting the project going forward.
[2394.44 --> 2394.56]  Yeah.
[2394.66 --> 2396.58]  That's the plan for this project.
[2397.26 --> 2402.82]  And Nitu, isn't the timeline to release the project, that's end of quarter, right?
[2402.92 --> 2403.20]  Yes.
[2403.30 --> 2405.64]  End of quarter is what we are aiming for.
[2406.10 --> 2406.28]  Cool.
[2406.78 --> 2408.60]  Soft commitment to launch.
[2409.52 --> 2413.16]  Awesome.
[2413.26 --> 2418.86]  Well, it's been an absolute pleasure chatting about this project and just general concepts here.
[2419.38 --> 2423.36]  I'm hoping that everyone who is listening now, who is going to listen in the future,
[2423.36 --> 2427.48]  is going to find it as interesting and thought-provoking as I did.
[2427.62 --> 2429.56]  It's a true pleasure to have you both on here.
[2429.96 --> 2436.40]  If you just final thoughts, if you wanted the go-time readers, I guess you can read the transcript,
[2436.40 --> 2443.90]  listeners, watchers, peeps of the world, to take one lesson learning fact away,
[2444.10 --> 2447.24]  can be a fun fact about the project if you'd like, what would it be?
[2447.24 --> 2448.08]  I.e.
[2448.08 --> 2453.62]  If they're fast-forwarding the episode and they just hear this little sound bite, what
[2453.62 --> 2455.64]  would be the most important thing that you want them to take away?
[2455.88 --> 2457.36]  I'll go to maybe you, Sam, first.
[2457.72 --> 2464.72]  I would say my one-liner would be there is so much more to open source than meets the eye.
[2464.72 --> 2466.80]  It's difficult to follow that.
[2467.44 --> 2467.68]  No!
[2468.00 --> 2468.78]  Sorry, Nita.
[2469.32 --> 2477.06]  But yeah, I'm just going to say microservices-based, dockerized solutions are the future, I feel,
[2477.16 --> 2484.20]  because we are moving into an Internet of Things era where more and more of these AI machine
[2484.20 --> 2487.50]  learning models are going to get integrated in the IoT field.
[2487.50 --> 2491.14]  And you need to have microservices-based, containerized solutions.
[2491.66 --> 2497.48]  And for microservices, I've been saying Golang is the language to develop on.
[2497.68 --> 2497.74]  Yeah.
[2498.58 --> 2499.28]  Love it.
[2499.62 --> 2501.80]  Promise I didn't pay you under the table to say it.
[2502.02 --> 2502.48]  I know.
[2502.64 --> 2502.84]  Okay.
[2503.16 --> 2507.68]  Without further ado, I will jump into unpopular opinions.
[2507.68 --> 2517.68]  Unpopular opinions.
[2527.68 --> 2532.08]  Sam, what is your unpopular opinion?
[2532.08 --> 2541.10]  I feel the pressure, but I think my unpopular opinion would have to be Christmas year-round.
[2541.52 --> 2545.92]  I know some people are believers that Christmas starts the day after Thanksgiving.
[2547.16 --> 2549.94]  Some feel it's just the month of December.
[2550.64 --> 2553.18]  But I am a believer of Christmas year-round.
[2553.92 --> 2555.48]  That's my unpopular opinion.
[2555.94 --> 2557.28]  And what would that look like?
[2557.28 --> 2559.92]  Are we saying, like, Christmas gift every day?
[2560.10 --> 2563.64]  Like, wear your jingle bells with pride every day?
[2563.70 --> 2566.88]  Like, what is that manifest as?
[2566.88 --> 2570.26]  So, I mean, the gifts, at first that sounds nice, right?
[2570.30 --> 2571.34]  Getting a gift every day.
[2571.76 --> 2575.06]  But then I'm like, we don't need much to be happy.
[2575.38 --> 2576.78]  So, I think it's the spirit.
[2577.02 --> 2578.76]  The Christmas spirit year-round.
[2579.26 --> 2580.30]  That's what I would go for.
[2580.30 --> 2583.74]  Because, you know, go, we have a lot of spirit in our community.
[2583.94 --> 2585.78]  A lot of passion and excitement.
[2586.22 --> 2588.16]  As you see with our episode, hopefully.
[2588.76 --> 2591.92]  So, I think Christmas spirit year-round, you can't lose.
[2592.50 --> 2592.80]  Okay.
[2593.06 --> 2595.04]  How would you categorize Christmas spirit?
[2595.12 --> 2596.22]  I'm actually quite intrigued by this.
[2596.30 --> 2598.86]  Like, what are the characteristics of Christmas spirit?
[2598.98 --> 2601.60]  Are we thinking, like, the elf of Christmas?
[2601.82 --> 2604.00]  Little cheeky elf energy?
[2604.00 --> 2611.62]  Are we thinking the robust, cozy, comfy, warm hug of a Santa Claus vibes?
[2611.76 --> 2612.40]  Like, what is...
[2612.40 --> 2612.76]  Yes.
[2613.34 --> 2614.42]  Sampta vibes.
[2614.78 --> 2615.22]  Okay.
[2615.76 --> 2619.06]  So, I can't be a cheeky Christmas elf year-round.
[2620.06 --> 2620.50]  Maybe.
[2622.22 --> 2625.72]  No, so, I always like to say Sampta because I go by Sam.
[2625.96 --> 2628.30]  So, it's like Santa Claus or Santa Claus.
[2628.46 --> 2630.00]  Like, year-round, I'd be cool with that.
[2630.16 --> 2633.66]  So, you're the ones who should be giving us gifts, right?
[2633.66 --> 2636.60]  Yeah, so, Sam should give everyone a gift.
[2637.50 --> 2638.82]  That's the conclusion of this.
[2638.92 --> 2645.22]  Sam is committing on the podcast to give everyone a gift in the world every day.
[2645.50 --> 2646.28]  This is what I'm hearing.
[2646.36 --> 2647.00]  Stay tuned.
[2647.38 --> 2647.56]  Yes.
[2648.26 --> 2649.38]  Stay tuned.
[2649.62 --> 2653.10]  She will containerize and package things for you every day.
[2653.20 --> 2653.44]  Yes.
[2653.54 --> 2655.28]  Only if they're wrapped in Go wrapping.
[2655.66 --> 2656.04]  Yeah.
[2656.30 --> 2659.72]  I really love that we could make this Go relevant, side note.
[2659.86 --> 2661.04]  Anyway, I agree.
[2661.04 --> 2665.66]  Okay, so, unpopular opinion, Christmas spirit every day, but it has to be warm, cuddly Santa
[2665.66 --> 2668.38]  or Santa Claus, not cheeky Angelica.
[2669.00 --> 2669.40]  Got it.
[2671.64 --> 2673.20]  Neetu, unpopular opinion?
[2673.48 --> 2673.76]  Yeah.
[2674.02 --> 2678.22]  So, I'm like, it's a little bit more on the technical side.
[2678.22 --> 2685.00]  So, 25, probably 20, 25 years back when I was in college, when we were learning about
[2685.00 --> 2689.58]  software development, we had this strategy that, you know, you should be architecting
[2689.58 --> 2695.24]  and designing 40% of your time and then 20% you should be coding and the remaining 40%
[2695.24 --> 2696.00]  is on testing.
[2696.00 --> 2702.36]  So, recently I saw on, like, Twitter, we are spending way too much time on testing, trying
[2702.36 --> 2704.82]  to fix all the corner cases.
[2705.46 --> 2709.72]  Instead, we should be figuring out how to handle these corner cases.
[2709.98 --> 2714.40]  How do we graciously fail, right, without pulling the entire application down?
[2714.40 --> 2720.44]  So, I felt like that is an unpopular opinion because I've seen a lot of corner cases when
[2720.44 --> 2726.44]  it comes to these AI ML solutions, like, a lot of them because it is a new field, right?
[2726.98 --> 2730.12]  Models don't work as they do in production.
[2730.96 --> 2737.12]  So, maybe we should be focusing more on how do we fail graciously rather than, you know,
[2737.14 --> 2743.16]  trying to find a solution to all these, like, corner cases or test all these corner cases.
[2743.16 --> 2744.18]  So, yeah.
[2744.64 --> 2748.66]  That's a thought-provoking comment, I think, more than an unpopular.
[2748.84 --> 2749.46]  I love it, though.
[2749.68 --> 2750.88]  Gives me a lot to think about.
[2751.28 --> 2751.52]  Okay.
[2751.86 --> 2756.66]  So, the percentages need to shift and we need to stop trying to make sure that things aren't
[2756.66 --> 2762.42]  going to fail and start thinking more about when they fail, because they will, how are
[2762.42 --> 2765.22]  we going to deal with that in a graceful manner?
[2765.66 --> 2767.14]  Not like a cheeky Christmas elf.
[2767.86 --> 2768.62]  That's hard.
[2770.58 --> 2772.34]  Well, thank you so, so much.
[2772.34 --> 2774.80]  But, regrettably, we are out of time.
[2775.06 --> 2779.28]  I would love to have you both on, speak more about everything and anything, really.
[2779.38 --> 2780.02]  You're both a joy.
[2780.92 --> 2783.88]  So, please have a great rest of your day.
[2784.02 --> 2787.12]  Let me know if you have any other cool projects to chat about.
[2787.60 --> 2791.80]  And without further ado, we're going to do a little GoTime outro.
[2791.80 --> 2793.22]  All right.
[2793.22 --> 2797.30]  All right.
[2797.48 --> 2799.06]  That is GoTime for this week.
[2799.30 --> 2800.06]  Thanks for listening.
[2800.70 --> 2803.98]  Have you heard about our recent refresh of the Changelog podcast?
[2804.64 --> 2806.52]  It is now three shows in one.
[2807.00 --> 2812.80]  Changelog news on Mondays, our classic interview on Wednesdays, and on Fridays, a brand new talk
[2812.80 --> 2814.00]  show for your weekend listening.
[2814.00 --> 2818.36]  It's like putting the hallway track at your favorite conference on repeat all year round.
[2818.84 --> 2823.30]  So, if you haven't listened to the Changelog in a bit, now's a good time to give it another go.
[2823.78 --> 2828.82]  Thanks once again to our partners for helping us bring you awesome developer pods each and every week.
[2829.18 --> 2833.84]  Check them out at Fastly.com, Fly.io, and Typesense.org.
[2833.84 --> 2840.72]  And thank you, of course, to the mysterious Breakmaster Cylinder for producing every beat on every Changelog podcast.
[2841.22 --> 2845.58]  That is all for now, but we'll talk to you again next time on GoTime.
[2863.84 --> 2872.70]  Game on.
