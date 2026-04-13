[0.08 --> 6.54]  Welcome to ShipIt.show, a podcast about ops, infrastructure, and rave mode.
[7.04 --> 12.14]  Fastly.com keeps us fast. Fly.io makes our app fly.
[12.42 --> 18.68]  This is episode 64, and in all previous episodes, we have not had anyone do something as unexpected.
[19.18 --> 24.30]  Our today's guest spent four days building a feature for his side project
[24.30 --> 28.16]  so that we could ship it together on ShipIt while recording.
[28.16 --> 31.36]  The feature is called rave mode and the context is bass,
[31.84 --> 37.70]  an interpreted functional scripting language written in Go, riffing on the ideas of kernel and closure.
[38.14 --> 43.14]  When the local build runs, you can now press R to synchronize the beats
[43.14 --> 47.04]  of your currently playing Spotify track with the build output.
[47.54 --> 52.34]  I mean, this is just a whole new level of fun and love for CI CD.
[52.34 --> 56.10]  Please welcome Alex Surachi, aka Vito,
[56.10 --> 59.10]  the creator of Concourse CI and bass.
[59.44 --> 60.76]  There's one more thing.
[61.24 --> 65.96]  This episode is dedicated to the late John Schutt, the creator of kernel.
[66.52 --> 68.70]  Your ideas continue in bass.
[69.20 --> 71.88]  Thank you for getting them out into the world.
[71.88 --> 79.20]  This episode is brought to you by Sourcegraph.
[79.30 --> 84.30]  With the launch of their Code Insights product, teams can now track what really matters in their code base.
[84.60 --> 90.92]  Code Insights instantly transforms your code base into a queryable database to create visual dashboards in seconds.
[91.30 --> 94.36]  And I'm here with Joel Cortler, the product manager of Code Insights for Sourcegraph.
[94.36 --> 98.94]  Joel, the way teams can use Code Insights seems to pretty much be limitless.
[99.08 --> 104.52]  But a particular problem every engineering team has is tracking versions of languages or packages.
[104.84 --> 107.72]  How big of a deal is it actually to track versions for teams?
[108.18 --> 109.92]  Yeah, it's a big deal for a couple of reasons.
[110.08 --> 111.90]  The first is, of course, just compatibility.
[111.90 --> 116.04]  You don't want things to break when you're testing locally or to break on your CI systems or test systems.
[116.22 --> 119.94]  You need to have some sort of level of like version unification, minimum versions afforded.
[119.94 --> 122.68]  And all of that needs to be compatible forward.
[122.96 --> 127.88]  But the other thing we learned was that for a lot of customers, especially, you know, engineer organizations that are pretty established,
[128.32 --> 133.96]  they have older versions of things or even older versions of like SaaS tools they don't use anymore that they haven't fully removed
[133.96 --> 136.84]  because they're like not sure if it's still in use or they lost focus on that.
[136.84 --> 139.96]  And they're spinning up old virtual machines that they're still paying for.
[140.08 --> 144.08]  They're using, you know, old SaaS subscriptions they're afraid to cancel because they're not sure if anyone's actually using it.
[144.20 --> 149.60]  And so getting off of those versions not just like saves you the headaches and the risks and the vulnerabilities of being on old versions,
[149.60 --> 157.46]  but also literally the money of, you know, older systems running more slowly or the build times or, you know, virtual machines and SaaS tools that you're no longer using.
[157.78 --> 159.66]  Before you had this ability, we talked to teams.
[159.98 --> 161.34]  There are basically three ways you could do this.
[161.62 --> 165.08]  You could slack a million people and ask for just like an update point in time.
[165.08 --> 174.32]  You could have sort of one human and one spreadsheet where like it's somebody's job every Friday or every two weeks to just like search all the code and find all the versions and write it down in a Google sheet.
[174.58 --> 178.86]  Or there were a couple of companies I came across with in-house systems that were sort of complicated.
[178.86 --> 181.98]  You had to know, you know, maybe Kotlin, but you didn't know Kotlin.
[182.06 --> 189.26]  But if you want to use this system, you had to learn Kotlin and you'd have to sort of build the whole world from scratch and run basically a tool like this with a pretty steep learning curve.
[189.34 --> 197.18]  And now for all three of those, you could replace it with a single line source graph search, which is basically just the name of the thing you're trying to track and the version string in the right format.
[197.46 --> 200.70]  And then we have templates that'll help you get started if you're not sure what that format is.
[200.86 --> 203.96]  And then it'll automatically track all the different versions for you, both historically.
[204.14 --> 206.28]  So even if you start using it today, you can see your historical patterns.
[206.68 --> 207.76]  And then, of course, going forward.
[207.76 --> 209.02]  Very cool. Thank you, Joel.
[209.12 --> 216.42]  So right now there is a treasure trove of insights just waiting for you living inside your code base right now.
[216.70 --> 220.40]  Teams are tracking migrations, adoption, deprecations.
[220.40 --> 223.58]  They're detecting and tracking versions of languages and packages.
[223.58 --> 227.56]  They're removing or ensuring the removal of security vulnerabilities.
[227.56 --> 229.52]  They understand their code by team.
[229.60 --> 231.28]  They can track their code smells and health.
[231.28 --> 235.84]  And they can visualize configurations and services and so much more with code insights.
[235.84 --> 242.48]  A good next step is to go to about.sourcegraph.com slash code dash insights.
[242.48 --> 245.30]  See how other teams are using this awesome feature.
[245.50 --> 250.38]  Again, about.sourcegraph.com slash code dash insights.
[250.38 --> 252.42]  This link is in the show notes.
[259.42 --> 260.70]  We are going to shift.
[260.86 --> 261.14]  Three.
[261.94 --> 262.24]  Two.
[262.84 --> 263.36]  One.
[263.36 --> 266.52]  One.
[266.52 --> 267.88]  One.
[267.88 --> 268.36]  One.
[276.62 --> 276.98]  One.
[276.98 --> 280.04]  I've been looking forward to this for some time now.
[280.62 --> 282.38]  Seven months to be more precise.
[282.38 --> 285.12]  and we have lots to talk about.
[285.72 --> 290.72]  Concourse CI, base, the wider CI-CD problem space,
[291.04 --> 294.18]  and we have just the right person for this today.
[295.06 --> 296.78]  Alex, welcome to ShipIt.
[297.02 --> 297.90]  Thanks, good to be here.
[298.50 --> 301.92]  So eight years ago, I think if I'm counting correctly,
[302.72 --> 304.88]  you had the idea of the CI-CD system
[304.88 --> 308.12]  that was different from everything else that came before.
[308.52 --> 310.20]  We all know it as Concourse CI.
[310.20 --> 313.84]  At the time, what made you believe
[313.84 --> 316.34]  that the world needed Concourse?
[316.72 --> 319.10]  It's a good question because there was already
[319.10 --> 321.36]  a lot of CI-CD systems out there,
[321.58 --> 323.38]  and there's even more every day, it seems like.
[323.66 --> 326.00]  But I mean, what really drove it was
[326.00 --> 327.78]  we were trying to use Jenkins,
[328.18 --> 330.32]  and we were trying to use that to automate
[330.32 --> 333.80]  all of Cloud Foundry, which was a massive pipeline.
[334.26 --> 335.92]  We were gluing together plugins
[335.92 --> 337.88]  and trying to keep that thing running,
[337.88 --> 339.38]  and it was kind of its own separate job,
[339.38 --> 340.84]  just keeping Jenkins in check.
[341.32 --> 344.58]  And meanwhile, we were building out this platform
[344.58 --> 346.26]  that was driven by declarative VM,
[346.34 --> 347.44]  where you just say what you want,
[347.54 --> 349.34]  and then you tell it to go, the system figures it out.
[349.70 --> 351.80]  And the thing that we were using to drive that
[351.80 --> 352.96]  was very much the opposite.
[353.30 --> 357.40]  So I wanted to try and take what we learned from that
[357.40 --> 359.02]  and apply it to CI-CD.
[359.58 --> 362.66]  I think the main motivation was having just clarity
[362.66 --> 363.86]  in how the whole system works,
[363.86 --> 365.70]  and being able to trust it,
[365.90 --> 370.40]  and not worrying about if that VM gets struck by lightning and dies,
[370.48 --> 372.58]  we have to spend another week just getting everything,
[372.82 --> 374.50]  clicking all the right buttons,
[374.92 --> 376.20]  getting it how it was again.
[376.50 --> 380.24]  So that's what brought Concourse to the world, really.
[380.80 --> 383.42]  Myself and Chris Brown raging at Jenkins.
[384.32 --> 385.08]  Chris Brown.
[385.38 --> 386.74]  We actually worked together.
[386.94 --> 388.08]  We were in the London office,
[388.08 --> 391.74]  and we were also struggling with Jenkins big time,
[391.92 --> 393.36]  and GoCD as well.
[393.42 --> 394.20]  We tried a couple.
[394.58 --> 397.40]  We went through a phase where we've been trying different CIs,
[397.56 --> 399.42]  and none of them were quite cutting it.
[399.80 --> 401.56]  We had the problem of the data services,
[402.16 --> 405.38]  Cassandra and MySQL and Redis and RabbitMQ.
[405.72 --> 410.90]  How do you package them in a way that platform teams can use them
[410.90 --> 414.52]  to enable developer teams to just get on with application code
[414.52 --> 415.54]  and just provision services?
[416.16 --> 417.98]  So how do you package that?
[418.08 --> 418.80]  How do you upgrade?
[419.08 --> 420.78]  And you obviously have to test all the things.
[421.14 --> 424.02]  How do you get CVEs out quickly enough?
[424.36 --> 425.82]  And a bunch of concerns like that.
[425.86 --> 426.72]  How do you scale?
[427.10 --> 428.44]  How do you degrade gracefully?
[429.14 --> 430.16]  It was such a pain.
[430.62 --> 433.72]  And interestingly, Jenkins was one of those services.
[434.84 --> 437.38]  And I remember Tamer at the time,
[437.70 --> 440.72]  he was the PM on the Pivotal side,
[440.72 --> 441.58]  and he was saying,
[441.78 --> 445.72]  hey, if the product that we're packaging doesn't work,
[445.72 --> 449.70]  let's not try and work around the shortcomings by automation.
[450.02 --> 451.14]  I remember that very clearly.
[451.28 --> 454.78]  So Jenkins, we were very intimate of how it worked,
[454.78 --> 457.72]  because we ourselves had to do it for other customers,
[457.72 --> 458.78]  and we were using it.
[458.82 --> 459.90]  We were like dogfooding it.
[459.90 --> 463.04]  And it was failing in so many weird and wonderful ways.
[463.58 --> 464.72]  And then Concourse came along.
[466.26 --> 466.74]  Nice.
[467.56 --> 468.12]  Chris Brown.
[468.26 --> 469.52]  Yeah, I haven't talked to him in years.
[469.68 --> 470.66]  How is he these days?
[470.78 --> 471.80]  Do you know about him?
[471.84 --> 472.84]  Hey, Chris, if you're listening,
[473.52 --> 474.34]  I'm saying hi.
[474.88 --> 475.66]  Hope you are.
[475.66 --> 478.06]  Yeah, he's just living it up at Stripe,
[478.32 --> 479.78]  doing a lot of...
[479.78 --> 482.88]  He's actually working on their workflow engine team,
[483.16 --> 486.90]  which uses Temporal under the hood,
[487.34 --> 488.02]  which is kind of a...
[488.02 --> 488.88]  Ooh, interesting.
[489.16 --> 490.16]  Yeah, kind of a funny coincidence,
[490.16 --> 492.72]  because they showed up on GitHub discussions a while back
[492.72 --> 496.14]  saying how they use Concourse to deliver Temporal.
[496.30 --> 496.68]  Wow.
[496.88 --> 498.50]  And they linked this article,
[498.94 --> 500.52]  and it was from San Diego Times or something.
[500.94 --> 503.26]  And the screenshot in the article was not Temporal.
[503.26 --> 505.54]  It was their dashboards, their Concourse dashboards
[505.54 --> 506.70]  that deliver Temporal.
[507.36 --> 508.00]  That's crazy.
[508.42 --> 509.58]  What a small world.
[509.82 --> 512.20]  Yeah, the places that Concourse Webby shows up
[512.20 --> 512.86]  is always interesting.
[513.44 --> 514.20]  Okay, okay.
[514.68 --> 519.60]  So I think one of the things that made Concourse so memorable
[519.60 --> 521.90]  and so it had a face,
[522.24 --> 523.46]  and the face was the pipeline.
[523.98 --> 526.14]  I don't think, at least in my experience,
[526.18 --> 529.44]  I haven't seen any other CI that did pipelines
[529.44 --> 530.92]  or that does pipelines,
[530.92 --> 533.82]  the views of a pipeline as good as Concourse did it.
[534.28 --> 535.44]  Whose idea was that,
[535.52 --> 538.02]  to make that the only,
[538.18 --> 539.70]  the default Concourse view
[539.70 --> 541.06]  and the only Concourse view?
[543.04 --> 545.28]  Well, it's since gotten a little more complicated.
[545.28 --> 547.06]  There's the whole dashboard that wraps it
[547.06 --> 549.28]  and it compresses into a thumbnail view thingy.
[550.00 --> 550.20]  Right.
[550.62 --> 551.56]  And you click into that.
[551.56 --> 555.72]  But ultimately, the UI that we have today
[555.72 --> 559.02]  was myself and Amit, Amit Gupta,
[559.70 --> 561.96]  just messing around after hours at Pivotal,
[562.08 --> 564.62]  trying to come up with what is a good visualization.
[565.14 --> 568.92]  The first stage was actually just using GraphViz
[568.92 --> 572.00]  and just feeding it a DAG
[572.00 --> 572.96]  and then seeing what it renders.
[573.22 --> 574.60]  And it did interesting things,
[574.68 --> 576.86]  but it couldn't quite express fan out, fan in,
[576.86 --> 578.20]  and all the different kinds of things.
[578.44 --> 581.88]  So that turned into just banging my face
[581.88 --> 584.30]  against JavaScript until things mostly worked
[584.30 --> 586.16]  and then fixing whatever bugs came up.
[586.82 --> 586.98]  Yeah.
[587.34 --> 588.02]  You're right.
[588.14 --> 588.98]  You're actually right.
[588.98 --> 591.98]  You mentioned the collection of pipelines.
[593.16 --> 594.26]  That was added later on.
[594.38 --> 595.60]  I remember it for many years,
[595.70 --> 598.04]  back in the time when it first came out.
[598.22 --> 599.44]  It was just the pipeline view
[599.44 --> 600.34]  and that kept improving.
[600.78 --> 603.00]  I really liked the small incremental improvements.
[603.00 --> 608.50]  I really liked the groove box-like initial design
[608.50 --> 609.50]  because then it changed,
[609.58 --> 610.64]  became a bit more brighter.
[611.00 --> 612.12]  Oh, I see what you mean, the colors.
[612.64 --> 613.74]  Yes, the colors, exactly.
[614.34 --> 615.42]  I really liked those.
[615.46 --> 616.18]  It was a bit rough,
[616.28 --> 618.08]  but it was just the right amount of rough
[618.08 --> 618.98]  and it was very memorable.
[619.14 --> 621.40]  And you could see it everywhere in all the offices,
[622.04 --> 623.14]  in all the Pivotal offices,
[623.14 --> 625.16]  because there was like so much stuff
[625.16 --> 625.88]  that we were building
[625.88 --> 627.40]  and there were monitors everywhere
[627.40 --> 629.10]  and you could just like take a look
[629.10 --> 630.70]  and see exactly what the problem was.
[631.18 --> 632.18]  And I think the problem was like
[632.18 --> 633.48]  that we had too many pipelines.
[633.82 --> 635.60]  So I think that's where the view came from, right?
[635.68 --> 636.50]  Like the one with-
[636.50 --> 637.06]  Yeah, the dashboard.
[637.22 --> 637.88]  Yeah, exactly.
[638.58 --> 639.96]  It's funny how it all evolved
[639.96 --> 642.78]  because initially Concourse was literally,
[643.00 --> 644.52]  you would start the ATC program,
[644.66 --> 646.46]  ATC being like the coordinator,
[646.72 --> 647.50]  web UI, everything,
[647.74 --> 648.70]  kind of a bit of a monolith.
[649.04 --> 650.86]  And you would literally just give it a config file.
[651.36 --> 652.98]  And that config file was the pipeline.
[652.98 --> 654.70]  And then we went from there to like,
[654.76 --> 655.96]  what if you want multiple pipelines?
[656.14 --> 657.08]  And then from there to like,
[657.32 --> 658.42]  what if you want multiple teams?
[658.76 --> 660.30]  And then pipeline groups.
[660.36 --> 661.48]  And now you have like the whole dashboard,
[661.48 --> 662.38]  like multiple teams
[662.38 --> 663.60]  and like entire enterprises
[663.60 --> 664.88]  putting everything on one box.
[665.02 --> 666.12]  And that's how you lead to like,
[666.94 --> 668.68]  melting machines and things like that.
[668.76 --> 671.52]  But it started off quaint and fun.
[672.28 --> 674.66]  What was the biggest early on challenge
[674.66 --> 676.08]  when you started Concourse?
[676.72 --> 677.18]  Do you remember?
[677.64 --> 679.82]  I think probably the biggest challenge
[679.82 --> 682.24]  was just managing the pace of onboarding
[682.24 --> 683.74]  and trying to balance like,
[684.62 --> 685.92]  having a good ratio of people
[685.92 --> 687.02]  that actually want to use it
[687.02 --> 688.86]  versus people that felt like
[688.86 --> 689.62]  there was some,
[689.70 --> 690.26]  you know,
[690.84 --> 691.98]  thing that they have to use it.
[692.70 --> 693.86]  Because that really changes
[693.86 --> 694.94]  the types of interactions
[694.94 --> 696.04]  that you get with people.
[696.18 --> 697.22]  Like if you're trying to,
[697.38 --> 698.22]  if you're providing something
[698.22 --> 700.20]  where you're solving a problem
[700.20 --> 700.86]  that they have,
[700.98 --> 702.72]  you'll get like much nicer interactions.
[702.72 --> 704.62]  But if you're building something
[704.62 --> 705.86]  that they feel like they have to use,
[705.90 --> 707.84]  then they don't pull as many punches.
[708.26 --> 709.22]  It's not going well.
[709.88 --> 711.70]  Did people feel instinctively,
[711.82 --> 713.22]  like did they know instinctively
[713.22 --> 714.30]  what to do with Concourse?
[714.30 --> 716.28]  Or did it take a while
[716.28 --> 718.08]  to explain what it is
[718.08 --> 719.72]  and how to configure it
[719.72 --> 720.32]  and how to,
[720.86 --> 721.82]  how did you find that?
[722.20 --> 723.82]  I think people did pretty okay
[723.82 --> 725.22]  at like picking up how to use it,
[725.24 --> 726.08]  at least within Pivotal.
[726.42 --> 727.44]  I'm not going to go as far
[727.44 --> 728.42]  as to say it was easy.
[728.62 --> 730.44]  They probably really stumbled for a while
[730.44 --> 731.92]  and I wouldn't be surprised
[731.92 --> 733.14]  if a lot of them didn't like it
[733.14 --> 734.12]  because the documentation
[734.12 --> 735.20]  was just, you know,
[735.48 --> 737.38]  us writing the best we could.
[737.50 --> 738.96]  It was all just like reference material.
[739.10 --> 742.14]  We never really had like a technical writer.
[742.14 --> 744.54]  Yeah, I think like there were a lot of times
[744.54 --> 745.74]  where it would be like called over
[745.74 --> 746.80]  to help someone figure out
[746.80 --> 747.92]  how to do something in a pipeline.
[748.96 --> 751.44]  One of the like most common pain points
[751.44 --> 754.54]  was like someone wanted to acquire an environment
[754.54 --> 757.12]  and then like use that environment
[757.12 --> 758.22]  through a few jobs
[758.22 --> 760.04]  and then release it in a later job.
[760.64 --> 762.92]  And that was always painful to do with Concourse.
[763.10 --> 765.96]  I think we never really had a great solution to that.
[766.06 --> 767.54]  We had like an interesting one
[767.54 --> 769.80]  that used a Git repo as a lock,
[769.80 --> 772.10]  which worked, but it was a little kludgy
[772.10 --> 773.76]  because you have to manually release it now and then.
[774.08 --> 774.90]  There were a lot of people doing that
[774.90 --> 776.12]  because there were a lot of people using Concourse
[776.12 --> 777.48]  for continuous delivery.
[778.52 --> 782.06]  I'm pretty sure that you are one of the people
[782.06 --> 783.30]  that felt that Concourse
[783.30 --> 785.36]  was more than a CICV system.
[785.70 --> 788.16]  It was like integrating with all these things
[788.16 --> 790.70]  and there was like so much possibility,
[791.08 --> 791.60]  as you mentioned,
[791.74 --> 793.20]  like integrating with Git, with GitHub,
[793.58 --> 796.04]  with a Git repository for like locks and S3.
[796.04 --> 799.44]  And it was basically the state
[799.44 --> 802.88]  you had to keep it outside of Concourse
[802.88 --> 805.24]  or like some very good, strong principles.
[805.64 --> 807.28]  How did you think of Concourse
[807.28 --> 808.82]  from the beginning all the way
[808.82 --> 811.84]  until like you stopped working on it?
[812.34 --> 813.38]  I always kind of thought of it
[813.38 --> 818.66]  as a way to codify your entire like dependency chain
[818.66 --> 820.30]  and automation process.
[820.94 --> 822.80]  Kind of like if this, then that,
[822.80 --> 824.56]  but more generally,
[824.76 --> 825.86]  like what are all the things
[825.86 --> 828.02]  that people would be manually doing
[828.02 --> 829.10]  within your organization
[829.10 --> 831.24]  or imagining you're like one person
[831.24 --> 832.68]  trying to drive an entire startup.
[832.96 --> 834.54]  That's kind of where I imagine
[834.54 --> 835.74]  Concourse being very useful
[835.74 --> 837.94]  because then you just can empower yourself
[837.94 --> 838.74]  to get more done
[838.74 --> 841.08]  because you've just like have something else
[841.08 --> 842.36]  doing it all for you.
[842.64 --> 844.44]  Whether that's like automated testing
[844.44 --> 847.16]  or automated like periodic longevity tests
[847.16 --> 848.16]  that like run every hour
[848.16 --> 849.34]  and just make sure your tests
[849.34 --> 850.58]  didn't suddenly get more flaky
[850.58 --> 853.26]  or like testing infrastructure reliability
[853.26 --> 856.68]  or just anything that you need to do continuously.
[857.28 --> 858.24]  Concourse was your guy.
[858.36 --> 858.86]  That was the idea.
[860.50 --> 864.22]  I always saw it as automation with a nice UI.
[864.70 --> 864.78]  Yeah.
[865.02 --> 865.96]  I mean, that's what it was.
[866.02 --> 867.64]  And you were able to do things,
[867.68 --> 868.58]  as you mentioned, checks.
[869.34 --> 870.66]  And at a glance,
[870.66 --> 871.86]  you could see are they passing
[871.86 --> 872.70]  or are they failing?
[873.06 --> 873.22]  Right.
[873.38 --> 875.38]  And what is the failure ratio?
[876.06 --> 876.78]  I mean, there were like
[876.78 --> 878.42]  so many interesting things there.
[878.42 --> 881.68]  The logs, the pipeline view is so important.
[881.78 --> 883.58]  Like the state of resources, for example,
[883.86 --> 886.06]  like it has some very simple primitives,
[886.06 --> 887.26]  but it was very versatile.
[887.70 --> 887.80]  Yeah.
[887.84 --> 889.86]  It was so much more than the CI-CD system.
[889.94 --> 891.60]  I think that's what people saw in it.
[892.12 --> 893.26]  I mean, at some point,
[893.30 --> 895.04]  I know it was like the distribution mechanism
[895.04 --> 896.20]  for the pivotal software
[896.20 --> 899.00]  because pretty much everyone that had,
[899.16 --> 901.60]  that was running all these like large clusters,
[901.80 --> 902.82]  whether it was Cloud Foundry,
[902.92 --> 904.42]  whether it was like all the stateful services,
[904.90 --> 906.54]  how do you keep everything up to date?
[906.54 --> 907.76]  Never mind the applications.
[908.34 --> 909.86]  So you needed to provide automation
[909.86 --> 911.24]  that shows you the health
[911.24 --> 913.42]  at the glance of what is happening.
[913.64 --> 915.12]  You had to have notifications,
[915.52 --> 916.38]  all that, all the thing.
[916.44 --> 917.80]  And also when there's a problem,
[917.92 --> 921.00]  you had to go and debug it quickly.
[921.88 --> 921.90]  Yeah.
[921.96 --> 924.24]  It kind of acted as like the central plane.
[924.34 --> 925.38]  It was like the source of truth
[925.38 --> 927.34]  for like what's the status of the whole system,
[927.66 --> 929.14]  which is kind of interesting
[929.14 --> 930.62]  because like when COVID hit
[930.62 --> 931.92]  and everyone started working from home,
[931.92 --> 933.52]  suddenly we didn't have like the central,
[933.72 --> 934.82]  you know, dashboard TV
[934.82 --> 936.58]  that everyone looked at became much harder
[936.58 --> 938.38]  to keep tabs on CICD
[938.38 --> 940.32]  and metrics and things like that.
[940.90 --> 942.58]  So that got me thinking more
[942.58 --> 943.96]  about like notifications
[943.96 --> 946.48]  or something that like keeps it more in your face,
[946.56 --> 948.90]  but don't have anything deep there.
[949.38 --> 951.22]  What was it like to work on Concourse
[951.22 --> 952.14]  for so many years?
[952.56 --> 954.76]  I mean, I think it was six, seven, roughly.
[955.24 --> 956.52]  It was a long ride.
[956.84 --> 957.02]  Yeah.
[957.34 --> 958.00]  What was it like?
[958.16 --> 958.78]  It was a lot of fun.
[958.78 --> 960.56]  The team obviously like, you know,
[960.60 --> 961.70]  changed in cycles,
[961.88 --> 963.02]  like Pivotal was all about
[963.02 --> 965.88]  like rotating people semi-frequently.
[966.14 --> 967.12]  They really slowed down.
[967.64 --> 968.92]  When I moved to Toronto,
[969.24 --> 971.26]  the rate of rotation like really slowed down.
[971.52 --> 972.86]  I think it was just different office culture,
[973.02 --> 974.88]  but like throughout those six years,
[974.88 --> 977.40]  it was just a lot of really fun engineers to work with.
[977.58 --> 980.52]  We had some good team culture things early on.
[980.60 --> 982.10]  We had every retro,
[982.32 --> 984.42]  someone from the team would like make a dish
[984.42 --> 986.72]  from their home culture and like bring it
[986.72 --> 988.34]  and we'd like let the whole office have it.
[988.34 --> 992.04]  And I think probably the highlight of my career though
[992.04 --> 994.44]  was when we had a retro
[994.44 --> 995.76]  and someone literally just put like,
[995.84 --> 997.34]  I love my job in the happy column.
[997.58 --> 998.86]  I was like, wow, cool.
[999.42 --> 1000.54]  Doing something right, I guess.
[1000.90 --> 1001.48]  That's amazing.
[1001.72 --> 1001.88]  Yeah.
[1002.34 --> 1003.90]  That was a very fortunate person.
[1004.10 --> 1005.48]  I was a very fortunate team.
[1006.14 --> 1008.98]  And I think we felt it as users.
[1009.38 --> 1011.32]  I mean, sure, we were frustrated at times,
[1011.32 --> 1013.72]  but we could see how hard everyone was working.
[1013.96 --> 1014.18]  Oh yeah.
[1014.18 --> 1017.12]  Seeing on GitHub, all the pull requests,
[1017.26 --> 1019.40]  all the issues, all the stuff that was going through.
[1019.48 --> 1022.42]  There was so much stuff, so many good things, great things.
[1023.14 --> 1024.62]  And even from the outside,
[1024.70 --> 1025.88]  it felt like it was a great ride.
[1027.06 --> 1031.46]  So after Concourse, you started something else, base.
[1031.96 --> 1032.62]  What is base?
[1033.56 --> 1036.10]  Base is kind of trying to learn
[1036.10 --> 1038.60]  from what I think were some of the mistakes with Concourse.
[1039.02 --> 1042.14]  One of them being try to express a system
[1042.14 --> 1044.98]  that can do everything, but like within the confines
[1044.98 --> 1046.84]  of a declarative YAML config.
[1047.58 --> 1048.54]  YAML is a problem.
[1048.80 --> 1050.84]  Like everyone listening, it's not the declarative part.
[1050.90 --> 1051.34]  That's okay.
[1051.42 --> 1051.78]  That's good.
[1051.84 --> 1052.34]  We like that.
[1052.74 --> 1054.86]  So what is wrong with YAML?
[1055.02 --> 1056.96]  What is wrong with that combination?
[1057.50 --> 1059.60]  I think there's, I could debate both parts, I think.
[1060.46 --> 1062.86]  Some aspects of declarative are also kind of falling
[1062.86 --> 1065.86]  out of favor with me, but that's, it's like largely a,
[1065.86 --> 1068.68]  I think it's because I'm kind of shifting away
[1068.68 --> 1069.72]  from both at the same time.
[1069.72 --> 1071.58]  So I'm really like considering alternatives
[1071.58 --> 1073.00]  to declarative systems too.
[1073.70 --> 1073.82]  Really?
[1074.52 --> 1075.14]  Do tell.
[1075.26 --> 1076.04]  That's very interesting.
[1076.54 --> 1078.54]  But yeah, I mean, with, with the YAML part,
[1078.58 --> 1080.76]  it's really just like not having a real language
[1080.76 --> 1081.48]  at your disposal.
[1081.48 --> 1083.88]  You're kind of inventing like a language within it.
[1084.56 --> 1087.42]  Like we like to say that Concourse pipelines
[1087.42 --> 1088.68]  were declarative schema,
[1088.68 --> 1091.18]  but really it was declaring a set of jobs
[1091.18 --> 1093.90]  that then had like an imperative plan within them.
[1094.28 --> 1097.62]  And the more, you know, bespoke we made that DSL,
[1097.62 --> 1100.24]  we got into things like scoping,
[1100.56 --> 1103.02]  like what's the scope of this value
[1103.02 --> 1104.54]  that's being bound within the build plan.
[1105.48 --> 1108.16]  Largely with like the across step is where this came up.
[1108.44 --> 1110.58]  The across step was like one of the most recently
[1110.58 --> 1113.06]  introduced ones where it's like across all these values
[1113.06 --> 1113.86]  do this step.
[1114.30 --> 1117.66]  So you end up like wanting to bind an asset to a value,
[1117.76 --> 1119.52]  but then it's like, does that scope,
[1119.74 --> 1121.92]  like does that binding escape to later steps?
[1122.48 --> 1124.46]  And then it's like, why are we just not implementing
[1124.46 --> 1127.02]  a language where like doing across is just a for loop?
[1127.02 --> 1129.72]  So that's kind of where I am with YAML.
[1129.96 --> 1132.20]  It's just not very well suited, I think,
[1132.26 --> 1135.14]  to actually expressing something.
[1135.90 --> 1138.46]  And that's why like so many people end up templating it.
[1139.04 --> 1140.68]  And then you just have like two problems.
[1140.78 --> 1142.82]  Now you're like thinking at like a template level
[1142.82 --> 1143.70]  and a YAML level.
[1144.68 --> 1146.66]  Now you need to like manage that pipeline
[1146.66 --> 1147.82]  feeding into the system.
[1148.28 --> 1150.74]  So yeah, it just makes things way more complicated, I think.
[1151.30 --> 1151.48]  Okay.
[1152.26 --> 1154.18]  So when it comes to the declarative part,
[1154.18 --> 1155.72]  I mean, I'm still stuck on that
[1155.72 --> 1157.52]  because I wasn't expecting it to be honest.
[1157.52 --> 1158.82]  And I'm surprised.
[1159.56 --> 1163.00]  And I'm just curious, like what could be better
[1163.00 --> 1164.26]  than declarative?
[1164.72 --> 1166.66]  There's a solid chance that I'm wrong in this.
[1166.74 --> 1169.88]  And like I go back to being declarative is great.
[1170.22 --> 1172.44]  But the problem that I see with it...
[1172.44 --> 1174.04]  All great engineers say that.
[1174.46 --> 1175.48]  All great engineers.
[1175.68 --> 1177.36]  There's a good chance I'm wrong with this.
[1177.42 --> 1179.14]  But still, this is what I think.
[1179.14 --> 1180.82]  So tick.
[1181.10 --> 1181.30]  Appreciate it.
[1181.74 --> 1185.22]  The problem I see with declarative approaches to CICD
[1185.22 --> 1189.20]  is the system they're building around is not declarative.
[1189.82 --> 1193.00]  Like the system being developers just running commands.
[1193.38 --> 1195.82]  Most people, they'll like go to CICD.
[1195.96 --> 1197.70]  They'll know what commands they want to run.
[1197.94 --> 1199.08]  Like I want to run GoTest.
[1199.16 --> 1201.00]  I want to run like RSpec or whatever.
[1201.66 --> 1203.12]  Or whatever their build process is.
[1203.26 --> 1205.24]  Like commands are already the foundation
[1205.24 --> 1206.80]  that we're really building everything upon.
[1206.80 --> 1210.78]  Even Docker and BuildKit kind of like build on that abstraction
[1210.78 --> 1212.64]  because they're all about just running commands in containers.
[1213.46 --> 1217.08]  The problem I see with declarative wrapping systems for that
[1217.08 --> 1220.62]  is that someone has to implement the mapping
[1220.62 --> 1223.10]  between like declaring what you want
[1223.10 --> 1224.60]  and having that boil down to commands.
[1225.30 --> 1226.90]  And we saw this with Concourse
[1226.90 --> 1229.24]  where like the Git resource started off
[1229.24 --> 1230.72]  as just like a perfect example
[1230.72 --> 1232.92]  of just a tiny little Concourse resource.
[1232.92 --> 1236.86]  It does like Git clone, Git fetch, Git push.
[1237.34 --> 1237.78]  That's it.
[1238.20 --> 1241.82]  But the reality was that like everyone uses Git differently.
[1242.88 --> 1245.74]  So if you look at the like slash ops,
[1245.84 --> 1247.54]  slash resource, slash inscript now,
[1247.66 --> 1251.04]  it's like a hundred line bash file
[1251.04 --> 1253.28]  handling like a bunch of different use cases,
[1253.98 --> 1256.40]  like tagged versioning, things like that.
[1256.40 --> 1260.46]  And you have to kind of distill that up to what in Concourse is YAML.
[1260.82 --> 1261.66]  Resource doesn't care.
[1261.76 --> 1262.22]  It's just JSON.
[1262.48 --> 1265.12]  But in any case, somewhere there's like a declarative config
[1265.12 --> 1267.26]  that maps to commands running.
[1267.38 --> 1269.68]  And it just like kind of adds an extra level of indirection
[1269.68 --> 1272.24]  between what the developer knows they want to run
[1272.24 --> 1274.26]  and how they know it's actually going to run.
[1274.54 --> 1277.76]  And there's like the added toil of someone managing that mapping interface.
[1278.72 --> 1279.90]  I mean, all that being said,
[1280.00 --> 1284.00]  like commands aren't necessarily the best interface to expose.
[1284.00 --> 1285.60]  It's just what people already know.
[1285.94 --> 1287.86]  I think if you are able to express something
[1287.86 --> 1289.58]  as just a declarative thing and it works
[1289.58 --> 1290.64]  and it's like low enough maintenance
[1290.64 --> 1292.82]  and maybe you get bells and whistles like static typing
[1292.82 --> 1296.06]  or easy to verify schemas and things like that,
[1296.12 --> 1299.48]  then I think like it is possible for the value tradeoff to be there.
[1299.64 --> 1302.26]  But I guess from my current perspective
[1302.26 --> 1305.14]  of like trying to build base as like a side thing,
[1305.54 --> 1306.66]  not expend too much effort,
[1306.82 --> 1308.40]  it would be a lot of effort for me
[1308.40 --> 1310.40]  to have to invent these mappings for everything
[1310.40 --> 1311.70]  as opposed to just being like,
[1311.80 --> 1312.80]  hey, it runs commands.
[1312.80 --> 1315.66]  So maybe that's my bias right now.
[1316.14 --> 1316.24]  Yeah.
[1316.68 --> 1317.90]  So when you say commands,
[1318.02 --> 1319.22]  are you thinking more like,
[1319.90 --> 1320.94]  rather than having this mapping
[1320.94 --> 1322.88]  between a declarative thing and a command,
[1323.52 --> 1325.74]  you're thinking just in terms of commands.
[1326.30 --> 1327.58]  So when I hear that,
[1327.64 --> 1329.50]  I'm thinking about the functional paradigm
[1329.50 --> 1331.18]  where you have a function,
[1331.32 --> 1332.62]  there's an input and an output,
[1333.08 --> 1334.64]  and then the focus is on the function,
[1334.90 --> 1335.84]  not on the mappings.
[1336.52 --> 1338.14]  Are you thinking along the same lines
[1338.14 --> 1339.30]  or is there something else?
[1339.30 --> 1340.48]  Kind of.
[1340.48 --> 1344.58]  I mean, a lot of commands really are just,
[1344.72 --> 1345.52]  you're running a function
[1345.52 --> 1347.12]  and you're expecting some output.
[1347.92 --> 1349.96]  I venture like 99% of the time,
[1350.06 --> 1352.10]  that output is either like a file on disk
[1352.10 --> 1354.30]  or something that it wrote to standard out,
[1354.48 --> 1356.36]  maybe a JSON stream or something like that.
[1357.24 --> 1359.12]  So you don't really control
[1359.12 --> 1360.92]  whether the commands are idempotent
[1360.92 --> 1363.90]  or like pure or anything like in a functional sense,
[1363.90 --> 1366.32]  but they do very much feel like a functional interface.
[1366.32 --> 1368.10]  And there are exceptions there
[1368.10 --> 1371.04]  where like some CLIs have like subcommands
[1371.04 --> 1372.80]  and like different like syntax for it,
[1372.82 --> 1374.16]  but it ultimately boils down to like
[1374.16 --> 1375.54]  you're identifying a function call,
[1375.80 --> 1377.02]  passing it parameters,
[1377.20 --> 1378.12]  and it's giving you outputs.
[1378.64 --> 1381.82]  So yeah, I guess I do kind of see command lines
[1381.82 --> 1383.54]  as a very functional interface.
[1383.88 --> 1386.08]  And being able to pass results
[1386.08 --> 1387.20]  from those commands to another,
[1387.34 --> 1389.78]  I think that's really where the special sauce is from base.
[1389.88 --> 1392.48]  Because if you try to just script things
[1392.48 --> 1394.60]  running commands in Bash,
[1394.60 --> 1396.52]  you have to like deal with those files.
[1396.60 --> 1397.54]  You have to put them somewhere,
[1397.74 --> 1398.90]  pass them to this other thing,
[1399.26 --> 1400.00]  clean them up after.
[1400.54 --> 1400.62]  Yeah.
[1400.82 --> 1402.78]  So I'm trying to build something that makes,
[1403.28 --> 1405.02]  I guess something that treats commands like functions
[1405.02 --> 1406.24]  that you can easily use.
[1406.46 --> 1406.56]  Yeah.
[1406.90 --> 1408.16]  Some team members have this joke
[1408.16 --> 1409.74]  on the RabbitMQ team,
[1410.36 --> 1412.46]  which RabbitMQ uses Erlang,
[1412.78 --> 1415.10]  which is a highly, highly functional language.
[1415.96 --> 1418.32]  And the joke was that
[1418.32 --> 1421.44]  if you're an experienced enough programmer,
[1422.22 --> 1423.98]  you're most likely functional programmer.
[1423.98 --> 1427.76]  Like basically it all boils down to function somewhere.
[1427.98 --> 1430.20]  And once you come to accept that,
[1430.58 --> 1432.00]  your world will be better.
[1432.36 --> 1434.24]  Obviously that's not always true.
[1434.30 --> 1437.46]  We had Gary Bernhardt a few episodes back.
[1437.78 --> 1441.08]  And if you haven't heard his faux-o talk,
[1441.14 --> 1441.56]  you should,
[1441.64 --> 1442.64]  because it's a very good one.
[1443.04 --> 1444.86]  This explains why functional is just weird
[1444.86 --> 1447.78]  and why object-oriented has its own shortcomings.
[1447.78 --> 1450.06]  But faux-o is a thing
[1450.06 --> 1451.48]  and I really like it.
[1452.08 --> 1452.52]  Anyways,
[1452.88 --> 1454.70]  we can put a link in the show notes.
[1456.02 --> 1457.90]  So I'm wondering if,
[1458.06 --> 1459.86]  because the base language,
[1460.16 --> 1460.84]  baselang,
[1460.94 --> 1463.78]  B-A-S-S-dash-lang.com,
[1464.40 --> 1464.68]  is it?
[1465.08 --> 1465.40]  Org.
[1465.56 --> 1465.98]  Org.
[1466.04 --> 1466.40]  Thank you.
[1466.48 --> 1466.88]  Org.
[1466.92 --> 1467.76]  I might own .com,
[1467.90 --> 1469.54]  but .org is the canonical one.
[1469.54 --> 1471.80]  So base.lang.org.
[1472.34 --> 1473.52]  It explains,
[1473.64 --> 1473.96]  by the way,
[1474.00 --> 1475.06]  it's a very nice website.
[1475.18 --> 1476.28]  The Groovebox theme,
[1476.60 --> 1477.48]  I love it.
[1477.80 --> 1478.62]  It's actually different.
[1479.00 --> 1479.30]  Okay.
[1479.48 --> 1481.08]  It's different every time you load the page.
[1481.46 --> 1481.82]  Really?
[1482.20 --> 1483.48]  There's like a handful of themes
[1483.48 --> 1484.18]  that it shuffles through.
[1484.94 --> 1487.64]  This is kind of a callback to Conqueror's
[1487.64 --> 1488.32]  because at one point
[1488.32 --> 1490.26]  we were thinking of switching the color scheme.
[1490.38 --> 1491.08]  So we added a,
[1491.48 --> 1492.84]  if you press like a special key,
[1492.84 --> 1494.20]  maybe it was like Alt-S or something,
[1494.32 --> 1496.14]  it would actually bring up a little drop-down
[1496.14 --> 1497.22]  so you could change the theme.
[1497.22 --> 1497.98]  Right.
[1498.16 --> 1500.32]  So I brought that back to base,
[1500.42 --> 1501.42]  but a little more extreme
[1501.42 --> 1502.24]  because it literally changes
[1502.24 --> 1503.18]  every time you load the page.
[1503.48 --> 1504.56]  But you can change it if you want
[1504.56 --> 1505.26]  at the bottom.
[1505.30 --> 1505.56]  Really?
[1505.70 --> 1506.82]  I don't think it changed.
[1507.06 --> 1508.54]  Mine has stayed the same
[1508.54 --> 1509.58]  ever since.
[1509.84 --> 1510.70]  Scroll all the way down.
[1511.28 --> 1512.44]  Do you have a reset button there?
[1512.98 --> 1513.38]  Reset?
[1513.80 --> 1514.80]  I do have a reset button.
[1515.12 --> 1517.06]  You probably pinned it to a theme at some point.
[1517.34 --> 1518.36]  Ah, so I picked it.
[1518.52 --> 1519.24]  See, I picked it.
[1519.30 --> 1519.56]  All right.
[1519.56 --> 1519.72]  Okay.
[1519.72 --> 1520.60]  Let me reset that.
[1520.74 --> 1520.88]  Okay.
[1520.98 --> 1522.24]  Oh, I see it now.
[1522.52 --> 1522.78]  Okay.
[1522.82 --> 1523.52]  Now when I reload,
[1523.64 --> 1524.04]  I see it.
[1524.08 --> 1524.16]  Yeah.
[1524.22 --> 1524.34]  Okay.
[1524.44 --> 1524.62]  Yeah.
[1524.62 --> 1525.80]  So I chose Groovebox.
[1525.88 --> 1525.98]  See?
[1526.14 --> 1526.30]  Okay.
[1526.44 --> 1527.08]  It was for me.
[1527.36 --> 1527.88]  All right.
[1527.88 --> 1528.64]  That's really cool.
[1529.02 --> 1530.16]  So every page is different,
[1530.34 --> 1531.42]  like differently colored.
[1531.96 --> 1532.64]  Every page load.
[1532.70 --> 1533.66]  That's really neat.
[1533.92 --> 1534.24]  Okay.
[1534.62 --> 1535.16]  Very nice.
[1535.38 --> 1537.26]  My favorite is Rose Pine.
[1538.08 --> 1538.48]  Rose Pine.
[1538.50 --> 1539.78]  Shout out to Rose Pine, I guess.
[1539.94 --> 1540.64]  Let's check it out.
[1540.74 --> 1540.94]  Hang on.
[1540.96 --> 1541.54]  It's very nice,
[1541.60 --> 1543.66]  like luxurious looking color scheme.
[1544.26 --> 1546.20]  Rose Pine Dawn Moon
[1546.20 --> 1547.06]  or the classic?
[1547.22 --> 1547.78]  Just regular.
[1547.90 --> 1548.66]  The regular Rose Pine.
[1548.66 --> 1549.44]  They're all good too,
[1549.56 --> 1551.30]  but like Dawn is the light mode.
[1551.92 --> 1552.48]  I see.
[1553.20 --> 1553.64]  Interesting.
[1553.88 --> 1554.58]  Rose Pine Dawn.
[1554.68 --> 1554.86]  Okay.
[1555.38 --> 1555.56]  Yeah.
[1555.56 --> 1556.18]  Go check it out.
[1556.18 --> 1556.84]  Oh yes.
[1556.84 --> 1557.30]  Rose Pine.
[1557.38 --> 1558.12]  That's like the dawn.
[1558.22 --> 1559.12]  That's like the light one.
[1559.54 --> 1560.64]  And the moon is a dark one.
[1561.26 --> 1561.94]  Very nice.
[1562.14 --> 1562.36]  Okay.
[1562.76 --> 1564.62]  So you have like all these concepts.
[1564.72 --> 1565.84]  You have like the basics.
[1566.48 --> 1566.70]  Yeah.
[1566.70 --> 1568.24]  And I love that.
[1568.28 --> 1569.12]  It's not a typo.
[1569.12 --> 1570.58]  There are double S's.
[1571.10 --> 1572.00]  The basics.
[1572.76 --> 1573.50]  Is the thunk,
[1573.56 --> 1574.60]  I'm looking for a thunk.
[1575.20 --> 1580.52]  Is that what would the function equivalent be in base?
[1581.24 --> 1582.44]  Thunks are,
[1582.66 --> 1583.82]  they're named that way
[1583.82 --> 1587.18]  because they kind of mirror zero arity function calls,
[1587.54 --> 1589.02]  but they represent commands.
[1589.02 --> 1589.68]  So that's,
[1589.68 --> 1590.64]  that's the distinction.
[1590.64 --> 1593.30]  Base is a functional language,
[1593.30 --> 1598.44]  but it represents commands as like a lazily evaluated data structure called a thunk.
[1598.80 --> 1602.44]  And it's also just called thunk because it sounds funny and semi musical.
[1603.26 --> 1603.28]  So.
[1603.42 --> 1603.56]  Yeah.
[1604.18 --> 1604.58]  Okay.
[1604.58 --> 1608.10]  Where does a space invaders thing come from?
[1608.18 --> 1609.78]  Because that's another thing which I noticed.
[1610.04 --> 1611.02]  That's a good one.
[1611.52 --> 1612.42]  That's a good question.
[1612.58 --> 1612.90]  Honestly,
[1612.96 --> 1614.62]  I don't know why I picked space invaders.
[1614.72 --> 1615.44]  I wanted something.
[1615.98 --> 1619.48]  There's a pattern in the docs where like sometimes it'll show a thunk
[1619.48 --> 1621.50]  and then show it again in another context.
[1621.50 --> 1624.20]  So I wanted it to be easy to recognize that they're actually the same.
[1624.86 --> 1629.44]  So it was either like gravatar or build like a space invaders thing.
[1629.48 --> 1631.20]  And I thought the space invaders would be more fun
[1631.20 --> 1634.26]  because I wanted a way to tie the colors to the color scheme
[1634.26 --> 1634.68]  too.
[1634.86 --> 1635.06]  Yeah.
[1635.06 --> 1637.06]  So that way I can control the whole stack.
[1637.44 --> 1638.20]  That makes sense.
[1638.52 --> 1641.30]  I'm just looking at the image now and I can see the three echoes,
[1641.30 --> 1644.18]  which have a space invader that looks the same.
[1644.56 --> 1646.56]  And it just shows it's actually the same command,
[1646.64 --> 1646.82]  right?
[1647.00 --> 1648.28]  That's what that's representing.
[1648.94 --> 1649.12]  Yeah.
[1649.12 --> 1650.06]  And if you click it,
[1650.10 --> 1652.24]  it'll show the actual attributes of the command.
[1652.84 --> 1652.98]  Oh,
[1653.08 --> 1653.44]  wow.
[1653.74 --> 1654.42]  That's amazing.
[1654.56 --> 1655.42]  You have to check it out.
[1655.52 --> 1656.26]  Like as a listener,
[1656.52 --> 1660.80]  it's okay to put on pause and to go and check baseline.org because this is a
[1660.80 --> 1661.82]  really nice website.
[1661.82 --> 1665.78]  I can't believe that you do this for fun in your free time.
[1665.78 --> 1667.92]  Like you must really love CICD,
[1668.42 --> 1669.12]  functional,
[1669.40 --> 1670.98]  the whole functional paradigm.
[1672.12 --> 1674.00]  And there's just problem space.
[1674.10 --> 1674.66]  Why is that?
[1674.78 --> 1676.32]  Why do you like it so much?
[1676.32 --> 1677.28]  Um,
[1677.36 --> 1680.12]  I think it's more broad than CICD.
[1680.54 --> 1680.98]  Um,
[1681.06 --> 1682.92]  I just like the experience,
[1683.04 --> 1684.18]  like the whole process,
[1684.18 --> 1686.90]  I think from building and publishing software,
[1686.90 --> 1689.42]  there's another side project,
[1689.42 --> 1690.66]  which I've been like putting out there,
[1690.72 --> 1693.40]  but really no one cares because it's just yet another static site engine,
[1693.40 --> 1695.12]  but this site is built in booklet,
[1695.48 --> 1697.10]  which also has its own,
[1697.32 --> 1699.76]  I think it's like booklet.page.
[1700.46 --> 1700.90]  Okay.
[1700.92 --> 1703.12]  And you can really tell I built both of them because they look like the
[1703.12 --> 1703.34]  same.
[1703.34 --> 1703.50]  Um,
[1703.50 --> 1704.66]  yes,
[1704.66 --> 1705.70]  I can see it.
[1706.12 --> 1706.48]  Okay.
[1706.64 --> 1707.98]  I can see the same structure.
[1708.16 --> 1708.98]  That's really cool.
[1709.64 --> 1710.72]  So I,
[1710.82 --> 1715.76]  I can see a lot of like a Lisp like structure here and Lisp like structures.
[1715.94 --> 1716.80]  That's true too.
[1717.02 --> 1717.54]  In booklet,
[1717.62 --> 1717.80]  you mean?
[1718.00 --> 1718.18]  Yeah.
[1718.66 --> 1719.44]  Why Lisp?
[1719.44 --> 1720.26]  I just,
[1720.42 --> 1726.14]  so I think the fundamental appeal of Lisp to me is being able to do a lot with a little
[1726.14 --> 1727.80]  languages.
[1728.56 --> 1731.46]  Maybe that's even the part of the appeal of go to me too,
[1731.46 --> 1732.32]  because go is,
[1732.44 --> 1733.96]  it's a pretty small language.
[1734.28 --> 1734.52]  Um,
[1734.52 --> 1736.02]  it also is like kind of in that mindset.
[1736.18 --> 1739.38]  I'll probably offend a lot of people saying like Lisp and go are similar to each other,
[1739.38 --> 1739.68]  but,
[1739.80 --> 1740.74]  uh,
[1740.74 --> 1743.38]  I think fundamentally it's the same thing that attracts me to both,
[1743.38 --> 1750.36]  but especially Lisp because like a long time ago before I actually got into like professional
[1750.36 --> 1751.14]  software engineering,
[1751.14 --> 1752.58]  I was just learning a lot of languages.
[1752.58 --> 1754.06]  I've always just really been into languages.
[1754.06 --> 1756.56]  And I especially liked ones where it's like,
[1756.56 --> 1760.06]  you start with these five primitives and from there on you can build anything out there.
[1760.06 --> 1760.94]  It's like Turing complete.
[1761.74 --> 1762.50]  So that's,
[1762.54 --> 1763.68]  that's what brought me to like scheme.
[1764.14 --> 1767.62]  Racket was also a lot of fun because it was all about building languages on top of
[1767.62 --> 1767.96]  Racket.
[1768.08 --> 1771.76]  And I think like the world needs a lot more of these like tiny domain specific languages
[1771.76 --> 1773.36]  that try to like focus on one thing.
[1773.48 --> 1776.50]  And Racket tried to be like the platform for building those languages.
[1777.80 --> 1782.68]  But there's actually kind of interesting story behind the specific flavor of Lisp.
[1782.68 --> 1784.32]  That's behind base.
[1784.74 --> 1785.10]  Um,
[1785.40 --> 1785.70]  okay.
[1785.92 --> 1786.30]  It's,
[1786.38 --> 1789.22]  it's actually based on a kind of lesser known one called kernel.
[1790.02 --> 1791.36]  Kernel's whole thing was,
[1791.94 --> 1792.12]  you know,
[1792.20 --> 1792.76]  scheme was,
[1792.76 --> 1793.30]  uh,
[1793.30 --> 1794.26]  six subtractions.
[1795.08 --> 1795.40]  Um,
[1795.40 --> 1798.26]  kernel is five because it took one and made it more generic.
[1798.42 --> 1798.80]  Right.
[1799.06 --> 1799.92]  So you know how like Lisp,
[1800.18 --> 1801.52]  they're known for having macros,
[1801.72 --> 1801.96]  right?
[1802.02 --> 1803.18]  Like compile time,
[1803.26 --> 1803.88]  macro expansion.
[1804.46 --> 1804.94]  Kernel,
[1805.18 --> 1805.54]  uh,
[1805.54 --> 1806.50]  instead of having macros,
[1806.54 --> 1807.82]  it had something called an operative,
[1808.34 --> 1811.58]  which is something that deferred the evaluation of its arguments.
[1811.58 --> 1813.54]  So when you called an operative,
[1813.64 --> 1816.44]  you would get the unevaluated forms and the color's scope,
[1816.48 --> 1818.96]  and then you could selectively evaluate them in the color's scope.
[1819.70 --> 1819.90]  Um,
[1819.90 --> 1821.78]  I think IO actually is kind of similar to this.
[1822.44 --> 1823.26]  So yeah,
[1823.28 --> 1824.00]  a long time ago,
[1824.14 --> 1825.48]  I tried implementing that.
[1825.64 --> 1828.08]  I implemented one in Haskell.
[1828.34 --> 1829.36]  It's called Hummus.
[1829.94 --> 1832.94]  Implemented one in our Python called Pumis.
[1832.94 --> 1835.86]  And one in my own language called Cletus.
[1836.28 --> 1837.52]  Guess which one was the fastest?
[1838.56 --> 1839.98]  Your own language?
[1840.12 --> 1840.80]  No way.
[1841.48 --> 1843.10]  Your own language is the fastest one.
[1844.00 --> 1844.24]  No.
[1844.66 --> 1844.98]  No?
[1846.72 --> 1847.92]  Wrong answers only.
[1847.98 --> 1848.52]  It was Python.
[1848.66 --> 1848.98]  Python.
[1849.04 --> 1849.68]  Python actually.
[1850.04 --> 1850.16]  Yeah.
[1850.28 --> 1851.92]  Because it was specifically our Python.
[1852.28 --> 1853.72]  So PyPy would compile it to C,
[1853.90 --> 1856.48]  and then it just like blew out the other implementations out of the water.
[1857.28 --> 1857.48]  So yeah,
[1857.54 --> 1859.66]  I did these like a long time ago,
[1859.70 --> 1860.64]  probably like 2010.
[1861.34 --> 1866.62]  And then right about the time I was leaving VMware and looking to start on base,
[1866.80 --> 1868.50]  someone actually approached me and said,
[1868.62 --> 1868.84]  um,
[1869.20 --> 1869.32]  Hey,
[1869.32 --> 1875.56]  we're trying to collect all the implementations or details for kernel because the guy that invented it just passed away.
[1875.66 --> 1876.02]  Wow.
[1876.10 --> 1876.42]  I was like,
[1876.66 --> 1876.82]  damn,
[1876.86 --> 1878.32]  I'd never talked to this guy.
[1878.40 --> 1879.72]  Now I feel kind of bad because like,
[1879.72 --> 1882.46]  I feel like I kind of carried the torch a bit with base,
[1882.58 --> 1884.54]  but there's nothing I can do to like,
[1884.58 --> 1884.80]  you know,
[1884.80 --> 1885.78]  make him aware of that.
[1885.78 --> 1886.46]  Uh,
[1886.86 --> 1887.06]  but yeah,
[1887.06 --> 1888.22]  he was a really cool dude.
[1888.40 --> 1888.64]  Uh,
[1888.64 --> 1889.14]  John shut.
[1889.50 --> 1890.74]  I'm just saying really cool.
[1890.80 --> 1891.30]  I don't know him.
[1891.42 --> 1892.32]  He's probably really cool.
[1892.54 --> 1894.38]  Really contributed to wiki news a lot.
[1894.60 --> 1894.92]  Okay.
[1895.22 --> 1895.40]  Well,
[1895.42 --> 1899.90]  if anyone knows John shot or anyone knows like this is a shout out to him.
[1900.30 --> 1902.52]  And if you know anyone that worked with him,
[1902.88 --> 1903.92]  that's amazing.
[1904.18 --> 1904.38]  Yeah.
[1904.38 --> 1910.66]  Just like let them know that the memory and his ideas live on in base.
[1911.22 --> 1911.66]  Wow.
[1912.10 --> 1913.26]  That's a great story.
[1913.84 --> 1914.66]  Very interesting.
[1914.66 --> 1915.96]  But the,
[1915.96 --> 1918.82]  the trouble with kernel was it's hard to optimize because there's literally a
[1918.82 --> 1920.44]  eval after every corner.
[1920.84 --> 1921.04]  Um,
[1921.10 --> 1921.34]  okay.
[1921.70 --> 1924.84]  But that doesn't matter in a language like base because the bottleneck is
[1924.84 --> 1926.84]  going to be like running containers.
[1926.84 --> 1928.16]  Like the runtime interpreters,
[1928.26 --> 1929.58]  probably not going to be slower than that.
[1940.18 --> 1940.92]  Hey friends,
[1940.92 --> 1945.08]  this episode is brought to you by century and their upcoming developer experience conference
[1945.08 --> 1945.84]  called decks.
[1945.84 --> 1947.10]  Sort the madness.
[1947.52 --> 1949.76]  Deploying new code can be a lot like making a really great sandwich,
[1950.08 --> 1952.42]  taking a bite and having all the contents fall out.
[1952.78 --> 1953.34]  It's exciting.
[1953.74 --> 1954.26]  It's chaotic.
[1954.26 --> 1955.52]  And it's maddening.
[1955.52 --> 1956.62]  If you know the feeling,
[1956.72 --> 1959.46]  then decks by a century might just be for you.
[1959.86 --> 1962.76]  This is a free conference by developers for developers.
[1962.76 --> 1966.50]  We'll sort through the madness and look for ways to improve workflow productivity.
[1967.00 --> 1971.84]  Join century for this event in San Francisco or virtually on September 28th and discover
[1971.84 --> 1973.96]  new ways to make your life a little easier.
[1973.96 --> 1979.60]  Save your seat now for this event at bit.ly slash decks 2022.
[1980.16 --> 1980.58]  Again,
[1980.70 --> 1983.44]  bit.ly slash decks 2022.
[1983.94 --> 1985.68]  This link is in the show notes.
[2003.96 --> 2007.64]  One of the base components is this,
[2007.80 --> 2008.52]  as you mentioned,
[2008.68 --> 2010.12]  the runtime compiler.
[2010.52 --> 2011.62]  Is that what you've said?
[2011.88 --> 2012.40]  Runtime.
[2012.84 --> 2013.20]  Well,
[2013.24 --> 2013.84]  there's runtimes.
[2013.96 --> 2014.52]  There's no compiler.
[2014.98 --> 2015.26]  All right.
[2015.32 --> 2015.48]  Sorry.
[2015.80 --> 2016.00]  Okay.
[2016.04 --> 2022.36]  How do you call basically the language in which you code the base?
[2022.72 --> 2023.76]  What is that component?
[2023.86 --> 2024.32]  So there's like,
[2024.32 --> 2025.00]  like the runtime,
[2025.18 --> 2026.08]  which actually runs it.
[2026.08 --> 2029.52]  And this is the front end of it.
[2029.74 --> 2032.50]  I'm just trying to find a name for it that describes it.
[2032.60 --> 2033.08]  What it is.
[2033.08 --> 2033.98]  The interpreter.
[2034.36 --> 2034.90]  The interpreter.
[2035.08 --> 2035.20]  Yes.
[2035.20 --> 2036.00]  Of the language itself.
[2036.28 --> 2036.52]  Yes.
[2036.62 --> 2037.02]  Yes.
[2037.06 --> 2037.44]  The interpreter.
[2037.68 --> 2037.88]  Okay.
[2038.46 --> 2040.16]  What is the runtime of base?
[2040.90 --> 2044.80]  So it gets just parsed into a syntax tree of like at that point,
[2044.82 --> 2045.58]  it's just forms,
[2045.76 --> 2046.02]  you know,
[2046.04 --> 2046.78]  as with Lisp,
[2046.82 --> 2049.02]  there's no difference between like a form and a value.
[2049.08 --> 2050.80]  It's just whether it's been evaluated or not.
[2050.98 --> 2053.14]  So that gets fed into go.
[2053.14 --> 2056.10]  It walks over each of the forms and calls a vowel on them.
[2056.42 --> 2059.92]  The tricky thing is everything is implemented in continuation passing style,
[2059.92 --> 2064.24]  which is a way of implementing tail recursion,
[2064.86 --> 2065.24]  essentially.
[2065.64 --> 2066.08]  Okay.
[2066.14 --> 2070.78]  So languages that are implemented on like a non tail call optimizing platform,
[2070.96 --> 2073.52]  usually do that because otherwise there's no way to do infinite loops.
[2073.92 --> 2074.44]  Right.
[2074.48 --> 2078.20]  Which would be bad for a continuous system because its point is to be an infinite
[2078.20 --> 2078.48]  loop.
[2078.48 --> 2080.66]  So if I didn't have like continuation passing style,
[2080.78 --> 2086.22]  then probably eventually base servers would die if anyone was using it for CICD.
[2086.84 --> 2087.16]  Yeah.
[2087.20 --> 2087.88]  That's a good one.
[2088.52 --> 2092.56]  I'm pretty sure that Erlang is optimized for that because it just like,
[2092.66 --> 2097.48]  it has to be able to deal with like infinite loops and yeah,
[2097.52 --> 2097.94]  it's optimized.
[2098.06 --> 2098.26]  Okay.
[2098.38 --> 2098.62]  Okay.
[2098.62 --> 2098.96]  So yeah,
[2098.96 --> 2099.72]  that makes sense.
[2100.14 --> 2101.76]  And the less comprehensions and all that,
[2101.80 --> 2103.62]  it can just keep recursing and you know,
[2103.64 --> 2105.98]  you won't blow any memory or any stack or anything like that.
[2106.22 --> 2106.50]  Okay.
[2106.50 --> 2109.58]  So where does all this code run?
[2110.20 --> 2112.42]  Like where do all those instructions run?
[2112.86 --> 2116.42]  And I'm trying to get to the build kit part because I know like looking at base
[2116.42 --> 2117.00]  that that's,
[2117.08 --> 2117.68]  that's the runtime,
[2117.98 --> 2119.86]  but where does that run?
[2120.00 --> 2120.84]  How does like,
[2120.94 --> 2127.68]  how does the interfacing happen and how does something useful get produced in
[2127.68 --> 2132.18]  base as a container or a file or whatever the case may be a binary?
[2133.12 --> 2133.56]  Well,
[2133.64 --> 2136.48]  the language runs in the same way that like Ruby or Python or N,
[2136.50 --> 2138.28]  any other interpreted language does.
[2138.96 --> 2141.32]  So that's one huge difference actually.
[2141.52 --> 2143.26]  And case hasn't been made clear yet,
[2143.28 --> 2147.00]  I guess it's like between concourse and base concourse is like a service that you
[2147.00 --> 2151.22]  deploy and you like point it to a database and it maintains all this stay and
[2151.22 --> 2152.02]  you feed it YAML.
[2152.20 --> 2154.72]  And like YAML is like the language that you're writing base.
[2154.86 --> 2155.50]  There's no server.
[2155.50 --> 2158.02]  It's just a language interpreter.
[2158.02 --> 2159.34]  So you just run base files.
[2159.48 --> 2161.20]  If you want to run a CICD server,
[2161.30 --> 2162.22]  you're just running a base file.
[2162.32 --> 2162.78]  That's a loop.
[2163.40 --> 2165.08]  So that's the key difference.
[2165.26 --> 2167.94]  But when it comes to build kit,
[2168.06 --> 2172.62]  that's where it actually just talks to build kit over the regular like GRPC interface that
[2172.62 --> 2173.10]  exposes.
[2173.10 --> 2175.60]  So that could be local or remote.
[2175.92 --> 2176.40]  Yeah.
[2176.46 --> 2178.96]  I think I've only really tested it locally,
[2178.96 --> 2180.66]  but in principle,
[2180.66 --> 2182.06]  it's just like calling over the API.
[2182.26 --> 2185.00]  And I think the client already handles like uploading files.
[2185.40 --> 2187.88]  So I think it would work remotely,
[2188.22 --> 2189.38]  but I haven't tried yet.
[2189.88 --> 2190.04]  Yeah.
[2190.40 --> 2193.16]  I also know there's like the base loop component.
[2194.16 --> 2194.52]  What is,
[2194.64 --> 2195.44]  what is the base loop?
[2196.00 --> 2201.72]  So base itself isn't really a CI thing any more than like Ruby or Python is.
[2202.02 --> 2204.14]  So base loop is basically the CI thing.
[2204.38 --> 2207.42]  I had been just running base in GitHub actions,
[2207.66 --> 2211.78]  but it was just very slow because you don't control the environment.
[2212.08 --> 2212.54]  Like,
[2212.60 --> 2212.80]  you know,
[2212.80 --> 2216.10]  I'm developing base on like a RX 4950,
[2216.28 --> 2217.16]  like whatever I've,
[2217.30 --> 2218.46]  I probably butchered the name,
[2218.52 --> 2221.84]  but like whatever the really nice AMD CPU is,
[2221.84 --> 2224.32]  but then it's like running on some co-located server,
[2224.58 --> 2226.00]  probably in GitHub actions.
[2226.40 --> 2230.36]  It's not able to use build kit efficiently because it's a new run.
[2230.44 --> 2231.88]  Every time you could use caching,
[2232.04 --> 2234.90]  but then you're trading like CPU time for just IO time,
[2234.98 --> 2235.76]  managing the caches.
[2236.24 --> 2241.50]  So what I wanted to do with base loop is have a server that I just run that
[2241.50 --> 2242.62]  receives GitHub web hooks,
[2242.84 --> 2245.42]  and then you bring a runner to it.
[2245.50 --> 2247.68]  So it doesn't have its own dedicated CI stack.
[2248.44 --> 2250.24]  And it's basically web hooks come in.
[2250.24 --> 2254.50]  It evaluates base code in response by like calling out to your repo.
[2255.12 --> 2256.44]  And where does the runner run?
[2256.94 --> 2259.16]  And what is the runner in this case?
[2259.60 --> 2263.04]  The runner is someone running base dash dash runner,
[2263.26 --> 2265.16]  and then github.baselang.org.
[2265.36 --> 2267.20]  What that essentially does is,
[2267.58 --> 2270.24]  if anyone's familiar with how concourse workers ran,
[2270.48 --> 2274.84]  it's very similar where concourse had like a SSH gateway called the TSA.
[2274.84 --> 2276.20]  You connect to it,
[2276.26 --> 2277.88]  it would forward some connections.
[2278.36 --> 2280.86]  And then when the ATC needed to use that worker,
[2281.44 --> 2284.90]  it would actually talk to a local forwarded address through SSH.
[2285.36 --> 2285.38]  Okay.
[2285.62 --> 2287.82]  So base runner is doing basically the same thing,
[2287.90 --> 2291.58]  where it exposes the local runtimes as a gRPC service.
[2291.84 --> 2295.10]  So then when a web hook comes into base loop,
[2295.44 --> 2297.82]  it connects to the forwarded address and then uses that runner.
[2297.82 --> 2301.68]  So that way I can actually use my like AMD massive developer machine
[2301.68 --> 2302.82]  instead of being, you know,
[2303.42 --> 2306.20]  stuck with whatever the free tier is on GitHub Actions.
[2306.82 --> 2307.30]  Interesting.
[2307.84 --> 2310.18]  What about registering your own GitHub runner?
[2310.34 --> 2311.28]  Have you considered that?
[2311.84 --> 2313.40]  I don't know what those words mean.
[2314.82 --> 2315.30]  Okay.
[2315.86 --> 2317.90]  So, you know, like you get like the free GitHub runner,
[2318.40 --> 2321.94]  just by default, but then you can run your own.
[2322.28 --> 2323.32]  And you can, you know,
[2323.32 --> 2327.34]  either have like a VM like process that registers with GitHub
[2327.34 --> 2330.02]  and then the runner is available to pick up jobs.
[2330.28 --> 2330.54]  Gotcha.
[2330.70 --> 2331.80]  Or, and I've seen,
[2331.92 --> 2333.28]  I've seen this as being more recommended
[2333.28 --> 2336.24]  because of the ephemeral state of GitHub runners.
[2336.36 --> 2338.28]  They're supposed to be like cleaned
[2338.28 --> 2340.30]  and like brand new on every single run.
[2340.50 --> 2343.98]  You can run a controller in Kubernetes
[2343.98 --> 2347.78]  and then the runners are like registered on demand
[2347.78 --> 2349.96]  based on what jobs are available.
[2350.28 --> 2352.42]  And that like scales a bit nicer
[2352.42 --> 2354.22]  and you get like containers, you get like,
[2354.58 --> 2357.42]  but again, you should be able to trust your infrastructure
[2357.42 --> 2359.88]  or, I mean, it's a tough problem.
[2360.14 --> 2361.78]  Like running this is a tough problem.
[2362.10 --> 2365.74]  And that's why the majority will just use the free tiers.
[2366.34 --> 2368.72]  Well, I mean, it sounds pretty similar.
[2368.80 --> 2369.84]  It sounds like something I could do,
[2369.90 --> 2371.36]  but I guess the other goal,
[2371.48 --> 2373.08]  which I didn't mention is escaping YAML.
[2374.00 --> 2375.50]  Yes, that's a good one.
[2375.68 --> 2377.20]  That's a worthy goal.
[2377.36 --> 2378.62]  If I'm using GitHub Actions,
[2378.80 --> 2380.14]  then I'm back to YAML.
[2380.28 --> 2380.80]  Oh, yes.
[2380.80 --> 2383.80]  Back to those like wrappers managed by,
[2383.88 --> 2386.46]  you know, random people doing their best,
[2386.68 --> 2388.70]  but still just a lot of dependencies to manage.
[2389.22 --> 2390.66]  Don't you miss the GitHub marketplace
[2390.66 --> 2394.42]  with all the actions that you could use from there?
[2394.80 --> 2397.72]  Not really, because like most things that I use,
[2397.80 --> 2398.78]  including GitHub itself,
[2399.02 --> 2401.18]  they already ship a CLI.
[2401.18 --> 2403.86]  So to ship base, for example,
[2403.86 --> 2406.88]  I just run, you know, ghrelease create or whatever,
[2407.06 --> 2408.06]  but as a base thunk.
[2408.60 --> 2408.80]  Yeah.
[2408.82 --> 2410.78]  I mean, that kind of gets back to what I was talking about
[2410.78 --> 2412.82]  with all the like declarative wrappers is
[2412.82 --> 2416.16]  if you avoid that and have your abstraction level be lower,
[2416.16 --> 2418.94]  then you automatically get like the entire marketplace,
[2418.94 --> 2421.18]  which is being built by everyone.
[2421.64 --> 2421.74]  Yeah.
[2421.74 --> 2424.98]  So you do have this file,
[2425.12 --> 2427.02]  which made me spell when I've noticed it.
[2427.32 --> 2430.08]  It is a base file and it's called a ship it file.
[2430.92 --> 2431.06]  Yeah.
[2431.56 --> 2433.16]  What does the ship it file do?
[2434.40 --> 2435.20]  It ships it.
[2435.20 --> 2438.80]  So the gist of it is it builds a binary
[2438.80 --> 2440.64]  for each supported platform.
[2440.78 --> 2444.92]  So Linux, Darwin, Windows, ARM for Darwin as well.
[2445.06 --> 2448.38]  And then just passes that to ghrelease create,
[2449.08 --> 2452.42]  which all those words I said about declarative wrappers,
[2452.42 --> 2455.28]  I actually wrote a wrapper myself for gh.
[2455.58 --> 2456.58]  So maybe it's just,
[2456.68 --> 2458.90]  I like functional wrappers more than declarative ones,
[2459.04 --> 2463.28]  but yeah, it's just a small script that takes the,
[2463.28 --> 2466.30]  it reuses the functions for building base
[2466.30 --> 2470.38]  and just passes the result into the ghrelease create command.
[2470.72 --> 2472.42]  But the nifty thing it also does
[2472.42 --> 2475.50]  is it takes the data representation of those thunks,
[2475.90 --> 2477.08]  like the JSON format,
[2477.30 --> 2479.30]  and publishes those to the release as well.
[2479.90 --> 2482.70]  And then it publishes like SHA-256 of each file.
[2482.98 --> 2485.10]  So kind of the neat thing
[2485.10 --> 2486.36]  that I want to be able to do with the base
[2486.36 --> 2488.96]  is like not only have it so you can build up those thunks
[2488.96 --> 2490.86]  and have them get like bigger and bigger and bigger
[2490.86 --> 2492.86]  as you pass like more results between them,
[2493.28 --> 2495.38]  but you can actually just snapshot them.
[2495.94 --> 2497.78]  And assuming those thunks are hermetic,
[2497.86 --> 2500.82]  then you have a reproducible build that you can publish.
[2502.04 --> 2502.58]  Interesting.
[2502.74 --> 2507.80]  So let's say hermetic mean something that is the same,
[2508.56 --> 2511.14]  something that it's like idempotent.
[2511.64 --> 2514.74]  It accounts for every input that might change its result
[2514.74 --> 2516.70]  is kind of how I sum it up.
[2516.96 --> 2519.64]  So if you have like a hermetic data structure
[2519.64 --> 2521.80]  and you run it like today and you run it tomorrow
[2521.80 --> 2525.28]  or assuming the inputs are still available, granted.
[2525.70 --> 2527.48]  But the point is, yeah, you should get the same result
[2527.48 --> 2528.46]  no matter where you run it,
[2528.80 --> 2530.70]  which is kind of a fundamental building block,
[2530.76 --> 2531.76]  I think, for CICD.
[2532.14 --> 2534.26]  It was something Concourse tried to enforce.
[2535.10 --> 2537.56]  But I think that's also where a lot of people
[2537.56 --> 2538.80]  ran into pain with it,
[2538.80 --> 2540.80]  was Concourse being a little too overbearing.
[2540.80 --> 2542.86]  No, I think that's really important,
[2543.00 --> 2545.24]  especially like supply chain security
[2545.24 --> 2547.52]  is more and more in our minds.
[2548.18 --> 2550.14]  And for that, you need to have this property.
[2550.26 --> 2553.60]  Without this property, it's very difficult to achieve that.
[2554.34 --> 2556.98]  I mean, you should be able to like to build the same thing,
[2557.06 --> 2559.16]  compare it bit for bit and make sure,
[2559.66 --> 2562.62]  again, given these inputs, this is the output.
[2563.32 --> 2565.30]  And if you can trust the inputs
[2565.30 --> 2566.60]  and you can verify the inputs
[2566.60 --> 2568.60]  and you can again access the same inputs,
[2568.60 --> 2570.48]  the output should be identical.
[2570.94 --> 2573.14]  And if it's not identical, you have a problem somewhere.
[2573.78 --> 2574.92]  I mean, you also have to trust the thing
[2574.92 --> 2576.60]  that's building it, I guess, but...
[2576.60 --> 2577.82]  Yes, for sure.
[2578.54 --> 2579.60]  But the thing that's building it,
[2579.66 --> 2582.90]  I mean, I suppose it can be the same,
[2583.06 --> 2587.76]  like if the same builder runs in multiple locations
[2587.76 --> 2590.68]  and it uses the same inputs,
[2591.34 --> 2593.40]  so it doesn't matter where the builder runs,
[2593.56 --> 2595.74]  the output should be the same, right?
[2595.78 --> 2598.08]  Because it's the whole, like, there's no state.
[2598.60 --> 2601.42]  The builder has, not even time,
[2601.88 --> 2604.48]  that makes it, you know, like if you have time drift,
[2604.60 --> 2606.66]  like milliseconds, micros, anything like that,
[2606.70 --> 2610.02]  it will not have any impact on the final artifact.
[2610.76 --> 2611.66]  And that's super important
[2611.66 --> 2613.24]  because it can compare two things,
[2613.32 --> 2614.42]  you know, run remotely
[2614.42 --> 2617.60]  and even like completely different architectures,
[2618.18 --> 2619.90]  but the end result should be always the same.
[2620.24 --> 2622.74]  It's a nice way of verifying it, I suppose, as well.
[2622.74 --> 2624.64]  So it's funny you mentioned time
[2624.64 --> 2626.16]  because that was one of the things
[2626.16 --> 2628.18]  that broke the initial builds of base
[2628.18 --> 2630.70]  was that when you archive something up,
[2630.76 --> 2632.26]  it has timestamps in it, right?
[2632.40 --> 2632.62]  Yep.
[2632.78 --> 2635.82]  So if you tried to download those JSON files
[2635.82 --> 2637.76]  and rebuild base back in the day,
[2637.96 --> 2639.44]  it wouldn't produce the same thing
[2639.44 --> 2641.50]  because the archive had different timestamps in it.
[2641.74 --> 2643.74]  So now what base does
[2643.74 --> 2646.68]  is it actually normalizes all the timestamps.
[2646.68 --> 2649.74]  So when you have a thunk build something
[2649.74 --> 2651.52]  and then you pass that result to another thunk,
[2651.98 --> 2654.40]  it'll actually see the timestamps as 1985.
[2655.10 --> 2655.48]  Okay.
[2655.66 --> 2657.42]  Some specific date.
[2657.62 --> 2658.84]  It's not your birthday, is it?
[2659.36 --> 2659.60]  No.
[2659.90 --> 2660.34]  No, good.
[2660.90 --> 2664.34]  I stole this from the Node community, I think.
[2664.52 --> 2664.96]  There's like a,
[2665.38 --> 2668.18]  it's the exact timestamp from Back to the Future.
[2669.02 --> 2671.56]  And I figured might as well make it a standard
[2671.56 --> 2673.40]  because either one's going to be arbitrary.
[2673.86 --> 2675.14]  That's an amazing reference.
[2675.14 --> 2675.50]  Okay.
[2675.62 --> 2677.08]  So that's part of base too.
[2677.52 --> 2679.54]  Space Invaders, Back to the Future.
[2679.82 --> 2681.04]  What else is part of base?
[2681.36 --> 2683.02]  This sounds like a very interesting project.
[2684.66 --> 2687.30]  So actually I was prepared to ship
[2687.30 --> 2689.48]  the next version of base on ship it,
[2689.64 --> 2692.86]  but I'm terrified of running this command on my machine
[2692.86 --> 2694.60]  while doing a screencast
[2694.60 --> 2697.56]  because I'm using my partner's like old MacBook.
[2698.16 --> 2700.12]  But it has a very important feature,
[2700.52 --> 2701.76]  which I call the rave mode,
[2702.00 --> 2703.90]  where if you press R,
[2703.90 --> 2706.76]  there's a little spinner by where it says playing.
[2708.14 --> 2709.68]  Actually, I can link you to the pull request
[2709.68 --> 2711.40]  that adds it because it has a pretty good GIF.
[2711.58 --> 2712.06]  Yes, please.
[2712.46 --> 2713.60]  That sounds amazing.
[2713.74 --> 2714.04]  No, wait.
[2714.16 --> 2714.58]  So hang on.
[2714.64 --> 2717.18]  You're trying to ship a new version of base on ship it?
[2717.38 --> 2718.60]  Is that what's happening right now?
[2718.76 --> 2719.32]  That was the plan.
[2719.50 --> 2720.48]  No way.
[2720.78 --> 2721.64]  No way.
[2722.28 --> 2724.00]  And by the way, dear listeners,
[2724.44 --> 2726.76]  it's Friday, 7 p.m.
[2726.76 --> 2728.08]  as we are recording this.
[2728.64 --> 2730.44]  So what could possibly go wrong?
[2730.80 --> 2732.02]  Oh yes, it's 2 p.m. for you.
[2732.08 --> 2732.16]  Yeah.
[2732.18 --> 2732.34]  Okay.
[2732.36 --> 2732.80]  So it's fine.
[2733.28 --> 2734.76]  It's only for me, 7 p.m.
[2736.60 --> 2737.42]  That's amazing.
[2737.62 --> 2737.86]  Okay.
[2738.30 --> 2740.46]  I put a link in the chat if you want to see.
[2740.76 --> 2741.36]  There's a GIF there.
[2741.48 --> 2742.02]  Yes, yes, yes.
[2742.06 --> 2742.60]  Thank you.
[2742.76 --> 2742.94]  Yep.
[2743.48 --> 2744.00]  Pull request.
[2744.18 --> 2744.76]  2-2-2.
[2745.00 --> 2745.60]  No way.
[2746.22 --> 2748.22]  We are not making this stuff up.
[2748.64 --> 2751.30]  It's the 22nd of July as we are recording this.
[2751.54 --> 2752.06]  2022.
[2752.84 --> 2754.62]  And the pull request is 2-2-2.
[2755.00 --> 2755.62]  No way.
[2756.58 --> 2757.14]  No way.
[2757.54 --> 2758.66]  This is too good.
[2759.28 --> 2760.84]  So I'm looking at the rave.
[2761.24 --> 2762.66]  I love that little bar.
[2762.66 --> 2763.54]  Is that it?
[2763.64 --> 2765.04]  Like the little, like the shrinking bar?
[2765.26 --> 2765.38]  Yep.
[2765.98 --> 2766.84]  Oh, wow.
[2767.56 --> 2770.42]  So this was actually quite an adventure.
[2770.70 --> 2773.38]  It took like four days to implement this thing.
[2773.46 --> 2774.66]  And this is four days of vacation,
[2774.66 --> 2776.36]  not just like four days after hours
[2776.36 --> 2779.08]  because it syncs with the Spotify API.
[2779.76 --> 2781.30]  So like each beat that you're seeing there
[2781.30 --> 2783.26]  is not only synced to like the BPM,
[2783.32 --> 2785.68]  it's actually literally rendering the beats in the song.
[2786.04 --> 2786.70]  No way, man.
[2786.90 --> 2787.54]  No way.
[2787.92 --> 2788.78]  So if you try to play,
[2788.90 --> 2791.36]  if you listen to like Lateralis by Tool,
[2791.36 --> 2794.64]  which has like changing time,
[2795.00 --> 2795.70]  I forget what it's called,
[2796.34 --> 2797.68]  but it'll actually like speed up
[2797.68 --> 2798.90]  and slow down at certain parts.
[2799.16 --> 2799.44]  Okay.
[2799.58 --> 2800.66]  This is too cool.
[2800.92 --> 2801.86]  This is too cool.
[2801.94 --> 2803.06]  So how can I try this?
[2803.12 --> 2804.16]  How can I test this?
[2804.66 --> 2805.80]  You can install from main,
[2806.48 --> 2807.18]  just like from source.
[2807.36 --> 2807.66]  Okay.
[2807.76 --> 2808.30]  If you want it.
[2808.48 --> 2808.80]  All right.
[2809.04 --> 2810.28]  But it integrates with Spotify.
[2810.48 --> 2811.30]  So I don't know if you use Spotify.
[2811.36 --> 2812.86]  This recording just got derailed.
[2814.42 --> 2816.02]  So I don't know whether we're metamode.
[2816.14 --> 2817.36]  I don't know what's happening anymore,
[2817.46 --> 2818.46]  but I know it's really cool.
[2818.52 --> 2819.90]  I don't want to try it out right now.
[2820.18 --> 2821.60]  You can probably just go install it.
[2821.64 --> 2821.90]  Actually,
[2821.94 --> 2823.34]  I don't think you need anything like that.
[2823.76 --> 2826.38]  If you brew install UPX.
[2827.14 --> 2828.98]  Brew install UPX.
[2828.98 --> 2829.74]  Yeah.
[2829.84 --> 2831.88]  That's one gotcha dependency that you'll need.
[2832.20 --> 2832.56]  UPX.
[2832.68 --> 2832.84]  Okay.
[2833.40 --> 2834.88]  That's for compressing the binaries.
[2835.16 --> 2835.92]  So like base has to,
[2836.06 --> 2837.60]  when it calls into build kit,
[2837.72 --> 2838.66]  it has to run thunks,
[2838.72 --> 2841.36]  like through a little shim to like meet the interfaces
[2841.36 --> 2841.88]  that it needs,
[2841.92 --> 2842.92]  like supporting standard in,
[2843.04 --> 2843.54]  standard in,
[2843.62 --> 2844.06]  for example.
[2844.62 --> 2844.90]  Okay.
[2845.00 --> 2847.80]  But those binaries are too large to pass over GRPC.
[2848.00 --> 2849.78]  So I have to compress them and then bundle them in.
[2850.02 --> 2851.02]  That's what UPX is for.
[2851.26 --> 2851.62]  Interesting.
[2851.82 --> 2852.04]  Okay.
[2852.10 --> 2852.78]  So I have Git,
[2852.86 --> 2853.38]  I have Go,
[2853.50 --> 2854.22]  I have UPX.
[2854.22 --> 2854.50]  Okay.
[2855.16 --> 2855.92]  Git clone,
[2856.26 --> 2856.46]  CD,
[2856.60 --> 2857.34]  and then make install.
[2857.84 --> 2858.06]  Yep.
[2858.46 --> 2859.02]  Should do it.
[2859.54 --> 2859.74]  Okay,
[2859.80 --> 2859.98]  cool.
[2860.50 --> 2860.68]  Man,
[2860.70 --> 2861.40]  this is really cool.
[2861.82 --> 2863.26]  I was not expecting this,
[2863.36 --> 2864.34]  but I'm loving it.
[2864.70 --> 2865.38]  Do you use Spotify?
[2865.88 --> 2866.28]  Really,
[2866.36 --> 2866.76]  really do.
[2868.62 --> 2869.02]  No.
[2869.78 --> 2870.02]  Oh,
[2870.20 --> 2871.12]  but I can get an account.
[2872.12 --> 2872.52]  Okay.
[2872.64 --> 2872.88]  No,
[2872.98 --> 2873.18]  I mean,
[2873.18 --> 2873.50]  seriously,
[2873.58 --> 2874.74]  I'm getting an account for this.
[2874.80 --> 2875.62]  This is like worth it.
[2875.66 --> 2876.52]  This just got derailed,
[2876.66 --> 2877.24]  but it's amazing.
[2877.40 --> 2877.88]  Sign up.
[2878.46 --> 2878.92]  Let's see.
[2879.56 --> 2880.42]  Sign up with Google.
[2881.12 --> 2881.38]  Yes,
[2881.38 --> 2881.56]  yes,
[2881.56 --> 2881.98]  yes.
[2882.54 --> 2882.74]  Oh,
[2883.26 --> 2883.70]  there you go.
[2884.88 --> 2885.10]  Oh,
[2885.18 --> 2886.84]  this email is already connected to an account.
[2886.84 --> 2887.76]  So I must have one.
[2888.22 --> 2888.50]  Okay.
[2888.54 --> 2889.24]  Continue with Google.
[2889.38 --> 2890.22]  And I don't even know one.
[2890.66 --> 2892.82]  You'd not have a Spotify connected to your Google account.
[2893.62 --> 2894.02]  Okay.
[2894.66 --> 2896.68]  I have a username and it works.
[2896.96 --> 2897.30]  Okay.
[2897.32 --> 2897.88]  I'm logged in.
[2898.18 --> 2900.14]  I do have Spotify and I didn't even know.
[2901.92 --> 2903.36]  That's how long ago it's been.
[2903.46 --> 2903.66]  Okay.
[2904.14 --> 2905.02]  So I have,
[2905.08 --> 2905.52]  um,
[2906.08 --> 2907.02]  I have base.
[2907.48 --> 2907.94]  Okay.
[2908.06 --> 2909.58]  And let me just install it.
[2910.18 --> 2910.62]  Okay.
[2911.40 --> 2912.06]  Off it goes.
[2912.88 --> 2914.76]  You'll need build kit running somewhere somehow.
[2914.98 --> 2915.10]  Okay.
[2915.18 --> 2915.66]  I have,
[2916.06 --> 2916.78]  uh,
[2917.06 --> 2918.02]  if you have Docker running,
[2918.06 --> 2918.46]  it should,
[2918.54 --> 2918.92]  uh,
[2918.92 --> 2919.88]  just start it for you now.
[2920.26 --> 2920.58]  Nice.
[2920.74 --> 2920.92]  Yes,
[2920.92 --> 2921.22]  I do.
[2921.28 --> 2921.54]  Actually,
[2921.60 --> 2922.32]  I need to update the,
[2922.52 --> 2923.42]  I need to push the docs.
[2923.92 --> 2924.30]  Yeah.
[2924.38 --> 2924.52]  Cool.
[2924.52 --> 2925.24]  I stole that from dagger.
[2926.40 --> 2927.18]  Very sweet.
[2927.52 --> 2928.30]  That's amazing.
[2928.80 --> 2929.14]  Okay.
[2929.38 --> 2930.18]  Great ideas.
[2930.44 --> 2930.94]  Great idea.
[2930.94 --> 2931.26]  You see,
[2931.60 --> 2932.38]  that's what happens.
[2932.88 --> 2933.26]  Okay.
[2933.40 --> 2934.10]  What is Lima?
[2935.30 --> 2935.74]  Uh,
[2935.80 --> 2936.32]  Lima is,
[2936.44 --> 2939.08]  it's a really cool project where they're trying to,
[2939.08 --> 2940.18]  you know,
[2940.24 --> 2944.20]  there's like this general pattern of like a lot of developers use Macs,
[2944.28 --> 2947.84]  but they need to use Docker or like some other Linux tool.
[2948.48 --> 2954.72]  Lima is basically generalizing that where instead of having like a VM managed by like Docker
[2954.72 --> 2956.12]  desktop and another VM,
[2956.12 --> 2956.90]  uh,
[2956.90 --> 2957.12]  if,
[2957.16 --> 2959.26]  if build kit like productized itself,
[2959.26 --> 2960.04]  uh,
[2960.04 --> 2965.22]  Lima is like a general template toolkit for spinning up VMs with software pre-installed.
[2965.90 --> 2967.22]  And they had one for build kit,
[2967.22 --> 2968.48]  but you shouldn't need it anymore.
[2968.62 --> 2969.02]  Uh,
[2969.02 --> 2972.40]  cause now it'll just spin up build kit in Docker.
[2972.86 --> 2973.30]  Interesting.
[2974.08 --> 2974.52]  Okay.
[2975.04 --> 2975.60]  I have base.
[2976.10 --> 2976.38]  Oh,
[2976.44 --> 2976.72]  it works.
[2977.06 --> 2977.62]  What do you do next?
[2977.70 --> 2978.18]  Base rave?
[2978.60 --> 2978.96]  Uh,
[2979.12 --> 2979.66]  base.
[2980.52 --> 2981.60]  You could run a demo,
[2981.72 --> 2982.28]  uh,
[2982.28 --> 2985.30]  like booklet test dot base demos,
[2985.42 --> 2985.96]  booklet test.
[2986.42 --> 2986.90]  Okay.
[2986.90 --> 2988.54]  So base B,
[2989.14 --> 2990.24]  base demos,
[2990.56 --> 2991.76]  booklet test.
[2992.34 --> 2992.50]  Yep.
[2992.86 --> 2993.04]  Uh,
[2993.04 --> 2993.78]  test dot base,
[2994.90 --> 2995.18]  uh,
[2995.32 --> 2997.12]  test dot base.
[2997.82 --> 2998.14]  Yes.
[2998.44 --> 2998.66]  Okay.
[2998.68 --> 2999.80]  Now press R.
[3000.36 --> 3000.66]  R.
[3000.86 --> 3001.10]  Yep.
[3001.42 --> 3001.64]  Yep.
[3001.94 --> 3002.34]  Okay.
[3002.62 --> 3003.92]  And that should open a browser.
[3004.72 --> 3005.24]  It did,
[3005.46 --> 3007.62]  but you don't see it because that's like on a separate one.
[3007.70 --> 3007.88]  Okay.
[3007.92 --> 3008.26]  Yes.
[3008.84 --> 3009.14]  Yeah.
[3009.72 --> 3011.80]  So now it should be synced.
[3011.86 --> 3012.58]  If you press D.
[3013.02 --> 3013.58]  D in here.
[3013.58 --> 3013.76]  Yep.
[3014.50 --> 3014.74]  Yeah.
[3015.42 --> 3016.04]  Like in base.
[3016.46 --> 3016.74]  Yes.
[3017.36 --> 3017.54]  Oh,
[3017.54 --> 3018.68]  it doesn't look like it's synced actually.
[3019.34 --> 3019.66]  Okay.
[3020.94 --> 3021.34]  Try.
[3021.90 --> 3022.28]  Let's see.
[3022.36 --> 3022.42]  I,
[3022.62 --> 3024.24]  maybe because you don't see the other window,
[3024.34 --> 3026.20]  maybe there's something wrong and you don't know what is wrong.
[3026.20 --> 3028.76]  So let me stop sharing this window and maybe share.
[3029.40 --> 3029.78]  You know what?
[3029.80 --> 3031.78]  Let me try sharing the entire screen.
[3031.94 --> 3032.60]  How about that?
[3032.64 --> 3034.08]  I'll share this entire screen.
[3034.80 --> 3037.42]  I'm going to move this on the left hand side.
[3037.52 --> 3039.44]  I'm going to move this on the right hand side.
[3040.06 --> 3041.32]  So that was Spotify.
[3042.16 --> 3042.98]  That's what I want to do.
[3043.12 --> 3044.56]  So base this one,
[3044.68 --> 3045.92]  press D you said,
[3046.44 --> 3046.60]  Oh,
[3046.64 --> 3048.28]  there it gets currently couldn't decode.
[3048.28 --> 3050.28]  User not registered in the develop dashboard.
[3051.16 --> 3052.44]  Do I have to enable users?
[3052.44 --> 3053.22]  I've never like,
[3053.38 --> 3054.62]  I'm the only user right now.
[3054.86 --> 3055.42]  So that's great.
[3055.50 --> 3056.20]  We're testing this.
[3056.28 --> 3056.78]  I love it.
[3057.38 --> 3058.36]  You haven't shipped it yet.
[3058.36 --> 3058.62]  Right?
[3058.64 --> 3060.46]  Like we are still working towards,
[3060.58 --> 3063.78]  I basically QAing the feature that you're about to ship.
[3063.92 --> 3064.56]  And I'm the,
[3064.70 --> 3067.04]  I'm the second ever user to do this.
[3067.04 --> 3067.92]  So that's right.
[3067.94 --> 3070.58]  I think this is exactly what we would expect to happen.
[3070.84 --> 3072.40]  It works on your computer.
[3073.16 --> 3073.60]  Yeah.
[3073.60 --> 3074.96]  But does it work on mine?
[3075.22 --> 3076.94]  That's the question we should try to answer now.
[3077.40 --> 3078.36]  How to enable.
[3078.98 --> 3079.36]  Oh,
[3079.36 --> 3080.66]  is it because it's in development mode?
[3080.94 --> 3081.18]  Okay.
[3081.76 --> 3082.38]  What's your,
[3082.56 --> 3084.14]  can you put your Spotify email?
[3084.66 --> 3086.22]  I think if I just add you here,
[3086.38 --> 3086.82]  it might work.
[3086.94 --> 3087.10]  Yes,
[3087.12 --> 3087.28]  yes,
[3087.30 --> 3087.56]  yes.
[3088.30 --> 3089.18]  It's this one.
[3089.82 --> 3090.58]  Good to know.
[3091.02 --> 3092.30]  And this is the Spotify username.
[3093.30 --> 3093.94]  Same as my Twitter,
[3094.08 --> 3094.64]  Gerhard Lassie.
[3095.12 --> 3095.50]  Okay.
[3095.70 --> 3096.18]  Try now.
[3096.74 --> 3096.84]  You,
[3096.96 --> 3098.54]  you probably also need to be playing something.
[3099.08 --> 3099.38]  Okay.
[3100.14 --> 3101.14]  Let me play this.
[3101.82 --> 3102.48]  If you want,
[3102.52 --> 3103.70]  you can run one that's like infinite.
[3104.16 --> 3106.94]  If you don't mind spending one of your cores,
[3106.94 --> 3109.62]  you could run demos slash fib dash loop.
[3110.14 --> 3110.96]  I have 10.
[3111.22 --> 3111.86]  Not a problem.
[3111.96 --> 3112.24]  There you go.
[3112.24 --> 3112.56]  20.
[3112.72 --> 3113.18]  But anyways,
[3113.80 --> 3116.24]  so demos fib loop.
[3116.46 --> 3116.66]  Yep.
[3116.82 --> 3117.60]  With the dash.
[3118.58 --> 3119.20]  Off it goes.
[3119.56 --> 3120.76]  And then try pressing R.
[3121.34 --> 3121.76]  R.
[3122.02 --> 3122.28]  Yes.
[3123.18 --> 3123.86]  Nothing happens.
[3124.16 --> 3125.68]  It didn't show that error now at least.
[3126.06 --> 3126.26]  No,
[3126.30 --> 3126.56]  it didn't.
[3126.66 --> 3127.44]  Maybe it's already connected.
[3127.98 --> 3130.72]  Try capital R to clear it.
[3130.78 --> 3131.92]  And then R again to.
[3132.40 --> 3132.78]  Yes.
[3133.36 --> 3134.30]  It opened this.
[3134.40 --> 3134.68]  Okay.
[3135.16 --> 3135.50]  Agree.
[3136.14 --> 3136.38]  Yep.
[3136.94 --> 3138.00]  That looks fine.
[3138.22 --> 3139.02]  And you're playing something.
[3139.26 --> 3140.82]  I'm not playing anything just yet,
[3140.86 --> 3142.22]  but I'm playing something now.
[3142.48 --> 3142.70]  Okay.
[3142.74 --> 3143.06]  And then,
[3143.14 --> 3143.42]  yeah.
[3143.58 --> 3145.80]  Press R again to sync it.
[3145.80 --> 3146.22]  R again.
[3146.38 --> 3146.52]  Yep.
[3147.18 --> 3147.46]  Yes.
[3147.56 --> 3148.32]  There you go.
[3149.06 --> 3149.50]  Nice.
[3149.78 --> 3150.54]  And if you press D,
[3150.74 --> 3152.14]  it'll show like the.
[3152.44 --> 3153.28]  And the D.
[3153.80 --> 3153.98]  Yep.
[3154.02 --> 3154.40]  There you go.
[3154.76 --> 3155.14]  Yes.
[3155.86 --> 3156.16]  Oh,
[3156.16 --> 3157.20]  no way.
[3157.80 --> 3160.24]  We made a thing change color.
[3160.82 --> 3162.72]  How many engineers does it actually be?
[3162.72 --> 3165.38]  Sing to a song that I'm playing in Spotify.
[3165.38 --> 3166.18]  Oh,
[3166.26 --> 3166.50]  wow.
[3166.50 --> 3167.82]  This is so cool.
[3168.70 --> 3169.58]  No way.
[3169.82 --> 3170.90]  The tragic thing though,
[3170.90 --> 3175.22]  is Spotify's API doesn't give you enough info to actually sync it perfectly.
[3175.44 --> 3176.82]  So it does its best.
[3176.92 --> 3177.20]  Okay.
[3177.20 --> 3178.22]  But if it's out of sync,
[3178.26 --> 3181.08]  you can press minus and plus to like adjust the timing.
[3181.58 --> 3181.88]  Okay.
[3182.56 --> 3183.86]  So if I do minus now,
[3184.36 --> 3185.46]  what does minus do?
[3186.06 --> 3189.08]  So it has it go back by like a hundred milliseconds.
[3189.76 --> 3190.16]  Okay.
[3190.16 --> 3190.52]  Yeah.
[3190.52 --> 3193.28]  So it's just like a slight timing because often it's out of sync.
[3193.80 --> 3194.60]  No way.
[3194.86 --> 3197.34]  So let me try and summarize what we've done here.
[3197.56 --> 3201.42]  We are running an infinite command in base.
[3202.08 --> 3205.28]  We have synced the base CLI.
[3205.44 --> 3206.90]  We've connected the base CLI.
[3207.00 --> 3209.30]  We've authenticated the base CLI with a Spotify,
[3209.98 --> 3211.28]  with my Spotify account.
[3211.28 --> 3213.76]  And whenever I'm playing a song,
[3214.04 --> 3216.34]  whatever's running in base locally,
[3216.34 --> 3223.72]  it's synchronized with a song and the BPMs and the colors match what is happening in the song.
[3223.94 --> 3225.00]  Is that what we've done here?
[3225.20 --> 3226.86]  It doesn't affect like the program or anything.
[3227.04 --> 3229.32]  It's just purely that little spinner thing there.
[3229.68 --> 3229.88]  But yeah,
[3229.98 --> 3230.18]  this.
[3230.54 --> 3231.08]  No way.
[3231.28 --> 3232.76]  Usually when I'm working on something,
[3232.82 --> 3234.56]  I'm listening to music at the same time.
[3234.56 --> 3237.80]  So it's just kind of fun to see like a spinner sync up to it.
[3238.22 --> 3240.46]  This is amazing.
[3240.72 --> 3241.40]  No way.
[3241.46 --> 3243.28]  I have to take a screenshot of all this.
[3243.38 --> 3246.80]  Like I'm going to move some windows around for us to see this.
[3246.86 --> 3251.48]  I'm going to stop sharing my screen so I can take a proper screenshot.
[3251.62 --> 3252.78]  I'm going to adjust some lighting.
[3253.78 --> 3255.92]  And this one is going in the show notes.
[3256.80 --> 3257.44]  All this.
[3257.78 --> 3260.08]  Because this is unbelievable.
[3260.08 --> 3261.28]  All right.
[3262.04 --> 3264.36]  This is a screenshot that will make it in the show notes.
[3264.86 --> 3267.12]  Not the one that we're taking early on.
[3267.58 --> 3270.94]  This one that shows this amazingness that we've just done.
[3271.36 --> 3271.54]  Okay.
[3272.24 --> 3273.80]  So step one is done.
[3274.82 --> 3275.74]  Step two,
[3276.62 --> 3277.18]  shipping it,
[3277.24 --> 3277.36]  right?
[3277.42 --> 3278.56]  Because we confirmed it works.
[3278.86 --> 3278.98]  Right.
[3279.30 --> 3279.62]  Well,
[3280.22 --> 3282.26]  anything else that needs to happen?
[3282.54 --> 3287.46]  It works as long as I'm acutely aware of everyone that uses base and add them as a user of this app.
[3287.46 --> 3291.08]  So I need to figure out how to change this app to a different status.
[3291.36 --> 3292.70]  So it's not developer anymore.
[3292.82 --> 3293.34]  That's the one.
[3293.60 --> 3293.74]  Yeah.
[3294.72 --> 3295.16]  Well,
[3295.54 --> 3296.36]  I have to tell you,
[3296.44 --> 3301.70]  I feel very special for being the first user other than you for which base works in this way.
[3301.70 --> 3303.66]  I'm super excited about this.
[3303.76 --> 3304.38]  Appreciate the testing.
[3304.78 --> 3305.24]  Anytime.
[3305.24 --> 3305.42]  time.
[3308.14 --> 3308.74]  So,
[3308.74 --> 3320.74]  this episode is brought to you by our friends at Retool.
[3320.88 --> 3324.82]  Retool helps teams focus on product development and customer value,
[3325.04 --> 3327.68]  not building and maintaining internal tools.
[3327.68 --> 3330.92]  It's a low code platform built specifically for developers.
[3331.50 --> 3332.62]  No more UI libraries,
[3333.14 --> 3334.64]  no more hacking together data sources,
[3335.18 --> 3337.38]  and no more worrying about access controls.
[3337.88 --> 3342.76]  Start shipping internal apps to move your business forward in minutes with basically zero uptime,
[3343.04 --> 3343.64]  reliability,
[3344.10 --> 3345.78]  or maintenance burden on your team.
[3346.10 --> 3347.88]  Some of the best teams out there trust Retool,
[3348.00 --> 3348.42]  Brex,
[3348.68 --> 3349.30]  Coinbase,
[3349.44 --> 3349.96]  Plaid,
[3350.28 --> 3350.90]  DoorDash,
[3351.14 --> 3351.98]  LegalGenius,
[3352.16 --> 3352.68]  Amazon,
[3352.88 --> 3353.32]  Allbirds,
[3353.48 --> 3353.82]  Peloton,
[3354.04 --> 3355.16]  and so many more.
[3355.16 --> 3360.22]  The developers at these teams trust Retool as their platform to build their internal tools,
[3360.42 --> 3361.68]  and that means you can too.
[3362.06 --> 3362.84]  It's free to try,
[3362.98 --> 3365.02]  so head to retool.com slash changelog.
[3365.18 --> 3365.66]  Again,
[3366.16 --> 3368.74]  retool.com slash changelog.
[3369.04 --> 3370.54]  And by our friends at Acuity,
[3370.70 --> 3375.80]  a new platform that brings fully managed Argo CD and enterprise services to the cloud or on-premise.
[3375.98 --> 3378.00]  And I'm here with two of the co-founders from Acuity,
[3378.30 --> 3380.16]  Jesse Suen and Alexander Matrusenchev.
[3381.12 --> 3383.70]  So the Acuity platform is in beta right now.
[3383.70 --> 3386.82]  You guys have some big ideas you're executing on around Argo CD,
[3387.32 --> 3388.16]  managed Argo CD,
[3388.46 --> 3389.84]  Kubernetes native application delivery,
[3390.18 --> 3391.32]  and the power of GitOps.
[3391.38 --> 3394.26]  Help me understand the what and the why of what you're doing right now.
[3394.50 --> 3399.58]  So we started Acuity because we saw what was happening in the Kubernetes community,
[3399.82 --> 3403.52]  the challenges that people were facing about developer experience.
[3403.92 --> 3407.34]  And having run Argo CD for Intuit for a couple of years,
[3407.48 --> 3410.44]  we knew it took like a small team to build this and scale it
[3410.44 --> 3413.62]  and provide a performant solution for the developers.
[3413.62 --> 3416.32]  And so at Acuity, in the QE platform,
[3416.50 --> 3417.76]  what we're trying to do is,
[3417.96 --> 3420.76]  the first thing we're trying to do is actually provide Argo CD
[3420.76 --> 3423.88]  as a fully managed solution to our users.
[3424.22 --> 3426.38]  But that is just actually the start of things.
[3426.50 --> 3429.32]  And we actually want to take the next steps
[3429.32 --> 3432.90]  on improving the whole GitOps and developer experience
[3432.90 --> 3437.34]  and providing new tools and ecosystems around Argo and the Argo project.
[3437.74 --> 3438.48]  Yeah, that's right, Jesse.
[3438.48 --> 3440.32]  So Argo CD is just the beginning,
[3440.74 --> 3446.08]  but every company eventually needs way more tools integrated into the DevOps platform.
[3446.52 --> 3449.22]  And that's what we're hoping to deliver with Acuity platform.
[3449.70 --> 3452.20]  So we're hoping to provide a great user interface
[3452.20 --> 3455.22]  that enables developers to achieve what they need
[3455.22 --> 3456.68]  in a matter of just a few clicks.
[3457.00 --> 3460.00]  But we also want to make Argo CD enterprise ready.
[3460.36 --> 3463.90]  What that means is our customers will get audit
[3463.90 --> 3469.02]  and insightful analytics out of the box without configuring anything.
[3469.50 --> 3471.14]  That's what we did at Intuit,
[3471.22 --> 3473.08]  and we learned that it was not so easy to do.
[3473.44 --> 3476.26]  And that's what we're hoping to solve for multiple organizations.
[3476.90 --> 3477.68]  Very cool. Thank you, Jesse.
[3477.84 --> 3478.56]  Thank you, Alex.
[3478.68 --> 3481.70]  Again, listeners, this is a closed beta.
[3482.02 --> 3482.64]  Check it out.
[3482.90 --> 3485.46]  Acuity.io slash changelog.
[3485.58 --> 3488.40]  Head there and see what this platform is all about.
[3488.40 --> 3491.10]  Again, Acuity.io slash changelog.
[3491.24 --> 3492.78]  Links are in the show notes.
[3493.90 --> 3507.00]  So do you want to ship it or not today?
[3507.34 --> 3508.04]  I can.
[3508.52 --> 3511.42]  So last time I tried to ship it is when I like disconnected
[3511.42 --> 3513.70]  and everything went wrong because I switched monitors
[3513.70 --> 3515.86]  and then this is connected through USB to that
[3515.86 --> 3517.10]  and just like everything crashed.
[3517.26 --> 3517.48]  I see.
[3517.84 --> 3519.76]  I will try, though.
[3519.94 --> 3521.48]  I'll try to do it just on this machine
[3521.48 --> 3526.12]  and it'll take a while because it has to like build the world.
[3526.62 --> 3530.26]  By the way, it's using more than one core.
[3530.56 --> 3533.28]  Okay, don't see it anymore because I'm not sharing my screen.
[3533.38 --> 3535.94]  But let me share this window.
[3536.72 --> 3540.92]  And if I do htop, if I sort by process,
[3541.02 --> 3542.04]  and I don't want to tree view.
[3542.72 --> 3543.28]  There you go.
[3543.72 --> 3544.44]  Actually, you're right.
[3544.50 --> 3546.14]  It's 120, 32%.
[3546.14 --> 3548.10]  So it's not quite that much.
[3548.10 --> 3552.14]  The rest is probably just re-rendering the UI because of the spinner.
[3552.48 --> 3553.58]  They're re-rendering the UI.
[3554.06 --> 3554.82]  You mean this one?
[3555.38 --> 3556.10]  Yeah, that.
[3556.46 --> 3557.20]  This one right here.
[3557.32 --> 3557.52]  Okay.
[3557.88 --> 3563.42]  There's a lot of magical shell escape sequences going on to render that.
[3563.94 --> 3564.68]  This is amazing.
[3564.92 --> 3565.88]  I mean, wow.
[3566.00 --> 3571.04]  I mean, we had like something similar with TTY2 and TTY on Dagger
[3571.04 --> 3572.34]  happening just like this week.
[3573.26 --> 3574.36]  And oh, wow.
[3574.82 --> 3576.44]  Some people have some questions for you.
[3576.50 --> 3579.62]  How did you accomplish this magical feat?
[3580.28 --> 3580.78]  And guess what?
[3580.90 --> 3581.64]  Base is open source.
[3581.78 --> 3584.96]  So anyone can go and check it out, including you, dear listener.
[3585.82 --> 3589.54]  Have a look at Veto Base on GitHub.
[3589.80 --> 3589.96]  Yep.
[3590.00 --> 3591.10]  I'll put the link in the show notes.
[3592.10 --> 3592.22]  Okay.
[3592.32 --> 3593.58]  Please refactor my code for me.
[3593.80 --> 3594.54]  Someone's got to do it.
[3594.96 --> 3595.50]  Yes, exactly.
[3595.50 --> 3595.94]  Yes.
[3596.46 --> 3597.50]  Pull requests, please.
[3598.14 --> 3600.52]  That's how all great software is built these days.
[3600.52 --> 3600.96]  Okay.
[3601.62 --> 3601.86]  Cool.
[3602.32 --> 3604.30]  I can start shipping it over here.
[3604.46 --> 3607.50]  Maybe I can try to share as well.
[3607.80 --> 3608.20]  Go for it.
[3608.24 --> 3608.40]  Yes.
[3608.58 --> 3611.68]  I'm going to stop sharing my screen so you can start sharing yours.
[3611.76 --> 3614.34]  I'm going to control C my fib loop.
[3615.08 --> 3615.92]  Control C.
[3616.24 --> 3616.48]  Yes.
[3617.18 --> 3618.20]  Man, this is too cool.
[3619.06 --> 3622.76]  I was not expecting this, but I'm delighted, I have to say.
[3623.36 --> 3624.32]  Mission accomplished.
[3625.20 --> 3625.40]  Yeah.
[3625.48 --> 3629.10]  So this is shipping base 0.9.
[3629.10 --> 3634.66]  It's going to take a long time because it has to build the Nix image for shipping base,
[3634.76 --> 3636.36]  which has a bunch of dependencies.
[3637.04 --> 3638.20]  And I don't think that's even started yet.
[3639.22 --> 3639.66]  Yeah.
[3639.66 --> 3642.82]  It's showing the music visualization there.
[3642.98 --> 3645.16]  There's no way to tell, but I'm sure it's out of sync.
[3645.16 --> 3645.92]  Yeah.
[3645.92 --> 3653.12]  This visualizer, the colors on the website, the space invaders, the little base clefts
[3653.12 --> 3656.02]  that show up next to paragraphs to give you a deep link.
[3657.10 --> 3663.06]  These are really all efforts to keep base fun for me as a maintainer and also make it obvious
[3663.06 --> 3664.70]  that this is a tool built for fun.
[3664.70 --> 3669.16]  And if you want to have fun, come hang out and contribute.
[3670.06 --> 3674.80]  Because I think that was one of the things that went kind of wrong with Concourse was it was,
[3675.52 --> 3680.68]  no matter how much we tried to inject fun into it, really the user base was like serious business.
[3680.82 --> 3685.94]  People trying to do like very serious things like ship software, run CI for their organization.
[3685.94 --> 3693.70]  One of the most controversial things I think in Concourse was if you run fly and Concourse isn't running,
[3694.16 --> 3696.04]  it says, is your Concourse running?
[3696.30 --> 3697.32]  Better go catch it, lol.
[3697.76 --> 3701.94]  Which we got some complaints about because it's like when my server is not running,
[3702.00 --> 3703.80]  I don't want to see you making fun of me, which is fair.
[3704.42 --> 3707.26]  But people taking themselves too seriously.
[3707.44 --> 3709.26]  You know, I do that sometimes.
[3709.26 --> 3710.66]  I do that often, actually.
[3711.66 --> 3713.34]  And I think we all do to some extent.
[3713.34 --> 3717.60]  I think taking ourselves first and foremost too seriously.
[3718.30 --> 3721.90]  You may be stressed and that's just like a sign that you're stressed.
[3722.84 --> 3727.50]  And some of the balance, the checks and balances aren't working quite as well as they should.
[3728.44 --> 3731.52]  And you stop seeing the fun in things.
[3732.54 --> 3734.22]  This stuff is supposed to be fun.
[3734.86 --> 3738.46]  We're supposed to be enjoying this because we spend so much time
[3738.46 --> 3741.20]  dealing with all sorts of weird stuff.
[3742.16 --> 3742.64]  Mistakes.
[3742.64 --> 3746.52]  Mistakes which, you know, well-intentioned people did the best they could
[3746.52 --> 3748.46]  with what they knew at the time.
[3749.20 --> 3749.76]  And that's it.
[3750.08 --> 3750.86]  That's all.
[3750.94 --> 3753.30]  Like, no one tried to introduce the bug.
[3753.44 --> 3755.90]  No one tried to ship the broken software.
[3756.58 --> 3760.22]  A number of things just, you know, went the way they do, as they do.
[3760.52 --> 3761.72]  And that's what we end up with.
[3761.80 --> 3762.90]  How are we going to improve it?
[3763.38 --> 3766.02]  How are we going to, you know, take it lightly,
[3766.70 --> 3768.60]  do the best we can, improve,
[3768.60 --> 3770.74]  and remember to keep having fun.
[3770.82 --> 3772.04]  So I really like that story.
[3772.16 --> 3773.76]  I really like how you're thinking about this.
[3773.82 --> 3775.38]  I think more of us need to do that.
[3775.92 --> 3776.08]  Yeah.
[3776.08 --> 3779.64]  I think there's nothing more humbling than trying to build software,
[3779.96 --> 3782.04]  especially if you're trying to build software for other people.
[3782.30 --> 3785.90]  And, like, it's easy to build software for yourself.
[3786.12 --> 3787.96]  That's mostly what I've been doing with Base.
[3788.30 --> 3789.46]  And I think that's a good thing.
[3789.46 --> 3792.26]  It's harder to build it for other people
[3792.26 --> 3795.16]  because you don't know exactly where they're coming from.
[3795.50 --> 3797.96]  That, I think, is, like, one of the things I kind of feel bad about with Concourse
[3797.96 --> 3799.82]  was it was very strongly opinionated.
[3800.12 --> 3803.08]  And over time, a lot of users came to Concourse
[3803.08 --> 3806.12]  not because they chose it and, like, you know, bought into those opinions,
[3806.26 --> 3807.80]  but because their organization chose it.
[3807.98 --> 3810.84]  And then they had to deal with the very strong opinions
[3810.84 --> 3812.00]  that Concourse had about things.
[3812.08 --> 3815.48]  For example, passing runtime data into tasks
[3815.48 --> 3818.42]  is, like, a hill that I died on in Concourse
[3818.42 --> 3819.88]  because I didn't want it to be possible
[3819.88 --> 3822.50]  to have your tasks become not hermetic
[3822.50 --> 3824.84]  and become dependent on Concourse itself.
[3825.02 --> 3827.84]  But there are reasons people end up wanting that
[3827.84 --> 3830.18]  because they've already bought into Concourse.
[3830.38 --> 3832.04]  And, like, having that become a blocker
[3832.04 --> 3834.46]  means having to buy out from it
[3834.46 --> 3836.32]  and, like, completely switch to something else,
[3836.38 --> 3838.10]  which, if you like the rest of it,
[3838.52 --> 3840.14]  it's not great to be blocked on that.
[3840.22 --> 3843.36]  So that's kind of another thing I'm doing differently with Base
[3843.36 --> 3845.96]  is trying to meet people where they are more
[3845.96 --> 3848.58]  and make, like, the good patterns feel obvious,
[3848.90 --> 3851.34]  make the bad patterns not feel great,
[3851.42 --> 3854.46]  but probably still be doable to some extent, you know?
[3854.60 --> 3857.46]  Still okay, but yeah, not the best experience for sure.
[3857.54 --> 3859.18]  I think a lot of frameworks,
[3859.34 --> 3860.76]  the ones that stood the test of time,
[3860.84 --> 3861.70]  are a bit like that.
[3862.16 --> 3863.72]  Things are possible within them,
[3863.96 --> 3865.12]  but then you'll feel the pain
[3865.12 --> 3866.92]  because you're trying to go against
[3866.92 --> 3868.16]  what they were designed to do.
[3868.16 --> 3872.50]  And I think it's almost like you need to know
[3872.50 --> 3875.00]  when you're off the well-trodden path
[3875.00 --> 3876.02]  or when you're off,
[3876.50 --> 3877.46]  like, not what is possible,
[3877.60 --> 3878.64]  but what is easy.
[3879.06 --> 3881.14]  And some things, though, may be unfinished,
[3881.52 --> 3883.68]  but if something is simple, I think,
[3883.98 --> 3885.80]  if something is minimal, as you mentioned,
[3885.88 --> 3886.90]  you mentioned...
[3886.90 --> 3887.16]  Scheme.
[3887.54 --> 3888.38]  Scheme, thank you.
[3888.48 --> 3888.74]  Scheme.
[3888.96 --> 3890.10]  Yes, that's one that you mentioned.
[3890.42 --> 3891.82]  So you went from six to five
[3891.82 --> 3894.04]  because you realize you don't need a sixth one.
[3894.54 --> 3895.78]  Really simple primitives,
[3895.78 --> 3897.28]  but that are dependable,
[3897.80 --> 3900.50]  that are intuitive to a certain degree
[3900.50 --> 3902.46]  because it's still, like, you know,
[3903.06 --> 3904.46]  all abstract stuff.
[3904.56 --> 3906.00]  And that tends to be hard,
[3906.26 --> 3907.84]  especially when you start combining things
[3907.84 --> 3909.30]  and then you can't imagine
[3909.30 --> 3911.16]  all the ways in which it can combine it,
[3911.20 --> 3911.90]  what happens next,
[3912.02 --> 3913.48]  second order, third order effects,
[3913.56 --> 3914.20]  so on and so forth.
[3915.02 --> 3916.00]  The point being,
[3916.34 --> 3917.50]  if the surface is small,
[3918.24 --> 3919.68]  if the interfaces are well-defined,
[3920.22 --> 3922.80]  if there aren't many combinations possible,
[3923.26 --> 3924.08]  because there shouldn't be
[3924.08 --> 3925.46]  that many combinations possible,
[3925.46 --> 3926.20]  I think,
[3926.80 --> 3927.48]  right, because you have, like,
[3927.50 --> 3928.58]  the number of items,
[3928.96 --> 3930.76]  of, like, items in the set is smaller,
[3931.32 --> 3933.62]  then fewer things can go wrong.
[3933.94 --> 3935.02]  And if something does go wrong,
[3935.08 --> 3936.66]  then you will address that one thing,
[3936.72 --> 3937.94]  but you don't add more features.
[3937.98 --> 3940.62]  You don't add the seventh, eighth, ninth element
[3940.62 --> 3941.80]  so that you start having, like,
[3941.82 --> 3945.06]  this explosion of, like, permutations.
[3945.48 --> 3946.50]  It's like, it's a system
[3946.50 --> 3949.36]  and everything ideally reflects on each other.
[3949.66 --> 3950.92]  I think you build a good system
[3950.92 --> 3952.80]  by having every component leverages
[3952.80 --> 3954.46]  some other component within it,
[3954.46 --> 3956.64]  because that's also what kind of installs
[3956.64 --> 3957.80]  those guardrails
[3957.80 --> 3959.64]  and at least makes it easier to justify,
[3959.96 --> 3961.20]  like, hey, this has to be this way
[3961.20 --> 3961.84]  because otherwise
[3961.84 --> 3963.82]  this other load-bearing property
[3963.82 --> 3964.96]  of concourse or base
[3964.96 --> 3965.96]  just doesn't work.
[3966.54 --> 3967.66]  And you need that because,
[3968.44 --> 3969.58]  well, you just want that.
[3969.72 --> 3970.66]  Like caching, for example,
[3971.26 --> 3972.74]  was kind of a forcing function
[3972.74 --> 3975.08]  for having resources be pure.
[3975.08 --> 3977.04]  And you definitely want to be caching
[3977.04 --> 3978.36]  all those fetches, right?
[3978.90 --> 3980.50]  How do you handle that, by the way,
[3980.62 --> 3982.90]  in base, the whole caching aspect?
[3983.22 --> 3984.30]  Because that's a big one.
[3984.38 --> 3986.06]  And actually, it's even, like, in the tagline.
[3986.62 --> 3987.76]  I'm going to read it
[3987.76 --> 3990.36]  because I want to say it exactly as it is.
[3991.32 --> 3992.82]  Base is a scripting language
[3992.82 --> 3994.10]  for running commands
[3994.10 --> 3995.86]  and caching the s*** out of them.
[3996.44 --> 3997.44]  That's supposed to be funny.
[3998.02 --> 3999.44]  Not ironic, not arrogant.
[3999.78 --> 4000.82]  I mean, it's just, you know,
[4001.24 --> 4001.98]  that's what we want.
[4002.04 --> 4003.82]  You want everything to be cached all the time.
[4003.82 --> 4005.06]  So, honestly,
[4005.18 --> 4006.52]  all the magic there is in BuildKit.
[4006.94 --> 4009.34]  Base is really just building up
[4009.34 --> 4010.72]  the LLB data structure
[4010.72 --> 4012.32]  and just setting it over the wire.
[4012.92 --> 4014.14]  BuildKit is the one that tracks
[4014.14 --> 4016.14]  all the dependencies between things.
[4017.16 --> 4019.56]  And if it doesn't need to run something
[4019.56 --> 4020.44]  because it already ran it,
[4020.46 --> 4021.24]  then it just won't run it.
[4021.42 --> 4023.62]  So if I run this ship it thing,
[4024.18 --> 4025.26]  if it ever finishes.
[4025.80 --> 4026.54]  If I run this again,
[4026.62 --> 4027.78]  theoretically, it just doesn't know up
[4027.78 --> 4029.26]  because every command is cached
[4029.26 --> 4030.46]  and every input is controlled.
[4031.10 --> 4032.42]  Where that starts to break down
[4032.42 --> 4033.86]  is when you start passing things in
[4033.86 --> 4034.76]  from the host machine.
[4035.10 --> 4035.68]  That's where you need
[4035.68 --> 4037.06]  like really good diffing properties.
[4037.70 --> 4038.92]  This one should be fine
[4038.92 --> 4039.82]  because none of this
[4039.82 --> 4040.86]  should be coming from the host.
[4041.00 --> 4042.28]  It passes the SHA in
[4042.28 --> 4044.16]  and like within this JSON file,
[4044.22 --> 4044.92]  there's a git clone
[4044.92 --> 4046.00]  and a git checkout somewhere
[4046.00 --> 4046.66]  of that SHA.
[4047.38 --> 4047.66]  Okay.
[4048.38 --> 4049.14]  And BuildKit,
[4049.22 --> 4050.32]  when it comes to running BuildKit,
[4050.42 --> 4051.96]  I know there's a couple of good talks,
[4052.10 --> 4053.10]  including one from Apple.
[4053.10 --> 4054.78]  I think it was from KubeCon 2021.
[4054.78 --> 4057.26]  I can leave a link in the show notes
[4057.26 --> 4058.66]  and they're talking about
[4058.66 --> 4060.32]  how to run BuildKit
[4060.32 --> 4061.64]  in the context of Kubernetes.
[4061.84 --> 4062.66]  You have a cluster
[4062.66 --> 4064.54]  of BuildKit instances
[4064.54 --> 4066.04]  and then you know
[4066.04 --> 4067.36]  where the caches are located.
[4067.54 --> 4069.30]  So you do like some smart routing.
[4069.46 --> 4070.98]  So you know like where to send jobs.
[4071.54 --> 4072.98]  You do some hash based routing.
[4073.46 --> 4074.80]  And then you have
[4074.80 --> 4076.66]  most likely things in the cache,
[4077.04 --> 4078.24]  but the cache is distributed.
[4078.92 --> 4078.98]  Yeah.
[4079.24 --> 4080.62]  It's tricky because like
[4080.62 --> 4081.74]  this is one of the things
[4081.74 --> 4083.20]  we struggled with with Concourse
[4083.20 --> 4085.34]  was do you bias
[4085.34 --> 4086.66]  to place workloads
[4086.66 --> 4087.64]  where a cache is present
[4087.64 --> 4088.66]  or where it's not present?
[4088.72 --> 4090.00]  Because if you do one,
[4090.10 --> 4091.12]  then you end up with like
[4091.12 --> 4092.00]  everything thundering
[4092.00 --> 4092.84]  onto one machine.
[4093.36 --> 4094.26]  If you do the other,
[4094.36 --> 4096.22]  then you're not caching as much.
[4096.78 --> 4097.50]  Ideally, you're like
[4097.50 --> 4098.78]  caching once per worker.
[4098.92 --> 4099.96]  So if you run things enough,
[4100.06 --> 4101.08]  it'll warm across the board.
[4101.56 --> 4102.54]  But yeah, that's,
[4103.12 --> 4105.56]  there's trickiness within there as well,
[4105.66 --> 4106.64]  I guess is all I'd say.
[4107.06 --> 4108.02]  Sometimes it comes down
[4108.02 --> 4108.66]  to the use case.
[4108.86 --> 4110.46]  Like user has to know
[4110.46 --> 4111.20]  if it's going to be cheaper
[4111.20 --> 4113.20]  to transfer this over the wire
[4113.20 --> 4115.08]  or just fetch it from scratch.
[4115.32 --> 4116.08]  Sometimes it's faster
[4116.08 --> 4117.26]  to just avoid the cache.
[4118.18 --> 4119.26]  It's like a giant repo.
[4119.76 --> 4120.06]  Interesting.
[4120.44 --> 4121.82]  Do you think that it's important
[4121.82 --> 4122.88]  for caching
[4122.88 --> 4125.48]  for it to be as close as possible
[4125.48 --> 4126.46]  to the compute?
[4126.88 --> 4127.84]  Or do you think
[4127.84 --> 4128.80]  it doesn't really matter
[4128.80 --> 4130.00]  if the cache is too close?
[4130.04 --> 4131.10]  Because in my mind,
[4131.64 --> 4132.32]  I think the cache
[4132.32 --> 4133.76]  should be on the same instance
[4133.76 --> 4134.92]  where the compute is.
[4135.64 --> 4137.20]  So it's almost like
[4137.20 --> 4139.00]  you want to distribute the job
[4139.00 --> 4140.06]  using maybe
[4140.06 --> 4141.62]  like a hash ring algorithm
[4141.62 --> 4143.16]  so that jobs,
[4143.26 --> 4143.88]  the same job
[4143.88 --> 4145.90]  ends up on the same host,
[4145.98 --> 4146.76]  on the same node.
[4147.14 --> 4148.06]  And I know that Cassandra
[4148.06 --> 4149.00]  had this,
[4149.08 --> 4151.36]  like a rebalancing mechanism
[4151.36 --> 4153.94]  where if you added more nodes
[4153.94 --> 4155.66]  into the cluster,
[4156.12 --> 4157.06]  there'll be the hash ring.
[4157.16 --> 4157.88]  So they would occupy,
[4157.88 --> 4159.22]  each node would occupy
[4159.22 --> 4161.34]  less of the hashing space.
[4161.78 --> 4162.40]  And there will be like
[4162.40 --> 4163.10]  some rebalancing
[4163.10 --> 4163.56]  where the data
[4163.56 --> 4164.74]  would move across.
[4164.74 --> 4166.28]  And then there would be
[4166.28 --> 4167.72]  like one or multiple nodes
[4167.72 --> 4168.24]  that would just like
[4168.24 --> 4170.18]  basically serve the cache
[4170.18 --> 4171.00]  that the new node
[4171.00 --> 4172.12]  was supposed to serve.
[4172.68 --> 4173.04]  I mean,
[4173.08 --> 4174.10]  is that too complicated,
[4174.22 --> 4174.80]  do you think?
[4174.82 --> 4176.04]  Or do you think it's necessary?
[4176.14 --> 4176.54]  Do you think there's
[4176.54 --> 4177.34]  something simpler?
[4177.96 --> 4178.88]  How do you think about that?
[4178.88 --> 4179.96]  Because that's a really
[4179.96 --> 4180.82]  interesting problem,
[4180.96 --> 4182.44]  especially for CI systems
[4182.44 --> 4183.64]  that need to run at scale.
[4184.58 --> 4185.84]  And you need to balance
[4185.84 --> 4186.28]  your right,
[4186.42 --> 4188.08]  the staleness.
[4188.72 --> 4188.94]  Like, sorry,
[4189.08 --> 4190.26]  like some jobs
[4190.26 --> 4191.02]  need to be fresh
[4191.02 --> 4191.96]  and other jobs
[4191.96 --> 4193.22]  need to have a cache
[4193.22 --> 4194.52]  because they'll run faster.
[4195.00 --> 4195.48]  That gets to like
[4195.48 --> 4196.36]  the fundamental question,
[4196.42 --> 4196.74]  I guess,
[4196.96 --> 4198.24]  is it's,
[4198.38 --> 4199.22]  I feel like it's impossible
[4199.22 --> 4200.14]  to predict really
[4200.14 --> 4201.06]  because it depends on
[4201.06 --> 4202.26]  how long does it take
[4202.26 --> 4203.16]  to build the cache
[4203.16 --> 4203.90]  versus how long
[4203.90 --> 4204.30]  does it take
[4204.30 --> 4205.18]  to transfer the cache.
[4205.74 --> 4206.38]  I don't have any
[4206.38 --> 4207.20]  unique insight
[4207.20 --> 4208.42]  on the Cassandra specific
[4208.42 --> 4209.30]  things you mentioned there,
[4209.38 --> 4210.04]  but that's the fundamental
[4210.04 --> 4210.80]  thing with concourse.
[4210.92 --> 4211.64]  And that's where we're like,
[4211.72 --> 4213.34]  at one point we were considering
[4213.34 --> 4216.18]  tracking the average duration,
[4216.36 --> 4218.30]  like on a task by task basis,
[4218.30 --> 4220.46]  because then you can kind of
[4220.46 --> 4222.34]  try to make that calculation,
[4222.34 --> 4223.62]  but you have to benchmark it
[4223.62 --> 4224.56]  against like the internal
[4224.56 --> 4225.38]  network transfer.
[4226.16 --> 4227.24]  So I guess ideally
[4227.24 --> 4228.02]  you would have a system
[4228.02 --> 4229.10]  that can kind of learn
[4229.10 --> 4229.82]  from the things
[4229.82 --> 4230.36]  that it's running,
[4230.64 --> 4232.50]  which that gets tricky
[4232.50 --> 4233.64]  because how do you identify
[4233.64 --> 4234.90]  these things?
[4235.78 --> 4236.74]  It depends on like
[4236.74 --> 4237.58]  their hermetic aspect,
[4237.72 --> 4237.84]  right?
[4237.84 --> 4238.50]  Because if you're running
[4238.50 --> 4239.72]  something that's
[4239.72 --> 4240.74]  completely controlling
[4240.74 --> 4241.34]  its inputs
[4241.34 --> 4242.76]  and like maybe it could reuse
[4242.76 --> 4244.00]  a git clone from earlier,
[4244.68 --> 4245.40]  you need some way
[4245.40 --> 4246.30]  of like identifying
[4246.30 --> 4247.30]  that they're really the same.
[4247.62 --> 4248.00]  Exactly, yes.
[4248.18 --> 4249.30]  One thing I was experimenting
[4249.30 --> 4250.16]  with in base
[4250.16 --> 4251.24]  was having it so that
[4251.24 --> 4252.86]  when you do a git clone,
[4253.14 --> 4253.72]  it would actually have
[4253.72 --> 4254.28]  multiple layers.
[4254.38 --> 4255.56]  It would have one initial layer
[4255.56 --> 4257.16]  that is like just git clone
[4257.16 --> 4257.64]  the repo,
[4258.40 --> 4259.50]  cache this every day,
[4259.88 --> 4261.42]  and then a later layer
[4261.42 --> 4262.64]  does it git fetch
[4262.64 --> 4263.94]  to bring it up to speed?
[4264.44 --> 4266.12]  And then the layer after that
[4266.12 --> 4266.78]  does it git checkout?
[4266.96 --> 4267.68]  That way you can kind of
[4267.68 --> 4268.50]  have fine grained.
[4269.14 --> 4270.16]  You can have coarse grained
[4270.16 --> 4271.36]  caching at the lowest level,
[4271.50 --> 4272.36]  so you're only cloning
[4272.36 --> 4272.88]  once a day,
[4272.98 --> 4274.28]  but then fetching
[4274.28 --> 4275.04]  at some other interval
[4275.04 --> 4276.36]  and then the final checkout
[4276.36 --> 4277.28]  is how you get there.
[4277.28 --> 4279.14]  So I guess that's one way
[4279.14 --> 4279.58]  to cut it
[4279.58 --> 4281.24]  and like have more
[4281.24 --> 4282.08]  fine grained caching
[4282.08 --> 4283.60]  of git repos specifically.
[4284.42 --> 4285.16]  That's interesting, yeah.
[4285.46 --> 4286.36]  Yeah, I don't think
[4286.36 --> 4286.98]  I've seen a system
[4286.98 --> 4287.80]  that really learns
[4287.80 --> 4288.80]  from the runtime
[4288.80 --> 4290.40]  of how long things
[4290.40 --> 4291.04]  take to run
[4291.04 --> 4292.44]  versus the size of the output
[4292.44 --> 4293.16]  that comes out of them.
[4293.54 --> 4294.18]  That sounds like
[4294.18 --> 4295.56]  a really interesting problem
[4295.56 --> 4297.32]  and I would love
[4297.32 --> 4298.54]  to solve that one day
[4298.54 --> 4300.48]  because it sounds like
[4300.48 --> 4301.60]  it will unlock so much.
[4301.74 --> 4302.70]  Like forget AI,
[4302.94 --> 4303.86]  forget machine learning,
[4304.06 --> 4305.36]  like forget all that stuff.
[4305.36 --> 4306.06]  I think it's like,
[4306.72 --> 4307.52]  I think it gets
[4307.52 --> 4308.58]  just too much hype.
[4309.30 --> 4311.04]  Something simple like this
[4311.04 --> 4312.54]  that can keep track
[4312.54 --> 4313.34]  of what is happening
[4313.34 --> 4313.98]  in the system
[4313.98 --> 4316.36]  and based on what happens,
[4316.80 --> 4317.44]  it can try
[4317.44 --> 4318.18]  and do something else,
[4318.28 --> 4318.82]  like literally,
[4318.98 --> 4320.26]  like little like optimizations,
[4320.40 --> 4320.58]  okay?
[4320.92 --> 4321.64]  Based on this,
[4321.70 --> 4322.62]  I'm going to try that
[4322.62 --> 4323.96]  and that result,
[4324.08 --> 4325.12]  it's going to use it
[4325.12 --> 4326.32]  for the next calculation.
[4326.98 --> 4328.10]  Based on all these things
[4328.10 --> 4328.56]  which I've done,
[4328.62 --> 4329.50]  I think this is going
[4329.50 --> 4330.10]  to be better
[4330.10 --> 4331.24]  and it's just like
[4331.24 --> 4332.24]  small iterations
[4332.24 --> 4333.22]  towards eventually
[4333.22 --> 4336.16]  finding its own sweet spot.
[4336.62 --> 4337.68]  It just reminds me
[4337.68 --> 4338.82]  a bit like Conway's
[4338.82 --> 4339.88]  Game of Life,
[4340.90 --> 4341.14]  you know,
[4341.18 --> 4341.90]  where like they just
[4341.90 --> 4342.58]  like keep changing
[4342.58 --> 4343.48]  and eventually
[4343.48 --> 4344.66]  like you start seeing
[4344.66 --> 4345.36]  those patterns
[4345.36 --> 4346.78]  and it just happens
[4346.78 --> 4348.38]  and they just know
[4348.38 --> 4349.16]  what to do.
[4349.34 --> 4349.92]  Like how is that
[4349.92 --> 4350.54]  even possible?
[4351.32 --> 4352.22]  They start like mimicking,
[4352.36 --> 4352.90]  you start seeing like,
[4352.98 --> 4353.88]  it's just fascinating.
[4354.14 --> 4356.38]  So that's what I imagine
[4356.38 --> 4358.82]  for this caching problem
[4358.82 --> 4359.76]  where it just learns
[4359.76 --> 4360.78]  and eventually just like
[4360.78 --> 4361.84]  gets to a point
[4361.84 --> 4363.42]  where it's stable,
[4363.52 --> 4363.94]  it's happy
[4363.94 --> 4365.00]  and there's nothing more
[4365.00 --> 4366.20]  than you can do to improve
[4366.20 --> 4368.02]  and then everything is cached.
[4368.52 --> 4368.60]  Right.
[4368.68 --> 4368.82]  Yeah.
[4369.48 --> 4369.74]  I mean,
[4369.74 --> 4370.04]  I guess,
[4370.26 --> 4371.92]  I guess it is machine learning.
[4371.92 --> 4372.16]  Yeah,
[4372.26 --> 4372.82]  in a certain way.
[4372.82 --> 4374.72]  Like in the basic,
[4374.84 --> 4375.86]  in the most basic sense,
[4375.92 --> 4376.06]  right?
[4376.44 --> 4377.60]  It's a machine learning,
[4377.94 --> 4378.84]  how long things take?
[4379.58 --> 4379.80]  Yeah,
[4379.82 --> 4380.28]  you're right.
[4380.42 --> 4380.76]  You're right.
[4380.82 --> 4381.14]  It is,
[4381.22 --> 4381.72]  but I think,
[4381.78 --> 4382.28]  I think it can,
[4382.36 --> 4383.34]  it can go so crazy,
[4383.44 --> 4383.62]  right?
[4383.66 --> 4383.82]  Like,
[4383.82 --> 4384.02]  like,
[4384.10 --> 4384.18]  oh,
[4384.18 --> 4385.18]  you have all the different,
[4385.56 --> 4386.18]  then you have like
[4386.18 --> 4387.16]  neural networks
[4387.16 --> 4388.42]  and Bayesian filters
[4388.42 --> 4388.98]  and like,
[4389.06 --> 4390.26]  it just goes a bit crazy
[4390.26 --> 4390.94]  after that
[4390.94 --> 4392.32]  and most of it
[4392.32 --> 4392.94]  is over my head
[4392.94 --> 4393.42]  to be honest,
[4393.52 --> 4395.40]  but I like think simple
[4395.40 --> 4397.20]  and I think simple
[4397.20 --> 4397.94]  is defined by,
[4398.04 --> 4398.12]  you know,
[4398.12 --> 4398.86]  like my capacity
[4398.86 --> 4399.94]  of understanding things
[4399.94 --> 4400.86]  because that's what it is
[4400.86 --> 4402.22]  and it's everyone's capacity.
[4402.52 --> 4403.58]  So there's like
[4403.58 --> 4404.34]  a common point
[4404.34 --> 4405.28]  where each of us,
[4405.72 --> 4406.50]  it's easy for us,
[4406.56 --> 4407.02]  for all of us
[4407.02 --> 4407.96]  to understand that
[4407.96 --> 4408.90]  quickly and easily
[4408.90 --> 4410.48]  and I think that's
[4410.48 --> 4411.22]  what's simple
[4411.22 --> 4412.50]  for most of us.
[4413.02 --> 4413.74]  That's how I think of it.
[4413.74 --> 4415.90]  I always also prefer simple
[4415.90 --> 4416.64]  because at least
[4416.64 --> 4417.28]  when it breaks,
[4417.78 --> 4419.18]  you know probably what happens.
[4419.38 --> 4420.48]  One failure mode for that,
[4420.56 --> 4420.94]  I guess,
[4421.04 --> 4423.20]  is you're running something
[4423.20 --> 4424.84]  on a shared machine
[4424.84 --> 4425.58]  that's also running
[4425.58 --> 4426.06]  something else
[4426.06 --> 4427.06]  that's really expensive.
[4427.06 --> 4428.14]  So it like messes
[4428.14 --> 4429.26]  with your numbers
[4429.26 --> 4430.38]  and it suddenly thinks
[4430.38 --> 4431.06]  it's more expensive
[4431.06 --> 4431.60]  in the future,
[4431.70 --> 4433.56]  but maybe there's just
[4433.56 --> 4434.80]  a button to clear the cache.
[4435.10 --> 4436.28]  All everything comes down to
[4436.28 --> 4436.98]  is clearing the cache.
[4437.08 --> 4437.54]  That's right.
[4437.78 --> 4438.64]  Cache invalidation,
[4438.72 --> 4438.90]  right?
[4439.14 --> 4439.44]  Right.
[4439.54 --> 4439.74]  Okay.
[4440.30 --> 4442.46]  So what was the most
[4442.46 --> 4443.64]  fun thing to work
[4443.64 --> 4444.74]  when it comes to base?
[4444.94 --> 4445.78]  The thing that you enjoyed
[4445.78 --> 4446.78]  working on the most
[4446.78 --> 4448.20]  because this was important.
[4448.40 --> 4450.48]  Like making base fun
[4450.48 --> 4451.64]  was important.
[4451.88 --> 4453.34]  What was the most fun thing
[4453.34 --> 4454.42]  so far?
[4455.08 --> 4455.92]  I think building
[4455.92 --> 4456.76]  the language itself.
[4457.06 --> 4457.94]  There's been a lot
[4457.94 --> 4459.00]  of different vectors
[4459.00 --> 4459.52]  for fun,
[4459.78 --> 4461.04]  but just getting back
[4461.04 --> 4462.38]  to what I was really into
[4462.38 --> 4463.12]  back in the day,
[4463.24 --> 4464.04]  just like coming up
[4464.04 --> 4465.94]  with a language
[4465.94 --> 4468.04]  and trying to have
[4468.04 --> 4469.70]  as few concepts
[4469.70 --> 4470.44]  as possible
[4470.44 --> 4471.26]  that like leverage
[4471.26 --> 4471.68]  each other
[4471.68 --> 4472.76]  in interesting ways.
[4473.32 --> 4474.46]  One example is
[4474.46 --> 4475.94]  in base,
[4476.22 --> 4477.10]  what you might call
[4477.10 --> 4478.40]  maps in Clojure
[4478.40 --> 4479.80]  or like hashes
[4479.80 --> 4480.38]  in Ruby
[4480.38 --> 4481.58]  is called scopes
[4481.58 --> 4483.76]  because they're used
[4483.76 --> 4484.52]  as both the data
[4484.52 --> 4485.36]  structure scope,
[4485.44 --> 4487.14]  but also as an actual
[4487.14 --> 4488.18]  scope when you evaluate
[4488.18 --> 4488.78]  base code.
[4489.42 --> 4490.52]  So if you,
[4490.74 --> 4491.12]  for example,
[4491.66 --> 4493.00]  take like a JSON scope,
[4493.62 --> 4494.56]  like a scope
[4494.56 --> 4494.90]  that was like
[4494.90 --> 4495.62]  parsed from JSON,
[4495.92 --> 4496.48]  you could actually
[4496.48 --> 4497.42]  evaluate base code
[4497.42 --> 4498.58]  using that as like
[4498.58 --> 4499.52]  the runtime environment.
[4500.10 --> 4501.30]  A lot of the times
[4501.30 --> 4502.40]  where I try to like,
[4502.94 --> 4503.94]  anytime I see like
[4503.94 --> 4504.66]  enough similarity
[4504.66 --> 4505.58]  between two concepts,
[4505.64 --> 4506.56]  I actually try to just
[4506.56 --> 4507.92]  magnetically like
[4507.92 --> 4508.64]  put them together
[4508.64 --> 4509.74]  and so far it's been
[4509.74 --> 4510.20]  paying off.
[4510.40 --> 4511.30]  I'm sure it'll blow up
[4511.30 --> 4512.38]  in my face by like
[4512.38 --> 4513.92]  over leveraging one concept
[4513.92 --> 4515.90]  in some interesting way,
[4516.02 --> 4516.92]  but I'm hoping that like
[4516.92 --> 4517.32]  the,
[4517.32 --> 4518.72]  the fact that base
[4518.72 --> 4519.62]  is kind of restricted
[4519.62 --> 4520.44]  to one domain,
[4520.60 --> 4521.56]  I'm hoping that keeps it
[4521.56 --> 4522.76]  like low likelihood
[4522.76 --> 4524.36]  of too many foot guns
[4524.36 --> 4525.44]  emerging from my
[4525.44 --> 4526.34]  overuse of concepts.
[4526.34 --> 4527.06]  Well,
[4527.50 --> 4528.02]  thing is,
[4528.06 --> 4528.76]  you never know
[4528.76 --> 4531.10]  until you keep trying
[4531.10 --> 4531.98]  and keep getting
[4531.98 --> 4532.56]  to a point
[4532.56 --> 4533.26]  where you realize,
[4533.34 --> 4533.58]  you know what,
[4533.62 --> 4534.34]  this doesn't work
[4534.34 --> 4535.32]  and that's okay
[4535.32 --> 4537.08]  because you always like,
[4537.20 --> 4538.06]  as long as you have
[4538.06 --> 4539.10]  a fitness function
[4539.10 --> 4540.04]  that can determine
[4540.04 --> 4541.48]  whether what you do
[4541.48 --> 4542.30]  gets you closer
[4542.30 --> 4542.80]  to where you're
[4542.80 --> 4543.64]  trying to get to,
[4544.16 --> 4544.70]  that's okay.
[4544.80 --> 4545.70]  If it says I'm closer,
[4545.82 --> 4546.50]  then I am closer
[4546.50 --> 4547.70]  unless the function
[4547.70 --> 4548.10]  is wrong,
[4548.20 --> 4549.34]  but I think you would know
[4549.34 --> 4550.22]  if the function was wrong
[4550.22 --> 4550.72]  because that's
[4550.72 --> 4551.66]  really fundamental
[4551.66 --> 4553.70]  and I think in your case,
[4553.92 --> 4554.76]  the fitness function
[4554.76 --> 4555.36]  is,
[4555.48 --> 4556.10]  is it fun?
[4556.42 --> 4557.58]  Am I having fun with this?
[4557.92 --> 4559.08]  And that's like instinct.
[4559.26 --> 4560.40]  You know that you're having fun.
[4560.58 --> 4561.62]  It's very difficult
[4561.62 --> 4562.32]  to game that,
[4562.56 --> 4563.08]  you know.
[4563.50 --> 4564.44]  There's no amount
[4564.44 --> 4565.40]  of like anything
[4565.40 --> 4566.06]  that you can do
[4566.06 --> 4566.84]  other than just
[4566.84 --> 4568.18]  be honest with yourself
[4568.18 --> 4570.06]  whether you're delivering
[4570.06 --> 4571.76]  towards that goal.
[4572.52 --> 4573.38]  So I see that
[4573.38 --> 4574.64]  and I've noticed
[4574.64 --> 4576.20]  that there's a lot of nicks,
[4576.72 --> 4577.50]  like I don't want
[4577.50 --> 4578.08]  to say a lot of,
[4578.12 --> 4579.24]  but like a significant amount
[4579.24 --> 4580.28]  of nicks in base.
[4580.82 --> 4581.92]  What is the relationship
[4581.92 --> 4583.58]  between nicks
[4583.58 --> 4585.46]  and base the language?
[4585.84 --> 4586.80]  So this is something
[4586.80 --> 4587.96]  I've been very careful about
[4587.96 --> 4589.28]  because I know nicks
[4589.28 --> 4590.14]  is one of those things
[4590.14 --> 4591.92]  where the mere mention
[4591.92 --> 4593.08]  of it near your project
[4593.08 --> 4594.14]  can send people
[4594.14 --> 4594.92]  like scurrying
[4594.92 --> 4595.86]  and running to the hills
[4595.86 --> 4596.84]  and trying to avoid it
[4596.84 --> 4598.28]  because some people
[4598.28 --> 4598.76]  see it as like
[4598.76 --> 4599.42]  very complicated
[4599.42 --> 4600.60]  and hard to get into
[4600.60 --> 4602.20]  and I think they're right,
[4602.28 --> 4603.04]  but there's a lot of like
[4603.04 --> 4604.58]  really cool parts to nicks
[4604.58 --> 4605.80]  that are hard to find
[4605.80 --> 4606.56]  anywhere else.
[4606.56 --> 4609.04]  To me, the biggest value
[4609.04 --> 4609.96]  to nicks is having
[4609.96 --> 4610.82]  just the largest
[4610.82 --> 4612.08]  and most up-to-date
[4612.08 --> 4614.02]  software package repository
[4614.02 --> 4614.90]  in the world.
[4615.26 --> 4616.36]  There's actually a dashboard
[4616.36 --> 4617.38]  like managing this
[4617.38 --> 4618.38]  and comparing nicks
[4618.38 --> 4619.42]  to all these other
[4619.42 --> 4619.94]  like Debian
[4619.94 --> 4621.64]  and all these other systems
[4621.64 --> 4622.58]  and it's just like
[4622.58 --> 4624.72]  nicks is like so far
[4624.72 --> 4625.90]  removed from them.
[4626.04 --> 4626.94]  It's not even funny.
[4627.04 --> 4627.58]  They have things
[4627.58 --> 4628.16]  that are just like
[4628.16 --> 4630.00]  literally automatically
[4630.00 --> 4631.00]  updating packages
[4631.00 --> 4631.78]  in the repo.
[4632.60 --> 4633.54]  Where is this dashboard?
[4633.72 --> 4634.72]  Because I haven't seen it
[4634.72 --> 4635.78]  and I'm very curious.
[4635.78 --> 4637.68]  I think I put it
[4637.68 --> 4638.44]  in the release notes
[4638.44 --> 4639.72]  for the first release
[4639.72 --> 4640.52]  where I started.
[4640.96 --> 4642.20]  For bass 010?
[4642.78 --> 4643.14]  Yeah.
[4643.54 --> 4644.20]  There's something
[4644.20 --> 4645.24]  which I need to mention here.
[4645.78 --> 4646.32]  Zero to okay.
[4646.90 --> 4648.66]  DJ Daniel Jones,
[4649.10 --> 4650.74]  congrats for your first
[4650.74 --> 4651.80]  pull request to bass.
[4652.76 --> 4654.42]  We go a long, long way back
[4654.42 --> 4655.56]  and seeing you
[4655.56 --> 4656.68]  as the first contributor
[4656.68 --> 4657.28]  to bass
[4657.28 --> 4658.60]  put a smile on my face.
[4659.36 --> 4660.54]  So if you're listening to this
[4660.54 --> 4661.44]  and if you're not listening,
[4661.56 --> 4661.96]  that's okay.
[4662.02 --> 4663.00]  I make sure that you are.
[4663.10 --> 4663.62]  I've sent you a link
[4663.62 --> 4664.34]  with this episode.
[4664.94 --> 4666.40]  Maybe even the exact timestamp.
[4666.94 --> 4667.66]  Well done for
[4667.66 --> 4668.88]  doing the first contribution
[4668.88 --> 4669.22]  to bass.
[4669.30 --> 4670.28]  That was very nice to see.
[4670.90 --> 4671.08]  Cool.
[4671.44 --> 4673.42]  So I'm looking at 010.
[4674.34 --> 4675.06]  Zero to.
[4675.28 --> 4676.18]  I just put the link
[4676.18 --> 4677.02]  in the chat
[4677.02 --> 4677.62]  as a shortcut.
[4678.24 --> 4679.52]  My machine is really suffering.
[4680.20 --> 4680.92]  10 minutes?
[4681.02 --> 4681.80]  More than 10 minutes.
[4681.88 --> 4682.54]  15 minutes?
[4682.68 --> 4683.26]  More than 15.
[4683.42 --> 4684.42]  17 minutes I think.
[4684.66 --> 4685.46]  This is like a
[4685.46 --> 4687.94]  it's a 2018 MacBook Pro.
[4688.62 --> 4689.72]  So it's not even M1.
[4689.84 --> 4690.22]  Right.
[4690.74 --> 4690.96]  Yeah.
[4691.06 --> 4691.60]  Run definitely.
[4691.76 --> 4692.40]  Running that.
[4692.54 --> 4693.96]  Like couldn't you have run it
[4693.96 --> 4696.04]  in on like your Ryzen?
[4696.36 --> 4697.12]  Because then that's what you have
[4697.12 --> 4698.38]  like your Ryzen 7.
[4698.58 --> 4699.18]  I'm imagining.
[4699.50 --> 4700.18]  That was the plan.
[4700.54 --> 4701.48]  But when I did that,
[4701.54 --> 4702.14]  that's when like
[4702.14 --> 4703.02]  everything disconnected.
[4703.48 --> 4703.54]  So.
[4703.54 --> 4704.26]  Oh, I see.
[4704.32 --> 4705.34]  So when you SSH into it,
[4705.36 --> 4705.92]  it doesn't work
[4705.92 --> 4707.00]  if you were to SSH?
[4707.38 --> 4707.76]  I don't.
[4707.84 --> 4709.04]  I don't think I have SSH set up.
[4709.08 --> 4710.34]  I was just switching the display.
[4710.56 --> 4711.88]  I have like a KVM button,
[4712.26 --> 4713.16]  but I forgot that
[4713.16 --> 4713.98]  everything else
[4713.98 --> 4715.02]  is also flowing through it.
[4715.10 --> 4715.22]  So.
[4715.86 --> 4717.04]  Oh, I see what you mean.
[4717.10 --> 4717.38]  I see.
[4717.46 --> 4717.66]  I see.
[4717.74 --> 4717.86]  I see.
[4718.58 --> 4718.86]  Okay.
[4719.68 --> 4720.80]  Repology.org.
[4721.68 --> 4722.08]  Wow.
[4722.68 --> 4723.44]  That is impressive.
[4723.56 --> 4724.38]  Number of packages
[4724.38 --> 4725.20]  in repository.
[4726.42 --> 4728.20]  Number of fresh packages.
[4728.52 --> 4729.36]  I see what you mean.
[4730.02 --> 4730.92]  I see what you mean.
[4731.92 --> 4732.32]  Deports.
[4732.52 --> 4732.92]  Fedora.
[4733.06 --> 4733.94]  Ubuntu 20.04.
[4733.94 --> 4735.08]  I'm looking for
[4735.08 --> 4735.94]  the number of packages,
[4736.74 --> 4737.72]  number of freshness.
[4737.72 --> 4739.70]  and I can't find
[4739.70 --> 4740.44]  in that graph.
[4740.58 --> 4741.50]  I can't find Nix
[4741.50 --> 4742.18]  and I don't think
[4742.18 --> 4742.80]  I can search
[4742.80 --> 4743.80]  because it's generated.
[4743.98 --> 4744.32]  It's rendered.
[4744.96 --> 4745.70]  Oh, it should be
[4745.70 --> 4747.10]  very top right
[4747.10 --> 4748.24]  on the first graph.
[4748.50 --> 4749.42]  You'll see Nix packages
[4749.42 --> 4749.92]  unstable.
[4750.22 --> 4750.84]  I can see that
[4750.84 --> 4752.04]  and yes, stable.
[4752.16 --> 4753.18]  But on the second one,
[4753.96 --> 4754.50]  yeah, what is that
[4754.50 --> 4755.02]  by the way?
[4755.90 --> 4756.90]  Zoomed in
[4756.90 --> 4758.34]  onto smaller repositories.
[4758.70 --> 4759.18]  Oh.
[4759.72 --> 4760.20]  Oh.
[4760.58 --> 4761.28]  It's actually
[4761.28 --> 4762.20]  outside of that.
[4762.60 --> 4763.38]  So that's like
[4763.38 --> 4764.08]  a zoom in.
[4764.20 --> 4765.02]  It's outside of that.
[4765.16 --> 4765.46]  Wow.
[4765.86 --> 4766.10]  Yeah.
[4766.28 --> 4767.14]  And that's zoomed
[4767.14 --> 4767.82]  in some more.
[4768.06 --> 4769.34]  Homebrew casks.
[4770.30 --> 4770.74]  Wow.
[4770.82 --> 4771.96]  That's so far away.
[4772.64 --> 4773.52]  That's so far away.
[4774.12 --> 4774.46]  Okay.
[4774.70 --> 4775.64]  That's really cool.
[4776.46 --> 4776.98]  To be fair,
[4777.20 --> 4777.58]  I think
[4777.58 --> 4779.10]  there's a lot
[4779.10 --> 4779.62]  of automation
[4779.62 --> 4780.30]  driving this.
[4780.44 --> 4781.24]  There's probably like
[4781.24 --> 4782.26]  maybe they're representing
[4782.26 --> 4784.22]  Python libraries
[4784.22 --> 4785.26]  and things like that
[4785.26 --> 4786.14]  as Nix packages.
[4786.28 --> 4786.72]  I'm not sure.
[4786.94 --> 4787.48]  But there's
[4787.48 --> 4788.62]  it's still
[4788.62 --> 4789.70]  usually
[4789.70 --> 4790.44]  when I want
[4790.44 --> 4791.10]  some software
[4791.10 --> 4792.34]  it's in there.
[4792.68 --> 4793.62]  It's up to date.
[4793.96 --> 4795.08]  If something shipped
[4795.08 --> 4796.14]  it's been up to date
[4796.14 --> 4796.78]  as of like
[4796.78 --> 4798.22]  a few days after it shipped.
[4798.54 --> 4798.74]  Yeah.
[4798.80 --> 4799.56]  Which is really
[4799.56 --> 4800.40]  what I'm looking for
[4800.40 --> 4801.44]  when I'm trying to build
[4801.44 --> 4802.04]  images
[4802.04 --> 4804.30]  and run things
[4804.30 --> 4804.78]  with base
[4804.78 --> 4805.58]  is I want something
[4805.58 --> 4806.16]  that's just like
[4806.16 --> 4807.02]  give me the latest version.
[4807.32 --> 4808.16]  I don't care about
[4808.16 --> 4808.92]  sticking to Debian.
[4809.08 --> 4809.66]  If I wanted Debian
[4809.66 --> 4810.40]  I could just use
[4810.40 --> 4811.60]  Debian and apt-get install
[4811.60 --> 4811.94]  or whatever.
[4812.20 --> 4813.72]  But the nice thing
[4813.72 --> 4814.90]  is that Nix also gives you
[4814.90 --> 4816.88]  precise reproducible builds.
[4818.42 --> 4819.70]  So interestingly
[4819.70 --> 4821.24]  I have
[4821.24 --> 4822.16]  my Linux system
[4822.16 --> 4823.20]  I switched it to
[4823.20 --> 4824.12]  and I have like
[4824.12 --> 4824.72]  a couple of
[4824.72 --> 4825.96]  workstations.
[4826.22 --> 4826.82]  One of them is
[4826.82 --> 4828.44]  this Nix OS host
[4828.44 --> 4830.56]  it's an AMD Ryzen 7
[4830.56 --> 4831.48]  it's a completely
[4831.48 --> 4832.36]  Fanda system.
[4832.94 --> 4834.14]  I really liked
[4834.14 --> 4834.60]  like the whole
[4834.60 --> 4835.22]  like configuring
[4835.22 --> 4836.22]  it was really nice
[4836.22 --> 4837.00]  it has like a desktop
[4837.00 --> 4837.66]  interface.
[4838.08 --> 4839.18]  I just used some dashboards
[4839.18 --> 4839.76]  on it
[4839.76 --> 4840.72]  Grafana dashboards
[4840.72 --> 4842.00]  as I monitor my connection
[4842.00 --> 4843.02]  my internet connection
[4843.02 --> 4843.86]  things like that.
[4844.44 --> 4845.40]  On a Mac
[4845.40 --> 4847.28]  I tried installing Nix
[4847.28 --> 4848.16]  and I have tried
[4848.16 --> 4848.86]  running it for about
[4848.86 --> 4849.56]  seven months.
[4850.60 --> 4851.80]  But it has this weird
[4851.80 --> 4852.72]  I don't know
[4852.72 --> 4853.88]  like I couldn't get
[4853.88 --> 4855.24]  updates to work
[4855.24 --> 4855.94]  consistently
[4855.94 --> 4856.94]  updating
[4856.94 --> 4858.26]  the channel
[4858.26 --> 4859.36]  didn't work.
[4859.92 --> 4860.88]  There's this Darwin
[4860.88 --> 4862.40]  like extension
[4862.40 --> 4863.36]  or something like that
[4863.36 --> 4864.24]  you need to install
[4864.24 --> 4865.78]  that was a bit weird.
[4866.24 --> 4867.52]  So my question to you
[4867.52 --> 4868.00]  is do you use
[4868.00 --> 4868.48]  Nix
[4868.48 --> 4869.76]  on Mac?
[4870.80 --> 4871.56]  I actually
[4871.56 --> 4873.02]  for my development
[4873.02 --> 4873.78]  I use WSL
[4873.78 --> 4874.66]  so I just use
[4874.66 --> 4876.04]  Nix within Linux
[4876.04 --> 4877.08]  within Windows.
[4877.62 --> 4878.16]  I see
[4878.16 --> 4879.06]  okay that makes sense
[4879.06 --> 4880.20]  okay so you have
[4880.20 --> 4881.16]  basically all three
[4881.16 --> 4882.30]  on your Mac.
[4882.72 --> 4884.12]  The host is Mac?
[4884.32 --> 4885.06]  Host is Windows.
[4885.36 --> 4886.12]  The host is Windows?
[4886.46 --> 4887.28]  No host is Windows
[4887.28 --> 4887.96]  yeah yeah yeah.
[4888.02 --> 4888.52]  Okay okay.
[4888.76 --> 4889.98]  I'm just using Mac right now
[4889.98 --> 4890.78]  because it has
[4890.78 --> 4891.78]  the Opal software
[4891.78 --> 4892.50]  for my webcam.
[4893.04 --> 4894.14]  Oh I see what you mean
[4894.14 --> 4894.78]  okay okay okay.
[4894.82 --> 4895.76]  So the whole reason
[4895.76 --> 4896.92]  for this being horrendously
[4896.92 --> 4898.20]  slow and like fumbling
[4898.20 --> 4898.88]  through all this
[4898.88 --> 4900.10]  is that Opal doesn't
[4900.10 --> 4901.16]  have software for Windows
[4901.16 --> 4901.82]  right now.
[4901.82 --> 4902.78]  Yeah I see
[4902.78 --> 4904.00]  okay that makes sense
[4904.00 --> 4904.88]  that makes sense okay
[4904.88 --> 4905.78]  but you're like
[4905.78 --> 4907.00]  Windows is like
[4907.00 --> 4908.32]  your host operating system
[4908.32 --> 4910.02]  in that you run Linux
[4910.02 --> 4911.76]  and all development works
[4911.76 --> 4912.98]  happens in Linux
[4912.98 --> 4913.74]  okay okay
[4913.74 --> 4914.40]  that makes sense
[4914.40 --> 4915.64]  and Linux
[4915.64 --> 4916.96]  I'm assuming you're using
[4916.96 --> 4917.42]  Nix OS
[4917.42 --> 4919.06]  that is your host
[4919.06 --> 4920.08]  so that's your
[4920.08 --> 4921.22]  Linux operating system.
[4921.96 --> 4922.90]  It's Ubuntu
[4922.90 --> 4924.16]  with Nix
[4924.16 --> 4926.18]  just for the package manager.
[4926.40 --> 4926.92]  Interesting.
[4927.14 --> 4927.80]  It's honestly
[4927.80 --> 4928.74]  pretty cobbled together
[4928.74 --> 4929.98]  I only started
[4929.98 --> 4930.78]  using Nix
[4930.78 --> 4931.76]  like once
[4931.76 --> 4932.26]  I had already
[4932.26 --> 4932.84]  started building
[4932.84 --> 4933.14]  base
[4933.14 --> 4933.74]  so I was already
[4933.74 --> 4934.74]  using Open2
[4934.74 --> 4935.06]  and everything
[4935.06 --> 4935.48]  for that
[4935.48 --> 4936.56]  so I just
[4936.56 --> 4937.64]  I wanted to see
[4937.64 --> 4938.18]  how Nix
[4938.18 --> 4938.96]  might interplay
[4938.96 --> 4939.56]  with base
[4939.56 --> 4940.12]  I guess I never
[4940.12 --> 4940.94]  finished that thought
[4940.94 --> 4941.86]  by the way
[4941.86 --> 4942.80]  which is that like
[4942.80 --> 4943.98]  I don't want Nix
[4943.98 --> 4944.80]  to be a dependency
[4944.80 --> 4945.32]  of base
[4945.32 --> 4946.28]  because that would
[4946.28 --> 4946.94]  be terrifying
[4946.94 --> 4947.40]  to people
[4947.40 --> 4947.86]  to have to
[4947.86 --> 4948.54]  not only learn
[4948.54 --> 4949.72]  my esoteric Lisp
[4949.72 --> 4950.52]  but learn
[4950.52 --> 4951.64]  this esoteric
[4951.64 --> 4952.40]  Nix language
[4952.40 --> 4953.06]  beneath it
[4953.06 --> 4954.52]  so it really
[4954.52 --> 4955.56]  only leverages it
[4955.56 --> 4956.26]  in so far
[4956.26 --> 4957.58]  as I
[4957.58 --> 4958.28]  as the project
[4958.28 --> 4958.82]  maintainer
[4958.82 --> 4959.40]  use Nix
[4959.40 --> 4959.86]  to build
[4959.86 --> 4960.60]  the images
[4960.60 --> 4962.18]  that feed
[4962.18 --> 4962.78]  into base
[4962.78 --> 4963.86]  and I use base
[4963.86 --> 4964.68]  to build those images
[4964.68 --> 4965.40]  using Nix
[4965.40 --> 4966.08]  so it's
[4966.08 --> 4967.54]  base just sees Nix
[4967.54 --> 4968.40]  as another command
[4968.40 --> 4968.82]  to run
[4968.82 --> 4969.24]  I see
[4969.24 --> 4969.94]  I'm just running
[4969.94 --> 4970.52]  Nix build
[4970.52 --> 4971.62]  and then that produces
[4971.62 --> 4973.00]  an OCI image tarball
[4973.00 --> 4973.98]  and then I pass that
[4973.98 --> 4974.66]  to another thunk
[4974.66 --> 4975.78]  because you can use
[4975.78 --> 4977.06]  thunks that use
[4977.06 --> 4978.28]  archives built
[4978.28 --> 4979.00]  from other thunks
[4979.00 --> 4979.68]  as an image
[4979.68 --> 4980.44]  right
[4980.44 --> 4981.26]  one other thing
[4981.26 --> 4981.96]  I've been experimenting
[4981.96 --> 4982.56]  with though
[4982.56 --> 4983.48]  is because Nix
[4983.48 --> 4984.08]  is so good
[4984.08 --> 4985.06]  for just like
[4985.06 --> 4985.94]  pulling in packages
[4985.94 --> 4986.90]  as dependencies
[4986.90 --> 4988.42]  and a lot of
[4988.42 --> 4989.36]  images that people
[4989.36 --> 4990.10]  build for CI
[4990.10 --> 4990.92]  are just
[4990.92 --> 4992.34]  I need Ruby
[4992.34 --> 4992.98]  installed
[4992.98 --> 4993.78]  or I need like
[4993.78 --> 4995.10]  but I don't need
[4995.10 --> 4995.52]  just Ruby
[4995.52 --> 4996.30]  I need like
[4996.30 --> 4997.38]  Ruby plus Git
[4997.38 --> 4998.56]  plus UPX
[4998.56 --> 4999.26]  or like whatever
[4999.26 --> 5000.52]  tool chain I use
[5000.52 --> 5001.96]  because it's pretty
[5001.96 --> 5002.52]  rare that you can
[5002.52 --> 5003.64]  just use Ruby
[5003.64 --> 5004.22]  off the shelf
[5004.22 --> 5004.70]  and have that
[5004.70 --> 5005.64]  provide like the
[5005.64 --> 5006.94]  library Ruby image
[5006.94 --> 5007.46]  and have that
[5007.46 --> 5007.94]  provide everything
[5007.94 --> 5008.32]  you need
[5008.32 --> 5009.82]  so one thing
[5009.82 --> 5010.50]  I'm planning
[5010.50 --> 5011.14]  to experiment
[5011.14 --> 5012.42]  with is having
[5012.42 --> 5014.08]  base just like
[5014.08 --> 5014.94]  it starts build kit
[5014.94 --> 5016.00]  have it start
[5016.00 --> 5017.02]  a Nixery host
[5017.02 --> 5018.28]  and then you can
[5018.28 --> 5018.80]  just do like
[5018.80 --> 5019.86]  from Nix
[5019.86 --> 5020.78]  slash GH
[5020.78 --> 5021.92]  slash Ruby
[5021.92 --> 5022.68]  slash go
[5022.68 --> 5023.60]  and it'll just like
[5023.60 --> 5024.32]  build an image
[5024.32 --> 5024.82]  on the fly
[5024.82 --> 5025.42]  with all those
[5025.42 --> 5025.82]  dependencies
[5025.82 --> 5027.38]  I want that
[5027.38 --> 5028.10]  yeah same
[5028.10 --> 5029.28]  that is so cool
[5029.28 --> 5030.36]  oh wow
[5030.36 --> 5031.58]  that would be so cool
[5031.58 --> 5032.08]  yeah
[5032.08 --> 5033.08]  no more like
[5033.08 --> 5033.50]  building
[5033.50 --> 5034.46]  throwaway images
[5034.46 --> 5035.38]  yeah especially
[5035.38 --> 5036.38]  I use Nixery
[5036.38 --> 5037.20]  dot dev often
[5037.20 --> 5038.18]  especially in demos
[5038.18 --> 5039.70]  so if I'm trying
[5039.70 --> 5041.10]  to put together
[5041.10 --> 5042.52]  a bunch of tools
[5042.52 --> 5043.84]  ad hoc
[5043.84 --> 5044.48]  arbitrary
[5044.48 --> 5044.92]  I don't know
[5044.92 --> 5045.54]  what they are
[5045.54 --> 5047.54]  I get this
[5047.54 --> 5048.48]  Nixery dev image
[5048.48 --> 5049.02]  which has all
[5049.02 --> 5049.40]  the tools
[5049.40 --> 5050.44]  that I need
[5050.44 --> 5051.40]  and that's my
[5051.40 --> 5052.08]  starting point
[5052.08 --> 5053.20]  I've done that
[5053.20 --> 5053.56]  often
[5053.56 --> 5054.92]  and it works
[5054.92 --> 5055.42]  so well
[5055.42 --> 5055.78]  it's like
[5055.78 --> 5056.42]  why don't
[5056.42 --> 5056.86]  more people
[5056.86 --> 5057.52]  do this
[5057.52 --> 5058.04]  yeah
[5058.04 --> 5058.44]  but again
[5058.44 --> 5059.16]  Nixery dot dev
[5059.16 --> 5059.56]  is like
[5059.56 --> 5060.22]  best effort
[5060.22 --> 5060.64]  basis
[5060.64 --> 5061.12]  and okay
[5061.12 --> 5061.52]  Vincent
[5061.52 --> 5061.98]  we have to
[5061.98 --> 5062.46]  talk again
[5062.46 --> 5063.34]  we really
[5063.34 --> 5064.22]  and I think
[5064.22 --> 5064.62]  that you need
[5064.62 --> 5065.22]  to talk to Alex
[5065.22 --> 5065.46]  too
[5065.46 --> 5066.38]  because there's
[5066.38 --> 5067.06]  something really
[5067.06 --> 5067.90]  cool about this
[5067.90 --> 5068.32]  and if you can
[5068.32 --> 5069.16]  run it locally
[5069.16 --> 5070.62]  because that's
[5070.62 --> 5071.06]  what I'm hearing
[5071.06 --> 5071.54]  from you
[5071.54 --> 5072.42]  if you can run
[5072.42 --> 5072.94]  Nixery dev
[5072.94 --> 5074.92]  locally via base
[5074.92 --> 5076.30]  oh my goodness
[5076.30 --> 5077.36]  me I want that
[5077.36 --> 5077.70]  yeah
[5077.70 --> 5078.48]  because then
[5078.48 --> 5078.86]  like
[5078.86 --> 5080.50]  what keeps
[5080.50 --> 5081.10]  biting me
[5081.10 --> 5081.96]  is the freaking
[5081.96 --> 5083.00]  Docker hub rate
[5083.00 --> 5083.34]  limits
[5083.34 --> 5084.60]  they're so low
[5084.60 --> 5084.94]  now
[5084.94 --> 5085.74]  oh yes
[5085.74 --> 5087.46]  tell me about it
[5087.46 --> 5087.84]  oh hey
[5087.84 --> 5088.36]  it finished
[5088.36 --> 5088.68]  something
[5088.68 --> 5089.44]  okay
[5089.44 --> 5090.30]  okay
[5090.30 --> 5091.38]  so by the way
[5091.38 --> 5092.00]  dear listener
[5092.00 --> 5092.96]  all this time
[5092.96 --> 5093.56]  we have been
[5093.56 --> 5093.96]  waiting
[5093.96 --> 5097.24]  for a base
[5097.24 --> 5098.00]  build
[5098.00 --> 5099.14]  at a base
[5099.14 --> 5099.46]  release
[5099.46 --> 5100.32]  0.9.0
[5100.32 --> 5101.30]  and we've been
[5101.30 --> 5101.98]  filling time
[5101.98 --> 5103.02]  and I'm so glad
[5103.02 --> 5103.36]  we did
[5103.36 --> 5103.94]  because we talked
[5103.94 --> 5104.58]  about so many
[5104.58 --> 5105.32]  interesting things
[5105.32 --> 5107.08]  so let us
[5107.08 --> 5107.84]  not get distracted
[5107.84 --> 5108.50]  by the release
[5108.50 --> 5109.72]  and please continue
[5109.72 --> 5110.26]  because this is
[5110.26 --> 5111.04]  super interesting
[5111.04 --> 5111.70]  what was it
[5111.70 --> 5112.04]  oh yeah
[5112.04 --> 5113.18]  so Docker hub
[5113.18 --> 5113.82]  and the rate
[5113.82 --> 5114.14]  limits
[5114.14 --> 5115.12]  it keeps making
[5115.12 --> 5115.84]  my tests fail
[5115.84 --> 5116.40]  because
[5116.40 --> 5118.04]  my tests run
[5118.04 --> 5118.66]  like they don't
[5118.66 --> 5119.16]  they don't have
[5119.16 --> 5119.68]  any authentication
[5119.68 --> 5120.22]  set up
[5120.22 --> 5120.68]  so it's always
[5120.68 --> 5121.30]  just using the
[5121.30 --> 5122.00]  anonymous
[5122.00 --> 5123.16]  rate limit
[5123.16 --> 5123.66]  which is like
[5123.66 --> 5125.38]  100 calls
[5125.38 --> 5126.58]  per 6 hours
[5126.58 --> 5127.08]  or something
[5127.08 --> 5127.38]  like
[5127.38 --> 5128.64]  which is
[5128.64 --> 5129.62]  sounds like a lot
[5129.62 --> 5130.26]  but it's really
[5130.26 --> 5130.98]  not when you're
[5130.98 --> 5131.80]  running tests
[5131.80 --> 5132.76]  that hit Docker hub
[5132.76 --> 5133.68]  and you're
[5133.68 --> 5134.98]  quickly iterating
[5134.98 --> 5135.58]  so like
[5135.58 --> 5136.30]  it would be great
[5136.30 --> 5136.94]  to use
[5136.94 --> 5137.98]  nix3.dev
[5137.98 --> 5138.60]  but then yeah
[5138.60 --> 5139.16]  I don't want to
[5139.16 --> 5139.46]  burden
[5139.46 --> 5140.18]  Vincent
[5140.18 --> 5140.72]  right
[5140.72 --> 5141.58]  Vincent
[5141.58 --> 5141.82]  yeah
[5141.82 --> 5142.16]  Vincent
[5142.16 --> 5142.54]  yeah
[5142.54 --> 5143.50]  I don't want
[5143.50 --> 5144.02]  to burden him
[5144.02 --> 5144.44]  with like
[5144.44 --> 5145.08]  me depending
[5145.08 --> 5145.42]  on it
[5145.42 --> 5146.00]  for production
[5146.00 --> 5146.62]  and I don't
[5146.62 --> 5146.88]  want to be
[5146.88 --> 5147.58]  like hitting
[5147.58 --> 5148.62]  his registry
[5148.62 --> 5149.24]  and adding
[5149.24 --> 5149.70]  load to it
[5149.70 --> 5150.10]  but if you're
[5150.10 --> 5150.46]  just running
[5150.46 --> 5150.86]  it locally
[5150.86 --> 5151.64]  then that solves
[5151.64 --> 5152.20]  both problems
[5152.20 --> 5153.28]  because there's
[5153.28 --> 5154.06]  no rate limit
[5154.06 --> 5155.20]  it should be
[5155.20 --> 5155.80]  much faster
[5155.80 --> 5156.34]  than this
[5156.34 --> 5157.54]  this entire time
[5157.54 --> 5158.10]  we've been talking
[5158.10 --> 5158.76]  we've just been
[5158.76 --> 5159.60]  waiting for nix
[5159.60 --> 5160.54]  to build and
[5160.54 --> 5162.08]  export an image
[5162.08 --> 5163.20]  which it would
[5163.20 --> 5163.90]  be much faster
[5163.90 --> 5164.54]  on my machine
[5164.54 --> 5165.62]  but what would
[5165.62 --> 5166.24]  be great is if I
[5166.24 --> 5166.72]  didn't even have
[5166.72 --> 5167.14]  to do this
[5167.14 --> 5168.00]  because nix3
[5168.00 --> 5169.16]  does all the
[5169.16 --> 5169.84]  like magic
[5169.84 --> 5170.88]  stuff with layers
[5170.88 --> 5171.40]  where you don't
[5171.40 --> 5172.00]  have to build
[5172.00 --> 5172.56]  and export
[5172.56 --> 5173.18]  and unpack
[5173.18 --> 5174.70]  because it all
[5174.70 --> 5175.16]  just happens
[5175.16 --> 5176.00]  registry side
[5176.00 --> 5178.20]  now I have
[5178.20 --> 5178.64]  to say
[5178.64 --> 5179.78]  that I've
[5179.78 --> 5180.52]  seen in our
[5180.52 --> 5180.86]  CI
[5180.86 --> 5181.84]  a dagger
[5181.84 --> 5183.76]  various failures
[5183.76 --> 5185.26]  related to
[5185.26 --> 5186.58]  images
[5186.58 --> 5188.06]  images on
[5188.06 --> 5188.74]  being pulled
[5188.74 --> 5189.64]  from registries
[5189.64 --> 5190.36]  it's usually
[5190.36 --> 5191.32]  Docker Hub
[5191.32 --> 5192.70]  but also
[5192.70 --> 5193.38]  caches
[5193.38 --> 5195.94]  so registries
[5195.94 --> 5196.54]  and caches
[5196.54 --> 5197.36]  I think registries
[5197.36 --> 5197.94]  are a type of
[5197.94 --> 5198.58]  cache that's the
[5198.58 --> 5198.96]  way I see
[5198.96 --> 5199.22]  them
[5199.22 --> 5201.18]  they are
[5201.18 --> 5202.06]  like once you
[5202.06 --> 5202.68]  start depending
[5202.68 --> 5203.16]  on them
[5203.16 --> 5203.80]  and once you
[5203.80 --> 5204.34]  start running
[5204.34 --> 5204.96]  like many
[5204.96 --> 5205.56]  many builds
[5205.56 --> 5205.92]  through
[5205.92 --> 5206.46]  and you have
[5206.46 --> 5206.84]  many pull
[5206.84 --> 5207.28]  requests
[5207.28 --> 5207.98]  and all that
[5207.98 --> 5208.96]  you start
[5208.96 --> 5209.98]  realizing basically
[5209.98 --> 5210.92]  how much
[5210.92 --> 5212.02]  degradation
[5212.02 --> 5212.80]  there is in
[5212.80 --> 5213.00]  them
[5213.00 --> 5214.32]  because it's
[5214.32 --> 5215.26]  and the way
[5215.26 --> 5216.34]  we see them
[5216.34 --> 5217.24]  is flakes
[5217.24 --> 5218.66]  run the test
[5218.66 --> 5219.12]  again it
[5219.12 --> 5219.44]  passes
[5219.44 --> 5220.66]  and you just
[5220.66 --> 5221.38]  get like errors
[5221.38 --> 5222.06]  from like
[5222.06 --> 5223.22]  endpoints
[5223.22 --> 5224.66]  so if you
[5224.66 --> 5225.14]  could have
[5225.14 --> 5225.80]  that somewhere
[5225.80 --> 5226.84]  close to
[5226.84 --> 5227.60]  where basically
[5227.60 --> 5228.18]  like where the
[5228.18 --> 5228.84]  compute is
[5228.84 --> 5229.94]  and you wouldn't
[5229.94 --> 5230.52]  need to do
[5230.52 --> 5231.00]  any of the
[5231.00 --> 5231.84]  network transfer
[5231.84 --> 5232.28]  that would be
[5232.28 --> 5233.02]  so much
[5233.02 --> 5233.38]  quicker
[5233.38 --> 5234.84]  because network
[5234.84 --> 5236.28]  has its own
[5236.28 --> 5236.84]  properties
[5236.84 --> 5238.34]  which is
[5238.34 --> 5238.76]  latency
[5238.76 --> 5240.02]  which is
[5240.02 --> 5241.54]  packet loss
[5241.54 --> 5242.68]  which is like
[5242.68 --> 5243.34]  all sorts of
[5243.34 --> 5243.68]  things
[5243.68 --> 5244.74]  and you've
[5244.74 --> 5245.24]  you've heard me
[5245.24 --> 5246.24]  talk about that
[5246.24 --> 5246.70]  for a while
[5246.70 --> 5248.26]  but Alex and
[5248.26 --> 5248.62]  Vincent
[5248.62 --> 5249.72]  hmm
[5249.72 --> 5250.86]  you gave me
[5250.86 --> 5251.36]  a bunch of
[5251.36 --> 5252.02]  ideas there
[5252.02 --> 5253.28]  yeah
[5253.28 --> 5254.58]  episode 37
[5254.58 --> 5255.54]  building fully
[5255.54 --> 5256.40]  declarative systems
[5256.40 --> 5256.92]  with Nix
[5256.92 --> 5258.32]  that was the
[5258.32 --> 5258.92]  episode when we
[5258.92 --> 5259.50]  talked and I
[5259.50 --> 5260.36]  think I think
[5260.36 --> 5260.80]  we should talk
[5260.80 --> 5261.40]  again because
[5261.40 --> 5262.12]  there is something
[5262.12 --> 5262.96]  really interesting
[5262.96 --> 5263.28]  here
[5263.28 --> 5264.74]  okay let me see
[5264.74 --> 5265.48]  what we can do
[5265.48 --> 5266.26]  there because I'm
[5266.26 --> 5267.04]  really excited about
[5267.04 --> 5267.76]  this and I
[5267.76 --> 5268.68]  definitely want this
[5268.68 --> 5270.06]  and we need to
[5270.06 --> 5270.52]  see how to
[5270.52 --> 5271.24]  continue my
[5271.24 --> 5272.02]  Nix OS journey
[5272.02 --> 5272.60]  because I'm
[5272.60 --> 5273.74]  I'm almost there
[5273.74 --> 5274.34]  but there's like a
[5274.34 --> 5274.98]  couple of things
[5274.98 --> 5275.80]  which I'm still
[5275.80 --> 5276.94]  missing for
[5276.94 --> 5278.16]  example putting on
[5278.16 --> 5278.92]  the version control
[5278.92 --> 5279.40]  everything
[5279.40 --> 5281.66]  the thing that we
[5281.66 --> 5282.34]  tried to do
[5282.34 --> 5284.42]  happened and I
[5284.42 --> 5284.92]  will let Alex
[5284.92 --> 5285.44]  tell us more
[5285.44 --> 5285.92]  about it
[5285.92 --> 5287.94]  we are preparing
[5287.94 --> 5288.52]  to wrap up
[5288.52 --> 5289.76]  I'm pretty sure
[5289.76 --> 5290.48]  that we could go
[5290.48 --> 5291.76]  easy for another
[5291.76 --> 5293.02]  hour like start
[5293.02 --> 5293.82]  unpacking some of
[5293.82 --> 5294.40]  the things there
[5294.40 --> 5294.98]  is so much
[5294.98 --> 5296.92]  there I'm super
[5296.92 --> 5297.50]  excited about
[5297.50 --> 5299.18]  bass I loved
[5299.18 --> 5300.12]  concourse for a
[5300.12 --> 5300.80]  long long time
[5300.80 --> 5303.36]  and it could have
[5303.36 --> 5304.06]  been so much
[5304.06 --> 5305.84]  more bass a
[5305.84 --> 5307.10]  new life I
[5307.10 --> 5308.26]  think I'm
[5308.26 --> 5309.66]  starting to see a
[5309.66 --> 5310.10]  lot of the
[5310.10 --> 5310.88]  similarities and
[5310.88 --> 5311.54]  thank you Alex for
[5311.54 --> 5312.48]  helping me see that
[5312.48 --> 5314.80]  but over to you as
[5314.80 --> 5315.76]  we prepare to wrap
[5315.76 --> 5317.04]  up like how
[5317.04 --> 5317.58]  would you like us
[5317.58 --> 5318.30]  to end this
[5318.30 --> 5319.80]  great conversation
[5319.80 --> 5321.32]  yeah I don't know
[5321.32 --> 5322.82]  check out bass if
[5322.82 --> 5323.18]  you want to have
[5323.18 --> 5324.04]  fun if you're
[5324.04 --> 5325.00]  interested in if
[5325.00 --> 5325.82]  you've been curious
[5325.82 --> 5327.12]  about like building
[5327.12 --> 5328.12]  a language but
[5328.12 --> 5329.84]  felt like the bar
[5329.84 --> 5330.46]  to that was too
[5330.46 --> 5332.04]  high bass is a
[5332.04 --> 5332.60]  great place to
[5332.60 --> 5333.24]  experiment with
[5333.24 --> 5333.88]  different ideas
[5333.88 --> 5335.32]  because their
[5335.32 --> 5336.08]  performance concerns
[5336.08 --> 5337.00]  are much lower
[5337.00 --> 5337.98]  than in other
[5337.98 --> 5338.86]  traditional languages
[5338.86 --> 5342.44]  if you feel like
[5342.44 --> 5343.64]  you're tired of
[5343.64 --> 5344.80]  YAML and tired
[5344.80 --> 5345.34]  of templating
[5345.34 --> 5345.74]  YAML
[5345.74 --> 5347.20]  and tired of
[5347.20 --> 5347.96]  gluing together
[5347.96 --> 5349.84]  bespoke abstractions
[5349.84 --> 5350.44]  and would rather
[5350.44 --> 5351.64]  try to glue
[5351.64 --> 5352.68]  together bespoke
[5352.68 --> 5354.14]  CLIs in a
[5354.14 --> 5354.94]  bespoke language
[5354.94 --> 5356.58]  then yeah
[5356.58 --> 5357.24]  check it out
[5357.24 --> 5358.16]  latest version
[5358.16 --> 5359.26]  has the most
[5359.26 --> 5359.94]  important release
[5359.94 --> 5360.72]  in a long time
[5360.72 --> 5361.44]  rave mode
[5361.44 --> 5363.32]  press R
[5363.32 --> 5364.90]  and just keep
[5364.90 --> 5365.62]  vibing from
[5365.62 --> 5366.32]  program to
[5366.32 --> 5366.70]  program
[5366.70 --> 5367.94]  that's really
[5367.94 --> 5368.26]  cool
[5368.26 --> 5369.80]  yeah so R
[5369.80 --> 5370.74]  rave connects
[5370.74 --> 5371.44]  to your Spotify
[5371.44 --> 5372.52]  the thing that
[5372.52 --> 5373.04]  we've been trying
[5373.04 --> 5373.48]  to do
[5373.48 --> 5374.42]  090
[5374.42 --> 5375.44]  that's amazing
[5375.44 --> 5376.20]  thank you very
[5376.20 --> 5376.94]  much for
[5376.94 --> 5377.62]  keeping the
[5377.62 --> 5378.14]  release for
[5378.14 --> 5378.68]  when we
[5378.68 --> 5379.60]  record it
[5379.60 --> 5380.36]  it made it
[5380.36 --> 5380.88]  feel so much
[5380.88 --> 5381.42]  more special
[5381.42 --> 5382.26]  I got very
[5382.26 --> 5382.88]  excited about
[5382.88 --> 5383.40]  it so
[5383.40 --> 5384.08]  if only it
[5384.08 --> 5384.62]  didn't take an
[5384.62 --> 5385.26]  hour because
[5385.26 --> 5385.80]  the stupid
[5385.80 --> 5386.22]  MacBook
[5386.22 --> 5387.76]  that's okay
[5387.76 --> 5388.88]  computers you know
[5388.88 --> 5390.02]  we know how to do
[5390.02 --> 5390.60]  it better next
[5390.60 --> 5391.70]  time but this
[5391.70 --> 5392.76]  was really
[5392.76 --> 5394.22]  really it was
[5394.22 --> 5394.94]  it was real fun
[5394.94 --> 5395.54]  let's put it that
[5395.54 --> 5396.16]  way so I think
[5396.16 --> 5397.32]  on that from
[5397.32 --> 5398.00]  that perspective
[5398.00 --> 5399.20]  I think you've
[5399.20 --> 5399.72]  accomplished your
[5399.72 --> 5400.96]  goal to keep
[5400.96 --> 5401.78]  it fun to
[5401.78 --> 5402.40]  keep it light
[5402.40 --> 5403.40]  and hopefully
[5403.40 --> 5403.88]  it will be the
[5403.88 --> 5404.52]  same for others
[5404.52 --> 5405.78]  an hour of fun
[5405.78 --> 5406.30]  that's the
[5406.30 --> 5407.14]  an hour of fun
[5407.14 --> 5408.00]  positive way to
[5408.00 --> 5408.52]  look at it
[5408.52 --> 5409.74]  well we are
[5409.74 --> 5411.06]  nerds what can
[5411.06 --> 5411.76]  I say you know
[5411.76 --> 5412.26]  that's like
[5412.26 --> 5412.98]  Jared's word
[5412.98 --> 5413.64]  like we are
[5413.64 --> 5415.08]  nerds so this
[5415.08 --> 5415.70]  is the fun that
[5415.70 --> 5416.88]  we have so
[5416.88 --> 5418.58]  Alex thank you
[5418.58 --> 5419.12]  much for joining
[5419.12 --> 5419.86]  me I'm looking
[5419.86 --> 5420.44]  forward to next
[5420.44 --> 5421.16]  time and I
[5421.16 --> 5421.76]  look forward to
[5421.76 --> 5422.24]  what happens
[5422.24 --> 5423.56]  with bass this
[5423.56 --> 5424.06]  is amazing
[5424.06 --> 5424.80]  thank you
[5424.80 --> 5425.46]  thanks for
[5425.46 --> 5425.86]  having me
[5425.86 --> 5430.14]  thank you for
[5430.14 --> 5430.92]  tuning into
[5430.92 --> 5431.66]  another episode
[5431.66 --> 5432.24]  of ship it
[5432.24 --> 5433.24]  check out our
[5433.24 --> 5434.02]  other podcasts
[5434.02 --> 5434.88]  for developers
[5434.88 --> 5436.32]  at changelog.com
[5436.32 --> 5437.50]  slash master
[5437.50 --> 5438.82]  you can connect
[5438.82 --> 5439.42]  with like-minded
[5439.42 --> 5440.36]  developers via
[5440.36 --> 5441.44]  changelog.com
[5441.44 --> 5442.66]  slash community
[5442.66 --> 5443.96]  thank you fastly
[5443.96 --> 5444.94]  for the worldwide
[5444.94 --> 5445.62]  low latency
[5445.62 --> 5446.72]  changelog.com
[5446.72 --> 5447.78]  our listeners
[5447.78 --> 5449.12]  love those
[5449.12 --> 5449.86]  blazing fast
[5449.86 --> 5450.70]  mp3s
[5450.70 --> 5451.76]  your beats
[5451.76 --> 5452.96]  are awesome
[5452.96 --> 5453.80]  breakmaster
[5453.80 --> 5454.22]  cylinder
[5454.22 --> 5455.34]  that's it for
[5455.34 --> 5455.76]  this week
[5455.76 --> 5456.40]  see you all
[5456.40 --> 5456.82]  next week
[5456.82 --> 5457.98]  the next two
[5457.98 --> 5459.26]  episodes follow
[5459.26 --> 5459.80]  up on this
[5459.80 --> 5460.88]  one the next
[5460.88 --> 5461.54]  one is with
[5461.54 --> 5462.14]  someone that
[5462.14 --> 5462.50]  you've already
[5462.50 --> 5463.04]  had the pleasure
[5463.04 --> 5464.00]  of in episode
[5464.00 --> 5464.64]  31
[5464.64 --> 5466.30]  tamer saleh is
[5466.30 --> 5467.16]  a former vp
[5467.16 --> 5467.70]  of engineering
[5467.70 --> 5468.22]  at pivotal
[5468.22 --> 5469.36]  the company
[5469.36 --> 5470.18]  where concourse
[5470.18 --> 5471.26]  ci was born
[5471.26 --> 5472.52]  he shares
[5472.52 --> 5473.52]  the two thumbs
[5473.52 --> 5474.00]  up trick
[5474.00 --> 5475.08]  and we try out
[5475.08 --> 5475.80]  the cool wall
[5475.80 --> 5476.58]  of cloud native
[5476.58 --> 5477.90]  it's going to
[5477.90 --> 5478.36]  be fun
[5478.36 --> 5480.92]  the next most
[5480.92 --> 5481.10]  his
[5481.10 --> 5485.04]  и
[5485.04 --> 5485.90]  and
[5485.90 --> 5486.62]  and
[5486.62 --> 5487.42]  and
[5487.42 --> 5487.80]  and
[5487.80 --> 5490.84]  and
[5490.84 --> 5491.28]  and
