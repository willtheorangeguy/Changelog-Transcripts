[0.22 --> 5.62]  You are listening to ShipIt, a podcast about operations, infrastructure, and the people
[5.62 --> 7.00]  that are Kubernetes-ing.
[8.04 --> 8.56]  Kubernetes-ing.
[9.28 --> 10.78]  K-T-ing, you know what I mean.
[11.44 --> 16.62]  I'm your host, Gerhard Lassil, and in this episode, I'm joined by Tamer Saleh, founder
[16.62 --> 20.40]  of Super Orbital and former VP of Engineering at Pivotal.
[20.86 --> 25.28]  Many years ago, we both used to work in the same London office on Cloud Foundry, and nowadays
[25.28 --> 26.44]  we are into Kubernetes.
[26.44 --> 31.32]  We start with table tennis, remote work, and then we spend the rest of the time talking
[31.32 --> 33.98]  about the challenges that teams have with Kubernetes.
[34.60 --> 39.26]  Tamer and his Super Orbital team are deeply experienced in this topic, and they help teams
[39.26 --> 44.78]  at companies like Bloomberg, Shopify, and federal US agencies tackle hard Kubernetes and DevOps
[44.78 --> 47.22]  problems through engineering and training.
[47.66 --> 50.40]  So why do companies need Kubernetes in the first place?
[50.80 --> 52.80]  Which are the right reasons for choosing it?
[53.14 --> 54.60]  Is Kubernetes even a platform?
[54.60 --> 59.54]  My favorite, I'm doing Kubernetes wrong, but it works better than when I was doing
[59.54 --> 59.98]  it right.
[60.24 --> 61.16]  So what's up with that?
[61.58 --> 63.22]  This last one was a lot of fun.
[63.54 --> 66.76]  And, as your request, we left the entire minute of laughter in.
[67.08 --> 70.66]  Big thanks to our partners Fastly, LaunchDarkly, and Linode.
[71.02 --> 72.82]  Thank you for the great bandwidth Fastly.
[73.26 --> 75.34]  You can learn more at Fastly.com.
[75.86 --> 80.10]  Ship new features with confidence by getting your feature flags powered by LaunchDarkly.com.
[80.10 --> 83.70]  And thank you, Linode, for keeping our Kubernetes fast and simple.
[84.20 --> 88.28]  Run your setup as we do via Linode.com forward slash changelog.
[88.28 --> 98.70]  This episode is brought to you by Honeycomb.
[99.16 --> 103.76]  Honeycomb is built on the belief that there's a more efficient way to understand exactly what
[103.76 --> 105.84]  is happening in production right now.
[105.84 --> 109.96]  When production is running slow, it's hard to know exactly where problems originate.
[110.26 --> 114.18]  Is it your application code, your users, or the underlying systems?
[114.18 --> 119.02]  Teams who don't use Honeycomb scroll through endless dashboards guessing at what they mean.
[119.26 --> 123.56]  They deal with alert floods, guessing which ones matter, and go from tool to tool to tool,
[123.86 --> 125.72]  guessing at how the puzzle pieces all fit together.
[126.04 --> 129.70]  It's this context switching and tool sprawl that are slowly killing your teams and your
[129.70 --> 130.16]  business.
[130.56 --> 135.06]  With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving
[135.06 --> 136.44]  your business, production.
[136.88 --> 140.94]  Honeycomb quickly shows you the correct source of issues, discover hidden problems, even in
[140.94 --> 145.24]  the most complex stacks, understand why your app feels slow to only some users.
[145.66 --> 148.12]  With Honeycomb, you guess less and no more.
[148.56 --> 153.04]  Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[153.04 --> 156.02]  Again, honeycomb.io slash changelog.
[156.02 --> 172.60]  We are going to ship in three, two, one.
[186.02 --> 190.50]  It's been several years since we worked together, 2016, 2017.
[191.44 --> 196.08]  And I think it's been too long since you and me played the game of table tennis.
[196.54 --> 197.14]  How's your game?
[197.24 --> 201.20]  I was so bad at table tennis.
[202.16 --> 203.06]  That's not true.
[203.46 --> 204.02]  That's not true.
[204.16 --> 205.18]  I've seen the improvement.
[206.00 --> 208.26]  I've seen those years in which you really improved.
[208.66 --> 211.02]  And the last games that we've had were really good.
[211.12 --> 212.06]  So I enjoyed them.
[212.20 --> 212.92]  It was a lot of fun.
[212.92 --> 217.04]  I don't know if you know this, it was never official, but it always kind of seemed like
[217.04 --> 221.86]  your seniority at Pivotal would directly correlate with how good you were at table tennis.
[222.84 --> 223.24]  Yes.
[224.52 --> 226.90]  I knew that, but I never mentioned it to anyone.
[227.04 --> 228.60]  I think it was like a little thing.
[228.74 --> 229.00]  Yes.
[229.68 --> 233.50]  I'm pretty sure most of my engineers let me win just to make me feel better.
[233.86 --> 234.58]  I'm sorry.
[235.02 --> 235.80]  Not me.
[236.98 --> 238.54]  No, we had some great games.
[238.68 --> 241.18]  So did you play much in the last three, four years?
[241.40 --> 242.18]  Not at all.
[242.30 --> 242.82]  Not at all.
[242.94 --> 244.52]  I mean, it was entirely a Pivotal thing.
[244.62 --> 246.60]  It was like part of, built into the Pivotal culture.
[246.78 --> 250.72]  You know, you're pair programming and you need a quick 15 minute break where you get
[250.72 --> 255.80]  up and you jump around and there's table tennis tables right there and you're playing doubles.
[255.94 --> 256.76]  So you're a pair.
[256.98 --> 258.72]  You find another pair that also needs a break.
[258.78 --> 261.34]  I mean, everything about it was just built around Pivotal.
[261.60 --> 261.80]  Yeah.
[261.90 --> 262.70]  I really miss that.
[262.70 --> 267.24]  Like from the whole office culture, which seems to be slowly disappearing when it comes
[267.24 --> 268.26]  to remote work.
[268.26 --> 273.66]  And, you know, this is like the new norm and we're in it for the long drive, shall I say.
[273.66 --> 278.98]  I really miss that table tennis, that social aspect, that, I mean, pairing is great.
[279.06 --> 279.80]  You can do it remotely.
[279.80 --> 282.36]  But what you can't do remotely is play table tennis.
[282.36 --> 283.10]  It's true.
[283.20 --> 287.44]  I mean, I've always been very passionately 100% remote.
[287.54 --> 291.12]  Our company has always been 100% remote, even before the apocalypse.
[291.50 --> 295.04]  And that made the apocalypse a little bit easier for us to weather as a company.
[295.04 --> 299.92]  But I do miss that camaraderie of going out to lunch together, that camaraderie of playing
[299.92 --> 301.48]  a game of table tennis together.
[302.00 --> 307.20]  And obviously there's a tax to being remote when it comes to communication, right?
[307.38 --> 310.54]  Communication is just more fluid when you're sitting right there.
[310.96 --> 313.82]  At the same time, there's always benefits one side or the other.
[314.26 --> 321.46]  And I think the benefits of being able to find amazing talent who's uninterested in moving
[321.46 --> 327.20]  to some central location and the benefit of everyone in the company being on equal footing.
[327.66 --> 331.92]  You know, the companies that do remote where there's a mothership and small offices, the
[331.92 --> 335.76]  small offices always feel like their growth is going to be stunted.
[335.76 --> 340.36]  And it is because they're not close to leadership and close to where the decisions are made.
[340.74 --> 346.54]  And even more important, and this is, I think this is more of a, about American culture and
[346.54 --> 351.44]  what's been happening to American culture over the past, I don't know, 20, 30, 40 years.
[352.10 --> 357.72]  As people congregate more into the cities, we are getting a very strong cultural divide.
[357.80 --> 361.20]  It's probably happening in other places too, but for us, it's incredibly strong between
[361.20 --> 363.90]  the cities and the countryside, right?
[364.62 --> 371.94]  And I feel like the more fully remote various companies move towards, the better it's going
[371.94 --> 377.68]  to be for society because you get people from different backgrounds all working together
[377.68 --> 379.56]  and you start to flatten out the cities.
[379.56 --> 383.98]  I think cities are not a great thing from a cultural point of view, right?
[384.36 --> 388.16]  They're a huge strain on infrastructure and it would just be much better if we could just
[388.16 --> 392.40]  flatten them a bit and have the small towns grow a bit bigger in the countrysides.
[392.56 --> 394.22]  And I think fully remote allows that.
[394.52 --> 395.44]  Yeah, I can see that.
[395.52 --> 399.24]  And I do have to say, having left a big city not that long ago, I mean, I'm still around
[399.24 --> 399.38]  it.
[399.42 --> 402.26]  I'm still around London, but I'm not living in London anymore.
[402.26 --> 408.00]  And I do appreciate the advantages to that, but I can also see some of the trade-offs.
[408.16 --> 409.98]  So there's always some trade-offs.
[410.26 --> 411.46]  We miss the really good dinners.
[412.14 --> 412.54]  Yeah.
[412.94 --> 413.90]  And the table tennis.
[414.30 --> 415.40]  And the table tennis, yeah.
[415.86 --> 416.14]  Okay.
[416.58 --> 421.38]  Now, one other topic that I know that you're really passionate about besides dinners and
[421.38 --> 422.64]  table tennis is Kubernetes.
[423.06 --> 423.78]  It's true.
[423.86 --> 424.32]  It's true.
[424.80 --> 425.40]  Same here.
[425.50 --> 425.88]  Same here.
[425.94 --> 426.44]  Big fans.
[426.44 --> 433.36]  So I know that you're seeing so many things around Kubernetes, so many social interactions,
[433.92 --> 436.86]  so many teams interacting with Kubernetes.
[437.58 --> 437.70]  Yeah.
[437.90 --> 444.70]  And I see companies these days, they no longer say, oh, Kubernetes is interesting.
[444.94 --> 445.88]  Maybe I should try it out.
[445.98 --> 447.68]  They need Kubernetes.
[448.26 --> 453.42]  And that's a very interesting mind shift which happened, I think, in the last maybe year,
[453.50 --> 453.94]  two years.
[453.94 --> 460.16]  So a company, when they start with Kubernetes, what problems do you see them having?
[460.44 --> 461.36]  Yeah, that's a great question.
[461.70 --> 463.26]  And just to put a little bit of context in it.
[463.54 --> 466.48]  So at Super Orbital, we have kind of two lines of business.
[466.72 --> 470.36]  One of the lines of business is, the biggest one is our engineering services.
[470.52 --> 474.10]  We help companies out with very difficult Kubernetes-related problems.
[474.30 --> 480.70]  We have a very small team of very senior, seasoned engineers with a lot of judgment.
[480.70 --> 487.38]  And when one of our clients has a very unusual and challenging problem with Kubernetes, like
[487.38 --> 492.76]  going on-premise via Kubernetes or doing some very deep security stuff with Kubernetes.
[492.92 --> 495.40]  That's when they bring us on board for short-term engagements, whatever.
[495.54 --> 495.96]  We help out.
[496.26 --> 501.74]  We also have a smaller part of our business, which is producing workshops and training.
[501.74 --> 506.78]  And the reason that I bring this up is because when we are doing our workshops, that's when
[506.78 --> 512.38]  we engage more with companies who are just starting to embrace Kubernetes, right?
[512.46 --> 520.68]  So we don't help those customers on the engineering front as often, but more likely, we get to train
[520.68 --> 525.18]  them and show them how complex Kubernetes is.
[525.46 --> 527.42]  That's the key problem with Kubernetes.
[527.42 --> 533.32]  I mean, everybody who's used it knows it, but the complexity is huge.
[533.62 --> 541.52]  I mean, there's something like 80 different resource types that the Kubernetes API understands
[541.52 --> 542.28]  the last time I looked.
[542.50 --> 549.94]  And each one of those can have dozens or hundreds of attributes that you have to, to some degree,
[550.06 --> 550.66]  understand.
[550.66 --> 557.64]  And especially as you're doing production workloads in Kubernetes, the defaults are not always
[557.64 --> 559.06]  in your favor, right?
[559.14 --> 564.22]  So things like affinity rules and stuff, which this stuff is improving, but affinity rules,
[564.64 --> 569.86]  security, all that stuff is things that are kind of left as an exercise to the reader with
[569.86 --> 570.20]  Kubernetes.
[570.58 --> 572.54]  And so the complexity is just enormous.
[573.04 --> 577.86]  And new releases, they used to happen quarterly and now literally slowed it down because quarterly
[577.86 --> 578.56]  was too fast.
[578.56 --> 581.96]  So now it's every three, three times a year, you know, new releases.
[582.16 --> 587.18]  Sure, it's a minor number, but we all know that in Kubernetes world, like the miners are
[587.18 --> 588.38]  basically majors, right?
[588.44 --> 591.24]  So, you know, 1.23 is around the corner right now.
[591.72 --> 593.28]  By the time this is published, it'll probably be out.
[593.68 --> 600.52]  And the interesting thing to me is that the original authors of Kubernetes, they never envisioned
[600.52 --> 605.58]  that Kubernetes would be used directly by application developers.
[605.78 --> 607.14]  That's fascinating to me, right?
[607.14 --> 613.44]  There's some tweet by Joe Beta where he said that they always viewed YAML as an implementation
[613.44 --> 614.04]  detail.
[614.18 --> 618.28]  It's like the assembly language or whatever, the API that you would talk to Kubernetes via,
[618.38 --> 622.72]  and there would always be something on top of it that would smooth over the rough edges
[622.72 --> 626.92]  and take care of a lot of that complexity and make all those decisions for the developers,
[627.12 --> 627.84]  for the engineers.
[628.20 --> 629.70]  But yeah, here we are, right?
[629.70 --> 634.50]  We are all wrangling YAML in order to use Kubernetes.
[634.76 --> 641.28]  So absolutely, when we train our customers in Kubernetes, our most popular workshop is
[641.28 --> 645.52]  this core Kubernetes workshop where it's like you just want to get your application developers
[645.52 --> 647.50]  up to speed on how to use Kubernetes.
[647.90 --> 650.30]  The complexity is just astounding.
[650.30 --> 655.76]  And you need all of your engineers to understand it if they're going to carry the pager, especially
[655.76 --> 662.02]  a smaller company where your application engineers need to be able to debug issues with their
[662.02 --> 663.12]  applications in the cluster.
[663.44 --> 667.64]  When things go sideways, they need far more knowledge than you would expect.
[667.64 --> 673.70]  So when companies come to you saying that, hey, Tamer and your awesome super orbital team,
[673.88 --> 674.56]  we need help.
[674.80 --> 675.84]  We really need help.
[676.10 --> 677.52]  What do they need help with?
[677.64 --> 678.20]  Is it training?
[678.48 --> 680.20]  Is it running stuff?
[680.44 --> 681.30]  What does that look like?
[681.50 --> 685.68]  We don't do, because of the nature of who we hire and how we're positioned, we don't like
[685.68 --> 687.34]  help with maintenance on clusters.
[687.34 --> 691.82]  We don't help with on-call or upgrading clusters and that kind of stuff, which it just doesn't
[691.82 --> 693.82]  make sense to engage with us for that kind of thing.
[693.82 --> 700.24]  But customers definitely come to us for training and they come to us, like I said, for the harder
[700.24 --> 702.04]  Kubernetes problems.
[702.82 --> 706.56]  Can you give us a few examples, like some hard Kubernetes problems that companies struggle
[706.56 --> 708.04]  with or teams struggle with?
[708.18 --> 714.64]  Yeah, we have a couple of clients who are attacking on-premise installations for their
[714.64 --> 714.92]  product.
[715.00 --> 720.28]  They have a product that they run, but they want to deliver it to other companies on-premise
[720.28 --> 725.08]  in the other companies, AWS accounts or even bare metal or whatever.
[725.86 --> 732.52]  And the interesting thing about Kubernetes is that it is becoming that ubiquitous platform.
[732.96 --> 738.30]  It is becoming that assumption that you can make that if I'm going to go on-premise, I want
[738.30 --> 743.20]  to target Kubernetes because that's going to hit the 80% of my potential customers.
[743.20 --> 744.52]  That's easily becoming the case.
[744.52 --> 750.80]  And going on-premise is very difficult, even with a substrate like Kubernetes to lean on,
[750.88 --> 753.90]  because often you get zero telemetry, right?
[754.08 --> 758.24]  You get no metrics, no logs, no hands on the keyboard.
[758.38 --> 761.06]  You can't kubectl exec into something and fix it.
[761.26 --> 767.06]  Usually with these engagements, it's with, or usually for our clients, their customers are
[767.06 --> 773.08]  highly regulated, highly secure companies that have very strong security postures.
[773.08 --> 779.20]  And so what our clients need is not only to believe that what they are going to be deploying
[779.20 --> 785.86]  into their customers' Kubernetes environments are well-engineered and using all of the best
[785.86 --> 790.16]  practices from Kubernetes' point of view, but often they also need a lot of custom code
[790.16 --> 792.94]  developed in order to do health checks.
[793.32 --> 800.38]  For one customer, we actually built a dashboard that their customers can go to and see the health
[800.38 --> 804.60]  of their application, but also the health of the underlying cluster, basically so that
[804.60 --> 809.46]  their customers can self-select into, should I file a ticket or is it actually a problem
[809.46 --> 812.16]  with our own cluster and we need to go to our own operations team?
[812.34 --> 814.30]  That kind of thing is fundamentally important.
[814.72 --> 820.00]  And when we were at Cloud Foundry, we have so much experience with the headaches of trying
[820.00 --> 825.62]  to ship on-premise that we just naturally, that's why we ended up with all these customers
[825.62 --> 828.04]  doing it, because we just had that experience already.
[828.04 --> 834.54]  Another fun example is we had a crypto client who wanted to integrate AWS Nitro Secure Enclaves
[834.54 --> 835.68]  with EKS.
[836.46 --> 842.86]  And the Nitro Enclave thing is a really interesting technology where you can run verified code
[842.86 --> 849.52]  in a highly secure hardware-based environment that has to be built into the chips on the actual
[849.52 --> 851.18]  machines that AWS gives you.
[851.18 --> 855.92]  And even AWS engineers cannot access the memory for that code.
[856.04 --> 857.78]  But using it is a huge pain.
[857.94 --> 859.94]  I mean, using it is incredibly difficult.
[860.60 --> 865.86]  And the code that runs inside this secure enclave cannot do things like network or anything.
[866.14 --> 870.12]  You can only communicate with it through this weird VSOC that happens at the kernel level.
[870.12 --> 873.54]  And so integrating that with EKS turned out to be very challenging.
[873.92 --> 875.66]  And so they brought us on board to help out with that.
[876.22 --> 881.68]  And as it turns out, we were, I think, maybe still the only people who have done that integration,
[881.86 --> 886.56]  the only people who have tied EKS and Nitro together so that you could launch a secure
[886.56 --> 890.70]  enclave from a pod and communicate with it directly from that pod.
[890.70 --> 895.20]  And we know that because we actually had to work with the AWS engineering team to get it done.
[895.74 --> 896.52]  And it was a lot of fun.
[896.68 --> 898.02]  And we got, you know, we blogged about it.
[898.28 --> 900.40]  And the engineer loved that work.
[900.54 --> 904.28]  It's part of the reason why we can attract such senior talent is because we get to work
[904.28 --> 905.86]  on the more interesting projects like that.
[906.14 --> 906.26]  Right.
[906.42 --> 907.38]  You've made so many things.
[907.72 --> 910.50]  And I'm going to ask one thing, which is very close to my heart.
[910.66 --> 915.54]  So in Cloud Foundry, we knew to use Bosch to manage Cloud Foundry.
[915.74 --> 915.96]  Yeah.
[915.96 --> 920.34]  Is there such a thing in Kubernetes where when you deploy Kubernetes on bare metal,
[920.70 --> 921.62]  what would you say?
[921.76 --> 927.06]  What, like, what should users or teams use for that management of Kubernetes on bare metal
[927.06 --> 927.78]  or on-prem?
[928.02 --> 931.88]  There's a variety of tools for deploying Kubernetes to bare metal installations.
[932.28 --> 935.86]  And that's not really the hard part with Kubernetes.
[936.16 --> 939.06]  In the cloud, there's managed Kubernetes and that solves all your problems.
[939.18 --> 942.04]  But that's really, that's not the problem with Kubernetes in complexity.
[942.04 --> 946.12]  In fact, getting a Kubernetes cluster up and running is fairly easy.
[946.76 --> 950.40]  On bare metal, you have some issues with the networking, but there's projects to solve that
[950.40 --> 955.54]  you've got Kube router and you've got Metal LB and you've got others that solve that problem
[955.54 --> 955.94]  for you.
[956.20 --> 958.74]  It's interesting that you brought up Bosch and Cloud Foundry.
[958.82 --> 963.52]  And for those who don't know, the way that Cloud Foundry was designed was that we had two
[963.52 --> 964.24]  different products.
[964.60 --> 972.22]  We had Bosch, which was sort of a competitor to Terraform and Ansible and Salt.
[972.54 --> 978.08]  I think, I don't know this for sure, but I think it came right out of the Google's Borg.
[978.08 --> 980.48]  It's like a rewrite of Borg, basically.
[980.66 --> 983.00]  And it's very difficult to use.
[983.12 --> 988.28]  But once you use it, like once you learn it, Stockholm syndrome kicks in and you start to
[988.28 --> 988.50]  love it.
[988.56 --> 991.20]  There's huge Bosch fanatics, right?
[991.34 --> 994.58]  And Bosch was the tool that the operator used to deploy Cloud Foundry.
[994.68 --> 996.74]  Very difficult to use, but very powerful.
[997.16 --> 1003.18]  And Cloud Foundry was the interface that the operator then could present to the application
[1003.18 --> 1007.80]  developers, which was basically a blatant ripoff of Heroku, which was a great model.
[1008.10 --> 1013.24]  12 factor build packs, all that stuff made it real easy for application developers.
[1013.70 --> 1014.58]  But here's the interesting thing.
[1014.82 --> 1021.12]  I refer to that as the great wall DevOps model, where Cloud Foundry allowed the operator to
[1021.12 --> 1028.58]  serve the application developer well by giving the operator this beautiful wall that both sides
[1028.58 --> 1029.50]  really appreciated.
[1029.50 --> 1033.48]  The operator appreciated how easy it was to manage Cloud Foundry through Bosch and the
[1033.48 --> 1038.04]  application developer appreciated how powerful it was for them to manage their application
[1038.04 --> 1039.34]  through Cloud Foundry.
[1040.22 --> 1042.00]  Kubernetes is entirely different from that, right?
[1042.08 --> 1047.52]  Kubernetes is what I call the kumbaya DevOps model, where everybody has to know everything,
[1047.74 --> 1047.96]  right?
[1048.32 --> 1052.06]  Kubernetes doesn't have the concept of an operator versus an application developer.
[1052.06 --> 1058.68]  At best, it gives you some tools where you can kind of build that using RBACs and stuff,
[1058.74 --> 1060.76]  but that's really difficult to do.
[1061.22 --> 1064.12]  And nobody knows quite where the line is supposed to be.
[1064.60 --> 1066.96]  And so, yeah, so everybody does it differently, you know?
[1067.48 --> 1067.64]  Yeah.
[1068.18 --> 1068.48]  Okay.
[1068.98 --> 1071.32]  So they do have YAML in common.
[1074.32 --> 1075.30]  That's still around.
[1076.52 --> 1078.86]  That's like still a paid, but maybe not for long.
[1078.94 --> 1079.30]  Who knows?
[1079.38 --> 1079.72]  We'll see.
[1079.72 --> 1080.12]  Okay.
[1080.12 --> 1086.62]  So what I'm taking away from this is that Kubernetes is everywhere and Teams, they need
[1086.62 --> 1090.08]  Kubernetes because it's the easiest way to get something out there.
[1090.16 --> 1090.76]  It's ubiquitous.
[1090.90 --> 1091.46]  It's everywhere.
[1091.92 --> 1092.06]  Yeah.
[1092.12 --> 1093.96]  And it handles the complexity really well.
[1094.14 --> 1094.98]  So you're right.
[1095.08 --> 1099.02]  The 80 resource types plus all the custom ones that you can install.
[1099.12 --> 1101.06]  And typically you get via CRDs.
[1101.28 --> 1101.46]  Yeah.
[1101.58 --> 1103.52]  You get even more and they get even more complicated.
[1103.52 --> 1109.56]  It's a great way of modeling some really complex software, whether it's microservices, whether
[1109.56 --> 1111.30]  it's stateful services.
[1111.30 --> 1115.50]  And that's like, hmm, not fully, but it's getting there for sure.
[1115.90 --> 1120.12]  I think there was like a maturity level that had to happen at the data services side as well.
[1120.12 --> 1122.54]  Just understand that operating model.
[1122.54 --> 1123.88]  It's not just ubiquitous.
[1124.02 --> 1125.92]  It's just becoming the standard, right?
[1126.00 --> 1132.76]  It's expected that if you're going to, as you said, model out your infrastructure, your
[1132.76 --> 1138.02]  application infrastructure, then you're going to do it in YAML using Kubernetes objects, right?
[1138.02 --> 1139.26]  So that you can deploy it anywhere.
[1139.48 --> 1143.48]  And there are some really great projects in this Kubernetes ecosystem and in the bigger cloud
[1143.48 --> 1145.60]  native ecosystem, which work well together.
[1145.60 --> 1152.06]  But it's intricacy of finding the right combination of the objects or like the products that make
[1152.06 --> 1152.76]  sense to you.
[1152.92 --> 1154.72]  And that's where the complexity lies in.
[1154.86 --> 1158.84]  So the kumbaya, anything goes and everything goes.
[1158.96 --> 1163.12]  And by the way, there are teams for which a certain combination makes sense, which would
[1163.12 --> 1164.32]  never work for other teams.
[1164.44 --> 1165.90]  And that's what gives it the beauty.
[1166.02 --> 1166.76]  Also the complexity.
[1167.28 --> 1168.54]  It's building blocks, right?
[1168.62 --> 1170.90]  The entire community is all about building blocks.
[1170.90 --> 1176.40]  And if you have a large enough team that you can dedicate a couple of people to choosing
[1176.40 --> 1181.16]  the right building blocks and wiring them all together and producing this really great
[1181.16 --> 1183.78]  experience for your engineers, then that's great.
[1184.02 --> 1186.30]  Do you think that teams would be better without Kubernetes?
[1186.70 --> 1186.96]  Yeah.
[1187.24 --> 1193.26]  I mean, again, it depends on the size of the team, but I'm going to just ballpark that 30%
[1193.26 --> 1198.34]  ish of people who come to us saying, we're looking to embrace Kubernetes.
[1198.42 --> 1199.24]  We're going to move to Kubernetes.
[1199.24 --> 1204.68]  And we'd like your training or your help on the engineering side to get it done and to
[1204.68 --> 1205.24]  get it done right.
[1205.50 --> 1211.00]  About 30% of the time when people come to us asking for that, we try really hard to convince
[1211.00 --> 1211.74]  them not to.
[1212.16 --> 1219.02]  Because if you're a small startup, then unless you're doing something really complicated,
[1219.24 --> 1222.28]  then it's just too much for you, right?
[1222.36 --> 1225.40]  I mean, you're not focused on your own innovation.
[1225.40 --> 1229.14]  Instead, you're focused on managing Kubernetes.
[1229.58 --> 1230.40]  So here's the story.
[1230.62 --> 1235.46]  When I was, I don't know, through most of my life, I've been a Linux user until around
[1235.46 --> 1237.90]  2006, I think it was.
[1238.26 --> 1241.44]  And I used to run Linux on all kinds of hardware.
[1241.78 --> 1246.04]  I ran, I was one of those geeks in college that had a small network of, you know, like
[1246.04 --> 1248.52]  Sun and different servers and things like that.
[1248.52 --> 1252.60]  And for the longest time, I ran Linux on my laptop as my daily driver.
[1253.16 --> 1259.42]  And around 2006, I realized that I was spending 20% of my time trying to figure out how to
[1259.42 --> 1263.24]  close my ThinkPad without the kernel panicking, right?
[1265.00 --> 1268.28]  It's like about an hour a day, every day, you know?
[1268.86 --> 1269.68]  Doesn't want to sleep.
[1270.00 --> 1270.72]  Linux doesn't sleep.
[1271.16 --> 1272.20]  Yeah, it's just it.
[1272.28 --> 1273.84]  Yeah, it's always working for you, you know?
[1274.28 --> 1277.74]  And I just flipped the table, I bought a Mac, and I never looked back, right?
[1278.02 --> 1282.10]  To me, the analogy is that Kubernetes is that Linux on the laptop experience, right?
[1282.16 --> 1286.78]  There's always going to be problems, because you're always integrating two dozen different
[1286.78 --> 1290.32]  technologies to get a full Kubernetes system running.
[1290.58 --> 1294.52]  And it's fine if you have administrators there to focus on that task.
[1294.52 --> 1298.50]  But if you're, you know, a 10 person startup, that's not where you need to be.
[1298.50 --> 1304.26]  You should be on like Heroku or Fly.io or what's the other one?
[1304.30 --> 1307.68]  Nitrous or Google Cloud Run, Fargate, like any of those, right?
[1307.86 --> 1308.04]  Yeah.
[1308.20 --> 1310.10]  Are better choices than Kubernetes.
[1310.38 --> 1316.70]  The litmus that we give these people when they come to us is stay on these fully managed
[1316.70 --> 1318.56]  platforms for as long as you can.
[1318.66 --> 1322.50]  And every time an engineer says, we should really use Kubernetes for this, that, or the
[1322.50 --> 1326.98]  other, you say, no, we should stay within the confines of a 12-factor app, like as much
[1326.98 --> 1327.94]  as you can, right?
[1327.94 --> 1332.46]  You change your product definition so that you can stay within that confine, whatever
[1332.46 --> 1338.46]  you can do, until you really believe that you need to provision raw EC2.
[1338.94 --> 1343.32]  When an engineer says, look, this is an important feature, the only way we can get this feature
[1343.32 --> 1347.10]  done is if you give me the keys to AWS, because I need to provision some instances, we're going
[1347.10 --> 1350.36]  to configure those instances, we're going to run systemd on them, we're going to tie in
[1350.36 --> 1353.42]  all the logging and all the metrics into some sort of centralized system, we're going
[1353.42 --> 1355.90]  to have alerting and everything set up and all of that.
[1355.90 --> 1358.32]  That's when you say, no, no, no, no, no, no.
[1358.40 --> 1365.00]  We're never going to provision raw instances because Kubernetes is the future for all things
[1365.00 --> 1369.22]  cloud level, all things that would be infrastructure as a service.
[1369.34 --> 1370.82]  Instead, you should be using Kubernetes.
[1371.12 --> 1372.34]  That's the inflection point.
[1372.34 --> 1387.74]  This episode is brought to you by our friends at Incident.io.
[1388.14 --> 1392.42]  Every software team on the planet has to manage incidents and a very large percentage of those
[1392.42 --> 1394.34]  teams are using Slack to communicate.
[1394.52 --> 1395.50]  That includes us.
[1395.50 --> 1400.76]  With Incident.io, you can create, manage, and resolve incidents directly inside Slack.
[1401.04 --> 1401.96]  Here's how it works.
[1402.22 --> 1404.30]  Head to Incident.io and sign up for free.
[1404.52 --> 1405.94]  Then add it to your Slack.
[1406.10 --> 1409.96]  From there, you have a brand new incidents channel where all incidents get announced.
[1410.34 --> 1412.90]  Use the slash incident command to create and manage incidents.
[1413.32 --> 1418.64]  This command lets you share updates, assign roles, set important links, and more, all without
[1418.64 --> 1419.92]  ever leaving the incident channel.
[1419.92 --> 1425.84]  Each incident gets their own Slack channel plus a high-res dashboard at Incident.io with
[1425.84 --> 1427.76]  the entire timeline from report to resolution.
[1428.30 --> 1431.50]  Get everyone on the same page from the moment they join the incident and help stakeholders
[1431.50 --> 1432.36]  stay in the loop.
[1432.72 --> 1436.86]  Add Incident.io to your Slack today and prove to yourself and your team that they have everything
[1436.86 --> 1438.46]  you need to streamline your incident management.
[1438.94 --> 1441.36]  Learn more and sign up for free at Incident.io.
[1441.66 --> 1442.72]  No credit card required.
[1443.22 --> 1444.62]  Again, Incident.io.
[1449.92 --> 1464.08]  I think that you've heard this question many times before, and I still have to ask it.
[1464.32 --> 1467.48]  Do you think that Kubernetes would have been as popular and successful?
[1467.82 --> 1468.70]  Was it not for Docker?
[1469.20 --> 1469.52]  Yeah.
[1469.70 --> 1470.56]  Yeah, that's a great question.
[1470.90 --> 1472.18]  I mean, obviously, who knows?
[1472.18 --> 1478.22]  But from my point of view, I don't think Kubernetes would have gotten off the ground at all if
[1478.22 --> 1481.94]  it wasn't for Docker as a standard, right?
[1482.14 --> 1484.06]  We all know that Docker is a company.
[1484.48 --> 1487.66]  They had an opportunity and they just couldn't quite execute on it.
[1487.84 --> 1489.02]  So whatever.
[1489.20 --> 1490.08]  That is what it is.
[1490.48 --> 1498.06]  But the thing that Docker gave to the technology community is that standard of what it means
[1498.06 --> 1499.06]  to be a container.
[1499.06 --> 1504.50]  And we all know that there were containers before Docker, right?
[1504.60 --> 1506.08]  I mean, LXD, LXD.
[1506.34 --> 1510.34]  There was Solaris Zones, FreeBSD Jails, sort of, right?
[1510.60 --> 1513.92]  And things like Solaris Zones arguably were better, if I remember correctly.
[1514.06 --> 1516.56]  They ran separate kernels per container, right?
[1516.78 --> 1524.00]  But it was that standardization of how you create a container and what a container or how
[1524.00 --> 1526.62]  you create a container image and what a container image actually is.
[1526.62 --> 1531.02]  And that allowed tools like Kubernetes to flourish.
[1531.48 --> 1532.50]  So absolutely not.
[1532.66 --> 1537.42]  I don't think Cates would have been a thing without Docker at all.
[1537.88 --> 1543.24]  Which, I mean, I understand that Kubernetes inside Google was Borg and Omega, right?
[1543.40 --> 1548.88]  So obviously, it existed before Docker existed inside Google.
[1548.88 --> 1550.14]  But that's a completely different thing.
[1550.14 --> 1555.30]  In order to get community adoption, in order for this open source thing to flourish, if
[1555.30 --> 1559.84]  Kubernetes had been built as an open source product and had its own idea of what a container
[1559.84 --> 1563.94]  is and had this thing of you have to run these commands to generate an image and then we run
[1563.94 --> 1566.20]  it, I just don't think it would have gotten adoption at all.
[1566.76 --> 1569.08]  It wasn't just the standardization of Docker, too.
[1569.18 --> 1573.74]  It was also, frankly, I don't want to use the term hype because Docker is a very powerful
[1573.74 --> 1575.14]  and important technology.
[1575.36 --> 1576.76]  But there was a wave, right?
[1576.92 --> 1581.28]  Where people were just really excited about Docker and anything that embraced Docker got
[1581.28 --> 1583.18]  an immediate uplift because of that.
[1583.26 --> 1585.58]  And I think Kubernetes, you know, benefited from that.
[1586.06 --> 1586.14]  Yeah.
[1586.48 --> 1591.80]  I remember that age and period really well when you had to, like, run containers.
[1591.98 --> 1593.24]  Didn't matter how, didn't matter where.
[1593.28 --> 1594.46]  You just had to run containers.
[1594.88 --> 1596.56]  And Kubernetes wasn't a thing back then.
[1596.56 --> 1598.86]  So few people even knew what containers were, right?
[1599.02 --> 1599.28]  Exactly.
[1599.42 --> 1599.84]  They're like, what?
[1599.96 --> 1600.46]  Containers what?
[1600.56 --> 1601.70]  Like, why would you want containers?
[1601.70 --> 1601.86]  containers.
[1602.40 --> 1605.10]  And I remember FreeBSDJLs as well.
[1605.22 --> 1608.18]  I'm yet to start a FreeBSDJL successfully.
[1608.54 --> 1613.46]  I've started that project when, like, 10 years ago when I got, like, my first FreeBSD
[1613.46 --> 1613.80]  server.
[1614.24 --> 1618.62]  And I never got to this day to get the jail up and running because how complicated it
[1618.62 --> 1618.88]  was.
[1618.98 --> 1619.24]  Yes.
[1619.34 --> 1621.68]  And I started, like, ah, there's, like, so many configuration options.
[1621.68 --> 1624.50]  And Docker made it run a command and you have it.
[1624.80 --> 1625.52]  That was brilliant.
[1626.16 --> 1628.68]  So as an idea, as a concept was really, really good.
[1628.68 --> 1633.02]  And things then, they got complicated and, you know, it happened what happened.
[1633.20 --> 1634.20]  But you're right.
[1634.26 --> 1637.96]  We are here today where Docker is no longer part of Kubernetes.
[1638.34 --> 1638.90]  It used to be.
[1639.00 --> 1640.94]  And that created quite the confusion.
[1641.44 --> 1644.78]  People say that, that, like, oh, Kubernetes dropped Docker and it's no longer.
[1644.92 --> 1648.16]  But that's my point, is that we shouldn't be thinking about the word Docker.
[1648.26 --> 1650.56]  We should be thinking about the standard that Docker created.
[1650.56 --> 1656.16]  So Kubernetes is still using Docker as a standard just as much as it did before, right?
[1656.42 --> 1656.64]  Yeah.
[1656.68 --> 1658.98]  It's still an integral part of what it means to be Kubernetes.
[1659.26 --> 1660.62]  I think it's the container runtime.
[1661.10 --> 1663.38]  That's, you know, that clarification came afterwards.
[1663.38 --> 1667.00]  Like, no, we're not dropping Docker support because Docker means so many things.
[1667.04 --> 1667.94]  It became an ecosystem.
[1668.28 --> 1672.80]  And even now, the default container registry is the Docker hub, right?
[1672.80 --> 1674.94]  So if you don't specify, and that's also Docker.
[1674.94 --> 1680.74]  It's part of Docker, but also the container runtime, the container D, run C, and a couple
[1680.74 --> 1681.18]  of others.
[1681.36 --> 1682.74]  But I think these are the two popular ones.
[1683.18 --> 1687.32]  So that's what they meant by removing Docker as a dependency of Kubernetes.
[1687.90 --> 1691.62]  And I'm wondering if you have to be good at Docker to do Kubernetes.
[1691.86 --> 1693.96]  Like, do you need any experience with Docker?
[1694.16 --> 1696.40]  Do you need to run Docker locally to get Kubernetes?
[1696.92 --> 1700.70]  I know that you can get Kubernetes in Docker, which confuses a lot of people.
[1700.70 --> 1704.96]  But I'd never recommend it, but, you know.
[1705.22 --> 1707.52]  Turtles all the way down and turtles in a circle even.
[1707.68 --> 1707.78]  Yeah.
[1707.98 --> 1712.14]  We actually get that question a lot, especially when we're talking to people about our workshops,
[1712.34 --> 1714.32]  because I guess the answer is sort of.
[1714.44 --> 1718.82]  You sort of need to be good with Docker in order to be good with Kubernetes.
[1719.10 --> 1724.40]  And what I mean by that is our core Kubernetes workshop actually doesn't use Docker at all.
[1724.50 --> 1727.08]  You never run a Docker command throughout that entire workshop.
[1727.08 --> 1731.66]  And even when we go under the hood, as you said, nowadays, you don't even see Docker on
[1731.66 --> 1733.92]  the nodes because it's all container-ty, right?
[1734.16 --> 1734.28]  Yep.
[1734.44 --> 1741.26]  You need to understand the concept of what containers are, as in sort of tiny VMs that
[1741.26 --> 1742.36]  can share some stuff.
[1742.48 --> 1746.90]  Like, we talk about the Linux namespaces that are being used in Kubernetes, right?
[1746.92 --> 1749.28]  When we talk about the different things you can share amongst containers.
[1749.58 --> 1753.16]  But you don't have to be great at crafting a Dockerfile, for example.
[1753.22 --> 1754.92]  And crafting a Dockerfile is an art.
[1754.92 --> 1760.20]  It is hard to create an efficient, really good Dockerfile and to understand all the security
[1760.20 --> 1761.16]  implications and everything.
[1761.76 --> 1766.66]  And to some degree, I think that shows how Docker did the tech community a service by
[1766.66 --> 1770.90]  giving us the standard, but did us a disservice by making that standard so low level.
[1771.04 --> 1775.72]  I mean, as an application developer, you need to understand not only apt-get install, but
[1775.72 --> 1779.78]  also the apt-cache and the difference between Alpine Linux and Ubuntu.
[1780.24 --> 1781.42]  All this stuff is kind of crazy.
[1781.42 --> 1788.84]  So most successful teams that I've seen instead centralize at least the skill of crafting Dockerfiles,
[1788.94 --> 1794.38]  if not just using a single centralized Dockerfile across all of your applications.
[1794.38 --> 1796.24]  That's like a thing you can do, right?
[1796.46 --> 1803.44]  So most teams I've seen have centralized that knowledge of how you create efficient Dockerfiles
[1803.44 --> 1803.94]  and all that.
[1803.94 --> 1808.52]  And then application developers just need to understand, maybe locally, they need to understand,
[1808.62 --> 1813.84]  you know, Docker Compose up and maybe a few Docker command line things.
[1813.88 --> 1817.14]  And they need to understand maybe how to push Docker images.
[1817.14 --> 1820.34]  But frankly, often that's just taken care of by the CICD system too.
[1820.76 --> 1826.06]  So no, I think you can make a lot of use of Kubernetes without having a deep understanding
[1826.06 --> 1826.42]  of Docker.
[1826.42 --> 1831.56]  For me, Kubernetes makes a lot more sense having started with Docker and having spent a couple
[1831.56 --> 1834.46]  of years in that ecosystem before Kubernetes was a thing.
[1835.14 --> 1839.66]  So, and that's very easy to ignore and forget because my beginning was not Kubernetes.
[1840.08 --> 1843.36]  But many people, this is where they start and they missed the whole Docker thing.
[1843.44 --> 1847.10]  I mean, they may have been running it locally, but not to the point that they understand it,
[1847.18 --> 1850.52]  not to the point that they've been using it for a couple of years and really understand
[1850.52 --> 1851.56]  what's happening under the hood.
[1851.56 --> 1856.62]  So I think some Docker concepts, and as I mentioned, and as you've mentioned, it's not
[1856.62 --> 1857.18]  just the runtime.
[1857.48 --> 1861.70]  There's so many other aspects of Docker are really helpful to get started with Kubernetes.
[1862.34 --> 1866.02]  What other things do you think are helpful when you get started with Kubernetes?
[1866.62 --> 1872.04]  In terms of knowledge, I think it's almost more important to have a deeper understanding
[1872.04 --> 1875.24]  of Linux networking and just networking in general.
[1875.40 --> 1881.12]  From our experience, understanding how a cluster IP service works, for example, and all the IP
[1881.12 --> 1886.04]  tables stuff that happens there, understanding how load balancers work, understanding why
[1886.04 --> 1890.76]  node ports are a terrible idea, or understanding how ingresses work at layer seven, right?
[1891.32 --> 1897.50]  All of that is conceptually harder for our students from what we've seen and conceptually harder
[1897.50 --> 1902.32]  for people who are new to Kubernetes because they just never had to deal with that kind
[1902.32 --> 1903.44]  of networking knowledge.
[1903.76 --> 1908.58]  I think another thing that's important for a team who's getting started with, well, first
[1908.58 --> 1910.26]  of all, let's talk about how you should adopt Kubernetes.
[1910.26 --> 1915.92]  First of all, even though I kind of pooh-poohed the value of the Kubernetes managed services
[1915.92 --> 1920.56]  like EKS, AKS, and GKE, you absolutely should use them.
[1920.68 --> 1923.20]  I mean, yes, you can deploy your own cluster, but why?
[1923.56 --> 1925.88]  Like, just go with one of the managed solutions.
[1926.10 --> 1928.44]  Frankly, they're cheaper, especially GKE, right?
[1928.54 --> 1933.50]  And if you have a choice just to, you know, if you have your druthers about which cloud to
[1933.50 --> 1940.64]  be on, GKE is by far the best experience, and Azure is by far the worst experience, not
[1940.64 --> 1943.40]  just in terms of Kubernetes, but just across the board, right?
[1943.86 --> 1945.10]  And AWS is what it is.
[1945.18 --> 1948.00]  So if you're on AWS, you're probably forced to be on AWS and whatever.
[1948.20 --> 1948.94]  You're on EKS.
[1949.16 --> 1952.76]  And then once you've got that, as I mentioned before, there's so much other stuff that has
[1952.76 --> 1955.10]  to be configured and deployed on top of that.
[1955.28 --> 1957.72]  And our best advice is just to keep it as simple as you can.
[1957.72 --> 1963.54]  Most of our customers have already spent so many innovation points when they are adopting
[1963.54 --> 1964.00]  Kubernetes.
[1964.40 --> 1970.18]  We kind of feel it's our mission, our job to help guide them towards more conservative
[1970.18 --> 1976.30]  solutions and fewer moving parts, because it's so tempting once you've got Kubernetes,
[1976.42 --> 1979.30]  like, oh, I guess I need Istio because Istio does all these cool things.
[1979.38 --> 1979.82]  It does.
[1980.08 --> 1982.16]  And if you need those things, that's great.
[1982.46 --> 1983.38]  Jump on board.
[1983.56 --> 1985.96]  But holy crap, is Istio complicated?
[1985.96 --> 1987.50]  And it's dangerous.
[1987.72 --> 1991.08]  I mean, like, if you misconfigure Istio, like, you can really do damage to your production
[1991.08 --> 1991.44]  traffic.
[1991.94 --> 1996.86]  And, you know, avoid any tooling that you don't have an immediate pain point for.
[1997.14 --> 2001.88]  When you look at the CNCF landscape, it can often look like you're in a toy store, you
[2001.88 --> 2002.02]  know?
[2002.12 --> 2005.42]  You see all these wonderful, cool gadgets, and you just want to grab them all up into
[2005.42 --> 2005.86]  your basket.
[2006.04 --> 2010.78]  But you need to show a lot of restraint, because every one of those that you add is something
[2010.78 --> 2012.40]  else you have to manage and understand.
[2012.90 --> 2013.26]  Oh, yes.
[2013.60 --> 2013.88]  Yes.
[2014.08 --> 2016.80]  Most people forget about that, like, install it, and that's it.
[2016.80 --> 2018.20]  Well, how are you going to upgrade it?
[2018.20 --> 2018.32]  Right.
[2018.52 --> 2021.26]  And some components don't upgrade as well as others.
[2021.64 --> 2021.80]  Yep.
[2021.98 --> 2026.02]  And then that just opens, like, a whole new world of problems, like, a whole new set of
[2026.02 --> 2026.36]  problems.
[2026.88 --> 2031.00]  Like, do you upgrade in place, or do you stand up another Kubernetes cluster?
[2031.34 --> 2034.74]  And if a cluster gets too big, well, should you split in multiple clusters?
[2034.82 --> 2038.36]  And before you know it, you're, like, you're solving problems that you didn't even know
[2038.36 --> 2040.00]  existed before you chose Istio.
[2040.00 --> 2041.02]  So maybe don't.
[2041.36 --> 2041.38]  Right.
[2041.56 --> 2042.00]  Exactly.
[2042.40 --> 2042.84]  Exactly.
[2043.28 --> 2044.44]  You're, like, where am I?
[2045.40 --> 2045.84]  Exactly.
[2046.60 --> 2048.02]  I thought I understood networking.
[2048.26 --> 2048.80]  No, you don't.
[2049.52 --> 2049.68]  Right.
[2049.80 --> 2050.00]  Yeah.
[2050.08 --> 2052.98]  When you understand networking, then you see how Istio actually works.
[2053.08 --> 2054.20]  You're, like, oh, my gosh.
[2054.74 --> 2058.12]  And there are some components that are kind of table stakes for a new cluster.
[2058.34 --> 2062.32]  Like, cert manager is a great example of just, okay, everybody should have cert manager
[2062.32 --> 2063.12]  running in their cluster.
[2063.12 --> 2068.70]  But there's so many other things that are cool and interesting, but probably not something
[2068.70 --> 2068.96]  you need.
[2069.20 --> 2070.48]  Another example is Helm.
[2070.76 --> 2077.36]  Helm, as a tool, is amazing for installing third-party packages, something that somebody
[2077.36 --> 2078.74]  else has to maintain, right?
[2078.76 --> 2079.70]  You need Postgres?
[2079.88 --> 2082.36]  Then, sure, use the official Postgres Helm chart.
[2082.42 --> 2084.56]  That's the best way to do it, by far.
[2085.06 --> 2088.42]  Well, Postgres may be a bad example, because there's also operators that do an even better
[2088.42 --> 2089.00]  job, right?
[2089.00 --> 2095.72]  But what I see teams immediately doing, because they just didn't know any better, they just
[2095.72 --> 2099.70]  assume that this is how you use Kubernetes, is they start building Helm charts for their
[2099.70 --> 2100.68]  internal applications.
[2100.94 --> 2102.66]  Small teams doing this.
[2103.08 --> 2110.80]  And Helm, although it's great for package distribution and consuming third-party software, in order
[2110.80 --> 2118.24]  to author a Helm chart, you are using a Turing-complete templating language in order to generate
[2118.24 --> 2120.98]  white space-sensitive data structures.
[2121.38 --> 2122.38]  How crazy is that?
[2122.74 --> 2123.08]  Oh, my goodness.
[2123.08 --> 2123.68]  It's just crazy.
[2123.78 --> 2124.54]  It's crazy, right?
[2124.84 --> 2126.00]  I'm glad it's not just me.
[2126.10 --> 2127.46]  That thing's exactly the same way.
[2127.58 --> 2128.68]  I'm glad it's not just me.
[2128.74 --> 2129.58]  So I'm not the crazy one.
[2129.64 --> 2130.06]  Okay, good.
[2130.86 --> 2133.44]  Okay, so I have confirmation that I'm not crazy.
[2134.90 --> 2135.26]  Okay.
[2135.50 --> 2138.68]  I don't know about that, but just one aspect, you're not crazy.
[2139.08 --> 2139.52]  Damn it.
[2139.68 --> 2140.00]  Almost.
[2140.64 --> 2141.00]  Almost.
[2143.00 --> 2143.36]  Almost.
[2143.74 --> 2145.96]  And the sad thing about it is they just don't know any better.
[2145.96 --> 2147.14]  They've got very simple applications.
[2147.14 --> 2151.84]  They're a small team, and they end up spending a lot of time building these Helm charts to
[2151.84 --> 2154.10]  make them, you know, to distribute them and stuff.
[2154.16 --> 2154.84]  You don't need that.
[2155.06 --> 2162.98]  Like, Customize, for example, is a great tool for managing your YAML when it's being deployed
[2162.98 --> 2163.90]  to multiple environments.
[2163.96 --> 2165.76]  Because you can make very small changes.
[2165.98 --> 2168.94]  Customize is much easier to understand, much easier to maintain.
[2169.36 --> 2171.64]  If you're really small, you don't even need a tool like that.
[2171.68 --> 2174.62]  You could just apply the YAML and just call it a day, you know?
[2174.62 --> 2181.22]  I think when a team chooses Kubernetes, where it should focus on is automation.
[2181.58 --> 2188.08]  Building out their own internal automation system, not just for managing the cluster using
[2188.08 --> 2193.60]  like Terraform, which is by far the best tool for that kind of stuff, but also for managing
[2193.60 --> 2195.46]  the resources inside the cluster.
[2195.46 --> 2200.34]  You know, a CI, CD pipeline, maybe using like GitOps at the end or whatever.
[2200.62 --> 2203.34]  That's the fundamentals that your team should focus on.
[2203.38 --> 2206.56]  Because once you have that, all the other changes become simpler.
[2206.68 --> 2212.66]  And frankly, that automation is the half of the value prop of Kubernetes because the Kubernetes
[2212.66 --> 2214.20]  API is so good.
[2214.68 --> 2217.16]  It's so easy to automate stuff through Kubernetes.
[2217.16 --> 2222.44]  And if you're not investing in that automation, you're wasting that value.
[2222.88 --> 2227.12]  And then obviously, I mean, I run a company, so I should say that like, if you're just choosing
[2227.12 --> 2230.20]  Kubernetes, you should be looking for training.
[2230.46 --> 2233.88]  And I love our workshops, obviously, but there's others, right?
[2233.94 --> 2239.12]  But you do need to invest in your engineer's knowledge because they are going to have to
[2239.12 --> 2240.40]  debug it when it goes sideways.
[2240.76 --> 2245.24]  And you don't want them floundering and using Stack Overflow in the middle of an outage.
[2245.24 --> 2250.64]  If you can find, we offer engineering services, usually not for people who are just now adopting
[2250.64 --> 2254.42]  Kubernetes, unless you've got a very interesting application you're moving over.
[2254.70 --> 2261.02]  But you should be finding experts, either hiring Kubernetes experts or finding a partner that
[2261.02 --> 2265.74]  you can integrate with your team that will give you those subject matter experts for Kubernetes,
[2265.92 --> 2271.60]  because you're going to save a lot more time and money in the long run if you do that early on.
[2275.24 --> 2287.82]  What's up, shippers?
[2287.94 --> 2290.48]  This episode is brought to you by Sentry.
[2290.72 --> 2294.70]  You already know working code means happy customers, and that's exactly why teams choose
[2294.70 --> 2295.08]  Sentry.
[2295.30 --> 2299.42]  From error tracking to performance monitoring, Sentry helps teams see what actually matters,
[2299.74 --> 2303.88]  resolve problems quicker, and learn continuously about their applications from the front end to
[2303.88 --> 2304.56]  the back end.
[2304.56 --> 2310.44]  Over a million developers and 70,000 organizations already ship better software faster with Sentry.
[2310.78 --> 2311.42]  And guess what?
[2311.58 --> 2312.30]  You can too.
[2312.70 --> 2315.50]  Ship it listeners new to Sentry get the team plan for free for three months.
[2315.86 --> 2317.96]  Use the code SHIPIT when you sign up.
[2318.20 --> 2320.78]  Head to sentry.io and use the code SHIPIT.
[2321.18 --> 2323.10]  And by our friends at Equinix Metal.
[2323.48 --> 2327.82]  If you want the choice and control of hardware with low overhead and the developer experience of
[2327.82 --> 2329.88]  the cloud, check out Equinix Metal.
[2330.24 --> 2334.36]  Deploying minutes across 18 global locations from Silicon Valley to Sydney,
[2334.78 --> 2339.74]  visit metal.equinix.com slash just add metal and receive $100 in credit to play with.
[2340.06 --> 2343.66]  Again, metal.equinix.com slash just add metal.
[2343.66 --> 2366.26]  You've touched on a really important point, namely the investment in automation.
[2366.90 --> 2371.14]  So if you use Kubernetes, that's great, especially if you need it.
[2371.14 --> 2373.48]  But you will have to invest in automation.
[2374.02 --> 2378.94]  And I think there's a set of principles which are really important that you have once you
[2378.94 --> 2385.22]  enter this world of cloud native, Kubernetes, because otherwise making choices will be really
[2385.22 --> 2385.66]  difficult.
[2386.22 --> 2391.44]  Automation is really important once you are in the world of Kubernetes, in the world of cloud
[2391.44 --> 2391.84]  native.
[2392.00 --> 2392.30]  Absolutely.
[2392.30 --> 2394.10]  What other things are important?
[2394.76 --> 2399.08]  Well, I mean, if you're going to move into that world, again, as we said before, the complication
[2399.08 --> 2400.12]  is just massive.
[2400.12 --> 2403.98]  I mean, there's so much that you're pinning together, that you're tying together.
[2404.28 --> 2410.16]  I think that it's important if you're going to do that, that you invest in education in
[2410.16 --> 2413.90]  your engineers so that they can understand this complexity.
[2414.88 --> 2420.04]  And depending on the size of the company that you are, depending on the size of your engineering
[2420.04 --> 2426.42]  team, many companies invest in what we're calling internal platforms.
[2426.42 --> 2430.38]  And you can just view that as an extension of the automation.
[2430.38 --> 2436.32]  It's almost a spectrum of how sophisticated these internal platforms get and kind of what
[2436.32 --> 2437.88]  model they use.
[2438.04 --> 2446.42]  All the way from on the lowest level side is just the platform team providing maybe centralized
[2446.42 --> 2449.46]  Docker file, maybe a centralized Helm chart.
[2449.64 --> 2452.64]  That's one of the few times we've seen Helm used internally in a good way.
[2452.64 --> 2458.68]  And a centralized CI CD system so that the application developers can plug their app into the Helm chart
[2458.68 --> 2460.20]  using that Docker file.
[2460.84 --> 2466.04]  And it gets automatically deployed to all the various environments and such.
[2466.58 --> 2470.52]  Then on the other side of the spectrum is implementing a full Heroku, right?
[2470.52 --> 2477.50]  Where the developers are insulated 100% from the details of Kubernetes and they're given a really
[2477.50 --> 2478.34]  nice interface.
[2478.68 --> 2481.30]  We have never seen that done successfully, just to be clear.
[2481.48 --> 2488.48]  Like I've never seen that work where the developers did not still have to understand the intricacies
[2488.48 --> 2492.24]  of Kubernetes because at some point they got to break glass in case of emergency.
[2492.78 --> 2492.88]  Yeah.
[2493.14 --> 2494.24]  Because you have to run it, right?
[2494.38 --> 2496.06]  You've built it, but you have to run it.
[2496.22 --> 2496.80]  And guess what?
[2496.82 --> 2497.66]  It's running on Kubernetes.
[2497.66 --> 2502.84]  So if you don't know how to debug it or even understand what is happening, good luck to you.
[2503.06 --> 2508.46]  And if your platform team is so good that they have actually built a full interface on top of
[2508.46 --> 2513.20]  Kubernetes that takes care of all the details and the application developer only needs to interact
[2513.20 --> 2515.30]  with that interface, that platform they built.
[2515.68 --> 2516.44]  I've got news for you.
[2516.46 --> 2517.68]  You're probably in the wrong industry.
[2517.88 --> 2521.30]  Like you should spin that off and clear house, right?
[2521.58 --> 2526.20]  Oh, you gave me an idea because even though we use Kubernetes to run all of changelog,
[2526.20 --> 2528.00]  the developers, they don't know that.
[2528.20 --> 2531.98]  They still just get push and all the automation takes care of the rest.
[2532.30 --> 2536.54]  So we were using Docker Swarm before and we were using Docker before.
[2536.70 --> 2540.20]  The experience, as far as developers are concerned, it has never changed.
[2540.42 --> 2542.22]  It has always been get push.
[2542.54 --> 2544.22]  Like, isn't that the heroic experience?
[2544.34 --> 2545.18]  Get push and it runs.
[2546.18 --> 2546.50]  That is.
[2546.60 --> 2546.88]  That is.
[2547.26 --> 2548.58]  But what happens when there's a fire?
[2548.76 --> 2550.20]  How do the developers debug when...
[2550.72 --> 2551.34]  They don't.
[2551.38 --> 2551.64]  Okay.
[2551.64 --> 2552.78]  They don't.
[2553.72 --> 2556.48]  So around that, we have a set of services.
[2556.70 --> 2561.66]  Like, for example, Grafana Cloud, where we send all the logs, all the metrics.
[2562.14 --> 2565.54]  So if there is a problem, that's one of the first places where you would look.
[2565.72 --> 2567.92]  The new addition was integrating with Honeycomb.
[2568.08 --> 2568.30]  Nice.
[2568.40 --> 2572.86]  And Honeycomb gets the Fastly logs as well, which is the CDN.
[2572.90 --> 2575.54]  Because it's not just Kubernetes, it's also what's in front of it.
[2575.68 --> 2577.02]  And then what's behind it as well.
[2577.14 --> 2578.24]  There's like all these components.
[2578.24 --> 2585.08]  So having these different ways of understanding what is happening in your runtime, whether
[2585.08 --> 2588.76]  it's Kubernetes or something else, is important regardless what the runtime is.
[2589.04 --> 2590.46]  For example, getting exceptions.
[2590.82 --> 2596.96]  That's like a really old thing, which we used to do when we used to SCP a Ruby code onto
[2596.96 --> 2598.22]  or FTP it, right?
[2598.48 --> 2600.36]  We still used to get like exceptions.
[2600.64 --> 2603.04]  I forget like what the name of that tool was.
[2603.14 --> 2605.38]  Do you remember what we used back in the day?
[2605.48 --> 2606.36]  There was a number of them.
[2606.36 --> 2607.94]  In fact, I actually wrote one of them.
[2608.24 --> 2608.64]  Exactly.
[2608.88 --> 2609.84]  That's why I'm asking you.
[2610.24 --> 2616.26]  I wrote Hop Toad, which later became Airbrake and competed against Get Exceptional.
[2616.44 --> 2621.80]  And hilariously, both Airbrake and Get Exceptional were purchased by the same person.
[2621.92 --> 2624.44]  And now they're actually running under the same umbrella, which is kind of funny.
[2625.06 --> 2625.34]  Right.
[2626.08 --> 2627.46]  Yeah, you need all these things.
[2627.56 --> 2630.86]  You need all these interfaces into understanding what your application is doing.
[2631.12 --> 2632.50]  I'm really excited, by the way.
[2632.58 --> 2635.74]  This is a bit of a tangent, but I'm really excited by all the stuff that's going on with
[2635.74 --> 2640.54]  EBPF, especially with things like, I think it's New Relics Pixie.
[2640.94 --> 2648.78]  So yeah, New Relics Pixie is really exciting because of the deep insight it can give in a
[2648.78 --> 2650.08]  language agnostic way.
[2650.30 --> 2654.90]  It's one of those things that you could see as a building block so that the developer does
[2654.90 --> 2658.34]  not need access to kubectl exec, for example.
[2658.34 --> 2658.78]  Exactly.
[2659.98 --> 2660.50]  That's it.
[2660.60 --> 2665.68]  That's, I think, what a successful ops side of running Kubernetes looks like, where you
[2665.68 --> 2666.80]  don't have to get there.
[2667.06 --> 2671.66]  As a developer, for example, Blue Green, if you do that properly, and if you have all
[2671.66 --> 2676.02]  the redundancies in place, even when something goes down, the end user doesn't see that.
[2676.32 --> 2677.86]  And it doesn't matter that it runs Kubernetes.
[2678.32 --> 2683.02]  And when it comes to debugging it, well, if you're a small team, and let's say the problem
[2683.02 --> 2684.32]  is in Heroku, what happens?
[2684.56 --> 2685.46]  Do you debug Heroku?
[2685.72 --> 2685.98]  No.
[2685.98 --> 2687.06]  No way.
[2687.48 --> 2690.70]  You don't get the keys to Heroku to debug the stack, right?
[2691.26 --> 2692.82]  It just gets scheduled somewhere else.
[2693.02 --> 2694.06]  And that's how that gets solved.
[2694.70 --> 2699.34]  So what I'm saying is having that visibility into how things run is really important.
[2699.92 --> 2703.96]  And if that's your experience and your interface, that's great.
[2704.06 --> 2708.32]  I think that's one of the principles that are really important, regardless what the runtime
[2708.32 --> 2708.74]  is.
[2708.92 --> 2710.54]  And if it's Kubernetes, so be it.
[2710.74 --> 2714.94]  If you're going to be using something like Kubernetes, you need to invest doubly strongly
[2714.94 --> 2718.46]  in observability and in all of that metrics.
[2718.46 --> 2725.44]  But I'd argue that you need that just as much, if not more, if you're not using Kubernetes.
[2725.44 --> 2732.30]  If you're trying to do raw AWS, for example, it's even harder to build all that observability
[2732.30 --> 2733.48]  infrastructure in place.
[2733.48 --> 2738.74]  But it's absolutely, if you're just moving into the cloud world and moving into this whole
[2738.74 --> 2745.50]  type of world where automation and where it's a cloudy world that's focused on automation,
[2745.50 --> 2751.06]  you need that observability, not only for your own ability to debug, but eventually you're
[2751.06 --> 2754.00]  going to feed that observability back into your automation, right?
[2754.06 --> 2759.48]  You're going to do automated blue-green rollouts where you want the automation to, over the course
[2759.48 --> 2763.88]  of maybe a day, to look for errors, look for reduced metrics, and to roll it back.
[2764.24 --> 2764.80]  Yeah, that's right.
[2765.04 --> 2771.14]  And I know that I read ops and infrastructure and that side of things, but our Kubernetes
[2771.14 --> 2773.70]  setup, it's simple on purpose.
[2774.06 --> 2775.50]  And some things could be better.
[2775.60 --> 2776.80]  It can always be improved.
[2776.92 --> 2777.48]  We have it public.
[2777.76 --> 2781.94]  Anyone can check it out to see how we run and how we set up and which components we pick.
[2782.48 --> 2783.66]  CertManager is part of it.
[2783.76 --> 2785.42]  External DNS, if you ingress Nginx.
[2785.48 --> 2785.66]  Yes.
[2785.78 --> 2786.28]  All the stock stuff.
[2786.28 --> 2788.18]  External DNS, also absolutely necessary.
[2788.18 --> 2788.88]  It's part of it.
[2789.02 --> 2792.92]  And the Kubernetes is managed, so we don't deploy on bare metal servers, even though
[2792.92 --> 2796.98]  that's become simpler over the years since we embarked on this journey.
[2797.56 --> 2800.62]  And there's other options which we will also be exploring.
[2801.28 --> 2806.96]  So whether you do Kubernetes or something else, there will be certain operational concerns which
[2806.96 --> 2807.68]  will be difficult.
[2808.06 --> 2812.84]  And there's a level of maturity that you need to have on the team to navigate them.
[2812.84 --> 2815.68]  And I think that's what is important to almost like reiterate.
[2815.68 --> 2815.82]  Great.
[2816.34 --> 2820.58]  And in certain cases, like Istio, I'm sure some things it makes better.
[2820.68 --> 2822.10]  But networking, I don't know.
[2822.16 --> 2824.22]  I think networking gets more complicated with Istio.
[2824.52 --> 2827.64]  And if you're okay with a trade-off, maybe it's a good one to make.
[2827.88 --> 2829.10]  But I wouldn't.
[2829.24 --> 2830.24]  We haven't chosen Istio.
[2830.40 --> 2831.10]  So there you go.
[2831.24 --> 2831.74]  I agree with you.
[2831.80 --> 2832.24]  100%.
[2832.24 --> 2838.42]  Talking about Kubernetes and how we run it, do you recommend a big cluster or do you recommend
[2838.42 --> 2839.48]  smaller clusters?
[2840.06 --> 2840.40]  Oh, yeah.
[2840.82 --> 2846.52]  So when Kubernetes first came out, I mean, first of all, short answer is many small clusters.
[2846.76 --> 2852.70]  The long answer is when Kubernetes first came out, CIOs looked at it and said, oh, this
[2852.70 --> 2853.14]  is great.
[2853.14 --> 2858.50]  We can, you know, we're probably using 20% of our CPU and memory across all of our VMs
[2858.50 --> 2863.00]  across our entire fleet, just because of natural inefficiencies between teams, right?
[2863.18 --> 2866.82]  You need a new app out, you throw a couple of VMs out there, you call it a day.
[2867.26 --> 2871.88]  And the CIOs job, part of it, is to reduce infrastructure costs, right?
[2872.18 --> 2874.72]  And so the CIOs looked around, they said, oh, this is great.
[2874.78 --> 2876.58]  We can bim pack the f*** out of this, right?
[2876.60 --> 2881.24]  We can take all that stuff and just shove it into one massive cluster, save so much money.
[2881.24 --> 2884.08]  And I think that drove a lot of initial Kubernetes adoption.
[2884.22 --> 2887.48]  I mean, obviously, there was a lot of grassroots adoption of Kubernetes, but there was also
[2887.48 --> 2891.78]  a lot of, there was a lot of adoption coming out of the IT organizations in larger companies
[2891.78 --> 2894.20]  because of that driving factor.
[2894.60 --> 2900.70]  Now, when the operators started using Kubernetes, they saw what I think of as the real benefits.
[2900.82 --> 2904.20]  I don't think the benefit of Kubernetes is about orchestrating containers.
[2904.42 --> 2909.36]  I think it's about that beautiful, idempotent, declarative, and ubiquitous API.
[2909.36 --> 2915.54]  And especially when you start extending that into external services, external resources
[2915.54 --> 2922.62]  that you're managing, like using, for example, Crossplane to provision AWS resources through
[2922.62 --> 2923.18]  KubeCuttle.
[2923.30 --> 2924.74]  It's a fantastic experience, right?
[2924.92 --> 2925.54]  Yes.
[2925.66 --> 2929.24]  And the operators looked at it and said, this whole Kubernetes thing is pretty cool.
[2929.50 --> 2932.42]  However, Blast Radius is a thing, right?
[2932.42 --> 2937.14]  And so if you've got everything in one big cluster, and especially those poor operators
[2937.14 --> 2946.90]  who went through the 1.8 through 111 upgrade path got burned so many times on trying to upgrade
[2946.90 --> 2947.90]  these clusters in place.
[2947.90 --> 2951.54]  And they started developing these complicated blue-green cluster upgrade strategies where
[2951.54 --> 2953.22]  they deploy an entirely new cluster.
[2953.42 --> 2955.50]  And that's necessary and great.
[2955.76 --> 2960.52]  But now we've figured out that, well, you should just be running many small clusters.
[2960.52 --> 2961.70]  And there's two different ways you could do it.
[2961.70 --> 2966.06]  You run a cluster per kind of bounded context for your microservices.
[2966.22 --> 2970.66]  In other words, you could have a cluster just for your shopping cart stuff and a cluster
[2970.66 --> 2975.56]  just for your front-end stuff and a cluster for your back-end and all that.
[2975.90 --> 2980.92]  But a better way of doing it is to run all these clusters as homogenous workloads, where they
[2980.92 --> 2982.68]  are all running identical workloads.
[2983.24 --> 2987.44]  In fact, one of our clients is doing that, and they're referring to it as fleets internally.
[2987.44 --> 2990.36]  So what they do is actually really smart.
[2990.62 --> 2995.06]  They run a cluster in AWS per availability zone.
[2995.36 --> 2996.46]  And that does a couple of things.
[2996.74 --> 2999.26]  It's a natural dividing point for the different clusters.
[2999.78 --> 3004.88]  And it means that they also keep all of their traffic inside each AD because all the services
[3004.88 --> 3007.86]  in cluster A are always talking to other services in cluster A.
[3007.92 --> 3009.72]  They don't try and do cross-cluster traffic.
[3010.18 --> 3013.58]  And that saves them a good amount of money because they have a lot of networking that's happening
[3013.58 --> 3014.10]  in AWS.
[3014.60 --> 3019.60]  But also, it means that when they're upgrading these clusters, they can just upgrade one.
[3019.86 --> 3021.20]  And if it goes sideways, who cares?
[3021.40 --> 3023.68]  Burn it down, rebuild it, and you're fine.
[3023.94 --> 3027.00]  You've only lost, what, 20%, 25% of your capacity?
[3027.18 --> 3028.46]  And you just keep moving.
[3028.98 --> 3031.72]  Now, of course, the big elephant here is state.
[3032.10 --> 3034.00]  You can't do that with databases.
[3034.38 --> 3039.00]  And so the best solution that we always propose to our customers is, look, if you're going to
[3039.00 --> 3043.06]  run stateful workloads in Kubernetes, which, by the way, that's a lot of innovation points.
[3043.48 --> 3046.14]  You really need a team to manage that if you're going to do that.
[3046.20 --> 3048.66]  That's a dangerous thing to do as a small company.
[3048.98 --> 3053.52]  But if you're going to run stateful workloads in Kubernetes, at least shove them into a smaller
[3053.52 --> 3055.48]  cluster that you know you have to treat as a pet.
[3055.94 --> 3058.90]  You've taken all of your other clusters, your stateless ones, and you've made them into
[3058.90 --> 3060.26]  cattle, which is beautiful.
[3060.80 --> 3062.86]  Then you constrain all your stateful workloads into one.
[3062.96 --> 3064.52]  Or just use RDS.
[3065.06 --> 3067.74]  Just externalize your databases entirely.
[3067.74 --> 3068.42]  Right?
[3068.66 --> 3069.46]  It's a tough problem.
[3069.64 --> 3073.46]  And yeah, unless you've been solving that problem for some years, it's really difficult
[3073.46 --> 3074.18]  to appreciate.
[3074.64 --> 3078.16]  And even the operators, I'm glad that you mentioned it earlier for PostgreSQL.
[3078.46 --> 3079.78]  Do you know how we run PostgreSQL?
[3079.96 --> 3080.32]  How do you?
[3080.80 --> 3082.78]  We run it as a stateful set.
[3083.04 --> 3085.34]  No help, no operator, nothing like that.
[3085.62 --> 3088.40]  And since we did that, it's been more stable.
[3088.58 --> 3092.12]  It has not failed since we went to a stateful set.
[3092.24 --> 3095.68]  Simple stateful set, PostgreSQL container, sorry, PostgreSQL image.
[3095.68 --> 3097.36]  And what were you doing before that?
[3097.36 --> 3099.36]  Were you doing RDS or were you doing?
[3099.66 --> 3106.96]  We tried running the Crunchy data, PostgreSQL operator, and it failed because of replication.
[3107.48 --> 3110.36]  Actually, we even covered this in like an episode at length.
[3110.46 --> 3114.74]  But the point was the primary stopped replicating to the replica.
[3114.96 --> 3115.10]  Yeah.
[3115.10 --> 3117.08]  So the write-ahead log filled up on the primary.
[3117.50 --> 3119.10]  The second it crashed.
[3119.24 --> 3121.54]  The secondary could not be promoted.
[3121.62 --> 3125.84]  The replica could not be promoted to primary because it was too far behind.
[3125.98 --> 3127.68]  And then we didn't have a database.
[3129.62 --> 3129.98]  Ouch.
[3129.98 --> 3133.46]  We couldn't reboot the main one because the PVC filled up.
[3133.72 --> 3135.18]  We couldn't resize the PVC either.
[3135.52 --> 3137.66]  And we thought, nah, let's just crunch data.
[3137.86 --> 3142.20]  We actually went to Zalanda one, the other PostgreSQL operator, and the same thing happened.
[3142.86 --> 3146.28]  So obviously the networking, there was an issue at that point with networking.
[3146.78 --> 3153.02]  And that broke replication, PostgreSQL replication, which resulted in a less stable database.
[3153.02 --> 3155.56]  Yeah, but I mean, come on, that's not because of those operators.
[3156.16 --> 3158.70]  You would have the same problem running a stateful set.
[3158.80 --> 3162.54]  I think you probably changed other things at the same time as moving to a stateful set,
[3162.58 --> 3164.72]  or maybe changed the way you use it or something like that.
[3164.74 --> 3165.56]  We don't replicate.
[3165.92 --> 3166.66]  Like it's single instance.
[3166.88 --> 3167.06]  Oh, okay.
[3167.16 --> 3167.62]  Well, there you go.
[3167.82 --> 3168.62]  We back everything up.
[3168.86 --> 3170.00]  We back every hour.
[3170.28 --> 3171.42]  We do like a full backup.
[3171.72 --> 3171.86]  Yeah.
[3171.88 --> 3175.38]  And we can restore from backup within two, three minutes.
[3175.84 --> 3182.58]  So a blank node can pull the backup down from S3 and boot up in three minutes.
[3182.58 --> 3183.90]  We'll have less downtime.
[3184.08 --> 3185.42]  And it's a very simple procedure.
[3185.80 --> 3187.24]  Now, would I choose a managed?
[3187.32 --> 3187.44]  Right.
[3187.48 --> 3191.46]  You've got a potential data loss issue of like up to an hour, right?
[3191.54 --> 3194.50]  Half an hour median data loss if you lose the PV, right?
[3194.72 --> 3195.06]  Exactly.
[3195.14 --> 3195.34]  Yes.
[3195.64 --> 3197.34]  But that's a trade-off that you're willing to make.
[3197.38 --> 3197.76]  That's fine.
[3197.84 --> 3198.46]  That works great.
[3198.62 --> 3198.90]  Exactly.
[3198.90 --> 3204.66]  And if I was to choose any PostgreSQL service, type of service, I would just go for a managed
[3204.66 --> 3207.10]  one, like CockroachDB, something like that.
[3207.22 --> 3211.06]  I mean, that's what I'm thinking because it's a really hard problem to solve.
[3211.54 --> 3214.30]  I've been trying to solve this for like a couple of years.
[3214.58 --> 3218.08]  I don't think I have in like a different context because it's really difficult.
[3218.34 --> 3224.52]  I got to tell you that I love the solution you just talked about because too many companies,
[3224.72 --> 3228.60]  and I've heard other people say this, not like this is some insight that I have, but
[3228.60 --> 3230.24]  I agree with it 100%.
[3230.24 --> 3234.50]  Too many companies look around and they see all this really interesting and production
[3234.50 --> 3238.18]  grade hardened technologies coming out of Google and Facebook and other companies
[3238.18 --> 3238.66]  like that.
[3238.66 --> 3241.84]  And they think, oh, okay, well, if we're going to play in the cloud, we got to have
[3241.84 --> 3242.62]  that, right?
[3242.86 --> 3243.66]  You don't.
[3243.96 --> 3250.36]  And if you try and build your system to be at that level, it's going to drag you down
[3250.36 --> 3251.56]  with the weight of it, right?
[3251.90 --> 3255.88]  And you looked at it and you said, yeah, we can, you know, worst case scenario, we lose
[3255.88 --> 3256.24]  a PV.
[3256.42 --> 3259.90]  We can handle half an hour's worth of data loss, right?
[3260.38 --> 3261.92]  It's not that big of a deal.
[3261.92 --> 3267.40]  Then you can go with a single instance of Postgres without replication and you are fine and your
[3267.40 --> 3269.06]  life is so much better, right?
[3269.20 --> 3274.42]  So I love that you had the self-awareness as a, you know, organization to make that choice.
[3274.74 --> 3274.84]  Yeah.
[3275.04 --> 3276.18]  We don't use PVs.
[3276.34 --> 3277.90]  But I don't have time for that story.
[3279.50 --> 3281.86]  Do you use the host disk for that or what do you do?
[3282.06 --> 3282.48]  Oh, yes.
[3282.70 --> 3284.24]  It's like 10 times faster.
[3284.96 --> 3285.18]  Yeah.
[3285.48 --> 3286.66]  Like we never lose that.
[3286.92 --> 3287.32]  You don't care.
[3287.32 --> 3290.82]  So it doesn't mean that like when you're rolling hosts under your cluster, you need
[3290.82 --> 3292.16]  to probably call downtime, right?
[3292.18 --> 3292.84]  You need to stop traffic.
[3292.84 --> 3293.58]  We have a single host.
[3297.26 --> 3298.40]  It's so good.
[3298.62 --> 3299.46]  It never went down.
[3302.96 --> 3304.92]  We have a much better integration with the CDN.
[3305.02 --> 3309.42]  And what that means is that even when the origin is down, we serve stale content.
[3309.82 --> 3315.58]  And unless you do posts or patches or anything like that, gets, it works.
[3315.58 --> 3320.58]  And parts of the website may be down for most users, but you get your MP3s.
[3320.88 --> 3321.98]  We'll serve that content.
[3322.24 --> 3322.94]  We'll get the pages.
[3323.84 --> 3328.60]  And basically what you're telling me is, boy, life is easy when you're a read-heavy workload.
[3328.72 --> 3329.26]  I'll tell you what.
[3329.82 --> 3331.06]  Yeah, it is.
[3331.54 --> 3332.58]  It definitely is.
[3332.66 --> 3336.78]  And if we were to, for example, if we had to have the database up, I really do think
[3336.78 --> 3341.22]  that going to a managed service, regardless who manages it, who manages that, it's a much
[3341.22 --> 3341.98]  better proposal.
[3342.24 --> 3342.68]  Oh, for sure.
[3342.68 --> 3346.38]  All the backups, like all the replication, all that stuff, it's managed.
[3346.66 --> 3347.72]  You don't have to do that.
[3347.74 --> 3350.24]  And you're just consuming the PostgreSQL interface.
[3350.38 --> 3350.76]  That's it.
[3351.10 --> 3353.16]  So that sounds like a much better proposal.
[3353.22 --> 3353.80]  Like a CDN.
[3353.88 --> 3354.96]  Would you run your own CDN?
[3355.14 --> 3355.54]  Maybe.
[3356.00 --> 3357.84]  I mean, if you're big enough, you'll have to.
[3358.24 --> 3359.62]  If you're that scale, sure.
[3359.92 --> 3360.08]  Right.
[3360.30 --> 3366.52]  And another thing about running databases inside Kubernetes is that you could think of
[3366.52 --> 3367.90]  it as almost addicting.
[3367.90 --> 3372.16]  Because once you make the decision that, well, we're not going to use an external database
[3372.16 --> 3372.64]  provider.
[3372.64 --> 3375.34]  Instead, we're going to just run them as stateful sets inside Kubernetes.
[3375.54 --> 3378.22]  And we believe in the Zolando operator, for example.
[3378.36 --> 3378.50]  Right.
[3378.56 --> 3381.70]  Well, you're going to find that your developers are naturally just going to be provisioning
[3381.70 --> 3382.26]  databases.
[3382.26 --> 3389.20]  And that's going to result in multiple stateful sets, not schemas in a large existing Postgres.
[3389.38 --> 3390.94]  It's just naturally going to proliferate.
[3391.60 --> 3396.16]  And that's the headache that you're going to feel, is that suddenly we have a client who's
[3396.16 --> 3399.00]  got hundreds of Postgres's.
[3399.20 --> 3401.02]  And I'm not going to name the client, obviously.
[3401.26 --> 3403.30]  But I will say they're running them wrong.
[3403.40 --> 3404.10]  And they know it.
[3404.20 --> 3404.52]  Right.
[3404.52 --> 3408.42]  It's technical debt that we're helping them dig out of.
[3408.58 --> 3413.00]  But it's a huge pain, huge cost for them.
[3413.34 --> 3414.62]  Once you get to a certain scale, you're right.
[3414.76 --> 3417.06]  You have to take a certain approach.
[3417.50 --> 3419.92]  But when you're not there, don't take that approach.
[3420.12 --> 3420.96]  Take the simpler one.
[3421.32 --> 3421.42]  Right.
[3421.48 --> 3425.42]  And what this approach means for us is that we can innovate elsewhere.
[3425.48 --> 3425.70]  Yes.
[3425.76 --> 3427.52]  And we can fight other battles.
[3427.86 --> 3431.40]  There will still be battles to fight, even if you don't do this one.
[3431.40 --> 3435.00]  It doesn't mean that you're less capable or less curious.
[3435.18 --> 3438.22]  It just means you've picked your battles in a way that suits you.
[3438.54 --> 3443.80]  And one of these days, as a company, you'll get big enough where you need that more interesting,
[3444.00 --> 3444.92]  innovative challenges.
[3445.40 --> 3448.44]  And there will be companies like ours to help you out when that happens.
[3448.74 --> 3451.66]  But please don't just assume you need that prematurely.
[3451.80 --> 3453.60]  There's a similar thing with writing code.
[3454.00 --> 3459.96]  I tell you, iterating on a code base, because I've spent half my career as an application developer
[3459.96 --> 3461.12]  as well as operations.
[3461.48 --> 3466.26]  Iterating on a code base before it's actually launched and in production is so much faster,
[3466.36 --> 3466.58]  right?
[3466.86 --> 3469.20]  You can make all kinds of schema changes.
[3469.44 --> 3470.12]  Like, who cares?
[3470.66 --> 3471.16]  Never ship.
[3471.24 --> 3471.94]  That's what you're saying.
[3472.02 --> 3472.24]  Yeah.
[3472.34 --> 3474.80]  Basically, never ship and you'll be the fastest startup.
[3475.20 --> 3476.44]  So the opposite of the show.
[3477.72 --> 3478.58]  Don't ship it.
[3480.48 --> 3482.20]  But I mean, it's the same thing.
[3482.46 --> 3486.36]  You launch when you need to launch, but you understand the fact that as soon as you launch,
[3486.36 --> 3489.46]  you're going to slow down by at least a factor of two, maybe three, right?
[3489.90 --> 3496.44]  And you increase the complexity of your operations stance, your Kubernetes usage when you need
[3496.44 --> 3496.66]  to.
[3496.76 --> 3500.46]  And you understand, I mean, even embracing Kubernetes, you do it when you need to.
[3500.54 --> 3503.46]  And you understand that that much complexity is going to slow you down.
[3504.08 --> 3505.10]  Yeah, that's a good one.
[3505.20 --> 3505.86]  That is a good one.
[3505.96 --> 3507.84]  So I think it's time to wrap up.
[3507.88 --> 3509.14]  We can have so much fun.
[3509.20 --> 3509.90]  I didn't realize.
[3510.52 --> 3511.94]  I think we just have to do this more often.
[3512.04 --> 3513.30]  That's the only conclusion again.
[3513.30 --> 3519.08]  As we are prepared to wrap up, what do you think the most important takeaway is for our
[3519.08 --> 3520.42]  listeners from this conversation?
[3521.92 --> 3525.60]  Well, I mean, I didn't think it was going to be this when we first started talking, but
[3525.60 --> 3529.10]  I think the most important takeaway is don't use Kubernetes unless you need to.
[3529.24 --> 3531.00]  Like delay the adoption of Kubernetes.
[3531.24 --> 3532.74]  It's going to be on your roadmap.
[3533.24 --> 3535.22]  It's going to happen as you grow.
[3535.60 --> 3539.80]  But just like anything else, don't try and tackle that problem early.
[3539.80 --> 3545.62]  Use one of the existing managed platforms, not managed Kubernetes installations.
[3545.90 --> 3548.00]  Although when you do adopt Kubernetes, do that.
[3548.56 --> 3549.96]  But just delay it for as long as you can.
[3550.04 --> 3553.00]  And then even then understand that you're spending innovation points.
[3553.14 --> 3559.32]  So use it in as simple of a way as you can, because you need to pay down that innovation
[3559.32 --> 3560.38]  debt, right?
[3560.52 --> 3566.78]  Focus on the automation and focus on the education for your people, because you will underestimate
[3566.78 --> 3568.58]  how complicated Kubernetes is.
[3568.58 --> 3573.64]  You will be surprised when you start using it and start seeing all of the different ways
[3573.64 --> 3577.34]  that you can configure it and all the best practices that are not codified in it.
[3577.76 --> 3581.50]  Well, thank you, Tamar, for sharing so much valuable information.
[3581.98 --> 3583.06]  And I had so much fun.
[3583.16 --> 3583.70]  This was great.
[3583.80 --> 3584.18]  Thank you.
[3584.38 --> 3585.54]  Yeah, I had so much fun too.
[3585.90 --> 3586.42]  Thank you.
[3586.56 --> 3587.80]  I'm looking forward to the next one.
[3587.96 --> 3588.44]  I really am.
[3588.52 --> 3588.86]  Absolutely.
[3589.12 --> 3589.40]  Thank you.
[3589.40 --> 3590.40]  Thank you.
[3590.46 --> 3591.40]  Thank you.
[3591.40 --> 3592.40]  Thank you.
[3592.40 --> 3593.08]  Thank you.
[3593.08 --> 3593.28]  Thank you.
[3593.28 --> 3595.14]  Thank you for tuning in to another episode of Ship It.
[3595.20 --> 3597.72]  This is just one of our podcasts for developers.
[3598.02 --> 3601.40]  Go to changelog.com forward slash master for the rest.
[3601.78 --> 3606.12]  You can join our community at changelog.com forward slash community.
[3606.48 --> 3607.98]  There are no imposters in our Slack.
[3608.20 --> 3609.46]  Everyone is welcome.
[3609.92 --> 3613.34]  Huge thanks to our partners Fastly, LaunchDarkly, and Linode.
[3613.34 --> 3616.72]  Thank you, Breakmaster Cylinder, for all our awesome beats.
[3617.02 --> 3617.90]  That's it for this week.
[3618.08 --> 3618.72]  See you next week.
[3643.34 --> 3650.86]  Hey-
[3650.86 --> 3651.58]  Bye-
[3651.58 --> 3652.98]  Bye-
[3652.98 --> 3655.32]  Bye-
[3655.60 --> 3655.92]  Bye-
[3655.92 --> 3656.04]  Bye-
[3656.04 --> 3656.98]  Bye-
[3656.98 --> 3657.50]  Bye-
[3657.58 --> 3657.74]  Bye-
[3657.74 --> 3659.30]  Bye-
[3659.30 --> 3659.96]  Bye-
[3659.96 --> 3661.02]  Bye-
[3661.02 --> 3661.64]  Bye-
[3661.64 --> 3662.78]  Bye-
[3662.78 --> 3663.62]  Bye-
[3663.62 --> 3665.90]  Bye-
[3665.90 --> 3666.42]  Bye-
[3667.64 --> 3668.94]  Bye-
[3669.00 --> 3671.16]  Bye-
[3671.58 --> 3671.66]  Bye-
[3671.66 --> 3672.36]  Bye-
[3672.36 --> 3673.26]  Bye-
[3673.26 --> 3673.32]  Bye-
